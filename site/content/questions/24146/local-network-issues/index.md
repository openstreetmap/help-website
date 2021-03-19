+++
type = "question"
title = "local network issues"
description = '''Hi, can someone take a look at the capture and let me know why so many dup acks and perhaps help me determine why my inside lan is so darn slow? this capture is a file transfer of malware bytes from my machine to my lan file server. thank you https://www.dropbox.com/s/rivkrj62a3g10a9/tmg%20file%20xf...'''
date = "2013-08-28T10:10:00Z"
lastmod = "2013-08-29T09:43:00Z"
weight = 24146
keywords = [ "dup", "ack", "lan", "slow", "reassemble" ]
aliases = [ "/questions/24146" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [local network issues](/questions/24146/local-network-issues)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24146-score" class="post-score" title="current number of votes">0</div><span id="post-24146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, can someone take a look at the capture and let me know why so many dup acks and perhaps help me determine why my inside lan is so darn slow? this capture is a file transfer of malware bytes from my machine to my lan file server.</p><p>thank you</p><p><a href="https://www.dropbox.com/s/rivkrj62a3g10a9/tmg%20file%20xfer.pcapng">https://www.dropbox.com/s/rivkrj62a3g10a9/tmg%20file%20xfer.pcapng</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dup" rel="tag" title="see questions tagged &#39;dup&#39;">dup</span> <span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-lan" rel="tag" title="see questions tagged &#39;lan&#39;">lan</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-reassemble" rel="tag" title="see questions tagged &#39;reassemble&#39;">reassemble</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Aug '13, 10:10</strong></p><img src="https://secure.gravatar.com/avatar/9ca4fbf8cef44a204aabf7d8d0ff66a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="netnerd&#39;s gravatar image" /><p><span>netnerd</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="netnerd has no accepted answers">0%</span></p></div></div><div id="comments-container-24146" class="comments-container"></div><div id="comment-tools-24146" class="comment-tools"></div><div class="clear"></div><div id="comment-24146-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24161"></span>

<div id="answer-container-24161" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24161-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24161-score" class="post-score" title="current number of votes">0</div><span id="post-24161-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You PC is configured with an MTU size of 1300 bytes, resulting in an MSS of 1260 bytes only. So this would be the first thing to check.</p><p>The majority of lost packets is reported by the LAN Server running in VMWare at 192.168.179.6. Given that this is a flat network I'd guess these packets are dropped in the VMWare environment.</p><blockquote><p>MTU size and the optimum mtu size for my laptop is 1300. pinging with mtu size of 1272 does not fragment</p></blockquote><p>That is certainly not the optimum for a flat Ethernet network but obviously it is configured.</p><pre><code>netsh interface ipv4 show subinterfaces</code></pre><p>will show the actual settings and</p><pre><code>netsh interface ipv4 set subinterface &quot;1&quot; mtu = 1500 store = persistent</code></pre><p>could be used to bump this up to the standard ethernet MTU size.</p><p>As for the packet drops in VMware I suggest you google on "vmware packet drops" and/or address this issue to a better suitable forum.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Aug '13, 04:21</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Aug '13, 12:41</strong> </span></p></div></div><div id="comments-container-24161" class="comments-container"><span id="24170"></span><div id="comment-24170" class="comment"><div id="post-24170-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your input. So do I need to look at the vmware environment, and what would you suggest for improving the performance? I checked my MTU size and the optimum mtu size for my laptop is 1300. pinging with mtu size of 1272 does not fragment, and then I add 28 for the 20bytes of iP header and 8 bytes of icmp echo header. So adjusting my mtu on my nic is not really necessary according to what I've been reading. Thanks for looking at this.</p></div><div id="comment-24170-info" class="comment-info"><span class="comment-age">(29 Aug '13, 09:43)</span> <span class="comment-user userinfo">netnerd</span></div></div></div><div id="comment-tools-24161" class="comment-tools"></div><div class="clear"></div><div id="comment-24161-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

