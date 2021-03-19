+++
type = "question"
title = "wireshark monitor mode on Windows"
description = '''I am using Windows 7 64bit edition and Intel(R) Centrino(R) Wireless-N 1030 q:why wireshark not working in Monitor mode and Microsoft Network Monitor 3.4 working fine wireshark in monitor mode I see only packets to and from my machine'''
date = "2014-05-21T14:13:00Z"
lastmod = "2014-05-21T14:29:00Z"
weight = 32962
keywords = [ "wireshark", "monitor", "mode" ]
aliases = [ "/questions/32962" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark monitor mode on Windows](/questions/32962/wireshark-monitor-mode-on-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32962-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using Windows 7 64bit edition and Intel(R) Centrino(R) Wireless-N 1030 q:why wireshark not working in Monitor mode and Microsoft Network Monitor 3.4 working fine wireshark in monitor mode I see only packets to and from my machine</p></div><div id="question-tags" class="tags-container tags">wireshark monitor mode</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 May '14, 14:13</strong></p><img src="https://secure.gravatar.com/avatar/457ef807adfa8ffbc503bb3bc92f6360?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mohammad&#39;s gravatar image" /><p>mohammad<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mohammad has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 May '14, 15:00</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-32962" class="comments-container"></div><div id="comment-tools-32962" class="comment-tools"></div><div class="clear"></div><div id="comment-32962-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32963"></span>

<div id="answer-container-32963" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32963-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Because WinPcap does not support monitor mode.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 May '14, 14:29</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-32963" class="comments-container"><span id="32964"></span><div id="comment-32964" class="comment"><div id="post-32964-score" class="comment-score"></div><div class="comment-text"><p>then why Microsoft Network Monitor 3.4 working fine</p></div><div id="comment-32964-info" class="comment-info"><span class="comment-age">(21 May '14, 14:45)</span> mohammad</div></div><span id="32965"></span><div id="comment-32965" class="comment"><div id="post-32965-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>what can I do?</p></blockquote><p>Use a different OS (even in a virtual machine), use a different sniffer, buy an Airpcap adapter (please google it) or extend/modify WinPcap to support monitor mode.</p></div><div id="comment-32965-info" class="comment-info"><span class="comment-age">(21 May '14, 14:57)</span> Kurt Knochner ♦</div></div><span id="32966"></span><div id="comment-32966" class="comment"><div id="post-32966-score" class="comment-score"></div><div class="comment-text"><p>thanks man</p></div><div id="comment-32966-info" class="comment-info"><span class="comment-age">(21 May '14, 15:25)</span> mohammad</div></div><span id="32967"></span><div id="comment-32967" class="comment"><div id="post-32967-score" class="comment-score"></div><div class="comment-text"><blockquote><p>then why Microsoft Network Monitor 3.4 working fine</p></blockquote><p>As it does not use WinPcap.</p><p>Btw: Please don't change your comments totally, otherwise it's hard to follow the discussion. My first comment does not make any sense after your comment rewrite.</p></div><div id="comment-32967-info" class="comment-info"><span class="comment-age">(21 May '14, 15:26)</span> Kurt Knochner ♦</div></div><span id="32968"></span><div id="comment-32968" class="comment"><div id="post-32968-score" class="comment-score"></div><div class="comment-text"><p>sorry .and thanks agan</p></div><div id="comment-32968-info" class="comment-info"><span class="comment-age">(21 May '14, 16:02)</span> mohammad</div></div><span id="32971"></span><div id="comment-32971" class="comment not_top_scorer"><div id="post-32971-score" class="comment-score"></div><div class="comment-text"><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-32971-info" class="comment-info"><span class="comment-age">(21 May '14, 21:46)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-32963" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-32963-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

