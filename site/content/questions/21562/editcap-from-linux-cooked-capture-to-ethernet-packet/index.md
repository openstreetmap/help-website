+++
type = "question"
title = "editcap from Linux cooked capture to Ethernet packet"
description = '''Hi, I am trying to convert/ encapsulation from Linux cooked capture to Ethernet packet; I am trying to use editcap and text2pcap - but don&#x27;t get the desired result. can anyone advice? Thanks in advanced, Diana'''
date = "2013-05-29T07:08:00Z"
lastmod = "2015-08-24T19:29:00Z"
weight = 21562
keywords = [ "editcap" ]
aliases = [ "/questions/21562" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [editcap from Linux cooked capture to Ethernet packet](/questions/21562/editcap-from-linux-cooked-capture-to-ethernet-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21562-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am trying to convert/ encapsulation from Linux cooked capture to Ethernet packet; I am trying to use editcap and text2pcap - but don't get the desired result. can anyone advice?</p><p>Thanks in advanced, Diana</p></div><div id="question-tags" class="tags-container tags">editcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 May '13, 07:08</strong></p><img src="https://secure.gravatar.com/avatar/900044aef60dc6223168781e5d576bfb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dianalab9&#39;s gravatar image" /><p>Dianalab9<br />
<span class="score" title="26 reputation points">26</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dianalab9 has no accepted answers">0%</span></p></div></div><div id="comments-container-21562" class="comments-container"></div><div id="comment-tools-21562" class="comment-tools"></div><div class="clear"></div><div id="comment-21562-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21583"></span>

<div id="answer-container-21583" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21583-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Editcap, alone, won't help here. As I stated in a comment on <a href="http://ask.wireshark.org/questions/21560/editcap-dosnt-seem-to-work-in-the-new-version-i-installed-187">your other related question</a>, editcap does <em>NOT</em> transform the contents of packets; it will not, for example, take packets with <a href="http://www.tcpdump.org/linktypes/LINKTYPE_LINUX_SLL.html">Linux cooked capture headers</a>, remove the cooked capture headers, construct Ethernet headers by:</p><ul><li>using the link-layer address (assuming it's 6 octets long; if not, it'd have to construct a fake one) as the source or destination address depending on whether the packet was sent by or received by the capturing host;</li><li>construct a fake address for the other MAC address;</li><li>construct a type/length field value depending on the "protocol type" field;</li></ul><p>and then prepend the resulting header.</p><p>text2pcap might help here, but it's not sufficient. You could take the packets, print their time stamps and raw hex data, write a program (in whatever language) to do the transformation described above and write the resulting file out, and then turn it into a pcap file using text2pcap.</p><p>The "write a program" step is the key one; I'm not sure there are any existing programs that will take a Linux cooked capture and generate an Ethernet capture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 May '13, 12:30</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-21583" class="comments-container"><span id="21589"></span><div id="comment-21589" class="comment"><div id="post-21589-score" class="comment-score"></div><div class="comment-text"><p>Great! I exported it to Hex, deleted first 16 bytes and ran: text2pcap.exe -e 0x800 Text.txt ConvertedoEthernet.pcap works beautifully :)</p><p>Thanks!</p></div><div id="comment-21589-info" class="comment-info"><span class="comment-age">(29 May '13, 23:36)</span> Dianalab9</div></div><span id="22745"></span><div id="comment-22745" class="comment"><div id="post-22745-score" class="comment-score"></div><div class="comment-text"><p>"I exported it to Hex, deleted first 16 bytes and ran: text2pcap.exe -e 0x800 Text.txt ConvertedoEthernet.pcap"</p><p>I am new in this field and trying to convert from Linux cooked capture to Ethernet packet.</p><p>Would you please elaborate how did you do it?</p><p>Thanks in advance.</p></div><div id="comment-22745-info" class="comment-info"><span class="comment-age">(08 Jul '13, 20:55)</span> badhon</div></div><span id="25670"></span><div id="comment-25670" class="comment"><div id="post-25670-score" class="comment-score"></div><div class="comment-text"><p>Just FYI: <a href="http://www.tracewrangler.com">TraceWrangler</a> latest version can now do the replacement of Linux cooked headers to Ethernet headers. It will automatically set the link layer type of the Interface Description Block to Ethernet and copy/set the MAC address to the fitting source or destination address in each frame if applicable. Packets to broadcast will get a broadcast MAC as destination address.</p></div><div id="comment-25670-info" class="comment-info"><span class="comment-age">(05 Oct '13, 16:48)</span> Jasper ♦♦</div></div></div><div id="comment-tools-21583" class="comment-tools"></div><div class="clear"></div><div id="comment-21583-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="45334"></span>

<div id="answer-container-45334" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45334-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p><code>tcprewrite</code> from <code>tcpreplay</code> can do this.</p><p>You need to overwride the output format to Ethernet II, and supply the source MAC and dest MAC which the Cooked Capture format mangles.</p><p>For example:</p><pre><code>tcprewrite --dlt=enet --enet-dmac=52:54:00:11:11:11 --enet-smac=52:54:00:22:22:22 -i in.pcap -o out.pcap</code></pre><p><code>tcprewrite</code> appears to understand the concept of a two-way conversation, so comma-separated MACs can be specified for each participant in a two-way conversation. See <code>man tcprewrite</code> for full syntax.</p><p>References:</p><ul><li><a href="http://sourceforge.net/p/tcpreplay/mailman/message/25348859/">http://sourceforge.net/p/tcpreplay/mailman/message/25348859/</a></li><li><a href="http://tcpreplay.synfin.net/wiki/tcprewrite#RewritingLayer2">http://tcpreplay.synfin.net/wiki/tcprewrite#RewritingLayer2</a></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '15, 19:29</strong></p><img src="https://secure.gravatar.com/avatar/1cadd3b79b540cd9f93ef00bdc3980da?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="superjamie&#39;s gravatar image" /><p>superjamie<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="superjamie has no accepted answers">0%</span></p></div></div><div id="comments-container-45334" class="comments-container"></div><div id="comment-tools-45334" class="comment-tools"></div><div class="clear"></div><div id="comment-45334-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

