+++
type = "question"
title = "TDS: Malformed Packet"
description = '''Good morning, When analyzing a trace I found this message for more I look online I find esponse to what is past, and if the error is real or not. Can you help? [Malformed Packet: TDS]  Expert Info (Error/Malformed): Malformed Packet (Exception occurred)  Message: Malformed Packet (Exception occurred...'''
date = "2011-04-13T01:30:00Z"
lastmod = "2011-09-11T20:28:00Z"
weight = 3475
keywords = [ "tds", "malformed" ]
aliases = [ "/questions/3475" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [TDS: Malformed Packet](/questions/3475/tds-malformed-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3475-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Good morning,</p><p>When analyzing a trace I found this message for more I look online I find esponse to what is past, and if the error is real or not. Can you help?</p><p>[Malformed Packet: TDS] Expert Info (Error/Malformed): Malformed Packet (Exception occurred) Message: Malformed Packet (Exception occurred) Severity level: Error Group: Malformed I have, Windows Server 2003 and SQL Server 2005. Thanks.</p></div><div id="question-tags" class="tags-container tags">tds malformed</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Apr '11, 01:30</strong></p><img src="https://secure.gravatar.com/avatar/66454f31c258595639d1ba0d08a0424a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dagonpal&#39;s gravatar image" /><p>dagonpal<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dagonpal has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Apr '11, 01:34</p></div></div><div id="comments-container-3475" class="comments-container"></div><div id="comment-tools-3475" class="comment-tools"></div><div class="clear"></div><div id="comment-3475-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="3486"></span>

<div id="answer-container-3486" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3486-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark thinks the packet is malformed. This could be because it really is malformed. A few possible reasons might be because the snaplen causes the packet to be truncated during capturing, or the packet could have been malformed originally by the sender. The packet could have become corrupted in transit or intentionally by a fuzz-tester, for example. On the other hand, the packet could be just fine and it's incorrectly being reported as malformed due to a bug in the Wireshark TDS dissector.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Apr '11, 09:04</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-3486" class="comments-container"><span id="3493"></span><div id="comment-3493" class="comment"><div id="post-3493-score" class="comment-score"></div><div class="comment-text"><p>OK, I understand, but, how do I know if I can truly be a malformed packet or a packet is correct?</p></div><div id="comment-3493-info" class="comment-info"><span class="comment-age">(14 Apr '11, 00:02)</span> dagonpal</div></div><span id="3499"></span><div id="comment-3499" class="comment"><div id="post-3499-score" class="comment-score"></div><div class="comment-text"><p>Well, that requires some knowledge of both the protocol and the dissector itself. Here are some links to documents that might help you out:</p><ul><li>The <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/dissectors/packet-tds.c?revision=36332&amp;view=markup">packet-tds.c</a> source code.</li><li>The <a href="http://www.freetds.org/tds.html">TDS Protocol Documentation</a> page.</li></ul><p>If, after some examination, you think the TDS dissector is somehow flawed, you might want to <a href="https://bugs.wireshark.org/bugzilla/">open a bug report</a> and upload your sample capture file to it.</p></div><div id="comment-3499-info" class="comment-info"><span class="comment-age">(14 Apr '11, 07:56)</span> cmaynard ♦♦</div></div><span id="3562"></span><div id="comment-3562" class="comment"><div id="post-3562-score" class="comment-score"></div><div class="comment-text"><p>OK perfect, thank´s.</p></div><div id="comment-3562-info" class="comment-info"><span class="comment-age">(18 Apr '11, 07:27)</span> dagonpal</div></div><span id="3582"></span><div id="comment-3582" class="comment"><div id="post-3582-score" class="comment-score"></div><div class="comment-text"><p>(I converted your "answer" to a "comment", that's the way this Q&amp;A site works best, see also the FAQ. Please also accept an "answer" by clicking on the checkmark next to it if it did indeed answer your question so that your question will not be listed on the unanswered questions list anymore)</p></div><div id="comment-3582-info" class="comment-info"><span class="comment-age">(18 Apr '11, 13:07)</span> SYN-bit ♦♦</div></div><span id="6287"></span><div id="comment-6287" class="comment"><div id="post-6287-score" class="comment-score"></div><div class="comment-text"><p>See also: <a href="http://msdn.microsoft.com/en-us/library/dd304523%28v=prot.13%29.aspx">[MS-TDS]: Tabular Data Stream Protocol Specification</a></p></div><div id="comment-6287-info" class="comment-info"><span class="comment-age">(12 Sep '11, 08:03)</span> Bill Meier ♦♦</div></div></div><div id="comment-tools-3486" class="comment-tools"></div><div class="clear"></div><div id="comment-3486-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3510"></span>

<div id="answer-container-3510" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3510-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In addition to the possibilities Chris Maynard suggested, the TDS dissector tries to detect TDS traffic not to or from ports 1433 or 2433 by looking at otherwise-unidentified TCP traffic to see if it looks like TDS traffic; this could result in incorrectly identifying non-TDS traffic as TDS and reporting it as malformed TDS traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '11, 09:36</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Apr '11, 09:36</p></div></div><div id="comments-container-3510" class="comments-container"></div><div id="comment-tools-3510" class="comment-tools"></div><div class="clear"></div><div id="comment-3510-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6276"></span>

<div id="answer-container-6276" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6276-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I had the same problem looking at a pcap from SQL Server and then I saw the hardware was Itanium. I changed it to big endian in the TDS protocol settings and everything parsed ok. Just noting it in case you have the same problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Sep '11, 20:28</strong></p><img src="https://secure.gravatar.com/avatar/62b20ca1c29bcd217fae490abdb04e72?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cfed&#39;s gravatar image" /><p>cfed<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cfed has no accepted answers">0%</span></p></div></div><div id="comments-container-6276" class="comments-container"></div><div id="comment-tools-6276" class="comment-tools"></div><div class="clear"></div><div id="comment-6276-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

