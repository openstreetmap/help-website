+++
type = "question"
title = "Filter to remove non-periodic events"
description = '''I am performing a Wireshark capture for 24 hours at a network endpoint. During these 24 hours, the endpoint communicates with multiple other endpoints, for example IP addresses A through K. The endpoint where the capture is being performed (my endpoint) constantly communicates with endpoints with IP...'''
date = "2013-08-20T12:22:00Z"
lastmod = "2013-08-21T03:35:00Z"
weight = 23883
keywords = [ "non-periodic", "events" ]
aliases = [ "/questions/23883" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Filter to remove non-periodic events](/questions/23883/filter-to-remove-non-periodic-events)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23883-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am performing a Wireshark capture for 24 hours at a network endpoint. During these 24 hours, the endpoint communicates with multiple other endpoints, for example IP addresses A through K. The endpoint where the capture is being performed (my endpoint) constantly communicates with endpoints with IP addresses A through J throughout the 24 hours. However, my endpoint only communicates with IP address K only a single time during the 24 hours. For example: 1. IP address A = 5 TCP connections during the 24 hours 2. IP address B = 23 TCP connections during the 24 hours 3. IP address C = 15 UDP connections during the 24 hours And so forth until: IP address K = 1 TCP connection during the 24 hours</p><p>Is there a way to display the number of TCP/UDP connections per IP address in Wireshark? Is there a way to remove (create a filter) to remove traffic from an IP address in which only a single TCP/UDP connection was made?</p></div><div id="question-tags" class="tags-container tags">non-periodic events</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Aug '13, 12:22</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-23883" class="comments-container"></div><div id="comment-tools-23883" class="comment-tools"></div><div class="clear"></div><div id="comment-23883-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23901"></span>

<div id="answer-container-23901" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23901-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there a way to display the number of TCP/UDP connections per IP address in Wireshark?</p></blockquote><p>Not directly. What you can do is this:</p><blockquote><p>Statistics -&gt; Conversations -&gt; IP</p></blockquote><p>Then count the amount of connections <strong>manually</strong> from your client -&gt; A,B,C,D,E etc.</p><p>You can do the same on the CLI</p><blockquote><p>tshark -nr input.pcap -q -z conv,ip</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '13, 03:35</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-23901" class="comments-container"><span id="23918"></span><div id="comment-23918" class="comment"><div id="post-23918-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the reply. I modified your suggestion to include tcp and udp ports: tshark -nr input.pcap -q -z conv,tcp tshark -nr input.pcap -q -z conv,udp</p><p>I combined the outputs to create one table that includes all the TCP and UDP ports. After doing some post-analysis, I was able to determine which IP addresses utilized multiple ports and therefore could no be a single TCP/UDP connection.</p><p>However, I have another issue. For NTP, the above analysis is invalid since port 123 is used for both source/destination ports and my endpoint performs numerous NTP transfers.</p><p>Is there a way to output (using tshark) the time when a certain IP address is being used?</p><p>For example: IP address A is access at 12400, 26800, 41200, etc..</p></div><div id="comment-23918-info" class="comment-info"><span class="comment-age">(21 Aug '13, 12:14)</span> Amato_C</div></div></div><div id="comment-tools-23901" class="comment-tools"></div><div class="clear"></div><div id="comment-23901-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

