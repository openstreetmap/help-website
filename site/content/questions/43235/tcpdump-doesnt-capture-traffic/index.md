+++
type = "question"
title = "tcpdump doesn&#x27;t capture traffic"
description = '''hi i,m new to tcpdump, i run it from linux terminal with this script but it only listens, it doesn&#x27;t capture anything although it should, is there command like -k in wireshark , that makes tcpdump start capturing immediately ?? #!/bin/bash tcpdump -i eth1 -s0 -c 700 -w ~/new.pcap &quot;tcp&quot; sleep 3 iperf...'''
date = "2015-06-17T02:59:00Z"
lastmod = "2015-06-17T04:21:00Z"
weight = 43235
keywords = [ "capture", "tcpdump" ]
aliases = [ "/questions/43235" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tcpdump doesn't capture traffic](/questions/43235/tcpdump-doesnt-capture-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43235-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi i,m new to tcpdump, i run it from linux terminal with this script but it only listens, it doesn't capture anything although it should, is there command like -k in wireshark , that makes tcpdump start capturing immediately ??</p><pre><code>#!/bin/bash
tcpdump -i eth1 -s0 -c 700 -w ~/new.pcap &quot;tcp&quot;
sleep 3
iperf -c 192.168.1.2  &amp;
sleep 6
killall tcpdump &amp;
killall iperf</code></pre></div><div id="question-tags" class="tags-container tags">capture tcpdump</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jun '15, 02:59</strong></p><img src="https://secure.gravatar.com/avatar/890399e77f2c0c0ff2f75ea2f43d3ff8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yas1234&#39;s gravatar image" /><p>yas1234<br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yas1234 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted to question 17 Jun '15, 03:32</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-43235" class="comments-container"><span id="43236"></span><div id="comment-43236" class="comment"><div id="post-43236-score" class="comment-score"></div><div class="comment-text"><p>Please don't tack new questions as an "Answer" to an existing unrelated question. Please read the FAQ for more info on using this site.</p></div><div id="comment-43236-info" class="comment-info"><span class="comment-age">(17 Jun '15, 03:33)</span> grahamb ♦</div></div><span id="43239"></span><div id="comment-43239" class="comment"><div id="post-43239-score" class="comment-score"></div><div class="comment-text"><p>@yas1234: BTW, if I look at your question history, it seems like you don't fully understand how this site is supposed to work.</p><p>It's pretty simple:</p><ul><li>You ask a question</li><li>people post their answers</li><li>if an answer is O.K. for you, <strong>you mark the answer</strong> as "accepted"</li></ul><p>You have asked quite a few questions in the past, with good answers, but you never accepted one of those answers. Please read the FAQ of this site and make yourself familiar with the site rules.</p><blockquote><p><a href="https://ask.wireshark.org/faq/">https://ask.wireshark.org/faq/</a></p></blockquote><p>Thanks!</p></div><div id="comment-43239-info" class="comment-info"><span class="comment-age">(17 Jun '15, 04:24)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-43235" class="comment-tools"></div><div class="clear"></div><div id="comment-43235-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43238"></span>

<div id="answer-container-43238" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43238-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You don't send the tcpdump command to the background (no &amp; at the end of the command), and thus the other commands will be executed only after tcpdump was stopped (I guess after you pressed CTRL-C)!</p><blockquote><p>is there command like -k in wireshark , that makes tcpdump start capturing immediately ??</p></blockquote><p>No, tcpdump starts to capture traffic, as soon as you start it.</p><p>BTW: If you add the &amp; to the tcpdump command, and you still don't see any traffic, you are either listening on the wrong interface (eth1) or the iperf command does not generate any traffic.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '15, 04:21</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Jun '15, 06:21</p></div></div><div id="comments-container-43238" class="comments-container"></div><div id="comment-tools-43238" class="comment-tools"></div><div class="clear"></div><div id="comment-43238-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

