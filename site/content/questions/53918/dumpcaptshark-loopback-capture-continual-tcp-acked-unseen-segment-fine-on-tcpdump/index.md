+++
type = "question"
title = "dumpcap/tshark loopback capture continual TCP ACKed unseen segment, fine on tcpdump"
description = '''I&#x27;m bumped into a weird bug on a virtualized RHEL/Centos 7.2 where if you capture on the loopback interface with tshark or dumpcap, that I get continual &quot;TCP ACKed unseen segment&quot; errors. But it works fine with tcpdump In this scenario, I have HAProxy doing SSL termination and then proxying to tomca...'''
date = "2016-07-07T16:43:00Z"
lastmod = "2017-08-01T17:50:00Z"
weight = 53918
keywords = [ "tcpdump", "unseen_segment", "tshark", "dumpcap" ]
aliases = [ "/questions/53918" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [dumpcap/tshark loopback capture continual TCP ACKed unseen segment, fine on tcpdump](/questions/53918/dumpcaptshark-loopback-capture-continual-tcp-acked-unseen-segment-fine-on-tcpdump)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53918-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm bumped into a weird bug on a virtualized RHEL/Centos 7.2 where if you capture on the loopback interface with tshark or dumpcap, that I get continual "TCP ACKed unseen segment" errors. But it works fine with tcpdump</p><p>In this scenario, I have HAProxy doing SSL termination and then proxying to tomcat running on 8080.</p><p>For example:</p><pre><code>$tshark -i lo -f &#39;tcp port 8080&#39;
Capturing on &#39;Loopback&#39;
  7 3.492486804    127.0.0.1 -&gt; 127.0.0.1    HTTP 436 [TCP ACKed unseen segment] HTTP/1.1 200 OK  (text/html)
  8 3.492498208    127.0.0.1 -&gt; 127.0.0.1    TCP 66 [TCP Previous segment not captured] 41497 &gt; http-alt [ACK] Seq=95 Ack=371 Win=44800 Len=0 TSval=701453508 TSecr=701453508
  9 3.492541125    127.0.0.1 -&gt; 127.0.0.1    HTTP 68 Continuation or non-HTTP traffic
 10 5.007425117    127.0.0.1 -&gt; 127.0.0.1    TCP 74 41499 &gt; http-alt [SYN] Seq=0 Win=43690 Len=0 MSS=65495 SACK_PERM=1 TSval=701455023 TSecr=0 WS=128
 11 1544792488.772437180    127.0.0.1 -&gt; 127.0.0.1    TCP 74 http-alt &gt; 41499 [SYN, ACK] Seq=0 Ack=1 Win=43690 Len=0 MSS=65495 SACK_PERM=1 TSval=701455023 TSecr=701455023 WS=128
 12 5.007450399    127.0.0.1 -&gt; 127.0.0.1    TCP 66 41499 &gt; http-alt [ACK] Seq=1 Ack=1 Win=43776 Len=0 TSval=701455023 TSecr=701455023
 13 5.007968787    127.0.0.1 -&gt; 127.0.0.1    HTTP 436 [TCP ACKed unseen segment] HTTP/1.1 200 OK  (text/html)
 14 5.007980410    127.0.0.1 -&gt; 127.0.0.1    TCP 66 [TCP Previous segment not captured] 41499 &gt; http-alt [ACK] Seq=95 Ack=371 Win=44800 Len=0 TSval=701455023 TSecr=701455023
 15 5.008025474    127.0.0.1 -&gt; 127.0.0.1    HTTP 68 Continuation or non-HTTP traffic
 16 8.422922387    127.0.0.1 -&gt; 127.0.0.1    TCP 74 41504 &gt; http-alt [SYN] Seq=0 Win=43690 Len=0 MSS=65495 SACK_PERM=1 TSval=701458438 TSecr=0 WS=128
 17 1544807156.089171770    127.0.0.1 -&gt; 127.0.0.1    TCP 74 http-alt &gt; 41504 [SYN, ACK] Seq=0 Ack=1 Win=43690 Len=0 MSS=65495 SACK_PERM=1 TSval=701458438 TSecr=701458438 WS=128
 18 8.422947104    127.0.0.1 -&gt; 127.0.0.1    TCP 66 41504 &gt; http-alt [ACK] Seq=1 Ack=1 Win=43776 Len=0 TSval=701458438 TSecr=701458438
 19 8.423516653    127.0.0.1 -&gt; 127.0.0.1    HTTP 436 [TCP ACKed unseen segment] HTTP/1.1 200 OK  (text/html)
 20 8.423526522    127.0.0.1 -&gt; 127.0.0.1    TCP 66 [TCP Previous segment not captured] 41504 &gt; http-alt [ACK] Seq=95 Ack=371 Win=44800 Len=0 TSval=701458439 TSecr=701458439
 21 8.423632416    127.0.0.1 -&gt; 127.0.0.1    HTTP 68 Continuation or non-HTTP traffic
 22 8.423633078    127.0.0.1 -&gt; 127.0.0.1    TCP 66 [TCP ACKed unseen segment] http-alt &gt; 41504 [FIN, ACK] Seq=371 Ack=95 Win=43776 Len=0 TSval=701458439 TSecr=701458439
 23 8.423657361    127.0.0.1 -&gt; 127.0.0.1    TCP 54 http-alt &gt; 41504 [RST] Seq=371 Win=0 Len=0</code></pre><p>However if I specify <em>any</em> snaplen (including 65535), then it works properly:</p><pre><code>$tshark -s 1500 -i lo -f &#39;tcp port 8080&#39;
Capturing on &#39;Loopback&#39;
  1 0.000000000    127.0.0.1 -&gt; 127.0.0.1    TCP 74 41926 &gt; http-alt [SYN] Seq=0 Win=43690 Len=0 MSS=65495 SACK_PERM=1 TSval=701753517 TSecr=0 WS=128
  2 1546074207.537697209    127.0.0.1 -&gt; 127.0.0.1    TCP 74 http-alt &gt; 41926 [SYN, ACK] Seq=0 Ack=1 Win=43690 Len=0 MSS=65495 SACK_PERM=1 TSval=701753517 TSecr=701753517 WS=128
  3 0.000023710    127.0.0.1 -&gt; 127.0.0.1    TCP 66 41926 &gt; http-alt [ACK] Seq=1 Ack=1 Win=43776 Len=0 TSval=701753517 TSecr=701753517
  4 0.000039374    127.0.0.1 -&gt; 127.0.0.1    HTTP 160 GET /opensso/isAlive.jsp HTTP/1.0
  5 0.000050069    127.0.0.1 -&gt; 127.0.0.1    TCP 66 http-alt &gt; 41926 [ACK] Seq=1 Ack=95 Win=43776 Len=0 TSval=701753517 TSecr=701753517
  6 0.000595231    127.0.0.1 -&gt; 127.0.0.1    HTTP 436 HTTP/1.1 200 OK  (text/html)
  7 0.000617025    127.0.0.1 -&gt; 127.0.0.1    TCP 66 41926 &gt; http-alt [ACK] Seq=95 Ack=371 Win=44800 Len=0 TSval=701753517 TSecr=701753517
  8 0.000733316    127.0.0.1 -&gt; 127.0.0.1    HTTP 68 Continuation or non-HTTP traffic
  9 0.000748411    127.0.0.1 -&gt; 127.0.0.1    TCP 66 http-alt &gt; 41926 [FIN, ACK] Seq=371 Ack=95 Win=43776 Len=0 TSval=701753518 TSecr=701753517
 10 0.000770966    127.0.0.1 -&gt; 127.0.0.1    TCP 54 http-alt &gt; 41926 [RST] Seq=371 Win=0 Len=0
 11 0.000777847    127.0.0.1 -&gt; 127.0.0.1    TCP 66 41926 &gt; http-alt [ACK] Seq=97 Ack=372 Win=44800 Len=0 TSval=701753518 TSecr=701753518
 12 0.000784413    127.0.0.1 -&gt; 127.0.0.1    TCP 66 41926 &gt; http-alt [FIN, ACK] Seq=97 Ack=372 Win=44800 Len=0 TSval=701753518 TSecr=701753518
 13 0.000784484    127.0.0.1 -&gt; 127.0.0.1    TCP 54 http-alt &gt; 41926 [RST] Seq=372 Win=0 Len=0
 14 0.000794534    127.0.0.1 -&gt; 127.0.0.1    TCP 54 http-alt &gt; 41926 [RST] Seq=372 Win=0 Len=0
 15 1.412536403    127.0.0.1 -&gt; 127.0.0.1    TCP 74 41928 &gt; http-alt [SYN] Seq=0 Win=43690 Len=0 MSS=65495 SACK_PERM=1 TSval=701754929 TSecr=0 WS=128
 16 1546080272.032933044    127.0.0.1 -&gt; 127.0.0.1    TCP 74 http-alt &gt; 41928 [SYN, ACK] Seq=0 Ack=1 Win=43690 Len=0 MSS=65495 SACK_PERM=1 TSval=701754929 TSecr=701754929 WS=128
 17 1.412560984    127.0.0.1 -&gt; 127.0.0.1    TCP 66 41928 &gt; http-alt [ACK] Seq=1 Ack=1 Win=43776 Len=0 TSval=701754929 TSecr=701754929
 18 1.412577999    127.0.0.1 -&gt; 127.0.0.1    HTTP 160 GET /opensso/isAlive.jsp HTTP/1.0</code></pre><p>This is strange because the help text says that the default snaplan is "65535", however it's clear from my testing that <code>-s</code> has additional side effects.</p><pre><code>$tshark --help
tshark: invalid option -- &#39;-&#39;
TShark 1.10.14 (Git Rev Unknown from unknown)
...
Capture interface:
  -i &lt;interface&gt;           name or idx of interface (def: first non-loopback)
  -f &lt;capture filter&gt;      packet filter in libpcap filter syntax
  -s &lt;snaplen&gt;             packet snapshot length (def: 65535)</code></pre><p>I raised a ticket with RedHat support and they have also confirmed with a virtualized RHEL 7.2 this issue is reproduceable, but it is fine on bare-metal.</p><p>I have tried this with Ubuntu 16.04 on AWS and it's fine there, so it only seems to affect RHEL/Centos.</p><p>I thought tcpdump and dumpcap/tshark used the same underlying capture library, libpcap?</p><p>Any ideas what's up with this?</p></div><div id="question-tags" class="tags-container tags">tcpdump unseen_segment tshark dumpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jul '16, 16:43</strong></p><img src="https://secure.gravatar.com/avatar/400af70f37e9e9b8a4b536cb03a63838?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joel%20Pearson&#39;s gravatar image" /><p>Joel Pearson<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joel Pearson has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jul '16, 05:33</p></div></div><div id="comments-container-53918" class="comments-container"></div><div id="comment-tools-53918" class="comment-tools"></div><div class="clear"></div><div id="comment-53918-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="63315"></span>

<div id="answer-container-63315" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63315-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Turns out it was an issue with the default capture buffer in RHEL 7, RedHat finally released a fix for it:</p><p><a href="https://git.centos.org/commitdiff/rpms!wireshark.git/60db69006fe48d5744fdfa2a1b982dc552b5fd1b">https://git.centos.org/commitdiff/rpms!wireshark.git/60db69006fe48d5744fdfa2a1b982dc552b5fd1b</a></p><p>It seems that the actual default snaplen is 262144, which would explain why it was running out of buffer too quickly and why changing it to 65536 helped.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '17, 17:50</strong></p><img src="https://secure.gravatar.com/avatar/400af70f37e9e9b8a4b536cb03a63838?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joel%20Pearson&#39;s gravatar image" /><p>Joel Pearson<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joel Pearson has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Aug '17, 17:52</p></div></div><div id="comments-container-63315" class="comments-container"></div><div id="comment-tools-63315" class="comment-tools"></div><div class="clear"></div><div id="comment-63315-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53929"></span>

<div id="answer-container-53929" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53929-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is not an issue of tshark, it's a side effect. TCPdump doesn't track TCP sequence numbers (meaning, it has no "TCP expert") like tshark does, so it won't complain about "TCP ACKed unseen segment". It has nothing to do with libpcap, but with the analyzing layers on top of it.</p><p>"ACKed unknown segment" means that the TCP expert has seen an acknowledge for a packet that it hasn't seen. This is usually a capture performance problem, meaning that your hardware can't capture the packets fast enough (for various possible reasons). Reducing the snaplength helps in this case of course, because you're writing less bytes to disk, allowing the capture to grab more frames in the same timespan.</p><p>If you need maximum capture performance, use dumpcap instead of tshark. See <a href="https://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/">this blog post</a> for more details why dumpcap is the better choice, and how to run it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '16, 04:23</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-53929" class="comments-container"><span id="53931"></span><div id="comment-53931" class="comment"><div id="post-53931-score" class="comment-score"></div><div class="comment-text"><p>I don't believe this is the problem. This happens at any capture rate even at 1 packer per second. Any value of snaplen fixes the problem. Even "-s 65535" fixes the problem.</p></div><div id="comment-53931-info" class="comment-info"><span class="comment-age">(08 Jul '16, 04:47)</span> Joel Pearson</div></div><span id="53933"></span><div id="comment-53933" class="comment"><div id="post-53933-score" class="comment-score"></div><div class="comment-text"><p>Okay, then it's probably related to the loopback capture I guess...</p></div><div id="comment-53933-info" class="comment-info"><span class="comment-age">(08 Jul '16, 05:37)</span> Jasper ♦♦</div></div><span id="53934"></span><div id="comment-53934" class="comment"><div id="post-53934-score" class="comment-score"></div><div class="comment-text"><p>Capturing on eth0 has no problems either. It's just loopback, it's just so odd that actually specifying a snaplen has different behaviour. I suppose RedHat will figure it out.</p></div><div id="comment-53934-info" class="comment-info"><span class="comment-age">(08 Jul '16, 06:30)</span> Joel Pearson</div></div></div><div id="comment-tools-53929" class="comment-tools"></div><div class="clear"></div><div id="comment-53929-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

