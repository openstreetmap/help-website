+++
type = "question"
title = "Dup ACKs question"
description = '''I have a capture of the beginning of a file transfer where there is a number of duplicate ACKs. This capture was taken between the client and server.  1: 15:56:07.240527 172.16.1.1.51629 &amp;gt; 192.168.1.100.80: S 1044283510:1044283510(0) win 8192 &amp;lt;mss 1460,nop,wscale 2,nop,nop,sackOK&amp;gt;  2: 15:56...'''
date = "2012-12-10T09:52:00Z"
lastmod = "2012-12-10T12:06:00Z"
weight = 16750
keywords = [ "ack" ]
aliases = [ "/questions/16750" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Dup ACKs question](/questions/16750/dup-acks-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16750-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I have a capture of the beginning of a file transfer where there is a number of duplicate ACKs. This capture was taken between the client and server.</p><pre><code>   1: 15:56:07.240527 172.16.1.1.51629 &gt; 192.168.1.100.80: S 1044283510:1044283510(0) win 8192 &lt;mss 1460,nop,wscale 2,nop,nop,sackOK&gt;
   2: 15:56:07.240740 192.168.1.100.80 &gt; 172.16.1.1.51629: S 1864868747:1864868747(0) ack 1044283511 win 4140 &lt;mss 1380,nop,wscale 0,sackOK,eol&gt;
   3: 15:56:07.241290 172.16.1.1.51629 &gt; 192.168.1.100.80: . ack 1864868748 win 16560
   4: 15:56:07.241991 172.16.1.1.51629 &gt; 192.168.1.100.80: P 1044283511:1044283940(429) ack 1864868748 win 16560
   5: 15:56:07.242831 192.168.1.100.80 &gt; 172.16.1.1.51629: . 1864868748:1864870128(1380) ack 1044283940 win 4569
   6: 15:56:07.242846 192.168.1.100.80 &gt; 172.16.1.1.51629: P 1864870128:1864870267(139) ack 1044283940 win 4569
   7: 15:56:07.242861 192.168.1.100.80 &gt; 172.16.1.1.51629: . 1864870267:1864871647(1380) ack 1044283940 win 4569
   8: 15:56:07.242876 192.168.1.100.80 &gt; 172.16.1.1.51629: . 1864871647:1864873027(1380) ack 1044283940 win 4569
   9: 15:56:07.243273 172.16.1.1.51629 &gt; 192.168.1.100.80: . ack 1864868748 win 16560 &lt;nop,nop,sack sack 1 {1864870128:1864870267} &gt;
   10: 15:56:07.243288 172.16.1.1.51629 &gt; 192.168.1.100.80: . ack 1864868748 win 16560 &lt;nop,nop,sack sack 1 {1864870128:1864871647} &gt;
   11: 15:56:07.243288 172.16.1.1.51629 &gt; 192.168.1.100.80: . ack 1864868748 win 16560 &lt;nop,nop,sack sack 1 {1864870128:1864873027} &gt;
   12: 15:56:07.243487 192.168.1.100.80 &gt; 172.16.1.1.51629: P 1864873027:1864874407(1380) ack 1044283940 win 4569
   13: 15:56:07.243487 192.168.1.100.80 &gt; 172.16.1.1.51629: P 1864874407:1864875787(1380) ack 1044283940 win 4569
   14: 15:56:07.243502 192.168.1.100.80 &gt; 172.16.1.1.51629: . 1864868748:1864870128(1380) ack 1044283940 win 4569</code></pre><p>Within this I am trying to locate the segment that was lost. My questions are :</p><ul><li>Does the ACK number correspond to the previous SEQ number or the SEQ plus the data total ?</li><li>In this capture is it right that it appears that the segment with the SEQ # 1864868748 is lost and then retransmitted ?</li><li>Is there any reason that in this case the next SEQ number is not the previous ACK + 1 ?.</li></ul><p>Thanks,</p></div><div id="question-tags" class="tags-container tags">ack</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Dec '12, 09:52</strong></p><img src="https://secure.gravatar.com/avatar/22baebd906c29ccfcb5b2aeb350b22fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bart80&#39;s gravatar image" /><p>bart80<br />
<span class="score" title="11 reputation points">11</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bart80 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Dec '12, 09:54</p></div></div><div id="comments-container-16750" class="comments-container"></div><div id="comment-tools-16750" class="comment-tools"></div><div class="clear"></div><div id="comment-16750-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16753"></span>

<div id="answer-container-16753" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16753-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>ACK Number always tells "give me the following sequence number in your next packet" So if you have recieved Sequence Number 1,001 containing 500 Bytes you (as TCP) go and ACK 1,501 --&gt; give me <a href="http://seq.nr">seq.nr</a>. 1,501 in your next packet.</p><p>That's also the reason why the next SEQ is not previous ACK+1.</p><p>You correctly interpreted the packet with Seq. xyz68748 as being the one getting lost. That's also why the reciever keeps telling ACK xyz68748 - "give me that packet"</p><p>If you're unfamiliar with those TCP basics, I suggest you start with <a href="http://en.wikipedia.org/wiki/Transmission_Control_Protocol">the WiKi Page about TCP</a> because from there you can easily follow everything inside wireshark to get a better understanding of the protocol.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Dec '12, 12:06</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-16753" class="comments-container"><span id="16756"></span><div id="comment-16756" class="comment"><div id="post-16756-score" class="comment-score"></div><div class="comment-text"><p>Many thanks. That all makes sense. I`ll check out the link. However can you confirm what the Segment SEQ 1044283511 is for. As the previous ACK is for 1864868748 so should the following packet be the 1864868748 SEQ #.</p></div><div id="comment-16756-info" class="comment-info"><span class="comment-age">(10 Dec '12, 13:32)</span> bart80</div></div><span id="16764"></span><div id="comment-16764" class="comment"><div id="post-16764-score" class="comment-score">1</div><div class="comment-text"><p>You mixed up the two stations SEQ and ACK numbers -&gt; in frame 1 you have SEQ Nr. 1044283510 containing the SYN Bit inside TCP header, which counts as 1 Byte Payload. That's why the next packet from that station has SEQ 1044283510+1</p></div><div id="comment-16764-info" class="comment-info"><span class="comment-age">(11 Dec '12, 02:59)</span> Landi</div></div><span id="16765"></span><div id="comment-16765" class="comment"><div id="post-16765-score" class="comment-score"></div><div class="comment-text"><p>That makes sense. Many Thanks,</p></div><div id="comment-16765-info" class="comment-info"><span class="comment-age">(11 Dec '12, 05:53)</span> bart80</div></div><span id="16766"></span><div id="comment-16766" class="comment"><div id="post-16766-score" class="comment-score"></div><div class="comment-text"><p>You're welcome - if the answer solved your questions please respond to that by clicking the Accept Button right next to the answer to mark the question as answered and closed</p></div><div id="comment-16766-info" class="comment-info"><span class="comment-age">(11 Dec '12, 07:08)</span> Landi</div></div></div><div id="comment-tools-16753" class="comment-tools"></div><div class="clear"></div><div id="comment-16753-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

