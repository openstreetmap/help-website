+++
type = "question"
title = "Which NIC do I capture on?"
description = '''Hello, I would like to analyze my network using Wireshark. The problem I have one internet connection, but two networks which run from the one connection. This means that on my admin computer, I have two NICs. One for each network. My question is, say I wanted to monitor internet protocols, how coul...'''
date = "2012-04-25T06:22:00Z"
lastmod = "2012-04-25T06:28:00Z"
weight = 10433
keywords = [ "nic" ]
aliases = [ "/questions/10433" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Which NIC do I capture on?](/questions/10433/which-nic-do-i-capture-on)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10433-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I would like to analyze my network using Wireshark. The problem I have one internet connection, but two networks which run from the one connection. This means that on my admin computer, I have two NICs. One for each network.</p><p>My question is, say I wanted to monitor internet protocols, how could I work out which NIC my computer is using to get a route outside to the internet. Would I need to check the routing table?</p><p>Both NICs have a connection to the internet and they both point to DNS servers on their own network. If I was to unplug one connection, the internet will continue to run on the other NIC and vice versa.</p><p>Any help would be great.</p></div><div id="question-tags" class="tags-container tags">nic</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Apr '12, 06:22</strong></p><img src="https://secure.gravatar.com/avatar/fa3b0bb1e872b69f465332e68b8c9735?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="computer_guy&#39;s gravatar image" /><p>computer_guy<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="computer_guy has no accepted answers">0%</span></p></div></div><div id="comments-container-10433" class="comments-container"></div><div id="comment-tools-10433" class="comment-tools"></div><div class="clear"></div><div id="comment-10433-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10434"></span>

<div id="answer-container-10434" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10434-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, you're not saying which OS you're using, but if you're multihomed with two or more adapters that both have a default gateway that points to the internet the OS decides which card is preferred. So depending on your OS you could try look it up somewhere, but why not go for a short trial &amp; error?</p><p>Capture on each interface, one after the other, and do something on the internet. If Wireshark shows packets coming in and going out, you've got the interface that has preference. If you see traffic on both, well, you're even wiser, because that means you'll have to capture both to get it all.</p><p>By the way, the current development version 1.7.x can capture on multiple NICs at the same time, so it might be worth trying it. But be aware that packets might get into the capture in the wrong order (happens to me all the time).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '12, 06:28</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-10434" class="comments-container"><span id="10471"></span><div id="comment-10471" class="comment"><div id="post-10471-score" class="comment-score"></div><div class="comment-text"><p>Hi, Thanks for your detailed Answer. I had no idea about 1.7.x and you are right, it does do multiple NICs which is perfect.</p><p>I have found one way of working out which adapter the OS is using... When selecting capture interfaces on Wireshark, it shows a preview screen which shows the NICs and live packet transfers. Whichever NIC has the most transfer must be the one the OS is using!</p><p>Thanks again for your useful post.</p></div><div id="comment-10471-info" class="comment-info"><span class="comment-age">(27 Apr '12, 01:54)</span> computer_guy</div></div></div><div id="comment-tools-10434" class="comment-tools"></div><div class="clear"></div><div id="comment-10434-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

