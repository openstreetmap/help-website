+++
type = "question"
title = "Meer blau färben (Garmin)"
description = '''Hallo, bin Neuling und habe in Madagascar Nosy Be und Diego Strassen und POI&#x27;s erstellt. Nach herunterladen des Files auf RAUMBEZUG merkte ich, dass das Meer und das Land weiss eingefärbt sind. Nun habe ich die Administriv Territorial Linie mit NATURE=Water bezeichnet und alles ist blau geworden. Wi...'''
date = "2010-12-17T15:20:00Z"
lastmod = "2011-03-15T02:25:00Z"
weight = 1849
keywords = [ "water", "garmin", "coastline", "lang-de" ]
aliases = [ "/questions/1849" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Meer blau färben (Garmin)](/questions/1849/meer-blau-farben-garmin)

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
<span id="post-1849-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1849-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-1849-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hallo, bin Neuling und habe in Madagascar Nosy Be und Diego Strassen und POI's erstellt. Nach herunterladen des Files auf RAUMBEZUG merkte ich, dass das Meer und das Land weiss eingefärbt sind. Nun habe ich die Administriv Territorial Linie mit NATURE=Water bezeichnet und alles ist blau geworden. Wie kann ich für das Garmin das Meer blau färbben? Danke für schnelle Hilfe Grüsse und schöne Festtage Roman Kissling (roki)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-water" rel="tag" title="see questions tagged &#39;water&#39;">water</span> <span class="post-tag tag-link-garmin" rel="tag" title="see questions tagged &#39;garmin&#39;">garmin</span> <span class="post-tag tag-link-coastline" rel="tag" title="see questions tagged &#39;coastline&#39;">coastline</span> <span class="post-tag tag-link-lang-de" rel="tag" title="see questions tagged &#39;lang-de&#39;">lang-de</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Dec '10, 15:20</strong></p>
<img src="https://secure.gravatar.com/avatar/5b7557383c261dac7e5ab63d3b643411?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="roki&#39;s gravatar image" />
<p><span>roki</span><br />
<span class="score" title="45 reputation points">45</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="roki has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Apr '13, 02:05</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-1849" class="comments-container">
&#10;</div>
<div id="comment-tools-1849" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1849-form-container" class="comment-form-container">
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

<span id="3807"></span>

<div id="answer-container-3807" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3807-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-3807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Das Meer wird in OSM nicht als Fläche gemappt, sondern nur die Küstenlinie. Für diese gibt es die Konvention, dass in Way-richtung links das Land und rechts das Wasser ist. Das Tag dafür ist natural=coastline. natural=water verwendet man dagegen für Binnenseen und sonstige Wasserflächen.</p>
<p>Die Küstenlinie darf nicht unterbrochen sein (alle Einzelstücke müssen ohne Lücke zusammenhängen).</p>
<p>Bei der Kartenumwandlung in das Garminformat muss für gefülltes Meer eine Option gesetzt werden. Wenn eine bestimmte Karte das Meer nicht darstellt, in anderen Karten funktioniert es aber (z.B. auf der OSM-Hauptseite), dann sollte man nichts am Mapping ändern sondern mit dem Kartenersteller Kontakt aufnehmen oder eine andere Karte versuchen.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Mar '11, 02:25</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Mar '11, 02:28</strong> </span></p>
</div>
</div>
<div id="comments-container-3807" class="comments-container">
&#10;</div>
<div id="comment-tools-3807" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3807-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1951"></span>

<div id="answer-container-1951" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1951-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1951-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-1951-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>So viel ich weiß heißt es eigentlich <a href="https://wiki.openstreetmap.org/wiki/DE:Tag:natural%3Dwater"><strong>natural=water</strong></a>. Probier's mit <strong>natural=water</strong> aus.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Dec '10, 14:22</strong></p>
<img src="https://secure.gravatar.com/avatar/e2a594f7acee8d0da21209c9bb88bc6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NUP&#39;s gravatar image" />
<p><span>NUP</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NUP has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1951" class="comments-container">
&#10;</div>
<div id="comment-tools-1951" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1951-form-container" class="comment-form-container">
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

