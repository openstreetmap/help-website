+++
type = "question"
title = "Filtering out TCP connection termination packets"
description = '''Hello I want to filter out the tcp connection closing i.e. the FIN and the respective ACK packets. In the case of FIN packets it is an easy task based on flags, but the ACK is tricky, as I want to keep the other ACK packets. One way that I can think of is by comparing the sequence number of this ACK...'''
date = "2016-09-30T04:21:00Z"
lastmod = "2016-09-30T04:39:00Z"
weight = 56002
keywords = [ "fin+ack", "tcp" ]
aliases = [ "/questions/56002" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Filtering out TCP connection termination packets](/questions/56002/filtering-out-tcp-connection-termination-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56002-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello I want to filter out the tcp connection closing i.e. the FIN and the respective ACK packets. In the case of FIN packets it is an easy task based on flags, but the ACK is tricky, as I want to keep the other ACK packets. One way that I can think of is by comparing the sequence number of this ACK packet to the acknowledgement number of the previous FIN packet, but I cannot get myself to come up with an expression for this case. How can this be achieved? Any other ways are also welcome.</p></div><div id="question-tags" class="tags-container tags">fin+ack tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Sep '16, 04:21</strong></p><img src="https://secure.gravatar.com/avatar/038ef8fec62f3268cb4a0981f613de71?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pooja&#39;s gravatar image" /><p>pooja<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pooja has no accepted answers">0%</span></p></div></div><div id="comments-container-56002" class="comments-container"></div><div id="comment-tools-56002" class="comment-tools"></div><div class="clear"></div><div id="comment-56002-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56005"></span>

<div id="answer-container-56005" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56005-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe <a href="https://wiki.wireshark.org/Mate">MATE</a> can be of help here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '16, 04:39</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-56005" class="comments-container"><span id="56008"></span><div id="comment-56008" class="comment"><div id="post-56008-score" class="comment-score"></div><div class="comment-text"><p>Also see the discussion on <a href="https://ask.wireshark.org/questions/55897/fin-ack-initiated-by-the-server">this</a> very similar question about why display filters can't be used to check values across more than one packet.</p></div><div id="comment-56008-info" class="comment-info"><span class="comment-age">(30 Sep '16, 05:10)</span> grahamb ♦</div></div><span id="56018"></span><div id="comment-56018" class="comment"><div id="post-56018-score" class="comment-score"></div><div class="comment-text"><p>I'm afraid that MATE won't help here, at least alone:</p><ul><li><p>MATE does not handle arithmetic, so exact matching of the <code>tcp.seq</code> of the packet bearing the FIN flag and the ˙tcp.ack` of the packet bearing the ACK to it is impossible as these two values differ by one.</p></li><li><p>as no data packet follows the one with FIN, the TCP dissector does not generate the <code>tcp.nxtseq</code> field which normally matches the <code>tcp.ack</code> of the acknowledging packet (if such exists)</p></li></ul><p>So to make the task "MATEable", you would have to first use a Lua post-dissector to add a metafield carrying the <code>tcp.seq + 1</code> value. It is then questionable whether it is not easier to use the Lua post-dissector to implement the complete task, the following way:</p><ul><li><p>build a table of <code>tcp.seq</code> values of all FIN packets in the capture, indexed by <code>tcp.stream</code> and direction (<code>tcp.srcport</code> of the packet carrying the FIN flag)</p></li><li><p>compare the ack numbers of all TCP packets in the capture to this table, and add a metafield like <code>tcp.analysis.ack_to_fin</code> to packets whose <code>tcp.ack</code> value would be higher than the stored <code>tcp.seq</code> of FIN packets for the same <code>tcp.stream</code> and <code>tcp.dstport</code> (opposite direction).</p></li></ul><p>The display filter showing all the FIN packets and their matching ACK ones would then be <code>tcp.flags.fin == 1 or tcp.analysis.ack_to_fin</code>.</p></div><div id="comment-56018-info" class="comment-info"><span class="comment-age">(30 Sep '16, 07:14)</span> sindy</div></div><span id="56043"></span><div id="comment-56043" class="comment"><div id="post-56043-score" class="comment-score">1</div><div class="comment-text"><p>OK, so using MATE you can generate metafields allowing you to display only the first FIN packet of each TCP session and all the packets following it (which may be more packets than just the one carrying the ACK to the FIN, but usually not too many). Is that enough for you?</p></div><div id="comment-56043-info" class="comment-info"><span class="comment-age">(01 Oct '16, 07:37)</span> sindy</div></div><span id="56129"></span><div id="comment-56129" class="comment"><div id="post-56129-score" class="comment-score"></div><div class="comment-text"><p>Hey, that helps a lot. Yes that would be enough for my application. I am getting to know MATE now, no clue about it, so will post if I succeed in it. Thank you.</p></div><div id="comment-56129-info" class="comment-info"><span class="comment-age">(04 Oct '16, 05:03)</span> pooja</div></div><span id="56130"></span><div id="comment-56130" class="comment"><div id="post-56130-score" class="comment-score">1</div><div class="comment-text"><p>what you'd do would be to</p><pre><code>Extract fin From tcp.flags.fin;
Extract stream From tcp.stream;</code></pre><p>into a <code>tcp</code> Pdu, and then <code>Start</code> on <code>(fin = 1)</code> a GoP of <code>tcp</code> which would use <code>stream</code> as its key.</p><p>Unfortunately, GoP's <code>Expiration</code> seems not to work, so you'll get everything after the first FIN as GoP members.</p><p>Hm, it seems writing a howto took almost more keypresses than writing the complete MATE configuration would :-)</p></div><div id="comment-56130-info" class="comment-info"><span class="comment-age">(04 Oct '16, 05:29)</span> sindy</div></div></div><div id="comment-tools-56005" class="comment-tools"></div><div class="clear"></div><div id="comment-56005-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

