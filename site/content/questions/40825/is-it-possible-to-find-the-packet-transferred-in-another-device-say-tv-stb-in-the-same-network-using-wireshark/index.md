+++
type = "question"
title = "Is it possible to find the packet transferred in another device ( Say TV, STB ) in the same network using wireshark ?"
description = '''Is it possible to find the packet transferred in another device ( Say TV, STB ) in the same network using wireshark ?'''
date = "2015-03-24T21:23:00Z"
lastmod = "2015-03-25T10:19:00Z"
weight = 40825
keywords = [ "transferred", "packet" ]
aliases = [ "/questions/40825" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to find the packet transferred in another device ( Say TV, STB ) in the same network using wireshark ?](/questions/40825/is-it-possible-to-find-the-packet-transferred-in-another-device-say-tv-stb-in-the-same-network-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40825-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40825-score" class="post-score" title="current number of votes">0</div><span id="post-40825-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible to find the packet transferred in another device ( Say TV, STB ) in the same network using wireshark ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-transferred" rel="tag" title="see questions tagged &#39;transferred&#39;">transferred</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Mar '15, 21:23</strong></p><img src="https://secure.gravatar.com/avatar/6403598046ec731fb5fa774a749526a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Magesh%20Gopal%20Sivan%20Devar&#39;s gravatar image" /><p><span>Magesh Gopal...</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Magesh Gopal Sivan Devar has no accepted answers">0%</span></p></div></div><div id="comments-container-40825" class="comments-container"><span id="40831"></span><div id="comment-40831" class="comment"><div id="post-40831-score" class="comment-score"></div><div class="comment-text"><p>The simple answer is yes. A computer with Wireshark and WinPcap will capture all network traffic when connected to a network. Now you need to find some kind of marker in the packet (MAC address, IP address, protocol used, etc.) to determine which packets are coming from/going to the device of interest. Can you post a capture to either dropbox or google drive and provide the link here?</p></div><div id="comment-40831-info" class="comment-info"><span class="comment-age">(25 Mar '15, 06:16)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="40834"></span><div id="comment-40834" class="comment"><div id="post-40834-score" class="comment-score"></div><div class="comment-text"><p>Okay Guys. Can you please tell me how it is ?</p><p>For Example:- My PC IP is :- 10.197.13.88(Runing Wireshark and WinPcap) , My STB Ip is : 10.197.13.89</p><p>If I want to collect the packet transferred between my STB(10.197.13.89) and other STB( Say 10.197.13.90) with Same network.</p><p>What Can I do to collect the packets from my PC.</p><p>Line by line explanation helps me more, For easy understanding.</p><p>Picture representation also help me!!!</p><p>Waiting for your response !!!1</p></div><div id="comment-40834-info" class="comment-info"><span class="comment-age">(25 Mar '15, 06:49)</span> <span class="comment-user userinfo">Magesh Gopal...</span></div></div><span id="40836"></span><div id="comment-40836" class="comment"><div id="post-40836-score" class="comment-score"></div><div class="comment-text"><p>So how are these device connected, wired Ethernet, WiFi or something else?</p></div><div id="comment-40836-info" class="comment-info"><span class="comment-age">(25 Mar '15, 06:51)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="40848"></span><div id="comment-40848" class="comment"><div id="post-40848-score" class="comment-score"></div><div class="comment-text"><p>Please make yourself familiar with the Wiki contents referenced in the answer. This will guide you in the right direction.</p></div><div id="comment-40848-info" class="comment-info"><span class="comment-age">(25 Mar '15, 09:45)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-40825" class="comment-tools"></div><div class="clear"></div><div id="comment-40825-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40832"></span>

<div id="answer-container-40832" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40832-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40832-score" class="post-score" title="current number of votes">0</div><span id="post-40832-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It depends.</p><p>It depends on the network media, is it wired Ethernet or Wireless and it depends on the components in the network, e.g. is there a router, switch or hub.</p><p>Capturing on a broadcast network such as WiFi can be done given a suitable wireless NIC, drivers and OS (note Windows is deficient here, without special hardware such as an AirPCap adaptor). See the Wiki page on <a href="https://wiki.wireshark.org/CaptureSetup/WLAN">Wireless Capture</a>.</p><p>Capturing on a wired network usually needs the cooperation of the switch to mirror traffic, or the insertion of a hub or tap. See the Wiki page on <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">Ethernet Capture</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '15, 06:40</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-40832" class="comments-container"><span id="40841"></span><div id="comment-40841" class="comment"><div id="post-40841-score" class="comment-score"></div><div class="comment-text"><p>It is connected with wired .</p></div><div id="comment-40841-info" class="comment-info"><span class="comment-age">(25 Mar '15, 07:54)</span> <span class="comment-user userinfo">Magesh Gopal...</span></div></div><span id="40842"></span><div id="comment-40842" class="comment"><div id="post-40842-score" class="comment-score"></div><div class="comment-text"><p>OK, so presumably both your PC and the two STB's are connected to a router of some sort, what is that device?</p></div><div id="comment-40842-info" class="comment-info"><span class="comment-age">(25 Mar '15, 07:59)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="40849"></span><div id="comment-40849" class="comment"><div id="post-40849-score" class="comment-score"></div><div class="comment-text"><p>It is a de-link connector.</p></div><div id="comment-40849-info" class="comment-info"><span class="comment-age">(25 Mar '15, 10:00)</span> <span class="comment-user userinfo">Magesh Gopal...</span></div></div><span id="40851"></span><div id="comment-40851" class="comment"><div id="post-40851-score" class="comment-score"></div><div class="comment-text"><p>Presuming you mean a D-Link router, then it's likely acting as a switch and as they're generally "home" class devices it won't easily span or mirror a port. Again I refer you to the Wiki page on <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">Ethernet Capture</a> in particular the section on <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet#Switched_Ethernet">switched Ethernet</a>.</p></div><div id="comment-40851-info" class="comment-info"><span class="comment-age">(25 Mar '15, 10:19)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-40832" class="comment-tools"></div><div class="clear"></div><div id="comment-40832-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

