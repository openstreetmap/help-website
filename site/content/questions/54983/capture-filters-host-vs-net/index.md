+++
type = "question"
title = "Capture filters host vs net"
description = '''What is the difference between host 172.18.5.4 and net 172.18.5.4?'''
date = "2016-08-19T08:48:00Z"
lastmod = "2016-08-19T09:00:00Z"
weight = 54983
keywords = [ "capture-filter" ]
aliases = [ "/questions/54983" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture filters host vs net](/questions/54983/capture-filters-host-vs-net)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54983-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What is the difference between host 172.18.5.4 and net 172.18.5.4?</p></div><div id="question-tags" class="tags-container tags">capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Aug '16, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/38cfd4921ab7292dd6be56ff1a602b9a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stevenlberntsen&#39;s gravatar image" /><p>stevenlberntsen<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stevenlberntsen has no accepted answers">0%</span></p></div></div><div id="comments-container-54983" class="comments-container"></div><div id="comment-tools-54983" class="comment-tools"></div><div class="clear"></div><div id="comment-54983-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54987"></span>

<div id="answer-container-54987" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54987-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>They're the same thing. From the pcap-filters man <a href="http://www.tcpdump.org/manpages/pcap-filter.7.html">page</a> for the net primitive:</p><blockquote><p>the netmask is 255.255.255.255 for a dotted quad (which means that it's really a host match),</p></blockquote></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Aug '16, 09:00</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Aug '16, 09:01</p></div></div><div id="comments-container-54987" class="comments-container"><span id="54988"></span><div id="comment-54988" class="comment"><div id="post-54988-score" class="comment-score"></div><div class="comment-text"><p>That matches what I am seeing. Thanks for your help.</p></div><div id="comment-54988-info" class="comment-info"><span class="comment-age">(19 Aug '16, 09:05)</span> stevenlberntsen</div></div><span id="54989"></span><div id="comment-54989" class="comment"><div id="post-54989-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-54989-info" class="comment-info"><span class="comment-age">(19 Aug '16, 09:06)</span> grahamb ♦</div></div></div><div id="comment-tools-54987" class="comment-tools"></div><div class="clear"></div><div id="comment-54987-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

