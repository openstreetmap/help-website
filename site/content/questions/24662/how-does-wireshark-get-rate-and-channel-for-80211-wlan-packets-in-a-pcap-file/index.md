+++
type = "question"
title = "How does wireshark get Rate and channel for 802.11 WLAN packets in a pcap file?"
description = '''The file format in http://wiki.wireshark.org/Development/LibpcapFileFormat has no field for rate or channel of the packets sniffed, i was wondering how wireshark extracts that information. Also please point me to how wireshark calculates the FCS for each packet. Thank you.'''
date = "2013-09-13T16:41:00Z"
lastmod = "2013-09-13T17:52:00Z"
weight = 24662
keywords = [ "wlan_rate_pcap" ]
aliases = [ "/questions/24662" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How does wireshark get Rate and channel for 802.11 WLAN packets in a pcap file?](/questions/24662/how-does-wireshark-get-rate-and-channel-for-80211-wlan-packets-in-a-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24662-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The file format in <a href="http://wiki.wireshark.org/Development/LibpcapFileFormat">http://wiki.wireshark.org/Development/LibpcapFileFormat</a> has no field for rate or channel of the packets sniffed, i was wondering how wireshark extracts that information. Also please point me to how wireshark calculates the FCS for each packet.</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">wlan_rate_pcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '13, 16:41</strong></p><img src="https://secure.gravatar.com/avatar/320250ab70b248159a7d2783bbc420a3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emma&#39;s gravatar image" /><p>emma<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emma has no accepted answers">0%</span></p></div></div><div id="comments-container-24662" class="comments-container"></div><div id="comment-tools-24662" class="comment-tools"></div><div class="clear"></div><div id="comment-24662-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24663"></span>

<div id="answer-container-24663" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24663-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>The file format in <a href="http://wiki.wireshark.org/Development/LibpcapFileFormat">http://wiki.wireshark.org/Development/LibpcapFileFormat</a> has no field for rate or channel of the packets sniffed</p></blockquote><p>It also has no field for the Ethernet address or type fields, or the PPP address and type fields, or the 802.11 frame control and address fields, or.... :-)</p><p>Per-link-layer type metadata, such as 802.11 radio information, is provided in "pseudo-headers" that are supplied as part of the packet data. The most common format for 802.11 radio information in pcap (and pcap-ng) files is the <a href="http://www.radiotap.org">radiotap</a> format, but there are some others that may be seen as well. See <a href="http://www.tcpdump.org/linktypes.html">the tcpdump.org list of link-layer header types</a> for details.</p><blockquote><p>point me to how wireshark calculates the FCS for each packet.</p></blockquote><p>If the capture data includes the FCS, Wireshark uses a 32-bit CRC routine (that routine is part of Wireshark) to calculate what the FCS <em>should</em> be, and compares that with the <em>actual</em> CRC to see whether there's a CRC error.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '13, 17:52</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-24663" class="comments-container"><span id="25251"></span><div id="comment-25251" class="comment"><div id="post-25251-score" class="comment-score"></div><div class="comment-text"><p>I am wondering how i can get the packet airtime in microseconds, not the beginning (timestamp), i mean the length of the packet but in microseconds</p></div><div id="comment-25251-info" class="comment-info"><span class="comment-age">(25 Sep '13, 17:39)</span> emma</div></div><span id="25252"></span><div id="comment-25252" class="comment"><div id="post-25252-score" class="comment-score">1</div><div class="comment-text"><p>Well, if you're willing to calculate it based on the packet length and the packet data rate (as, for example, <a href="http://code.google.com/p/skybluetero/">SkyBlueTero</a> does; see the tshark command it runs in <a href="http://code.google.com/p/skybluetero/source/browse/trunk/filterer.py">filter.py</a>), you could parse the radiotap header (if present), looking for the data rate field, and use that, along with the packet length field from the packet's pcap header. (If the packet doesn't have a radio metadata header that gives the data rate, you can't do it).</p></div><div id="comment-25252-info" class="comment-info"><span class="comment-age">(25 Sep '13, 17:47)</span> Guy Harris ♦♦</div></div><span id="25288"></span><div id="comment-25288" class="comment"><div id="post-25288-score" class="comment-score"></div><div class="comment-text"><p>That is exactly what i was trying to do and i noticed that some pcap files don't have the radio tap header. Thank you so much, you have been a great help :)</p></div><div id="comment-25288-info" class="comment-info"><span class="comment-age">(26 Sep '13, 10:51)</span> emma</div></div><span id="25289"></span><div id="comment-25289" class="comment"><div id="post-25289-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>i noticed that some pcap files don't have the radio tap header</p></blockquote><p>If they start with an Ethernet header, they were probably not captured in monitor mode; on most OSes, you can only get radio information (and 802.11 headers rather than fake Ethernet headers) in monitor mode.</p><p>If they start with an 802.11 header, whoever captured it probably explicitly asked for just 802.11 headers without radiotap headers.</p></div><div id="comment-25289-info" class="comment-info"><span class="comment-age">(26 Sep '13, 10:56)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-24663" class="comment-tools"></div><div class="clear"></div><div id="comment-24663-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

