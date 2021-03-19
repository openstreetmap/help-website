+++
type = "question"
title = "Citrix server capture showing Duplicate Acks and Retransmits"
description = '''I have a client complaining of delays in printing to a printer connected off of a Citrix server. Wireshark capture on the Citrix server shows a ton of Dup ACKs and retransmits. The Duplicate Acks appear to be happening to fast to be real. I am hoping someone can help analyze this capture http://www....'''
date = "2013-05-01T12:34:00Z"
lastmod = "2014-12-23T10:18:00Z"
weight = 20882
keywords = [ "duplicate", "wireshark", "acks", "tcp", "retransmits" ]
aliases = [ "/questions/20882" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Citrix server capture showing Duplicate Acks and Retransmits](/questions/20882/citrix-server-capture-showing-duplicate-acks-and-retransmits)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20882-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20882-score" class="post-score" title="current number of votes">0</div><span id="post-20882-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a client complaining of delays in printing to a printer connected off of a Citrix server. Wireshark capture on the Citrix server shows a ton of Dup ACKs and retransmits. The Duplicate Acks appear to be happening to fast to be real. I am hoping someone can help analyze this capture <a href="http://www.cloudshark.org/captures/2046db994407">http://www.cloudshark.org/captures/2046db994407</a></p><p>I'm trying to determine a possible cause of the dup acks. The host ip is 172.18.30.28 and the citrix server ip is 172.26.19.101</p><p>I assume the TCP retransmits are being seen because there was no ACK to the previous TCP segment.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-duplicate" rel="tag" title="see questions tagged &#39;duplicate&#39;">duplicate</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-acks" rel="tag" title="see questions tagged &#39;acks&#39;">acks</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-retransmits" rel="tag" title="see questions tagged &#39;retransmits&#39;">retransmits</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 May '13, 12:34</strong></p><img src="https://secure.gravatar.com/avatar/833f8f03010008b583dba9740ff0b330?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sbaker00&#39;s gravatar image" /><p><span>sbaker00</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sbaker00 has no accepted answers">0%</span></p></div></div><div id="comments-container-20882" class="comments-container"><span id="20883"></span><div id="comment-20883" class="comment"><div id="post-20883-score" class="comment-score"></div><div class="comment-text"><p>Are you sure that this is a print job? The packets are all pretty small (average packet size is 76 bytes) and they are priorized as class 2, while most print jobs I have seen so far use prio class 3.</p><p>Otherwise it looks like you've got massive packet loss (Wireshark notices this as "previous segment not captured") with massive retransmissions coming in.</p></div><div id="comment-20883-info" class="comment-info"><span class="comment-age">(01 May '13, 12:46)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="20884"></span><div id="comment-20884" class="comment"><div id="post-20884-score" class="comment-score"></div><div class="comment-text"><p>Strange thing is that I can ping between the client and server all day without any packet loss and response times are good.</p></div><div id="comment-20884-info" class="comment-info"><span class="comment-age">(01 May '13, 13:16)</span> <span class="comment-user userinfo">sbaker00</span></div></div></div><div id="comment-tools-20882" class="comment-tools"></div><div class="clear"></div><div id="comment-20882-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="20886"></span>

<div id="answer-container-20886" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20886-score" class="post-score" title="current number of votes">2</div><span id="post-20886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Pings are not a good thing to compare TCP or UDP transmissions to, because they're small and have delta times that are often measured in seconds instead of milliseconds.</p><p>The problem I have with your trace is that there is no indicator why the packets are lost, and the retransmissions seem to be quite massive after the initial communication is just doing fine for about 10 seconds. Maybe there are other data transfers hogging the network while the packets are lost, but that can't be seen in the trace. You have 204 lost segments, but 11749 retransmission, which seems to be cause by packets being retransmitted multiple times until they finally get accepted. Example: filter for "tcp.seq==1660 or tcp.ack==1660" (with relative TCP sequence numbers) and you'll see 10 retransmissions for the same packet, and just one acknowledge. So I think the receiver is having some sort of trouble with the incoming packets, or they get lost in the path somewhere.</p><p>You might want to do a capture at the server and the printer at the same time to see what packets you see on both ends.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 May '13, 13:48</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-20886" class="comments-container"></div><div id="comment-tools-20886" class="comment-tools"></div><div class="clear"></div><div id="comment-20886-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38687"></span>

<div id="answer-container-38687" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38687-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38687-score" class="post-score" title="current number of votes">0</div><span id="post-38687-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>is/was there a VIP involved? if so, make sure you are only using the vip or only the server ip to communicate with the printer, not both.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Dec '14, 10:18</strong></p><img src="https://secure.gravatar.com/avatar/b569ecc6314ac29543dd3475e36d4e28?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="slicerpro&#39;s gravatar image" /><p><span>slicerpro</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="slicerpro has no accepted answers">0%</span></p></div></div><div id="comments-container-38687" class="comments-container"></div><div id="comment-tools-38687" class="comment-tools"></div><div class="clear"></div><div id="comment-38687-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

