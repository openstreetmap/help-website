+++
type = "question"
title = "grouping by conversations"
description = '''I have a very big TCP dump between two servers. There are only two IP addresses so each conversation is defined by the TCP ports used. My question is how do I group the the data by conversations such that all the output is still there just grouped by unique conversation'''
date = "2013-11-08T13:29:00Z"
lastmod = "2013-11-10T22:52:00Z"
weight = 26786
keywords = [ "conversation", "tcp" ]
aliases = [ "/questions/26786" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [grouping by conversations](/questions/26786/grouping-by-conversations)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26786-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26786-score" class="post-score" title="current number of votes">0</div><span id="post-26786-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a very big TCP dump between two servers. There are only two IP addresses so each conversation is defined by the TCP ports used. My question is how do I group the the data by conversations such that all the output is still there just grouped by unique conversation</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-conversation" rel="tag" title="see questions tagged &#39;conversation&#39;">conversation</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '13, 13:29</strong></p><img src="https://secure.gravatar.com/avatar/6987a1a2019e720d16630dc2f9f8e371?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrw_1955&#39;s gravatar image" /><p><span>mrw_1955</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrw_1955 has no accepted answers">0%</span></p></div></div><div id="comments-container-26786" class="comments-container"></div><div id="comment-tools-26786" class="comment-tools"></div><div class="clear"></div><div id="comment-26786-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="26787"></span>

<div id="answer-container-26787" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26787-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26787-score" class="post-score" title="current number of votes">0</div><span id="post-26787-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is no such grouping feature in Wireshark, at least not in the 'main' GUI.</p><p>What you can do:</p><ul><li>View Conversations: <code>Statistics -&gt; Conversations -&gt; TCP (tab)</code>. Then select one conversation and click on 'Follow Stream'. That will create a <a href="http://wiki.wireshark.org/DisplayFilters">display filter</a> to show only that single conversation</li><li>Set a display filter manually: <code>tcp.stream eq 0</code> or <code>tcp.stream eq 1</code> etc.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '13, 15:36</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-26787" class="comments-container"></div><div id="comment-tools-26787" class="comment-tools"></div><div class="clear"></div><div id="comment-26787-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26831"></span>

<div id="answer-container-26831" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26831-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26831-score" class="post-score" title="current number of votes">0</div><span id="post-26831-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>try using Splitcap tool, its excellent, works very fast and has various options to manipulate the capture file</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Nov '13, 22:52</strong></p><img src="https://secure.gravatar.com/avatar/3e5e9d76a54debaa630d909e37048da8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="deepacket&#39;s gravatar image" /><p><span>deepacket</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="deepacket has no accepted answers">0%</span></p></div></div><div id="comments-container-26831" class="comments-container"></div><div id="comment-tools-26831" class="comment-tools"></div><div class="clear"></div><div id="comment-26831-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

