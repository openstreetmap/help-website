+++
type = "question"
title = "Strange packets captured."
description = '''Does anybody have any idea on why the client received so many ACK packets within such a short time?  16562 16:03:24.960676 122.11.56.106 10.201.228.43 TCP [TCP segment of a reassembled PDU]  16563 16:03:24.961409 10.201.228.43 122.11.56.106 TCP 41945 &amp;gt; 80 [ACK] Seq=305 Ack=4912489 Win=224352 Len=...'''
date = "2011-11-23T23:31:00Z"
lastmod = "2011-11-25T14:47:00Z"
weight = 7594
keywords = [ "tcp" ]
aliases = [ "/questions/7594" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Strange packets captured.](/questions/7594/strange-packets-captured)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7594-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does anybody have any idea on why the client received so many ACK packets within such a short time?</p><pre><code>  16562 16:03:24.960676 122.11.56.106         10.201.228.43         TCP      [TCP segment of a reassembled PDU]
  16563 16:03:24.961409 10.201.228.43         122.11.56.106         TCP      41945 &gt; 80 [ACK] Seq=305 Ack=4912489 Win=224352 Len=0 TSV=24813 TSER=1978476727
  16567 16:03:24.967421 122.11.56.106         10.201.228.43         TCP      [TCP segment of a reassembled PDU]
  16569 16:03:24.979078 122.11.56.106         10.201.228.43         TCP      [TCP segment of a reassembled PDU]
  16570 16:03:24.979872 10.201.228.43         122.11.56.106         TCP      41945 &gt; 80 [ACK] Seq=305 Ack=4915225 Win=224352 Len=0 TSV=24815 TSER=1978476727
  16573 16:03:24.982801 122.11.56.106         10.201.228.43         TCP      [TCP segment of a reassembled PDU]
  16574 16:03:24.983015 10.201.228.43         122.11.56.106         TCP      41945 &gt; 80 [ACK] Seq=305 Ack=4916594 Win=224352 Len=0 TSV=24815 TSER=1978476731
  16578 16:03:25.044386 122.11.56.106         10.201.228.43         TCP      [TCP Dup ACK 16573#1] 80 &gt; 41945 [ACK] Seq=4916594 Ack=305 Win=6912 Len=0 TSV=1978476745 TSER=24805
  16580 16:03:25.186384 122.11.56.106         10.201.228.43         TCP      [TCP Dup ACK 16573#2] 80 &gt; 41945 [ACK] Seq=4916594 Ack=305 Win=6912 Len=0 TSV=1978476759 TSER=24815
  16587 16:03:25.218489 122.11.56.106         10.201.228.43         TCP      [TCP Dup ACK 16573#3] 80 &gt; 41945 [ACK] Seq=4916594 Ack=305 Win=6912 Len=0 TSV=1978476761 TSER=24815
  16589 16:03:25.261427 122.11.56.106         10.201.228.43         TCP      [TCP Dup ACK 16573#4] 80 &gt; 41945 [ACK] Seq=4916594 Ack=305 Win=6912 Len=0 TSV=1978476765 TSER=24815
  16590 16:03:25.276075 10.201.228.43         122.11.56.106         TCP      41945 &gt; 80 [FIN, ACK] Seq=305 Ack=4916594 Win=224352 Len=0 TSV=24844 TSER=1978476765
  16594 16:03:25.287672 122.11.56.106         10.201.228.43         TCP      [TCP Dup ACK 16573#5] 80 &gt; 41945 [ACK] Seq=4916594 Ack=305 Win=6912 Len=0 TSV=1978476769 TSER=24815
  16596 16:03:25.315748 122.11.56.106         10.201.228.43         TCP      [TCP Dup ACK 16573#6] 80 &gt; 41945 [ACK] Seq=4916594 Ack=305 Win=6912 Len=0 TSV=1978476771 TSER=24815
  16601 16:03:25.350416 122.11.56.106         10.201.228.43         TCP      [TCP Dup ACK 16573#7] 80 &gt; 41945 [ACK] Seq=4916594 Ack=305 Win=6912 Len=0 TSV=1978476775 TSER=24815
  16603 16:03:25.366804 122.11.56.106         10.201.228.43         TCP      [TCP Dup ACK 16573#8] 80 &gt; 41945 [ACK] Seq=4916594 Ack=305 Win=6912 Len=0 TSV=1978476777 TSER=24815
  16605 16:03:25.424574 122.11.56.106         10.201.228.43         TCP      [TCP Dup ACK 16573#9] 80 &gt; 41945 [ACK] Seq=4916594 Ack=305 Win=6912 Len=0 TSV=1978476783 TSER=24815
  16608 16:03:25.471785 122.11.56.106         10.201.228.43         TCP      [TCP Dup ACK 16573#10] 80 &gt; 41945 [ACK] Seq=4916594 Ack=305 Win=6912 Len=0 TSV=1978476787 TSER=24815
  16610 *REF*           122.11.56.106         10.201.228.43         TCP      [TCP Dup ACK 16573#11] 80 &gt; 41945 [ACK] Seq=4916594 Ack=305 Win=6912 Len=0 TSV=1978476789 TSER=24815
  16612 16:03:25.536055 122.11.56.106         10.201.228.43         TCP      [TCP Dup ACK 16573#12] 80 &gt; 41945 [ACK] Seq=4916594 Ack=305 Win=6912 Len=0 TSV=1978476793 TSER=24815
  16614 16:03:25.564375 122.11.56.106         10.201.228.43         TCP      [TCP Dup ACK 16573#13] 80 &gt; 41945 [ACK] Seq=4916594 Ack=305 Win=6912 Len=0 TSV=1978476797 TSER=24815
  16616 16:03:25.589369 122.11.56.106         10.201.228.43         TCP      [TCP Dup ACK 16573#14] 80 &gt; 41945 [ACK] Seq=4916594 Ack=305 Win=6912 Len=0 TSV=1978476799 TSER=24815
  16618 16:03:25.651716 122.11.56.106         10.201.228.43         TCP      [TCP Dup ACK 16573#15] 80 &gt; 41945 [ACK] Seq=4916594 Ack=305 Win=6912 Len=0 TSV=1978476805 TSER=24815
  16620 16:03:25.664869 122.11.56.106         10.201.228.43         TCP      [TCP Dup ACK 16573#16] 80 &gt; 41945 [ACK] Seq=4916594 Ack=305 Win=6912 Len=0 TSV=1978476807 TSER=24815
  16623 16:03:25.710402 122.11.56.106         10.201.228.43         TCP      [TCP Dup ACK 16573#17] 80 &gt; 41945 [ACK] Seq=4916594 Ack=305 Win=6912 Len=0 TSV=1978476811 TSER=24815
  16625 16:03:25.744459 122.11.56.106         10.201.228.43         TCP      [TCP Dup ACK 16573#18] 80 &gt; 41945 [ACK] Seq=4916594 Ack=305 Win=6912 Len=0 TSV=1978476815 TSER=24815
  16627 16:03:25.769270 122.11.56.106         10.201.228.43         TCP      [TCP Dup ACK 16573#19] 80 &gt; 41945 [ACK] Seq=4916594 Ack=305 Win=6912 Len=0 TSV=1978476817 TSER=24815
  16629 16:03:25.807508 122.11.56.106         10.201.228.43         TCP      [TCP Dup ACK 16573#20] 80 &gt; 41945 [ACK] Seq=4916594 Ack=305 Win=6912 Len=0 TSV=1978476821 TSER=24815
  16631 16:03:25.853346 122.11.56.106         10.201.228.43         TCP      [TCP Dup ACK 16573#21] 80 &gt; 41945 [ACK] Seq=4916594 Ack=305 Win=6912 Len=0 TSV=1978476825 TSER=24815
  16633 16:03:25.894026 122.11.56.106         10.201.228.43         TCP      [TCP Dup ACK 16573#22] 80 &gt; 41945 [ACK] Seq=4916594 Ack=305 Win=6912 Len=0 TSV=1978476829 TSER=24815
  16635 16:03:25.939314 122.11.56.106         10.201.228.43         TCP      [TCP Dup ACK 16573#23] 80 &gt; 41945 [ACK] Seq=4916594 Ack=305 Win=6912 Len=0 TSV=1978476833 TSER=24815
  16636 16:03:26.115217 10.201.228.43         122.11.56.106         TCP      41945 &gt; 80 [FIN, ACK] Seq=305 Ack=4916594 Win=224352 Len=0 TSV=24929 TSER=1978476833
  16638 16:03:26.130659 122.11.56.106         10.201.228.43         TCP      [TCP Dup ACK 16573#24] 80 &gt; 41945 [ACK] Seq=4916594 Ack=305 Win=6912 Len=0 TSV=1978476835 TSER=24815
  16640 16:03:26.131636 122.11.56.106         10.201.228.43         TCP      [TCP Dup ACK 16573#25] 80 &gt; 41945 [ACK] Seq=4916594 Ack=305 Win=6912 Len=0 TSV=1978476839 TSER=24815
  16642 16:03:26.133131 122.11.56.106         10.201.228.43         TCP      [TCP Dup ACK 16573#26] 80 &gt; 41945 [ACK] Seq=4916594 Ack=305 Win=6912 Len=0 TSV=1978476843 TSER=24815
  16644 16:03:26.134016 122.11.56.106         10.201.228.43         TCP      [TCP Dup ACK 16573#27] 80 &gt; 41945 [ACK] Seq=4916594 Ack=305 Win=6912 Len=0 TSV=1978476845 TSER=24815
  16664 16:03:27.805159 10.201.228.43         122.11.56.106         TCP      41945 &gt; 80 [FIN, ACK] Seq=305 Ack=4916594 Win=224352 Len=0 TSV=25098 TSER=1978476845
  16666 16:03:31.175459 10.201.228.43         122.11.56.106         TCP      41945 &gt; 80 [FIN, ACK] Seq=305 Ack=4916594 Win=224352 Len=0 TSV=25435 TSER=1978476845
  16669 16:03:37.905470 10.201.228.43         122.11.56.106         TCP      41945 &gt; 80 [FIN, ACK] Seq=305 Ack=4916594 Win=224352 Len=0 TSV=26108 TSER=1978476845
  16671 16:03:51.385481 10.201.228.43         122.11.56.106         TCP      41945 &gt; 80 [FIN, ACK] Seq=305 Ack=4916594 Win=224352 Len=0 TSV=27456 TSER=1978476845
  16756 16:04:47.805531 10.201.228.43         122.11.56.106         TCP      41945 &gt; 80 [FIN, ACK] Seq=305 Ack=4916594 Win=224352 Len=0 TSV=30152 TSER=1978476845</code></pre><p>I don’t understand why we have so many ACK packets within such a short time, <strong>10.201.228.43</strong> is local address.</p></div><div id="question-tags" class="tags-container tags">tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '11, 23:31</strong></p><img src="https://secure.gravatar.com/avatar/6535877de270eac71c394ebbe2c5dae5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Crs&#39;s gravatar image" /><p>Crs<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Crs has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Nov '11, 23:37</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-7594" class="comments-container"></div><div id="comment-tools-7594" class="comment-tools"></div><div class="clear"></div><div id="comment-7594-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7639"></span>

<div id="answer-container-7639" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7639-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>All the duplicate ACK's that you receive mean that the server did not get one (or more) packets in the stream, but it does receive later packet. For each packet it receives, it will send an ACK asking for the missing packet.</p><p>It is your TCP/IP stack that should retransmit the missing data, either by waiting for the retransmit timer to go off or by detecting a couple of the duplicate ACK's (by which time the sender can assume a packet was really lost instead of just received in a different time order). The exact behavior depends on specific implementation of the IP stack of the sending system.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '11, 14:47</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-7639" class="comments-container"><span id="7671"></span><div id="comment-7671" class="comment"><div id="post-7671-score" class="comment-score"></div><div class="comment-text"><p>I understand what duplicate ACK means, but from the tcpdump, 10.201.228.43 was receiving data from the server and acknowledge data it received, it was not transmitting any data, so the server should not have transmitted so many ACK packets, if the server had not received ACK packets, it should have retransmitted the last segment, but not so many ACK's. Anyway, thanks for your reply.</p></div><div id="comment-7671-info" class="comment-info"><span class="comment-age">(28 Nov '11, 05:04)</span> Crs</div></div></div><div id="comment-tools-7639" class="comment-tools"></div><div class="clear"></div><div id="comment-7639-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

