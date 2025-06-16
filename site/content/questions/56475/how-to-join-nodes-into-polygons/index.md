+++
type = "question"
title = "How to join nodes into polygons?"
description = '''I&#x27;m using JOSM and can&#x27;t seem to figure out how to make my nodes into polygons-- so when I tag things, every node has the building icon, instead of the center of the shape. I have 100+ shapes, so want to do this in bulk. These are closed shapes coming from a shapefile. Trying to upload a buildings l...'''
date = "2017-06-06T19:16:00Z"
lastmod = "2017-06-07T10:30:00Z"
weight = 56475
keywords = [ "josm", "buildings", "nodes", "relations", "polygons" ]
aliases = [ "/questions/56475" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to join nodes into polygons?](/questions/56475/how-to-join-nodes-into-polygons)

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
<span id="post-56475-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56475-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56475-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm using JOSM and can't seem to figure out how to make my nodes into polygons-- so when I tag things, every node has the building icon, instead of the center of the shape. I have 100+ shapes, so want to do this in bulk. These are closed shapes coming from a shapefile. Trying to upload a buildings layer that was digitized for a project at the planning/design firm where I work. Sorry for a potentially stupid question. Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-buildings" rel="tag" title="see questions tagged &#39;buildings&#39;">buildings</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-polygons" rel="tag" title="see questions tagged &#39;polygons&#39;">polygons</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jun '17, 19:16</strong></p>
<img src="https://secure.gravatar.com/avatar/730ad8c39310f07e94e2ddba846a1a9e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="corinne_j&#39;s gravatar image" />
<p><span>corinne_j</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="corinne_j has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Jun '17, 19:17</strong> </span></p>
</div>
</div>
<div id="comments-container-56475" class="comments-container">
&#10;</div>
<div id="comment-tools-56475" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56475-form-container" class="comment-form-container">
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

<span id="56488"></span>

<div id="answer-container-56488" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56488-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56488-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56488-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could first select the shapes (e.g. with the lasso tool), then select way nodes (CMD-N on Mac, I guess CTRL-N on PC), then just add the tag building=yes. Please do not upload this to the OSM database, it is incorrect.</p>
<p>The above does not turn the nodes in polygons, it just adds a tag to the nodes. JOSM's renderer will then show building icons on all nodes. This is also incorrect tagging in OSM. Nodes should not have this tag, but (multi-)polygons do. Buildings are represented by (multi-) polygons. In some cases isolated nodes can represent buildings, but never nodes belonging to a polygon not.</p>
<p>What you are trying to achieve seems odd, so it is very well possible that I misunderstood you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '17, 04:16</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-56488" class="comments-container">
<span id="56493"></span>
<div id="comment-56493" class="comment">
<div id="post-56493-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>or do you want to select only the ways ? In that case, use the lasso or rectangle to select all nodes and ways in an area, then press Shift-U to deselect the nodes and keep the ways selected</p>
</div>
<div id="comment-56493-info" class="comment-info">
<span class="comment-age">(07 Jun '17, 10:30)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-56488" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56488-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="56489"></span>

<div id="answer-container-56489" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56489-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56489-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56489-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi</p>
<p>Are you selecting all the nodes with Ctrl + A? If you do, then adding tags will apply to all the nodes. What you require is to select each way and provide tags for them. To do that, you can select all by pressing Ctrl + A and then press Shift + E to select only the ways and then add tags.</p>
<p>However there are restrictions regarding imports. Before you do any, kindly read the guidelines: <a href="https://wiki.openstreetmap.org/wiki/Import">https://wiki.openstreetmap.org/wiki/Import</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '17, 06:36</strong></p>
<img src="https://secure.gravatar.com/avatar/c482180b767d07897d150d7b426ca4e0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmahmud&#39;s gravatar image" />
<p><span>mmahmud</span><br />
<span class="score" title="638 reputation points">638</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmahmud has one accepted answer">3%</span></p>
</div>
</div>
<div id="comments-container-56489" class="comments-container">
&#10;</div>
<div id="comment-tools-56489" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56489-form-container" class="comment-form-container">
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

