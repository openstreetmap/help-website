+++
type = "question"
title = "Richtige Richtung eines Way"
description = '''Hi, immer wieder lese ich im Forum von der Richtung eines Way bzw. von einer falschen Richtung bzw. von unumkehrbare Ways. Was ist die richtige Richtung ?'''
date = "2013-07-22T09:41:00Z"
lastmod = "2013-07-22T12:14:00Z"
weight = 24432
keywords = [ "way", "lang-de" ]
aliases = [ "/questions/24432" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Richtige Richtung eines Way](/questions/24432/richtige-richtung-eines-way)

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
<span id="post-24432-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24432-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24432-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, immer wieder lese ich im Forum von der Richtung eines Way bzw. von einer falschen Richtung bzw. von unumkehrbare Ways.</p>
<p>Was ist die richtige Richtung ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span> <span class="post-tag tag-link-lang-de" rel="tag" title="see questions tagged &#39;lang-de&#39;">lang-de</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jul '13, 09:41</strong></p>
<img src="https://secure.gravatar.com/avatar/070282c59f23d8268813b03dbc535b27?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cb650cx&#39;s gravatar image" />
<p><span>cb650cx</span><br />
<span class="score" title="184 reputation points">184</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cb650cx has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24432" class="comments-container">
&#10;</div>
<div id="comment-tools-24432" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24432-form-container" class="comment-form-container">
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

<span id="24434"></span>

<div id="answer-container-24434" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24434-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24434-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-24434-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Die Richtung eines Weges ist nur bei bestimmten Eigenschaften von Bedeutung. Dazu zählen vor allem <a href="https://wiki.openstreetmap.org/wiki/DE:Key:oneway">Einbahnstraßen</a> (oneway=yes), bei der sich die Richtung der Einbahnstraße an der Richtung des Weges orientiert. Ähnlich ist es bei der <a href="https://wiki.openstreetmap.org/wiki/DE:Key:incline">Steigung</a> des Weges. Darüber hinaus gibt es auch weitere Tags, die die Eigenschaft einer einzelnen Straßenseite näher beschreiben, wie beispielsweise <a href="http://wiki.openstreetmap.org/wiki/Sidewalks">sidewalk=left/right</a>. Bei Flüssen wiederum gibt die Wegrichtung gleichzeitig die Fließrichtung des Wassers an. Dann gibt es noch <a href="https://wiki.openstreetmap.org/wiki/DE:Relation">Relationen</a>, deren Mitglieder die Rollen <em>forward</em> und <em>backward</em> haben können und auch hier wieder die Richtung des Weges von Bedeutung ist. In all diesen Fällen führt eine Umkehrung der Wegrichtung auch gleichzeitig zu einer Bedeutungsänderung aufgrund der entsprechenden Tags.</p>
<p>Daher sollte man sich vor der Änderung der Wegrichtung immer genau die Tags anschauen. Aber die meisten Editoren bieten hierbei Unterstützung, indem sie einerseits den Benutzer darauf hinweisen, dass das Umkehren bestimmte Tags beeinflusst, und indem sie andererseits den Benutzer fragen, ob auch die Tags umgedreht werden sollen (beispielsweise <em>incline=up</em> zu <em>incline=down</em> oder <em>sidewalk=left</em> zu <em>sidewalk=right</em>). Bei den meisten Wegen ist die Richtung aber vollkommen egal.</p>
<p>Ein <em>unumkehrbar</em> gibt es eigentlich nicht, jeder Weg kann umgekehrt werden. Es kann sich ja auch mal die Richtung einer Einbahnstraße ändern. Aber bei manchen, wenigen Wegen ist das Umkehren überhaupt nicht sinnvoll, beispielsweise bei Flüssen. Außer natürlich der Weg war vorher falschherum eingetragen.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jul '13, 10:05</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-24434" class="comments-container">
<span id="24451"></span>
<div id="comment-24451" class="comment">
<div id="post-24451-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>… und erkennen kann man die Richtung eines Weges wie auf <span>Forward &amp; backward, left &amp; right</span> beschrieben (noch nicht auf Deutsch verfügbar, <a href="http://www.google.com/translate?u=http%3A%2F%2Fwiki.openstreetmap.org%2Fwiki%2FForward_%2526_backward%2C_left_%2526_right&amp;hl=en&amp;ie=UTF8&amp;sl=auto&amp;tl=de">automatische Übersetzung</a>).</p>
</div>
<div id="comment-24451-info" class="comment-info">
<span class="comment-age">(22 Jul '13, 12:14)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-24434" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24434-form-container" class="comment-form-container">
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

