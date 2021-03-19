+++
type = "question"
title = "Strangly high memory consumption when using capture filters"
description = '''Hi folks, I need to do a long term capture on a server under high load and try to find session initiations with a TCP(SYN) that were not answered(SYN,ACK). Since there is a high load on this server i thougt that I probably need capture filters so that i dont run out of memory on the server. What i d...'''
date = "2012-11-08T07:52:00Z"
lastmod = "2012-11-08T08:06:00Z"
weight = 15725
keywords = [ "capture-filter", "bug", "memory" ]
aliases = [ "/questions/15725" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Strangly high memory consumption when using capture filters](/questions/15725/strangly-high-memory-consumption-when-using-capture-filters)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15725-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi folks,</p><p>I need to do a long term capture on a server under high load and try to find session initiations with a TCP(SYN) that were not answered(SYN,ACK).</p><p>Since there is a high load on this server i thougt that I probably need capture filters so that i dont run out of memory on the server.</p><p>What i did was to add a capture filter that said "tcp[0xd]&amp;2=2". It seems to work great. I see only SYN and SYN,ACK packets. I can then filter the capture with a display filter to look at the relevant IP address with a "ip.addr == 1.2.3.4".</p><p>My take on this is that wireshark will not use more memory than the amount of data that passes through from the capture filter.</p><p>My result is that i have ben running for 10 minutes capturing 19000 SYN and SYN,ACK packets. I have then used the display filter to narrow the result down to 48 packets. The problem is that Wireshark uses 2,43GB RAM after 10 minutes to store these 19000 packets. Some math on this says that it is using 126KB for storing each SYN/SYN,ACK.</p><p>Am i getting all this backwards somehow or could it be that more data is getting through the capture filter and stored in memory than what the capture filter says?</p><p>OS: Windows 2008 R2 Wireshark 1.8.3 64-bit</p><p>Thankfull for all help :)</p></div><div id="question-tags" class="tags-container tags">capture-filter bug memory</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '12, 07:52</strong></p><img src="https://secure.gravatar.com/avatar/ad8ebeb4bcd82977f4bc3ff88135b485?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MrTernstrom&#39;s gravatar image" /><p>MrTernstrom<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MrTernstrom has no accepted answers">0%</span></p></div></div><div id="comments-container-15725" class="comments-container"></div><div id="comment-tools-15725" class="comment-tools"></div><div class="clear"></div><div id="comment-15725-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15727"></span>

<div id="answer-container-15727" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15727-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark maintains state about conversations, i.e. SYN/SYN,ACK and this uses memory.</p><p>Use dumpcap to capture the data as this doesn't retain any state info. In addition you may want to set a snaplen (-s) to limit the amount of data actually captured and written to disk.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '12, 08:06</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-15727" class="comments-container"></div><div id="comment-tools-15727" class="comment-tools"></div><div class="clear"></div><div id="comment-15727-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

