+++
type = "question"
title = "how can i get congestion window from traces"
description = '''i have wireshark trace of uploading a file and i want to know congestion window at different times how can i know this??'''
date = "2013-12-02T01:07:00Z"
lastmod = "2013-12-03T10:18:00Z"
weight = 27648
keywords = [ "network", "tcp" ]
aliases = [ "/questions/27648" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how can i get congestion window from traces](/questions/27648/how-can-i-get-congestion-window-from-traces)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27648-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i have wireshark trace of uploading a file and i want to know congestion window at different times how can i know this??</p></div><div id="question-tags" class="tags-container tags">network tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '13, 01:07</strong></p><img src="https://secure.gravatar.com/avatar/62879cb2c5f61b4906febc715a1ac9b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sync2013&#39;s gravatar image" /><p>sync2013<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sync2013 has no accepted answers">0%</span></p></div></div><div id="comments-container-27648" class="comments-container"></div><div id="comment-tools-27648" class="comment-tools"></div><div class="clear"></div><div id="comment-27648-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="27657"></span>

<div id="answer-container-27657" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27657-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you mean CWND by 'congestion window' as defined in <a href="http://tools.ietf.org/html/rfc2581">RFC 2581</a>, the answer to your question is: <strong>You can't 'get' that value</strong> directly from the capture file, <strong>as it is not advertized</strong>.</p><pre><code>   CONGESTION WINDOW (cwnd):  A TCP state variable that limits the
      amount of data a TCP can send.  At any given time, a TCP MUST NOT
      send data with a sequence number higher than the sum of the
      highest acknowledged sequence number and the minimum of cwnd and
      rwnd.</code></pre><p>To be more specific:</p><p>The CWND is just an internal variable on the sender side to manage the amount of bytes that it is allowed to send at any time. The value of CWND is calculated according to a certain algorithm (see the RFC). Basically the value is increased for every 'good' ACK (in time, not duplicate) and decreased for a 'bad' ACK (timeout, DUP ACK). So, during a TCP connection the value of CWND is somewhere between a defined start value (depends on the algorithm) and the Receiver Window Size (RWND), as advertized by the receiver. In a capture file you can see the RWND (advertized value: <code>tcp.window_size_value</code>, with scaling factor: <code>tcp.window_size</code>) but <strong>not the CWND</strong>, as it is only calculated <strong>within</strong> the senders TCP implementation.</p><p><strong>However</strong>: You can <strong>'estimate' the CWND</strong> at any time during a TCP connection, if you know the senders congestion algorithm and the configuration values (amount of bytes for increase/decreas), by looking at the sent frames and the received ACKs. There is no such functionality in Wireshark, but with some scripting (tshark) it should be possible to calculate the CWND, at least as an estimation.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '13, 03:02</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Dec '13, 03:19</p></div></div><div id="comments-container-27657" class="comments-container"><span id="27669"></span><div id="comment-27669" class="comment"><div id="post-27669-score" class="comment-score"></div><div class="comment-text"><p>thanx i knew about this but i thought we can get estimate using sender side traces.</p></div><div id="comment-27669-info" class="comment-info"><span class="comment-age">(02 Dec '13, 12:51)</span> sync2013</div></div><span id="27670"></span><div id="comment-27670" class="comment"><div id="post-27670-score" class="comment-score"></div><div class="comment-text"><p>As I said, you <strong>can</strong> estimate the CWND, by doing the calculation yourself. What you need: a pretty good insight into the TCP implementation of the sender OS.</p><p>BTW: Why do you need that value? There is not much information you can gain from it...</p></div><div id="comment-27670-info" class="comment-info"><span class="comment-age">(02 Dec '13, 13:21)</span> Kurt Knochner ♦</div></div><span id="27671"></span><div id="comment-27671" class="comment"><div id="post-27671-score" class="comment-score"></div><div class="comment-text"><p>Hint: If you want to automate the CWND estimation, you could use tcptrace, which contains a module to estimate a CWND value, kind of....</p><blockquote><p><a href="http://www.tcptrace.org/manual/node10_ct.html">http://www.tcptrace.org/manual/node10_ct.html</a></p></blockquote></div><div id="comment-27671-info" class="comment-info"><span class="comment-age">(02 Dec '13, 13:25)</span> Kurt Knochner ♦</div></div><span id="27729"></span><div id="comment-27729" class="comment"><div id="post-27729-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your help. actually i was studying congestion control algorithms, mainly westwood and cubic and since both implement sender side congestion window modification for faster recovery so i thought congestion window is a good parameter to compare them.</p></div><div id="comment-27729-info" class="comment-info"><span class="comment-age">(03 Dec '13, 11:13)</span> sync2013</div></div><span id="27731"></span><div id="comment-27731" class="comment"><div id="post-27731-score" class="comment-score"></div><div class="comment-text"><p>you probably know this already, but if you google for 'comparison Westwood cubic' you'll find some papers that did the comparison based on the congestion window, by reading Linux kernel values. Maybe those papers will inspire your own studies...</p></div><div id="comment-27731-info" class="comment-info"><span class="comment-age">(03 Dec '13, 11:38)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-27657" class="comment-tools"></div><div class="clear"></div><div id="comment-27657-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="27725"></span>

<div id="answer-container-27725" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27725-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Having a trace at the sender I'm using the IO-Graph and draw the tcp.analysis.bytes_in_flight vs. the advertized tcp.window_size over the time. If the bytes in flight is well below the advertized, then this is dominated by the congestion window size (I assume...) <img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-18.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '13, 10:18</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div></div><div id="comments-container-27725" class="comments-container"><span id="27726"></span><div id="comment-27726" class="comment"><div id="post-27726-score" class="comment-score"></div><div class="comment-text"><blockquote><p>If the bytes in flight is well below the advertized, then this is dominated by the congestion window size (I assume...)</p></blockquote><p>not necessarily. bytes_in_flight are un-ACKed bytes for Wireshark. So, if bytes_in_flight is below the advertized window size, it can also mean that the receiver ACKed before the receive window was full.</p></div><div id="comment-27726-info" class="comment-info"><span class="comment-age">(03 Dec '13, 10:25)</span> Kurt Knochner ♦</div></div><span id="27730"></span><div id="comment-27730" class="comment"><div id="post-27730-score" class="comment-score"></div><div class="comment-text"><p>advertised tcp window size is basically receive window which is generally high. however time-sequence number graph can give a better idea about congestion and how fast is the recovery. it doesn't give you numerical values to perform calculations. anyways thanx</p></div><div id="comment-27730-info" class="comment-info"><span class="comment-age">(03 Dec '13, 11:21)</span> sync2013</div></div></div><div id="comment-tools-27725" class="comment-tools"></div><div class="clear"></div><div id="comment-27725-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

