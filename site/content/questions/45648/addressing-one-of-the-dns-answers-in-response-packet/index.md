+++
type = "question"
title = "addressing one of the DNS answers in response packet"
description = '''Here is a pcap with DNS response containing multiple answers. How do we check if the TTL in the second answer is less than 10 second? It seems that all the ttl fields (in all the answers in this packet) are referred in display filter as &quot;dns.resp.ttl&quot;.  Any ideas? Thanks.'''
date = "2015-09-06T17:05:00Z"
lastmod = "2015-09-06T17:53:00Z"
weight = 45648
keywords = [ "wireshark" ]
aliases = [ "/questions/45648" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [addressing one of the DNS answers in response packet](/questions/45648/addressing-one-of-the-dns-answers-in-response-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45648-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Here is a <a href="https://www.cloudshark.org/captures/c6d6a45a1bb6">pcap</a> with DNS response containing multiple answers. How do we check if the TTL in the second answer is less than 10 second?</p><p>It seems that all the ttl fields (in all the answers in this packet) are referred in display filter as "dns.resp.ttl".</p><p>Any ideas? Thanks.</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Sep '15, 17:05</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p>pktUser1001<br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-45648" class="comments-container"></div><div id="comment-tools-45648" class="comment-tools"></div><div class="clear"></div><div id="comment-45648-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45649"></span>

<div id="answer-container-45649" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45649-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>When a field, such as <em>dns.resp.ttl</em>, occurs multiple times in a packet, there is no way to use display filters to distinguish individual occurrences of that field.</p><p>So the display filter "dns.resp.ttl &lt; 10" will show all packets that have one or more dns.resp.ttl fields with a value less than 10. There is no way in the Wireshark GUI to compare specifically against the dns.resp.ttl field in the second answer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Sep '15, 17:53</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-45649" class="comments-container"><span id="45650"></span><div id="comment-45650" class="comment"><div id="post-45650-score" class="comment-score"></div><div class="comment-text"><p>We we can address it like <code>dns.resp.answers[1].ttl</code>.</p></div><div id="comment-45650-info" class="comment-info"><span class="comment-age">(06 Sep '15, 20:08)</span> pktUser1001</div></div></div><div id="comment-tools-45649" class="comment-tools"></div><div class="clear"></div><div id="comment-45649-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

