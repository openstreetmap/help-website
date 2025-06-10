+++
type = "question"
title = "Population tag for nodes in France cities/towns/villages"
description = '''Hi, I have recently noticed that quite an amount of the population tags in the cities/towns/villages nodes have been removed in bulk on different change sets. Is there any particular reason for this, since that tag is widely used when getting our dataset and can&#x27;t seem any reason for removing data f...'''
date = "2020-01-27T14:20:00Z"
lastmod = "2020-01-27T19:08:00Z"
weight = 72716
keywords = [ "france", "changeset", "nodes", "cities", "population" ]
aliases = [ "/questions/72716" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Population tag for nodes in France cities/towns/villages](/questions/72716/population-tag-for-nodes-in-france-citiestownsvillages)

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
<span id="post-72716-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72716-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72716-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have recently noticed that quite an amount of the population tags in the cities/towns/villages nodes have been removed in bulk on different change sets. Is there any particular reason for this, since that tag is widely used when getting our dataset and can't seem any reason for removing data from OSM. If this was done wrongfully, is there a way to revert the changes?</p>
<p>Thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-france" rel="tag" title="see questions tagged &#39;france&#39;">france</span> <span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-cities" rel="tag" title="see questions tagged &#39;cities&#39;">cities</span> <span class="post-tag tag-link-population" rel="tag" title="see questions tagged &#39;population&#39;">population</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jan '20, 14:20</strong></p>
<img src="https://secure.gravatar.com/avatar/6bb7c379dadac2bf492b7fc4b66f6f85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Clinton%20Mercieca&#39;s gravatar image" />
<p><span>Clinton Merc...</span><br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Clinton Mercieca has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72716" class="comments-container">
<span id="72721"></span>
<div id="comment-72721" class="comment">
<div id="post-72721-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do you have a few examples of such changesets?</p>
</div>
<div id="comment-72721-info" class="comment-info">
<span class="comment-age">(27 Jan '20, 17:13)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="72722"></span>
<div id="comment-72722" class="comment">
<div id="post-72722-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This appears to be one changeset where lots of population tags were removed from the place nodes and added instead on the administrative boundary relations. <a href="https://www.openstreetmap.org/changeset/79698989">https://www.openstreetmap.org/changeset/79698989</a> In general, the population tag would normally be on the place nodes, so this change could break things for a number of data consumers.</p>
</div>
<div id="comment-72722-info" class="comment-info">
<span class="comment-age">(27 Jan '20, 18:22)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="72723"></span>
<div id="comment-72723" class="comment">
<div id="post-72723-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It looks like these changeset have been discussed on the talk-fr mailing list starting here: <a href="https://lists.openstreetmap.org/pipermail/talk-fr/2020-January/096261.html">https://lists.openstreetmap.org/pipermail/talk-fr/2020-January/096261.html</a></p>
<p>It is a long thread (about 40 messages) and I haven't looked through it to see if it specifically explains the move from nodes to relations.</p>
</div>
<div id="comment-72723-info" class="comment-info">
<span class="comment-age">(27 Jan '20, 18:37)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
<span id="72724"></span>
<div id="comment-72724" class="comment">
<div id="post-72724-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I had a quick further look at that mailing list discussion. I think the issue may be that the available population figures relate to communes rather than villages, so should be associated with the commune boundary rather than for example a place=village node (as there may be inhabitants outside the village).</p>
<p>You may need to make contact with the French community for further details.</p>
</div>
<div id="comment-72724-info" class="comment-info">
<span class="comment-age">(27 Jan '20, 18:51)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
</div>
<div id="comment-tools-72716" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72716-form-container" class="comment-form-container">
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

<span id="72725"></span>

<div id="answer-container-72725" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72725-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72725-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72725-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I will go through the thread and try to get in touch with the French community to try and figure this out, thanks for the feedback.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jan '20, 19:08</strong></p>
<img src="https://secure.gravatar.com/avatar/6bb7c379dadac2bf492b7fc4b66f6f85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Clinton%20Mercieca&#39;s gravatar image" />
<p><span>Clinton Merc...</span><br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Clinton Mercieca has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72725" class="comments-container">
&#10;</div>
<div id="comment-tools-72725" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72725-form-container" class="comment-form-container">
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

