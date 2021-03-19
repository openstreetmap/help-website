+++
type = "question"
title = "Using Wireshark to find out what&#x27;s causing slowness in streamiung youtube videos"
description = '''Hello Experts, I am streaming a youtube video on my system. Sometimes it plays very fast and sometimes it just becomes slow. I want to know how to use wireshark to find out where the problem is coming from. Whether its coming from network fluctuations from my ISP or wherever. Thank you.'''
date = "2013-09-24T22:36:00Z"
lastmod = "2013-09-25T02:25:00Z"
weight = 25187
keywords = [ "youtube" ]
aliases = [ "/questions/25187" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Using Wireshark to find out what's causing slowness in streamiung youtube videos](/questions/25187/using-wireshark-to-find-out-whats-causing-slowness-in-streamiung-youtube-videos)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25187-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Experts,</p><p>I am streaming a youtube video on my system. Sometimes it plays very fast and sometimes it just becomes slow. I want to know how to use wireshark to find out where the problem is coming from. Whether its coming from network fluctuations from my ISP or wherever.</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">youtube</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Sep '13, 22:36</strong></p><img src="https://secure.gravatar.com/avatar/bdd518b12f0c5066476bcbf76fda9c65?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="topzy2000&#39;s gravatar image" /><p>topzy2000<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="topzy2000 has no accepted answers">0%</span></p></div></div><div id="comments-container-25187" class="comments-container"></div><div id="comment-tools-25187" class="comment-tools"></div><div class="clear"></div><div id="comment-25187-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25194"></span>

<div id="answer-container-25194" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25194-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I want to know how to use wireshark to find out where the problem is coming from.</p></blockquote><p>Capture a session and check if Wireshark shows a 'more than usual' number of</p><ul><li>[TCP Dup ACK ..]</li><li>[TCP Retransmission]</li><li>[TCP Previous segment lost]</li><li>[TCP Window Full]</li><li>[TCP ZeroWindow]</li></ul><blockquote><p>Whether its coming from network fluctuations from my ISP or wherever.</p></blockquote><p>With only one capture point at the client, it's very hard to figure out who/what causes the problems, especially if the problem is within the ISP network, as you cannot distinguish those problems from problems 'in the internet' or from problems in the youtube network and/or servers.</p><p>In a home environment, I would tend to look at the client itself (your PC) as the most likely reason for the problem, like some software that slows it down occasionally.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '13, 02:25</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-25194" class="comments-container"></div><div id="comment-tools-25194" class="comment-tools"></div><div class="clear"></div><div id="comment-25194-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

