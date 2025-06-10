+++
type = "question"
title = "first time renderd problem on ubuntu 20.04"
description = '''renderd -f -c /usr/local/etc/renderd.conf renderd[74909]: Rendering daemon started renderd[74909]: Initiating request_queue renderd[74909]: Parsing section renderd renderd[74909]: Parsing render section 0 renderd[74909]: Parsing section mapnik renderd[74909]: Parsing section ajt renderd[74909]: conf...'''
date = "2020-06-15T13:55:00Z"
lastmod = "2020-06-15T16:36:00Z"
weight = 75332
keywords = [ "renderd" ]
aliases = [ "/questions/75332" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [first time renderd problem on ubuntu 20.04](/questions/75332/first-time-renderd-problem-on-ubuntu-2004)

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
<span id="post-75332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75332-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<pre><code>renderd -f -c /usr/local/etc/renderd.conf
renderd[74909]: Rendering daemon started
renderd[74909]: Initiating request_queue
renderd[74909]: Parsing section renderd
renderd[74909]: Parsing render section 0
renderd[74909]: Parsing section mapnik
renderd[74909]: Parsing section ajt
renderd[74909]: config renderd: unix socketname=/var/run/renderd/renderd.sock
renderd[74909]: config renderd: num_threads=2
renderd[74909]: config renderd: num_slaves=0
renderd[74909]: config renderd: tile_dir=/var/lib/mod_tile
renderd[74909]: config renderd: stats_file=/var/run/renderd/renderd.stats
renderd[74909]: config mapnik:  plugins_dir=/usr/lib/mapnik/3.0/input
renderd[74909]: config mapnik:  font_dir=/usr/share/fonts/truetype
renderd[74909]: config mapnik:  font_dir_recurse=1
renderd[74909]: config renderd(0): Active
renderd[74909]: config renderd(0): unix socketname=/var/run/renderd/renderd.sock
renderd[74909]: config renderd(0): num_threads=2
renderd[74909]: config renderd(0): tile_dir=/var/lib/mod_tile
renderd[74909]: config renderd(0): stats_file=/var/run/renderd/renderd.stats
renderd[74909]: config map 0:   name(ajt) file(/home/hus/src/openstreetmap-carto/mapnik.xml) uri(/hot/) htcp() host(localhost)
renderd[74909]: Initialising unix server socket on /var/run/renderd/renderd.sock
renderd[74909]: Created server socket 4
renderd[74909]: Renderd is using mapnik version 3.0.23
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/lohit-oriya/Lohit-Odia.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/arphic/uming.ttc
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/arphic/ukai.ttc
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/samyak/Samyak-Devanagari.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/malayalam/Meera-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/malayalam/Suruma.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/malayalam/AnjaliOldLipi-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/malayalam/RaghuMalayalamSans-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/malayalam/Keraleeyam-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/malayalam/Karumbi-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/malayalam/Rachana-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/malayalam/Rachana-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/malayalam/Dyuthi-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/malayalam/Uroob-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-beng-extra/JamrulNormal.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-beng-extra/mitra.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-beng-extra/LikhanNormal.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-beng-extra/MuktiNarrowBold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-beng-extra/ani.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-beng-extra/MuktiNarrow.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/freefont/FreeSerifBoldItalic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/freefont/FreeMonoOblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/freefont/FreeSans.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/freefont/FreeMonoBold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/freefont/FreeMono.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/freefont/FreeSansBoldOblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/freefont/FreeMonoBoldOblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/freefont/FreeSansBold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/freefont/FreeSerifBold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/freefont/FreeSerif.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/freefont/FreeSerifItalic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/freefont/FreeSansOblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCypriot-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTakri-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSinhala-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansHanifiRohingya-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifHebrew-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBuginese-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoNaskhArabicUI-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifThai-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGlagolitic-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifArmenian-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansNewa-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansElbasan-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOsage-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifGeorgian-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDevanagari-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTifinagh-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoMono-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMyanmarUI-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansModi-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOldItalic-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBrahmi-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifSinhala-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOlChiki-SemiBold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansArabicUI-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGujarati-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifHebrew-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifBengali-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLisu-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifKhmer-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGeorgian-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansArabic-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifTelugu-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifMyanmar-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansThaiUI-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSaurashtra-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTirhuta-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansHebrew-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTaiTham-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifLao-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifSinhala-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKannadaUI-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBuhid-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTibetan-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMandaic-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoMusic-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDuployan-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMath-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSymbols2-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansPhagsPa-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansUgaritic-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansArmenian-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCherokee-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLaoUI-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSans-BoldItalic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansPahawhHmong-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansChakma-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCherokee-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKhmer-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansRunic-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBamum-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTibetan-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDevanagariUI-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLisu-SemiBold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerif-BoldItalic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansZanabazarSquare-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoNaskhArabic-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOldPermic-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansHanunoo-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifKannada-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDisplay-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoColorEmoji.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMayanNumerals-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSinhalaUI-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSyriac-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansJavanese-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansNKo-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOsmanya-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSylotiNagri-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOldSouthArabian-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSamaritan-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansAnatolianHieroglyphs-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansPauCinHau-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKhmerUI-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansInscriptionalParthian-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansImperialAramaic-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMeeteiMayek-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifDevanagari-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifEthiopic-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLimbu-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMiao-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansArmenian-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifTamilSlanted-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKhmer-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBengaliUI-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansThaana-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansAdlam-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGurmukhi-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSinhalaUI-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMalayalam-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMro-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansVai-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTamilSupplement-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifGujarati-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGunjalaGondi-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansHatran-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGujarati-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKhmerUI-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansArabic-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansThai-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSharada-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansInscriptionalPahlavi-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansThai-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifBalinese-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCham-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBengali-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifDogra-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansPalmyrene-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSans-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTelugu-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifLao-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBatak-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifTamil-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMendeKikakui-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGeorgian-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansThaiUI-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMalayalamUI-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMeroitic-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTamilUI-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMyanmar-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifGeorgian-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMarchen-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTagbanwa-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoKufiArabic-Extrabold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTeluguUI-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKhojki-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansIndicSiyaqNumbers-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSans-Italic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoKufiArabic-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSymbols-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOriyaUI-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGrantha-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOlChiki-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifKannada-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansJavanese-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLisu-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoKufiArabic-Light.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifGujarati-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKaithi-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansAvestan-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGothic-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansYi-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifDisplay-Italic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansPsalterPahlavi-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifTelugu-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOldTurkic-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSoyombo-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOlChiki-Medium.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoKufiArabic-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifTangut-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMono-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCanadianAboriginal-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansArabicUI-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOldHungarian-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifArmenian-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSogdian-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLepcha-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMahajani-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoNastaliqUrdu-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansShavian-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMyanmarUI-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGujaratiUI-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansHebrew-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMongolian-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansWarangCiti-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansEthiopic-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSiddham-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKharoshthi-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansPhoenician-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansAdlamUnjoined-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMalayalamUI-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOldPersian-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCaucasianAlbanian-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoKufiArabic-Black.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerif-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLycian-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOgham-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifDisplay-BoldItalic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKayahLi-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifDisplay-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDevanagariUI-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKhudawadi-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDisplay-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKannada-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerif-Italic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoKufiArabic-Extralight.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTaiViet-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBengaliUI-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKannada-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOldSogdian-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLinearA-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTamil-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifMyanmar-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifTibetan-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansKannadaUI-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBhaiksuki-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTamilUI-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifTamil-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDevanagari-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifEthiopic-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifDisplay-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoNaskhArabicUI-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSymbols-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOldNorthArabian-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifKhmer-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansEgyptianHieroglyphs-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMasaramGondi-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansThaana-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifAhom-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOriya-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOriya-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSinhala-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansNewTaiLue-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCarian-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCanadianAboriginal-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoNastaliqUrdu-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTamil-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDisplay-BoldItalic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifTibetan-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCoptic-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansWancho-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBassaVah-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansNabataean-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMono-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoKufiArabic-Thin.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMyanmar-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSundanese-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDeseret-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGurmukhiUI-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansManichaean-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLao-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifThai-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLisu-Medium.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansRejang-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifTamilSlanted-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGurmukhiUI-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMultani-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCham-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOriyaUI-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLao-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTelugu-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLaoUI-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTaiLe-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansDisplay-Italic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansOlChiki-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansGujaratiUI-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLinearB-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTeluguUI-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansSoraSompeng-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansLydian-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansCuneiform-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansBengali-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifMalayalam-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerifGurmukhi-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansEthiopic-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSans-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansTagalog-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/noto/NotoSansMalayalam-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/Nakula/nakula.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-guru-extra/Saab.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst-one/KacstOne.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst-one/KacstOne-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/sinhala/lklug.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-khmeros-core/KhmerOSsys.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/ttf-khmeros-core/KhmerOS.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/lohit-telugu/Lohit-Telugu.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Kinnari-Italic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgTypewriter-BoldOblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Umpush.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Norasi-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgTypo-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgTypewriter.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Sawasdee-BoldOblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Waree-Oblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgTypewriter-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Kinnari-BoldOblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Norasi.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgMono-Oblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Garuda-Oblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Umpush-Light.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Purisa-BoldOblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Umpush-Oblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgTypist.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Norasi-Italic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Loma-BoldOblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Laksaman-Italic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Laksaman-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Umpush-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Purisa-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgTypo-BoldOblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Garuda.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Waree.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Garuda-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Garuda-BoldOblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgTypist-Oblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgMono-BoldOblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Umpush-LightOblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Laksaman-BoldItalic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgTypewriter-Oblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgTypo-Oblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Kinnari.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Loma.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Kinnari-BoldItalic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Purisa-Oblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Kinnari-Oblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Norasi-Oblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Loma-Oblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Kinnari-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Norasi-BoldItalic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgMono.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgTypist-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Umpush-BoldOblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Sawasdee.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Waree-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgTypist-BoldOblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Sawasdee-Oblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgTypo.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Waree-BoldOblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Laksaman.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Sawasdee-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/TlwgMono-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Loma-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Norasi-BoldOblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tlwg/Purisa.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/lao/Phetsarath_OT.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/openoffice/opens___.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/KacstPoster.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/KacstDigital.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/KacstTitleL.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/KacstArt.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/KacstNaskh.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/KacstFarsi.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/mry_KacstQurn.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/KacstDecorative.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/KacstPen.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/KacstScreen.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/KacstTitle.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/KacstOffice.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/KacstQurn.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/KacstBook.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/kacst/KacstLetter.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-kalapi/Kalapi.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/lohit-tamil/Lohit-Tamil.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/abyssinica/AbyssinicaSIL-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansMono-BoldOblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSans-BoldOblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSans-ExtraLight.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuMathTeXGyre.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansCondensed.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed-Italic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansMono-Oblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Oblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerif-BoldItalic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerifCondensed-BoldItalic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-BoldOblique.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-deva-extra/samanata.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-deva-extra/chandas1-2.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-deva-extra/kalimati.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/lohit-malayalam/Lohit-Malayalam.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/Sarai/Sarai.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/samyak-fonts/Samyak-Gujarati.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/samyak-fonts/Samyak-Malayalam.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/samyak-fonts/Samyak-Tamil.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/Gubbi/Gubbi.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationMono-BoldItalic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationMono-Italic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationSansNarrow-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationSansNarrow-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationSansNarrow-Italic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationSans-BoldItalic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationSansNarrow-BoldItalic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/Sahadeva/sahadeva.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/lohit-punjabi/Lohit-Gurmukhi.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-gujr-extra/padmaa.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-gujr-extra/aakar-medium.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-gujr-extra/padmaa-Bold.1.1.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-gujr-extra/Rekha.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-gujr-extra/padmaa-Medium-0.5.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/pagul/Pagul.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation2/LiberationMono-BoldItalic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation2/LiberationMono-Italic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation2/LiberationSerif-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation2/LiberationSerif-BoldItalic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation2/LiberationMono-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation2/LiberationSans-Italic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation2/LiberationSerif-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation2/LiberationSerif-Italic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation2/LiberationSans-BoldItalic.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation2/LiberationMono-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/Gargi/Gargi.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/lohit-kannada/Lohit-Kannada.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/lohit-bengali/Lohit-Bengali.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/Navilu/Navilu.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/lohit-assamese/Lohit-Assamese.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/padauk/Padauk-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/padauk/Padauk-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/padauk/PadaukBook-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/padauk/PadaukBook-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/unifont/unifont_upper.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/unifont/unifont_sample.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/unifont/unifont_csur.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/unifont/unifont.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/tibetan-machine/TibetanMachineUni.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/lohit-tamil-classical/Lohit-Tamil-Classical.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/lohit-devanagari/Lohit-Devanagari.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-yrsa-rasa/Rasa-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-yrsa-rasa/Yrsa-Light.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-yrsa-rasa/Rasa-SemiBold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-yrsa-rasa/Yrsa-Regular.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-yrsa-rasa/Rasa-Medium.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-yrsa-rasa/Rasa-Light.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-yrsa-rasa/Yrsa-SemiBold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-yrsa-rasa/Yrsa-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-yrsa-rasa/Rasa-Bold.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-yrsa-rasa/Yrsa-Medium.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-telu-extra/vemana2000.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-telu-extra/Pothana2000.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/ubuntu/Ubuntu-LI.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/ubuntu/UbuntuMono-B.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/ubuntu/Ubuntu-M.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/ubuntu/Ubuntu-C.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/ubuntu/Ubuntu-L.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/ubuntu/Ubuntu-Th.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/ubuntu/Ubuntu-BI.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/ubuntu/UbuntuMono-R.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/ubuntu/Ubuntu-B.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/ubuntu/Ubuntu-R.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/ubuntu/UbuntuMono-BI.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/ubuntu/UbuntuMono-RI.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/ubuntu/Ubuntu-MI.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/ubuntu/Ubuntu-RI.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/fonts-orya-extra/utkal.ttf
renderd[74909]: DEBUG: Loading font: /usr/share/fonts/truetype/lohit-gujarati/Lohit-Gujarati.ttf
Running in foreground mode...
renderd[74909]: Starting stats thread
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[74909]: Loading parameterization function for 
debug: init_storage_backend: initialising file storage backend at: /var/lib/mod_tile
renderd[74909]: Loading parameterization function for 
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;Noto Sans Balinese Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;Noto Sans Balinese Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;Noto Sans Syriac Eastern Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;Noto Sans Syriac Eastern Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-0&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;Noto Sans Balinese Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;Noto Sans Syriac Eastern Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;Noto Sans Balinese Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;Noto Sans Syriac Eastern Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;Noto Sans CJK JP Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-1&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;Noto Sans CJK JP Bold&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;Noto Sans Balinese Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;Noto Sans Syriac Eastern Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;Noto Sans CJK JP Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;Noto Sans Balinese Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;Noto Sans Syriac Eastern Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;Noto Emoji Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;HanaMinA Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;HanaMinB Regular&#39; in FontSet &#39;fontset-2&#39;
Mapnik LOG&gt; 2020-06-15 08:23:29: warning: unable to find face-name &#39;unifont Medium&#39; in FontSet &#39;fontset-2&#39;
renderd[74909]: Using web mercator projection settings
renderd[74909]: Using web mercator projection settings
^C</code></pre>
<p>how can I fix?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jun '20, 13:55</strong></p>
<img src="https://secure.gravatar.com/avatar/c900cb79e779b08898ce87c7de1ee948?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="huseyin30&#39;s gravatar image" />
<p><span>huseyin30</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="huseyin30 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Jun '20, 14:12</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span></p>
</div>
</div>
<div id="comments-container-75332" class="comments-container">
<span id="75333"></span>
<div id="comment-75333" class="comment">
<div id="post-75333-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What is your problem? Your question is just an unformatted splat of log output.</p>
<p>Please explain what you are trying to do, what instructions you are following, and what isn't working.</p>
</div>
<div id="comment-75333-info" class="comment-info">
<span class="comment-age">(15 Jun '20, 13:58)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-75332" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75332-form-container" class="comment-form-container">
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

<span id="75334"></span>

<div id="answer-container-75334" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75334-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75334-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75334-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I got below errors on output. Is this normal?</p>
<p>-06-15 08:23:29: warning: unable to find face-name 'Noto Sans CJK JP Regular'</p>
<p><a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/</a></p>
<p>I followed above instructions. Could someone help?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jun '20, 14:56</strong></p>
<img src="https://secure.gravatar.com/avatar/c900cb79e779b08898ce87c7de1ee948?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="huseyin30&#39;s gravatar image" />
<p><span>huseyin30</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="huseyin30 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Jun '20, 14:56</strong> </span></p>
</div>
</div>
<div id="comments-container-75334" class="comments-container">
<span id="75336"></span>
<div id="comment-75336" class="comment">
<div id="post-75336-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you haven't installed those fonts, those errors are normal.</p>
<p>Does the server actually render an example tile?</p>
</div>
<div id="comment-75336-info" class="comment-info">
<span class="comment-age">(15 Jun '20, 15:13)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="75337"></span>
<div id="comment-75337" class="comment">
<div id="post-75337-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How can i check installation?</p>
</div>
<div id="comment-75337-info" class="comment-info">
<span class="comment-age">(15 Jun '20, 15:24)</span> <span class="comment-user userinfo">huseyin30</span>
</div>
</div>
<span id="75338"></span>
<div id="comment-75338" class="comment">
<div id="post-75338-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>As suggested in <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/</a> , point a web browser at: <a href="http://yourserveripaddress/hot/0/0/0.png">http://yourserveripaddress/hot/0/0/0.png</a> . You should see a map of the world in your browser and some more debug on the command line, including “DEBUG: START TILE” and “DEBUG: DONE TILE”.</p>
</div>
<div id="comment-75338-info" class="comment-info">
<span class="comment-age">(15 Jun '20, 16:36)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-75334" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75334-form-container" class="comment-form-container">
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

