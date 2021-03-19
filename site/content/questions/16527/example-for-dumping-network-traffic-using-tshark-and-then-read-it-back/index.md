+++
type = "question"
title = "Example for dumping network traffic using  tshark and then read it back"
description = '''Hello, I am new to use tshark. I want to dump the network traffic and then read the dumped file. Is there is some link or some sample examples through which i may get help. warm regards, monz'''
date = "2012-12-04T02:31:00Z"
lastmod = "2012-12-04T02:49:00Z"
weight = 16527
keywords = [ "tshark", "wireshark" ]
aliases = [ "/questions/16527" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Example for dumping network traffic using tshark and then read it back](/questions/16527/example-for-dumping-network-traffic-using-tshark-and-then-read-it-back)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16527-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am new to use tshark. I want to dump the network traffic and then read the dumped file. Is there is some link or some sample examples through which i may get help. warm regards, monz</p></div><div id="question-tags" class="tags-container tags">tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Dec '12, 02:31</strong></p><img src="https://secure.gravatar.com/avatar/86a2938611b19f95680b86803b74e494?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="monz&#39;s gravatar image" /><p>monz<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="monz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Dec '12, 13:51</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-16527" class="comments-container"><span id="16556"></span><div id="comment-16556" class="comment"><div id="post-16556-score" class="comment-score"></div><div class="comment-text"><p>"Dump" in what format? The raw binary capture-file format (in which case you might want to use <code>dumpcap</code>), or the dissected output format that TShark produces, showing the packet details?</p></div><div id="comment-16556-info" class="comment-info"><span class="comment-age">(04 Dec '12, 13:52)</span> Guy Harris ♦♦</div></div><span id="16669"></span><div id="comment-16669" class="comment"><div id="post-16669-score" class="comment-score"></div><div class="comment-text"><p>dump in readable format so that it is easy for me to read it and sent it back after filling it on my structures</p></div><div id="comment-16669-info" class="comment-info"><span class="comment-age">(06 Dec '12, 21:27)</span> monz</div></div><span id="16671"></span><div id="comment-16671" class="comment"><div id="post-16671-score" class="comment-score"></div><div class="comment-text"><p>"[Send] it back" where? Retransmit it on the network or have tcpdump/Wireshark/Tshark read it? Or something else?</p></div><div id="comment-16671-info" class="comment-info"><span class="comment-age">(07 Dec '12, 00:19)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-16527" class="comment-tools"></div><div class="clear"></div><div id="comment-16527-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16528"></span>

<div id="answer-container-16528" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16528-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Try Google. You should find plenty of examples.</p><p>Some examples are in this <a href="http://www.cafewebmaster.com/packet-sniffing-and-monitoring-tshark-wireshark">link</a>.</p><p>Also, you can find the manual <a href="http://manpages.ubuntu.com/manpages/intrepid/man1/tshark.1.html">here</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Dec '12, 02:49</strong></p><img src="https://secure.gravatar.com/avatar/46196bc495ce51058590c4e4ae334d22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SidR&#39;s gravatar image" /><p>SidR<br />
<span class="score" title="245 reputation points">245</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SidR has 3 accepted answers">30%</span></p></div></div><div id="comments-container-16528" class="comments-container"></div><div id="comment-tools-16528" class="comment-tools"></div><div class="clear"></div><div id="comment-16528-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

