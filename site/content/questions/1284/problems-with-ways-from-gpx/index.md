+++
type = "question"
title = "Problems with ways from gpx"
description = '''I recently created two new trails from gpx files I recorded on my gps. After uploading the gpx files, I converted them to ways, joined them to existing trails, changed the attributes to footpath and then unlocked them. Everything seemed to work ok. When I view the area, though, they behave oddly. Th...'''
date = "2010-10-23T15:46:00Z"
lastmod = "2010-10-24T12:46:00Z"
weight = 1284
keywords = [ "way", "gpx", "waypoint", "visibility", "zoom" ]
aliases = [ "/questions/1284" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Problems with ways from gpx](/questions/1284/problems-with-ways-from-gpx)

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
<span id="post-1284-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1284-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-1284-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I recently created two new trails from gpx files I recorded on my gps. After uploading the gpx files, I converted them to ways, joined them to existing trails, changed the attributes to footpath and then unlocked them. Everything seemed to work ok. When I view the area, though, they behave oddly. They are visible at some zoom levels but not others. And at some magnifications they appear as broken segments with sections missing. Did I do something wrong or is there another step I need to take? The edits are #6145636 and #6145318. They show up as "still editing." Is that a problem?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-waypoint" rel="tag" title="see questions tagged &#39;waypoint&#39;">waypoint</span> <span class="post-tag tag-link-visibility" rel="tag" title="see questions tagged &#39;visibility&#39;">visibility</span> <span class="post-tag tag-link-zoom" rel="tag" title="see questions tagged &#39;zoom&#39;">zoom</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Oct '10, 15:46</strong></p>
<img src="https://secure.gravatar.com/avatar/958a320e0d82334feb45b1a6913a98b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mdougm&#39;s gravatar image" />
<p><span>mdougm</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mdougm has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Oct '10, 15:29</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span></p>
</div>
</div>
<div id="comments-container-1284" class="comments-container">
&#10;</div>
<div id="comment-tools-1284" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1284-form-container" class="comment-form-container">
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

<span id="1285"></span>

<div id="answer-container-1285" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1285-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1285-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-1285-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The mapnik map layer takes some time to render all the tiles. During this time you can experience that some tiles are rendered with the new data and some with the old. This can cause all the symptoms. Just wait a couple of hours before the whole area is rerendered with the new data.</p>
<p>As to the "still editing" on the changesets, it is because potlatch has not closed the changeset as it has no way to know you are done editing. After one hour of inactivity the changesets will get closed automaticly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Oct '10, 16:10</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Oct '10, 19:33</strong> </span></p>
</div>
</div>
<div id="comments-container-1285" class="comments-container">
<span id="1288"></span>
<div id="comment-1288" class="comment">
<div id="post-1288-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Potlatch can't automatically close the changeset when you end your session, because this is simply done by the user closing their browser window (as a result of which Potlatch will stop executing). If you want to close the changeset manually, not that it really makes much difference, you can choose 'Close changeset' from the Advanced menu or press C.</p>
</div>
<div id="comment-1288-info" class="comment-info">
<span class="comment-age">(23 Oct '10, 18:02)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-1285" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1285-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1293"></span>

<div id="answer-container-1293" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1293-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1293-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-1293-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The render processes that are behind the map display at <a href="http://www.openstreetmap.org">www.openstreetmap.org</a> always need some time to render each tile in all the zoom levels you can choose after you added or modified the data. Sometimes the render job is done in seconds, mostly in minutes, but it might even take hours or days when there is some trouble on the servers or when they are overcrowded.</p>
<p>There is one way to be sure whether your data has arrived on the main OSM data server after your editing:</p>
<p>go to <a href="http://www.openstreetmap.org">www.openstreetmap.org</a>, choose the area you have been working on ans click on the white plus-symbol (+) at the upper right corner of the screen.</p>
<p>Besides you can choose the renderer to display the map, you can choose the "data layer" to display the objects in the OSM data as they are in the data in the right moment now.</p>
<p>There you can check your recently added objects about their position and tagging.</p>
<p>(More details at <a href="http://wiki.openstreetmap.org/wiki/Data_layer"></a><a href="http://wiki.openstreetmap.org/wiki/Data_layer"></a><a href="http://wiki.openstreetmap.org/wiki/Data_layer">http://wiki.openstreetmap.org/wiki/Data_layer</a>)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Oct '10, 12:46</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Oct '10, 13:16</strong> </span></p>
</div>
</div>
<div id="comments-container-1293" class="comments-container">
&#10;</div>
<div id="comment-tools-1293" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1293-form-container" class="comment-form-container">
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

