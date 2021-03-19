+++
type = "question"
title = "Not finding raw ethernet packets"
description = '''I&#x27;m wondering if there might be incoming raw ethernet packets received by my computer, but being rejected or somehow hidden from wireshark and if this is the case I&#x27;m wondering how to stop them from being rejected. I have a little hardware setup where I communicate with an FPGA from my computer usin...'''
date = "2015-07-22T14:24:00Z"
lastmod = "2015-07-23T13:46:00Z"
weight = 44388
keywords = [ "windows", "capture", "wireshark", "ubuntu", "ethernet" ]
aliases = [ "/questions/44388" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Not finding raw ethernet packets](/questions/44388/not-finding-raw-ethernet-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44388-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44388-score" class="post-score" title="current number of votes">0</div><span id="post-44388-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm wondering if there might be incoming raw ethernet packets received by my computer, but being rejected or somehow hidden from wireshark and if this is the case I'm wondering how to stop them from being rejected.</p><p>I have a little hardware setup where I communicate with an FPGA from my computer using an ethernet cable and a protocol which uses raw ethernet packets (i.e. they are not encapsulated in high other higher level protocols such as TCP or IP). I have set up this system with various machines and OSes including a couple different versions of Scientific Linux as well as Windows.</p><p>However, I have run into trouble getting this to work recently on two laptops I have been trying to setup. Despite installing the software, and using wireshark to confirm that I am in fact sending out the correct ethernet packets to the FPGA I see nothing coming back. By simply switching the ethernet cable I'm able to use a different computer to talk to the same FPGA with the same firmware and I can check that the packets being sent to the FPGA are identical in both cases. Yet when using either of these two laptops with which I'm having trouble I get nothing back.</p><p>I'm not a networking expert by any means, so I'm wondering if someone might have a plausible explanation (and solution!) for this. I'm wondering if its possible that these raw ethernet packets are being rejected by the laptops for some kind of security or other reason before wireshark can spy on them?</p><p>One of the laptops is an HP running Ubuntu 14.04 with a RealTek RTL8101E/RTL8102E PCI Express Fast Ethernet controller the other is an ASUS running windows (apologies, I don't have access to it at the moment so I can't give any more details as to OS version or hardware).</p><p>Please let me know if there's any important information I might have left out.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span> <span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jul '15, 14:24</strong></p><img src="https://secure.gravatar.com/avatar/6309c30455b6c0f52bb2a45f53c63880?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ignnt&#39;s gravatar image" /><p><span>Ignnt</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ignnt has no accepted answers">0%</span></p></div></div><div id="comments-container-44388" class="comments-container"><span id="44398"></span><div id="comment-44398" class="comment"><div id="post-44398-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Despite installing the software</p></blockquote><p>To which software are you referring here? What is the software that's supposed to be receiving the packets from the FPGA?</p><blockquote><p>I see nothing coming back</p></blockquote><p>So the software in question isn't, in fact, seeing those packets?</p></div><div id="comment-44398-info" class="comment-info"><span class="comment-age">(22 Jul '15, 17:48)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="44408"></span><div id="comment-44408" class="comment"><div id="post-44408-score" class="comment-score"></div><div class="comment-text"><p>The software I was referring to is a custom program designed for interacting with this particular hardware setup. I'm using Wireshark mostly for debugging. I have, on other set ups using linux, had to set up a pipe with a root user account to make the packets available to non root users, but this doesn't seem to make a difference on my system.</p><p>Neither Wireshark nor the custom software I'm using seem to be seeing the packets, but given that all of the hardware on the other end of the Ethernet connection is the same and the outgoing packets are the same my best guess is that the FPGA is in fact sending the packets.</p><p>Thanks.</p></div><div id="comment-44408-info" class="comment-info"><span class="comment-age">(23 Jul '15, 01:26)</span> <span class="comment-user userinfo">Ignnt</span></div></div><span id="44418"></span><div id="comment-44418" class="comment"><div id="post-44418-score" class="comment-score"></div><div class="comment-text"><p>Are you capturing in promiscuous mode?</p><p>I infer from "I have a little hardware setup where I communicate with an FPGA from my computer using an ethernet cable" that you just have an Ethernet cable between your computer and the device with the FPGA, i.e. no hub or switch connects them. Is that correct?</p></div><div id="comment-44418-info" class="comment-info"><span class="comment-age">(23 Jul '15, 12:23)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="44419"></span><div id="comment-44419" class="comment"><div id="post-44419-score" class="comment-score"></div><div class="comment-text"><p>Yes, I am capturing in promiscuous mode. Should this in theory capture anything being sent on the line?</p><p>And yes, you're right it's just a direct ethernet connection from the computer to the FPGA.</p></div><div id="comment-44419-info" class="comment-info"><span class="comment-age">(23 Jul '15, 12:49)</span> <span class="comment-user userinfo">Ignnt</span></div></div></div><div id="comment-tools-44388" class="comment-tools"></div><div class="clear"></div><div id="comment-44388-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44420"></span>

<div id="answer-container-44420" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44420-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44420-score" class="post-score" title="current number of votes">1</div><span id="post-44420-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, capturing in promiscuous mode should show you <em>all</em> packets - or, at least, all packets that the hardware doesn't reject due to some form of malformation, such as an invalid CRC, although some adapters on some OSes with some drivers might even let those through in promiscuous mode.</p><p>It might be interesting to <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_an_Ethernet_hub">get a true Ethernet hub (not a switched hub) and plug your laptop, the device with the FPGA, and one of the machines on which this <em>does</em> work into the hub</a>, and use the machine on which this <em>does</em> work as a passive sniffer, or <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet#Capture_using_a_network_tap">to do something similar with a network tap</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '15, 13:02</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-44420" class="comments-container"><span id="44421"></span><div id="comment-44421" class="comment"><div id="post-44421-score" class="comment-score"></div><div class="comment-text"><p>Great, thanks for the info. I'll see if I can set up one of the sniffers you suggest (and if I can, I will let you know the results). Not sure if there's a handy hub I can use, but I would like to set this up to check regardless. Thanks again for the help.</p></div><div id="comment-44421-info" class="comment-info"><span class="comment-age">(23 Jul '15, 13:46)</span> <span class="comment-user userinfo">Ignnt</span></div></div></div><div id="comment-tools-44420" class="comment-tools"></div><div class="clear"></div><div id="comment-44420-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

