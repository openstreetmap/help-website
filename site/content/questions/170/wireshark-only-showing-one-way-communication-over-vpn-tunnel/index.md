+++
type = "question"
title = "Wireshark only showing one way communication over VPN tunnel"
description = '''I&#x27;m running wireshark 1.2.10 on Fedora 13 and trying to capture traffic across the VPN tunnel to my office. I&#x27;m using Cisco&#x27;s VPN client for linux. When I capture the traffic I see my requests going out but I don&#x27;t see the responses coming back. I know they are coming back because the internal web s...'''
date = "2010-09-17T04:57:00Z"
lastmod = "2010-09-17T10:43:00Z"
weight = 170
keywords = [ "traffic", "one-way", "vpn", "cisco", "linux" ]
aliases = [ "/questions/170" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark only showing one way communication over VPN tunnel](/questions/170/wireshark-only-showing-one-way-communication-over-vpn-tunnel)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-170-score" class="post-score" title="current number of votes">0</div><span id="post-170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm running wireshark 1.2.10 on Fedora 13 and trying to capture traffic across the VPN tunnel to my office. I'm using Cisco's VPN client for linux. When I capture the traffic I see my requests going out but I don't see the responses coming back. I know they are coming back because the internal web sites I'm going to display just fine. I just don't see the return traffic in wireshark. this is a clean install of wireshark and I haven't created or applied any capture or display filters.</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-one-way" rel="tag" title="see questions tagged &#39;one-way&#39;">one-way</span> <span class="post-tag tag-link-vpn" rel="tag" title="see questions tagged &#39;vpn&#39;">vpn</span> <span class="post-tag tag-link-cisco" rel="tag" title="see questions tagged &#39;cisco&#39;">cisco</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Sep '10, 04:57</strong></p><img src="https://secure.gravatar.com/avatar/da593d419ea30f77941ce78170d7eed5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sdb6585&#39;s gravatar image" /><p><span>sdb6585</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sdb6585 has no accepted answers">0%</span></p></div></div><div id="comments-container-170" class="comments-container"></div><div id="comment-tools-170" class="comment-tools"></div><div class="clear"></div><div id="comment-170-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="187"></span>

<div id="answer-container-187" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-187-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-187-score" class="post-score" title="current number of votes">0</div><span id="post-187-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are <a href="http://wiki.wireshark.org/CaptureSetup/InterferingSoftware">many problems reported with not seeing traffic one way or even both way when VPN software is installed on Windows</a>. I suspect the same kind of problems can manifest themselves on other OS'es with VPN software. The problem is that the VPN has to nest itself somewhere low in the TCP/IP stack to be able to get to the packets in time. This might interfere with libpcap's ability to get to the packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '10, 10:43</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-187" class="comments-container"></div><div id="comment-tools-187" class="comment-tools"></div><div class="clear"></div><div id="comment-187-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

