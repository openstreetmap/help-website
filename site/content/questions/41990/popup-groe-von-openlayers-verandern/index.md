+++
type = "question"
title = "Popup-Größe von openlayers verändern"
description = '''Über dieses Programm  http://osmtools.de/easymap/index.php?lang=de&amp;amp;page=editor erstelle ich eine Karte (zur Verwendung auf einer Webseite) mit einem oder mehreren Markern. Wenn man auf die Marker klickt, öffnet sich ein Popup mit dem von mir vorgegebenen Text. Da der Text etwas umfangreicher ist...'''
date = "2015-03-29T15:55:00Z"
lastmod = "2015-03-31T07:38:00Z"
weight = 41990
keywords = [ "größe", "popup", "openlayers", "lang-de" ]
aliases = [ "/questions/41990" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Popup-Größe von openlayers verändern](/questions/41990/popup-groe-von-openlayers-verandern)

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
<span id="post-41990-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41990-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41990-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Über dieses Programm <a href="http://osmtools.de/easymap/index.php?lang=de&amp;page=editor">http://osmtools.de/easymap/index.php?lang=de&amp;page=editor</a> erstelle ich eine Karte (zur Verwendung auf einer Webseite) mit einem oder mehreren Markern.</p>
<p>Wenn man auf die Marker klickt, öffnet sich ein Popup mit dem von mir vorgegebenen Text. Da der Text etwas umfangreicher ist, muss in dem Popup gescrollt werden. Das möchte ich vermeiden, sondern lieber die Größe des Popups ändern. Ich vermute mal, dass das in einer der CSS-Dateien möglich ist.</p>
<p>Wenn mir jemand einen Hinweis geben könnte, wo genau, wäre ich sehr dankbar, weil ich sonst nach dem Motto "Trial and Error" alles ausprobieren müsste. Vielen Dank im voraus!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-größe" rel="tag" title="see questions tagged &#39;größe&#39;">größe</span> <span class="post-tag tag-link-popup" rel="tag" title="see questions tagged &#39;popup&#39;">popup</span> <span class="post-tag tag-link-openlayers" rel="tag" title="see questions tagged &#39;openlayers&#39;">openlayers</span> <span class="post-tag tag-link-lang-de" rel="tag" title="see questions tagged &#39;lang-de&#39;">lang-de</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Mar '15, 15:55</strong></p>
<img src="https://secure.gravatar.com/avatar/e472b8dab1c474090d72739b5d8270fb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hadedeha&#39;s gravatar image" />
<p><span>hadedeha</span><br />
<span class="score" title="51 reputation points">51</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hadedeha has one accepted answer">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Mar '15, 14:53</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-41990" class="comments-container">
<span id="42013"></span>
<div id="comment-42013" class="comment">
<div id="post-42013-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Die von osmtools generierten Karten verwenden OpenLayers, demnach ist die Lösung dort zu suchen. Anscheinend kann man einem <a href="http://dev.openlayers.org/docs/files/OpenLayers/Popup-js.html">OpenLayers.Popup</a> die Größe beim Erstellen mitteilen.</p>
</div>
<div id="comment-42013-info" class="comment-info">
<span class="comment-age">(30 Mar '15, 11:47)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41990" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41990-form-container" class="comment-form-container">
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

<span id="42032"></span>

<div id="answer-container-42032" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42032-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42032-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-42032-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="aseerel4c26 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Dankeschön! Für alle, die auch danach suchen: Es muss die util.js angepasst werden, in Line 33 ab Column 103:</p>
<pre><code>feature.popupClass = OpenLayers.Class(OpenLayers.Popup.FramedCloud, {minSize: new OpenLayers.Size(200, 120) } );</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Mar '15, 16:32</strong></p>
<img src="https://secure.gravatar.com/avatar/e472b8dab1c474090d72739b5d8270fb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hadedeha&#39;s gravatar image" />
<p><span>hadedeha</span><br />
<span class="score" title="51 reputation points">51</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hadedeha has one accepted answer">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>30 Mar '15, 19:53</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span></p>
</div>
</div>
<div id="comments-container-42032" class="comments-container">
<span id="42033"></span>
<div id="comment-42033" class="comment">
<div id="post-42033-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>[Meta:] ich wollte hier den Kommentar von scai in eine Antwort umwandeln, leider klappt das nicht, da die Oberfläche vom FAQ-System "unknown error" zurückgibt. Früher hat das imme rgeklappt mit dem Umwandeln von Kommentar in Antwort und umgekehrt. Ist das bei euch reproduzierbar?</p>
</div>
<div id="comment-42033-info" class="comment-info">
<span class="comment-age">(30 Mar '15, 18:11)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="42037"></span>
<div id="comment-42037" class="comment">
<div id="post-42037-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>meta <a href="http://help.openstreetmap.org/users/99/stephan75"></a><a href="http://help.openstreetmap.org/users/99/stephan75">@stephan75</a>: ja, ich bekomme dieselbe Fehlermeldung. Das ist <span>seit</span> dem letzten Update(?) so. Bei manchen Fragen geht es, ein ander mal wieder nicht. Besonders blöd ist das, wenn man eine "Antwort", die "Kommentare" besitzt, in einen Kommentar (zur "Frage") umwandeln will – dann werden die angehängten "Kommentare" trotzdem verschoben.</p>
</div>
<div id="comment-42037-info" class="comment-info">
<span class="comment-age">(30 Mar '15, 20:43)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="42056"></span>
<div id="comment-42056" class="comment">
<div id="post-42056-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Jop, das Interface ist leider aktuell ziemlich kaputt :\</p>
</div>
<div id="comment-42056-info" class="comment-info">
<span class="comment-age">(31 Mar '15, 07:38)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-42032" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42032-form-container" class="comment-form-container">
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

