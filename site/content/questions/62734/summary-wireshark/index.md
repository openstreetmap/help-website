+++
type = "question"
title = "Summary wireshark"
description = '''How to count packet loss in summary wireshark'''
date = "2017-07-13T02:45:00Z"
lastmod = "2017-07-13T14:27:00Z"
weight = 62734
keywords = [ "packetloss" ]
aliases = [ "/questions/62734" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Summary wireshark](/questions/62734/summary-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62734-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to count packet loss in summary wireshark</p></div><div id="question-tags" class="tags-container tags">packetloss</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jul '17, 02:45</strong></p><img src="https://secure.gravatar.com/avatar/2b52f4ef29dea620dbfe99c82e986c00?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wiwiasmara&#39;s gravatar image" /><p>wiwiasmara<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wiwiasmara has no accepted answers">0%</span></p></div></div><div id="comments-container-62734" class="comments-container"><span id="62737"></span><div id="comment-62737" class="comment"><div id="post-62737-score" class="comment-score"></div><div class="comment-text"><p>Hardly.</p><p>To count lost packets, you first have to know that they should have been there. So you need to compare captures taken at source and destination, or there must be some packet numbering in the received flows you are interested in. So edit your question with more details, and you'll het a more detailed answer.</p></div><div id="comment-62737-info" class="comment-info"><span class="comment-age">(13 Jul '17, 03:32)</span> sindy</div></div></div><div id="comment-tools-62734" class="comment-tools"></div><div class="clear"></div><div id="comment-62734-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62764"></span>

<div id="answer-container-62764" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62764-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Do you mean, <em>"How does Wireshark determine the number of dropped packets?"</em></p><p>Wireshark is relying on libpcap (or WinPcap) to report this information. Basically, it's the number of packets that were received and would have been placed into the kernel's buffer but which were dropped because the buffer was full, likely due to Wireshark not reading those packets out of the buffer fast enough.</p><p>Refer to Guy Harris' explanation <a href="http://seclists.org/tcpdump/2013/q4/55">here</a> and my answer to <a href="https://stackoverflow.com/questions/39866757/how-to-resolve-tcpdump-dropped-packets">this other question</a> over at Stack Overflow, which is also based on Guy's superb explanations. These questions and answers happen to pertain to tcpdump, but Wireshark relies on the same mechanism essentially.</p><p>(If you mean something else, then kindly elaborate as sindy indicated.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jul '17, 14:27</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-62764" class="comments-container"></div><div id="comment-tools-62764" class="comment-tools"></div><div class="clear"></div><div id="comment-62764-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

