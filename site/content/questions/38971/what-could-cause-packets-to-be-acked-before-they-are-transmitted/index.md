+++
type = "question"
title = "What could cause packets to be ACKed before they are transmitted?"
description = '''Hi I captured info from dumpcap installed on a computer with windows 7 x64 installed. The computer has the IP address: 172.16.6.96. Throughout the file packets are ACKed before they are transmitted. The ACKs are marked as TCP ACKed unseen segment. Any ideas what could cause this? Attached are two im...'''
date = "2015-01-08T11:14:00Z"
lastmod = "2015-01-14T17:42:00Z"
weight = 38971
keywords = [ "ack", "unseen_segment" ]
aliases = [ "/questions/38971" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [What could cause packets to be ACKed before they are transmitted?](/questions/38971/what-could-cause-packets-to-be-acked-before-they-are-transmitted)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38971-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I captured info from dumpcap installed on a computer with windows 7 x64 installed. The computer has the IP address: 172.16.6.96. Throughout the file packets are ACKed before they are transmitted. The ACKs are marked as TCP ACKed unseen segment. Any ideas what could cause this? Attached are two images from the capture with examples of the issue.</p><p>There are no retransmissions, etc. there are several keep alive messages not show in the image of the capture.</p><p>[2] <a href="http://www.tiikoni.com/tis/view/?id=879459f">http://www.tiikoni.com/tis/view/?id=879459f</a></p></div><div id="question-tags" class="tags-container tags">ack unseen_segment</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jan '15, 11:14</strong></p><img src="https://secure.gravatar.com/avatar/e66a2644f8a1189cb900ec2f89777486?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mark%20Nassy&#39;s gravatar image" /><p>Mark Nassy<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mark Nassy has no accepted answers">0%</span></p></div></div><div id="comments-container-38971" class="comments-container"><span id="38972"></span><div id="comment-38972" class="comment"><div id="post-38972-score" class="comment-score"></div><div class="comment-text"><p><a href="http://www.tiikoni.com/tis/view/?id=9bcfb15">http://www.tiikoni.com/tis/view/?id=9bcfb15</a></p></div><div id="comment-38972-info" class="comment-info"><span class="comment-age">(08 Jan '15, 11:17)</span> Mark Nassy</div></div></div><div id="comment-tools-38971" class="comment-tools"></div><div class="clear"></div><div id="comment-38971-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="38975"></span>

<div id="answer-container-38975" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38975-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Packets are not--and cannot--be ACKed before they are sent. "TCP ACKed unseen segment" means that the ACK is present in your Wireshark trace file, but the data packet that is being acknowledged is not present in the trace. The data packet did make it all the way from the sender to the receiver, otherwise there would not be an ACK, but the data packet is not in the trace file. This means that your file is incomplete, and you need to use caution in using it for analysis.</p><p>There are two common causes of this problem:</p><p>First, there is asymmetric routing, so not all packets take the same path, and you captured somewhere along the path where Wireshark did not see all packets.</p><p>Second, Wireshark was simply not able to keep up and not all packets were written into the trace file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '15, 15:09</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-38975" class="comments-container"><span id="38976"></span><div id="comment-38976" class="comment"><div id="post-38976-score" class="comment-score"></div><div class="comment-text"><p>The ACK's do seem to be received before the corresponding TCP segment. However I don't recognise the output format. Can the OP post a pcap of the data rather than a screenshot interpretation of the data.</p></div><div id="comment-38976-info" class="comment-info"><span class="comment-age">(08 Jan '15, 15:31)</span> grahamb ♦</div></div><span id="38981"></span><div id="comment-38981" class="comment"><div id="post-38981-score" class="comment-score"></div><div class="comment-text"><p>Thanks. 1.I captured the network traffic using dumpcap.exe installed on the client with the issue. The client has only one network adapter. 2.The network adapter is 100 Mbps, and dumpcap.exe said the kernel did not drop any packets. The network adapter is not heavily utilized, as well as the CPU at the time of the issue. This always happens on the 4 packet for HTTP, and TNS traffic. SYN, SYN-ACK, ACK, then unseen ACK.</p><p>I tried to turn on TCP time stamping in the hope I would be able to determine if there was any missing packets by using the echo value but was unsuccessful.</p><p>I was able to turn on Errors in the LAN connection status window and it shows 0 errors.</p><p>I plan to capture traffic on Monday using a switch connected right next to the client and see if I get anything different.</p><p>For my knowledge: if I capture at the client and dumpcap drops (in this case) an outgoing packet, and it receives an ACK for the packet (by ACK number) that was dropped, why does it show that the packet was transmitted later on in the trace file?</p></div><div id="comment-38981-info" class="comment-info"><span class="comment-age">(08 Jan '15, 16:04)</span> Mark Nassy</div></div><span id="38982"></span><div id="comment-38982" class="comment"><div id="post-38982-score" class="comment-score"></div><div class="comment-text"><p>I will work on getting a better capture on Monday and update the post at that time.</p></div><div id="comment-38982-info" class="comment-info"><span class="comment-age">(08 Jan '15, 16:08)</span> Mark Nassy</div></div><span id="38983"></span><div id="comment-38983" class="comment"><div id="post-38983-score" class="comment-score"></div><div class="comment-text"><p>FYI: Some of the output columns are from the TRANSSUM lua plugin.</p></div><div id="comment-38983-info" class="comment-info"><span class="comment-age">(08 Jan '15, 16:21)</span> Mark Nassy</div></div></div><div id="comment-tools-38975" class="comment-tools"></div><div class="clear"></div><div id="comment-38975-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39137"></span>

<div id="answer-container-39137" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39137-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I ran a capture from another computer connected to a switch with a SPAN port and did not see any unseen segments ACKed. The end result was the same as in the previous capture. The same SQL query showed a delay in the time it took for the server to send its response. I don't know why capturing on the client computer that issued the sql query resulted in unseen segments.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '15, 17:42</strong></p><img src="https://secure.gravatar.com/avatar/e66a2644f8a1189cb900ec2f89777486?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mark%20Nassy&#39;s gravatar image" /><p>Mark Nassy<br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mark Nassy has no accepted answers">0%</span></p></div></div><div id="comments-container-39137" class="comments-container"></div><div id="comment-tools-39137" class="comment-tools"></div><div class="clear"></div><div id="comment-39137-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

