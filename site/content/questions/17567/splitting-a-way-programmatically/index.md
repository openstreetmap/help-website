+++
type = "question"
title = "splitting a way programmatically"
description = '''Hello all! I am programatically reading an osm file and save the nodes and ways and ways to node relationsship in a sql server database. I have a need to be able to split a way into multiple ways, depending if they intersect another way. If a way intersects two other ways, then I need to split it in...'''
date = "2012-11-07T21:15:00Z"
lastmod = "2012-11-09T13:55:00Z"
weight = 17567
keywords = [ "intersection", "osm" ]
aliases = [ "/questions/17567" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [splitting a way programmatically](/questions/17567/splitting-a-way-programmatically)

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
<span id="post-17567-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17567-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17567-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello all! I am programatically reading an osm file and save the nodes and ways and ways to node relationsship in a sql server database. I have a need to be able to split a way into multiple ways, depending if they intersect another way. If a way intersects two other ways, then I need to split it into three differnt ways. From starting point to the intersection point of the first way it intersect. from the intersection point of the first way it intersections to the intersection point of the second way it intersects and then from the intersection point with the second way to the end of the way.</p>
<p>My question is this. Is there any tags for a given way or the nodes that make it up that tell me it is an intersection point? I dont recognize any node tags. Has anyone done this?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-intersection" rel="tag" title="see questions tagged &#39;intersection&#39;">intersection</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Nov '12, 21:15</strong></p>
<img src="https://secure.gravatar.com/avatar/343237842fce1f7a82f69ebf7a92f6b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kcjailbirds&#39;s gravatar image" />
<p><span>kcjailbirds</span><br />
<span class="score" title="141 reputation points">141</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kcjailbirds has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17567" class="comments-container">
&#10;</div>
<div id="comment-tools-17567" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17567-form-container" class="comment-form-container">
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

<span id="17571"></span>

<div id="answer-container-17571" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17571-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17571-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17571-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am assuming that you want to detect actual intersection nodes, i.e. nodes that are shared between more than one way and are not the start or end node for the ways that share the node.</p>
<p>Without pre-processing, there is no way to detect those, because the way objects do not possess geometry, only the nodes do. So you would at least keep all the node IDs in memory or in a temporary file and then check for each way member node whether that node is also used by another way.</p>
<p>If you import your OSM file into an Osmosis <a href="https://wiki.openstreetmap.org/wiki/Database_schema#Database_Schemas">schema</a> PostGIS database, you will find the way_nodes table useful for checking intersections.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Nov '12, 22:48</strong></p>
<img src="https://secure.gravatar.com/avatar/acea3c9fd5908d7ff09596d16b8724d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mvexel&#39;s gravatar image" />
<p><span>mvexel</span><br />
<span class="score" title="762 reputation points">762</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mvexel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17571" class="comments-container">
<span id="17574"></span>
<div id="comment-17574" class="comment">
<div id="post-17574-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. I am looking for actual intersections were some could be at the end or begining of a way and some could be in the middle. You suggestion is just what I was thinking to do. Just wanted to see if there was an easier way.</p>
</div>
<div id="comment-17574-info" class="comment-info">
<span class="comment-age">(08 Nov '12, 00:50)</span> <span class="comment-user userinfo">kcjailbirds</span>
</div>
</div>
</div>
<div id="comment-tools-17571" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17571-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17583"></span>

<div id="answer-container-17583" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17583-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17583-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17583-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Assume you have extracted/created all the poly-lines in accordance with ways-nodes relations. From that point your question may be understood more generally than the former answer is suggesting. Namely, you are looking for a function that converts a set of poly-lines into a set of simple poly-lines (a simple poly-line has no common point with any other poly-line except maybe the end-points). But then, if a crossing point can be anywhere on poly-lines the issue is more complex and complicated. I am not shore you can find standard and open-source solution to it (you know, any computer calculated crossing of two vectors/straight line segments is never on any of them except maybe in some trivial cases). At the same time, the mentioned function is essential in vector map data preparation phase (e.g. finding a simple area coverage for complicated area structures with overlaps or like a hole having a common border section with container/outer border, or even slightly crossing it, or when recognizing wrong/not tagged roundabouts in a road class and so on). So, if you don’t mind, here is a model how I/we handle your issue: First, we decompose all poly-lines into single (independent) vectors. Next, any crossing or overlapping vectors are divided into none-crossing and none overlapping vectors. So, neighboring vectors (those having one and only one common end-point) are linear-connected to (simple) poly-lines again. Finally, there are some cosmetic updates regarding orientations, name assignments, rule assignments and so on. Now, these poly-lines are what you are looking for. The whole poly_lines-to-simple-poly_lines (how we call it) process takes some seconds or minutes (in case of huge data-sets like the Planet forests, river-lines…) on a medium strong laptop.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Nov '12, 11:53</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-17583" class="comments-container">
<span id="17588"></span>
<div id="comment-17588" class="comment">
<div id="post-17588-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for the detailed explaination. This solution seems very complicated but it might be the only way to go! Do you have any sample code on how you have or would do this?</p>
</div>
<div id="comment-17588-info" class="comment-info">
<span class="comment-age">(08 Nov '12, 16:30)</span> <span class="comment-user userinfo">kcjailbirds</span>
</div>
</div>
<span id="17608"></span>
<div id="comment-17608" class="comment">
<div id="post-17608-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Pretty interested in this as well, if you're willing to share any code examples...cheers!</p>
</div>
<div id="comment-17608-info" class="comment-info">
<span class="comment-age">(09 Nov '12, 13:55)</span> <span class="comment-user userinfo">Csc</span>
</div>
</div>
</div>
<div id="comment-tools-17583" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17583-form-container" class="comment-form-container">
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

