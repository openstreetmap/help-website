+++
type = "question"
title = "Wireshark doesn&#x27;t decode ESP encrypted responses"
description = '''Hi, I have the following topology for two systems which have an ipsec tunnel A[10.203.199.109]------------ B [10.203.199.126] I have configured ESP preferences in Wireshark running in B system with the information got from &#x27;ip xfrm state&#x27; as mentioned below. When I send icmp ping packets/SCTP Hearbe...'''
date = "2010-12-29T05:36:00Z"
lastmod = "2010-12-30T02:48:00Z"
weight = 1508
keywords = [ "not", "decoded", "response", "preferences", "esp" ]
aliases = [ "/questions/1508" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark doesn't decode ESP encrypted responses](/questions/1508/wireshark-doesnt-decode-esp-encrypted-responses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1508-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1508-score" class="post-score" title="current number of votes">0</div><span id="post-1508-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have the following topology for two systems which have an ipsec tunnel A[10.203.199.109]------------ B [10.203.199.126]</p><p>I have configured ESP preferences in Wireshark running in B system with the information got from 'ip xfrm state' as mentioned below.</p><p>When I send icmp ping packets/SCTP Hearbeat packets from A and start capturning the requests and responses in wireshark (System B), I observe that wireshark doesn't decrypt the response from B to A(they appear as ESP protocol packets) while the icmp requests/SCTP Hearbeat packets sent by A are displayed after decryption.</p><p>Could you plese help me out?<br />
</p><p>Wireshark Version used: 0.99.3a</p><p>Output of 'ip xfrm state' in B: src 10.203.199.126 dst 10.203.199.109 proto esp spi 0xcb0232de reqid 1 mode tunnel replay-window 32 auth sha1 0x4e40e2628b172f0331393242f29ab1eba951c825 enc aes 0xc84d1235c49a83caadc9a330513ab281 src 10.203.199.109 dst 10.203.199.126 proto esp spi 0xcec7a22e reqid 1 mode tunnel replay-window 32 auth sha1 0x9fb4979b6d5807f7ca83e33c1c9cc993b6a93a7e enc aes 0x1cbc2ca4c000975b1c91dfb775cb9c7c</p><p>ESP Preferences Configuration in B: SA #1:IPv4|10.203.199.109|10.203.199.126|* Encrypt Algorithm #1 : aes-cbc Authentication Algorithm #1:hmac-sha1-96 Encryption Key #1 : 0x1cbc2ca4c000975b1c91dfb775cb9c7c Authentication Key #1:x9fb4979b6d5807f7ca83e33c1c9cc993b6a93a7e</p><p>SA #2: IPV4|10.203.199.126|10.203.199.109|* Encrypt Algorithm #2 :aes-cbc Authentication Algorithm #2:hmac-sha1-96 Encryption Key #2 : 0xc84d1235c49a83caadc9a330513ab281 Authentication Key #2:0x4e40e2628b172f0331393242f29ab1eba951c825</p><p>I've enabled "attempt to detect/decode encrypted ESP payloads" and "Attempt to check ESP Authentication" and both A and B are running Linux kernel version:2.6.18.1 and</p><p>Regards, Sethu</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-not" rel="tag" title="see questions tagged &#39;not&#39;">not</span> <span class="post-tag tag-link-decoded" rel="tag" title="see questions tagged &#39;decoded&#39;">decoded</span> <span class="post-tag tag-link-response" rel="tag" title="see questions tagged &#39;response&#39;">response</span> <span class="post-tag tag-link-preferences" rel="tag" title="see questions tagged &#39;preferences&#39;">preferences</span> <span class="post-tag tag-link-esp" rel="tag" title="see questions tagged &#39;esp&#39;">esp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Dec '10, 05:36</strong></p><img src="https://secure.gravatar.com/avatar/a7b575b26261c85de00417df123887dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sethuraman&#39;s gravatar image" /><p><span>Sethuraman</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sethuraman has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-1508" class="comments-container"></div><div id="comment-tools-1508" class="comment-tools"></div><div class="clear"></div><div id="comment-1508-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1536"></span>

<div id="answer-container-1536" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1536-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1536-score" class="post-score" title="current number of votes">0</div><span id="post-1536-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your setup looks oke, apart from the ancient Wireshark version. Please take the capture and load it, and the configuration, in Wireshark 1.4.2 and see what comes out.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Dec '10, 02:48</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-1536" class="comments-container"></div><div id="comment-tools-1536" class="comment-tools"></div><div class="clear"></div><div id="comment-1536-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

