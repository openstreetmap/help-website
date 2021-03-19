+++
type = "question"
title = "bytes on wire vs. bytes captured"
description = '''hi guys,  can you please tell me, what is the difference between Bytes on wire vs. bytes captured   Bytes on wire = 550 bytes. The log of the application I&#x27;m working with says &quot;Sending 508 bytes to&quot;.  8 bytes UDP Header + 20 TCP + 14 Eth II = 550 bytes  what is this value bytes captured ?  Next what...'''
date = "2015-09-25T05:55:00Z"
lastmod = "2015-09-27T14:32:00Z"
weight = 46163
keywords = [ "flight", "bytes", "in" ]
aliases = [ "/questions/46163" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [bytes on wire vs. bytes captured](/questions/46163/bytes-on-wire-vs-bytes-captured)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46163-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46163-score" class="post-score" title="current number of votes">0</div><span id="post-46163-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi guys,</p><p>can you please tell me, what is the difference between Bytes on wire vs. bytes captured <img src="https://osqa-ask.wireshark.org/upfiles/1_VKfNfXk.JPG" alt="alt text" /></p><p>Bytes on wire = 550 bytes. The log of the application I'm working with says "Sending 508 bytes to".</p><p>8 bytes UDP Header + 20 TCP + 14 Eth II = 550 bytes</p><p>what is this value bytes captured ?</p><p>Next what i don't understand: <img src="https://osqa-ask.wireshark.org/upfiles/2_N18XTdC.JPG" alt="alt text" /></p><p>the UDP "Length" filed =A field that specifies the length in bytes of the UDP header and UDP data.</p><p>wait a minute "UDP header and UDP data" so the Length equals to 516 bytes and Data 54 bytes , sp 516 - 54 = UDP header ??? is it not 8 bytes ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-flight" rel="tag" title="see questions tagged &#39;flight&#39;">flight</span> <span class="post-tag tag-link-bytes" rel="tag" title="see questions tagged &#39;bytes&#39;">bytes</span> <span class="post-tag tag-link-in" rel="tag" title="see questions tagged &#39;in&#39;">in</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '15, 05:55</strong></p><img src="https://secure.gravatar.com/avatar/2b3f26f3a24449776af62dd8cca7715a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adasko&#39;s gravatar image" /><p><span>adasko</span><br />
<span class="score" title="86 reputation points">86</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adasko has no accepted answers">0%</span></p></img></div></div><div id="comments-container-46163" class="comments-container"></div><div id="comment-tools-46163" class="comment-tools"></div><div class="clear"></div><div id="comment-46163-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="46164"></span>

<div id="answer-container-46164" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46164-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46164-score" class="post-score" title="current number of votes">2</div><span id="post-46164-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="adasko has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can look here: <a href="https://blog.packet-foo.com/2015/08/frame-bytes-vs-frame-file-headers/">https://blog.packet-foo.com/2015/08/frame-bytes-vs-frame-file-headers/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '15, 06:05</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p><span>Christian_R</span><br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></img></div></div><div id="comments-container-46164" class="comments-container"><span id="46184"></span><div id="comment-46184" class="comment"><div id="post-46184-score" class="comment-score">1</div><div class="comment-text"><p>96 Bytes captured -(8 UDP Header +20 IP Header +14 ETH Header) = 54 Bytes left for actual captured Data</p><p>Wireshark shows you at this point of the tree only the actual captured data (info)</p></div><div id="comment-46184-info" class="comment-info"><span class="comment-age">(25 Sep '15, 13:21)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-46164" class="comment-tools"></div><div class="clear"></div><div id="comment-46164-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46177"></span>

<div id="answer-container-46177" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46177-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46177-score" class="post-score" title="current number of votes">1</div><span id="post-46177-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When you start a packet capture you can specify how many bytes from a packet you want to capture e.g. the default with tcpdump is 96 bytes. You can change it with the -s option. If you say -s0 you will capture the full packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '15, 11:32</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p><span>Roland</span><br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-46177" class="comments-container"><span id="46178"></span><div id="comment-46178" class="comment"><div id="post-46178-score" class="comment-score"></div><div class="comment-text"><p>ok, so the blog and Roland's comment helped me to understand it, now it's clear but what about the second sreen shot? it says UDP length equals 516 bytes but Data = 54 bytes so how can the UDP header by 8 bytes long ?</p></div><div id="comment-46178-info" class="comment-info"><span class="comment-age">(25 Sep '15, 12:25)</span> <span class="comment-user userinfo">adasko</span></div></div><span id="46181"></span><div id="comment-46181" class="comment"><div id="post-46181-score" class="comment-score"></div><div class="comment-text"><p>What version of Wireshark are you using?</p></div><div id="comment-46181-info" class="comment-info"><span class="comment-age">(25 Sep '15, 12:51)</span> <span class="comment-user userinfo">Roland</span></div></div><span id="46183"></span><div id="comment-46183" class="comment"><div id="post-46183-score" class="comment-score">1</div><div class="comment-text"><p>Only 96 bytes were captured. Subtracting 14 bytes for the Ethernet header, 20 bytes for the IP header, and 8 bytes for the UDP header, leaves 54 bytes of UDP data in the packet captured by Wireshark. In other words, because only 96 bytes were captured, Wireshark only has the first 54 bytes of the 508-byte UDP payload. The 508-byte payload, plus the 8-byte UDP header, addes up to 516 bytes, so that's what is in the Length field of the UDP header, and the Length field is included in the 96 bytes that were captured. That value is the length of the UDP datagram in the original packet as transmitted on the wire, not the truncated packet captured by Wireshark.</p></div><div id="comment-46183-info" class="comment-info"><span class="comment-age">(25 Sep '15, 13:18)</span> <span class="comment-user userinfo">Jim Aragon</span></div></div><span id="46201"></span><div id="comment-46201" class="comment"><div id="post-46201-score" class="comment-score"></div><div class="comment-text"><p>thank you all guys. The link did in fact answer all my question!</p><p>Best Regards</p><p>Adam</p></div><div id="comment-46201-info" class="comment-info"><span class="comment-age">(27 Sep '15, 14:32)</span> <span class="comment-user userinfo">adasko</span></div></div></div><div id="comment-tools-46177" class="comment-tools"></div><div class="clear"></div><div id="comment-46177-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

