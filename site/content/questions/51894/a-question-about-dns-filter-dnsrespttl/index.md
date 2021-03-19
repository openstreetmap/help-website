+++
type = "question"
title = "A question about dns filter dns.resp.ttl"
description = '''I need to do some filtering on DNS response TTL field. However, I am not sure exactly what the following means: dns.resp.ttl &amp;lt; 100  The problem is that in a DNS response, there could be multiple A record, each with a different IP and possibly a different TTL. So the above expression can potential...'''
date = "2016-04-23T09:11:00Z"
lastmod = "2016-04-23T10:18:00Z"
weight = 51894
keywords = [ "wireshark" ]
aliases = [ "/questions/51894" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [A question about dns filter dns.resp.ttl](/questions/51894/a-question-about-dns-filter-dnsrespttl)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51894-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to do some filtering on DNS response TTL field. However, I am not sure exactly what the following means:</p><pre><code>dns.resp.ttl &lt; 100</code></pre><p>The problem is that in a DNS response, there could be multiple A record, each with a different IP and possibly a different TTL. So the above expression can potentially mean one of the following:</p><ul><li>One of the A-records has TTL &lt; 100</li><li>All the A-records have TTL &lt; 100</li></ul><p>The page <a href="https://www.wireshark.org/docs/dfref/d/dns.html">https://www.wireshark.org/docs/dfref/d/dns.html</a> didn't have enough information. Any ideas?</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '16, 09:11</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p>pktUser1001<br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-51894" class="comments-container"></div><div id="comment-tools-51894" class="comment-tools"></div><div class="clear"></div><div id="comment-51894-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51895"></span>

<div id="answer-container-51895" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51895-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The first one. It means "the packet has at least one dns.resp.ttl field with a value less than 100."</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '16, 10:18</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-51895" class="comments-container"><span id="52047"></span><div id="comment-52047" class="comment"><div id="post-52047-score" class="comment-score"></div><div class="comment-text"><p>Thanks @jim-aragon, sorry for the late reply.</p><p>Wonder if there is a way to express "all TTLs &lt; 100". Thanks.</p></div><div id="comment-52047-info" class="comment-info"><span class="comment-age">(28 Apr '16, 06:59)</span> pktUser1001</div></div><span id="52055"></span><div id="comment-52055" class="comment"><div id="post-52055-score" class="comment-score"></div><div class="comment-text"><p><code>dns.resp.ttl and !(dns.resp.ttl &gt;= 100)</code> should do the job. Means: at least one field <code>dns.resp.ttl</code> is present in the packet and none of the ones present has a value &gt;= 100.</p></div><div id="comment-52055-info" class="comment-info"><span class="comment-age">(28 Apr '16, 08:33)</span> sindy</div></div></div><div id="comment-tools-51895" class="comment-tools"></div><div class="clear"></div><div id="comment-51895-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

