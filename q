[1mdiff --git a/Versie 1.0/SLD_Extern_Uitwisselberichten/Controle XSLT/SIKB_SLD WBB New Decision.xslt b/Versie 1.0/SLD_Extern_Uitwisselberichten/Controle XSLT/SIKB_SLD WBB New Decision.xslt[m
[1mindex aa78180..69fd182 100644[m
[1m--- a/Versie 1.0/SLD_Extern_Uitwisselberichten/Controle XSLT/SIKB_SLD WBB New Decision.xslt[m	
[1m+++ b/Versie 1.0/SLD_Extern_Uitwisselberichten/Controle XSLT/SIKB_SLD WBB New Decision.xslt[m	
[36m@@ -263,7 +263,7 @@[m
 				[m
 		<xsl:copy-of select="sikb:checkExistence(., $prGUID, 'decisionType', 'ERROR')"/>[m
 		<xsl:copy-of select="sikb:checkFilled(., $prGUID, 'decisionType', 'ERROR')" />[m
[31m-		<xsl:copy-of select="sikb:checkLookupId(., $prGUID, 'decisionType', 'Besluit', 'WARNING')"/>[m
[32m+[m		[32m<xsl:copy-of select="sikb:checkLookupId(., $prGUID, 'decisionType', 'Besluit', 'ERROR')"/> <!-- without a decision there is no new decision -->[m
 		[m
 		<xsl:copy-of select="sikb:checkExistence(., $prGUID,'startTime','ERROR')" />[m
 		<xsl:copy-of select="sikb:checkFilled(., $prGUID, 'startTime', 'ERROR')"/>[m
