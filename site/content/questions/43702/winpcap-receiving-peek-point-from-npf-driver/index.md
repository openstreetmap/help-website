+++
type = "question"
title = "winpcap receiving peek point from npf driver"
description = '''Hi All,  This is karun from india(Hyderabad) of Redpine signals.Actually I want to give my own packet inorder to display in wireshark.So i am going through the source code of Wireshark and winpcap(as it is the capturing library,driver).I figured out the peek point where packet.dll is used for packet...'''
date = "2015-06-29T22:34:00Z"
lastmod = "2015-06-30T21:48:00Z"
weight = 43702
keywords = [ "winpcap" ]
aliases = [ "/questions/43702" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [winpcap receiving peek point from npf driver](/questions/43702/winpcap-receiving-peek-point-from-npf-driver)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43702-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43702-score" class="post-score" title="current number of votes">0</div><span id="post-43702-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><pre><code>    This is karun from india(Hyderabad) of Redpine signals.Actually I want to give my own packet inorder to display in wireshark.So i am going through the source code of Wireshark and winpcap(as it is the capturing library,driver).I figured out the peek point where packet.dll is used for packet capturing from nfs driver as described below.

    Wireshark&lt;--wpcap.dll&lt;--packet.dll&lt;--npf.sys(driver where actual capture happens)&lt;-packets.

    pcap_read_win32_npf()-&gt;PacketReceivePacket() function in wpcap/libpcap/pcap-win32.c.

    So i hard coded my known packet format after returning from PacketReceivepacket() function in winpcap 4.1.3 source code.And after compilation and copied the packet.dll,wpacp.dll,&amp; ndf.sys to their respective folders,i am able to see my known packet in wireshark application as LLC packet,but along with mine some other packets so called UDP,LMNR,NBNS,SSDP,ARP packets are also coming to the wireshark&#39;s application.Can any one tell me where these packets are coming as pcap_read_win32_npf is the only function to capture packets(to best of my knowledge).</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-winpcap" rel="tag" title="see questions tagged &#39;winpcap&#39;">winpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jun '15, 22:34</strong></p><img src="https://secure.gravatar.com/avatar/50c4b78862c6ca806916c3a71498cdf3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="karun256&#39;s gravatar image" /><p><span>karun256</span><br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="karun256 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Jun '15, 22:44</strong> </span></p></div></div><div id="comments-container-43702" class="comments-container"></div><div id="comment-tools-43702" class="comment-tools"></div><div class="clear"></div><div id="comment-43702-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43765"></span>

<div id="answer-container-43765" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43765-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43765-score" class="post-score" title="current number of votes">0</div><span id="post-43765-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi I am getting my hard coded packet,other packets are not coming its because of memory issue i used memset before calling PacketReceivePacket function and copied my packet using memcpy.Now its working fine.I ma able to see my packet ,now challenge is to update timestamp,I am getting the 0.0000 time stamp for my every packet,can any one tell me where i can find the time stamp updation.</p><p>Thanks, karun.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jun '15, 21:48</strong></p><img src="https://secure.gravatar.com/avatar/50c4b78862c6ca806916c3a71498cdf3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="karun256&#39;s gravatar image" /><p><span>karun256</span><br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="karun256 has no accepted answers">0%</span></p></div></div><div id="comments-container-43765" class="comments-container"></div><div id="comment-tools-43765" class="comment-tools"></div><div class="clear"></div><div id="comment-43765-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

