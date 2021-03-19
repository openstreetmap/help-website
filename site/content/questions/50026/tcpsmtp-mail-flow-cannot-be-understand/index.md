+++
type = "question"
title = "TCP/SMTP mail flow cannot be understand ?"
description = '''SMTP mail server problem cannot be understand how it was gone. Can you help me to identify the attack or type of issue regarding this source and destination ? cloud shark - https://www.cloudshark.org/captures/50e23e13bb31 ip.src == 172.17.107.32 &amp;amp;&amp;amp; ip.dst == 104.88.178.74 '''
date = "2016-02-09T12:42:00Z"
lastmod = "2016-02-09T13:24:00Z"
weight = 50026
keywords = [ "smtp" ]
aliases = [ "/questions/50026" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP/SMTP mail flow cannot be understand ?](/questions/50026/tcpsmtp-mail-flow-cannot-be-understand)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50026-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>SMTP mail server problem cannot be understand how it was gone. <strong>Can you help me to identify the attack or type of issue regarding this source and destination ?</strong></p><p>cloud shark - <a href="https://www.cloudshark.org/captures/50e23e13bb31">https://www.cloudshark.org/captures/50e23e13bb31</a></p><p>ip.src == 172.17.107.32 &amp;&amp; ip.dst == 104.88.178.74</p><p><img src="https://osqa-ask.wireshark.org/upfiles/smtp_02_ZHZD7HN.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">smtp</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '16, 12:42</strong></p><img src="https://secure.gravatar.com/avatar/ff7c46d7b334bbb8fa01a5eef4ea3b14?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bhagya&#39;s gravatar image" /><p>Bhagya<br />
<span class="score" title="4 reputation points">4</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bhagya has no accepted answers">0%</span></p></img></div></div><div id="comments-container-50026" class="comments-container"></div><div id="comment-tools-50026" class="comment-tools"></div><div class="clear"></div><div id="comment-50026-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50028"></span>

<div id="answer-container-50028" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50028-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you use a slightly different display filter, <code>ip.src == 172.17.107.32 and ip.dst == 104.88.178.74</code> , you'll see that the 172...32 (probably yours as it is on a private IP address) has attempted to send an e-mail from [email protected], but the receiving SMTP server 104..74 has refused to accept it, explaining that the domain virginmedia.com is on some blacklist.</p><p>If you use a display filter <code>smtp</code>, you'll see that such kind of rejection is not rare in the capture, from several different SMTP servers.</p><p>So now</p><ul><li><p>if the 172...32 is your PC attempting to send this without your knowledge, it indicates that it became part of some botnet due to infection by some malware. Sending spam is just one of things the owner of the botnet can ask your PC to do, so you should visit your malware specialist immediately (and disconnect the PC from the net as the first thing),</p></li><li><p>if the 172...32 is your mailserver, you should take some measures similar to those used by the peer SMTP servers so that you wouldn't forward the spam sent to you by other SMTP servers.</p></li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '16, 13:24</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-50028" class="comments-container"><span id="50134"></span><div id="comment-50134" class="comment"><div id="post-50134-score" class="comment-score"></div><div class="comment-text"><p>It's the way of botnet. Analyzing could be find out about it.</p><p>Thank you very much.</p><p>And while going through the other streams found things to</p><p>1) What is TCP Re-transmission ?</p><p>2) [PSH, ACK] defines ?</p></div><div id="comment-50134-info" class="comment-info"><span class="comment-age">(12 Feb '16, 04:48)</span> Bhagya</div></div><span id="50135"></span><div id="comment-50135" class="comment"><div id="post-50135-score" class="comment-score"></div><div class="comment-text"><p>PSH is an attribute of a TCP packet which the sender uses if it wants the recipient to immediately start handling the data received so far. Normally, the TCP stack at receiver side would accumulate the received data in a buffer and offer them to the application when the buffer is full enough (to save CPU time); reception of a packet with PSH flag set says it should offer the buffer contents to the application immediately, regardless its size. So if the communication between the client and the server is message-based, and a single protocol message (PDU, protocol data unit) uses more than one TCP packet, the last packet carrying the PDU is often sent with PSH set to 1.</p><p>A re-transmission means that a source sends again a packet which it has already sent before, because it has learnt, by explicit or implicit means, that the previously sent packet has not reached the recipient. It is not a TCP-specific behaviour.</p></div><div id="comment-50135-info" class="comment-info"><span class="comment-age">(12 Feb '16, 05:06)</span> sindy</div></div><span id="50159"></span><div id="comment-50159" class="comment"><div id="post-50159-score" class="comment-score"></div><div class="comment-text"><p>So, PSH is said that to push the data immediately back to the application which requests ?</p><p>PSH flag mention that main task is to push up the receiving application data immediate ?</p></div><div id="comment-50159-info" class="comment-info"><span class="comment-age">(12 Feb '16, 09:32)</span> Bhagya</div></div><span id="50163"></span><div id="comment-50163" class="comment"><div id="post-50163-score" class="comment-score"></div><div class="comment-text"><p>@Bhagya, these questions regarding TCP retransmission and meaning of PSH should have been asked as separate new Questions, as this is the idea of this site. So I'll try to clarify the PSH still here, as it seems you didn't get the point of my explanation, but please ask any additional questions (although they may be loosely related to what we have discussed here) as separate ones.</p><p>Now to the PSH: a TCP session provides a bi-directional, point-to-point communication channel over IP network. Imagine just one direction of the data transmission to consist of the following elements:</p><ul><li>the sending application</li><li>the TCP, IP, ethernet protocol stack on the sending machine</li><li>the IP network</li><li>the ethernet, IP, TCP stack on the receiving machine</li><li>the receiving application.</li></ul><p>When the sending application indicates to the sending TCP stack that the data it has just written to the sending buffer should be marked with PSH, the tcp stack sends out whatever data it currently has in its buffer, in as many packets as necessary to accommodate that data, and in the last packet sent, it sets the PSH bit. The receiving TCP stack stores any received packets' payload in its receiving buffer, and notifies the receiving application about availability of new data in that buffer based on its own decision. But if it receives a packet with PSH set, it notifies the receiving application immediately.</p><p>So no push "back" takes place. The push is in the same direction like the data itself.</p></div><div id="comment-50163-info" class="comment-info"><span class="comment-age">(12 Feb '16, 12:22)</span> sindy</div></div><span id="51516"></span><div id="comment-51516" class="comment"><div id="post-51516-score" class="comment-score"></div><div class="comment-text"><p>Got it.. This was very helpful and all were went clear. Thank you for kind response.</p></div><div id="comment-51516-info" class="comment-info"><span class="comment-age">(08 Apr '16, 08:20)</span> Bhagya</div></div></div><div id="comment-tools-50028" class="comment-tools"></div><div class="clear"></div><div id="comment-50028-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

