+++
type = "question"
title = "Malformed MIH 802.21 Packet"
description = '''I have the following capture from a network of two nodes using MIH 802.21 Protocol. I am using Wireshark Version 1.12.7 on Ubuntu 14.04 x64. The MIH message seems to be OK in the binary format, however Wireshark considers it as a malformed packet. Wireshark is not able to interpret after the TLV len...'''
date = "2015-10-29T03:42:00Z"
lastmod = "2015-10-29T05:17:00Z"
weight = 47054
keywords = [ "802.21", "malformed", "mih" ]
aliases = [ "/questions/47054" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Malformed MIH 802.21 Packet](/questions/47054/malformed-mih-80221-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47054-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have the following capture from a network of two nodes using MIH 802.21 Protocol. I am using Wireshark Version 1.12.7 on Ubuntu 14.04 x64. The MIH message seems to be OK in the binary format, however Wireshark considers it as a malformed packet. Wireshark is not able to interpret after the TLV length field of the Source MIHF ID TLV. So is it a problem in the protocol serialization or Wireshark dissector itself?</p><p>From the binary format: We have MIH header length of 8 Bytes which is interpreted correctly by Wireshark. Then Source MIHF ID TLV is 1 + 1 + 12 = 14 Bytes. The same thing for the destination MIHF ID TLV = 14 Bytes. Then Link Identifier List TLV comes which has TLV Type of (25 in Decimal or 0x19) and length of zero. Finally Registration Code TLV which has TLV Type of (11 in Decimal or 0xb) and length of one byte. The total size of this MIH frame is 41 Bytes.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screenshot_from_2015-10-29_11:02:17.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">802.21 malformed mih</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Oct '15, 03:42</strong></p><img src="https://secure.gravatar.com/avatar/566cfe38b17a31f0dc825c86538cf3d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hany%20Assasa&#39;s gravatar image" /><p>Hany Assasa<br />
<span class="score" title="21 reputation points">21</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hany Assasa has no accepted answers">0%</span></p></img></div></div><div id="comments-container-47054" class="comments-container"></div><div id="comment-tools-47054" class="comment-tools"></div><div class="clear"></div><div id="comment-47054-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47060"></span>

<div id="answer-container-47060" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47060-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>A proper bug report in <a href="https://bugs.wireshark.org">bugzilla</a> could see this solved in a following release.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Oct '15, 05:17</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-47060" class="comments-container"><span id="47145"></span><div id="comment-47145" class="comment"><div id="post-47145-score" class="comment-score"></div><div class="comment-text"><p>I have already reported it as a bug <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11653">MIH Malformed Packet</a></p></div><div id="comment-47145-info" class="comment-info"><span class="comment-age">(02 Nov '15, 04:03)</span> Hany Assasa</div></div></div><div id="comment-tools-47060" class="comment-tools"></div><div class="clear"></div><div id="comment-47060-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

