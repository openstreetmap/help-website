+++
type = "question"
title = "Overpass: get older version"
description = '''Is it possible to get older versions of objects via the Overpass API? Or whats the fastest way to get a specific version of an OSM object like a node?'''
date = "2013-03-05T10:20:00Z"
lastmod = "2013-03-05T12:20:00Z"
weight = 20506
keywords = [ "overpass", "version", "query" ]
aliases = [ "/questions/20506" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass: get older version](/questions/20506/overpass-get-older-version)

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
<span id="post-20506-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20506-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20506-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is it possible to get older versions of objects via the Overpass API? Or whats the fastest way to get a specific version of an OSM object like a node?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-version" rel="tag" title="see questions tagged &#39;version&#39;">version</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Mar '13, 10:20</strong></p>
<img src="https://secure.gravatar.com/avatar/2c52393df51ceb5327c1e19e3b0efbfe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mattes_tili&#39;s gravatar image" />
<p><span>Mattes_tili</span><br />
<span class="score" title="146 reputation points">146</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mattes_tili has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-20506" class="comments-container">
&#10;</div>
<div id="comment-tools-20506" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20506-form-container" class="comment-form-container">
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

<span id="20508"></span>

<div id="answer-container-20508" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20508-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20508-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-20508-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Mattes_tili has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use the regular <a href="http://wiki.openstreetmap.org/wiki/API_v0.6#Version:_GET_.2Fapi.2F0.6.2F.5Bnode.7Cway.7Crelation.5D.2F.23id.2F.23version">API</a> directly, e.g.: <a href="http://www.openstreetmap.org/api/0.6/node/123456/7">http://www.openstreetmap.org/api/0.6/node/123456/7</a> will retrieve version 7 of node 123456.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '13, 12:20</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-20508" class="comments-container">
&#10;</div>
<div id="comment-tools-20508" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20508-form-container" class="comment-form-container">
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

