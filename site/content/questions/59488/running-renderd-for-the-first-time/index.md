+++
type = "question"
title = "Running renderd for the first time"
description = '''Hello, i have followed the instructions from https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/ to manually build my own tile server. I followed the instruction &amp;gt;&amp;gt; renderd -f -c /usr/local/etc/renderd.conf &amp;lt;&amp;lt; to get a map via the web browser, but it doesnt work.  rendera...'''
date = "2017-09-08T12:53:00Z"
lastmod = "2017-09-11T07:12:00Z"
weight = 59488
keywords = [ "renderd", "tileserver" ]
aliases = [ "/questions/59488" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Running renderd for the first time](/questions/59488/running-renderd-for-the-first-time)

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
<span id="post-59488-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59488-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59488-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>i have followed the instructions from <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a> to manually build my own tile server.</p>
<p>I followed the instruction &gt;&gt; renderd -f -c /usr/local/etc/renderd.conf &lt;&lt; to get a map via the web browser, but it doesnt work.</p>
<pre><code>renderaccount@lantech-MOBILE-1524:~/src/openstreetmap-carto$ renderd -f -c /usr/local/etc/renderd.conf
renderd[21650]: Rendering daemon started
renderd[21650]: Initiating request_queue
renderd[21650]: Parsing section renderd
renderd[21650]: Parsing render section 0
renderd[21650]: Parsing section mapnik
renderd[21650]: Parsing section ajt
renderd[21650]: config renderd: unix socketname=/var/run/renderd/renderd.sock
renderd[21650]: config renderd: num_threads=4
renderd[21650]: config renderd: num_slaves=0
renderd[21650]: config renderd: tile_dir=/var/lib/mod_tile
renderd[21650]: config renderd: stats_file=/var/run/renderd/renderd.stats
renderd[21650]: config mapnik:  plugins_dir=/usr/lib/mapnik/3.0/input
renderd[21650]: config mapnik:  font_dir=/usr/share/fonts/truetype
renderd[21650]: config mapnik:  font_dir_recurse=1
renderd[21650]: config renderd(0): Active
renderd[21650]: config renderd(0): unix socketname=/var/run/renderd/renderd.sock
renderd[21650]: config renderd(0): num_threads=4
renderd[21650]: config renderd(0): tile_dir=/var/lib/mod_tile
renderd[21650]: config renderd(0): stats_file=/var/run/renderd/renderd.stats
renderd[21650]: config map 0:   name(ajt) file(/home/renderaccount/src/openstreetmap-carto/mapnik.xml) uri(/hot/) htcp() host(localhost)
renderd[21650]: Initialising unix server socket on /var/run/renderd/renderd.sock
renderd[21650]: Created server socket 5
renderd[21650]: Renderd is using mapnik version 3.0.9
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/padauk/Padauk-bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/padauk/Padauk-bookbold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/padauk/Padauk.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/padauk/Padauk-book.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Umpush-Light.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Norasi.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Purisa.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Loma-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Waree-Oblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Umpush.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Kinnari-Oblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Sawasdee-Oblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Kinnari-BoldOblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgMono.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Loma-BoldOblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Laksaman.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Kinnari-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgTypewriter-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Laksaman-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Norasi-Italic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Sawasdee-BoldOblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Waree-BoldOblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgTypo-Oblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Loma-Oblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgMono-Oblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Norasi-Oblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgTypist-BoldOblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Garuda-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgTypo.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgTypewriter-BoldOblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Garuda.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Umpush-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Sawasdee.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Kinnari.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgTypist-Oblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgTypewriter.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Umpush-Oblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Umpush-BoldOblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Purisa-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Garuda-BoldOblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Kinnari-Italic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Umpush-LightOblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Purisa-BoldOblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Purisa-Oblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgTypo-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Laksaman-Italic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Norasi-BoldOblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Laksaman-BoldItalic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Kinnari-BoldItalic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgMono-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Norasi-BoldItalic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgTypo-BoldOblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Garuda-Oblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Waree-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Loma.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgTypewriter-Oblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgTypist.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgTypist-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Sawasdee-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgMono-BoldOblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Waree.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Norasi-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/openoffice/opens___.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansThaiUI-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKannada-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSaurashtra-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLaoUI-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansInscriptionalParthian-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSyriacEstrangela-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOldTurkic-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansArmenian-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDevanagari-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifThai-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansShavian-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBengali-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOldPersian-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansHebrew-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansEthiopic-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTibetan-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoNastaliqUrdu-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansUI-Italic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDevanagariUI-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifLao-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGujarati-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGothic-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKharoshthi-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansUI-BoldItalic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDevanagariUI-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKannadaUI-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansArmenian-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansNewTaiLue-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCarian-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifTelugu-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDeseret-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDevanagari-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSans-BoldItalic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifLao-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMalayalamUI-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansHebrew-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOsmanya-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGujaratiUI-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMyanmar-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBuhid-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTibetan-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKhmerUI-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSyriacWestern-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoKufiArabic-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCypriot-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCherokee-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGeorgian-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGujaratiUI-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansAvestan-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSylotiNagri-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifArmenian-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOriyaUI-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansThaana-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGujarati-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLaoUI-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMyanmarUI-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLinearB-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifGeorgian-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerif-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKaithi-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKannada-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansHanunoo-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTifinagh-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifBengali-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCanadianAboriginal-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTelugu-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMeeteiMayek-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoNaskhArabicUI-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBamum-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLao-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKhmer-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansYi-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifArmenian-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansUI-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKhmer-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBatak-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansThaiUI-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBengaliUI-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBengaliUI-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSinhala-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBrahmi-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKayahLi-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTaiViet-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOriya-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKannadaUI-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLisu-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBengali-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMandaic-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSans-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMalayalam-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansRunic-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerif-BoldItalic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTamil-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOlChiki-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGurmukhiUI-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansThaana-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTagbanwa-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTamilUI-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCuneiform-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMalayalam-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTagalog-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansImperialAramaic-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansPhagsPa-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLao-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSamaritan-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansUI-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansJavanese-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerif-Italic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansVai-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSundanese-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBuginese-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOldItalic-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSans-Italic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTaiLe-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifGujarati-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoNaskhArabic-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLimbu-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTamilUI-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCham-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLepcha-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMyanmarUI-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLycian-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSymbols-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBalinese-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifTamil-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansThai-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMalayalamUI-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansPhoenician-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTelugu-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoNaskhArabicUI-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansEthiopic-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKhmerUI-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLydian-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCoptic-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansEgyptianHieroglyphs-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansThai-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCham-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoKufiArabic-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOriyaUI-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansInscriptionalPahlavi-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGeorgian-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTaiTham-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGlagolitic-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansRejang-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifThai-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansNKo-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOldSouthArabian-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTeluguUI-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOgham-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansUgaritic-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTeluguUI-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSyriacEastern-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGurmukhiUI-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSans-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifKannada-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTamil-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifKhmer-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifGeorgian-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/unifont/unifont.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/unifont/unifont_csur.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/unifont/unifont_upper_csur.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/unifont/unifont_sample.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/unifont/unifont_upper.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/sinhala/lklug.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-guru-extra/Saab.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/tibetan-machine/TibetanMachineUni.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-khmeros-core/KhmerOS.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-khmeros-core/KhmerOSsys.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/nanum/NanumMyeongjo.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/nanum/NanumGothicBold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/nanum/NanumBarunGothicBold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/nanum/NanumGothic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/nanum/NanumMyeongjoBold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/lao/Phetsarath_OT.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst-one/KacstOne-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst-one/KacstOne.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed-BoldItalic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-Oblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-ExtraLight.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans-BoldOblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif-Italic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-Oblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-Oblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-BoldOblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed-BoldOblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed-Italic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSansMono-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerifCondensed.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-dejavu/DejaVuSerif-BoldItalic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-japanese-gothic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/lohit-punjabi/Lohit-Punjabi.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/freefont/FreeSerifItalic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/freefont/FreeMonoOblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/freefont/FreeMono.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/freefont/FreeSansBold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/freefont/FreeMonoBold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/freefont/FreeMonoBoldOblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/freefont/FreeSerifBoldItalic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/freefont/FreeSansBoldOblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/freefont/FreeSerifBold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/freefont/FreeSansOblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/freefont/FreeSans.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/freefont/FreeSerif.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ancient-scripts/Symbola_hint.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationSansNarrow-Italic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationSansNarrow-BoldItalic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationSansNarrow-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationMono-BoldItalic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationSans-BoldItalic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationSansNarrow-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationMono-Italic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansCondensed.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed-BoldItalic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSans-ExtraLight.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSans-BoldOblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansMono-Oblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Oblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansMono-BoldOblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-BoldOblique.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed-Italic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed-Bold.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerif-BoldItalic.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/abyssinica/AbyssinicaSIL-R.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-M.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-BI.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-LI.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-MI.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-B.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-RI.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ubuntu-font-family/UbuntuMono-RI.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ubuntu-font-family/UbuntuMono-B.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-L.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ubuntu-font-family/UbuntuMono-R.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ubuntu-font-family/UbuntuMono-BI.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-C.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-R.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/KacstOffice.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/KacstBook.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/KacstLetter.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/KacstArt.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/KacstPen.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/KacstDigital.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/KacstDecorative.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/KacstPoster.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/KacstNaskh.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/KacstTitleL.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/mry_KacstQurn.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/KacstTitle.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/KacstQurn.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/KacstFarsi.ttf
renderd[21650]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/KacstScreen.ttf
Running in foreground mode...
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[21650]: Loading parameterization function for 
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[21650]: Loading parameterization function for 
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[21650]: Starting stats thread
renderd[21650]: Loading parameterization function for 
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[21650]: Loading parameterization function for 
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;Noto Sans CJK JP Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;Noto Sans CJK JP Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02:renderd[21650]: An error occurred while loading the map layer &#39;ajt&#39;: Shape Plugin: shapefile &#39;/home/renderaccount/src/openstreetmap-carto/data/simplified-land-polygons-complete-3857/simplified_land_polygons.shp&#39; does not exist  encountered during parsing of layer &#39;world&#39; in Layer at line 268 of &#39;/home/renderaccount/src/openstreetmap-carto/mapnik.xml&#39;
 warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;Noto Sans CJK JP Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;Noto Sans CJK JP Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02:renderd[21650]: An error occurred while loading the map layer &#39;ajt&#39;: Shape Plugin: shapefile &#39;/home/renderaccount/src/openstreetmap-carto/data/simplified-land-polygons-complete-3857/simplified_land_polygons.shp&#39; does not exist  encountered during parsing of layer &#39;world&#39; in Layer at line 268 of &#39;/home/renderaccount/src/openstreetmap-carto/mapnik.xml&#39;
 warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2017-09-08 13:36:02: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-2&#39;
