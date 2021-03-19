+++
type = "question"
title = "Wireshark reporting different parameters in different machines"
description = '''I have Wireshark installed in two laptops, one injecting custom packets into the network and another sniffing these injected packets. When I transmit the packets using the fist machine (Macbook Pro using Broadcom BCM 4331 interface card), I am able to see these packets in Wireshark with all the vari...'''
date = "2012-06-18T15:58:00Z"
lastmod = "2012-06-18T16:38:00Z"
weight = 12032
keywords = [ "wireless", "radiotap", "wireshark" ]
aliases = [ "/questions/12032" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark reporting different parameters in different machines](/questions/12032/wireshark-reporting-different-parameters-in-different-machines)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12032-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have Wireshark installed in two laptops, one injecting custom packets into the network and another sniffing these injected packets. When I transmit the packets using the fist machine (Macbook Pro using Broadcom BCM 4331 interface card), I am able to see these packets in Wireshark with all the various fields such as SSI, Noise etc.</p><p>But the Wireshark installed on the other machine (Dell Latitude E6410 using the Intel Corporation Centrino Ultimate-N 6300 interface card) shows the radio-tap header to be of length 18 only, and is missing parameters like Noise and timestamp.</p><p>Could anyone explain why this is happening? Is it because different wireless drivers treat radio-tap in a different way? If so, how can I get the missing parameters like background noise?</p><p>I have attached screen-shots of wireshark running on the two machines.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Mac.png" alt="Wireshark-running-on-MacbookPro" /> <img src="https://osqa-ask.wireshark.org/upfiles/Screenshot_from_2012-06-18_11:36:04_1.png" alt="Wireshark-running-on-Dell" /></p></div><div id="question-tags" class="tags-container tags">wireless radiotap wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jun '12, 15:58</strong></p><img src="https://secure.gravatar.com/avatar/c8295900dc6e2ff2fccacb803179e07f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hektor&#39;s gravatar image" /><p>hektor<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hektor has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 18 Jun '12, 19:04</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></img></div></div><div id="comments-container-12032" class="comments-container"></div><div id="comment-tools-12032" class="comment-tools"></div><div class="clear"></div><div id="comment-12032-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12034"></span>

<div id="answer-container-12034" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12034-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Some wirless network interaces do not make the additional information available. The details are dependent on the OS involved, the Wireshark version, and the mode you have set up in the interface. There is a good discussion at <a href="http://wiki.wireshark.org/CaptureSetup/WLAN#Link-Layer_.28Radio.29_packet_headers">http://wiki.wireshark.org/CaptureSetup/WLAN#Link-Layer_.28Radio.29_packet_headers</a> which should get you started.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jun '12, 16:38</strong></p><img src="https://secure.gravatar.com/avatar/b64129b7a3bf2a9f1760fbdee1b3b74c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="inetdog&#39;s gravatar image" /><p>inetdog<br />
<span class="score" title="167 reputation points">167</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="inetdog has 3 accepted answers">14%</span></p></div></div><div id="comments-container-12034" class="comments-container"><span id="12061"></span><div id="comment-12061" class="comment"><div id="post-12061-score" class="comment-score"></div><div class="comment-text"><p>I am using airmon-ng to create the monitor interface and inject packets through it. All packets sniffed through the monitor interface in Wireshark running on the receiver machine show the radio-tap header to be malformed. I'm not sure whether this is a problem in the way i am constructing the packet using the radio-tap and ieee80211 headers. If it was, the packets wouldn't be able to go through right? Or could it be some sort of bug in Wireshark?</p><p>If the additional information is not available through Wireshark, is there another way through which i can determine these paramters?</p></div><div id="comment-12061-info" class="comment-info"><span class="comment-age">(19 Jun '12, 09:10)</span> hektor</div></div></div><div id="comment-tools-12034" class="comment-tools"></div><div class="clear"></div><div id="comment-12034-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

