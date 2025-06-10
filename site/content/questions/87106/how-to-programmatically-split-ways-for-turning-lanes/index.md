+++
type = "question"
title = "How to programmatically split ways for turning lanes?"
description = '''I would like to split the ways in my OSM data that contain turn lane information. For example, if a way has 3 lanes, but 4 turn lanes, I want to split the way into 2, with a 4-lane section at the end of the road (perhaps using the last 2 geometry points) I wonder if anyone has any suggestions on how...'''
date = "2023-04-13T09:36:00Z"
lastmod = "2023-04-21T15:37:00Z"
weight = 87106
keywords = [ "ways", "split", "programing", "turnlanes" ]
aliases = [ "/questions/87106" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to programmatically split ways for turning lanes?](/questions/87106/how-to-programmatically-split-ways-for-turning-lanes)

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
<span id="post-87106-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87106-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87106-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to split the ways in my OSM data that contain turn lane information. For example, if a way has 3 lanes, but 4 turn lanes, I want to split the way into 2, with a 4-lane section at the end of the road (perhaps using the last 2 geometry points)</p>
<p>I wonder if anyone has any suggestions on how this might be done programmatically?</p>
<p>I am using the OSM data as an input to build a network in traffic simulator <a href="https://www.eclipse.org/sumo/">SUMO</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-split" rel="tag" title="see questions tagged &#39;split&#39;">split</span> <span class="post-tag tag-link-programing" rel="tag" title="see questions tagged &#39;programing&#39;">programing</span> <span class="post-tag tag-link-turnlanes" rel="tag" title="see questions tagged &#39;turnlanes&#39;">turnlanes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Apr '23, 09:36</strong></p>
<img src="https://secure.gravatar.com/avatar/84bb2b757c48fde0ecb9f1d32eab3028?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gladegan&#39;s gravatar image" />
<p><span>gladegan</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gladegan has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87106" class="comments-container">
<span id="87109"></span>
<div id="comment-87109" class="comment">
<div id="post-87109-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I may be hopelessly naive here (not familiar with SUMO), but it seems to me like the correct place to do this programmatically would be in the converter from OSM format to SUMO format as described in <a href="https://github.com/eclipse/sumo/issues/1990">this issue</a> on their GitHub? From <a href="https://github.com/eclipse/sumo/issues/12978">this</a> later issue and <a href="https://sumo.dlr.de/docs/Networks/Import/OpenStreetMap.html#lane-to-lane_connections">some of the docs</a>, it looks like it might have been implemented?</p>
</div>
<div id="comment-87109-info" class="comment-info">
<span class="comment-age">(13 Apr '23, 15:12)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="87151"></span>
<div id="comment-87151" class="comment">
<div id="post-87151-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, thanks for replying. As far as I understand, SUMO reads turn lane information and applies them to the indicated number of lanes. If the number of lanes is 1 and the number of turn lanes is 2, the turn lanes are not applied.</p>
<p>An example here: <a href="https://www.openstreetmap.org/way/1121159178">https://www.openstreetmap.org/way/1121159178</a></p>
<p>I would like to split such a way into 2 parts, where the turning part has the right number of turning lanes.</p>
</div>
<div id="comment-87151-info" class="comment-info">
<span class="comment-age">(21 Apr '23, 15:37)</span> <span class="comment-user userinfo">gladegan</span>
</div>
</div>
</div>
<div id="comment-tools-87106" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87106-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

