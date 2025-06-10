+++
type = "question"
title = "Tiles do not render for low zoom levels"
description = '''I tried to build a tile server (see https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/) Unfortunately, tiles with a low zoom level are not rendering. The DONE TILE is missing. What can be the reason for that??? These don&#x27;t work: http://xyz/hot/0/0/0.png http://xyz/hot/1/0/0.png http...'''
date = "2017-12-10T04:23:00Z"
lastmod = "2017-12-28T03:33:00Z"
weight = 61120
keywords = [ "zoomlevel", "rendering", "tiles", "renderd", "problem" ]
aliases = [ "/questions/61120" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Tiles do not render for low zoom levels](/questions/61120/tiles-do-not-render-for-low-zoom-levels)

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
<span id="post-61120-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61120-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61120-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I tried to build a tile server (see <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/)">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/)</a></p>
<p>Unfortunately, tiles with a low zoom level are not rendering. The <code>DONE TILE</code> is missing. What can be the reason for that???</p>
<p>These don't work:</p>
<pre><code>http://xyz/hot/0/0/0.png
http://xyz/hot/1/0/0.png
http://xyz/hot/2/0/0.png
http://xyz/hot/3/0/0.png
http://xyz/hot/4/0/0.png</code></pre>
<p>It works from zoom level 5:</p>
<pre><code>http://xyz/hot/5/0/0.png
http://xyz/hot/6/0/0.png</code></pre>
<p>etc...</p>
<p>Here is the output of <code>renderd -f -c /usr/local/etc/renderd.conf</code></p>
<pre><code>renderd[18356]: Rendering daemon started
renderd[18356]: Initiating request_queue
renderd[18356]: Parsing section renderd
renderd[18356]: Parsing render section 0
renderd[18356]: Parsing section mapnik
renderd[18356]: Parsing section ajt
renderd[18356]: config renderd: unix socketname=/var/run/renderd/renderd.sock
renderd[18356]: config renderd: num_threads=8
renderd[18356]: config renderd: num_slaves=0
renderd[18356]: config renderd: tile_dir=/var/lib/mod_tile
renderd[18356]: config renderd: stats_file=/var/run/renderd/renderd.stats
renderd[18356]: config mapnik:  plugins_dir=/usr/lib/mapnik/3.0/input
renderd[18356]: config mapnik:  font_dir=/usr/share/fonts/truetype
renderd[18356]: config mapnik:  font_dir_recurse=1
renderd[18356]: config renderd(0): Active
renderd[18356]: config renderd(0): unix socketname=/var/run/renderd/renderd.sock
renderd[18356]: config renderd(0): num_threads=8
renderd[18356]: config renderd(0): tile_dir=/var/lib/mod_tile
renderd[18356]: config renderd(0): stats_file=/var/run/renderd/renderd.stats
renderd[18356]: config map 0:   name(ajt) file(/home/osm/src/openstreetmap-carto/mapnik.xml) uri(/hot/) htcp() host(localhost)
renderd[18356]: Initialising unix server socket on /var/run/renderd/renderd.sock
renderd[18356]: Created server socket 5
renderd[18356]: Renderd is using mapnik version 3.0.9
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Oblique.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed-Italic.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansMono-Oblique.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSans-BoldOblique.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansMono-BoldOblique.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansCondensed.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerif-BoldItalic.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-BoldOblique.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed-BoldItalic.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSans-ExtraLight.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansThaana-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansHebrew-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKhmer-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansRunic-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansThai-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTamilUI-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMyanmarUI-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTamilUI-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGujarati-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoNastaliqUrdu-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansUI-Italic.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGeorgian-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLaoUI-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTeluguUI-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKannada-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifArmenian-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLao-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBatak-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansUI-BoldItalic.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBengaliUI-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKhmerUI-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansUgaritic-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifLao-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKhmer-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTelugu-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMyanmar-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansThaana-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifBengali-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBengaliUI-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansImperialAramaic-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGothic-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMyanmarUI-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOldPersian-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansYi-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansUI-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGlagolitic-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMalayalam-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLinearB-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOlChiki-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOsmanya-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansEgyptianHieroglyphs-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLaoUI-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKhmerUI-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKannadaUI-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBuginese-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTeluguUI-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLimbu-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifTelugu-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansAvestan-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoKufiArabic-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDevanagariUI-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOriyaUI-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTaiViet-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOldItalic-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMandaic-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansHebrew-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifKhmer-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerif-BoldItalic.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGurmukhiUI-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGeorgian-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTifinagh-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDevanagari-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSundanese-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifGeorgian-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDevanagariUI-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLydian-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansPhoenician-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBalinese-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKaithi-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansVai-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSans-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGujaratiUI-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerif-Italic.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLycian-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansShavian-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTaiTham-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOriya-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDeseret-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansPhagsPa-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCham-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansNKo-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTaiLe-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCarian-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoNaskhArabic-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSymbols-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansEthiopic-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansThaiUI-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansArmenian-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansHanunoo-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCypriot-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSyriacEastern-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMeeteiMayek-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLisu-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifTamil-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBrahmi-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoKufiArabic-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansRejang-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMalayalamUI-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifGujarati-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKannada-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBuhid-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansInscriptionalParthian-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTibetan-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerif-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTibetan-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSaurashtra-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGujaratiUI-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBengali-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansArmenian-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTelugu-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansThaiUI-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSans-Italic.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCham-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansEthiopic-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKayahLi-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTamil-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTagalog-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOgham-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifThai-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCoptic-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSylotiNagri-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMalayalam-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLepcha-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansThai-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSinhala-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCherokee-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifThai-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBamum-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOldTurkic-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansInscriptionalPahlavi-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansJavanese-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKharoshthi-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTamil-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSans-BoldItalic.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifArmenian-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoNaskhArabicUI-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMalayalamUI-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSyriacEstrangela-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOldSouthArabian-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifKannada-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLao-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGujarati-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGurmukhiUI-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBengali-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCanadianAboriginal-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoNaskhArabicUI-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSans-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCuneiform-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifLao-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOriyaUI-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKannadaUI-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTagbanwa-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDevanagari-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSamaritan-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansUI-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansNewTaiLue-Regular.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifGeorgian-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/unifont/unifont_upper_csur.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/unifont/unifont_upper.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/unifont/unifont_sample.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/unifont/unifont_csur.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/unifont/unifont.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif-Italic.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-Oblique.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed-Italic.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-Oblique.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-BoldOblique.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-BoldOblique.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Oblique.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif-BoldItalic.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-BoldOblique.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed-BoldItalic.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed-Bold.ttf
renderd[18356]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-ExtraLight.ttf
Running in foreground mode...
renderd[18356]: Starting stats thread
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[18356]: Loading parameterization function for
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[18356]: Loading parameterization function for
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[18356]: Loading parameterization function for
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[18356]: Loading parameterization function for
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[18356]: Loading parameterization function for
renderd[18356]: Loading parameterization function for
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[18356]: Loading parameterization function for
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[18356]: Loading parameterization function for
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Sans Arabic UI Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-12-10 05:13:06: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-2&#39;
renderd[18356]: DEBUG: Got incoming connection, fd 13, number 1
renderd[18356]: DEBUG: Got incoming request with protocol version 2
renderd[18356]: DEBUG: Got command RenderPrio fd(13) xml(ajt), z(0), x(0), y(0), mime(image/png), options()
renderd[18356]: Using web mercator projection settings
renderd[18356]: DEBUG: START TILE ajt 0 0-0 0-0, new metatile
renderd[18356]: Rendering projected coordinates 0 0 0 -&gt; -20037508.342800|-20037508.342800 20037508.342800|20037508.342800 to a 1 x 1 tile
renderd[18356]: Using web mercator projection settings
renderd[18356]: Using web mercator projection settings
renderd[18356]: Using web mercator projection settings
renderd[18356]: Using web mercator projection settings
renderd[18356]: Using web mercator projection settings
renderd[18356]: Using web mercator projection settings
renderd[18356]: Using web mercator projection settings
renderd[18356]: DEBUG: Connection 0, fd 13 closed, now 0 left</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-problem" rel="tag" title="see questions tagged &#39;problem&#39;">problem</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Dec '17, 04:23</strong></p>
<img src="https://secure.gravatar.com/avatar/199bb0e1e35e833c4cc9f8e5a2da4f43?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LudBi&#39;s gravatar image" />
<p><span>LudBi</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LudBi has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Dec '17, 21:05</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-61120" class="comments-container">
<span id="61123"></span>
<div id="comment-61123" class="comment">
<div id="post-61123-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For info what you should see is something like:</p>
<pre><code>Dec 10 11:30:31 Ubuntuvm49 renderd[6920]: DEBUG: Got incoming connection, fd 8, number 1
Dec 10 11:30:31 Ubuntuvm49 renderd[6920]: DEBUG: Got incoming request with protocol version 2
Dec 10 11:30:31 Ubuntuvm49 renderd[6920]: DEBUG: Got command RenderPrio fd(8) xml(ajt), z(0), x(0), y(0), mime(image/png), options()
Dec 10 11:30:31 Ubuntuvm49 renderd[6920]: DEBUG: START TILE ajt 0 0-0 0-0, new metatile
Dec 10 11:30:31 Ubuntuvm49 renderd[6920]: Rendering projected coordinates 0 0 0 -&gt; -20037508.342800|-20037508.342800 20037508.342800|20037508.342800 to a 1 x 1 tile
Dec 10 11:30:32 Ubuntuvm49 renderd[6920]: DEBUG: DONE TILE ajt 0 0-0 0-0 in 0.908 seconds
Dec 10 11:30:32 Ubuntuvm49 renderd[6920]: DEBUG: Sending render cmd(3 ajt 0/0/0) with protocol version 2 to fd 8
Dec 10 11:30:32 Ubuntuvm49 renderd[6920]: DEBUG: Connection 0, fd 8 closed, now 0 left</code></pre>
<p>Not sure why you're not getting that. I can only suggest (a) installing the missing fonts and trying again and (b) rechecking the particular contents of lower zoom levels (maybe some shape files aren't accessible)?</p>
</div>
<div id="comment-61123-info" class="comment-info">
<span class="comment-age">(10 Dec '17, 11:37)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="61276"></span>
<div id="comment-61276" class="comment">
<div id="post-61276-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your suggestions. I've installed the OSM server again as described in <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a> Unfortunately, it's not working. Had the same problem again. Does anyone has any suggestions? I don't get any helpful error messages.</p>
</div>
<div id="comment-61276-info" class="comment-info">
<span class="comment-age">(19 Dec '17, 06:33)</span> <span class="comment-user userinfo">LudBi</span>
</div>
</div>
</div>
<div id="comment-tools-61120" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61120-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="61315"></span>

<div id="answer-container-61315" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61315-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61315-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-61315-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>How long are you waiting for completion?</p>
<p>Low zoom tiles can take a significant amount of time to render (particularly if you are doing this on the full planet) and you should not dynamically (aka on-demand) render them. Use render-list to pre-render, see the text at the end of <a href="https://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">https://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Dec '17, 19:21</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-61315" class="comments-container">
<span id="61316"></span>
<div id="comment-61316" class="comment">
<div id="post-61316-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's a possibility, but the reason why I suspect it's not "low zooms take a long time" is that z0 is normally pretty quick. Here's a quick test:</p>
<pre><code>Dec 21 20:50:40 ubuntuvm40 renderd[1606]: DEBUG: START TILE ajt 0 0-0 0-0, age 60.41 days
Dec 21 20:51:38 ubuntuvm40 renderd[1606]: DEBUG: DONE TILE ajt 0 0-0 0-0 in 57.526 seconds</code></pre>
<p>that's on a VM on a cheap desktop PC that's actually very busy with a minutely update.</p>
</div>
<div id="comment-61316-info" class="comment-info">
<span class="comment-age">(21 Dec '17, 20:53)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="61318"></span>
<div id="comment-61318" class="comment">
<div id="post-61318-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah put is that the HOT style? osm-carto uses a reduced data set at low zooms, iirc (HOT layer currently seems to be broken) the hOT style has a lot more going on at low zooms.</p>
</div>
<div id="comment-61318-info" class="comment-info">
<span class="comment-age">(21 Dec '17, 21:02)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="61319"></span>
<div id="comment-61319" class="comment">
<div id="post-61319-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's actually <a href="https://github.com/SomeoneElseOSM/openstreetmap-carto-AJT">https://github.com/SomeoneElseOSM/openstreetmap-carto-AJT</a> , which makes use of shapefiles of non-OSM data at low zooms (OSM Carto uses shapefiles of OSM data now as I understand it). OSM Carto takes 3 times as long to process by "carto" as my style, but doesn't seem to take longer to render - at least zooms from 8 or so up (can't say I've tested &lt;8 for a while, but don't remember a specific problem).</p>
</div>
<div id="comment-61319-info" class="comment-info">
<span class="comment-age">(21 Dec '17, 21:07)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-61315" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61315-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="61390"></span>

<div id="answer-container-61390" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61390-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61390-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61390-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you for the comments. I've used render-list to pre-render tiles at low zoom levels and it's working now.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Dec '17, 03:33</strong></p>
<img src="https://secure.gravatar.com/avatar/199bb0e1e35e833c4cc9f8e5a2da4f43?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LudBi&#39;s gravatar image" />
<p><span>LudBi</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LudBi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61390" class="comments-container">
&#10;</div>
<div id="comment-tools-61390" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61390-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

