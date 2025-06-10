+++
type = "question"
title = "Download POI aus OSM Planetfile"
description = '''Hallo Forums-Mitglieder, ich danke Euch bereits für die Mithilfe. Ich benötige Kartenmaterial zu einer Auswahl an selbst definierten POI wie bspw. &quot;Schützenverein&quot; oder &quot;Kino&quot; für die Bundesrepublik Deutschland. Ist es technisch möglich entsprechende Geodaten aus dem Planetfile von OSM zu generieren...'''
date = "2017-02-15T14:29:00Z"
lastmod = "2017-02-15T15:08:00Z"
weight = 54649
keywords = [ "download", "poi" ]
aliases = [ "/questions/54649" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Download POI aus OSM Planetfile](/questions/54649/download-poi-aus-osm-planetfile)

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
<span id="post-54649-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54649-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54649-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hallo Forums-Mitglieder,</p>
<p>ich danke Euch bereits für die Mithilfe. Ich benötige Kartenmaterial zu einer Auswahl an selbst definierten POI wie bspw. "Schützenverein" oder "Kino" für die Bundesrepublik Deutschland. Ist es technisch möglich entsprechende Geodaten aus dem Planetfile von OSM zu generieren? Falls ja, bitte ich um eine kurze Beschreibung.</p>
<p>Danke</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Feb '17, 14:29</strong></p>
<img src="https://secure.gravatar.com/avatar/8bcddb3cf318b9ad33a8b52fe5c76629?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KevinM1989&#39;s gravatar image" />
<p><span>KevinM1989</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KevinM1989 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54649" class="comments-container">
&#10;</div>
<div id="comment-tools-54649" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54649-form-container" class="comment-form-container">
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

<span id="54650"></span>

<div id="answer-container-54650" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54650-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54650-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-54650-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Ja, mit Programmen wie "osmfilter", "osmosis" oder "osmgrep" kannst Du aus einem Planetfile (oder einem Deutschland-Extrakt) bestimmte Objekte herausfiltern. Allerdings können POIs in OSM verschiedene Gestalten haben , und der Rückschluss auf die Geometrie ist manchmal mit Indirektionen verbunden (z.B. das Kino ist in OSM ein Objekt vom Typ Relation, dies verweist auf Objekte vom Typ Way, diese verweisen auf Objekte vom Typ Node, und erst an denen erkennt man, ob das Kino in München oder in Hamburg ist).</p>
<p>Alternativen sind der Online-Dienst "Overpass Turbo", der Dir die Resultate auch gleich als GeoJSON aufbereiten kann, oder der Import der OSM-Daten in eine PostGIS mit osm2pgsql, wo Du dann beliebige Abfragen starten kannst und die Geometrien auch bereits für Dich zusammengebaut sind.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Feb '17, 15:08</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-54650" class="comments-container">
&#10;</div>
<div id="comment-tools-54650" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54650-form-container" class="comment-form-container">
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

