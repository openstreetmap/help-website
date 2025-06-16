+++
type = "question"
title = "National park not rendered in standard layer"
description = '''Yesterday I found out that somebody traced the boundary of Parco Nazionale del Vesuvio, near Naples: https://www.openstreetmap.org/way/199207733#map=14/40.7895/14.4613. But it was not rendered on the standard OSM layer, and I realized that the way lacked of some tags that can be found in similar park...'''
date = "2014-12-11T12:20:00Z"
lastmod = "2014-12-11T19:47:00Z"
weight = 39214
keywords = [ "national_park", "mapnik", "tagging" ]
aliases = [ "/questions/39214" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [National park not rendered in standard layer](/questions/39214/national-park-not-rendered-in-standard-layer)

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
<span id="post-39214-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39214-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-39214-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Yesterday I found out that somebody traced the boundary of Parco Nazionale del Vesuvio, near Naples: <a href="https://www.openstreetmap.org/way/199207733#map=14/40.7895/14.4613">https://www.openstreetmap.org/way/199207733#map=14/40.7895/14.4613</a>. But it was not rendered on the standard OSM layer, and I realized that the way lacked of some tags that can be found in similar parks, so I fixed it - or I think so, at least. After almost one day, it is not rendered yet, whereas more recent edits not far from it are. How come?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-national_park" rel="tag" title="see questions tagged &#39;national_park&#39;">national_park</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Dec '14, 12:20</strong></p>
<img src="https://secure.gravatar.com/avatar/0e00cf7b1db1273b37a075c54b383d02?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Decan&#39;s gravatar image" />
<p><span>Decan</span><br />
<span class="score" title="351 reputation points">351</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Decan has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Dec '14, 12:21</strong> </span></p>
</div>
</div>
<div id="comments-container-39214" class="comments-container">
&#10;</div>
<div id="comment-tools-39214" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39214-form-container" class="comment-form-container">
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

<span id="39227"></span>

<div id="answer-container-39227" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-39227-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-39227-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-39227-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Decan has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/1141">known problem</a> with the standard OSM rendering style and is currently under investigation. <strong>Relations</strong> tagged with <code>boundary=national_park</code> will be rendered, but <strong>ways</strong> won't, such as in your example.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Dec '14, 19:47</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-39227" class="comments-container">
&#10;</div>
<div id="comment-tools-39227" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-39227-form-container" class="comment-form-container">
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

