+++
type = "question"
title = "Get useless results querying aerodrome"
description = '''Hello, I have been trying to find airports using the two R-packages osmdata and osmar. In the example below I am searching for an airport in a place called wahnheide, knowing, that there is an airport Flughafen Köln/Bonn. First, I am creating a bounding box with the function center_bbox and then que...'''
date = "2021-02-01T18:26:00Z"
lastmod = "2021-02-01T18:26:00Z"
weight = 78629
keywords = [ "r", "aerodrome" ]
aliases = [ "/questions/78629" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Get useless results querying aerodrome](/questions/78629/get-useless-results-querying-aerodrome)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78629-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78629-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78629-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I have been trying to find airports using the two R-packages osmdata and osmar. In the example below I am searching for an airport in a place called wahnheide, knowing, that there is an airport Flughafen Köln/Bonn. First, I am creating a bounding box with the function center_bbox and then querying the tag aeroway:aerodrome.</p>
<pre><code>library(osmdata)
library(osmar)
&#10;wahnheide &lt;- c(7.107108659486173, 50.8700493119623)
central_point &lt;- wahnheide
bb &lt;- center_bbox(central_point[1], central_point[2], 5000, 5000)
&#10;# aerodrome
&#10;q &lt;- bb %&gt;% opq (timeout = 25*100) %&gt;% add_osm_feature(key = &quot;aeroway&quot;, value = &quot;aerodrome&quot;)
&#10;aerodrome &lt;- sapply(osmdata_sf(q)$osm_points, function(x) iconv(x, from = &quot;UTF-8&quot;, to = &quot;UTF-8&quot;))</code></pre>
<p>The result I get is a table with four columns: osm_id, barrier, source and geometry, like attached below.</p>
<p>What I expect is something usable, like the name of the place, address, etc. Is it possitble to get this information modifying the query? or using the osm_ids?</p>
<pre><code>aerodrome  &lt;- structure(c(&quot;53398845&quot;, &quot;53398860&quot;, &quot;53398865&quot;, &quot;53403325&quot;, &quot;53403328&quot;, 
               &quot;90727693&quot;, &quot;90727719&quot;, &quot;90727721&quot;, &quot;90727725&quot;, &quot;90727726&quot;, &quot;90727729&quot;, 
               &quot;90727733&quot;, &quot;90727745&quot;, &quot;90727747&quot;, &quot;90727749&quot;, &quot;90727754&quot;, &quot;90727758&quot;, 
               &quot;90727760&quot;, &quot;90727763&quot;, &quot;90727765&quot;, &quot;90727771&quot;, &quot;90727773&quot;, &quot;90727776&quot;, 
               &quot;90727780&quot;, &quot;303381016&quot;, &quot;303381017&quot;, &quot;303381018&quot;, &quot;303381020&quot;, 
               &quot;305577320&quot;, &quot;338493431&quot;, &quot;338493432&quot;, &quot;388619605&quot;, &quot;444984453&quot;, 
               &quot;503256114&quot;, &quot;503256131&quot;, &quot;693414125&quot;, &quot;975856241&quot;, &quot;982585071&quot;, 
               &quot;982585074&quot;, &quot;982585099&quot;, &quot;982585300&quot;, &quot;982585318&quot;, &quot;1256789186&quot;, 
               &quot;1256789190&quot;, &quot;1256789191&quot;, &quot;1256789198&quot;, &quot;1278005777&quot;, &quot;1278005778&quot;, 
               &quot;1278005779&quot;, &quot;1513076932&quot;, &quot;1513076933&quot;, &quot;1513076934&quot;, &quot;1513076935&quot;, 
               &quot;1513076936&quot;, &quot;1513076937&quot;, &quot;1513076938&quot;, &quot;1513076939&quot;, &quot;1513076943&quot;, 
               &quot;1513076947&quot;, &quot;1513076949&quot;, &quot;1513076952&quot;, &quot;1513076954&quot;, &quot;1513076955&quot;, 
               &quot;1513076961&quot;, &quot;1513076967&quot;, &quot;1513076969&quot;, &quot;1513076970&quot;, &quot;1513076971&quot;, 
               &quot;1513076980&quot;, &quot;1513076999&quot;, &quot;1513077000&quot;, &quot;1513077001&quot;, &quot;1513077003&quot;, 
               &quot;1513077008&quot;, &quot;1513077012&quot;, &quot;1513077013&quot;, &quot;1513077014&quot;, &quot;1513077038&quot;, 
               &quot;1513077054&quot;, &quot;1513077062&quot;, &quot;1513077073&quot;, &quot;1513077074&quot;, &quot;1513077075&quot;, 
               &quot;1513077076&quot;, &quot;1513077077&quot;, &quot;1513077080&quot;, &quot;1514349799&quot;, &quot;1603899023&quot;, 
               &quot;1603899025&quot;, &quot;1603899027&quot;, &quot;1611111803&quot;, &quot;1737314262&quot;, &quot;1737314270&quot;, 
               &quot;1737314271&quot;, &quot;1737314272&quot;, &quot;1737314273&quot;, &quot;1737314274&quot;, &quot;1737314275&quot;, 
               &quot;1737314282&quot;, &quot;1737314283&quot;, &quot;1737314284&quot;, &quot;1737314286&quot;, &quot;1737314288&quot;, 
               &quot;1737314290&quot;, &quot;1737314291&quot;, &quot;1737314294&quot;, &quot;1737314304&quot;, &quot;1737314306&quot;, 
               &quot;1737314308&quot;, &quot;1737314310&quot;, &quot;1737314311&quot;, &quot;1737314313&quot;, &quot;1737314315&quot;, 
               &quot;1737314319&quot;, &quot;1737314322&quot;, &quot;1737314325&quot;, &quot;1868389062&quot;, &quot;1868389090&quot;, 
               &quot;1868389092&quot;, &quot;1868389095&quot;, &quot;1868389098&quot;, &quot;1868389101&quot;, &quot;1868389105&quot;, 
               &quot;1868389106&quot;, &quot;1942418794&quot;, &quot;1991402715&quot;, &quot;1991402721&quot;, &quot;2149996723&quot;, 
               &quot;2149996730&quot;, &quot;2149996743&quot;, &quot;2149996746&quot;, &quot;2149996755&quot;, &quot;2149996770&quot;, 
               &quot;2149996787&quot;, &quot;2150455272&quot;, &quot;2150455329&quot;, &quot;2301210581&quot;, &quot;2355175960&quot;, 
               &quot;2399040138&quot;, &quot;2687584301&quot;, &quot;2687584303&quot;, &quot;3239092981&quot;, &quot;3263357122&quot;, 
               &quot;3263357127&quot;, &quot;3825207782&quot;, &quot;3825207783&quot;, &quot;4103701261&quot;, &quot;4103701262&quot;, 
               &quot;4103701263&quot;, &quot;4103701266&quot;, &quot;4103701267&quot;, &quot;4103701268&quot;, &quot;4103701269&quot;, 
               &quot;4103701270&quot;, &quot;4103701271&quot;, &quot;4103701272&quot;, &quot;4103701274&quot;, &quot;4103701275&quot;, 
               &quot;4103701276&quot;, &quot;4103701277&quot;, &quot;4103701278&quot;, &quot;4103701279&quot;, &quot;4103701280&quot;, 
               &quot;5046878828&quot;, &quot;5046878830&quot;, &quot;5200880764&quot;, &quot;7275520072&quot;, &quot;7275597689&quot;, 
               &quot;7275597690&quot;, &quot;7275597691&quot;, &quot;7275597743&quot;, &quot;7275597744&quot;, &quot;7275597745&quot;, 
               &quot;7275597746&quot;, &quot;7275597749&quot;, &quot;7275597751&quot;, &quot;7275597764&quot;, &quot;7275597765&quot;, 
               &quot;7275597766&quot;, &quot;7275597767&quot;, &quot;7275597768&quot;, &quot;7275597769&quot;, &quot;7275597770&quot;, 
               &quot;7275597771&quot;, &quot;7275597772&quot;, &quot;7275597773&quot;, &quot;7275597774&quot;, &quot;7275597775&quot;, 
               &quot;7275597776&quot;, &quot;7275597777&quot;, &quot;8200300056&quot;, NA, NA, NA, NA, NA, 
               NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, 
               NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, 
               NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, 
               NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, 
               NA, NA, NA, NA, NA, NA, NA, NA, NA, &quot;gate&quot;, NA, NA, NA, NA, &quot;gate&quot;, 
               NA, NA, NA, NA, NA, &quot;gate&quot;, NA, NA, NA, NA, NA, NA, NA, NA, NA, 
               NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, 
               NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, 
               NA, NA, NA, NA, NA, &quot;gate&quot;, NA, NA, NA, NA, NA, &quot;gate&quot;, NA, &quot;gate&quot;, 
               NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, 
               NA, NA, NA, NA, &quot;gate&quot;, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, 
               NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, 
               NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, 
               NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, 
               NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, 
               NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, 
               NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, &quot;seen&quot;, NA, 
               NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, 
               NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, 
               NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, 
               NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, 
               NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, 
               NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, 
               NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, NA, &quot;c(7.1596728, 50.8675326)&quot;, 
               &quot;c(7.1594811, 50.8732307)&quot;, &quot;c(7.1588775, 50.8736457)&quot;, &quot;c(7.1709033, 50.8563279)&quot;, 
               &quot;c(7.1684331, 50.8580434)&quot;, &quot;c(7.1215113, 50.8846538)&quot;, &quot;c(7.1577605, 50.8740119)&quot;, 
               &quot;c(7.1582833, 50.8738986)&quot;, &quot;c(7.1593787, 50.8670762)&quot;, &quot;c(7.1579936, 50.8652953)&quot;, 
               &quot;c(7.1579382, 50.8651661)&quot;, &quot;c(7.1637246, 50.8612768)&quot;, &quot;c(7.1744018, 50.8485948)&quot;, 
               &quot;c(7.1685356, 50.8495791)&quot;, &quot;c(7.1645922, 50.850256)&quot;, &quot;c(7.1583425, 50.853538)&quot;, 
               &quot;c(7.152706, 50.8562489)&quot;, &quot;c(7.1451792, 50.8546241)&quot;, &quot;c(7.1180104, 50.8579515)&quot;, 
               &quot;c(7.1184121, 50.8588979)&quot;, &quot;c(7.1178592, 50.8679345)&quot;, &quot;c(7.1173157, 50.8690389)&quot;, 
               &quot;c(7.1149798, 50.8721996)&quot;, &quot;c(7.1109705, 50.8730305)&quot;, &quot;c(7.1187524, 50.8606415)&quot;, 
               &quot;c(7.1190139, 50.8620776)&quot;, &quot;c(7.1185084, 50.8633001)&quot;, &quot;c(7.1168392, 50.8667116)&quot;, 
               &quot;c(7.1187245, 50.8578149)&quot;, &quot;c(7.1594448, 50.8672126)&quot;, &quot;c(7.1593147, 50.8662857)&quot;, 
               &quot;c(7.1192087, 50.8862498)&quot;, &quot;c(7.1274656, 50.8560652)&quot;, &quot;c(7.1200316, 50.8571792)&quot;, 
               &quot;c(7.1375415, 50.8539322)&quot;, &quot;c(7.1607277, 50.8684893)&quot;, &quot;c(7.1094338, 50.8756193)&quot;, 
               &quot;c(7.1318781, 50.8546793)&quot;, &quot;c(7.1334321, 50.854118)&quot;, &quot;c(7.122546, 50.856602)&quot;, 
               &quot;c(7.1161954, 50.8704297)&quot;, &quot;c(7.1189396, 50.8623565)&quot;, &quot;c(7.1788073, 50.8518339)&quot;, 
               &quot;c(7.1754817, 50.8498641)&quot;, &quot;c(7.1756599, 50.849335)&quot;, &quot;c(7.1744335, 50.8538987)&quot;, 
               &quot;c(7.1121063, 50.8835169)&quot;, &quot;c(7.1111398, 50.8835777)&quot;, &quot;c(7.1107519, 50.8835921)&quot;, 
               &quot;c(7.1611519, 50.8526031)&quot;, &quot;c(7.1595574, 50.8527078)&quot;, &quot;c(7.1750686, 50.8538773)&quot;, 
               &quot;c(7.1383822, 50.853999)&quot;, &quot;c(7.1390607, 50.8541726)&quot;, &quot;c(7.1400722, 50.854275)&quot;, 
               &quot;c(7.1416068, 50.8543694)&quot;, &quot;c(7.1444638, 50.8545775)&quot;, &quot;c(7.1582625, 50.854622)&quot;, 
               &quot;c(7.148056, 50.855367)&quot;, &quot;c(7.1291405, 50.8559914)&quot;, &quot;c(7.1490328, 50.8556219)&quot;, 
               &quot;c(7.1505143, 50.8557426)&quot;, &quot;c(7.1549338, 50.8569102)&quot;, &quot;c(7.1654299, 50.86011)&quot;, 
               &quot;c(7.1600634, 50.8637924)&quot;, &quot;c(7.159879, 50.8639859)&quot;, &quot;c(7.1592812, 50.8645083)&quot;, 
               &quot;c(7.1580069, 50.8650761)&quot;, &quot;c(7.1602408, 50.8680314)&quot;, &quot;c(7.1487208, 50.8725832)&quot;, 
               &quot;c(7.1462354, 50.8727484)&quot;, &quot;c(7.1514029, 50.8728809)&quot;, &quot;c(7.1530627, 50.8731089)&quot;, 
               &quot;c(7.155243, 50.8736174)&quot;, &quot;c(7.1570646, 50.8740068)&quot;, &quot;c(7.143621, 50.8744925)&quot;, 
               &quot;c(7.1435235, 50.8750864)&quot;, &quot;c(7.1413533, 50.876645)&quot;, &quot;c(7.1392444, 50.8781201)&quot;, 
               &quot;c(7.1357114, 50.880533)&quot;, &quot;c(7.130943, 50.8838309)&quot;, &quot;c(7.1294039, 50.8849008)&quot;, 
               &quot;c(7.1237363, 50.8850928)&quot;, &quot;c(7.1278527, 50.885909)&quot;, &quot;c(7.1222151, 50.886153)&quot;, 
               &quot;c(7.1207726, 50.8871502)&quot;, &quot;c(7.143246, 50.8753309)&quot;, &quot;c(7.1166652, 50.8670108)&quot;, 
               &quot;c(7.1165737, 50.8672025)&quot;, &quot;c(7.1166426, 50.8672302)&quot;, &quot;c(7.1145735, 50.87147)&quot;, 
               &quot;c(7.1312116, 50.8554401)&quot;, &quot;c(7.1308343, 50.8558053)&quot;, &quot;c(7.1254629, 50.8559264)&quot;, 
               &quot;c(7.1266752, 50.8559774)&quot;, &quot;c(7.1304234, 50.8559932)&quot;, &quot;c(7.1185501, 50.8594183)&quot;, 
               &quot;c(7.1189222, 50.859728)&quot;, &quot;c(7.1155802, 50.8708666)&quot;, &quot;c(7.1163261, 50.8713979)&quot;, 
               &quot;c(7.1095918, 50.8725286)&quot;, &quot;c(7.1102637, 50.8730573)&quot;, &quot;c(7.1090923, 50.8800228)&quot;, 
               &quot;c(7.1072915, 50.8802163)&quot;, &quot;c(7.1065359, 50.8803151)&quot;, &quot;c(7.1082283, 50.882398)&quot;, 
               &quot;c(7.1086125, 50.8827628)&quot;, &quot;c(7.1082363, 50.8829883)&quot;, &quot;c(7.1077811, 50.8831816)&quot;, 
               &quot;c(7.1076365, 50.8832918)&quot;, &quot;c(7.1052847, 50.8833852)&quot;, &quot;c(7.1075706, 50.8835207)&quot;, 
               &quot;c(7.1094057, 50.8836983)&quot;, &quot;c(7.1075655, 50.8839013)&quot;, &quot;c(7.1075276, 50.8840923)&quot;, 
               &quot;c(7.1073947, 50.8842792)&quot;, &quot;c(7.1092781, 50.8778496)&quot;, &quot;c(7.1093589, 50.8802181)&quot;, 
               &quot;c(7.1085314, 50.8802345)&quot;, &quot;c(7.1086788, 50.8802715)&quot;, &quot;c(7.1092265, 50.8803148)&quot;, 
               &quot;c(7.1090858, 50.8803856)&quot;, &quot;c(7.1088111, 50.8804417)&quot;, &quot;c(7.109075, 50.8804459)&quot;, 
               &quot;c(7.1177331, 50.8676678)&quot;, &quot;c(7.1100975, 50.8725404)&quot;, &quot;c(7.1107719, 50.8730983)&quot;, 
               &quot;c(7.1142993, 50.8715419)&quot;, &quot;c(7.115582, 50.8717896)&quot;, &quot;c(7.1119801, 50.871955)&quot;, 
               &quot;c(7.1124218, 50.8719669)&quot;, &quot;c(7.1118905, 50.8720537)&quot;, &quot;c(7.1118081, 50.8722463)&quot;, 
               &quot;c(7.111641, 50.8724831)&quot;, &quot;c(7.1149582, 50.8833278)&quot;, &quot;c(7.1201726, 50.8843959)&quot;, 
               &quot;c(7.1593171, 50.8663043)&quot;, &quot;c(7.118445, 50.859766)&quot;, &quot;c(7.1194211, 50.857447)&quot;, 
               &quot;c(7.1500275, 50.8727031)&quot;, &quot;c(7.1526174, 50.8730609)&quot;, &quot;c(7.1189395, 50.8613577)&quot;, 
               &quot;c(7.1593273, 50.8663837)&quot;, &quot;c(7.1593185, 50.8667754)&quot;, &quot;c(7.1436339, 50.8745573)&quot;, 
               &quot;c(7.1436404, 50.8745903)&quot;, &quot;c(7.1611741, 50.8689405)&quot;, &quot;c(7.1613083, 50.8690611)&quot;, 
               &quot;c(7.1614478, 50.869211)&quot;, &quot;c(7.1616027, 50.8694204)&quot;, &quot;c(7.1616643, 50.8695406)&quot;, 
               &quot;c(7.1617032, 50.8696618)&quot;, &quot;c(7.1617288, 50.8697871)&quot;, &quot;c(7.1617413, 50.8698967)&quot;, 
               &quot;c(7.1617464, 50.8699928)&quot;, &quot;c(7.1617196, 50.8701947)&quot;, &quot;c(7.1616774, 50.8703124)&quot;, 
               &quot;c(7.1616162, 50.8704459)&quot;, &quot;c(7.1614907, 50.8706298)&quot;, &quot;c(7.1613351, 50.8708402)&quot;, 
               &quot;c(7.1612432, 50.8709595)&quot;, &quot;c(7.16104, 50.8712324)&quot;, &quot;c(7.160784, 50.8715545)&quot;, 
               &quot;c(7.1476107, 50.8725826)&quot;, &quot;c(7.1467738, 50.8725822)&quot;, &quot;c(7.1601743, 50.872335)&quot;, 
               &quot;c(7.1485387, 50.8725831)&quot;, &quot;c(7.1527403, 50.8730706)&quot;, &quot;c(7.1521925, 50.8729995)&quot;, 
               &quot;c(7.1507954, 50.8727878)&quot;, &quot;c(7.1615326, 50.8693127)&quot;, &quot;c(7.1617406, 50.8700858)&quot;, 
               &quot;c(7.1524845, 50.8730428)&quot;, &quot;c(7.1529269, 50.8730885)&quot;, &quot;c(7.1542061, 50.8733772)&quot;, 
               &quot;c(7.1559625, 50.8737844)&quot;, &quot;c(7.1568231, 50.8739759)&quot;, &quot;c(7.1566424, 50.8739383)&quot;, 
               &quot;c(7.1572663, 50.8740187)&quot;, &quot;c(7.1574735, 50.8740215)&quot;, &quot;c(7.1579433, 50.8739838)&quot;, 
               &quot;c(7.1581309, 50.8739495)&quot;, &quot;c(7.1584374, 50.8738404)&quot;, &quot;c(7.1585793, 50.8737825)&quot;, 
               &quot;c(7.1590852, 50.8735495)&quot;, &quot;c(7.1594221, 50.8733138)&quot;, &quot;c(7.1593438, 50.8733907)&quot;, 
               &quot;c(7.159221, 50.8734731)&quot;, &quot;c(7.1596607, 50.873005)&quot;, &quot;c(7.1598357, 50.8727748)&quot;, 
               &quot;c(7.1185362, 50.8593659)&quot;), .Dim = c(191L, 4L), .Dimnames = list(
                   NULL, c(&quot;osm_id&quot;, &quot;barrier&quot;, &quot;source&quot;, &quot;geometry&quot;)))</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-r" rel="tag" title="see questions tagged &#39;r&#39;">r</span> <span class="post-tag tag-link-aerodrome" rel="tag" title="see questions tagged &#39;aerodrome&#39;">aerodrome</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Feb '21, 18:26</strong></p>
<img src="https://secure.gravatar.com/avatar/3a980c677d8f8b63d40c2471a838899b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="anzor_sardalov&#39;s gravatar image" />
<p><span>anzor_sardalov</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="anzor_sardalov has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78629" class="comments-container">
&#10;</div>
<div id="comment-tools-78629" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78629-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

