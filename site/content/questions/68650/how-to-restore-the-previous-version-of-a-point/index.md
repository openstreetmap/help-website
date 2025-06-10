+++
type = "question"
title = "How to restore the previous version of a point"
description = '''I have moved a point by mistake in a series of JOSM edits.1 Though I have moved it to a place near the original place, it results in an additional version of a way I didn&#x27;t intend to edit.  Are there any way to restore the original location of the point? (this is useful when I don&#x27;t know where the p...'''
date = "2019-04-04T20:03:00Z"
lastmod = "2019-04-05T11:10:00Z"
weight = 68650
keywords = [ "josm" ]
aliases = [ "/questions/68650" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to restore the previous version of a point](/questions/68650/how-to-restore-the-previous-version-of-a-point)

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
<span id="post-68650-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68650-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68650-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have moved a point by mistake in a series of JOSM edits.<a href="https://www.openstreetmap.org/node/2516156498">1</a> Though I have moved it to a place near the original place, it results in an additional version of a way I didn't intend to edit.</p>
<ol>
<li>Are there any way to restore the original location of the point? (this is useful when I don't know where the point originally is.)</li>
<li>Are there any way to undo the move of the point in JOSM before the changes are uploaded, without losting succeeding changes? This will prevent the unnecessary version to be saved.</li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Apr '19, 20:03</strong></p>
<img src="https://secure.gravatar.com/avatar/055be0a1f215071b4c2c172f569cc7cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="a828245&#39;s gravatar image" />
<p><span>a828245</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="a828245 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68650" class="comments-container">
&#10;</div>
<div id="comment-tools-68650" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68650-form-container" class="comment-form-container">
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

<span id="68653"></span>

<div id="answer-container-68653" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68653-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68653-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-68653-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>After an upload you can use the reverter plugin (however this will create even one more object version of the node). Ways don't get a new object version if you only move their nodes.</p>
<p>Before an upload you can select the node, use Edit -&gt; Purge to "remove" the node and the connected ways from your dataset and download that area again.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Apr '19, 20:46</strong></p>
<img src="https://secure.gravatar.com/avatar/b904d75b8ea950f64710d2a8303cead7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Klumbumbus&#39;s gravatar image" />
<p><span>Klumbumbus</span><br />
<span class="score" title="543 reputation points">543</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Klumbumbus has one accepted answer">8%</span></p>
</div>
</div>
<div id="comments-container-68653" class="comments-container">
<span id="68663"></span>
<div id="comment-68663" class="comment">
<div id="post-68663-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>this is a really useful tip!</p>
</div>
<div id="comment-68663-info" class="comment-info">
<span class="comment-age">(05 Apr '19, 11:10)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-68653" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68653-form-container" class="comment-form-container">
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

