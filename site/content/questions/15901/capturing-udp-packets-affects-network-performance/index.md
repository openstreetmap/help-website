+++
type = "question"
title = "Capturing UDP packets affects network performance"
description = '''is it possible that Wireshark is slowing down my network application, when im sniffing udp packets?'''
date = "2012-11-14T06:06:00Z"
lastmod = "2012-11-14T06:11:00Z"
weight = 15901
keywords = [ "down", "udp", "slow", "slowdown" ]
aliases = [ "/questions/15901" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing UDP packets affects network performance](/questions/15901/capturing-udp-packets-affects-network-performance)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15901-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>is it possible that Wireshark is slowing down my network application, when im sniffing udp packets?</p></div><div id="question-tags" class="tags-container tags">down udp slow slowdown</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '12, 06:06</strong></p><img src="https://secure.gravatar.com/avatar/49065fcf0be61cc80827f3898f23f4a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alexg&#39;s gravatar image" /><p>alexg<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alexg has no accepted answers">0%</span></p></div></div><div id="comments-container-15901" class="comments-container"><span id="15903"></span><div id="comment-15903" class="comment"><div id="post-15903-score" class="comment-score"></div><div class="comment-text"><p>is Wireshark running on the same system as your "network application"? If so, the system resources that wireshark needs (CPU, RAM, disk) will be unavailable for your "network application" and then it might affect the performance of that application.</p></div><div id="comment-15903-info" class="comment-info"><span class="comment-age">(14 Nov '12, 07:05)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-15901" class="comment-tools"></div><div class="clear"></div><div id="comment-15901-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15902"></span>

<div id="answer-container-15902" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15902-score" class="post-score" title="current number of votes">5</div></div></td><td><div class="item-right"><div class="answer-body"><p>No. Wireshark is a passive network analysis tool, which means it does not interfere with the network at all - unless, of course, you use network name resolution, which leads to DNS reverse pointer queries. To avoid any traffic coming from the PC running Wireshark you can disable all protocol bindings on the network card you're capturing on. That way the PC cannot communicate anymore, but Wireshark can still record incoming packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '12, 06:11</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-15902" class="comments-container"></div><div id="comment-tools-15902" class="comment-tools"></div><div class="clear"></div><div id="comment-15902-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

