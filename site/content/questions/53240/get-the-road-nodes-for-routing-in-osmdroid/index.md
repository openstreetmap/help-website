+++
type = "question"
title = "Get the road nodes for routing in osmdroid"
description = '''I have a .osm file that contains the list of highways. How do i parse it so that it&#x27;ll get the nodes so i can use it for my djikstra algorithm which computes the shortest path? I have followed the answer here. The problem is i don&#x27;t know what command should i use in the osmfilter in step 2. I checke...'''
date = "2016-12-05T04:21:00Z"
lastmod = "2016-12-05T09:30:00Z"
weight = 53240
keywords = [ "osmfilter", ".osm", "parsing" ]
aliases = [ "/questions/53240" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get the road nodes for routing in osmdroid](/questions/53240/get-the-road-nodes-for-routing-in-osmdroid)

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
<span id="post-53240-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53240-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53240-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a .osm file that contains the list of highways. How do i parse it so that it'll get the nodes so i can use it for my djikstra algorithm which computes the shortest path? I have followed the answer <a href="/questions/19213/how-can-i-convert-an-osm-xml-file-into-a-graph-representation">here</a>. The problem is i don't know what command should i use in the osmfilter in step 2. I checked the Osmfilter wiki site and it does not tell me how to split the way into two edges. I'm lost on what to put the command so i can parse only the road nodes for routing purposes.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span> <span class="post-tag tag-link-.osm" rel="tag" title="see questions tagged &#39;.osm&#39;">.osm</span> <span class="post-tag tag-link-parsing" rel="tag" title="see questions tagged &#39;parsing&#39;">parsing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Dec '16, 04:21</strong></p>
<img src="https://secure.gravatar.com/avatar/2934739662b710a46fcac3c9e99d5a05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marisannn&#39;s gravatar image" />
<p><span>Marisannn</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marisannn has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Dec '16, 08:23</strong> </span></p>
</div>
</div>
<div id="comments-container-53240" class="comments-container">
&#10;</div>
<div id="comment-tools-53240" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53240-form-container" class="comment-form-container">
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

<span id="53245"></span>

<div id="answer-container-53245" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53245-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53245-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53245-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="/questions/19213/how-can-i-convert-an-osm-xml-file-into-a-graph-representation/19214">described algorithm</a> is completely independent from osmfilter. You have to implement it in <em>your</em> application. It describes the things you have to do while parsing an OSM file in order to construct a graph representation <em>inside your</em> application.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Dec '16, 09:30</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-53245" class="comments-container">
&#10;</div>
<div id="comment-tools-53245" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53245-form-container" class="comment-form-container">
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

