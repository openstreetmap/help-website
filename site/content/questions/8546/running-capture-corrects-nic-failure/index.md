+++
type = "question"
title = "running capture corrects NIC failure"
description = '''I am using a Realtek PCIe GBE NIC on a Sony Vaio running Windows 7. Suddenly last week this NIC stopped commuicating beyone its gateway. The NIC can successfully ping its gateway but does not receive ping replies from any host beyond the gateway. So I attempted to use Wireshark to diagnose this fail...'''
date = "2012-01-22T15:33:00Z"
lastmod = "2012-01-22T19:37:00Z"
weight = 8546
keywords = [ "nic" ]
aliases = [ "/questions/8546" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [running capture corrects NIC failure](/questions/8546/running-capture-corrects-nic-failure)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8546-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8546-score" class="post-score" title="current number of votes">0</div><span id="post-8546-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using a Realtek PCIe GBE NIC on a Sony Vaio running Windows 7.</p><p>Suddenly last week this NIC stopped commuicating beyone its gateway. The NIC can successfully ping its gateway but does not receive ping replies from any host beyond the gateway.</p><p>So I attempted to use Wireshark to diagnose this failure. Astoundingly, as soon as I started the Wireshark capture, the NIC is able to successfully communicate with the Internet. When I stop the capture, the NIC can no longer communicate beyond the gateway. The NIC runs successfully when a Wireshark capture is running and fails when the capture is not running.</p><p>Can someone suggest what Wireshark does that enables the NIC to function correctly?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nic" rel="tag" title="see questions tagged &#39;nic&#39;">nic</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '12, 15:33</strong></p><img src="https://secure.gravatar.com/avatar/af72142937969e7f23e189aef8152def?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="utahoc&#39;s gravatar image" /><p><span>utahoc</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="utahoc has no accepted answers">0%</span></p></div></div><div id="comments-container-8546" class="comments-container"></div><div id="comment-tools-8546" class="comment-tools"></div><div class="clear"></div><div id="comment-8546-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8552"></span>

<div id="answer-container-8552" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8552-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8552-score" class="post-score" title="current number of votes">0</div><span id="post-8552-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>About the only thing I can think of that it would be doing would be putting the adapter into promiscuous mode. What happens if you run Wireshark with the "promiscuous mode" checkbox <em>not</em> checked? If that doesn't fix the problem, but capturing with "promiscuous mode" checked does fix the problem, that's probably the issue.</p><p>If that turns out the be the issue, then why the NIC couldn't get past the gateway if not in promiscuous mode is another question. What happens if you try to use the <code>tracert</code> command to ping hosts beyond the gateway? What does it report if you can't ping those hosts?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '12, 19:37</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-8552" class="comments-container"></div><div id="comment-tools-8552" class="comment-tools"></div><div class="clear"></div><div id="comment-8552-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

