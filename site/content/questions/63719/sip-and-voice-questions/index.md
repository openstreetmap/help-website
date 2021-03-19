+++
type = "question"
title = "SIP and Voice Questions"
description = '''Hello, I have recently introduced SIP into our network and I&#x27;m having a hard time tracking down some intermittent phone quality issues. Before, I can track down my issues I need to understand why Wireshark is behaving the way it is. when I run a capture on my SIP proxy box and open up Telephony-&amp;gt;...'''
date = "2017-10-06T12:51:00Z"
lastmod = "2017-10-07T01:21:00Z"
weight = 63719
keywords = [ "and", "player", "sip", "question", "rtp" ]
aliases = [ "/questions/63719" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SIP and Voice Questions](/questions/63719/sip-and-voice-questions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63719-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have recently introduced SIP into our network and I'm having a hard time tracking down some intermittent phone quality issues. Before, I can track down my issues I need to understand why Wireshark is behaving the way it is.</p><p>when I run a capture on my SIP proxy box and open up Telephony-&gt;VOIP Calls and find a call that I'm interested in listening to. Sometimes when I click on the file and hit play stream the RTP player opens up but there is nothing in the box that shows source address port etc....so I cannot play the file why is that? Then I will find other calls that show codec is unsupported as there g729 calls. I found an article on WS showing the process to do this is that still valid as I'm running 2.1.1?</p><p>On my PBX there is a section where I can turn on voice stats and there are calls with a large number of packet loss. At the time there's no congestion on the WAN link or issues with the phone's LAN switchport so I'm trying to track down what's the root cause of my packet loss. I've got high loss with G711 and G729. I am new to SIP so if anyone has any pointers please let me know.</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags">and player sip question rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Oct '17, 12:51</strong></p><img src="https://secure.gravatar.com/avatar/a6414c2ff8204ee9c4a3bc2a646c4644?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rock90&#39;s gravatar image" /><p>rock90<br />
<span class="score" title="21 reputation points">21</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rock90 has no accepted answers">0%</span></p></div></div><div id="comments-container-63719" class="comments-container"></div><div id="comment-tools-63719" class="comment-tools"></div><div class="clear"></div><div id="comment-63719-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63725"></span>

<div id="answer-container-63725" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63725-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>One, this is somewhat of a grab bag of questions, probably more suitable for wireshark-users mailing list, but here goes with some answers.</p><ul><li>Make sure the network is clean (easier said than done), voice it time critical. That means network elements and nodes need to meet real time constraints.</li><li>There are various ways to get at RTP stream analysis. Results depend on the presence of SIP/SDP info in your capture.</li><li>'An article' is hard to comment on, but if it refers to saving the RTP payload as raw and then post process, this should still be ok.</li><li>Wireshark 2.1.1 is some weird intermediate development version, which at best is unsupported. See if you can move to improved release version, eg. 2.4.1</li><li>Does G.729 include silence suppression? That may trip up certain tools.</li><li>High loss could be anything, from blocked ports, unidirectional flows, incorrect timestamps, underflowing jitter buffers and what not.</li></ul><p>It may take a lot of drilling down into various system parts to get all blockages out.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '17, 01:21</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-63725" class="comments-container"><span id="63726"></span><div id="comment-63726" class="comment"><div id="post-63726-score" class="comment-score">1</div><div class="comment-text"><p>SIP is just the control part. RTP is what you have to concentrate at.</p><p>G.729 did not work for me even in 2.4.1, I had to install 2.5.0-something to get the G.729 player to work.</p><p>Newer codecs cannot be played at all either because their patents are still in force so they cannot be bundled to GPL software, or because no one has implemented them even though they aren't patended. But that shouldn't bother you as you only really need to playback the captures if you are sure that the network is perfect and you want to confirm that the sound inside the RTP stream was garbled already when the RTP packet was being formed.</p><p>As <a href="https://ask.wireshark.org/users/4/jaap"></a><a href="https://ask.wireshark.org/users/4/jaap">@Jaap</a> wrote, voice is time critical. Each VoIP equipment sets up its own compromise between requirements to the smallest possible microphone-to-speaker delay and to the highest possible tolerance to jitter (irregularity of packet delivery times between source and destination) by intentionally delaying playback of received packets by temporarily storing them in a buffer. So if a given RTP packet arrives too late to be played in its due time, there is an audible gap in the playback.</p><p>Therefore, even if no RTP packets are actually lost, they may be reported as such by the codec (and thus in the statistics of your PBX), because it didn't have them when it needed them.</p><p>In the Wireshark player you can simulate a jitter buffer size to see and hear how that stream would be handled by a receiver with such jitter buffer size, but you usually do not know what size the receiver in question actually uses, leaving aside that it may even dynamically change.</p><p>So I'd capture right in front of each of the two endpoints of the RTP flow and compare the jitter and RTP sequence numbers at sending and receiving side. If some RTP sequence numbers are missing at receiving side although they exist at the sending side, there is a real packet loss in the network. If the RTP packets come to the receiving side irregularly, or even do not come in monotonously ascending order of the sequence numbers, find out where this comes from. Years ago I've seen devices delaying some packets for seconds which must have been a bug, but delays above 50 ms may already cause audio problems depending on settings of the receiver's dejittering buffer. Multiple paths through networks, large packets on slow lines, and wrongly configured QoS (packet prioritization) rules are most frequent causes of jitter.</p></div><div id="comment-63726-info" class="comment-info"><span class="comment-age">(07 Oct '17, 05:32)</span> sindy</div></div><span id="63758"></span><div id="comment-63758" class="comment"><div id="post-63758-score" class="comment-score"></div><div class="comment-text"><p>Thank you both for responding.</p></div><div id="comment-63758-info" class="comment-info"><span class="comment-age">(09 Oct '17, 05:09)</span> rock90</div></div></div><div id="comment-tools-63725" class="comment-tools"></div><div class="clear"></div><div id="comment-63725-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

