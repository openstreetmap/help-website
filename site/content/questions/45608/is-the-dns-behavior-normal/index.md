+++
type = "question"
title = "is the DNS behavior normal?"
description = '''Here is a short pcap With some DNS packets captured from a PC. The host sent two DNS requests, one to 8.8.8.8 and the other one to 8.8.4.4. Its request to 8.8.8.8 didn&#x27;t get a response but it didn&#x27;t retransmit wonder if this is normal behavior or is it some sort of indication of malware present in t...'''
date = "2015-09-02T19:59:00Z"
lastmod = "2015-09-02T23:39:00Z"
weight = 45608
keywords = [ "wireshark" ]
aliases = [ "/questions/45608" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [is the DNS behavior normal?](/questions/45608/is-the-dns-behavior-normal)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45608-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Here is a short <a href="https://www.cloudshark.org/captures/6331f39f285b">pcap</a> With some DNS packets captured from a PC. The host sent two DNS requests, one to 8.8.8.8 and the other one to 8.8.4.4. Its request to 8.8.8.8 didn't get a response but it didn't retransmit wonder if this is normal behavior or is it some sort of indication of malware present in the PC.</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Sep '15, 19:59</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p>pktUser1001<br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-45608" class="comments-container"></div><div id="comment-tools-45608" class="comment-tools"></div><div class="clear"></div><div id="comment-45608-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45610"></span>

<div id="answer-container-45610" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45610-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think it is normal, or at least depending on the stack. It asks the secondary DNS as a fallback, and when that didn't work the queries are repeated.</p><p>There is no reason at all to assume malware being present.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Sep '15, 23:39</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-45610" class="comments-container"><span id="45618"></span><div id="comment-45618" class="comment"><div id="post-45618-score" class="comment-score"></div><div class="comment-text"><p>When neither the primary or secondary DNS server responded, I thought it should retry on primary DNS server, but this pcap showed it actually retried on secondary DNS server. A little weird, but I agree, it's unlikely malware will go down to the business of actually generating DNS request packets.</p></div><div id="comment-45618-info" class="comment-info"><span class="comment-age">(03 Sep '15, 08:15)</span> pktUser1001</div></div></div><div id="comment-tools-45610" class="comment-tools"></div><div class="clear"></div><div id="comment-45610-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

