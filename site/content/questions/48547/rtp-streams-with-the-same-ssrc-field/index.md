+++
type = "question"
title = "RTP streams with the same SSRC field"
description = '''I&#x27;m trying to test a network by sending calls directly between two SIPp instances. However when I try to analyze the stream with wireshark it cannot understand the RTP. It only show a stream in one direction, which has the count of all packets in both directions. I have a suspicion that the problem ...'''
date = "2015-12-15T13:53:00Z"
lastmod = "2015-12-17T12:10:00Z"
weight = 48547
keywords = [ "ssrc", "rtp" ]
aliases = [ "/questions/48547" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [RTP streams with the same SSRC field](/questions/48547/rtp-streams-with-the-same-ssrc-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48547-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to test a network by sending calls directly between two SIPp instances. However when I try to analyze the stream with wireshark it cannot understand the RTP. It only show a stream in one direction, which has the count of all packets in both directions.</p><p>I have a suspicion that the problem lies in the SSRC value which is the same in both directions.</p><pre><code>10    2015-12-15 15:35:02.090403    194.247.61.193 194.247.61.197
RTP    214    PT=ITU-T G.711 PCMA, SSRC=0xC1A0112, Seq=0, Time=0, Mark
11    2015-12-15 15:35:02.094980    194.247.61.197 194.247.61.193
RTP    214    PT=ITU-T G.711 PCMA, SSRC=0xC1A0112, Seq=0, Time=0, Mark</code></pre><p>It is not easy to change the SSRC value in the test. So before I go and recompile something, I would like to hear if this is really a problem to Wireshark, or if I should look else where.</p></div><div id="question-tags" class="tags-container tags">ssrc rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '15, 13:53</strong></p><img src="https://secure.gravatar.com/avatar/b0ac00407121781dba912c3cd3ede4c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kjeld%20Flarup&#39;s gravatar image" /><p>Kjeld Flarup<br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kjeld Flarup has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Dec '15, 13:56</p></div></div><div id="comments-container-48547" class="comments-container"><span id="48548"></span><div id="comment-48548" class="comment"><div id="post-48548-score" class="comment-score"></div><div class="comment-text"><p>Please post the pcap file, containing at least 10 RTP packets in each direction and at least the part of SIP message exchange which contains the SDP negotiation, somewhere on the web (google drive, skydrive, cloudshark...) and put a link to it here. Without having a look at the file it is hard to say what is wrong. Wireshark's automatic <em>detection</em> of RTP streams is bound to SDP, and <em>analysis</em> of RTP depends also on timestamps and sequence numbers (if at all on ssrc which I doubt but I'm not a Wireshark developer).</p></div><div id="comment-48548-info" class="comment-info"><span class="comment-age">(15 Dec '15, 14:01)</span> sindy</div></div></div><div id="comment-tools-48547" class="comment-tools"></div><div class="clear"></div><div id="comment-48547-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48620"></span>

<div id="answer-container-48620" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48620-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>After checking the pcap received directly from Kjeld, I'm answering here for others: in Wireshark 2.0.0, the same SSRC in both directions of RTP stream does cause confusion, but only if dealing with RTP via Telephony -&gt; VoIP calls -&gt; Flow Sequence. If dealing with it via RTP -&gt; Stream analysis, the directions are not mixed together and RTP stream analysis as well as playback work as expected. I'll file the bug.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '15, 12:10</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-48620" class="comments-container"></div><div id="comment-tools-48620" class="comment-tools"></div><div class="clear"></div><div id="comment-48620-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

