+++
type = "question"
title = "Orphan nodes by Redaction Bot"
description = '''It seems that sometimes the Redaction Bot deleted ways and related nodes and sometimes deleted ways but not the related nodes thus creating what we call &quot;orphan nodes&quot;. Do you know why it was &quot;redacted&quot; differently ?'''
date = "2012-08-24T15:02:00Z"
lastmod = "2012-08-24T16:43:00Z"
weight = 15482
keywords = [ "redaction", "orphan-nodes" ]
aliases = [ "/questions/15482" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Orphan nodes by Redaction Bot](/questions/15482/orphan-nodes-by-redaction-bot)

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
<span id="post-15482-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15482-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-15482-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>It seems that sometimes the Redaction Bot deleted ways and related nodes and sometimes deleted ways but not the related nodes thus creating what we call "orphan nodes". Do you know why it was "redacted" differently ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-redaction" rel="tag" title="see questions tagged &#39;redaction&#39;">redaction</span> <span class="post-tag tag-link-orphan-nodes" rel="tag" title="see questions tagged &#39;orphan-nodes&#39;">orphan-nodes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Aug '12, 15:02</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Aug '12, 16:06</strong> </span></p>
</div>
</div>
<div id="comments-container-15482" class="comments-container">
&#10;</div>
<div id="comment-tools-15482" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15482-form-container" class="comment-form-container">
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

<span id="15488"></span>

<div id="answer-container-15488" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15488-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15488-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-15488-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Pieren has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One scenario:</p>
<ul>
<li>First somebody who accepted the license created a way (including the nodes).</li>
<li>Next someone merged the way with another way that was created by a decliner. So the original way is gone, but it's nodes are still there.</li>
<li>Last the redactionbot removed the way created by the decliner. Of course it wouldn't touch the nodes that came from the "other" way.</li>
</ul>
<p>Another scenario:</p>
<ul>
<li>First somebody who accepted the license created a way (including the nodes).</li>
<li>Next a decliner splits the way. So for one part he is seen as the creator of the way, but he is the creator of non of the nodes.</li>
<li>Next somebody deletes the part of the original way that had the original ID.</li>
<li>Last the redactionbot removed the way "created" by the decliner. (The redactionbot doesn't do undeletes.)</li>
</ul>
<p>Third scenario:</p>
<ul>
<li>First a decliner creates a way.</li>
<li>Next somebody who accepted adds a lot of nodes to the way to improve it's accuracy.</li>
<li>Last the redactionbot removes the way and it's original nodes, but not the extra nodes.</li>
</ul>
<p>You can create other scenarios where the nodes and the ways were both created by a decliner.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Aug '12, 16:43</strong></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cartinus has 35 accepted answers">27%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Aug '12, 16:48</strong> </span></p>
</div>
</div>
<div id="comments-container-15488" class="comments-container">
&#10;</div>
<div id="comment-tools-15488" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15488-form-container" class="comment-form-container">
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

