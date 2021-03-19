+++
type = "question"
title = "Can I block response for request using WireShark"
description = '''Please help. How can I simulate the &quot;time out&quot; error for my request. Can I block response for request using WireShark (CoAP protocol) If it posible - please advise how can I do it'''
date = "2016-04-13T01:04:00Z"
lastmod = "2016-04-13T20:17:00Z"
weight = 51621
keywords = [ "request", "response", "block", "for" ]
aliases = [ "/questions/51621" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can I block response for request using WireShark](/questions/51621/can-i-block-response-for-request-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51621-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Please help. How can I simulate the "time out" error for my request. Can I block response for request using WireShark (CoAP protocol) If it posible - please advise how can I do it</p></div><div id="question-tags" class="tags-container tags">request response block for</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Apr '16, 01:04</strong></p><img src="https://secure.gravatar.com/avatar/6692d195da01f0362d9ea84958afefec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AMitiev&#39;s gravatar image" /><p>AMitiev<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AMitiev has no accepted answers">0%</span></p></div></div><div id="comments-container-51621" class="comments-container"></div><div id="comment-tools-51621" class="comment-tools"></div><div class="clear"></div><div id="comment-51621-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="51622"></span>

<div id="answer-container-51622" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51622-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>No. Wireshark is a monitoring tool and does not affect the data flows (except indirectly due to changing interface settings which is useless for your case).</p><p>I would recommend to use netfilter (iptables) for the purpose - if it cannot be used on the client or server machine directly, use a linux box as an intermediate router and implement the "network spoiler" there.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Apr '16, 01:26</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-51622" class="comments-container"></div><div id="comment-tools-51622" class="comment-tools"></div><div class="clear"></div><div id="comment-51622-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="51656"></span>

<div id="answer-container-51656" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51656-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi @AMitiev,</p><p>If you are using Windows, you can use Npcap to implement a firewall. It supports the PASS, DROP and MODIFY operation. You need to parse the packet contents by yourself to determine how to handle the packet.</p><p>See the description on the release of Npcap 0.05 R11 for usage:</p><p><a href="https://github.com/nmap/npcap/releases/tag/v0.05-r11">https://github.com/nmap/npcap/releases/tag/v0.05-r11</a></p><p>You can use the latest normal (non -wifi, the latest is 0.05 R14) version Npcap at:</p><p><a href="https://github.com/nmap/npcap/releases">https://github.com/nmap/npcap/releases</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Apr '16, 20:17</strong></p><img src="https://secure.gravatar.com/avatar/0f8ec58f46e4af3a67f768675c20aac8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yang%20Luo&#39;s gravatar image" /><p>Yang Luo<br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yang Luo has one accepted answer">4%</span></p></div></div><div id="comments-container-51656" class="comments-container"></div><div id="comment-tools-51656" class="comment-tools"></div><div class="clear"></div><div id="comment-51656-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

