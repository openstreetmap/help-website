+++
type = "question"
title = "unicast frame not seen by Wireshark"
description = '''In which condition Wireshark does not see 64 - 127 byte unicast frames? I have a specific converter connected to PC and according to egress interface counters of this converter, it sends 64 - 127 byte unicast frames towards the PC, but Wireshark running in PC does not see those frames. I am aware th...'''
date = "2013-10-10T06:00:00Z"
lastmod = "2013-10-10T06:06:00Z"
weight = 25873
keywords = [ "unicast" ]
aliases = [ "/questions/25873" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [unicast frame not seen by Wireshark](/questions/25873/unicast-frame-not-seen-by-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25873-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In which condition Wireshark does not see 64 - 127 byte unicast frames? I have a specific converter connected to PC and according to egress interface counters of this converter, it sends 64 - 127 byte unicast frames towards the PC, but Wireshark running in PC does not see those frames. I am aware that those packets are malformed. Is it possible that certain NIC's drop unicast frames targeted to some other destination MAC address other than the one they have? In which condition PC running Wireshark does not see unicast frames?</p></div><div id="question-tags" class="tags-container tags">unicast</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Oct '13, 06:00</strong></p><img src="https://secure.gravatar.com/avatar/c153148e19e1e7c04c48a2a5c4f68b54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrtn&#39;s gravatar image" /><p>mrtn<br />
<span class="score" title="11 reputation points">11</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrtn has no accepted answers">0%</span></p></div></div><div id="comments-container-25873" class="comments-container"></div><div id="comment-tools-25873" class="comment-tools"></div><div class="clear"></div><div id="comment-25873-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25874"></span>

<div id="answer-container-25874" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25874-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If the packets are malformed it probably means that the checksums are incorrect as well, so it is quite possible that the NIC/NIC driver decides to drop the frame and never tells Wireshark about it. I assume you do you captures in promiscuous mode, which should lead to the NIC accepting MACs other than its own. Still, broken checksums could lead to the frame being dropped.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Oct '13, 06:06</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-25874" class="comments-container"></div><div id="comment-tools-25874" class="comment-tools"></div><div class="clear"></div><div id="comment-25874-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

