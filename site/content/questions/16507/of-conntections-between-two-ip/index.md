+++
type = "question"
title = "# of conntections between two ip"
description = '''new to wireshark and teacher hasn&#x27;t responded to me, Im trying to find out how many connections(sessions) happen between two IP&#x27;s. im using filter ip.src==xxx.xxx.xxx.xxx&amp;amp;&amp;amp;ip.dst==xxx.xxx.xxx.xxx&amp;amp;&amp;amp;tcp.syn==1&amp;amp;&amp;amp;tcp.ack==0 but Im pretty sure thats not what I need. any info would...'''
date = "2012-12-03T12:02:00Z"
lastmod = "2012-12-03T15:54:00Z"
weight = 16507
keywords = [ "connection" ]
aliases = [ "/questions/16507" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\# of conntections between two ip](/questions/16507/of-conntections-between-two-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16507-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>new to wireshark and teacher hasn't responded to me, Im trying to find out how many connections(sessions) happen between two IP's. im using filter ip.src==xxx.xxx.xxx.xxx&amp;&amp;ip.dst==xxx.xxx.xxx.xxx&amp;&amp;tcp.syn==1&amp;&amp;tcp.ack==0 but Im pretty sure thats not what I need. any info would help</p></div><div id="question-tags" class="tags-container tags">connection</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Dec '12, 12:02</strong></p><img src="https://secure.gravatar.com/avatar/00d8ba8fc4168fb81fea4df24d6de179?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EMEDINA&#39;s gravatar image" /><p>EMEDINA<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EMEDINA has no accepted answers">0%</span></p></div></div><div id="comments-container-16507" class="comments-container"></div><div id="comment-tools-16507" class="comment-tools"></div><div class="clear"></div><div id="comment-16507-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16515"></span>

<div id="answer-container-16515" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16515-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>EMEDINA, All you want to see is the number of TCP connections between two PC's? How about this: Create your display filter "ip.addr==xxx.xxx.xxx.xxx&amp;&amp;ip.addr==xxx.xxx.xxx.xxx" (Notice, I'm using ip.addr). Then go to "statistics" "conversations" on the Wireshark munu bar. Select the "TCP" tab and check "Limit to display filter". This should show the the number of TCP sessions between the hosts referenced in the display filter.</p><p>Good luck.</p><p>Owen</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '12, 15:54</strong></p><img src="https://secure.gravatar.com/avatar/e12b8d5f904f018189f5cf3c69cbe5f9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Owen&#39;s gravatar image" /><p>Owen<br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Owen has no accepted answers">0%</span></p></div></div><div id="comments-container-16515" class="comments-container"></div><div id="comment-tools-16515" class="comment-tools"></div><div class="clear"></div><div id="comment-16515-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

