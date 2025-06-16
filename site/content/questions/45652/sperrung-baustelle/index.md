+++
type = "question"
title = "Sperrung, Baustelle"
description = '''Hallo an alle. werden bei der Navigation mit OSMand für Android Straßensperrungen durch Baustellen usw berücksichtigt und Alternativrouten angeboten. kann ich als User hier eine Baustelle/Sperrung einarbeiten. Grüße aus Brandenburg Frank'''
date = "2015-09-29T10:15:00Z"
lastmod = "2015-10-07T17:32:00Z"
weight = 45652
keywords = [ "sperrung", "baustelle", "lang-de" ]
aliases = [ "/questions/45652" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Sperrung, Baustelle](/questions/45652/sperrung-baustelle)

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
<span id="post-45652-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45652-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-45652-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hallo an alle. werden bei der Navigation mit OSMand für Android Straßensperrungen durch Baustellen usw berücksichtigt und Alternativrouten angeboten. kann ich als User hier eine Baustelle/Sperrung einarbeiten. Grüße aus Brandenburg Frank</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-sperrung" rel="tag" title="see questions tagged &#39;sperrung&#39;">sperrung</span> <span class="post-tag tag-link-baustelle" rel="tag" title="see questions tagged &#39;baustelle&#39;">baustelle</span> <span class="post-tag tag-link-lang-de" rel="tag" title="see questions tagged &#39;lang-de&#39;">lang-de</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Sep '15, 10:15</strong></p>
<img src="https://secure.gravatar.com/avatar/aa8bdcd8170bb16d1eab6c4c59e7da34?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="franki43&#39;s gravatar image" />
<p><span>franki43</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="franki43 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Sep '15, 12:56</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-45652" class="comments-container">
&#10;</div>
<div id="comment-tools-45652" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45652-form-container" class="comment-form-container">
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

<span id="45653"></span>

<div id="answer-container-45653" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45653-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45653-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-45653-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Ja, man kann Baustellen eintragen. Und ja, sie werden dann auch von allen Routern berücksichtigt. Siehe dazu <a href="https://wiki.openstreetmap.org/wiki/DE:Key:construction">Key:construction</a>.</p>
<p>Beispiel: Um eine momentan als <em>highway=primary</em> eingetragene Straße als Baustelle zu markieren, änderst du die Attribute auf <em>highway=construction</em>, <em>construction=primary</em>. Für secondary, tertiary, residential etc. läuft es analog ab. Dabei gibt es mehrere Dinge zu bedenken.</p>
<ol>
<li>Die Straße ist dadurch für Router komplett gesperrt, also u.a. auch für Fußgänger und Fahrradfahrer. Falls sich die Sperrung aber nicht auf diese Gruppen auswirkt, dann solltest du via foot=yes bzw. bicycle=yes deren Zugang wieder erlauben.</li>
<li>Die Sperrung wirkt sich solange aus, bis du die entsprechenden Attribute wieder rückgängig machst <em>und</em>(!) alle Nutzer ihre Kartendaten wieder aktualisiert haben. Gerade der letzte Punkt ist besonders wichtig. Aus ihm folgt, dass kurzzeitige Baustellen <em>nicht</em> eingetragen werden sollten. Denn andernfalls kann es passieren, dass viele Nutzer die Baustelle noch in ihren (veralteten) Karten haben, obwohl sie gar nicht mehr existiert.</li>
</ol>
<p>Ab welcher Dauer Baustellen eingetragen werden sollten ist nicht klar definiert und hängt einerseits vom Aktualisierungsintervall des entsprechenden Routers ab und andererseits davon, wie oft jeder Anwender seine Kartendaten selbst aktualisiert. Du hast OSMand als Beispiel angegeben, dort ist das Aktualisierungsintervall ungefähr zwei mal monatlich, manchmal auch nur einmal im Monat soweit ich weiß. Das heißt, dass es bereits kritisch ist, Baustellen einzutragen, die lediglich einen Monat lang existieren. Online Router haben oft ein höheres Aktualisierungsintervall, andere Kartenanbieter können hingegen aber auch ein wesentlich selteneres Intervall nutzen.</p>
<p>Falls du weißt, bis wann die Baustelle in etwa existieren wird, kannst du dieses Datum auch mittels <a href="https://wiki.openstreetmap.org/wiki/Key:opening_date">opening_date</a> angeben. Allerdings ist mir bisher kein Router bekannt, welcher dieses Attribut auswertet.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Sep '15, 12:47</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Sep '15, 12:54</strong> </span></p>
</div>
</div>
<div id="comments-container-45653" class="comments-container">
<span id="45658"></span>
<div id="comment-45658" class="comment">
<div id="post-45658-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>es sei noch angemerkt, dass auch wenn eine (z.b. einwöchige) Baustelle korrekterweise nicht in den OSM-Daten eingetragen ist, Router wie OsmAnd trotzdem die Baustelle umgehen können, indem sie Baustellen/Sperrungen/Stau/... aus einer anderen Quelle beziehen.</p>
</div>
<div id="comment-45658-info" class="comment-info">
<span class="comment-age">(29 Sep '15, 20:06)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="45667"></span>
<div id="comment-45667" class="comment">
<div id="post-45667-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Das ist natürlich richtig. Durch die Attribute highway=construction, construction=* ist es für jeden Router möglich, die Baustelle wieder "rauszurechnen" und zu ignorieren.</p>
</div>
<div id="comment-45667-info" class="comment-info">
<span class="comment-age">(30 Sep '15, 07:35)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="45793"></span>
<div id="comment-45793" class="comment">
<div id="post-45793-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/158/scai">@scai</a>: Statt opening_data kann man auch mit Conditional Restrictions (deutsch: bedingte Beschränkungen) arbeiten. <a href="https://wiki.openstreetmap.org/wiki/DE:Conditional_restrictions">https://wiki.openstreetmap.org/wiki/DE:Conditional_restrictions</a></p>
</div>
<div id="comment-45793-info" class="comment-info">
<span class="comment-age">(07 Oct '15, 17:32)</span> <span class="comment-user userinfo">Nakaner</span>
</div>
</div>
</div>
<div id="comment-tools-45653" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45653-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="45672"></span>

<div id="answer-container-45672" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45672-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45672-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45672-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Osmand beherrscht bisher nur die Sperrung eines Streckenabschnitts, wenn bereits eine Route mit Start und Ziel berechnet wurde. In dem Menü zur berechneten Strecke kann man dann über das Baustellensymbol einen Punkt auf der Karte auswählen, der eine Sperrung auf der hoffentlich naheliegenden Straße berücksichtigt, es erfolgt umgehend eine Neuberechnung.</p>
<p>Leider speichert Osmand bisher diese Sperrungen nicht ab, also muss man eine Sperrung bisher immer neu angeben.</p>
<p>Eventuell beherrscht Mapfactor Navigator Free eine längere Benutzerdefinierte Sperrung von einzelnen Straßen, habs aber noch nicht ausprobiert.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Sep '15, 17:19</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-45672" class="comments-container">
<span id="45673"></span>
<div id="comment-45673" class="comment">
<div id="post-45673-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>du meinst Sperrungen, die der OsmAnd-Benutzer nur für sich (und nicht in die allgemeinen OSM-Daten) einträgt? Deutlich verschieden also von scais (anscheinendem) Verständnis der Frage.</p>
</div>
<div id="comment-45673-info" class="comment-info">
<span class="comment-age">(30 Sep '15, 20:42)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-45672" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45672-form-container" class="comment-form-container">
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

