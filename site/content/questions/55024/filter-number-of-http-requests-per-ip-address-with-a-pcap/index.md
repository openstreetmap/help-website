+++
type = "question"
title = "Filter number of http requests per IP address with a PCAP?"
description = '''I&#x27;ve been playing around with statistics to try and achieve this but unsuccessful so far.  the problem is wireshark crashes when I open the endpoints window due to he fact the IP list is over 2.5 million. The pcap i&#x27;m analyzing is a ddos attack against my server.  Just wondering has anyone been able...'''
date = "2016-08-21T05:30:00Z"
lastmod = "2016-08-21T11:47:00Z"
weight = 55024
keywords = [ "http.request", "ddos", "statistics", "wireshark" ]
aliases = [ "/questions/55024" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Filter number of http requests per IP address with a PCAP?](/questions/55024/filter-number-of-http-requests-per-ip-address-with-a-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55024-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been playing around with statistics to try and achieve this but unsuccessful so far.</p><p>the problem is wireshark crashes when I open the endpoints window due to he fact the IP list is over 2.5 million. The pcap i'm analyzing is a ddos attack against my server.</p><p>Just wondering has anyone been able to get a list of requests per IP address within a pcap before?</p></div><div id="question-tags" class="tags-container tags">http.request ddos statistics wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Aug '16, 05:30</strong></p><img src="https://secure.gravatar.com/avatar/7106df1abcb09ba2c929757f51612d27?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bhoot&#39;s gravatar image" /><p>bhoot<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bhoot has no accepted answers">0%</span></p></div></div><div id="comments-container-55024" class="comments-container"></div><div id="comment-tools-55024" class="comment-tools"></div><div class="clear"></div><div id="comment-55024-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55028"></span>

<div id="answer-container-55028" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55028-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should look into processing such PCAP file through tshark. Using single pass dissection, preventing out-of-memory problem, would give you a 'text-based' output which you can process further through other tools.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '16, 11:47</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-55028" class="comments-container"><span id="55044"></span><div id="comment-55044" class="comment"><div id="post-55044-score" class="comment-score"></div><div class="comment-text"><p>Thank you ill take a look at this. In the meantime another tool NetWitness seems to work.</p></div><div id="comment-55044-info" class="comment-info"><span class="comment-age">(22 Aug '16, 04:23)</span> bhoot</div></div></div><div id="comment-tools-55028" class="comment-tools"></div><div class="clear"></div><div id="comment-55028-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

