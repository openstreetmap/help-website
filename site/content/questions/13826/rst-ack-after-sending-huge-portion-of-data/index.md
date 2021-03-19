+++
type = "question"
title = "RST, ACK after sending huge portion of data"
description = '''I have IMAP server (e.g. Dovecot). I try to create 1200 mailboxes (for test performance). Servers successfully performs it. After this operation I want to list all created folders. Server gives some portion of data but after some time (near 1 second) CLIENT sends RST, ACK to server while server resp...'''
date = "2012-08-22T12:53:00Z"
lastmod = "2012-08-26T01:27:00Z"
weight = 13826
keywords = [ "reset", "rst", "tcp" ]
aliases = [ "/questions/13826" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [RST, ACK after sending huge portion of data](/questions/13826/rst-ack-after-sending-huge-portion-of-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13826-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have <strong>IMAP</strong> server (e.g. <strong>Dovecot</strong>). I try to create 1200 mailboxes (for test performance). Servers successfully performs it. After this operation I want to list all created folders. Server gives some portion of data but after some time (near 1 second) CLIENT sends <strong>RST, ACK</strong> to server while server responds with <strong>IMAP</strong> protocol's command about the list of created folders.</p><p>Here is all mine <strong>Wireshark</strong>'s dump snippet:</p><p><strong>IMAP</strong>: Src Port: imap (143), Dst Port: 56794 (56794), Seq: 29186, Ack: 20533, Len: 24</p><p><strong>IMAP</strong>: Src Port: 56794 (56794), Dst Port: imap (143), Seq: 20533, Ack: 29210, Len: 15</p><p><strong>IMAP</strong>: Src Port: imap (143), Dst Port: 56794 (56794), Seq: 29210, Ack: 20548, Len: 16384</p><p><strong>TCP</strong>: 56794 &gt; imap [ACK] Seq=20548 Ack=45594 Win=49408 Len=0 TSV=3940902 TSER=3940902</p><p><strong>IMAP</strong>: Src Port: imap (143), Dst Port: 56794 (56794), Seq: 45594, Ack: 20548, Len: 16384</p><p><strong>TCP</strong>: 56794 &gt; imap [RST, ACK] Seq=20548 Ack=61978 Win=49408 Len=0 TSV=3940902 TSER=3940902</p><p><strong>Edit:</strong> Well, I think I figured out why <strong>RST</strong> flag is sent by client. The reason is server exceed <strong>MTU</strong> value for my loopback interface. I have checked similar behavior for sample Mina server - and all is OK there, i.e. huge packets are spited by TCP/IP protocol. So <strong>Dovecot</strong> can't manage packets wisely. But I have my own IMAP server (based on MINA) and the problem still persist there!</p><p>I've captured with Wireshark all negotiation, if interested: <a href="http://www.4shared.com/file/ymJ90Y1s/rst_mtu_555.html">http://www.4shared.com/file/ymJ90Y1s/rst_mtu_555.html</a> , the MTU value here set to 555</p><p><strong>So why TCP/IP protocol manages sent packets (split them according to MTU value) wisely only for some apps but not for all?</strong></p></div><div id="question-tags" class="tags-container tags">reset rst tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Aug '12, 12:53</strong></p><img src="https://secure.gravatar.com/avatar/3db629d9f410495f7e183245eb2b2395?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michael%20Z&#39;s gravatar image" /><p>Michael Z<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michael Z has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Aug '12, 00:05</p></div></div><div id="comments-container-13826" class="comments-container"></div><div id="comment-tools-13826" class="comment-tools"></div><div class="clear"></div><div id="comment-13826-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13896"></span>

<div id="answer-container-13896" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13896-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>sounds like your IMAP client crashed while getting (parsing) the mailbox/folder list.</p><p>Some questions:</p><ul><li>What is your IMAP client?</li><li>What is your OS version where your run the IMAP client?</li><li>Do you see any error messages on the IMAP client?</li><li>Did you try another IMAP client?</li><li>A "malformed" IMAP answer might cause the client to crash or close the connection. Did you check the answer of the IMAP server in the capture file? Does it "look good" (according to the IMAP specs)? It should, if the server is a decent version of dovecot.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '12, 01:27</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-13896" class="comments-container"><span id="13905"></span><div id="comment-13905" class="comment"><div id="post-13905-score" class="comment-score"></div><div class="comment-text"><p>By order: 1) Client is my own written Java code that connects to IMAP port. 2) Ubuntu 10.04 64 bit 3) No. See 1) 4) Yes, I've tried Evolution. It successfully lists all 1200 mailboxes. 5) There is no malformed answer from IMAP server. IT answer interrupted by client after some portion of data. As for Dovecot it writes <em>Connection closed: Connection reset by peer bytes=20505/68146</em></p><p>Please see my edit in addition.</p></div><div id="comment-13905-info" class="comment-info"><span class="comment-age">(27 Aug '12, 00:03)</span> Michael Z</div></div><span id="13910"></span><div id="comment-13910" class="comment"><div id="post-13910-score" class="comment-score"></div><div class="comment-text"><blockquote><p>4) Yes, I've tried Evolution. It successfully lists all 1200 mailboxes.</p></blockquote><p>So, obviously not network or server problem.</p><blockquote><p>IT answer interrupted by client after some portion of data.</p></blockquote><p>Well, then I guess it's a bug in your Java client. I don't think you can troubleshoot that with Wireshark, as the reason for the connection RESET cannot be detected by Wireshark. It might be a buffer "overflow" at the client or simply a programming error.</p><p>I suggest to debug the Java client.</p></div><div id="comment-13910-info" class="comment-info"><span class="comment-age">(27 Aug '12, 04:21)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-13896" class="comment-tools"></div><div class="clear"></div><div id="comment-13896-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

