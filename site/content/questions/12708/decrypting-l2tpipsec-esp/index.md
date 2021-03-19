+++
type = "question"
title = "Decrypting L2TP/IPsec, ESP"
description = '''Hello, I need to diagnose L2TP/Ipsec VPN Connection which has encrypted packets exchanged between the server and client.  Is there any way to test the connection by decrypting the packets using wireshark, like we do it for SSL/TLS connection using the private key/pem file. If there is some other way...'''
date = "2012-07-13T15:04:00Z"
lastmod = "2014-08-22T06:36:00Z"
weight = 12708
keywords = [ "ipsec", "vpn", "l2tp", "esp" ]
aliases = [ "/questions/12708" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Decrypting L2TP/IPsec, ESP](/questions/12708/decrypting-l2tpipsec-esp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12708-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12708-score" class="post-score" title="current number of votes">1</div><span id="post-12708-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I need to diagnose L2TP/Ipsec VPN Connection which has encrypted packets exchanged between the server and client. Is there any way to test the connection by decrypting the packets using wireshark, like we do it for SSL/TLS connection using the private key/pem file. If there is some other way out there I would be very thankful for the same. Also, when I am trying to capture packets in wireshark while initiating L2TP connection I cannot see l2tp packets in the capture. But can only see ISAKMP and ESP packets in the capture. The filter I have used in wireshark is 'isakmp or esp or l2tp' [Info] Wireshark: Version 1.6.8 (SVN Rev 42761 from /trunk-1.6) Mac OSx 10.7 Client and Server</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ipsec" rel="tag" title="see questions tagged &#39;ipsec&#39;">ipsec</span> <span class="post-tag tag-link-vpn" rel="tag" title="see questions tagged &#39;vpn&#39;">vpn</span> <span class="post-tag tag-link-l2tp" rel="tag" title="see questions tagged &#39;l2tp&#39;">l2tp</span> <span class="post-tag tag-link-esp" rel="tag" title="see questions tagged &#39;esp&#39;">esp</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jul '12, 15:04</strong></p><img src="https://secure.gravatar.com/avatar/14f4ddd77cb3126d745b7ee9ff9d028d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Azee&#39;s gravatar image" /><p><span>Azee</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Azee has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Jul '12, 15:11</strong> </span></p></div></div><div id="comments-container-12708" class="comments-container"></div><div id="comment-tools-12708" class="comment-tools"></div><div class="clear"></div><div id="comment-12708-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12711"></span>

<div id="answer-container-12711" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12711-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12711-score" class="post-score" title="current number of votes">1</div><span id="post-12711-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To decrypt ESP, you must give Wireshark details about the SA (<a href="http://wiki.wireshark.org/ESP_Preferences).">http://wiki.wireshark.org/ESP_Preferences).</a> You can get those details either from an IPSEC debug log or from internal state tables of the IPSEC implementation. For Mac OS X: take a look at the man page of your IPSEC implementation how to enable debug logs or how to extract the SA information. I don't know how to do that on Mac OS X.</p><blockquote><p>Also, when I am trying to capture packets in wireshark while initiating L2TP connection I cannot see l2tp packets in the capture. But can only see ISAKMP and ESP packets in the capture.</p></blockquote><p>because you are encapsulating L2TP in IPSEC (L2TP over IPSEC). L2TP does not provide encryption itself, that's why it is combined with IPSEC. Unless you are able to decrypt the ESP packets, you won't see the L2TP communication.</p><blockquote><p>If there is some other way out there I would be very thankful for the same.</p></blockquote><p>You say, both L2TP client and server are Mac OS X 10.7. If so, you should have configured <a href="https://developer.apple.com/library/mac/#documentation/Darwin/Reference/Manpages/man8/vpnd.8.html#//apple_ref/doc/man/8/vpnd">vpnd</a> and <a href="https://developer.apple.com/library/mac/#documentation/Darwin/Reference/Manpages/man8/pppd.8.html#//apple_ref/doc/man/8/pppd">pppd</a>. Both provide some form of debug logging (see man pages). Maybe that helps to identify your problem, besides decrypting the traffic with Wireshark.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jul '12, 16:50</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Jul '12, 17:00</strong> </span></p></div></div><div id="comments-container-12711" class="comments-container"><span id="35672"></span><div id="comment-35672" class="comment"><div id="post-35672-score" class="comment-score"></div><div class="comment-text"><p>To extract SA information in MAC OS X (at least in 10.9): sudo setkey -D</p></div><div id="comment-35672-info" class="comment-info"><span class="comment-age">(22 Aug '14, 06:36)</span> <span class="comment-user userinfo">nnkken</span></div></div></div><div id="comment-tools-12711" class="comment-tools"></div><div class="clear"></div><div id="comment-12711-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

