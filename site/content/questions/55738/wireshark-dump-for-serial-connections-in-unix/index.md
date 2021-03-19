+++
type = "question"
title = "wireshark dump for serial connections in unix ??"
description = '''Is there a command to write a wireshark dump for serial connections in unix machine ? &amp;amp; how to read that data ?'''
date = "2016-09-21T23:08:00Z"
lastmod = "2016-09-22T00:53:00Z"
weight = 55738
keywords = [ "unix" ]
aliases = [ "/questions/55738" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark dump for serial connections in unix ??](/questions/55738/wireshark-dump-for-serial-connections-in-unix)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55738-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a command to write a wireshark dump for serial connections in unix machine ? &amp; how to read that data ?</p></div><div id="question-tags" class="tags-container tags">unix</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Sep '16, 23:08</strong></p><img src="https://secure.gravatar.com/avatar/ab36206c05032ab4ec2d07be3801f17e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SohanRawat&#39;s gravatar image" /><p>SohanRawat<br />
<span class="score" title="2 reputation points">2</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SohanRawat has no accepted answers">0%</span></p></div></div><div id="comments-container-55738" class="comments-container"><span id="55739"></span><div id="comment-55739" class="comment"><div id="post-55739-score" class="comment-score"></div><div class="comment-text"><p>Do you have in mind dumping/capturing of IP packets sent over SLIP &amp; PPP (i.e. IP over serial channel) lines, or dumping of raw serial traffic on those interfaces?</p></div><div id="comment-55739-info" class="comment-info"><span class="comment-age">(22 Sep '16, 00:27)</span> sindy</div></div><span id="55740"></span><div id="comment-55740" class="comment"><div id="post-55740-score" class="comment-score"></div><div class="comment-text"><p>@Sindy : dumping of raw serial traffic on those interfaces</p></div><div id="comment-55740-info" class="comment-info"><span class="comment-age">(22 Sep '16, 00:32)</span> SohanRawat</div></div></div><div id="comment-tools-55738" class="comment-tools"></div><div class="clear"></div><div id="comment-55738-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55741"></span>

<div id="answer-container-55741" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55741-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is no direct way at the moment. For serious analysis, you would need to track not only the value of each byte sent but also its timestamp, maybe also the state of the control lines like RTS, CTS, DSR, ... so the capture file format would require quite a lot of extra fields, leaving aside the dissection of the captured data in Wireshark.</p><p>But if you can live with less accuracy regarding timing and control signals, I suggest you to insert a pair of back-to-back connected Serial-over-LAN adaptors into your serial connection and use Wireshark (or tcpdump) to capture the TCP session between those two. The adaptors usually buffer the incoming traffic to save overhead, so as long as the serial data are coming in continuously enough, the adaptor accumulates them into a packet and only sends the packet when it reaches the MSS size; if longer time than some tens of milliseconds elapses since the last byte has come in, the packet is sent (with a PSH flag set) even if there is still free space available in it.</p><p>If you have enough serial ports on the machine where you capture, you may connect the first one (to which your communication application is bound) to the second one using a null modem cable, run the SoL application on the second and third serial adaptor and let them talk to each other over the loopback interface (127.0.0.1), and connect the original serial cable (previously connected to the first port) to the third one.</p><p>The above is just an illustration of the principle; actually, you may connect your application to a virtual serial port which, instead of connecting to an external SoL adaptor, connects across the loopback to a local SoL application connected to the original port, so no additional hardware ports are required.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '16, 00:53</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Sep '16, 00:57</p></div></div><div id="comments-container-55741" class="comments-container"><span id="55742"></span><div id="comment-55742" class="comment"><div id="post-55742-score" class="comment-score"></div><div class="comment-text"><p>@Sindy , Is there any planning from wireshark regarding the direct capturing for the serial communication dump for the next releases ?</p></div><div id="comment-55742-info" class="comment-info"><span class="comment-age">(22 Sep '16, 01:45)</span> SohanRawat</div></div><span id="55745"></span><div id="comment-55745" class="comment"><div id="post-55745-score" class="comment-score"></div><div class="comment-text"><p>Not that I know of, note that wireshark doesn't actually make the capture itself, that's performed by an OS specific capture library, e.g. libpcap, WinPcap or npcap and all of those are network capture libraries.</p><p>Wireshark capturing capabilities can be extended using extcap utilities that are separate executables than are launched by Wireshark to perform specific capture tasks and the pass the captured traffic back to Wireshark in pcap format, so that might be an avenue you wish to explore.</p></div><div id="comment-55745-info" class="comment-info"><span class="comment-age">(22 Sep '16, 02:51)</span> grahamb ♦</div></div><span id="55747"></span><div id="comment-55747" class="comment"><div id="post-55747-score" class="comment-score"></div><div class="comment-text"><p>To give you a better overview: such an extension of Wireshark and the capturing mechanism would have to include the following steps:</p><ul><li><p>decide what would be the unit of captured data - a single byte is most logical but most expensive in terms of overhead, a contiguous sequence of bytes leads to loss of timing information accuracy and may complicate things if there are no gaps between the bytes at all.</p></li><li><p>depending on the above, decide how to handle parity errors</p></li><li><p>decide what to do with information regarding the state of control lines, whether to attach their instant status as an additional information to each byte, or record status changes independently from the serial data as events</p></li><li><p>how to accommodate the above into pcapng format (pcap is definitely not flexible enough)</p></li><li><p>modify the serial line driver so that it would provide this information to some output data stream read by libpcap or an extcap aplication (which both have to generate the pcapng output)</p></li><li><p>create a set of dissectors for Wireshark which would render the raw information from the capture into a human readable form and be able to eventually invoke higher layer dissectors for cases where a SLIP or PPP runs over the line</p></li></ul><p>So this is far from simple, and far from how network capturing and analysis typically works.</p><p>What is your use case?</p></div><div id="comment-55747-info" class="comment-info"><span class="comment-age">(22 Sep '16, 04:47)</span> sindy</div></div></div><div id="comment-tools-55741" class="comment-tools"></div><div class="clear"></div><div id="comment-55741-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

