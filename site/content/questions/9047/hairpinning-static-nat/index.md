+++
type = "question"
title = "hairpinning static NAT"
description = '''Hi network experts, My question is not directly related to wireshark. But when I start wireshark, the network behaviour is changed and I don&#x27;t know why. I have the following setup: Linux machine (OpenSuse 12.1) with one physical network interface. Interface has many IP&#x27;s like 192.168.10.10, 192.168....'''
date = "2012-02-15T18:56:00Z"
lastmod = "2012-02-20T08:23:00Z"
weight = 9047
keywords = [ "hairpinning", "static", "nat" ]
aliases = [ "/questions/9047" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [hairpinning static NAT](/questions/9047/hairpinning-static-nat)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9047-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9047-score" class="post-score" title="current number of votes">0</div><span id="post-9047-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi network experts,</p><p>My question is not directly related to wireshark. But when I start wireshark, the network behaviour is changed and I don't know why.</p><p>I have the following setup: Linux machine (OpenSuse 12.1) with one physical network interface. Interface has many IP's like 192.168.10.10, 192.168.10.11 ... 192.168.10.15</p><p>KVM is running on this box using libvirt and virt-manage.</p><p>Second interface is a virtual bridge virbr0 with IP 10.1.1.1</p><p>One to One NAT is setup from the host to the guests using shorewall.</p><p>Everything works except, connecting from guest to it's own 'external' ip. Let's assume guest has IP 10.1.1.15 and 192.168.1.15 is nat-ed to 10.1.1.15; connections from this guest (10.1.1.15) to 192.168.1.15 are failing. Connecting to any other 192.168.1.x IP's are working find (including other virtual machines).</p><p>When I start wireshark on the host, connections from 10.1.1.15 to 192.168.1.15 start to work!</p><p>Any suggestion is appreciated.</p><p>Regards, happyp3nguin</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-hairpinning" rel="tag" title="see questions tagged &#39;hairpinning&#39;">hairpinning</span> <span class="post-tag tag-link-static" rel="tag" title="see questions tagged &#39;static&#39;">static</span> <span class="post-tag tag-link-nat" rel="tag" title="see questions tagged &#39;nat&#39;">nat</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Feb '12, 18:56</strong></p><img src="https://secure.gravatar.com/avatar/d23547e38431516cb8d8dc8f076cfef6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="happyp3nguin&#39;s gravatar image" /><p><span>happyp3nguin</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="happyp3nguin has no accepted answers">0%</span></p></div></div><div id="comments-container-9047" class="comments-container"></div><div id="comment-tools-9047" class="comment-tools"></div><div class="clear"></div><div id="comment-9047-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9053"></span>

<div id="answer-container-9053" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9053-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9053-score" class="post-score" title="current number of votes">1</div><span id="post-9053-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Even though I have no experience with your kind of setup, my guess is that putting the capture interface in Promiscuous mode (like Wireshark does by default when capturing) is the reason it suddenly works. You can verify this by using Wireshark without putting the interface in promiscuous mode.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '12, 01:45</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-9053" class="comments-container"><span id="9141"></span><div id="comment-9141" class="comment"><div id="post-9141-score" class="comment-score"></div><div class="comment-text"><p>thanks for the answer, I have realized this today when I saw messages like this in the kernel log: device virbr0 entered promiscuous mode</p></div><div id="comment-9141-info" class="comment-info"><span class="comment-age">(20 Feb '12, 08:13)</span> <span class="comment-user userinfo">happyp3nguin</span></div></div><span id="9142"></span><div id="comment-9142" class="comment"><div id="post-9142-score" class="comment-score"></div><div class="comment-text"><p>(I converted your "answer" to a "comment", please see the FAQ for details)</p></div><div id="comment-9142-info" class="comment-info"><span class="comment-age">(20 Feb '12, 08:23)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-9053" class="comment-tools"></div><div class="clear"></div><div id="comment-9053-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

