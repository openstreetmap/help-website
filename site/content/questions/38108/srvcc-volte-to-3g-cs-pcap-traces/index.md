+++
type = "question"
title = "SRVCC VoLTE to 3G CS pcap traces"
description = '''Hello, I am looking for SRVCC PS to CS Cancel (and Ack) messages example (gtpv2) in order to understand how this packet is built. Can I find these Wireshark traces&amp;gt; BR, Diana'''
date = "2014-11-24T09:25:00Z"
lastmod = "2014-11-25T21:24:00Z"
weight = 38108
keywords = [ "lte" ]
aliases = [ "/questions/38108" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SRVCC VoLTE to 3G CS pcap traces](/questions/38108/srvcc-volte-to-3g-cs-pcap-traces)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38108-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am looking for SRVCC PS to CS Cancel (and Ack) messages example (gtpv2) in order to understand how this packet is built.</p><p>Can I find these Wireshark traces&gt;</p><p>BR, Diana</p></div><div id="question-tags" class="tags-container tags">lte</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '14, 09:25</strong></p><img src="https://secure.gravatar.com/avatar/900044aef60dc6223168781e5d576bfb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dianalab9&#39;s gravatar image" /><p>Dianalab9<br />
<span class="score" title="26 reputation points">26</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dianalab9 has no accepted answers">0%</span></p></div></div><div id="comments-container-38108" class="comments-container"></div><div id="comment-tools-38108" class="comment-tools"></div><div class="clear"></div><div id="comment-38108-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38150"></span>

<div id="answer-container-38150" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38150-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I can't get it to you as a pcap, but I could probably answer field questions if you have specific things you're not sure on. That's the best I can do. :/</p><p>Also see section 5.2.6 and 5.2.7 of TS 29.280 for the IE breakdown of those two messages. There's really not a lot to it. <a href="http://www.etsi.org/deliver/etsi_ts/129200_129299/129280/12.02.00_60/ts_129280v120200p.pdf">http://www.etsi.org/deliver/etsi_ts/129200_129299/129280/12.02.00_60/ts_129280v120200p.pdf</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '14, 21:24</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Nov '14, 21:25</p></div></div><div id="comments-container-38150" class="comments-container"><span id="38154"></span><div id="comment-38154" class="comment"><div id="post-38154-score" class="comment-score"></div><div class="comment-text"><p>Hi, yes, I do have a specific question:</p><p>It is stated in the standard 29.280 that: "The TEID field in the SRVCC CS to PS Cancel Notification message header shall be set to "0" if the message is sent before reception of the acceptance response to the SRVCC CS to PS Request" From the possible IEs in Cancel Notification message, it doesn't include any address for Control (for the other direction) so what I don't understand is on which TEID-C the Cancel Acknowledge message will ride.</p><p>Do you have an explanation on this?</p></div><div id="comment-38154-info" class="comment-info"><span class="comment-age">(25 Nov '14, 23:51)</span> Dianalab9</div></div><span id="38190"></span><div id="comment-38190" class="comment"><div id="post-38190-score" class="comment-score"></div><div class="comment-text"><p>The request and response messages are tied together by the GTP sequence numbers. Because one UE can have only one control TEID pair on an Sv interface (mandatory, section 5.2.1), and because the cancel message contains the UE's permanent identifier (IMSI or, for emergency scenario, IMEI), there's no need for the acknowledgement to specify any control TEID for both sides to cleanly map the exchange to a given subscriber and handover attempt.</p><p>One thing to keep in mind here is that Sv is indirectly governed by TS 29.274. Fields inherent to GTPv2c apply here as well (such as request/response sequence numbers).</p></div><div id="comment-38190-info" class="comment-info"><span class="comment-age">(26 Nov '14, 15:54)</span> Quadratic</div></div></div><div id="comment-tools-38150" class="comment-tools"></div><div class="clear"></div><div id="comment-38150-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

