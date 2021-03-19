+++
type = "question"
title = "Intercepting traffic of cable modems"
description = '''Hi there, i want to check differences in Traffic which occur between cable modem and router, and traffic between the coaxial jack and cable modem. As i can easily set up a proxy between modem and router and intercept ethernet traffic with tcpdump or wireshark the other side of the cable modem seems ...'''
date = "2014-03-12T02:26:00Z"
lastmod = "2015-04-19T08:35:00Z"
weight = 30711
keywords = [ "modem", "eurodocsis", "coaxial", "cable", "docsis" ]
aliases = [ "/questions/30711" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Intercepting traffic of cable modems](/questions/30711/intercepting-traffic-of-cable-modems)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30711-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>i want to check differences in Traffic which occur between cable modem and router, and traffic between the coaxial jack and cable modem. As i can easily set up a proxy between modem and router and intercept ethernet traffic with tcpdump or wireshark the other side of the cable modem seems to be more complicated.</p><p>Cable modems are using DOCSIS standard (EuroDOCSIS in Europe) which can be encrypted. As well i don't have an idea how i could connect my proxy with the coaxial cable. Are there any adapters which can help here in connection with a demodulator?</p><p>Because wireshark has got a DOCSIS dissector i assume, that it should be possible to catch that docsis traffic "out of the cable".</p><p>I found a video called "Sniffing cable modems" but the aspect how to connect the proxy via coaxial cable is not discussed in detail.</p><p>Best Regards, Bastian</p></div><div id="question-tags" class="tags-container tags">modem eurodocsis coaxial cable docsis</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Mar '14, 02:26</strong></p><img src="https://secure.gravatar.com/avatar/1cd9e3324f5061cdcb2ea68cb5fe8a01?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CipherSpec&#39;s gravatar image" /><p>CipherSpec<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CipherSpec has no accepted answers">0%</span></p></div></div><div id="comments-container-30711" class="comments-container"></div><div id="comment-tools-30711" class="comment-tools"></div><div class="clear"></div><div id="comment-30711-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="30750"></span>

<div id="answer-container-30750" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30750-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Because wireshark has got a DOCSIS dissector i assume, that it should be possible to catch that docsis traffic "out of the cable".</p></blockquote><p>Not necessarily. Wireshark can read captures in many different file formats, and some of them contain packet types that the mechanisms that libpcap/WinPcap use can't capture.</p><p>In the case of DOCSIS, that was added to Wireshark because some Cisco "cable modem termination systems" (CMTS) for the "head end" of cable modem networks (i.e., for use at the cable company's site) can take DOCSIS packets, wrap them in Ethernet low-level framing (no Ethernet header, just the raw octets of a DOCSIS packet, preceded by an Ethernet preamble and start frame delimiter and terminated by an Ethernet FCS), and put them out on an Ethernet. Support was added to libpcap/WinPcap to, when capturing on an Ethernet device, use a link-layer header type of DOCSIS rather than Ethernet, and Wireshark can read those files.</p><p>Sadly, I don't know of any cable <em>modems</em> that support the same mechanism that the Cisco CMTSes do.</p><p>The "sniffing cable modems" video that pops up when I do a search is the one by Guy Martin; <a href="https://har2009.org/program/attachments/62_sniffing-cable-modems-har2009.pdf">the slides from that talk</a> speak of using a DVB-C card to capture traffic in one direction and a <a href="http://home.ettus.com">USRP</a> device to capture traffic in the other direction, but don't give any details. Guy Martin definitely knows about Wireshark, and the slides have his e-mail address; he might have some advice on hardware to use to sniff cable modem traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '14, 19:26</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-30750" class="comments-container"></div><div id="comment-tools-30750" class="comment-tools"></div><div class="clear"></div><div id="comment-30750-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41572"></span>

<div id="answer-container-41572" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41572-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>A <code>cable monitor</code> command that forwards packets on the cable interface to the Ethernet interface(for use by external analyzers) is only available on Cisco broadband routers on CMTS (like Cisco uBRxxxx). Wireshark DOCSIS dissector is only for that kind of usage. Docsis use RF interface to transmit Ethernet packets, i.e. Ethernet packets are translated into radio frequency signals that sent to the head-end, then translated back to Ethernet and dropped into the cable network. RF-interface use different type of network adapter, and different standard for link-layer data transmission, it's not Ethernet adapter. Therefore, this requires demodulate RF-interface packets into Ethernet interface packets, so hardware is needed to implement this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '15, 08:35</strong></p><img src="https://secure.gravatar.com/avatar/246308319911b02b765397caa24b76c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="quantex&#39;s gravatar image" /><p>quantex<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="quantex has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Apr '15, 08:37</p></div></div><div id="comments-container-41572" class="comments-container"><span id="41578"></span><div id="comment-41578" class="comment"><div id="post-41578-score" class="comment-score"></div><div class="comment-text"><p>Actually, DOCSIS uses the RF interface to transmit DOCSIS packets; that's what the Wireshark DOCSIS dissector dissects, and what would be included in packets for which the link-layer header type value is <code>LINKTYPE_DOCSIS</code>, as per <a href="http://www.tcpdump.org/linktypes.html">the tcpdump.org link-layer header types page</a>.</p><p>That entry says</p><blockquote><p>DOCSIS MAC frames, as described by <a href="http://www.cablelabs.com/specifications/CM-SP-MULPIv3.0-I15-110210.pdf">the DOCSIS 3.0 MAC and Upper Layer Protocols Interface Specification</a>.</p></blockquote><p>So it's not just "Ethernet over cable".</p></div><div id="comment-41578-info" class="comment-info"><span class="comment-age">(19 Apr '15, 11:54)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-41572" class="comment-tools"></div><div class="clear"></div><div id="comment-41572-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

