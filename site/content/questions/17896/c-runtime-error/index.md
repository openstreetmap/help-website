+++
type = "question"
title = "C++ Runtime error"
description = '''I have installed wireshark on 2 computers, One is W-7 Pro sp-1 32 bit and the other is Windows XP Pro sp-3 32 bit. After a few minutes of capture, I receive an error message &quot;This application has requested the Runtime to terminate it in an unusual way. Please contact the application&#x27;s support team f...'''
date = "2013-01-23T07:02:00Z"
lastmod = "2013-01-23T07:13:00Z"
weight = 17896
keywords = [ "c++" ]
aliases = [ "/questions/17896" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [C++ Runtime error](/questions/17896/c-runtime-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17896-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have installed wireshark on 2 computers, One is W-7 Pro sp-1 32 bit and the other is Windows XP Pro sp-3 32 bit. After a few minutes of capture, I receive an error message "This application has requested the Runtime to terminate it in an unusual way. Please contact the application's support team fro more information." I have setup wireshark to capture the local interface, use multiple files next every 1 megabyte and to stop the capture after 10 hours. I am saving the files to an external hard drive connected via USB.</p><p>I have seen that others are also having the error and that the work around is to use dumpcap. That doesn't really solve the issue.</p><p>I have tried using v 1.8.4 and 1.6.12 and get the same results.</p><p>It appears that wireshark is using increasingly more and more memory as it captures the data.</p><p>Is there a solution to the problem?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">c++</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jan '13, 07:02</strong></p><img src="https://secure.gravatar.com/avatar/052caed975f81cc277db457e2c2ae6be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bmerryusa&#39;s gravatar image" /><p>bmerryusa<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bmerryusa has no accepted answers">0%</span></p></div></div><div id="comments-container-17896" class="comments-container"></div><div id="comment-tools-17896" class="comment-tools"></div><div class="clear"></div><div id="comment-17896-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17897"></span>

<div id="answer-container-17897" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17897-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, use dumpcap. Wireshark (and to a lesser extent tshark) retain state even when using multiple files, and this will build up over time and cause the program to run out of memory.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jan '13, 07:13</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-17897" class="comments-container"><span id="17940"></span><div id="comment-17940" class="comment"><div id="post-17940-score" class="comment-score"></div><div class="comment-text"><p>I switched back to 1.6.5 and the memory loss is much slower allowing me time to get the captures I need. Is there a way to keep Wireshark from retaining state? This seems to be a severe limitation. When I have a bit of time, I will see if I can get dumpcap to do the job.</p><p>Thanks</p></div><div id="comment-17940-info" class="comment-info"><span class="comment-age">(24 Jan '13, 12:14)</span> bmerryusa</div></div><span id="17942"></span><div id="comment-17942" class="comment"><div id="post-17942-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately Wireshark needs to build up state info to be able to offer such things as conversation tracking.</p><p>Wireshark itself uses dumpcap to capture traffic, so you won't be losing any features by using it.</p></div><div id="comment-17942-info" class="comment-info"><span class="comment-age">(24 Jan '13, 13:20)</span> grahamb ♦</div></div></div><div id="comment-tools-17897" class="comment-tools"></div><div class="clear"></div><div id="comment-17897-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

