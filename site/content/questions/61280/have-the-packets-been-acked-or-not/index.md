+++
type = "question"
title = "Have the packets been ACKed or not ?"
description = '''Hi, I&#x27;m troubleshooting a strange behaviour in an HTTP download. I&#x27;m capturing (at the moment) just by client side. https://www.dropbox.com/s/q3bxhxos55j1cv0/Test_1_Client_view_1.0.xlsx?dl=0 In the following days I will do the same in several points in the path and on the server too. But now I need ...'''
date = "2017-05-08T05:41:00Z"
lastmod = "2017-05-09T00:57:00Z"
weight = 61280
keywords = [ "ack" ]
aliases = [ "/questions/61280" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Have the packets been ACKed or not ?](/questions/61280/have-the-packets-been-acked-or-not)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61280-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm troubleshooting a strange behaviour in an HTTP download.</p><p>I'm capturing (at the moment) just by client side. <a href="https://www.dropbox.com/s/q3bxhxos55j1cv0/Test_1_Client_view_1.0.xlsx?dl=0">https://www.dropbox.com/s/q3bxhxos55j1cv0/Test_1_Client_view_1.0.xlsx?dl=0</a></p><p>In the following days I will do the same in several points in the path and on the server too.</p><p>But now I need to explain this:</p><p>Client receives 307 Spurious Retransmission from Server. It means that it has received also the original 307 packets.</p><p>I know that a cause of these 307 Retransmissions done by the server towards the client could be that the server did not receive the ACK from client.</p><p>Before moving to have a look at the capture in the path and on the server, my questions are :</p><p>In the capture taken on client.....</p><ul><li><p>Did the client acknowledge the original 307 packets coming from the server ?</p></li><li><p>For example, the first SEQ 3996984356 coming from the Server, in which ACK packet has been acknowledged by the client ?</p></li><li><p>How do you discover it ?</p></li></ul><p>Thanks a lot</p></div><div id="question-tags" class="tags-container tags">ack</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 May '17, 05:41</strong></p><img src="https://secure.gravatar.com/avatar/bba638c3a54975c52c98530defa199af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ValerioItaly&#39;s gravatar image" /><p>ValerioItaly<br />
<span class="score" title="5 reputation points">5</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ValerioItaly has no accepted answers">0%</span></p></div></div><div id="comments-container-61280" class="comments-container"><span id="61283"></span><div id="comment-61283" class="comment"><div id="post-61283-score" class="comment-score"></div><div class="comment-text"><p>Is the link you provided an Excel spreadsheet? Can you instead provide a link to a packet capture file?</p></div><div id="comment-61283-info" class="comment-info"><span class="comment-age">(08 May '17, 08:00)</span> cmaynard ♦♦</div></div><span id="61288"></span><div id="comment-61288" class="comment"><div id="post-61288-score" class="comment-score"></div><div class="comment-text"><p>Sanitize your pcap if you need to: <a href="https://blog.packet-foo.com/2016/11/the-wireshark-qa-trace-file-sharing-tutorial/">https://blog.packet-foo.com/2016/11/the-wireshark-qa-trace-file-sharing-tutorial/</a></p></div><div id="comment-61288-info" class="comment-info"><span class="comment-age">(08 May '17, 08:52)</span> Jasper ♦♦</div></div><span id="61292"></span><div id="comment-61292" class="comment"><div id="post-61292-score" class="comment-score"></div><div class="comment-text"><p>Here you can find the capture : <a href="https://www.cloudshark.org/captures/f9c27db6a2aa">https://www.cloudshark.org/captures/f9c27db6a2aa</a></p><p>Thanks a lot</p></div><div id="comment-61292-info" class="comment-info"><span class="comment-age">(08 May '17, 13:42)</span> ValerioItaly</div></div><span id="61314"></span><div id="comment-61314" class="comment"><div id="post-61314-score" class="comment-score"></div><div class="comment-text"><p>Hi, about what kind of environment do we talk? I can see a round trip time of (iRTT) of 22 ms. Is there a WAN link in the path?</p></div><div id="comment-61314-info" class="comment-info"><span class="comment-age">(09 May '17, 13:22)</span> Christian_R</div></div></div><div id="comment-tools-61280" class="comment-tools"></div><div class="clear"></div><div id="comment-61280-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61296"></span>

<div id="answer-container-61296" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61296-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The data you referencing (display filter <code>tcp.seq == 3996984356</code>) gets transmitted by the server (for the the first time ) in frame 4655 (<code>frame.number==4655</code>). Then there is a spurious retransmit in frame 5634 for this data..</p><p>It's spurious because the client already acknowledges the data with a <a href="https://tools.ietf.org/html/rfc2018">Selective ACK</a> in frame 4656 (so right after receiving the first transmit).</p><p>Site note: The SACK option can only handle five ranges (due to max size of TCP header). However in your capture it's seems there is more packet loss. Therefore the ranges shifts during the data transfer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 May '17, 00:57</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p>Uli<br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-61296" class="comments-container"><span id="61297"></span><div id="comment-61297" class="comment"><div id="post-61297-score" class="comment-score"></div><div class="comment-text"><p>Hi Uli, thanks a lot for your help.</p><p>Very useful to know the "Site Note" about the Max couples of SLE/SRE that can be displayed.</p><p>Could you kindly help me to understand how can you notice that in the SLE/SRE info of the packet 4656, there is the ACK of the packet 4655 ?</p></div><div id="comment-61297-info" class="comment-info"><span class="comment-age">(09 May '17, 01:40)</span> ValerioItaly</div></div><span id="61299"></span><div id="comment-61299" class="comment"><div id="post-61299-score" class="comment-score"></div><div class="comment-text"><p>Frame 4655 has a SEQ#3996984356, TCP data length is 1380 Bytes =&gt; tcp.nxtseq == <strong>3996985736</strong>.</p><p>Frame 4656 ACKs 3995738216 and additional the SACK for ranges 3996982976-3996985736, 3996920876-3996981596, 3996862916-3996919496 and 3996798056-3996861536.</p><p>This means the client has received among others the bytes 3996982976-<strong>3996985736</strong> =&gt; Data which was transmitted in frame 4655 (and some other frames before).</p></div><div id="comment-61299-info" class="comment-info"><span class="comment-age">(09 May '17, 02:47)</span> Uli</div></div><span id="61328"></span><div id="comment-61328" class="comment"><div id="post-61328-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot !!</p></div><div id="comment-61328-info" class="comment-info"><span class="comment-age">(10 May '17, 05:44)</span> ValerioItaly</div></div><span id="61329"></span><div id="comment-61329" class="comment"><div id="post-61329-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-61329-info" class="comment-info"><span class="comment-age">(10 May '17, 05:46)</span> grahamb ♦</div></div></div><div id="comment-tools-61296" class="comment-tools"></div><div class="clear"></div><div id="comment-61296-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

