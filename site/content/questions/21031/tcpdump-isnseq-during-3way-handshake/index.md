+++
type = "question"
title = "TCPDump ISN/SEQ during 3way handshake"
description = '''Im trying to compare some seq numbers from a wireshark output with the same capture being read in by tcpdump. Quick question, in terms of the numbers (i.e S 181839597:181839597) within the inital 3 way handshake, what do this relate to. Also is anyone able to explain the difference in relative and a...'''
date = "2013-05-08T07:46:00Z"
lastmod = "2013-05-08T07:53:00Z"
weight = 21031
keywords = [ "sequence" ]
aliases = [ "/questions/21031" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCPDump ISN/SEQ during 3way handshake](/questions/21031/tcpdump-isnseq-during-3way-handshake)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21031-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Im trying to compare some seq numbers from a wireshark output with the same capture being read in by tcpdump. Quick question, in terms of the numbers (i.e S 181839597:181839597) within the inital 3 way handshake, what do this relate to. Also is anyone able to explain the difference in relative and absoulte seq numbers and how they are difference in wireshark compared to tcpdump, as the seq number I obtained from wireshark Im unable to find when issuing a tcpdump -r &lt;cap.file&gt;</p><pre><code>[[email protected] tmp]# tcpdump -ni any port 8000
tcpdump: WARNING: Promiscuous mode not supported on the &quot;any&quot; device
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on any, link-type LINUX_SLL (Linux cooked), capture size 96 bytes
15:40:41.055988 IP 80.1.1.1.30119 &gt; 10.1.1.1.irdmi: S 181839597:181839597(0) win 8192 &lt;mss 1380,nop,wscale 8,nop,nop,sackOK,nop,nop,nop,nop,nop,nop,nop,nop,nop,nop,nop,nop,nop,nop,nop,nop,nop,nop,eol&gt;
15:40:41.064798 IP 10.1.1.1.irdmi &gt; 80.1.1.1.30119: S 3969924799:3969924799(0) ack 181839598 win 5840 &lt;mss 1460,nop,nop,sackOK,nop,wscale 4&gt;
15:40:41.066814 IP 80.1.1.1.30119 &gt; 10.1.1.1.irdmi: . ack 1 win 260</code></pre><p>Update : Also the seq numbers then throughout the rest of the capture appear to be relative.</p><pre><code>15:40:41.363895 IP 80.1.1.1.30123 &gt; 10.1.1.1.irdmi: S 2325112793:2325112793(0) win 8192 &lt;mss 1380,nop,wscale 8,nop,nop,sackOK,nop,nop,nop,nop,nop,nop,nop,nop,nop,nop,nop,nop,nop,nop,nop,nop,nop,nop,eol&gt;
15:40:41.363955 IP 10.1.1.1.irdmi &gt; 80.1.1.1.30123: S 592517166:592517166(0) ack 2325112794 win 5840 &lt;mss 1460,nop,nop,sackOK,nop,wscale 4&gt;
15:40:41.375282 IP 80.1.1.1.30123 &gt; 10.1.1.1.irdmi: . ack 1 win 260
15:40:41.375471 IP 80.1.1.1.30123 &gt; 10.1.1.1.irdmi: P 1:823(822) ack 1 win 260
15:40:41.375485 IP 10.1.1.1.irdmi &gt; 80.1.1.1.30123: . ack 823 win 468
15:40:41.440757 IP 10.1.1.1.irdmi &gt; 80.1.1.1.30123: P 1:18(17) ack 823 win 468
15:40:41.441019 IP 10.1.1.1.irdmi &gt; 80.1.1.1.30123: . 18:1398(1380) ack 823 win 468
15:40:41.441403 IP 10.1.1.1.irdmi &gt; 80.1.1.1.30123: . 1398:2778(1380) ack 823 win 468
15:40:41.441411 IP 10.1.1.1.irdmi &gt; 80.1.1.1.30123: FP 2778:4124(1346) ack 823 win 468
15:40:41.443848 IP 80.1.1.1.30123 &gt; 10.1.1.1.irdmi: . ack 1398 win 260
15:40:41.445975 IP 80.1.1.1.30123 &gt; 10.1.1.1.irdmi: . ack 4125 win 260
15:40:41.484158 IP 80.1.1.1.30123 &gt; 10.1.1.1.irdmi: F 823:823(0) ack 4125 win 260
15:40:41.484195 IP 10.1.1.1.irdmi &gt; 80.1.1.1.30123: . ack 824 win 468</code></pre><p>Thanks,</p></div><div id="question-tags" class="tags-container tags">sequence</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 May '13, 07:46</strong></p><img src="https://secure.gravatar.com/avatar/22baebd906c29ccfcb5b2aeb350b22fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bart80&#39;s gravatar image" /><p>bart80<br />
<span class="score" title="11 reputation points">11</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bart80 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 May '13, 08:00</p></div></div><div id="comments-container-21031" class="comments-container"><span id="35914"></span><div id="comment-35914" class="comment"><div id="post-35914-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>I'm curious about the number of (Nop)'s in a row on this output can some one explain to me is this normal? I thought there should be no more than 4 in a row?</p></div><div id="comment-35914-info" class="comment-info"><span class="comment-age">(01 Sep '14, 09:36)</span> Ciag</div></div></div><div id="comment-tools-21031" class="comment-tools"></div><div class="clear"></div><div id="comment-21031-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21032"></span>

<div id="answer-container-21032" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21032-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In your output, 181839597 is the absolute sequence number (the actual value of the seq field in the TCP header).</p><p>In wireshark, sequence numbers are by default relative (which means, the seq of the initial SYN packet is set to 0 and all other sequence numbers are calculated from there).</p><p>To be able to compare the sequence numbers, you can make wireshark show the absolute sequence numbers by going to the TCP protocol preferences and disable "Relative Sequence Numbers"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '13, 07:53</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-21032" class="comments-container"><span id="21035"></span><div id="comment-21035" class="comment"><div id="post-21035-score" class="comment-score"></div><div class="comment-text"><p>Question updated....</p></div><div id="comment-21035-info" class="comment-info"><span class="comment-age">(08 May '13, 08:23)</span> bart80</div></div></div><div id="comment-tools-21032" class="comment-tools"></div><div class="clear"></div><div id="comment-21032-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

