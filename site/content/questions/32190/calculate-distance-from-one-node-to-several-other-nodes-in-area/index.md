+++
type = "question"
title = "Calculate distance from one node to several other nodes in area"
description = '''Hi all, first of all, I am not expecting a complete solution to my following problem but for someone to point me in the right direction would be much appreciated as I am new to OSM and programming in general. What I am trying to do, is calculating the distance from one given node to several nodes ar...'''
date = "2014-04-08T08:36:00Z"
lastmod = "2014-04-08T15:55:00Z"
weight = 32190
keywords = [ "distance", "routing" ]
aliases = [ "/questions/32190" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Calculate distance from one node to several other nodes in area](/questions/32190/calculate-distance-from-one-node-to-several-other-nodes-in-area)

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
<span id="post-32190-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32190-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32190-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>first of all, I am not expecting a complete solution to my following problem but for someone to point me in the right direction would be much appreciated as I am new to OSM and programming in general.</p>
<p>What I am trying to do, is calculating the distance from one given node to several nodes around that one (e.g. The routing distance from point A to all pubs within a 1000m radius)</p>
<p>I do not need a graphical display on a map, but only the data of what nodes are in the area and distances to each.</p>
<p>Identifying the relevant nodes I did on <a href="http://overpass-turbo.eu">http://overpass-turbo.eu</a> with a &lt;around radius="xxx"/&gt; command. So the next step would be to use the data found with the "around" command to calculate distances.</p>
<p>If anyone could point me toward a program which makes this possible it would really help me a lot!</p>
<p>Thanks in advance!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-distance" rel="tag" title="see questions tagged &#39;distance&#39;">distance</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Apr '14, 08:36</strong></p>
<img src="https://secure.gravatar.com/avatar/26b660ce523769d2f7f3173a731b881c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="qotsa&#39;s gravatar image" />
<p><span>qotsa</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="qotsa has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-32190" class="comments-container">
<span id="32193"></span>
<div id="comment-32193" class="comment">
<div id="post-32193-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Do you want a routed distance or are you happy with a crow's flight distance. The answers are significantly different, with the former being more complex.</p>
</div>
<div id="comment-32193-info" class="comment-info">
<span class="comment-age">(08 Apr '14, 10:53)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-32190" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32190-form-container" class="comment-form-container">
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

<span id="32205"></span>

<div id="answer-container-32205" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32205-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32205-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-32205-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want to calculate distances by goinmg via existing ways in the OSM data, see <a href="http://wiki.openstreetmap.org/wiki/Routing">Routing</a> in the OSM wiki.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Apr '14, 15:55</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-32205" class="comments-container">
&#10;</div>
<div id="comment-tools-32205" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32205-form-container" class="comment-form-container">
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

