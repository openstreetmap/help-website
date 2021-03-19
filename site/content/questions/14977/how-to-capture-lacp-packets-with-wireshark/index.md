+++
type = "question"
title = "How to capture LACP packets with wireshark"
description = '''I am using Wireshark ver 1.8.3 but unable to capture LACP packets. Can you please tell me step by step procedure to capture LACP using Wireshark'''
date = "2012-10-12T21:46:00Z"
lastmod = "2012-10-13T12:11:00Z"
weight = 14977
keywords = [ "lacp" ]
aliases = [ "/questions/14977" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture LACP packets with wireshark](/questions/14977/how-to-capture-lacp-packets-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14977-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I am using Wireshark ver 1.8.3 but unable to capture LACP packets. Can you please tell me step by step procedure to capture LACP using Wireshark</p></div><div id="question-tags" class="tags-container tags">lacp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Oct '12, 21:46</strong></p><img src="https://secure.gravatar.com/avatar/3967c8c05fe3d82ad32e057cbb8bff59?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chirantan&#39;s gravatar image" /><p>chirantan<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chirantan has no accepted answers">0%</span></p></div></div><div id="comments-container-14977" class="comments-container"></div><div id="comment-tools-14977" class="comment-tools"></div><div class="clear"></div><div id="comment-14977-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="14980"></span>

<div id="answer-container-14980" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14980-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What is your system and your NIC driver? LACP is done at the driver level. So maybe, you don't see those packets, because the driver strips those packets before they arrive at wireshark.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '12, 01:28</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-14980" class="comments-container"></div><div id="comment-tools-14980" class="comment-tools"></div><div class="clear"></div><div id="comment-14980-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14990"></span>

<div id="answer-container-14990" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14990-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I've done a few test captures (a year back or so) to see how LACP worked, and used copper 1GBit TAPs to do that - I can't remember exactly if I used Wireshark for the actual capturing process; it may have been one of our big Network General S6000 devices.</p><p>Using a SPAN port instead of a TAP can be problematic because you do not know if the switch will mirror the packets correctly, and maybe (as Kurt said) your NIC will not accept them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '12, 12:11</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Oct '12, 12:12</p></div></div><div id="comments-container-14990" class="comments-container"><span id="14997"></span><div id="comment-14997" class="comment"><div id="post-14997-score" class="comment-score"></div><div class="comment-text"><p>Please provide the step by step procedure to make setting of Wireshark in order to capture LACP packets,</p><p>If any perticular filter setting is required then kindly let me know.</p></div><div id="comment-14997-info" class="comment-info"><span class="comment-age">(14 Oct '12, 00:54)</span> chirantan</div></div><span id="15001"></span><div id="comment-15001" class="comment"><div id="post-15001-score" class="comment-score"></div><div class="comment-text"><p>I can try to setup a test connection this week and give you more details, but it will take a while.</p></div><div id="comment-15001-info" class="comment-info"><span class="comment-age">(14 Oct '12, 13:29)</span> Jasper ♦♦</div></div></div><div id="comment-tools-14990" class="comment-tools"></div><div class="clear"></div><div id="comment-14990-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

