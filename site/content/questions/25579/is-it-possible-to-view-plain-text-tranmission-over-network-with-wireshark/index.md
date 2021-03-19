+++
type = "question"
title = "Is it possible to view plain text tranmission over network with wireshark?"
description = '''Few chat engines, say IRC and Pidgin doesn&#x27;t encrypt the package when they send. Is it possible to capture those non encrypted plain text information using wireshark and view those informations?'''
date = "2013-10-03T00:24:00Z"
lastmod = "2013-10-03T02:20:00Z"
weight = 25579
keywords = [ "plain-text" ]
aliases = [ "/questions/25579" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Is it possible to view plain text tranmission over network with wireshark?](/questions/25579/is-it-possible-to-view-plain-text-tranmission-over-network-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25579-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Few chat engines, say IRC and Pidgin doesn't encrypt the package when they send. Is it possible to capture those non encrypted plain text information using wireshark and view those informations?</p></div><div id="question-tags" class="tags-container tags">plain-text</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Oct '13, 00:24</strong></p><img src="https://secure.gravatar.com/avatar/b41802fe7f333c0b2b2b68be7da4f757?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Karthick&#39;s gravatar image" /><p>Karthick<br />
<span class="score" title="21 reputation points">21</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Karthick has no accepted answers">0%</span></p></div></div><div id="comments-container-25579" class="comments-container"></div><div id="comment-tools-25579" class="comment-tools"></div><div class="clear"></div><div id="comment-25579-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25580"></span>

<div id="answer-container-25580" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25580-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark will (hopefully) capture whatever traffic passes through the capturing interfaces. If the application sends in plain text then it will be visible in the capture, however if there is no dissector for the protocols being used then it will just appear as "data".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Oct '13, 02:20</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-25580" class="comments-container"><span id="25619"></span><div id="comment-25619" class="comment"><div id="post-25619-score" class="comment-score"></div><div class="comment-text"><p>Can you just tell me what filter do I have to use for seeing Plain Text Chats (I.E IRC etc)?</p></div><div id="comment-25619-info" class="comment-info"><span class="comment-age">(03 Oct '13, 23:18)</span> Karthick</div></div><span id="25623"></span><div id="comment-25623" class="comment"><div id="post-25623-score" class="comment-score"></div><div class="comment-text"><p>There is not "one" filter to do that, as there are different protocols used for different chat systems. You will need to find out which chat protocols are used and can then filter on the tcp (or udp) ports used by the protocol.</p><p>For IRC you can use the (capture) filter "tcp port 6667" for instance...</p></div><div id="comment-25623-info" class="comment-info"><span class="comment-age">(04 Oct '13, 00:18)</span> SYN-bit ♦♦</div></div><span id="25674"></span><div id="comment-25674" class="comment"><div id="post-25674-score" class="comment-score"></div><div class="comment-text"><p>Hi I am going to present a session about wireshark. Can anybody tell me what and all can be shown live to the users. Like tracing plain texts using wireshark etc etc..</p></div><div id="comment-25674-info" class="comment-info"><span class="comment-age">(06 Oct '13, 07:45)</span> Karthick</div></div><span id="25677"></span><div id="comment-25677" class="comment"><div id="post-25677-score" class="comment-score"></div><div class="comment-text"><p>Make some captures and have a look, non-tls email to a pop server (port 110) is usually good with passwords in plain text.</p></div><div id="comment-25677-info" class="comment-info"><span class="comment-age">(06 Oct '13, 11:03)</span> grahamb ♦</div></div><span id="25685"></span><div id="comment-25685" class="comment"><div id="post-25685-score" class="comment-score"></div><div class="comment-text"><p>Is it possible to divert all traffic to http instead of https using sslstripe or anything that can do this? I just want to have this setup to show a demo for education purpose.</p></div><div id="comment-25685-info" class="comment-info"><span class="comment-age">(06 Oct '13, 17:36)</span> Karthick</div></div></div><div id="comment-tools-25580" class="comment-tools"></div><div class="clear"></div><div id="comment-25580-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

