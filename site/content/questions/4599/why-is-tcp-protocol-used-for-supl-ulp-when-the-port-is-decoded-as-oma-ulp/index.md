+++
type = "question"
title = "Why is TCP protocol used for SUPL (ulp) when the port is decoded as oma-ulp?"
description = '''Wireshark V1.4.7 or v1.6.0 is able to detect the ulp port 7275 in both directions (oma-ulp, Src port or Dst port), but is not able to re-assemble the TCP segments in one ULP message, in other words decode a ulp message. For each segment, TCP protocol is used: Example: Transmission Control Protocol, ...'''
date = "2011-06-16T10:47:00Z"
lastmod = "2011-06-22T10:24:00Z"
weight = 4599
keywords = [ "assembly", "ulp", "supl", "oma-ulp" ]
aliases = [ "/questions/4599" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Why is TCP protocol used for SUPL (ulp) when the port is decoded as oma-ulp?](/questions/4599/why-is-tcp-protocol-used-for-supl-ulp-when-the-port-is-decoded-as-oma-ulp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4599-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Wireshark V1.4.7 or v1.6.0 is able to detect the ulp port 7275 in both directions (oma-ulp, Src port or Dst port), but is not able to re-assemble the TCP segments in one ULP message, in other words decode a ulp message. For each segment, TCP protocol is used: Example: Transmission Control Protocol, Src Port:14740 (14740), Dst Port: oma-ulp (7275), Seq..... Our tester has an older version of Wireshark 0.99.6a that is able the decode ulp messages</p></div><div id="question-tags" class="tags-container tags">assembly ulp supl oma-ulp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jun '11, 10:47</strong></p><img src="https://secure.gravatar.com/avatar/db8c2a3c84aa3354d3d291eb7ff42cc2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pcerf&#39;s gravatar image" /><p>pcerf<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pcerf has no accepted answers">0%</span></p></div></div><div id="comments-container-4599" class="comments-container"><span id="4605"></span><div id="comment-4605" class="comment"><div id="post-4605-score" class="comment-score"></div><div class="comment-text"><p>Wireshark 1.6.0 may support SUPL2.0 only (not backwards SUPL1.0 compatible).</p></div><div id="comment-4605-info" class="comment-info"><span class="comment-age">(16 Jun '11, 13:53)</span> pcerf</div></div></div><div id="comment-tools-4599" class="comment-tools"></div><div class="clear"></div><div id="comment-4599-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4628"></span>

<div id="answer-container-4628" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4628-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you tried turning off reassembly (deselect the "Allow subdissector to reassemble TCP segments" in the TCP protocol preferences)?</p><p>When a protocol uses TCP reassembly, only the packet which contains the last segment of the PDU is dissected and the rest of them show up as TCP (with the info field being [TCP segment of a reassembled PDU]).</p><p>Maybe something goes wrong in the reassembly that prevents you from seeing the reassembled PDU.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jun '11, 20:24</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4628" class="comments-container"></div><div id="comment-tools-4628" class="comment-tools"></div><div class="clear"></div><div id="comment-4628-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4673"></span>

<div id="answer-container-4673" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4673-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thank you for your help: I have disabled "Allow subdissector to reassemble TCP segments" and I do see ONE ULP message created on the display in the "Protocol" section (there should be a complete message flow decoded in the pcap file I have recorded). Moreover, the decoded message is msSUPLINIT [Unreassembled Packet] and there is no such message in a SET initiated SUPL session; the first message should be SUPL START.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '11, 10:24</strong></p><img src="https://secure.gravatar.com/avatar/db8c2a3c84aa3354d3d291eb7ff42cc2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pcerf&#39;s gravatar image" /><p>pcerf<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pcerf has no accepted answers">0%</span></p></div></div><div id="comments-container-4673" class="comments-container"><span id="4674"></span><div id="comment-4674" class="comment"><div id="post-4674-score" class="comment-score"></div><div class="comment-text"><p>Hi, The version Wireshark dissects is http://member.openmobilealliance.org/ftp/Public_documents/LOC/Permanent_documents/OMA-TS-ULP-V2_0-20100816-C.zip</p></div><div id="comment-4674-info" class="comment-info"><span class="comment-age">(22 Jun '11, 12:07)</span> Anders ♦</div></div><span id="4675"></span><div id="comment-4675" class="comment"><div id="post-4675-score" class="comment-score"></div><div class="comment-text"><p>UlpMessage ::= CHOICE { msSUPLINIT SUPLINIT, msSUPLSTART SUPLSTART, msSUPLRESPONSE SUPLRESPONSE, msSUPLPOSINIT SUPLPOSINIT, msSUPLPOS SUPLPOS, msSUPLEND SUPLEND, msSUPLAUTHREQ SUPLAUTHREQ, msSUPLAUTHRESP SUPLAUTHRESP, ..., msSUPLTRIGGEREDSTART Ver2-SUPLTRIGGEREDSTART, msSUPLTRIGGEREDRESPONSE Ver2-SUPLTRIGGEREDRESPONSE, msSUPLTRIGGEREDSTOP Ver2-SUPLTRIGGEREDSTOP, msSUPLNOTIFY Ver2-SUPLNOTIFY, msSUPLNOTIFYRESPONSE Ver2-SUPLNOTIFYRESPONSE, msSUPLSETINIT Ver2-SUPLSETINIT, msSUPLREPORT Ver2-SUPLREPORT}</p></div><div id="comment-4675-info" class="comment-info"><span class="comment-age">(22 Jun '11, 12:10)</span> Anders ♦</div></div></div><div id="comment-tools-4673" class="comment-tools"></div><div class="clear"></div><div id="comment-4673-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

