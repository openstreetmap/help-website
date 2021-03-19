+++
type = "question"
title = "9641GS phone capture RTP packets"
description = '''I am trying to do some testing of SRTP packets with an Avaya 9641GS phone. I have my computer plugged into the PC port on the phone. I turned on just normal RTP packets and I am not seeing the traffic in wireshark. I am using G711Ulaw 64k codec (just in case it matters). I wanted to show the RTP pac...'''
date = "2016-12-15T14:27:00Z"
lastmod = "2016-12-15T16:02:00Z"
weight = 58148
keywords = [ "9641gs", "avaya", "rtp" ]
aliases = [ "/questions/58148" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [9641GS phone capture RTP packets](/questions/58148/9641gs-phone-capture-rtp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58148-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to do some testing of SRTP packets with an Avaya 9641GS phone. I have my computer plugged into the PC port on the phone. I turned on just normal RTP packets and I am not seeing the traffic in wireshark. I am using G711Ulaw 64k codec (just in case it matters). I wanted to show the RTP packets when SRTP was turned off and then no packets when SRTP was used showing it was actually working as intended.</p><p>Oddly enough, I saw some RTP traffic but not consistently with an old version of wireshark. I upgraded to 2.2.3 and I do not see any RTP packets anymore. I made sure that Analyze&gt;Enabled Protocols&gt;RDP_UDP along with all the other options for RTP. I feel like I am missing something silly but I can not figure it out for the life of me. Any and all help would be greatly appreciated.</p></div><div id="question-tags" class="tags-container tags">9641gs avaya rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '16, 14:27</strong></p><img src="https://secure.gravatar.com/avatar/7e95d4256fac1843538059f8cec35815?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="critchey880&#39;s gravatar image" /><p>critchey880<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="critchey880 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Dec '16, 14:29</p></div></div><div id="comments-container-58148" class="comments-container"></div><div id="comment-tools-58148" class="comment-tools"></div><div class="clear"></div><div id="comment-58148-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58154"></span>

<div id="answer-container-58154" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58154-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You're not going to see the phone's signaling/media traffic by capturing off of the PC port.</p><p>Think of that phone as a 3 port switch. The LAN port [1], the PC Port [2], and the internal port for phone application [3]. Unless that particular model has a mirroring/span function, which I don't think it does, you will only see broadcast/multicast traffic from the VoIP application of the phone.</p><p>I recommend getting yourself a mirroring switch or TAP. Dualcomm makes a great little switchTAP that won't break the bank.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Dec '16, 16:02</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p>Rooster_50<br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Dec '16, 16:06</p></div></div><div id="comments-container-58154" class="comments-container"><span id="58170"></span><div id="comment-58170" class="comment"><div id="post-58170-score" class="comment-score"></div><div class="comment-text"><p>Thanks that is what I missing. My switch does allow mirroring and I was able to see the packets as expected finally. I did notice something off though.</p><p>Everything worked exactly as expected using RTP. I saw the packets, captured the phone call, and could play back the audio. The interesting part was when I used SRTP. My understanding was that wireshark could not see the SRTP packets but it actually did see the packets as RTP. It captured the phone call and even allowed me playback. The wavelengths were completely different and the only playback was static.</p><p>So my test worked showing that SRTP was working, it just worked in an unexpected way (unexpected by me).</p><p>Thanks for the information I appreciate the help.</p></div><div id="comment-58170-info" class="comment-info"><span class="comment-age">(16 Dec '16, 08:18)</span> critchey880</div></div><span id="58171"></span><div id="comment-58171" class="comment"><div id="post-58171-score" class="comment-score"></div><div class="comment-text"><p>SRTP only encrypts the payload (i.e. voice samples). The headers are still there, so Wirehsark is able to interpret the RTP packets.</p></div><div id="comment-58171-info" class="comment-info"><span class="comment-age">(16 Dec '16, 09:20)</span> Rooster_50</div></div><span id="58172"></span><div id="comment-58172" class="comment"><div id="post-58172-score" class="comment-score"></div><div class="comment-text"><p>See <a href="https://tools.ietf.org/html/rfc3711#section-3.1">here</a>.</p></div><div id="comment-58172-info" class="comment-info"><span class="comment-age">(16 Dec '16, 10:01)</span> Jaap ♦</div></div></div><div id="comment-tools-58154" class="comment-tools"></div><div class="clear"></div><div id="comment-58154-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

