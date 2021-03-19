+++
type = "question"
title = "PNIO Dissector Incorrect When FCS in Capture"
description = '''I am using the EtherShark tap and it delivers the Ethernet Frame Check Sum, along with the rest of the frame, to Wireshark. Wireshark dissector for PNIO messages incorrectly assumes that the FCS is part of the Profinet data resulting in the following errors: 1) Cycle number incorrectly identified as...'''
date = "2014-11-14T07:26:00Z"
lastmod = "2014-11-14T07:33:00Z"
weight = 37859
keywords = [ "pnio", "fcs" ]
aliases = [ "/questions/37859" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [PNIO Dissector Incorrect When FCS in Capture](/questions/37859/pnio-dissector-incorrect-when-fcs-in-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37859-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using the EtherShark tap and it delivers the Ethernet Frame Check Sum, along with the rest of the frame, to Wireshark. Wireshark dissector for PNIO messages incorrectly assumes that the FCS is part of the Profinet data resulting in the following errors: 1) Cycle number incorrectly identified as the first 2 bytes of the FCS 2) Data Status incorrectly identified as byte 3 of FCS 3) Transfer Status incorrectly identified as byte 4 of FCS 4) Profinet IO Cyclic Service Data Unit length bloated by 4 bytes 5) User Data (including GAP and RTCPadding) bloated by 4 bytes.</p><p>Other profinet messages seem unaffected, although I have not studied other message types in great detail as of yet.</p><p>I tried using editcap to remove the last 4 bytes but this did not work as the dissectors recognized the bytes were missing.</p><p>How can I work around this problem??</p></div><div id="question-tags" class="tags-container tags">pnio fcs</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '14, 07:26</strong></p><img src="https://secure.gravatar.com/avatar/ee762f19ea4e10a09e7e59252fade168?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mark_w1&#39;s gravatar image" /><p>mark_w1<br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mark_w1 has no accepted answers">0%</span></p></div></div><div id="comments-container-37859" class="comments-container"></div><div id="comment-tools-37859" class="comment-tools"></div><div class="clear"></div><div id="comment-37859-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37860"></span>

<div id="answer-container-37860" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37860-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you tried setting the preferences for the Ethernet dissector to "Assume packets have FCS"?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '14, 07:33</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-37860" class="comments-container"><span id="37868"></span><div id="comment-37868" class="comment"><div id="post-37868-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much for the answer. It does resolve the PNIO dissector issue, however, all frames now show FCS errors. I believe the tap or USB driver removed the VLAN(0) tag QOS/TOS bits and therfore the checksum is incorrect. I will investigate further.</p></div><div id="comment-37868-info" class="comment-info"><span class="comment-age">(14 Nov '14, 10:34)</span> mark_w1</div></div></div><div id="comment-tools-37860" class="comment-tools"></div><div class="clear"></div><div id="comment-37860-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

