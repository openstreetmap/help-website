+++
type = "question"
title = "rssi field in wireshark"
description = '''hello, the rssi field is 8 bits according to ieee 802.11 standard . so i wanted to know how wireshark is using these 8 bits? iein which format it filling them.?? thank you in advance'''
date = "2016-10-20T19:21:00Z"
lastmod = "2016-10-21T07:38:00Z"
weight = 56547
keywords = [ "rssi" ]
aliases = [ "/questions/56547" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [rssi field in wireshark](/questions/56547/rssi-field-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56547-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello, the rssi field is 8 bits according to ieee 802.11 standard . so i wanted to know how wireshark is using these 8 bits? iein which format it filling them.??</p><p>thank you in advance</p></div><div id="question-tags" class="tags-container tags">rssi</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Oct '16, 19:21</strong></p><img src="https://secure.gravatar.com/avatar/11d703ea8508cf72c52f1718280bb7bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="misbah&#39;s gravatar image" /><p>misbah<br />
<span class="score" title="0 reputation points">0</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="misbah has no accepted answers">0%</span></p></div></div><div id="comments-container-56547" class="comments-container"></div><div id="comment-tools-56547" class="comment-tools"></div><div class="clear"></div><div id="comment-56547-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56568"></span>

<div id="answer-container-56568" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56568-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I assume you are talking about the RSSI (SSI Signal) in the radiotap header. The value reported in the packet details pane is in dBm, which is a measure of RF signal power at the antenna, in decibels difference from 1mW.</p><p>The radiotap spec says the field is a signed 8-bit value, so to get from the raw hex bytes shown in the packet bytes pane to the value reported in the packet details pane, you need to take the two's complement.</p><p>For example: if 0xD1 is shown in the bytes panel, the two's complement of that is shown in the details pane (-47 dBm)</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_sYgLx8q.PNG" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '16, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/6acf3c1293dde7d08c204b9265e46764?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="J_Turner&#39;s gravatar image" /><p>J_Turner<br />
<span class="score" title="71 reputation points">71</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="J_Turner has no accepted answers">0%</span></p></img></div></div><div id="comments-container-56568" class="comments-container"><span id="56574"></span><div id="comment-56574" class="comment"><div id="post-56574-score" class="comment-score"></div><div class="comment-text"><p>thank you @j_Turner , that explains my doubt. i was also wondering what is the entire field in the highlighted 0010 register??</p></div><div id="comment-56574-info" class="comment-info"><span class="comment-age">(21 Oct '16, 14:18)</span> misbah</div></div><span id="56575"></span><div id="comment-56575" class="comment"><div id="post-56575-score" class="comment-score"></div><div class="comment-text"><p>It's not a field, it's a bunch of fields. It is part of the <a href="http://www.radiotap.org">radiotap header</a>, which is a variable-length header that the networking drivers on *BSD and macOS, the drivers and mac80211 code on Linux, and the drivers and Npcap code on Windows, provide as a "pseudo-header" before the packet data when capturing.</p><p>There are other 802.11 radio information pseudo-headers used with the pcap and pcapng file formats, and other capture file formats may provide that information in some other fashion. Wireshark 2.x transforms the radiotap and other pseudo-headers, and the information supplied in other file formats, into a standard format, and displays that under "802.11 radio information", so that information is provided twice for radiotap and other pseudo-headers.</p></div><div id="comment-56575-info" class="comment-info"><span class="comment-age">(21 Oct '16, 21:02)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-56568" class="comment-tools"></div><div class="clear"></div><div id="comment-56568-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

