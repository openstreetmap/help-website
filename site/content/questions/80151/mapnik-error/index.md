+++
type = "question"
title = "mapnik error"
description = '''I install tileserver according to this instruction https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/ But at the stage &quot;Running renderd for the first time&quot; I get errors and do not see the tiles renderaccount@tileserver:~/src/openstreetmap-carto$ renderd -f -c /usr/local/...'''
date = "2021-05-13T08:05:00Z"
lastmod = "2021-09-23T10:10:00Z"
weight = 80151
keywords = [ "mapnik" ]
aliases = [ "/questions/80151" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [mapnik error](/questions/80151/mapnik-error)

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
<span id="post-80151-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80151-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80151-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I install tileserver according to this instruction <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/</a></p>
<p>But at the stage "Running renderd for the first time" I get errors and do not see the tiles</p>
<pre><code>renderaccount@tileserver:~/src/openstreetmap-carto$ renderd -f -c /usr/local/etc/renderd.conf
renderd[94587]: Rendering daemon started
renderd[94587]: Initiating request_queue
renderd[94587]: Parsing section renderd
renderd[94587]: Parsing render section 0
renderd[94587]: Parsing section mapnik
renderd[94587]: Parsing section ajt
renderd[94587]: config renderd: unix socketname=/var/run/renderd/renderd.sock
renderd[94587]: config renderd: num_threads=4
renderd[94587]: config renderd: num_slaves=0
renderd[94587]: config renderd: tile_dir=/var/lib/mod_tile
renderd[94587]: config renderd: stats_file=/var/run/renderd/renderd.stats
renderd[94587]: config mapnik:  plugins_dir=/usr/lib/mapnik/3.0/input
renderd[94587]: config mapnik:  font_dir=/usr/share/fonts/truetype
renderd[94587]: config mapnik:  font_dir_recurse=1
renderd[94587]: config renderd(0): Active
renderd[94587]: config renderd(0): unix socketname=/var/run/renderd/renderd.sock
renderd[94587]: config renderd(0): num_threads=4
renderd[94587]: config renderd(0): tile_dir=/var/lib/mod_tile
renderd[94587]: config renderd(0): stats_file=/var/run/renderd/renderd.stats
renderd[94587]: config map 0:   name(ajt) file(/home/renderaccount/src/openstreetmap-carto/mapnik.xml) uri(/hot/) htcp()                                                    host(localhost)
renderd[94587]: Initialising unix server socket on /var/run/renderd/renderd.sock
renderd[94587]: Created server socket 4
renderd[94587]: Renderd is using mapnik version 3.0.23
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/unifont/unifont_upper.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/unifont/unifont_csur.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/unifont/unifont_sample.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/unifont/unifont.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSans-BoldOblique.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansMono-BoldOblique.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSans-ExtraLight.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansMono-Oblique.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Oblique.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed-Italic.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuMathTeXGyre.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerif-BoldItalic.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed-BoldItalic.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansCondensed.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-BoldOblique.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifHebrew-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTibetan-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoNastaliqUrdu-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansZanabazarSquare-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansWarangCiti-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBengali-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMath-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGujarati-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOgham-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMendeKikakui-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTeluguUI-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansChakma-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTamil-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansThai-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifTamilSlanted-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifDisplay-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDevanagari-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoNaskhArabicUI-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSamaritan-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGeorgian-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMiao-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansArabicUI-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKharoshthi-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBamum-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKayahLi-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKhudawadi-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBhaiksuki-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansPalmyrene-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoNastaliqUrdu-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoNaskhArabicUI-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLycian-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifArmenian-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDevanagari-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSinhalaUI-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansRejang-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGunjalaGondi-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGothic-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDisplay-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifThai-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDevanagariUI-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGlagolitic-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifTelugu-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDevanagariUI-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKannadaUI-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansArabicUI-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCypriot-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansJavanese-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerif-BoldItalic.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLisu-SemiBold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifDogra-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoNaskhArabic-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSoyombo-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLisu-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansInscriptionalParthian-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKhojki-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMalayalam-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMro-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTamilSupplement-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDisplay-Italic.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBuhid-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifDisplay-BoldItalic.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansHanunoo-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansArabic-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLisu-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBengali-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBrahmi-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCherokee-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTaiTham-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansUgaritic-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDuployan-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSiddham-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSinhalaUI-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifKannada-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOlChiki-Medium.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTaiLe-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansHebrew-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKannadaUI-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCanadianAboriginal-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMono-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSinhala-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansHanifiRohingya-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansPahawhHmong-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLao-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCham-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifTibetan-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTelugu-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBuginese-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTamilUI-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSharada-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifKhmer-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLaoUI-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOldTurkic-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLinearA-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifTamilSlanted-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLepcha-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansNabataean-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansNKo-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSans-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDisplay-BoldItalic.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKhmerUI-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoKufiArabic-Light.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansIndicSiyaqNumbers-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOlChiki-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansThai-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansRunic-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTelugu-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansThaiUI-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansWancho-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifDisplay-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLisu-Medium.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSans-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansElbasan-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGeorgian-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoKufiArabic-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSogdian-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifTibetan-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansEgyptianHieroglyphs-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifSinhala-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKhmer-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDeseret-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCanadianAboriginal-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGurmukhiUI-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOriyaUI-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerif-Italic.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSans-Italic.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOriyaUI-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTeluguUI-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifArmenian-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTifinagh-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansThaiUI-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBatak-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMono-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCham-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansAdlam-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBengaliUI-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMalayalamUI-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSaurashtra-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDisplay-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSymbols2-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSyriac-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTakri-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansAnatolianHieroglyphs-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGurmukhiUI-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLimbu-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifLao-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLao-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLaoUI-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLinearB-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifBalinese-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifMyanmar-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKaithi-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansEthiopic-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoKufiArabic-Extralight.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTamilUI-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMyanmar-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansAvestan-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKhmerUI-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansArmenian-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMahajani-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansPhagsPa-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifGeorgian-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBengaliUI-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerif-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKannada-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMasaramGondi-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansNewTaiLue-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTamil-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMultani-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansVai-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSoraSompeng-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMyanmarUI-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOldSogdian-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTagbanwa-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMandaic-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoKufiArabic-Thin.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOriya-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoMusic-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMyanmarUI-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCoptic-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMalayalam-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansYi-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansHebrew-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifLao-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOlChiki-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOldHungarian-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoKufiArabic-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoKufiArabic-Extrabold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifTangut-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifEthiopic-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifBengali-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLydian-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansAdlamUnjoined-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGujaratiUI-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOlChiki-SemiBold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMeeteiMayek-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTaiViet-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGrantha-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCarian-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSymbols-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCaucasianAlbanian-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCherokee-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoKufiArabic-Black.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOldNorthArabian-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSans-BoldItalic.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKhmer-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSylotiNagri-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifHebrew-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansModi-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansManichaean-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifAhom-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMayanNumerals-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOsage-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGujarati-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansJavanese-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansThaana-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifThai-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifEthiopic-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKannada-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBassaVah-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGujaratiUI-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTibetan-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifMyanmar-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOldPermic-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMarchen-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansThaana-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansPhoenician-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOsmanya-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansEthiopic-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifGujarati-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCuneiform-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifDisplay-Italic.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansHatran-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansNewa-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansPsalterPahlavi-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansArabic-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSymbols-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOldSouthArabian-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifTamil-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTagalog-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSundanese-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMalayalamUI-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifGeorgian-Bold.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansImperialAramaic-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOldPersian-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansPauCinHau-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOldItalic-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansInscriptionalPahlavi-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansShavian-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMeroitic-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansArmenian-Regular.ttf
renderd[94587]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTirhuta-Regular.ttf
Running in foreground mode...
renderd[94587]: Starting stats thread
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[94587]: Loading parameterization function for renderd[94587]: Loading parameterization function for
&#10;debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[94587]: Loading parameterization function for debug: init_storage_backend: initialising file storage backend at:                                                    /var/lib/mod_tile
&#10;renderd[94587]: Loading parameterization function for
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans Balinese Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans Balinese Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans Balinese Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans Balinese Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans Syriac Eastern Regular&#39; in FontSet &#39;fontse                                                   t-0&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans Syriac Eastern Regular&#39; in FontSet &#39;fontse                                                   t-0&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans Syriac Eastern Regular&#39; in FontSet &#39;fontse                                                   t-0&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans Syriac Eastern Regular&#39; in FontSet &#39;fontse                                                   t-0&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans Balinese Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans Balinese Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans Syriac Eastern Regular&#39; in FontSet &#39;fontse                                                   t-1&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans Syriac Eastern Regular&#39; in FontSet &#39;fontse                                                   t-1&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans CJK JP Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans CJK JP Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans Balinese Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans Balinese Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans Syriac Eastern Regular&#39; in FontSet &#39;fontse                                                   t-1&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans CJK JP Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans Balinese Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans Syriac Eastern Regular&#39; in FontSet &#39;fontse                                                   t-1&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans Balinese Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans Syriac Eastern Regular&#39; in FontSet &#39;fontse                                                   t-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans Syriac Eastern Regular&#39; in FontSet &#39;fontse                                                   t-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans CJK JP Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans Balinese Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans Syriac Eastern Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans Balinese Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Sans Syriac Eastern Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2021-05-13 06:43:24: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-2&#39;
renderd[94587]: An error occurred while loading the map layer &#39;ajt&#39;: Postgis Plugin: ERROR:  relation &quot;icesheet_polygons&quot; does not exist
LINE 1: SELECT ST_SRID(&quot;way&quot;) AS srid FROM icesheet_polygons WHERE &quot;...
                                           ^
in executeQuery Full sql was: &#39;SELECT ST_SRID(&quot;way&quot;) AS srid FROM icesheet_polygons WHERE &quot;way&quot; IS NOT NULL LIMIT 1;&#39;
  encountered during parsing of layer &#39;icesheet-poly&#39; in Layer at line 5895 of &#39;/home/renderaccount/src/openstreetmap-carto/mapnik.xml&#39;
renderd[94587]: An error occurred while loading the map layer &#39;ajt&#39;: Postgis Plugin: ERROR:  relation &quot;icesheet_polygons&quot; does not exist
LINE 1: SELECT ST_SRID(&quot;way&quot;) AS srid FROM icesheet_polygons WHERE &quot;...
                                           ^
in executeQuery Full sql was: &#39;SELECT ST_SRID(&quot;way&quot;) AS srid FROM icesheet_polygons WHERE &quot;way&quot; IS NOT NULL LIMIT 1;&#39;
  encountered during parsing of layer &#39;icesheet-poly&#39; in Layer at line 5895 of &#39;/home/renderaccount/src/openstreetmap-carto/mapnik.xml&#39;
renderd[94587]: An error occurred while loading the map layer &#39;ajt&#39;: Postgis Plugin: ERROR:  relation &quot;icesheet_polygons&quot; does not exist
LINE 1: SELECT ST_SRID(&quot;way&quot;) AS srid FROM icesheet_polygons WHERE &quot;...
                                           ^
in executeQuery Full sql was: &#39;SELECT ST_SRID(&quot;way&quot;) AS srid FROM icesheet_polygons WHERE &quot;way&quot; IS NOT NULL LIMIT 1;&#39;
  encountered during parsing of layer &#39;icesheet-poly&#39; in Layer at line 5895 of &#39;/home/renderaccount/src/openstreetmap-carto/mapnik.xml&#39;
renderd[94587]: An error occurred while loading the map layer &#39;ajt&#39;: Postgis Plugin: ERROR:  relation &quot;icesheet_polygons&quot; does not exist
LINE 1: SELECT ST_SRID(&quot;way&quot;) AS srid FROM icesheet_polygons WHERE &quot;...
                                           ^
in executeQuery Full sql was: &#39;SELECT ST_SRID(&quot;way&quot;) AS srid FROM icesheet_polygons WHERE &quot;way&quot; IS NOT NULL LIMIT 1;&#39;
  encountered during parsing of layer &#39;icesheet-poly&#39; in Layer at line 5895 of &#39;/home/renderaccount/src/openstreetmap-carto/mapnik.xml&#39;
renderd[94587]: DEBUG: Got incoming connection, fd 11, number 1
renderd[94587]: DEBUG: Got incoming request with protocol version 2
renderd[94587]: DEBUG: Got command RenderPrio fd(11) xml(ajt), z(0), x(0), y(0), mime(image/png), options()
renderd[94587]: Received request for map layer &#39;ajt&#39; which failed to load
renderd[94587]: DEBUG: Sending render cmd(4 ajt 0/0/0) with protocol version 2 to fd 11
renderd[94587]: DEBUG: Connection 0, fd 11 closed, now 0 left
renderd[94587]: DEBUG: Got incoming connection, fd 11, number 1
renderd[94587]: DEBUG: Got incoming request with protocol version 2
renderd[94587]: DEBUG: Got command RenderPrio fd(11) xml(ajt), z(0), x(0), y(0), mime(image/png), options()
renderd[94587]: Received request for map layer &#39;ajt&#39; which failed to load
renderd[94587]: DEBUG: Sending render cmd(4 ajt 0/0/0) with protocol version 2 to fd 11
renderd[94587]: DEBUG: Connection 0, fd 11 closed, now 0 left</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 May '21, 08:05</strong></p>
<img src="https://secure.gravatar.com/avatar/0f74346ddbb786aa15a232dc85ad5201?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nimistren&#39;s gravatar image" />
<p><span>nimistren</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nimistren has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-80151" class="comments-container">
&#10;</div>
<div id="comment-tools-80151" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80151-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="81891"></span>

<div id="answer-container-81891" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81891-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81891-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81891-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><code>An error occurred while loading the map layer 'ajt': Postgis Plugin: ERROR: relation "icesheet_polygons" does not exist LINE 1: SELECT ST_SRID("way") AS srid FROM icesheet_polygons WHERE "...</code></p>
<p>You forgot to import the shapefiles into your db. I think that's a quite new step in osm-carto. Check <a href="https://github.com/gravitystorm/openstreetmap-carto/blob/master/INSTALL.md#scripted-download">https://github.com/gravitystorm/openstreetmap-carto/blob/master/INSTALL.md#scripted-download</a> .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Sep '21, 09:41</strong></p>
<img src="https://secure.gravatar.com/avatar/e4587465b2b1b94834e5e625b80a29dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marcos%20Dione&#39;s gravatar image" />
<p><span>Marcos Dione</span><br />
<span class="score" title="71 reputation points">71</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marcos Dione has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81891" class="comments-container">
<span id="81893"></span>
<div id="comment-81893" class="comment">
<div id="post-81893-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That process is problematic for a couple of reasons - one is that <a href="https://github.com/nvkelso/natural-earth-vector/issues/581#issuecomment-913988101">Natural Earth Data is moving</a>, and that the "get-externa-ldata" process provides <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/4358">no feedback</a>.</p>
<p>I suspect that the user will need to:</p>
<p>1) Get the latest version of the map style</p>
<p>2) Ensure "get-external-data" does not fail</p>
<p>3) Probably, after <a href="https://lists.openstreetmap.org/pipermail/dev/2021-September/031199.html">https://lists.openstreetmap.org/pipermail/dev/2021-September/031199.html</a> , (though I do not have a proper documentation link yet) add a new index as per <a href="https://github.com/openstreetmap/chef/issues/450">https://github.com/openstreetmap/chef/issues/450</a> .</p>
</div>
<div id="comment-81893-info" class="comment-info">
<span class="comment-age">(23 Sep '21, 10:10)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-81891" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81891-form-container" class="comment-form-container">
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

