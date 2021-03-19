+++
type = "question"
title = "RST sequence number and window size"
description = '''RFC793 states the following about RST processing: &quot;In all states except SYN-SENT, all reset (RST) segments are validated by checking their SEQ-fields. A reset is valid if its sequence number is in the window.&quot; But I&#x27;m not sure what does this statement means exactly. Let&#x27;s say I have the following sc...'''
date = "2016-03-23T20:38:00Z"
lastmod = "2016-03-24T10:39:00Z"
weight = 51139
keywords = [ "tcpip", "tcp", "wireshark" ]
aliases = [ "/questions/51139" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [RST sequence number and window size](/questions/51139/rst-sequence-number-and-window-size)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51139-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>RFC793 states the following about RST processing: "<em>In all states except SYN-SENT, all reset (RST) segments are validated by checking their SEQ-fields. A reset is valid if its sequence number is in the window.</em>"</p><p>But I'm not sure what does this statement means exactly. Let's say I have the following scenario:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/1_q0digCg.png" alt="alt text" /></p><p>So socket 2 tells socket 1 that its window size is 6 KB, and then socket 1 sends 6 KB worth of data to socket 2.</p><p>And then socket 1 decides to close the connection ungracefully, so it sends an RST packet to socket 2:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/2_6ExgbYk.png" alt="alt text" /></p><p>What will happen in this case, will this RST packet be accepted by socket 2 (will it be considered a valid packet)? If yes then why will it be accepted, I mean isn't this RST packet considered to be outside the window (since the window has already been filled by the 6 KB)?</p></div><div id="question-tags" class="tags-container tags">tcpip tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Mar '16, 20:38</strong></p><img src="https://secure.gravatar.com/avatar/633b94b5d3fe24751e56eb3cd795abe3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="john_9163&#39;s gravatar image" /><p>john_9163<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="john_9163 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-51139" class="comments-container"></div><div id="comment-tools-51139" class="comment-tools"></div><div class="clear"></div><div id="comment-51139-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51158"></span>

<div id="answer-container-51158" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51158-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That depends on timings and the TCP stack of the receiver. Some or all of your 6KB worth of data could have just been processed (pulled from the Window by the application) on socket 2 in the time the RST travels, so there's space again when the RST arrives - which would mean there's no problem.</p><p>If the RST arrives while the window is still full it's possible that the RST gets dropped, but in the end it's the stack that decides what to do. It may accept it nonetheless - you'd have to look at each individual TCP stack to check what it'll do.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Mar '16, 10:39</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></img></div></div><div id="comments-container-51158" class="comments-container"></div><div id="comment-tools-51158" class="comment-tools"></div><div class="clear"></div><div id="comment-51158-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

