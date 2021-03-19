+++
type = "question"
title = "wireshark ICMP &#x27;seq&#x27; in packet info"
description = '''I am trying to understand the capture for PING in wireshark. Can some one tell me what is the meaning of seq=1/256 or seq=3/768 in ICMP packet info? Thanks in advance'''
date = "2017-06-09T04:32:00Z"
lastmod = "2017-06-09T04:34:00Z"
weight = 61899
keywords = [ "wireshark", "ubuntu" ]
aliases = [ "/questions/61899" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark ICMP 'seq' in packet info](/questions/61899/wireshark-icmp-seq-in-packet-info)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61899-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to understand the capture for PING in wireshark. Can some one tell me what is the meaning of seq=1/256 or seq=3/768 in ICMP packet info? Thanks in advance</p></div><div id="question-tags" class="tags-container tags">wireshark ubuntu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '17, 04:32</strong></p><img src="https://secure.gravatar.com/avatar/89600711cdbd05ed6826a8b944665142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lokeshboddeti&#39;s gravatar image" /><p>lokeshboddeti<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lokeshboddeti has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jun '17, 04:33</p></div></div><div id="comments-container-61899" class="comments-container"></div><div id="comment-tools-61899" class="comment-tools"></div><div class="clear"></div><div id="comment-61899-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61900"></span>

<div id="answer-container-61900" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61900-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's the sequence number that ICMP echo packets have, and since it can be in <a href="https://en.wikipedia.org/wiki/Endianness">little endian or big endian byte order</a>, Wireshark shows both interpretations, separated by the "/".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jun '17, 04:34</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-61900" class="comments-container"><span id="61901"></span><div id="comment-61901" class="comment"><div id="post-61901-score" class="comment-score"></div><div class="comment-text"><p>Thank you jasper, for the clarification.</p></div><div id="comment-61901-info" class="comment-info"><span class="comment-age">(09 Jun '17, 04:36)</span> lokeshboddeti</div></div><span id="61906"></span><div id="comment-61906" class="comment"><div id="post-61906-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-61906-info" class="comment-info"><span class="comment-age">(09 Jun '17, 06:12)</span> Jaap ♦</div></div></div><div id="comment-tools-61900" class="comment-tools"></div><div class="clear"></div><div id="comment-61900-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

