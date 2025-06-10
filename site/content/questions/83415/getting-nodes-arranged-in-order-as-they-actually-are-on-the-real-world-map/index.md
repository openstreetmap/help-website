+++
type = "question"
title = "Getting nodes arranged in order as they actually are on  the real world map"
description = '''Hi, in the project that I am currently building, i need series of points (nodes) in orderly manner as i transverse along the way from one point to the other. In other words if I am traversing the way, the nodes need to be in the same order in the map data that they are in reality But when i download...'''
date = "2022-02-08T18:48:00Z"
lastmod = "2022-02-09T09:00:00Z"
weight = 83415
keywords = [ "nodes" ]
aliases = [ "/questions/83415" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Getting nodes arranged in order as they actually are on the real world map](/questions/83415/getting-nodes-arranged-in-order-as-they-actually-are-on-the-real-world-map)

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
<span id="post-83415-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83415-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83415-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, in the project that I am currently building, i need series of points (nodes) in orderly manner as i transverse along the way from one point to the other. In other words if I am traversing the way, the nodes need to be in the same order in the map data that they are in reality But when i downloaded the OSM data, some of the nodes did not follow a uniform progression on the along the way.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Feb '22, 18:48</strong></p>
<img src="https://secure.gravatar.com/avatar/d91bc4f974e22ffeb60227442e03aafa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Segunlakata&#39;s gravatar image" />
<p><span>Segunlakata</span><br />
<span class="score" title="16 reputation points">16</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Segunlakata has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-83415" class="comments-container">
&#10;</div>
<div id="comment-tools-83415" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83415-form-container" class="comment-form-container">
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

<span id="83418"></span>

<div id="answer-container-83418" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83418-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83418-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83418-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not sure if I understood your question correctly. The order in which nodes in the downloaded XML file appear is irrelevant. Each way has <code>&lt;nd ref="..."/&gt;</code> elements where all nodes of the way are referenced in the correct order. So in order to determine the correct order of nodes for a way you have to look at this section. For more information see <a href="https://wiki.openstreetmap.org/wiki/OSM_XML">OSM_XML</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Feb '22, 09:00</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-83418" class="comments-container">
&#10;</div>
<div id="comment-tools-83418" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83418-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83417"></span>

<div id="answer-container-83417" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83417-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83417-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83417-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If I'm clear on what you're asking, that is, you need ways having a series of nodes with timestamps progressing in the direction the way was originally drawn, then the answer is no.</p>
<p>That's because a mapper can come along at a later date and add or delete nodes, for example, to improve the accuracy of the way. Also, ways are split and new nodes added for objects like bridges, number of lanes, or changes in maxspeed. There are any number of legitimate reasons that nodes might be added or deleted on ways.</p>
<p>I hope this helps answer your question.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Feb '22, 01:22</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-83417" class="comments-container">
&#10;</div>
<div id="comment-tools-83417" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83417-form-container" class="comment-form-container">
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

