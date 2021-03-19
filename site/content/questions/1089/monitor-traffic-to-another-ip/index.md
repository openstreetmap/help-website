+++
type = "question"
title = "Monitor traffic to another IP"
description = '''I need a tool to log Ethernet based Modbus TCP transactions to/from a specific IP address different than the PC running Wireshark. Can I do this with Wireshark and can you point me to someone that can push me off in the right direction after I&#x27;ve downloaded Wireshark?'''
date = "2010-11-23T14:43:00Z"
lastmod = "2010-11-23T18:53:00Z"
weight = 1089
keywords = [ "modbus", "ethernet", "traffic", "log" ]
aliases = [ "/questions/1089" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Monitor traffic to another IP](/questions/1089/monitor-traffic-to-another-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1089-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need a tool to log Ethernet based Modbus TCP transactions to/from a specific IP address different than the PC running Wireshark. Can I do this with Wireshark and can you point me to someone that can push me off in the right direction after I've downloaded Wireshark?</p></div><div id="question-tags" class="tags-container tags">modbus ethernet traffic log</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Nov '10, 14:43</strong></p><img src="https://secure.gravatar.com/avatar/c4d7700d7c6e1e8c634dc6f74dd02825?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chuckh&#39;s gravatar image" /><p>chuckh<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chuckh has no accepted answers">0%</span></p></div></div><div id="comments-container-1089" class="comments-container"></div><div id="comment-tools-1089" class="comment-tools"></div><div class="clear"></div><div id="comment-1089-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1100"></span>

<div id="answer-container-1100" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1100-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>First step - capture some traffic - ya gotta be in the path somewhere to capture it. Then... look at it - does Wireshark dissect it (there is a Modbus dissector - mbtcp I think).</p><p>Here's a nifty doc showing a group who used Wireshark to analyze malicious Modbus/TCP traffic.</p><p>http://critis08.dia.uniroma3.it/pdf/CRITIS_08_26.pdf</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '10, 18:53</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p>lchappell ♦<br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-1100" class="comments-container"></div><div id="comment-tools-1100" class="comment-tools"></div><div class="clear"></div><div id="comment-1100-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1094"></span>

<div id="answer-container-1094" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1094-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm no expert, but I'll give it a shot. I think you need a network adapter that supports promiscuous mode. If you have that capability, I think you should be able to accomplish what you want. You can download WinPCap for free if your driver doesn't have promiscuous mode.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Nov '10, 16:56</strong></p><img src="https://secure.gravatar.com/avatar/3b8a4f21d2910124c8a2e4a70a46c186?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ActualRandy&#39;s gravatar image" /><p>ActualRandy<br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ActualRandy has no accepted answers">0%</span></p></div></div><div id="comments-container-1094" class="comments-container"></div><div id="comment-tools-1094" class="comment-tools"></div><div class="clear"></div><div id="comment-1094-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

