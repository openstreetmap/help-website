+++
type = "question"
title = "Distribution of the Nodes"
description = '''Hi, I&#x27;d like to know if there is any standard for node distribution in any way for the OSM. More specifically, I know that ways are created from points(nodes). However, is there any limitation for the position or (distance) of the next node?  Ex: Say, I have a way, and it consists of 6 nodes. Is the...'''
date = "2022-02-08T15:19:00Z"
lastmod = "2022-02-08T16:35:00Z"
weight = 83405
keywords = [ "ways", "nodes", "osm" ]
aliases = [ "/questions/83405" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Distribution of the Nodes](/questions/83405/distribution-of-the-nodes)

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
<span id="post-83405-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83405-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83405-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'd like to know if there is any standard for node distribution in any way for the OSM. More specifically, I know that ways are created from points(nodes). However, is there any limitation for the position or (distance) of the next node? Ex: Say, I have a way, and it consists of 6 nodes. Is there any limitation for the distribution of these nodes? Is it possible to have 3. node very near to 4. node or 2. node? In contrast, is it possible to have 3. node quite far from the 2. node?</p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Feb '22, 15:19</strong></p>
<img src="https://secure.gravatar.com/avatar/761de0d6d13397df82446f39cf1098b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alisvndk88&#39;s gravatar image" />
<p><span>alisvndk88</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alisvndk88 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83405" class="comments-container">
&#10;</div>
<div id="comment-tools-83405" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83405-form-container" class="comment-form-container">
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

<span id="83406"></span>

<div id="answer-container-83406" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83406-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-83406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In general it depends on the shape and complexity of the object (or part of an object) in the real world that the way represents, e.g.</p>
<ul>
<li>A long completely straight stretch of road may have 2 nodes a long distance apart</li>
<li>A roundabout may have a large number of nodes to approximately represent a circle</li>
<li>A building with a simple rectangular shape may be drawn with just 4 nodes</li>
<li>A building of the same size but with various protruding parts may need many more nodes.</li>
</ul>
<p>Even within all those, it will also depend on the precision of the source that mappers are using, and to some extent on the personal taste of the mappers. There are no universal rules, for example, about how many nodes are needed to represent a curve in a road.</p>
<p>If you have a specific application in mind that has prompted this question, we might be able to give further guidance beyond my generic answer above.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Feb '22, 15:59</strong></p>
<img src="https://secure.gravatar.com/avatar/8da3fc19d7250ff5fbdbcbf467f9458f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alan_gr&#39;s gravatar image" />
<p><span>alan_gr</span><br />
<span class="score" title="2623 reputation points"><span>2.6k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="45 badges"><span class="bronze">●</span><span class="badgecount">45</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alan_gr has 10 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Feb '22, 16:00</strong> </span></p>
</div>
</div>
<div id="comments-container-83406" class="comments-container">
<span id="83409"></span>
<div id="comment-83409" class="comment">
<div id="post-83409-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the info. I'm trying to estimate the curvature using nodes using 3 points(menger curvature). But, due to distributions, it is not accurate as I expected.</p>
</div>
<div id="comment-83409-info" class="comment-info">
<span class="comment-age">(08 Feb '22, 16:35)</span> <span class="comment-user userinfo">alisvndk88</span>
</div>
</div>
</div>
<div id="comment-tools-83406" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83406-form-container" class="comment-form-container">
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

