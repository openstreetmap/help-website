+++
type = "question"
title = "capture length with 60 bytes"
description = '''Hi, I have, on my hp switch log with : &quot;A device on port 24 is transmitting packets shorter than 64 bytes or longer than 1518 bytes (longer than 1522 bytes if tagged), with valid CRCs&quot; I capture the traffic with monitoring the port in default and a lot of packets have a length of 60 bytes, can i con...'''
date = "2011-12-05T07:26:00Z"
lastmod = "2011-12-05T07:36:00Z"
weight = 7769
keywords = [ "networks", "troubleshooting" ]
aliases = [ "/questions/7769" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [capture length with 60 bytes](/questions/7769/capture-length-with-60-bytes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7769-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have, on my hp switch log with : "A device on port 24 is transmitting packets shorter than 64 bytes or longer than 1518 bytes (longer than 1522 bytes if tagged), with valid CRCs"</p><p>I capture the traffic with monitoring the port in default and a lot of packets have a length of 60 bytes, can i conclude that the equipement connected to my procurve send wrong packet ?</p><p>Thanks for the reponse</p><p>Best regards</p></div><div id="question-tags" class="tags-container tags">networks troubleshooting</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '11, 07:26</strong></p><img src="https://secure.gravatar.com/avatar/9c9bbe0dcb147699a3a5d92dfff582ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="networkmanager&#39;s gravatar image" /><p>networkmanager<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="networkmanager has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Dec '11, 07:29</p></div></div><div id="comments-container-7769" class="comments-container"></div><div id="comment-tools-7769" class="comment-tools"></div><div class="clear"></div><div id="comment-7769-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7772"></span>

<div id="answer-container-7772" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7772-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, because Wireshark will not capture the FCS (Frame Check Sequence), which is 4 bytes, so actually you have to add 4 bytes in mind to each frame you capture. So each 64 byte packet on the wire is displayed as 60 bytes in the capture file - unless you have a special capture device that will capture the FCS as well, but those are usually special capture devices.</p><p>By the way, packets that are too long or too short will be dropped by the switch on reception, so you won't even see it on your monitoring port, because it doesn't get there.</p><p>Maybe you have a device with Jumbo Frames enabled that will result in messages like that; otherwise it will be difficult to find out what is causing this message. You'd need to access the link in question (port 24 as it seems) with a Hub or TAP and a capture device that can record broken frames, which rules out any standard PC NIC - because a "normal" NIC will also drop broken frames, so Wireshark won't see it even if it was there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '11, 07:34</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-7772" class="comments-container"></div><div id="comment-tools-7772" class="comment-tools"></div><div class="clear"></div><div id="comment-7772-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7773"></span>

<div id="answer-container-7773" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7773-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, the reason that you see 60 bytes frames in Wireshark is because the NIC verifies the frame-check-sequence (FCS, which HP denotes as CRC) and strips it before Wireshark gets the packets (from libpcap/winpcap).</p><p>I suspect that the only way to see which frames are actually to short or to long, you will need to insert a TAP between port 24 of the switch and the system(s) that are connected to it. As I suspect that the HP switch drops the frames which are too short or too long.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '11, 07:36</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-7773" class="comments-container"></div><div id="comment-tools-7773" class="comment-tools"></div><div class="clear"></div><div id="comment-7773-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

