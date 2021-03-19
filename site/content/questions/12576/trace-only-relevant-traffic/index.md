+++
type = "question"
title = "Trace only relevant traffic"
description = '''Hi, I am absolutely new to Wireshark but I am asked to trace the complete traffic between to machines (IP addresses are known, but nothing else). How can I do this? thx a lot'''
date = "2012-07-10T16:30:00Z"
lastmod = "2012-07-10T19:53:00Z"
weight = 12576
keywords = [ "filter", "trace" ]
aliases = [ "/questions/12576" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Trace only relevant traffic](/questions/12576/trace-only-relevant-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12576-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am absolutely new to Wireshark but I am asked to trace the complete traffic between to machines (IP addresses are known, but nothing else). How can I do this?</p><p>thx a lot</p></div><div id="question-tags" class="tags-container tags">filter trace</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '12, 16:30</strong></p><img src="https://secure.gravatar.com/avatar/95d95cffc639de5af2c564ab02a01c5c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="palustris&#39;s gravatar image" /><p>palustris<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="palustris has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Jul '12, 19:53</p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span></p></div></div><div id="comments-container-12576" class="comments-container"></div><div id="comment-tools-12576" class="comment-tools"></div><div class="clear"></div><div id="comment-12576-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12586"></span>

<div id="answer-container-12586" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12586-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>First you have to position Wireshark where it can capture the traffic between the two machines. You can install Wireshark on one of the two machines, or you can connect your Wireshark computer to a switch that the traffic passes through and use port mirroring.</p><p>To limit the captured traffic to only the IP traffic between the two machines, enter this capture filter: "host <em>ip-address-1</em> and host <em>ip-address-2</em>" For example, "host 192.168.1.1 and host 192.168.1.25"</p><p>Or you can capture all the traffic and then use this display filter to show only the traffic between the two machines: "ip.addr==192.168.1.1 &amp;&amp; ip.addr==192.168.1.25"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '12, 19:53</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-12586" class="comments-container"><span id="12602"></span><div id="comment-12602" class="comment"><div id="post-12602-score" class="comment-score"></div><div class="comment-text"><p>thank you for your answer. I have a long time capture of the complete traffic. When using the display filter, is it possible to save a new file from it that only content the filtered traffic?</p></div><div id="comment-12602-info" class="comment-info"><span class="comment-age">(11 Jul '12, 03:55)</span> palustris</div></div><span id="12615"></span><div id="comment-12615" class="comment"><div id="post-12615-score" class="comment-score"></div><div class="comment-text"><p>Yes, you can save the filtered packets by selecting:</p><ul><li>File -&gt; Save As... (Wireshark version &lt; 1.8.0)</li><li>File -&gt; Export Specified Packets... (Wireshark version 1.8.0 and higher)</li></ul></div><div id="comment-12615-info" class="comment-info"><span class="comment-age">(11 Jul '12, 04:54)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-12586" class="comment-tools"></div><div class="clear"></div><div id="comment-12586-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

