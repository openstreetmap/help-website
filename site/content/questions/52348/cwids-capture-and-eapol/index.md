+++
type = "question"
title = "CWIDS Capture and EAPoL"
description = '''Hi, I am currently using a Cisco Autonomous access point in monitor mode. I forward the captured frames to my pc using an UDP port that is not open (that is why you will only see odd numbers in the captures) and capture it with Wireshark configured with the correct CWIDS port. The problem I got is t...'''
date = "2016-05-09T07:56:00Z"
lastmod = "2016-05-09T13:48:00Z"
weight = 52348
keywords = [ "cwids", "eapol", "packet-capture", "cisco" ]
aliases = [ "/questions/52348" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [CWIDS Capture and EAPoL](/questions/52348/cwids-capture-and-eapol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52348-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am currently using a Cisco Autonomous access point in monitor mode. I forward the captured frames to my pc using an UDP port that is not open (that is why you will only see odd numbers in the captures) and capture it with Wireshark configured with the correct CWIDS port.</p><p>The problem I got is that the frames that contain the EAPoL messages are misread and so I cannot decrypt my data.</p><p>When looking more deeply in the QoS data header I noticed that the QoS Control flags were set at 0xaaaa which corresponds exactly to the 2 first byte of the LLC header (SNAP). If I look at the rest of the frame in hexa and do not consider the QoS Control field then I am able to find the LLC header and the EAPoL header. Is that normal?</p><p>This could be a Cisco-side bug in their monitor mode but I saw you had the same kind of problem with PEEKREMOTE frames in old versions of the software so I decided to ask the question. You will find a capture in the 1.12 and another in the 2.0.3 versions.</p><p>Thanks in advance for your answers,</p><p>YB</p><p><img src="https://osqa-ask.wireshark.org/upfiles/CWIDSCapture_LLCmissread_WiresharkV1_12_djJVeC1.JPG" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/CWIDSCapture_LLCmissread_WireSharkV2_0_3.JPG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">cwids eapol packet-capture cisco</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 May '16, 07:56</strong></p><img src="https://secure.gravatar.com/avatar/d3817490e1e3a5109754697c5806f2a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yonibley&#39;s gravatar image" /><p>Yonibley<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yonibley has no accepted answers">0%</span></p></img></div></div><div id="comments-container-52348" class="comments-container"><span id="52365"></span><div id="comment-52365" class="comment"><div id="post-52365-score" class="comment-score"></div><div class="comment-text"><p>I saw that A-MSDU is being used (Aggregate MSDU). I am wondering if the A-MSDU is causing an error in deciphering the information in Wireshark.</p><p>Is it possible to disable A-MSDU and re-capture?</p><p>May be a wild guess, but it is strange behavior.</p></div><div id="comment-52365-info" class="comment-info"><span class="comment-age">(09 May '16, 13:07)</span> Amato_C</div></div></div><div id="comment-tools-52348" class="comment-tools"></div><div class="clear"></div><div id="comment-52348-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52371"></span>

<div id="answer-container-52371" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52371-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As both dissectors were originally written by me (and a third one I wrote also has that problem) I should probably take a look at the fix in peekremote to find out what I don't understand so far :-) Can you please open a bug, attach a sample capture (it you are worried about private data, set the private flag for the attachment) and assign it to me (jmayer at loplof de)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '16, 13:48</strong></p><img src="https://secure.gravatar.com/avatar/f1397f7833ee927f0c26a9fcb92fff11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmayer&#39;s gravatar image" /><p>jmayer<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmayer has no accepted answers">0%</span></p></img></div></div><div id="comments-container-52371" class="comments-container"><span id="52381"></span><div id="comment-52381" class="comment"><div id="post-52381-score" class="comment-score"></div><div class="comment-text"><p>+1 - doing all those things will make it a <em>lot</em> easier for us to figure out what's happening and, if possible, make it happen the way it's supposed to happen, and thus will make it a <em>lot</em> more likely that this problem will be fixed.</p><p>I'm guessing that either 1) the CWIDS header isn't as long as our dissector thinks it will be, and we're treating some byte in the middle of the 802.11 header as being at the beginning of the 802.11 header (and thus treating bytes in the LLC header as if they're part of the 802.11 header) or 2) the 802.11 header is somehow mangled in the packets that the Cisco AP is sending out (and perhaps there's something in the CWIDS header to tell us this).</p><p>The joys of <a href="https://en.wikipedia.org/wiki/Reverse_engineering">reverse engineering</a> - we don't have a spec for CWIDS so we have to guess how it works.</p></div><div id="comment-52381-info" class="comment-info"><span class="comment-age">(09 May '16, 23:10)</span> Guy Harris ♦♦</div></div><span id="52383"></span><div id="comment-52383" class="comment"><div id="post-52383-score" class="comment-score"></div><div class="comment-text"><p>Well, that could just be off by 2 bytes - the aa aa 03 is an 802.2 header, which appears right after the 802.11 header. If we could see the 2 bytes <em>before</em> what Wireshark is claiming to be the frame control field, that would be interesting. It would also be interesting to see the full dissection of the Cisco WIDS header.</p><p>But don't put that as answers or further comments in this item, add them to the bug which you will have filed first.</p></div><div id="comment-52383-info" class="comment-info"><span class="comment-age">(09 May '16, 23:58)</span> Guy Harris ♦♦</div></div><span id="52385"></span><div id="comment-52385" class="comment"><div id="post-52385-score" class="comment-score"></div><div class="comment-text"><p>And if the problem with peekremote was <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9586">bug 9586</a>, then it's <em>somewhat</em> similar, in that both bugs <em>might</em> be due to not handling newer versions of the headers, but Wildpackets^WSavvius and Cisco are different companies, so it's not as if Savvius's protocol design had anything to do with Cisco's protocol design - there might be no connection between the two issues other than "both protocols encapsulate 802.11 packets and send them over the wire".</p></div><div id="comment-52385-info" class="comment-info"><span class="comment-age">(10 May '16, 00:04)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-52371" class="comment-tools"></div><div class="clear"></div><div id="comment-52371-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

