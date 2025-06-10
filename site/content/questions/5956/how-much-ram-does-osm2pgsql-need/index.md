+++
type = "question"
title = "How much RAM does osm2pgsql need?"
description = '''For slim mode, how much RAM is ideal for an import? In non-slim mode, how much is likely to be needed in all? Obviously, the more data in a .osm file, the more memory that will be needed, so what I&#x27;m looking for is an answer along the lines of, &quot;xMB per thousand nodes, yMB per thousand ways&quot; or &quot;suc...'''
date = "2011-06-22T19:21:00Z"
lastmod = "2011-06-23T18:51:00Z"
weight = 5956
keywords = [ "osm2pgsql", "memory" ]
aliases = [ "/questions/5956" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How much RAM does osm2pgsql need?](/questions/5956/how-much-ram-does-osm2pgsql-need)

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
<span id="post-5956-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5956-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-5956-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>For slim mode, how much RAM is ideal for an import?</p>
<p>In non-slim mode, how much is likely to be needed in all?</p>
<p>Obviously, the more data in a .osm file, the more memory that will be needed, so what I'm looking for is an answer along the lines of, "<em>x</em>MB per thousand nodes, <em>y</em>MB per thousand ways" or "<em>such and such</em> based on the highest node ID".</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-memory" rel="tag" title="see questions tagged &#39;memory&#39;">memory</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jun '11, 19:21</strong></p>
<img src="https://secure.gravatar.com/avatar/f72f5a9d1556bec1f4e40411651651e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="asciiphil&#39;s gravatar image" />
<p><span>asciiphil</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="asciiphil has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-5956" class="comments-container">
&#10;</div>
<div id="comment-tools-5956" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5956-form-container" class="comment-form-container">
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

<span id="5971"></span>

<div id="answer-container-5971" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5971-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5971-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-5971-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="asciiphil has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For slim mode you can use as much or as little RAM as you like, but I wouldn't try anything under 1Gb. For a planet file you will find more RAM makes everything go faster up to at least 24GB if not further. The RAM functions as a cache for the nodes data that's repeatedly needed for constructing the ways and relations - if the node isn't in RAM it'll be fetched from disk with is much slower.</p>
<p>For non-slim mode, you have hard limits since there is no intermediate disk store for the nodes. A full planet import in non-slim mode currently requires about 40 Gb of RAM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jun '11, 18:51</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Jun '11, 05:43</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/dd3858f5f89f5a6b738f9dbe59824440?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emj&#39;s gravatar image" />
<p><span>emj</span><br />
<span class="score" title="2024 reputation points"><span>2.0k</span></span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span></p>
</div>
</div>
<div id="comments-container-5971" class="comments-container">
&#10;</div>
<div id="comment-tools-5971" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5971-form-container" class="comment-form-container">
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