renderd[21650]: An error occurred while loading the map layer &#39;ajt&#39;: Shape Plugin: shapefile &#39;/home/renderaccount/src/openstreetmap-carto/data/simplified-land-polygons-complete-3857/simplified_land_polygons.shp&#39; does not exist  encountered during parsing of layer &#39;world&#39; in Layer at line 268 of &#39;/home/renderaccount/src/openstreetmap-carto/mapnik.xml&#39;
renderd[21650]: An error occurred while loading the map layer &#39;ajt&#39;: Shape Plugin: shapefile &#39;/home/renderaccount/src/openstreetmap-carto/data/simplified-land-polygons-complete-3857/simplified_land_polygons.shp&#39; does not exist  encountered during parsing of layer &#39;world&#39; in Layer at line 268 of &#39;/home/renderaccount/src/openstreetmap-carto/mapnik.xml&#39;
renderd[21650]: DEBUG: Got incoming connection, fd 8, number 1
renderd[21650]: DEBUG: Got incoming request with protocol version 2
renderd[21650]: DEBUG: Got command RenderPrio fd(8) xml(ajt), z(0), x(0), y(0), mime(image/png), options()
renderd[21650]: Received request for map layer &#39;ajt&#39; which failed to load
renderd[21650]: DEBUG: Sending render cmd(4 ajt 0/0/0) with protocol version 2 to fd 8
renderd[21650]: DEBUG: Connection 0, fd 8 closed, now 0 left</code></pre>
<p>Could anybody help me to resolve the problem ?</p>
<p>Regards Boki</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Sep '17, 12:53</strong></p>
<img src="https://secure.gravatar.com/avatar/af6aa01f49eba45057355124d57dc823?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Boki_Z&#39;s gravatar image" />
<p><span>Boki_Z</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Boki_Z has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-59488" class="comments-container">
<span id="59493"></span>
<div id="comment-59493" class="comment">
<div id="post-59493-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Have you checked to see if the file '/home/renderaccount/src/openstreetmap-carto/data/simplified-land-polygons-complete-3857/simplified_land_polygons.shp' exists? The error says it doesn't, so that seems like the obvious place to start troubleshooting.</p>
</div>
<div id="comment-59493-info" class="comment-info">
<span class="comment-age">(08 Sep '17, 17:18)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="59494"></span>
<div id="comment-59494" class="comment">
<div id="post-59494-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For info, as of about a week ago, the scripts that unpack the lowzoom shapefiles still worked for me when I set up a tile server this way.</p>
<p>Perhaps you forgot to do the "Shapefile download" bit (and perhaps fonts too)?</p>
</div>
<div id="comment-59494-info" class="comment-info">
<span class="comment-age">(08 Sep '17, 17:33)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="59523"></span>
<div id="comment-59523" class="comment">
<div id="post-59523-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Oh yes my mistake. I have created the folder /data in /renderaccount. Now i get the tile on localhost/hot/0/0/0.png.</p>
<p>Thank you :).</p>
</div>
<div id="comment-59523-info" class="comment-info">
<span class="comment-age">(11 Sep '17, 07:12)</span> <span class="comment-user userinfo">Boki_Z</span>
</div>
</div>
</div>
<div id="comment-tools-59488" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59488-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

