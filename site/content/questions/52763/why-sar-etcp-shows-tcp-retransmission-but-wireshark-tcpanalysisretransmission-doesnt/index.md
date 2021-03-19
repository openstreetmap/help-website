+++
type = "question"
title = "Why sar ETCP shows TCP retransmission but wireshark tcp.analysis.retransmission doesn&#x27;t"
description = '''I am trying to investigate the cause of TCP retransmission. When I use sadc and sar, it shows that there are tcp retransmissions, but when I use wireshark on all of the server&#x27;s interfaces, it doesn&#x27;t show any retransmissions and quits after 2 minutes with write to disk full. But sar shows that with...'''
date = "2016-05-19T05:32:00Z"
lastmod = "2016-07-19T08:45:00Z"
weight = 52763
keywords = [ "tcp_retransmission" ]
aliases = [ "/questions/52763" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why sar ETCP shows TCP retransmission but wireshark tcp.analysis.retransmission doesn't](/questions/52763/why-sar-etcp-shows-tcp-retransmission-but-wireshark-tcpanalysisretransmission-doesnt)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52763-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to investigate the cause of TCP retransmission. When I use <a href="http://linux.die.net/man/8/sadc"><code>sadc</code></a> and <a href="http://linux.die.net/man/1/sar"><code>sar</code></a>, it shows that there are tcp retransmissions, but when I use wireshark on all of the server's interfaces, it doesn't show any retransmissions and quits after 2 minutes with write to disk full. But <code>sar</code> shows that within the first minute, there are retransmissions.</p><p>sar shows retransmission</p><pre><code>[[email protected] ~]# /usr/lib64/sa/sadc -S INT -S DISK -S XDISK -S SNMP -S IPV6 1 50 /tmp/sadc_stats.log

[[email protected] ~]# sar -f /tmp/sadc_stats.log -n ETCP
09:25:55 AM atmptf/s estres/s retrans/s isegerr/s orsts/s
Average: 2.07 0.04 1.38 0.00 2.71</code></pre><p>wireshark doesn't show retransmission</p><pre><code>tshark -i xsi1 -R tcp.analysis.retransmission</code></pre><p>I tried all other interfaces in addition to xsi1.</p><p>Another thing is that I am using both of these commands within a VM on the host server.</p><p>Thank you!</p><p>Desong</p></div><div id="question-tags" class="tags-container tags">tcp_retransmission</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '16, 05:32</strong></p><img src="https://secure.gravatar.com/avatar/eb434238f7445e2a3826289832f98195?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="desongyu&#39;s gravatar image" /><p>desongyu<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="desongyu has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Jul '16, 08:48</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-52763" class="comments-container"></div><div id="comment-tools-52763" class="comment-tools"></div><div class="clear"></div><div id="comment-52763-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54159"></span>

<div id="answer-container-54159" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54159-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I've never used <a href="http://linux.die.net/man/8/sadc"><code>sadc</code></a> or <a href="http://linux.die.net/man/1/sar"><code>sar</code></a>, so I'm not sure what to make of the output, but as for <code>tshark</code> ... what version of wireshark are you using? It must be fairly old; otherwise you would see a message such as follows when attempting to run it the way you are:</p><pre><code>tshark: -R without -2 is deprecated. For single-pass filtering use -Y.</code></pre><p>And if you attempted to use <code>-2R</code>, you would see:</p><pre><code>tshark: Live captures do not support two-pass analysis.</code></pre><p>I would suggest updating Wireshark, if possible and then retest, although you may be better off post-analyzing the data after saving the traffic to a capture file using the "<code>-w file.pcapng</code>" option.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '16, 08:45</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-54159" class="comments-container"><span id="54162"></span><div id="comment-54162" class="comment"><div id="post-54162-score" class="comment-score"></div><div class="comment-text"><p>Also consider using dumpcap rather than tshark to make the capturing process even lighter on resource usage.</p></div><div id="comment-54162-info" class="comment-info"><span class="comment-age">(19 Jul '16, 09:08)</span> grahamb ♦</div></div></div><div id="comment-tools-54159" class="comment-tools"></div><div class="clear"></div><div id="comment-54159-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

