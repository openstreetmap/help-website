+++
type = "question"
title = "Plot arrival time of UDP packets"
description = '''My application should send a UDP packet every 16.7mS. I would like to see how much the arrival time varies. I want what &quot;Statistics-&amp;gt;TCP StreamGraph-&amp;gt;Stephens&quot; does for TCP except for UDP. I tried &quot;Statistics-&amp;gt;IO Graph&quot; but couldn&#x27;t get it to do what I wanted. Any hints? Thanks, Todd'''
date = "2012-08-07T13:18:00Z"
lastmod = "2012-08-07T17:31:00Z"
weight = 13441
keywords = [ "arrival", "plot", "udp", "graph", "time" ]
aliases = [ "/questions/13441" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Plot arrival time of UDP packets](/questions/13441/plot-arrival-time-of-udp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13441-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My application should send a UDP packet every 16.7mS. I would like to see how much the arrival time varies. I want what "Statistics-&gt;TCP StreamGraph-&gt;Stephens" does for TCP except for UDP. I tried "Statistics-&gt;IO Graph" but couldn't get it to do what I wanted.</p><p>Any hints? Thanks, Todd</p></div><div id="question-tags" class="tags-container tags">arrival plot udp graph time</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Aug '12, 13:18</strong></p><img src="https://secure.gravatar.com/avatar/746f25240c5f0a3afd05a41fa4889bab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sampsont&#39;s gravatar image" /><p>sampsont<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sampsont has no accepted answers">0%</span></p></div></div><div id="comments-container-13441" class="comments-container"></div><div id="comment-tools-13441" class="comment-tools"></div><div class="clear"></div><div id="comment-13441-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13445"></span>

<div id="answer-container-13445" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13445-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I would like to see how much the <strong>arrival time varies</strong></p></blockquote><p>If you want to draw the variation of the arrival time ('similar' to jitter - see also <a href="http://ask.wireshark.org/questions/12837/udp-packets-jitter-and-delay/12861">my answer for another question</a>), you would need something in Wireshark that is able to calculate the mean value of the delta time between several past packets and then measure the deviation of the current packet (arrival time) from that mean value. Without scripting (either parsing tshark output or using a Lua listener), this is not possible with the standard Wireshark binary.</p><p>The best thing you can do (without scripting) is this:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wireshark.jpg" alt="screenshot" /></p><p>Please adjust the 'Filter:' string to whatever matches your application protocol. The X-Axis at the right should show your 16.7 ms. The variation of the hight of the spikes, should give you an idea if the packets arrive "equally spaced" or with some deviation. Please change the "X-Axis tick interval" if you don't get usefull data!</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Aug '12, 17:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 07 Aug '12, 17:39</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-13445" class="comments-container"><span id="13476"></span><div id="comment-13476" class="comment"><div id="post-13476-score" class="comment-score"></div><div class="comment-text"><p>Thanks for taking the time and making the effort to return such a clear and helpful response!</p></div><div id="comment-13476-info" class="comment-info"><span class="comment-age">(08 Aug '12, 11:20)</span> sampsont</div></div></div><div id="comment-tools-13445" class="comment-tools"></div><div class="clear"></div><div id="comment-13445-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

