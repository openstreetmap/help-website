+++
type = "question"
title = "DNS Service Response Time"
description = '''Hello all. Firstly, thanks for a brilliant piece of software: The Swiss Army Knife of the network engineer&#x27;s toolbox. My question is generally, how do you create a new SRT measurement tool? Specifically, is there one/could there be one for measuring DNS response (time between a query/response pair)?...'''
date = "2015-11-03T04:21:00Z"
lastmod = "2015-11-03T06:41:00Z"
weight = 47180
keywords = [ "time", "service", "dns", "response" ]
aliases = [ "/questions/47180" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [DNS Service Response Time](/questions/47180/dns-service-response-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47180-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all. Firstly, thanks for a brilliant piece of software: The Swiss Army Knife of the network engineer's toolbox.</p><p>My question is generally, how do you create a new SRT measurement tool? Specifically, is there one/could there be one for measuring DNS response (time between a query/response pair)? Or is there an easy way to achieve that anyway via some other means, for DNS?</p><p>Thoughts appreciated please. Thanks, Greg - Wireshark novice</p></div><div id="question-tags" class="tags-container tags">time service dns response</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Nov '15, 04:21</strong></p><img src="https://secure.gravatar.com/avatar/d043de6006e8bfbb1af73c5a8e9855c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gchoules&#39;s gravatar image" /><p>gchoules<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gchoules has no accepted answers">0%</span></p></div></div><div id="comments-container-47180" class="comments-container"></div><div id="comment-tools-47180" class="comment-tools"></div><div class="clear"></div><div id="comment-47180-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47184"></span>

<div id="answer-container-47184" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47184-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark already calculates the time between the query and the response, if both packets are present in the trace. The field is <em>dns.time</em>. Of course, this is the time between the request packet and the response packet <em>at the capture point</em>, which, if the capture was not done at or near the client, may not be the time between when the request was actually sent by the client and when the response was received by the client.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Nov '15, 06:41</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-47184" class="comments-container"></div><div id="comment-tools-47184" class="comment-tools"></div><div class="clear"></div><div id="comment-47184-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

