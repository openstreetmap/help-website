+++
type = "question"
title = "Decode of libpcap file."
description = '''I have written a program to decode and use the capture file from wireshark in real time.  It failed when I moved it to a different computer since I had a check for valid header which was actually looking for my IP(I thought it was just a magic number) Problem is, I read and followed your Global Head...'''
date = "2011-07-24T19:20:00Z"
lastmod = "2011-07-24T23:16:00Z"
weight = 5198
keywords = [ "libpcap" ]
aliases = [ "/questions/5198" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Decode of libpcap file.](/questions/5198/decode-of-libpcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5198-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have written a program to decode and use the capture file from wireshark in real time.</p><p>It failed when I moved it to a different computer since I had a check for valid header which was actually looking for my IP(I thought it was just a magic number)</p><p>Problem is, I read and followed your Global Header second and Record header section in the doc, but you did not outline the format of the actual data packet. Thus I was not aware the first few bytes were destination then source then some other stuff I have no idea about. In total 54 bytes of something from what I can tell. Where can I find the spec on those 54 bytes of the packet?</p><p>[email protected]</p><p>Many thanks Glen Lalonde www.binarysearchtree.com</p></div><div id="question-tags" class="tags-container tags">libpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '11, 19:20</strong></p><img src="https://secure.gravatar.com/avatar/f0a8ad33336d6c842aa05b1343308083?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="codewarrior&#39;s gravatar image" /><p>codewarrior<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="codewarrior has no accepted answers">0%</span></p></div></div><div id="comments-container-5198" class="comments-container"></div><div id="comment-tools-5198" class="comment-tools"></div><div class="clear"></div><div id="comment-5198-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5201"></span>

<div id="answer-container-5201" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5201-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The easiest way to read a libpcap file is, not surprisigly, to use libpcap (or, on Windows, WinPcap).</p><p>However, that won't help you understand the format of the data packet. The data packet is just raw packet data, possibly preceded by a pseudo-header; the link-layer type value returned by <code>pcap_datalink()</code> indicates what the pseudo-header, if any, and the link-layer header format for the packet are - see <a href="http://www.tcpdump.org/linktypes.html">the link-layer header types page</a> on the tcpdump.org Web site for the description of the types. For example, a type value of 1 (<code>DLT_EN10MB</code> as returned by <code>pcap_datalink()</code>) indicates that the packets are Ethernet packets, beginning with an Ethernet header; the link-layer header types page links to a page for the IEEE 802.3 specifications, which describes the Ethernet link-layer header (which has 6 octets of destination address, 6 octets of source address, and 2 octets of a type/length field - that field is in network byte order, and has the value <code>0x0800</code> for IPv4 packets, for example).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '11, 23:16</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-5201" class="comments-container"><span id="5221"></span><div id="comment-5221" class="comment"><div id="post-5221-score" class="comment-score"></div><div class="comment-text"><p>Using what you said I found this page which had all the details at the level I needed. Many thanks. Page: http://en.wikipedia.org/wiki/EtherType</p></div><div id="comment-5221-info" class="comment-info"><span class="comment-age">(25 Jul '11, 07:43)</span> codewarrior</div></div></div><div id="comment-tools-5201" class="comment-tools"></div><div class="clear"></div><div id="comment-5201-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5199"></span>

<div id="answer-container-5199" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5199-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, libpacps file format can be found [here] the development version of Wireshark uses pcapng as the default file format.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '11, 21:20</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-5199" class="comments-container"><span id="5200"></span><div id="comment-5200" class="comment"><div id="post-5200-score" class="comment-score"></div><div class="comment-text"><p>http://wiki.wireshark.org/Development/LibpcapFileFormat</p></div><div id="comment-5200-info" class="comment-info"><span class="comment-age">(24 Jul '11, 21:21)</span> Anders ♦</div></div><span id="5220"></span><div id="comment-5220" class="comment"><div id="post-5220-score" class="comment-score"></div><div class="comment-text"><p>That was the document I was already reading, it does not indicate enough detail about the actual packet, it just details the two headers.</p></div><div id="comment-5220-info" class="comment-info"><span class="comment-age">(25 Jul '11, 07:10)</span> codewarrior</div></div></div><div id="comment-tools-5199" class="comment-tools"></div><div class="clear"></div><div id="comment-5199-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

