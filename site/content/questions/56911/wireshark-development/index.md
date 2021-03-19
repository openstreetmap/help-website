+++
type = "question"
title = "Wireshark development"
description = '''I was wondering if it is possible to get the packet information in wireshark for tcp packets such as source ip, destination ip, and various other packet information and to be able to show this information in a new gui screen as I am making a TCP connection annalyser module. How would I go about show...'''
date = "2016-11-01T11:13:00Z"
lastmod = "2016-11-01T12:52:00Z"
weight = 56911
keywords = [ "development", "guide", "tcp", "wireshark" ]
aliases = [ "/questions/56911" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark development](/questions/56911/wireshark-development)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56911-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was wondering if it is possible to get the packet information in wireshark for tcp packets such as source ip, destination ip, and various other packet information and to be able to show this information in a new gui screen as I am making a TCP connection annalyser module.</p><p>How would I go about showing these two pieces of information as i'm having trouble finding out from the code?</p><p>Any help would be much appreciated.</p></div><div id="question-tags" class="tags-container tags">development guide tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Nov '16, 11:13</strong></p><img src="https://secure.gravatar.com/avatar/3b7eb282c454b776eac0e960a3798043?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ModuleMan&#39;s gravatar image" /><p>ModuleMan<br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ModuleMan has no accepted answers">0%</span></p></div></div><div id="comments-container-56911" class="comments-container"></div><div id="comment-tools-56911" class="comment-tools"></div><div class="clear"></div><div id="comment-56911-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="56912"></span>

<div id="answer-container-56912" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56912-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The Statistics -&gt; Conversations dialog shows a lot of info for TCP connections (and Ethernet, IP and UDP as well). The info for this dialog is produced from taps and code in epan\conversation_table.c</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '16, 12:29</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-56912" class="comments-container"></div><div id="comment-tools-56912" class="comment-tools"></div><div class="clear"></div><div id="comment-56912-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="56915"></span>

<div id="answer-container-56915" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56915-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You may want to look at the tshark manual page, where you'll find various filter and output options, which could be used as your data source. If you want to have a JSON stream, you may want to look at the development version.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '16, 12:52</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-56915" class="comments-container"></div><div id="comment-tools-56915" class="comment-tools"></div><div class="clear"></div><div id="comment-56915-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

