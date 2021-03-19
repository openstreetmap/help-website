+++
type = "question"
title = "How to find syn not followed by a syn+ack"
description = '''I am having trouble with occasional connect timeouts. Is there anyway in wireshark to find where the three way handshake fails? Thanks in advance Chip'''
date = "2012-05-03T08:26:00Z"
lastmod = "2012-05-07T16:42:00Z"
weight = 10640
keywords = [ "handshake", "three-way" ]
aliases = [ "/questions/10640" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to find syn not followed by a syn+ack](/questions/10640/how-to-find-syn-not-followed-by-a-synack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10640-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am having trouble with occasional connect timeouts. Is there anyway in wireshark to find where the three way handshake fails?</p><p>Thanks in advance</p><p>Chip</p></div><div id="question-tags" class="tags-container tags">handshake three-way</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '12, 08:26</strong></p><img src="https://secure.gravatar.com/avatar/f05edaccdf6f8c7f737ac66f67fd31c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="blueridge55&#39;s gravatar image" /><p>blueridge55<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="blueridge55 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 May '12, 12:41</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-10640" class="comments-container"></div><div id="comment-tools-10640" class="comment-tools"></div><div class="clear"></div><div id="comment-10640-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="10641"></span>

<div id="answer-container-10641" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10641-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Use the display filter 'tcp.flags eq 0x02' (only SYN flag set)<br />
then: Statistics -&gt; Conversations</p><p>Select the option "Limit to display filter" (at the bottom)<br />
Select the tab TCP<br />
</p><p>Sort the output by "Packets".</p><p>Those connections with 1 packet are likely the "good" connections (one SYN only)</p><p>Those connections with &gt; 1 packets are most likely the unanswered connections (several packets with SYN as a result of a retry).</p><p>EDIT: I just realized that the same question has already been answered some time ago:<br />
<a href="http://ask.wireshark.org/questions/6576/identify-syn-packets-without-synack">http://ask.wireshark.org/questions/6576/identify-syn-packets-without-synack</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '12, 08:29</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 May '12, 10:30</p></div></div><div id="comments-container-10641" class="comments-container"><span id="10648"></span><div id="comment-10648" class="comment"><div id="post-10648-score" class="comment-score"></div><div class="comment-text"><p>Yap, but some question openers never vote / accept so ;)</p></div><div id="comment-10648-info" class="comment-info"><span class="comment-age">(03 May '12, 13:39)</span> Landi</div></div><span id="10649"></span><div id="comment-10649" class="comment"><div id="post-10649-score" class="comment-score"></div><div class="comment-text"><p>Maybe they don't know about the voting system. The Q&amp;A system here is totally different to other forums. I think only frequent forum users do understand the system and make use of votes.</p><p>My impression is that a lot of users are one-time users. They subscribe to get a problem "fixed" and then they stop participating. However, I might be wrong. After all, I'm just a forum member for a few days now - whereas I'm using wireshark for years.</p></div><div id="comment-10649-info" class="comment-info"><span class="comment-age">(03 May '12, 14:22)</span> Kurt Knochner ♦</div></div><span id="11079"></span><div id="comment-11079" class="comment"><div id="post-11079-score" class="comment-score"></div><div class="comment-text"><p>Its true. Sometime the work loads do not permit to do that. Your support is highly appreciated. NizamSri</p></div><div id="comment-11079-info" class="comment-info"><span class="comment-age">(16 May '12, 22:20)</span> NizamSri</div></div></div><div id="comment-tools-10641" class="comment-tools"></div><div class="clear"></div><div id="comment-10641-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10687"></span>

<div id="answer-container-10687" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10687-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Assuming that you're truly going through a timeout on initial connection attempts, you would have retransmitted SYN packets. Every common operating system will try at least 3 times (sometime 5) to establish a connection before giving up; they do this by retransmitting the SYN packet. So, if you captured traffic on system A when A attempts to connect to system B and fails, applying 'tcp.flags eq 0x02 &amp;&amp; tcp.analysis.retransmission' to the capture would show you any retransmitted SYN packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 May '12, 12:14</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p>wesmorgan1<br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span> </br></br></p></div></div><div id="comments-container-10687" class="comments-container"><span id="10693"></span><div id="comment-10693" class="comment"><div id="post-10693-score" class="comment-score"></div><div class="comment-text"><p>This filter does not work on my Windows Vista PC. Wireshark does not identify the repeated SYNs as retransmissions, so no packets are shown.</p></div><div id="comment-10693-info" class="comment-info"><span class="comment-age">(04 May '12, 21:05)</span> Jim Aragon</div></div></div><div id="comment-tools-10687" class="comment-tools"></div><div class="clear"></div><div id="comment-10687-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10758"></span>

<div id="answer-container-10758" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10758-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><strong>MATE</strong> can help as well</p><blockquote><p><code>http://wiki.wireshark.org/Mate/GettingStarted</code></p></blockquote><p>Load <strong>tcp.mate</strong> from the Wiki. After a restart of Wireshark, use this display filter:</p><blockquote><p><code>tcp.flags eq 0x02 and mate.tcp_ses.NumOfPdus &lt; 4</code><br />
</p></blockquote><p>That's all packets with only a SYN flag and where the conversation contains less than 4 packets.</p><p>Well, that's not perfect, but at least it will find the 'regular' threefold retry attempt.</p><p><strong>Sample</strong> to test with: <strong><a href="http://cloudshark.org/captures/9279c75f8161">http://cloudshark.org/captures/9279c75f8161</a></strong></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '12, 16:42</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 May '12, 16:46</p></div></div><div id="comments-container-10758" class="comments-container"></div><div id="comment-tools-10758" class="comment-tools"></div><div class="clear"></div><div id="comment-10758-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

