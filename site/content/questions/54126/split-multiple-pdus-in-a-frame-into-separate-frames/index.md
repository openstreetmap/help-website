+++
type = "question"
title = "Split multiple PDU&#x27;s in a frame into separate frames?"
description = '''I am capturing MAP, CAMEL, BSSAP, RANAP etc... When the frames come through there are more often than not multiple protocol messages included in a single frame (example below). What I am wondering is there any way in wireshark to split the frame and display only 1 protocol at a time. So as below the...'''
date = "2016-07-18T07:41:00Z"
lastmod = "2016-07-18T09:25:00Z"
weight = 54126
keywords = [ "frames", "map", "frame", "cap", "protocol" ]
aliases = [ "/questions/54126" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Split multiple PDU's in a frame into separate frames?](/questions/54126/split-multiple-pdus-in-a-frame-into-separate-frames)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54126-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am capturing MAP, CAMEL, BSSAP, RANAP etc... When the frames come through there are more often than not multiple protocol messages included in a single frame (example below). What I am wondering is there any way in wireshark to split the frame and display only 1 protocol at a time. So as below there is M3UA:SCCP:TCAP:GSM_MAP:M3UA:SCCP:TCAP:GSM_MAP would like to see 2 messages M3UA:SCCP:TCAP:GSM_MAP and M3UA:SCCP:TCAP:GSM_MAP</p><pre><code>[Protocols in frame: eth:ethertype:ip:sctp:m3ua:sccp:tcap:gsm_map:m3ua:sccp:tcap:gsm_map]

Frame 1134: 406 bytes on wire (3248 bits), 406 bytes captured (3248 bits) on interface 0
    Interface id: 0 ({6B391584-8061-4004-84B2-5D9975BA121D})
    Encapsulation type: Ethernet (1)
    Arrival Time: Jul 18, 2016 08:55:56.493430000 Central Daylight Time
    [Time shift for this packet: 0.000000000 seconds]
    Epoch Time: 1468850156.493430000 seconds
    [Time delta from previous captured frame: 0.000149000 seconds]
    [Time delta from previous displayed frame: 0.027730000 seconds]
    [Time since reference or first frame: 2.027353000 seconds]
    Frame Number: 1134
    Frame Length: 406 bytes (3248 bits)
    Capture Length: 406 bytes (3248 bits)
    [Frame is marked: False]
    [Frame is ignored: False]
    [Protocols in frame: eth:ethertype:ip:sctp:m3ua:sccp:tcap:gsm_map:m3ua:sccp:tcap:gsm_map]
Ethernet II, Src: CiscoInc_a9:f3:c0 (00:19:07:a9:f3:c0), Dst: ba:f3:f1:1b:ec:57 (ba:f3:f1:1b:ec:57)
Internet Protocol Version 4, Src: 192.168.124.5, Dst: 192.168.123.37
Stream Control Transmission Protocol, Src Port: m3ua (2905), Dst Port: 50497 (50497)
MTP 3 User Adaptation Layer
[ANSI_STANDARD]
Signalling Connection Control Part
Transaction Capabilities Application Part
GSM Mobile Application
Stream Control Transmission Protocol
MTP 3 User Adaptation Layer
[ANSI_STANDARD]
Signalling Connection Control Part
Transaction Capabilities Application Part
GSM Mobile Application</code></pre></div><div id="question-tags" class="tags-container tags">frames map frame cap protocol</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jul '16, 07:41</strong></p><img src="https://secure.gravatar.com/avatar/4bc0fe37a8150f1e564b5943078ed660?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michael%20Pierotti&#39;s gravatar image" /><p>Michael Pier...<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michael Pierotti has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Jul '16, 08:58</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-54126" class="comments-container"></div><div id="comment-tools-54126" class="comment-tools"></div><div class="clear"></div><div id="comment-54126-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54129"></span>

<div id="answer-container-54129" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54129-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Take a look at the exported pdu functionality in the latest wireshark version.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jul '16, 09:25</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-54129" class="comments-container"><span id="54130"></span><div id="comment-54130" class="comment"><div id="post-54130-score" class="comment-score"></div><div class="comment-text"><p>Which version? I am running 2.0.4</p></div><div id="comment-54130-info" class="comment-info"><span class="comment-age">(18 Jul '16, 09:41)</span> Michael Pier...</div></div><span id="54133"></span><div id="comment-54133" class="comment"><div id="post-54133-score" class="comment-score"></div><div class="comment-text"><p>Grahamb..... Wow, yeah OSI Layer 3 and I got exactly what I wanted!</p></div><div id="comment-54133-info" class="comment-info"><span class="comment-age">(18 Jul '16, 10:24)</span> Michael Pier...</div></div></div><div id="comment-tools-54129" class="comment-tools"></div><div class="clear"></div><div id="comment-54129-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

