+++
type = "question"
title = "Malformed Packet: DCERPC Protocol"
description = '''Hi,  I encountered malformed packets although the application works ok. This is based on WireShark 1.4.4 and 1.5.  The traffic is between my Application Server via F5 to DB (and vice versa). Attached is the dump: 0000 00 1b 21 33 8b 9b 00 01 d7 c1 e5 03 08 00 45 00 ..!3.... ......E. 0010 00 39 a6 6d...'''
date = "2011-03-30T00:04:00Z"
lastmod = "2011-04-01T03:50:00Z"
weight = 3222
keywords = [ "packets", "malformed" ]
aliases = [ "/questions/3222" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Malformed Packet: DCERPC Protocol](/questions/3222/malformed-packet-dcerpc-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3222-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I encountered malformed packets although the application works ok. This is based on WireShark 1.4.4 and 1.5.</p><p>The traffic is between my Application Server via F5 to DB (and vice versa). Attached is the dump:</p><p>0000 00 1b 21 33 8b 9b 00 01 d7 c1 e5 03 08 00 45 00 ..!3.... ......E. 0010 00 39 a6 6d 40 00 ff 06 8e 82 0a 32 a8 d2 0a 32 [email protected] ...2...2 0020 89 98 f7 b0 fc b2 23 a7 42 35 de 8d 0e d0 50 18 ......#. B5....P. 0030 80 00 df 1b 00 00 05 00 02 30 b9 01 01 00 00 00 ........ .0...... 0040 00 01 01 00 00 00 00 01 14 00 00 00 02 76 73 5f ........ .....vs_ 0050 6f 72 61 63 6c 65 00 00 00 00 00 00 00 oracle.. .....</p><p>Does anyone has any ideas on the reason(s)?</p><p>Thanks!</p><p>regards, Jackson</p></div><div id="question-tags" class="tags-container tags">packets malformed</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Mar '11, 00:04</strong></p><img src="https://secure.gravatar.com/avatar/42c84876390390081c1f435fd96d3406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jackson%20Lim&#39;s gravatar image" /><p>Jackson Lim<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jackson Lim has no accepted answers">0%</span></p></div></div><div id="comments-container-3222" class="comments-container"><span id="3225"></span><div id="comment-3225" class="comment"><div id="post-3225-score" class="comment-score"></div><div class="comment-text"><p>This is decoded as DCERPC response. Does your connection use RPC? If not, you can consider to disable DCERPC for a time, since it's called by heuristic.</p></div><div id="comment-3225-info" class="comment-info"><span class="comment-age">(30 Mar '11, 04:24)</span> harper</div></div></div><div id="comment-tools-3222" class="comment-tools"></div><div class="clear"></div><div id="comment-3222-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3267"></span>

<div id="answer-container-3267" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3267-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi Harper,</p><p>I believe WireShark made a mistake in diagnosing the packet as a DCERPC response. The connection in question is actually an Oracle SQL*NET connection on TCP. There are no DCERPC protocol used as the only DCE found in Oracle, which is used for authentication as part of Oracle Advanced Security, is not enabled at all (i.e. sqlnet.ora does not exist at all).</p><p>I tried to decipher the packet manually using packet specification found in the RFC document of TCP, which specifies (as formalized in the following RFC-793: http://www.ietf.org/rfc/rfc793.txt) the requirement that the TCP header ends with padding (of variable length of zeroes) to ensure that the data starts at the 32-bit boundary. It did not specify that the data part of the TCP packet must start with any bits.</p><p>The data byte of the TCP packet starts with byte "05 00" and the second packet (which is not flagged as malformed") starts with "03 81." However it seems that from WireShark's diagnosis, the byte "05 00" from the first packet denotes the start of a DCE/RPC packet of ncacn_ip_tcp type (DCE/RPC that run on top of TCP protocol). In my opinion, the byte "05 00" is actually a normal and valid TCP packet and not a DCE/RPC packet.</p><p>Can you help to confirm my findings? In addition, how do I reflect this findings to the WireShark Core Development Team so that the next version of WireShark will avoid this incorrect analysis?</p><p>Thanks for your advice.</p><p>regards, Jackson</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Apr '11, 03:50</strong></p><img src="https://secure.gravatar.com/avatar/42c84876390390081c1f435fd96d3406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jackson%20Lim&#39;s gravatar image" /><p>Jackson Lim<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jackson Lim has no accepted answers">0%</span></p></div></div><div id="comments-container-3267" class="comments-container"><span id="3318"></span><div id="comment-3318" class="comment"><div id="post-3318-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>It seems that WireShark has wrongly decoded the Oracle packets at Network Layer 4 as DCE-RPC protocol instead of Oracle TNS protocol. By manually setting the decoder to "TNS", there were no packets "deemed to be malformed".</p><p>Can this behaviour be automatically incorporated into the next version of WireShark?</p><p>regards, Jackson</p></div><div id="comment-3318-info" class="comment-info"><span class="comment-age">(03 Apr '11, 23:48)</span> Jackson Lim</div></div><span id="3373"></span><div id="comment-3373" class="comment"><div id="post-3373-score" class="comment-score"></div><div class="comment-text"><p>I don't know if this discussion is monitored by the core developers. I suggest to post this to the wireshark developer list.</p><p>see http://www.wireshark.org/lists/</p></div><div id="comment-3373-info" class="comment-info"><span class="comment-age">(06 Apr '11, 06:43)</span> harper</div></div><span id="3378"></span><div id="comment-3378" class="comment"><div id="post-3378-score" class="comment-score"></div><div class="comment-text"><p>DCE RPC packets <em>ARE</em> "normal and valid TCP packets"; DCE RPC runs on top of TCP as well as UDP and other protocols (such as SMB).</p><p>DCE RPC protocols (with a few exceptions) do not have particular ports assigned to them; therefore, the only way Wireshark can detect them automatically is to look at part of the payload for transport protocols such as TCP and UDP to see if the packet looks as if it might be a DCE RPC packet. Those "heuristics" do not, and cannot, always get the right answer.</p></div><div id="comment-3378-info" class="comment-info"><span class="comment-age">(06 Apr '11, 09:21)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-3267" class="comment-tools"></div><div class="clear"></div><div id="comment-3267-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

