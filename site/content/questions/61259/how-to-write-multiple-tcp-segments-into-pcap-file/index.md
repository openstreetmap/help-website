+++
type = "question"
title = "How to write multiple TCP segments into PCAP file?"
description = '''Hello all, I am able to successfully write one TCP packet with payload to a PCAP file. The written PCAP file has one frame obviously. Now, I need to write multiple frames into this PCAP file. Here is the procedure I have done so far to write two frames into PCAP file: 1&amp;gt; write global header pcap_...'''
date = "2017-05-05T13:48:00Z"
lastmod = "2017-05-05T14:10:00Z"
weight = 61259
keywords = [ "pcap", "tcp" ]
aliases = [ "/questions/61259" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to write multiple TCP segments into PCAP file?](/questions/61259/how-to-write-multiple-tcp-segments-into-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61259-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>I am able to successfully write one TCP packet with payload to a PCAP file. The written PCAP file has one frame obviously.</p><p>Now, I need to write multiple frames into this PCAP file. Here is the procedure I have done so far to write two frames into PCAP file:</p><pre><code>1&gt; write global header pcap_hdr_t
2&gt; write first packet header pcaprec_hdr_t
3&gt; write first packet data(TCP with a payload of 10 bytes)
4&gt; write second packet header pcaprec_hdr_t
5&gt; write second packet data(TCP with a payload of 4 bytes)</code></pre><p>For the sequence and acknowledge numbers, I always write 0 as follows:</p><pre><code>tcpHeader.seq_num = 0x00;
tcpHeader.ack_num = 0x00;</code></pre><p>After loading the generated PCAP with wireshark, the complains that "This frame is out of order segment". Basically, I have two sequence of bytes and need to store them as PCAP format(i.e. payloads of TCP packet) and I don't care about the ACK etc typically come with TCP/IP packet from network.</p><p>Question&gt; What is the correct way to fix this issue?</p><p>Thank you</p><p><img src="https://osqa-ask.wireshark.org/upfiles/ack1.PNG" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/ack2.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">pcap tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 May '17, 13:48</strong></p><img src="https://secure.gravatar.com/avatar/ec5ada4e8208a8fa410847ae421bf229?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="q0987&#39;s gravatar image" /><p>q0987<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="q0987 has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 05 May '17, 14:52</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></img></div></div><div id="comments-container-61259" class="comments-container"></div><div id="comment-tools-61259" class="comment-tools"></div><div class="clear"></div><div id="comment-61259-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61260"></span>

<div id="answer-container-61260" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61260-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to increment the TCP sequence number for the second packet by the amount of TCP payload bytes in the first packet, so it needs to be 10, not 0 for the second packet. The third packet (if you're going to write it later) has to have a sequence number of 14 (10 from the first, 4 from the second packet), and so on.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 May '17, 14:10</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-61260" class="comments-container"></div><div id="comment-tools-61260" class="comment-tools"></div><div class="clear"></div><div id="comment-61260-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

