+++
type = "question"
title = "SCTP unknown payload ID, unknown layer between SCTP and MTP3"
description = '''Greetings! I was asked today to decode a PCAP format capture file that Wireshark (1.12.3) could not decode. From looking at the exported octets, I could tell that the stack is: Ethernet:IPv4:SCTP:(unknown layer header of 9 octets):MTP3:SCCP:TCAP:MAP/IS41/CAMEL The nine octets are always of the form:...'''
date = "2015-05-06T13:31:00Z"
lastmod = "2015-05-07T06:14:00Z"
weight = 42155
keywords = [ "telecom", "sctp", "mtp3", "sigtran" ]
aliases = [ "/questions/42155" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [SCTP unknown payload ID, unknown layer between SCTP and MTP3](/questions/42155/sctp-unknown-payload-id-unknown-layer-between-sctp-and-mtp3)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42155-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings! I was asked today to decode a PCAP format capture file that Wireshark (1.12.3) could not decode. From looking at the exported octets, I could tell that the stack is:</p><p>Ethernet:IPv4:SCTP:(unknown layer header of 9 octets):MTP3:SCCP:TCAP:MAP/IS41/CAMEL</p><p>The nine octets are always of the form:</p><p>01 (1d,3d,6e,6f) 06 01 00 00 00 (33,4a,69,6b,6c,6d,73,81,8e,91,9d,bd) 3f</p><p>So you can see the 2nd octet has four possible values, and the 8th octet had 12 different values. The rest of the octets were static. I am tempted to think this is a "user-adaptation" layer, with the 1st octet being the version, but usually the 2nd octet would be "spare" and should be zero. The 5th,6th,7th,8th octets appear to be the length starting with the MTP3 SIO. I have no idea what the 3f is for.</p><p>I went through all possible "Decode As" for SCTP and turned up nothing. Any help would be appreciated.</p></div><div id="question-tags" class="tags-container tags">telecom sctp mtp3 sigtran</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 May '15, 13:31</strong></p><img src="https://secure.gravatar.com/avatar/d6872b1cae1da5fcd92837a89d05942c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tiger762&#39;s gravatar image" /><p>tiger762<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tiger762 has no accepted answers">0%</span></p></div></div><div id="comments-container-42155" class="comments-container"></div><div id="comment-tools-42155" class="comment-tools"></div><div class="clear"></div><div id="comment-42155-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="42177"></span>

<div id="answer-container-42177" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42177-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like M2PA version 2 to me. To decode it edit your M2PA preferences to set the SCTP port appropriately and then select draft version 2 of the RFC.</p><p>(The 2nd octet is spare and is supposed to be 00 but the rest of the bytes line up.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '15, 06:14</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-42177" class="comments-container"><span id="42179"></span><div id="comment-42179" class="comment"><div id="post-42179-score" class="comment-score"></div><div class="comment-text"><p>Excellent! Thank you so much!</p><p>That worked perfectly. By default, I was trying to decode it as RFC4165 and so Wireshark was looking for BSN/FSN which aren't there.</p></div><div id="comment-42179-info" class="comment-info"><span class="comment-age">(07 May '15, 06:44)</span> tiger762</div></div><span id="42180"></span><div id="comment-42180" class="comment"><div id="post-42180-score" class="comment-score"></div><div class="comment-text"><p>You're welcome. Please be sure to Accept the answer (by clicking the check mark) so this question disappears from the list of unanswered questions.</p></div><div id="comment-42180-info" class="comment-info"><span class="comment-age">(07 May '15, 06:54)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-42177" class="comment-tools"></div><div class="clear"></div><div id="comment-42177-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42163"></span>

<div id="answer-container-42163" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42163-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What is the value of SCTP's payload protocol identifier? That should give you a pretty clear indication: <a href="http://www.iana.org/assignments/sctp-parameters/sctp-parameters.xhtml#sctp-parameters-25">http://www.iana.org/assignments/sctp-parameters/sctp-parameters.xhtml#sctp-parameters-25</a></p><p>If it's using an unassigned value, I don't think it's really possible to say without more context behind where the capture was taken. All things being equal I would normally assume M2xA between SCTP and pure MTP3, but as you note those field values are not consistent with them, particularly as they are storing values in what would be their reserved field.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 May '15, 18:13</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-42163" class="comments-container"><span id="42174"></span><div id="comment-42174" class="comment"><div id="post-42174-score" class="comment-score"></div><div class="comment-text"><p>Sorry, I should have been more clear. The SCTP PPID is zero/unknown. This is in the context of a telecom customer sending data in to our STP. What I ended up doing is looking at the raw octets. The MTP3 SIO octet (0x83, national/SCCP) with a 09 (SCCP UNITDATA) 8 octets downstream, followed by one of: [00,01,80,81] (class / error handling) followed by 03 (pointer to called party address). I wrote a small program to locate MTP3 then copy from that point forward to the end of the packet into a new PCAP file. I set the encapsulation type to MTP3 in the global header, and gave them back a new PCAP which has everything below MTP3 discarded.</p><p>The unknown PPID as well as the data in what is probably a "spare" octet, is what I found disturbing.</p></div><div id="comment-42174-info" class="comment-info"><span class="comment-age">(07 May '15, 05:14)</span> tiger762</div></div></div><div id="comment-tools-42163" class="comment-tools"></div><div class="clear"></div><div id="comment-42163-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

