+++
type = "question"
title = "OSM routing - turning one way into an edge"
description = '''I&#x27;m building my own routing engine - which means I&#x27;m not using any of the routing frameworks for OSM.  So far I&#x27;ve built a graph with edges and vertices. I&#x27;m parsing all the ways that are highways (I&#x27;m not taking areas). My question is: how can turn a way into an edge (with one only two nodes, one d...'''
date = "2015-02-06T15:23:00Z"
lastmod = "2015-02-06T17:06:00Z"
weight = 40827
keywords = [ "development", "graph", "routing", "parsing" ]
aliases = [ "/questions/40827" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM routing - turning one way into an edge](/questions/40827/osm-routing-turning-one-way-into-an-edge)

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
<span id="post-40827-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40827-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40827-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm <a href="/questions/38328/building-a-graph-out-of-osm-xml">building my own routing engine</a> - which means I'm not using any of the routing frameworks for OSM.</p>
<p>So far I've built a graph with edges and vertices.</p>
<p>I'm parsing all the ways that are highways (I'm not taking areas).</p>
<p><em>My question is:</em> how can turn a way into an edge (with one only two nodes, one defining the start and one defining the end) and remove all the ones in the middle? What approach has developers taken with this problem?</p>
<p>Thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-graph" rel="tag" title="see questions tagged &#39;graph&#39;">graph</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-parsing" rel="tag" title="see questions tagged &#39;parsing&#39;">parsing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Feb '15, 15:23</strong></p>
<img src="https://secure.gravatar.com/avatar/a759928a25662633a5d3ba0288eb1561?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="echoalphapapa&#39;s gravatar image" />
<p><span>echoalphapapa</span><br />
<span class="score" title="41 reputation points">41</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="echoalphapapa has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Feb '15, 15:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-40827" class="comments-container">
&#10;</div>
<div id="comment-tools-40827" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40827-form-container" class="comment-form-container">
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

<span id="40828"></span>

<div id="answer-container-40828" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40828-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40828-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40828-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You could of course have a look at the existing routing engines which you don't want to use, each of which have solved that problem in one way or the other.</p>
<p>The question that you have been linked to in the post you reference above actually contains the answer. Re-read it: <a href="https://help.openstreetmap.org/questions/19213/how-can-i-convert-an-osm-xml-file-into-a-graph-representation">How can I convert an OSM XML file into a graph representation?</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Feb '15, 15:46</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Feb '15, 15:48</strong> </span></p>
</div>
</div>
<div id="comments-container-40828" class="comments-container">
<span id="40829"></span>
<div id="comment-40829" class="comment">
<div id="post-40829-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was looking for an explanation that's a bit more low level.</p>
</div>
<div id="comment-40829-info" class="comment-info">
<span class="comment-age">(06 Feb '15, 15:59)</span> <span class="comment-user userinfo">echoalphapapa</span>
</div>
</div>
<span id="40830"></span>
<div id="comment-40830" class="comment">
<div id="post-40830-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you be more specific? Which parts are unclear to you? Where are you stuck?</p>
</div>
<div id="comment-40830-info" class="comment-info">
<span class="comment-age">(06 Feb '15, 17:06)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-40828" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40828-form-container" class="comment-form-container">
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

