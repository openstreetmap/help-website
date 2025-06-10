+++
type = "question"
title = "move a tag"
description = '''I&#x27;ve want to move a traffic light by dragging( is in the wrong position). But in Potlatch and ID, it drags the road away with.  How exactly can I move the tag alone?'''
date = "2014-04-25T14:21:00Z"
lastmod = "2014-04-25T17:04:00Z"
weight = 32634
keywords = [ "move", "tags" ]
aliases = [ "/questions/32634" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [move a tag](/questions/32634/move-a-tag)

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
<span id="post-32634-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32634-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32634-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've want to move a traffic light by dragging( is in the wrong position). But in Potlatch and ID, it drags the road away with. How exactly can I move the tag alone?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-move" rel="tag" title="see questions tagged &#39;move&#39;">move</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Apr '14, 14:21</strong></p>
<img src="https://secure.gravatar.com/avatar/13c853bf8740f6310151023d9ca5e3a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bummibaer&#39;s gravatar image" />
<p><span>Bummibaer</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bummibaer has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-32634" class="comments-container">
&#10;</div>
<div id="comment-tools-32634" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32634-form-container" class="comment-form-container">
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

<span id="32635"></span>

<div id="answer-container-32635" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32635-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32635-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-32635-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Bummibaer has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It seems as if the node of traffic light in question is actually part of the road. The simple way to fix your problem is to create a new node and add the tags from the original one to the new one (and remove them from the old node). Doing it this way has the disadvantage of losing the history of the old node.</p>
<p>JOSM has a dedicated "detach" node function that does it the "proper" way, you can emulate this in iD by:</p>
<ul>
<li>adding a node on both sides of the traffic light on the way</li>
<li>spliting and unjoining the way at both new nodes</li>
<li>moving the three node way you now have out of the way and joining the original way again</li>
<li>removing the end points from the three node way, leaving you with the traffic light node</li>
</ul>
<p>I wouldn't :-)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Apr '14, 14:46</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-32635" class="comments-container">
<span id="32636"></span>
<div id="comment-32636" class="comment">
<div id="post-32636-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi thanks! I will try it.</p>
</div>
<div id="comment-32636-info" class="comment-info">
<span class="comment-age">(25 Apr '14, 14:47)</span> <span class="comment-user userinfo">Bummibaer</span>
</div>
</div>
<span id="32637"></span>
<div id="comment-32637" class="comment">
<div id="post-32637-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>Note you should check if what you want to do is actually compatible with <a href="http://wiki.openstreetmap.org/wiki/Tag:highway=traffic_signals">http://wiki.openstreetmap.org/wiki/Tag:highway=traffic_signals</a> which in general assumes that the signal is mapped on the actual way.</p>
</div>
<div id="comment-32637-info" class="comment-info">
<span class="comment-age">(25 Apr '14, 15:05)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="32638"></span>
<div id="comment-32638" class="comment">
<div id="post-32638-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>In OSM we usually prefer to map the signal's effect (which is to stop traffic, and implies placing it on a way's node) rather than the physical object (of which there can be many for a single stop location).</p>
<p>The reason for this (appart from avoiding too micro a mapping) is that it would be very hard for routing engines to use the traffic signal information if it wasn't placed on the way being routed.</p>
<p>I wouldn't move the traffic signal off the way unless you understand very well what you're doing.</p>
</div>
<div id="comment-32638-info" class="comment-info">
<span class="comment-age">(25 Apr '14, 15:58)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="32639"></span>
<div id="comment-32639" class="comment">
<div id="post-32639-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have to strongly agree with vincent-de-phily on this: Don't remove the tag from the highway! One of the main "rendering" (i.e. users) of OSM data are routing engines which use this information to determine the best route. By adding highway=stop, highway=give_way and highway=traffic_signal tags to appropriate nodes on highways routing engines can make a better decisions on a good route.</p>
<p>See also: <a href="http://wiki.openstreetmap.org/wiki/Tag:highway%3Dtraffic_signals#Complex_intersections">http://wiki.openstreetmap.org/wiki/Tag:highway%3Dtraffic_signals#Complex_intersections</a></p>
<p>If you must, add a separate node in the actual physical location for a map image renderer.</p>
</div>
<div id="comment-32639-info" class="comment-info">
<span class="comment-age">(25 Apr '14, 17:04)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
</div>
<div id="comment-tools-32635" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32635-form-container" class="comment-form-container">
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

