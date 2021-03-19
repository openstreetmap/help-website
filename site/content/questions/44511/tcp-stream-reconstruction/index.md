+++
type = "question"
title = "TCP stream reconstruction"
description = '''Hello, I have a program that parses and extracts the pcap information and I&#x27;m trying toreassemble the TCP session. The WS method is:  void reassemble_tcp(int tcp_stream, long sequence, long acknowledgement, int dataLength, byte[] data, int capturedDataLength, boolean synflag,  Address sourceIp, Addr...'''
date = "2015-07-26T20:51:00Z"
lastmod = "2015-07-26T20:51:00Z"
weight = 44511
keywords = [ "follow.tcp.stream" ]
aliases = [ "/questions/44511" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP stream reconstruction](/questions/44511/tcp-stream-reconstruction)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-44511-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have a program that parses and extracts the pcap information and I'm trying toreassemble the TCP session. The WS method is:</p><p>void reassemble_tcp(int tcp_stream, long sequence, long acknowledgement, int dataLength, byte[] data, int capturedDataLength, boolean synflag, Address sourceIp, Address destinationIp, int srcport, int dstport, long packet_num) The problem is one or both 2 lengths. They seem to change names in the code and it's hard to follow.</p><p>It seems that the first length argument is the segment length calculated by subtracting the header lengths from reported length.</p><p>-I calculate the reported length as long reported_len=getIpTotalLength()-getIpHeaderLength(); and that does match most of the time the WS segment length but not all the times.</p><p>-The other length that is called data_length in the signature I calculate using dataStartOffset = packetHeaderSize + ETHERNET_HEADER_LENGTH + getIpHeaderLength()+tcpHeaderLength; and then dataLength =packet length - dataStartOffset;// where packetLength includes the packetHeaderSize.</p><p>I need help understanding how these lengths differ and if my formulas are fine.</p><p>I get all the other metadata (like header lengths etc) and they match the WS but my calculations for the these 2 lengths seem to match in most cases but not all. I've been struggling for quite a while trying to find answer.Need to find if my formulas are wrong and if so what are the proper formulas.</p><p>Thank you in advance, Adrian</p></div><div id="question-tags" class="tags-container tags">follow.tcp.stream</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jul '15, 20:51</strong></p><img src="https://secure.gravatar.com/avatar/4c677562260c945708be7ab99ca96a1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adriannuix&#39;s gravatar image" /><p>adriannuix<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adriannuix has no accepted answers">0%</span></p></div></div><div id="comments-container-44511" class="comments-container"></div><div id="comment-tools-44511" class="comment-tools"></div><div class="clear"></div><div id="comment-44511-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

