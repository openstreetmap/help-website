+++
type = "question"
title = "Combine ending part of packet with starting part of the next packet. (to dissect later on.))"
description = '''Hi all; We have developed a dissector to analyze a log file filled with TCP packets. Each packet contains one or more messages that are previously specified with starting and ending keywords(bytes).  But we faced with a problem. Some messages starts at the end of a packet and continues at the start ...'''
date = "2013-05-16T01:26:00Z"
lastmod = "2013-05-16T02:08:00Z"
weight = 21171
keywords = [ "merge", "dissector", "combine", "reassemble", "tcp" ]
aliases = [ "/questions/21171" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Combine ending part of packet with starting part of the next packet. (to dissect later on.))](/questions/21171/combine-ending-part-of-packet-with-starting-part-of-the-next-packet-to-dissect-later-on)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21171-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all; We have developed a dissector to analyze a log file filled with TCP packets. Each packet contains one or more messages that are previously specified with starting and ending keywords(bytes).</p><p>But we faced with a problem. Some messages starts at the end of a packet and continues at the start of the next packet. How can we combine these two parts of bytes and then apply dissection on it?</p><p>Anyone has an experience with that kind of case?</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">merge dissector combine reassemble tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 May '13, 01:26</strong></p><img src="https://secure.gravatar.com/avatar/6a00de8bbb0f734aa577de7dd00b3e52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="barisalis&#39;s gravatar image" /><p>barisalis<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="barisalis has one accepted answer">100%</span></p></div></div><div id="comments-container-21171" class="comments-container"></div><div id="comment-tools-21171" class="comment-tools"></div><div class="clear"></div><div id="comment-21171-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21173"></span>

<div id="answer-container-21173" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21173-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>What you need is reassembly. There are two ways of doing this:</p><ol><li>Use tcp_dissect_pdus() when you can determine the total length of the PDU within a fixed amount of bytes at the beginning of your PDU.</li><li>Modify the pinfo struct to tell the TCP dissector to collect more data.</li></ol><p>Both options are described in par 2.7 of <a href="http://anonsvn.wireshark.org/viewvc/trunk/doc/README.developer">README.developer</a></p><p>If you need more info or help after reading README.developer, feel free to ask :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '13, 02:08</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 May '13, 02:08</p></div></div><div id="comments-container-21173" class="comments-container"><span id="21176"></span><div id="comment-21176" class="comment"><div id="post-21176-score" class="comment-score"></div><div class="comment-text"><p>For our case; 1) Packet sizes are not fixed. <em>(Packets can contain one or more than one messages inside.)</em> 2) Message lengths are not fixed. <em>(Different lengths for different messages)</em></p><p>So I think we should work on the second option <em>(Modify the pinfo struct to tell the TCP dissector to collect more data.)</em>.</p><p>What you suggest further?</p></div><div id="comment-21176-info" class="comment-info"><span class="comment-age">(16 May '13, 03:27)</span> barisalis</div></div><span id="21177"></span><div id="comment-21177" class="comment"><div id="post-21177-score" class="comment-score"></div><div class="comment-text"><p>Can you determine the length of each PDU by reading some part of the header of the PDU? If so, then use tcp_dissect_pdus(). If not, i.e. you have to read to the end of the pdu to determine its length then the 2nd method should be used.</p></div><div id="comment-21177-info" class="comment-info"><span class="comment-age">(16 May '13, 03:35)</span> grahamb ♦</div></div><span id="21179"></span><div id="comment-21179" class="comment"><div id="post-21179-score" class="comment-score"></div><div class="comment-text"><p>Thanks!! we can see the result as below. But we wonder if there is any way to dissect this reassembled PDU.</p><hr /><p>2 Reassembled TCP Segments (160 bytes): #5641(20), #5643(140)</p><p>Frame: 5641, payload: 0-19 (20 bytes)</p><p>Frame: 5643, payload: 20-159 (140 bytes)</p><p>Segment count: 2</p><p>Reassembled TCP length: 160</p></div><div id="comment-21179-info" class="comment-info"><span class="comment-age">(16 May '13, 04:08)</span> barisalis</div></div><span id="21181"></span><div id="comment-21181" class="comment"><div id="post-21181-score" class="comment-score"></div><div class="comment-text"><p>The problem is perfectly solved. Thanks for your quick help.</p></div><div id="comment-21181-info" class="comment-info"><span class="comment-age">(16 May '13, 04:58)</span> barisalis</div></div></div><div id="comment-tools-21173" class="comment-tools"></div><div class="clear"></div><div id="comment-21173-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

