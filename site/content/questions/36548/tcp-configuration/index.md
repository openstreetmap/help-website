+++
type = "question"
title = "TCP Configuration"
description = '''I am currently in the process of troubleshooting a file transfer between the sender (which in this case is a z/OS main frame) and a receiver server across a WAN. The RTT between sender and server is 72ms. In reviewing the captures and traces I am seeing A LOT of DUP ACKs and FAST Retransmits. I am o...'''
date = "2014-09-23T17:13:00Z"
lastmod = "2014-09-25T23:19:00Z"
weight = 36548
keywords = [ "tcpconfiguration" ]
aliases = [ "/questions/36548" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Configuration](/questions/36548/tcp-configuration)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36548-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am currently in the process of troubleshooting a file transfer between the sender (which in this case is a z/OS main frame) and a receiver server across a WAN. The RTT between sender and server is 72ms. In reviewing the captures and traces I am seeing A LOT of DUP ACKs and FAST Retransmits. I am of the believe that the main frame is not optimized for WAN transfers as between the DUP ACKs and the reply FAST Retransmits are occurring in less than 0.0003 seconds. So my question is: Is it possible to configure a server to make it look like there is a network problem? I am thinking that there is a queuing or timeout setting that is being overlooked.</p><p>I truly don't feel a main frame is not the right choice for a WAN transfer. As they are meant for data center transactions (IMO).</p></div><div id="question-tags" class="tags-container tags">tcpconfiguration</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Sep '14, 17:13</strong></p><img src="https://secure.gravatar.com/avatar/5b20990cd21bd091665e684410ebe9fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdJ&#39;s gravatar image" /><p>EdJ<br />
<span class="score" title="16 reputation points">16</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdJ has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Sep '14, 06:07</p></div></div><div id="comments-container-36548" class="comments-container"><span id="36549"></span><div id="comment-36549" class="comment"><div id="post-36549-score" class="comment-score"></div><div class="comment-text"><p>For an anonymizer, download tracewrangler from www.tracewrangler.com.</p></div><div id="comment-36549-info" class="comment-info"><span class="comment-age">(23 Sep '14, 18:19)</span> Jim Aragon</div></div><span id="36573"></span><div id="comment-36573" class="comment"><div id="post-36573-score" class="comment-score"></div><div class="comment-text"><p>To answer your question; very probably.</p><p>But maybe to help further:</p><p>What is the bandwidth of the smallest link between the sites? What throughput are you getting? What throughput were you expecting? If you produce an IO stat graph, do you see a constant level of load? Which file transfer mechanism is being used?</p><p>Best regards...Paul</p></div><div id="comment-36573-info" class="comment-info"><span class="comment-age">(24 Sep '14, 14:59)</span> PaulOfford</div></div><span id="36590"></span><div id="comment-36590" class="comment"><div id="post-36590-score" class="comment-score"></div><div class="comment-text"><blockquote><p>www.tracewrangler.com</p></blockquote><p>Tracewranger... Cool.</p></div><div id="comment-36590-info" class="comment-info"><span class="comment-age">(25 Sep '14, 05:32)</span> smp</div></div></div><div id="comment-tools-36548" class="comment-tools"></div><div class="clear"></div><div id="comment-36548-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36621"></span>

<div id="answer-container-36621" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36621-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><pre><code>&quot;file transfer between the sender z/OS mainframe and a receiver server across a WAN (RTT 72ms)&quot;  
&quot; A LOT of DUP ACKs and FAST Retransmits. &quot;
&quot;mainframe is not optimized for WAN transfers...   
between the DUP ACKs and the reply FAST Retransmits are occurring in less than 0.0003 seconds.&quot;</code></pre><p>A lot of DUPACKs are an indication that packets arrive out of order at the receiver. When the TCP stack receives the 3rd dupack it retransmits the missing segment withhout a delay, so the 300µs is why it is called a 'Fast' Retransmit' and this is happening on purpose.<br />
</p><pre><code>&quot; So my question is: Is it possible to configure a server to make it look like there is a network problem? &quot;</code></pre><p>Not sure I understand the question. You want to make the zOS believe that there is a network problem and refrain from 'Fast Retransmitting' missing packets? If so, contact IBM support, they might have something in their back pocket ;-) Not sure if you really would want this though...</p><p>"I am thinking that there is a queuing or timeout setting that is being overlooked."</p><p>There is an old APAR PQ82943 (2004) that is fixing a similar problem but I assume you are at a current z/OS release so that fix should be implemented in your TCP stack already. As for Out-of-Order arrival, it is often due to a <a href="http://en.wikipedia.org/wiki/Equal-cost_multi-path_routing">multipath-per-packet</a> configuration somewhere along the path. This could start within z/OS sending packets out via different OSA cards. To avoid this make sure that you have MULTIPATH PERConnection in your <a href="http://pic.dhe.ibm.com/infocenter/zos/v1r13/index.jsp?topic=%2Fcom.ibm.zos.r13.halz001%2Fipconf.htm">IPCONFIG</a> statement.</p><p>" I truly <strong>don't</strong> feel a main frame is <strong>not</strong> the right choice for a WAN transfer.<br />
As they are meant for data center transactions (IMO)."</p><p>So if you feel that the mainframe <strong>IS</strong> the right choice I agree with you. They (mainframes) are meant for all types of workloads, including long latency connections.</p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '14, 23:19</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-36621" class="comments-container"></div><div id="comment-tools-36621" class="comment-tools"></div><div class="clear"></div><div id="comment-36621-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

