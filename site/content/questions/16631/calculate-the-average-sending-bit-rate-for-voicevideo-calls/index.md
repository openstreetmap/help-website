+++
type = "question"
title = "Calculate the average sending bit rate for Voice/Video Calls"
description = '''I made an Voice/Video phone call in an easy Asterisk environment User1000--------Asterisk Server---------User2000 Then I captured the traffic using wireshark. Code: Voice G.711 Video H.263 So, How to calculate the &#x27;average sending bit rate&#x27; for voice / video ? Someone told me that the Wireshark--&amp;gt...'''
date = "2012-12-06T04:20:00Z"
lastmod = "2012-12-07T16:15:00Z"
weight = 16631
keywords = [ "hierarchy", "voice", "sendingbitrate", "video" ]
aliases = [ "/questions/16631" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Calculate the average sending bit rate for Voice/Video Calls](/questions/16631/calculate-the-average-sending-bit-rate-for-voicevideo-calls)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16631-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I made an Voice/Video phone call in an easy Asterisk environment User1000--------Asterisk Server---------User2000</p><p>Then I captured the traffic using wireshark.</p><p>Code: Voice G.711 Video H.263</p><p>So, How to calculate the 'average sending bit rate' for voice / video ? Someone told me that the Wireshark--&gt;Statistics--&gt;protocol hierarchy could do this. So, I went to see the details of it. But there are only 'Mbit/s' and 'End Mbit/s'.</p><p>I found that the Packet number of 'RTP' is 30392 and the packet number of 'ITU-T Recommendation H.263' is 8979. Then, the 'end packets' of 'RTP' is 21413 (maybe is 30392-8979). So, I guess maybe I should use 'End Mbit/s' of RTP as the 'average sending bit rate' of voice packets and the 'End Mbit/s' of 'ITU-T Recommendation H.263' as the 'average sending bit rate' of video packets. Does these correct ?</p><p>Thanks for your help !</p><p>CARL</p></div><div id="question-tags" class="tags-container tags">hierarchy voice sendingbitrate video</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Dec '12, 04:20</strong></p><img src="https://secure.gravatar.com/avatar/ea0aa05a9bccde4884b3616ab8f6a12d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CARL%20YU&#39;s gravatar image" /><p>CARL YU<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CARL YU has no accepted answers">0%</span></p></div></div><div id="comments-container-16631" class="comments-container"></div><div id="comment-tools-16631" class="comment-tools"></div><div class="clear"></div><div id="comment-16631-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16716"></span>

<div id="answer-container-16716" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16716-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well the payload size for the voice is worked out as 64kbps for the sampling rate with 10ms sampling intervals = (64*10)/8 = 80 bytes the default voice payload size is 20ms which = 160 Bytes for G.711</p><p>for the H.263 i am struggling to find info on for my assignment aswell ;)</p><p>source for the voice: <a href="http://www.cisco.com/en/US/tech/tk652/tk698/technologies_tech_note09186a0080094ae2.shtml">http://www.cisco.com/en/US/tech/tk652/tk698/technologies_tech_note09186a0080094ae2.shtml</a> &amp; lecture slides</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '12, 16:15</strong></p><img src="https://secure.gravatar.com/avatar/8f824ff6080ef3a67843f43803a619cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vade&#39;s gravatar image" /><p>vade<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vade has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Dec '12, 16:17</p></div></div><div id="comments-container-16716" class="comments-container"></div><div id="comment-tools-16716" class="comment-tools"></div><div class="clear"></div><div id="comment-16716-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

