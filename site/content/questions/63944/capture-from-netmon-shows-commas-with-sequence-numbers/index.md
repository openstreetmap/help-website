+++
type = "question"
title = "Capture from NetMon shows commas with sequence numbers"
description = '''Hi There: I have a capture that was done using NetMon. Some of the streams seem disjointed, there are FIN, SYN, RST, PSH ECN flags set. Also what is weird is that the sequence number has comma&#x27;s in them, like 1082,0 No idea what to do with this. Thank you paul'''
date = "2017-10-16T14:27:00Z"
lastmod = "2017-10-17T11:35:00Z"
weight = 63944
keywords = [ "streaming", "netmon" ]
aliases = [ "/questions/63944" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture from NetMon shows commas with sequence numbers](/questions/63944/capture-from-netmon-shows-commas-with-sequence-numbers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63944-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi There:</p><p>I have a capture that was done using NetMon.</p><p>Some of the streams seem disjointed, there are FIN, SYN, RST, PSH ECN flags set.</p><p>Also what is weird is that the sequence number has comma's in them, like 1082,0</p><p>No idea what to do with this.</p><p>Thank you</p><p>paul</p></div><div id="question-tags" class="tags-container tags">streaming netmon</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Oct '17, 14:27</strong></p><img src="https://secure.gravatar.com/avatar/fbe6825b890bc4c637a5160e6fb707a3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pauli&#39;s gravatar image" /><p>Pauli<br />
<span class="score" title="0 reputation points">0</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pauli has no accepted answers">0%</span></p></div></div><div id="comments-container-63944" class="comments-container"><span id="63947"></span><div id="comment-63947" class="comment"><div id="post-63947-score" class="comment-score"></div><div class="comment-text"><p>We'd need to see the capture file (preferably <em>not</em> a screenshot or a printout of it, but the file itself) to look at it and determine what's happening.</p></div><div id="comment-63947-info" class="comment-info"><span class="comment-age">(16 Oct '17, 15:53)</span> Guy Harris ♦♦</div></div><span id="63963"></span><div id="comment-63963" class="comment"><div id="post-63963-score" class="comment-score"></div><div class="comment-text"><p><a href="https://osqa-ask.wireshark.org/upfiles/Bogus_header_364.jpg">link text</a></p></div><div id="comment-63963-info" class="comment-info"><span class="comment-age">(17 Oct '17, 06:09)</span> Pauli</div></div><span id="63964"></span><div id="comment-63964" class="comment"><div id="post-63964-score" class="comment-score"></div><div class="comment-text"><p>Hi Guy:</p><p>Thanks for the reply, I added a screen shot in the previous comment.</p><p>The trouble packet is 364.</p><p>The packet is a response from the server (which is actually and MFP).</p><p>The communication is from packet 348 to 367, which is communication over port 50003.</p><p>What is weird is that packet 364 shows a completely different port number. We know this is the correct packet stream because we see it on the other side.</p><p>Thanks for any help you can provide.</p><p>Pauli</p></div><div id="comment-63964-info" class="comment-info"><span class="comment-age">(17 Oct '17, 06:14)</span> Pauli</div></div><span id="63976"></span><div id="comment-63976" class="comment"><div id="post-63976-score" class="comment-score"></div><div class="comment-text"><p>Please show the detailed dissection of frame 364. Without that, we can't determine 1) why there are two sequence numbers being shown in the SEQ column and 2) why it shows a different port number.</p></div><div id="comment-63976-info" class="comment-info"><span class="comment-age">(17 Oct '17, 11:17)</span> Guy Harris ♦♦</div></div><span id="63977"></span><div id="comment-63977" class="comment"><div id="post-63977-score" class="comment-score"></div><div class="comment-text"><p>Here you go, I dont think you will need the TLS:</p><p><a href="https://osqa-ask.wireshark.org/upfiles/Bogus_header_364-1.jpg">link text</a></p></div><div id="comment-63977-info" class="comment-info"><span class="comment-age">(17 Oct '17, 11:29)</span> Pauli</div></div></div><div id="comment-tools-63944" class="comment-tools"></div><div class="clear"></div><div id="comment-63944-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63978"></span>

<div id="answer-container-63978" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63978-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>OK, the SSL/TLS dissector somehow thinks that what's being carried over TLS is raw TCP, so, as interpreted by Wireshark, there are (as I suspected) two TCP headers in the packet, and there are therefore</p><ul><li>two sequence numbers in the packet, so it's displaying two sequence numbers in the SEQ column (which is presumably a custom column showing the <code>tcp.seq</code> field);</li><li>two source port numbers in the packet, and two destination port numbers in the packet, and the Info column shows the ones for the headers that are last in the packet, i.e. the purported TCP header atop TLS.</li></ul><p>This may just be a bug in Wireshark. Please file a bug in <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>, and attach the <em>raw capture file</em> (not a screenshot, but the <em>raw capture file</em>) to the bug. In order to determine the cause of the bug, and to test the fix, we need the <em>raw capture file</em>, so that we can see how Wireshark dissects it, and make sure it dissects it correctly once we've made a fix.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '17, 11:35</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Oct '17, 11:36</p></div></div><div id="comments-container-63978" class="comments-container"></div><div id="comment-tools-63978" class="comment-tools"></div><div class="clear"></div><div id="comment-63978-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

