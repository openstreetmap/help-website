+++
type = "question"
title = "In JOSM: Jump to objects in a search result set"
description = '''I&#x27;m looking for a way to jump to selected objects in JOSM. For example, I might run a search for all nodes in the current view having a certain tag. My search string might look like this if I&#x27;m looking for nodes that were incorrectly tagged:  type:node and highway=track  In the selection box I might...'''
date = "2014-03-30T10:03:00Z"
lastmod = "2014-03-30T15:34:00Z"
weight = 31994
keywords = [ "josm", "search" ]
aliases = [ "/questions/31994" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [In JOSM: Jump to objects in a search result set](/questions/31994/in-josm-jump-to-objects-in-a-search-result-set)

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
<span id="post-31994-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31994-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-31994-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm looking for a way to jump to selected objects in JOSM. For example, I might run a search for all nodes in the current view having a certain tag. My search string might look like this if I'm looking for nodes that were incorrectly tagged:</p>
<blockquote>
<p>type:node and highway=track</p>
</blockquote>
<p>In the selection box I might see 15 nodes meeting the search criteria. These are highlighted in the map view area but can be downright difficult to find. Is there a way to jump to, or cause JOSM to focus on, each one in succession?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Mar '14, 10:03</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-31994" class="comments-container">
&#10;</div>
<div id="comment-tools-31994" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31994-form-container" class="comment-form-container">
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

<span id="31996"></span>

<div id="answer-container-31996" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31996-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31996-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-31996-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AlaskaDave has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, this is possible via the <em>todo</em> plugin. Just add all selected elements to the todo list. Then iterate through all of them via the <em>Pass</em> or <em>Mark</em> buttons. <em>Pass</em> will keep them in the list while iterating, <em>Mark</em> will remove them simultaneously.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Mar '14, 10:33</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-31996" class="comments-container">
<span id="32000"></span>
<div id="comment-32000" class="comment">
<div id="post-32000-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Sweet! Just what I wanted — thanks very much.</p>
</div>
<div id="comment-32000-info" class="comment-info">
<span class="comment-age">(30 Mar '14, 15:34)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-31996" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31996-form-container" class="comment-form-container">
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

