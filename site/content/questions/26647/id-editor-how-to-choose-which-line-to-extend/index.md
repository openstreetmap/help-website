+++
type = "question"
title = "iD editor: how to choose which line to extend?"
description = '''Take a situation where multiple ways are connected at a node. I would like to extend one of them (to keep tags, etc), but in the iD Editor, when I click the &quot;Line&quot; button, then the node, I cannot choose which way to extend.  (yes, I can just extend whichever way iD selects, then cut the way and merg...'''
date = "2013-09-23T15:06:00Z"
lastmod = "2013-09-25T19:13:00Z"
weight = 26647
keywords = [ "ideditor", "selection", "extension", "way" ]
aliases = [ "/questions/26647" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [iD editor: how to choose which line to extend?](/questions/26647/id-editor-how-to-choose-which-line-to-extend)

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
<span id="post-26647-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26647-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26647-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Take a situation where multiple ways are connected at a node. I would like to extend one of them (to keep tags, etc), but in the iD Editor, when I click the "Line" button, then the node, I cannot choose which way to extend.</p>
<p>(yes, I can just extend whichever way iD selects, then cut the way and merge the new section with the way I wanted to extend, but that's ugly and time consuming)<br />
</p>
<p>In Potlatch 2, I would select the way, then click the end node and extend the line. I'm thinking there must be a way to do this in iD that I've missed?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-selection" rel="tag" title="see questions tagged &#39;selection&#39;">selection</span> <span class="post-tag tag-link-extension" rel="tag" title="see questions tagged &#39;extension&#39;">extension</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Sep '13, 15:06</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span> </br></p>
</div>
</div>
<div id="comments-container-26647" class="comments-container">
&#10;</div>
<div id="comment-tools-26647" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26647-form-container" class="comment-form-container">
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

<span id="26736"></span>

<div id="answer-container-26736" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26736-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26736-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26736-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Found out that a solution will be in the next release: <a href="https://github.com/systemed/iD/issues/1721">https://github.com/systemed/iD/issues/1721</a></p>
<p>Here's what it'll do:</p>
<ul>
<li>The line draw tool will always start a new way</li>
<li>The way you continue an existing line is by a "Continue" menu item when clicking on a vertex (#560).</li>
<li>Disambiguation can be done by selecting a vertex, then a line to continue and using the "Continue" action.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Sep '13, 19:13</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-26736" class="comments-container">
&#10;</div>
<div id="comment-tools-26736" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26736-form-container" class="comment-form-container">
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

