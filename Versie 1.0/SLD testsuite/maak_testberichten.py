"""Maakt extra testberichten in versies/<versie>/testberichten/, afgeleid van de officiële SLD-voorbeeldberichten.

Sommige controles in de XSLT's worden door geen enkel voorbeeldbericht bereikt (bijv. een Project bij
New Decision, of een broId bij het Dossier van een Complete Report). Deze afgeleide berichten vullen dat
gat, zodat de automatische controles en de dekking ook die delen meenemen. Elk testbericht moet zelf
'goed' zijn (0 ERRORs); dat controleert run_tests.py.

Gebruik: python maak_testberichten.py                  alle versies (overschrijft versies/<versie>/testberichten/)
         python maak_testberichten.py "SLD_Extern_Uitwisselberichten v15.0"   alleen deze versie
"""
import copy
import json
import sys
from pathlib import Path

from lxml import etree

SUITE_DIR = Path(__file__).resolve().parent
FOLDERS = json.loads((SUITE_DIR / "suite.json").read_text(encoding="utf-8"))["mappen"]
# Gezet per versie door main()
EXAMPLES_DIR = OUT_DIR = None

IMSIKB = "http://www.sikb.nl/imsikb0101"
IMMETINGEN = "http://www.sikb.nl/immetingen"
GML = "http://www.opengis.net/gml/3.2"
XLINK = "http://www.w3.org/1999/xlink"
NS = {"imsikb0101": IMSIKB, "immetingen": IMMETINGEN, "gml": GML, "xlink": XLINK}


def load(name):
    return etree.parse(str(EXAMPLES_DIR / name))


def first(tree, xpath):
    return tree.xpath(xpath, namespaces=NS)[0]


def element(local, text, ns=IMSIKB):
    el = etree.Element(f"{{{ns}}}{local}")
    el.text = text
    return el


def save(tree, name, description):
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    root = tree.getroot()
    root.insert(0, etree.Comment(f" TESTBERICHT (gegenereerd door maak_testberichten.py): {description} "))
    tree.write(str(OUT_DIR / name), encoding="UTF-8", xml_declaration=True)
    print(f"  {name}")


def make_all():
    for old in OUT_DIR.glob("*.xml"):
        old.unlink()
    print(f"Testberichten in {OUT_DIR}:")

    # T1: New Decision met een Project (type 11) bij de Remediation, en endTime bij Remediation en
    # ContaminationInformation. Het Project komt uit het WBB Complete Report-voorbeeld.
    tree = load("03c_registrationRequest_SLD_NewDecision_IMBROA_WBB_2.xml")
    source = load("02_registrationRequest_SLD_CompleteReport_IMBROA_WBB.xml")
    project_member = copy.deepcopy(first(source, "//imsikb0101:featureMember[imsikb0101:Project/imsikb0101:projectType"
                                                 "[contains(., 'id:11')]]"))
    project_id = project_member[0].get(f"{{{GML}}}id")
    first(tree, "//imsikb0101:featureMember[imsikb0101:Remediation]").addprevious(project_member)
    remediation = first(tree, "//imsikb0101:Remediation")
    first(remediation, "imsikb0101:project").set(f"{{{XLINK}}}href", f"#{project_id}")
    for obj in (remediation, first(tree, "//imsikb0101:ContaminationInformation")):
        if not obj.xpath("imsikb0101:endTime", namespaces=NS):
            obj.append(element("endTime", "2004-12-13"))
    save(tree, "T1. New Decision met Project en endTime (van 03c_2).xml",
         "03c_2 + Project (projectType 11, uit 02) gekoppeld aan de Remediation; endTime bij Remediation en "
         "ContaminationInformation")

    # T2: Change SoilLocation met een naam bij de SoilLocation
    tree = load("03b_registrationRequest_SLD_ChangeSoilLocation_IMBROA_WBB.xml")
    soil_location = first(tree, "//imsikb0101:SoilLocation")
    if not soil_location.xpath("imsikb0101:name", namespaces=NS):
        soil_location.append(element("name", "Axelsestraat 163-165"))
    save(tree, "T2. Change SoilLocation met naam (van 03b).xml", "03b + naam bij de SoilLocation")

    # T3: WBB Complete Report met een broId bij het Dossier
    tree = load("02_registrationRequest_SLD_CompleteReport_IMBROA_WBB.xml")
    dossier = first(tree, "//imsikb0101:Dossier")
    if not dossier.xpath("imsikb0101:broId", namespaces=NS):
        dossier.append(element("broId", "SLD000000012349"))
    save(tree, "T3. WBB Complete Report met Dossier-broId (van 02).xml", "02_registration + broId bij het Dossier")


def main():
    global EXAMPLES_DIR, OUT_DIR
    names = sys.argv[1:]
    versions = [SUITE_DIR.parent / n for n in names] if names else sorted(
        d for d in SUITE_DIR.parent.iterdir()
        if (d / FOLDERS["xslt"]).is_dir() and (SUITE_DIR / "versies" / d.name).is_dir())
    for version in versions:
        EXAMPLES_DIR = version / FOLDERS["inname"]
        OUT_DIR = SUITE_DIR / "versies" / version.name / "testberichten"
        make_all()


if __name__ == "__main__":
    main()
