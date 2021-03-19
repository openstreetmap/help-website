+++
type = "question"
title = "communication between two servers fails with large data (not too large)"
description = '''We have some issue on our production environment. In normal condition, communication between two servers(JBOSS application server and SQL 2005 database server) works perfectly. But In some situation, two servers(JBOSS application server and SQL 2005 database server) can communicate with each other f...'''
date = "2011-03-25T00:04:00Z"
lastmod = "2011-03-25T01:32:00Z"
weight = 3101
keywords = [ "zero-window", "nop-tcp-option" ]
aliases = [ "/questions/3101" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [communication between two servers fails with large data (not too large)](/questions/3101/communication-between-two-servers-fails-with-large-data-not-too-large)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3101-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have some issue on our production environment. In normal condition, communication between two servers(JBOSS application server and SQL 2005 database server) works perfectly.</p><p>But In some situation, two servers(JBOSS application server and SQL 2005 database server) can communicate with each other for small data (20 records) but communication fails with slightly large data(1000 records). Once this problem happens we have to restart the machine( the server on which JBOSS application server is deployed) to resolve the problem.</p><p>Note: After restarting the machine(the server on which JBOSS deployed) communication works perfectly (i.e. even with large data).</p><p>We are doing wireshark packet capture for this problem. It shows following warning in analysis.</p><p><strong><em>1)4 NOP in Row</em></strong></p><p><strong><em>2)Zero Window</em></strong></p><p>What is meaning of above warning? Can these warnings are related to disconnect problem? Any suggestion to isolate the issue would be great help to us...</p></div><div id="question-tags" class="tags-container tags">zero-window nop-tcp-option</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Mar '11, 00:04</strong></p><img src="https://secure.gravatar.com/avatar/513b0e255920948294008d9284662567?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Maulin&#39;s gravatar image" /><p>Maulin<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Maulin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>retagged 25 Mar '11, 02:33</p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span></p></div></div><div id="comments-container-3101" class="comments-container"></div><div id="comment-tools-3101" class="comment-tools"></div><div class="clear"></div><div id="comment-3101-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3103"></span>

<div id="answer-container-3103" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3103-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>NOPs "No Operation" might not be a problem, they're often used as a keep-alive mechanism to prevent an established session from being terminated (especially if it has to pass a firewall with state timeouts).</p><p>Zero Window is a problem if it is not a reset packet (which Wireshark should not mark as zero window). The TCP window is a receive buffer that gets filled with packets coming in from the sender. If the OS or the application doesn't process incoming data fast enough the remaining buffer (the window) will become smaller and smaller. If it hits zero the receiver tells the sender that it cannot process any more data until further notice (usually through a "window update", but the sender can also test if he can continue using "window probing").</p><p>If you encounter zero window problems you are usually facing an overworked receiving station, it is not a network problem but the receiver is not capable to process incoming data fast enough. You should investigate if you can improve the receivers performance by tuning the hardware, the OS settings or (worst case) the application.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '11, 01:24</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-3103" class="comments-container"></div><div id="comment-tools-3103" class="comment-tools"></div><div class="clear"></div><div id="comment-3103-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3105"></span>

<div id="answer-container-3105" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3105-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Just to support Jasper's statement - you can use "netstat -an" command (should be available on most of the platforms) and 2nd column should show you nos. of packets that are waiting in Q for processing. You can try to tweak "tcp read buffers"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '11, 01:32</strong></p><img src="https://secure.gravatar.com/avatar/d1e5efe891c907bf6be8231eca9db31a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vijay%20Gharge&#39;s gravatar image" /><p>Vijay Gharge<br />
<span class="score" title="36 reputation points">36</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vijay Gharge has no accepted answers">0%</span></p></div></div><div id="comments-container-3105" class="comments-container"></div><div id="comment-tools-3105" class="comment-tools"></div><div class="clear"></div><div id="comment-3105-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

