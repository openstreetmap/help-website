+++
type = "question"
title = "Absolute time and time resolution in tshark I/O statistics"
description = '''Hey there, is there any way I can specify the tshark -r file.pcap -qz &quot;io,stat,1,AVG(tcp.analysis.ack_rtt)tcp.analysis.ack_rtt&quot; output, to   1. give me absolute time intervals and 2. give me more than milliseconds as a resolution for the AVG values? thx as always in advance'''
date = "2012-01-05T09:14:00Z"
lastmod = "2012-01-05T10:45:00Z"
weight = 8233
keywords = [ "statistics", "advanced", "tshark", "io" ]
aliases = [ "/questions/8233" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Absolute time and time resolution in tshark I/O statistics](/questions/8233/absolute-time-and-time-resolution-in-tshark-io-statistics)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8233-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey there,</p><p>is there any way I can specify the</p><p><code>tshark -r file.pcap -qz "io,stat,1,AVG(tcp.analysis.ack_rtt)tcp.analysis.ack_rtt"</code></p><p>output, to 1. give me absolute time intervals and 2. give me more than milliseconds as a resolution for the AVG values?</p><p>thx as always in advance</p></div><div id="question-tags" class="tags-container tags">statistics advanced tshark io</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jan '12, 09:14</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p>Landi<br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Jan '12, 19:22</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-8233" class="comments-container"></div><div id="comment-tools-8233" class="comment-tools"></div><div class="clear"></div><div id="comment-8233-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8235"></span>

<div id="answer-container-8235" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8235-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>(1) is not currently possible. <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=1850">Bug 1850</a> has been asking for that functionality since 2007. (It just needs someone to implement it.)</p><p>For (2) you can upgrade to 1.7.0 (or the SVN trunk) and io,stat will give you microseconds.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jan '12, 10:45</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-8235" class="comments-container"></div><div id="comment-tools-8235" class="comment-tools"></div><div class="clear"></div><div id="comment-8235-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

