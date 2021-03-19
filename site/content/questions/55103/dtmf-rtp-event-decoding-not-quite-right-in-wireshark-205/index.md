+++
type = "question"
title = "&quot;DTMF RTP EVENT&quot; decoding not quite right in Wireshark 2.0.5"
description = '''I ran into an issue with Wireshark 2.0.5 not decoding one direction of DTMF Relay (RFC2833). In the attached trace, the DTMF events are decoded when coming from 10.0.0.12, but when coming from 192.168.21.55 it just shows...[Payload type: DynamicRTP-Type-96 (96)] Now, I have a very old version of Wir...'''
date = "2016-08-24T20:47:00Z"
lastmod = "2016-08-25T04:04:00Z"
weight = 55103
keywords = [ "rtpevent", "sdp", "rtp", "voip", "dtmf" ]
aliases = [ "/questions/55103" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# ["DTMF RTP EVENT" decoding not quite right in Wireshark 2.0.5](/questions/55103/dtmf-rtp-event-decoding-not-quite-right-in-wireshark-205)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55103-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I ran into an issue with Wireshark 2.0.5 not decoding one direction of DTMF Relay (RFC2833).</p><p>In the attached trace, the DTMF events are decoded when coming from 10.0.0.12, but when coming from 192.168.21.55 it just shows...[Payload type: DynamicRTP-Type-96 (96)]</p><p>Now, I have a very old version of Wireshark still loaded because of some needed plugins that only run on version 99.6a. I decided to open in that version, and it decodes perfectly.</p><p>Has anyone else run into this issue, or does it seem to be an isolated case due to something I am doing?</p><p>Thanks for any help/input anyone can provide.</p><p>Travis</p><p>PCAP DOWNLOAD LINK --=&gt; <a href="https://drive.google.com/file/d/0B-1XjlBS4UNxX283YXdBbWZucG8/view">DTMF_RTP-EVENT.pcap</a></p></div><div id="question-tags" class="tags-container tags">rtpevent sdp rtp voip dtmf</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Aug '16, 20:47</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p>Rooster_50<br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Aug '16, 20:48</p></div></div><div id="comments-container-55103" class="comments-container"></div><div id="comment-tools-55103" class="comment-tools"></div><div class="clear"></div><div id="comment-55103-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55111"></span>

<div id="answer-container-55111" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55111-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please, <a href="https://bugs.wireshark.org/bugzilla/enter_bug.cgi">file a bug</a> and place its number to a comment here.</p><p>Grounds: the SDP in the 200 OK is decoded properly, the<br />
<code>a=rtpmap:96 telephone-event/8000</code><br />
is there and at proper place, so the VoIP call tracker should have no issues to identify the RTP packets with payload type number 96 as telephone-event (RFC2833) ones also in the calling -&gt; called direction.</p><p>As a quick workaround, you may open the preferences of <code>RTP Event</code> protocol (through <code>Edit-&gt;Preferences...-&gt;Protocols-&gt;RTP Event</code> or by right-clicking the <code>RFC 2833 RTP Event</code> line in the packet dissection pane of the packet which was auto-detected and choosing <code>Protocol preferences</code> from the context menu) and change the value of the <code>Payload Type for RFC2833 RTP Events</code> parameter from the default 101 to your 96.</p><p>But don't forget to file the bug.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Aug '16, 04:04</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span> </br></br></p></div></div><div id="comments-container-55111" class="comments-container"><span id="55115"></span><div id="comment-55115" class="comment"><div id="post-55115-score" class="comment-score"></div><div class="comment-text"><p>Will do, thanks Sindy</p></div><div id="comment-55115-info" class="comment-info"><span class="comment-age">(25 Aug '16, 07:45)</span> Rooster_50</div></div><span id="55118"></span><div id="comment-55118" class="comment"><div id="post-55118-score" class="comment-score"></div><div class="comment-text"><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12788">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12788</a></p></div><div id="comment-55118-info" class="comment-info"><span class="comment-age">(25 Aug '16, 09:33)</span> Rooster_50</div></div></div><div id="comment-tools-55111" class="comment-tools"></div><div class="clear"></div><div id="comment-55111-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

