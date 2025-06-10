+++
type = "question"
title = "UMAP: fehlerhafte Serverantwort"
description = '''Hi, Beim Anzeigen meiner UMAP-Karte mit verschiedenen Ebenen über Overpass-api-Abfragen, bekomme ich oft die Meldung &quot;fehlerhafte Serverantwort&quot;. Vermutlich machen einzelne POIs Probleme. Wie kann ich die Fehlerursache herausfinden? Gruß schoka'''
date = "2017-09-01T15:31:00Z"
lastmod = "2017-09-05T21:22:00Z"
weight = 58912
keywords = [ "overpass", "server", "lang-de", "umap" ]
aliases = [ "/questions/58912" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [UMAP: fehlerhafte Serverantwort](/questions/58912/umap-fehlerhafte-serverantwort)

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
<span id="post-58912-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58912-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-58912-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Beim Anzeigen meiner <a href="http://u.osmfr.org/m/161185/">UMAP-Karte</a> mit verschiedenen Ebenen über Overpass-api-Abfragen, bekomme ich oft die Meldung "fehlerhafte Serverantwort". Vermutlich machen einzelne POIs Probleme. Wie kann ich die Fehlerursache herausfinden?</p>
<p>Gruß</p>
<p>schoka</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span> <span class="post-tag tag-link-lang-de" rel="tag" title="see questions tagged &#39;lang-de&#39;">lang-de</span> <span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Sep '17, 15:31</strong></p>
<img src="https://secure.gravatar.com/avatar/a9422e2e0a11da3736d6581ddd72dd4e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="schoka&#39;s gravatar image" />
<p><span>schoka</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="schoka has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Sep '17, 20:32</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span></p>
</div>
</div>
<div id="comments-container-58912" class="comments-container">
<span id="58956"></span>
<div id="comment-58956" class="comment">
<div id="post-58956-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ich weiss nicht genau, was das Problem verursacht, aber du könntest mal Folgendes versuchen: In Chrome/Firefox F12 drücken und ins richtige Untermenü wechseln, so dass die einzelnen HTTP-Anfragen sichtbar sind, anschliessend auf die HTTP Statuscodes achten. 4xx und 5xx weisen auf ein Problem hin, siehe <a href="https://de.wikipedia.org/wiki/HTTP-Statuscode">https://de.wikipedia.org/wiki/HTTP-Statuscode</a> . Falls nur Codes mit 1xx, 2xx und 3xx sichtbar sind, mal auf den Inhalt der jeweiligen Antworten achten.</p>
</div>
<div id="comment-58956-info" class="comment-info">
<span class="comment-age">(04 Sep '17, 06:40)</span> <span class="comment-user userinfo">skorbut</span>
</div>
</div>
</div>
<div id="comment-tools-58912" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58912-form-container" class="comment-form-container">
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

<span id="58957"></span>

<div id="answer-container-58957" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58957-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58957-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-58957-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Den Kommentar habe ich geschrieben, ohne gemerkt zu haben, dass du deine Karte ja verlinkt hast. Mittels Net Panel von Firefox sind zwei Probleme feststellbar:</p>
<ol>
<li>Es werden zuviele Einzel-Anfragen an overpass-api.de abgeschickt. (HTTP Statuscode 429). Hier solltest du versuchen, diese Anfragen zu bündeln.</li>
<li>Es wird der URL (<a href="http://openstreetmap.fr/piwik/piwik.php?action_name=Bio%20in%20deiner%20N%C3%A4he%20-%20uMap&amp;idsite=8&amp;rec=1&amp;r=981152&amp;h=7&amp;m=40&amp;s=57&amp;url=http%3A%2F%2Fumap.openstreetmap.fr%2Fde%2Fmap%2Fbio-in-deiner-nahe_161185%2311%2F48.5423%2F12.2704&amp;_id=bbd05973fe316fcc&amp;_idts=1504503658&amp;_idvc=1&amp;_idn=0&amp;_refts=0&amp;_viewts=1504503658&amp;send_image=1&amp;pdf=0&amp;qt=0&amp;realp=0&amp;wma=0&amp;dir=0&amp;fla=1&amp;java=0&amp;gears=0&amp;ag=0&amp;cookie=1&amp;res=1920x1080&amp;gt_ms=629&amp;pv_id=j7qxe5">link</a>) aufgerufen . Ich sehe den Zweck dafür gerade nicht, jedoch verursacht das einen Fehler 500 (Internal Server Error). Das impliziert, dass die HTTP-Anfrage korrekt formuliert ist, der Server jedoch ein Problem hat und diese nicht handhaben kann.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Sep '17, 06:48</strong></p>
<img src="https://secure.gravatar.com/avatar/be8434a6bf8d224ff9367c80548447c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skorbut&#39;s gravatar image" />
<p><span>skorbut</span><br />
<span class="score" title="206 reputation points">206</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skorbut has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Nov '20, 19:58</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span></p>
</div>
</div>
<div id="comments-container-58957" class="comments-container">
<span id="58993"></span>
<div id="comment-58993" class="comment">
<div id="post-58993-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Danke für die Anwort. 429 deutet wohl auf "too many requests" hin. Obwohl der Kartenausschnitt begrenzt ist und die Treffermenge auch nicht hoch ist. Allerdings wird die Abfrage meiner 4 Layers mit jeder Kartenverschiebung/Zoom erneut angestossen. Auch beim reinzoomen - obwohl sich die Ergebnismenge nicht ändert. Das kann ich in UMAP nicht beeinflussen. Die overpass Abfrage für einen Layer lautet z.B.: <a href="https://overpass-api.de/api/interpreter?data=%5Bout:json%5D%5Btimeout:25%5D;(node%5Bshop=bakery%5D%5Borganic%5D(%7Bsouth%7D,%7Bwest%7D,%7Bnorth%7D,%7Beast%7D);way%5Bshop=bakery%5D%5Borganic%5D(%7Bsouth%7D,%7Bwest%7D,%7Bnorth%7D,%7Beast%7D););out"><code>https://overpass-api.de/api/interpreter?data=[out:json][timeout:25];(node[shop=bakery][organic]({south},{west},{north},{east});way[shop=bakery][organic]({south},{west},{north},{east}););out</code></a><code> center qt;</code> Kann man da noch optimieren?</p>
</div>
<div id="comment-58993-info" class="comment-info">
<span class="comment-age">(05 Sep '17, 21:22)</span> <span class="comment-user userinfo">schoka</span>
</div>
</div>
</div>
<div id="comment-tools-58957" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58957-form-container" class="comment-form-container">
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

