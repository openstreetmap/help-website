+++
type = "question"
title = "Wireshark support for infiniband"
description = '''Does Wireshark(tshark) support infiniband packet capturing? (ex, capturing on IP over IB and Ethernet over IB, etc). If yes, whether Solaris is supported? i.e If I compile Wireshark latest bits, will I be able to capture IP over IB packets on Solaris? Thanks in advance. Regards, Chand'''
date = "2013-03-01T01:57:00Z"
lastmod = "2013-03-01T16:03:00Z"
weight = 19017
keywords = [ "ipoib", "infiniband" ]
aliases = [ "/questions/19017" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark support for infiniband](/questions/19017/wireshark-support-for-infiniband)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19017-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does Wireshark(tshark) support infiniband packet capturing? (ex, capturing on IP over IB and Ethernet over IB, etc). If yes, whether Solaris is supported? i.e If I compile Wireshark latest bits, will I be able to capture IP over IB packets on Solaris? Thanks in advance.</p><p>Regards, Chand</p></div><div id="question-tags" class="tags-container tags">ipoib infiniband</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Mar '13, 01:57</strong></p><img src="https://secure.gravatar.com/avatar/609d27d4b18a5baa8e18b3c31b815422?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chand&#39;s gravatar image" /><p>Chand<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chand has no accepted answers">0%</span></p></div></div><div id="comments-container-19017" class="comments-container"></div><div id="comment-tools-19017" class="comment-tools"></div><div class="clear"></div><div id="comment-19017-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19082"></span>

<div id="answer-container-19082" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19082-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If, on whatever operating system you're running libpcap supports capturing on Infiniband (which may just mean "if whatever the native capture mechanism libpcap uses supports capturing on Infiniband" plus "libpcap knows about the native link-layer type value for Infiniband captures and knows a <code>DLT_</code> value to which it can map it), and if you're using a version of Wireshark that supports the link-layer type value used by libpcap for Infiniband, then Wireshark and TShark will support Infiniband packet capturing.</p><p>Currently, <a href="http://www.tcpdump.org/linktypes.html">the list of link-layer header types for libpcap/WinPcap and for pcap and pcap-ng capture files</a> includes two link-layer header types for Infiniband:</p><ul><li><code>LINKTYPE_IPOIB</code>/<code>DLT_IPOIB</code>, for IP-over-Infiniband frames, as specified by <a href="http://tools.ietf.org/html/rfc4391#section-6">RFC 4391 section 6</a>;</li><li><code>LINKTYPE_INFINIBAND</code>/<code>DLT_INFINIBAND</code>, for raw Infiniband frames, starting with the Local Routing Header, as specified in Chapter 5 "Data packet format" of <a href="http://members.infinibandta.org/kwspub/spec/V1r1_2_1.Release_12062007.zip">InfiniBand™ Architectural Specification Release 1.2.1 Volume 1 - General Specifications</a>.</li></ul><p>On Solaris prior to Solaris 11, libpcap (which I think you'd have to install yourself) uses DLPI to capture traffic; libpcap doesn't support capturing Infiniband traffic using DLPI, so, even if Solaris prior to Solaris 11 supports capturing Infiniband traffic using DLPI, you'd have to hack libpcap to use it. <em>If</em> snoop can capture Infiniband traffic on some pre-Solaris 11 version of Solaris, then:</p><ol><li>DLPI presumably supports capturing Infiniband traffic on that version of Solaris, so libpcap <em>could</em> presumably be hacked to support it;</li><li>Wireshark 1.8.0 and later can probably read the IP-over-Infiniband snoop files captured on that version of Solaris (earlier versions won't be able to do so).</li></ol><p>On Solaris 11, libpcap (which I think is part of Solaris 11, so you wouldn't have to install it yourself) uses BPF to capture traffic. Capturing IP-over-Infiniband might Just Work there, if you're using Wireshark 1.8.0 or later. I don't know whether capturing raw Infiniband frames is supported; that might be what you'd need for Ethernet-over-Infiniband.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '13, 16:03</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-19082" class="comments-container"><span id="19146"></span><div id="comment-19146" class="comment"><div id="post-19146-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot Harris and also for the details explanation :) I am compiling wireshark now, Thanks again.</p></div><div id="comment-19146-info" class="comment-info"><span class="comment-age">(05 Mar '13, 04:51)</span> Chand</div></div></div><div id="comment-tools-19082" class="comment-tools"></div><div class="clear"></div><div id="comment-19082-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

