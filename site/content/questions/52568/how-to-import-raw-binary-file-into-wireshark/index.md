+++
type = "question"
title = "how to import raw binary file into wireshark"
description = '''I have a raw data file - not text - not formatted in any way. It appears to be packet based, as i see continue flags - 7E - with by bursts of activity in between. How can i import this into wireshark? the import features seem to be looking for known framing or encapsulation types...'''
date = "2016-05-14T11:57:00Z"
lastmod = "2016-05-15T00:44:00Z"
weight = 52568
keywords = [ "raw" ]
aliases = [ "/questions/52568" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to import raw binary file into wireshark](/questions/52568/how-to-import-raw-binary-file-into-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52568-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a raw data file - not text - not formatted in any way. It appears to be packet based, as i see continue flags - 7E - with by bursts of activity in between.</p><p>How can i import this into wireshark?<br />
the import features seem to be looking for known framing or encapsulation types...</p></div><div id="question-tags" class="tags-container tags">raw</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 May '16, 11:57</strong></p><img src="https://secure.gravatar.com/avatar/0b80a3ff9dd964002f7cf803e3622186?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jcss7&#39;s gravatar image" /><p>jcss7<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jcss7 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-52568" class="comments-container"><span id="52575"></span><div id="comment-52575" class="comment"><div id="post-52575-score" class="comment-score"></div><div class="comment-text"><p>So where did you get that file? What program produced it?</p></div><div id="comment-52575-info" class="comment-info"><span class="comment-age">(14 May '16, 20:10)</span> Guy Harris ♦♦</div></div><span id="52576"></span><div id="comment-52576" class="comment"><div id="post-52576-score" class="comment-score"></div><div class="comment-text"><p>My own program for E1 monitoring. so all 31 timeslots appear to be one bonded IP stream.</p></div><div id="comment-52576-info" class="comment-info"><span class="comment-age">(14 May '16, 20:34)</span> jcss7</div></div></div><div id="comment-tools-52568" class="comment-tools"></div><div class="clear"></div><div id="comment-52568-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="52570"></span>

<div id="answer-container-52570" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52570-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You'll need to write code for Wireshark's libwiretap to recognize and read it. As it's your program, you know what the format is.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 May '16, 12:24</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 May '16, 23:40</p></div></div><div id="comments-container-52570" class="comments-container"><span id="52571"></span><div id="comment-52571" class="comment"><div id="post-52571-score" class="comment-score"></div><div class="comment-text"><p>Sounds like an ISDN S/T interface trace of the LAPD protocol.</p></div><div id="comment-52571-info" class="comment-info"><span class="comment-age">(14 May '16, 13:23)</span> Jaap ♦</div></div><span id="52574"></span><div id="comment-52574" class="comment"><div id="post-52574-score" class="comment-score"></div><div class="comment-text"><p>Or <a href="https://tools.ietf.org/html/rfc1662">PPP in HDLC-like Framing</a>?</p><p>See also, <a href="https://en.wikipedia.org/wiki/High-Level_Data_Link_Control">High-Level Data Link Control</a>.</p></div><div id="comment-52574-info" class="comment-info"><span class="comment-age">(14 May '16, 19:58)</span> cmaynard ♦♦</div></div><span id="52580"></span><div id="comment-52580" class="comment"><div id="post-52580-score" class="comment-score"></div><div class="comment-text"><p>I was handling a similar scenario, extraction of LAPD from an E1 timeslot, and ended up extracting the PDUs and writing them in pcap or pcapng format. As I am a "non-dev", i.e. I don't speack C fluently and haven't rolled out the development environment necessary to write binary Wireshark plugins, I've used perl to code the whole thing, from reading from the E1 to generating the pcap(ng) stream.</p><p>As by then (and maybe until now?) Wireshark couldn't read pcapng from a pipe, I had to choose between the ability to run live capture and the ability to provide packet metadata (direction and L1 errors), so I've chosen the second.</p><p>Important points:</p><ul><li><p>HDLC normally doesn't have any field to indicate the application protocol it carries (Cisco HDLC is an exception), so you have to identify it yourself, and choose the right encapsulation type in order to properly plant the dissection tree. Look <a href="http://www.tcpdump.org/linktypes.html">here</a> for existing link types (encapsulations). If what you've caught is really PPP over HDLC, then LINKTYPE_PPP_WITH_DIR, LINKTYPE_C_HDLC_WITH_DIR may be your best candidates for pcap format, and their predecessors lacking the direction information for pcapng format where the direction is part of the metadata. If it is some proprietary packet encapsulation, you'll have to either write your own dissector to bridge the gap between the HDLC and the standards-macthing part of the frame data and use one of the USER link types to tell Wireshark that it should use that dissector, or extract only the standards-matching part of the frame and use the corresponding link type identifier.</p></li><li><p>although HDLC allows not to use the bit-escaping of 11111 with 111110 if the carrier is byte-structured, some HDLC over structured E1 implementations don't make use of this option (namely, LAPD doesn't). It should be easy to tell: if you can see not only long series of 7E but also long series of FC and 3F in your byte stream, there is a good chance that the implementation uses the byte-structured carrier as a raw bit stream and you'll have to work with it the same way to be able to properly identify PDU borders.</p></li></ul></div><div id="comment-52580-info" class="comment-info"><span class="comment-age">(15 May '16, 01:22)</span> sindy</div></div><span id="52594"></span><div id="comment-52594" class="comment"><div id="post-52594-score" class="comment-score"></div><div class="comment-text"><p>thanks. it is LAPD and i see the long strings of 7E FC, and EF. i'll give it a try</p></div><div id="comment-52594-info" class="comment-info"><span class="comment-age">(15 May '16, 07:26)</span> jcss7</div></div></div><div id="comment-tools-52570" class="comment-tools"></div><div class="clear"></div><div id="comment-52570-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52579"></span>

<div id="answer-container-52579" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52579-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>i wound up resurrecting some old code and parsed the data. it is in fact HDLC/LAPD with supervisory and information messages.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 May '16, 00:44</strong></p><img src="https://secure.gravatar.com/avatar/0b80a3ff9dd964002f7cf803e3622186?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jcss7&#39;s gravatar image" /><p>jcss7<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jcss7 has no accepted answers">0%</span></p></div></div><div id="comments-container-52579" class="comments-container"></div><div id="comment-tools-52579" class="comment-tools"></div><div class="clear"></div><div id="comment-52579-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

