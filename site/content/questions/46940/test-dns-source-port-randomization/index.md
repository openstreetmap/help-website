+++
type = "question"
title = "Test DNS Source Port Randomization"
description = '''I am trying to filter DNS traffic in a capture file based upon ip address and udp source port randomization. I tried multiple filter strings with tshark but have been unable to come up with a solution. tshark -n -r capture.pcap -T fields -e ip.src -e udp.port|sort -u '''
date = "2015-10-26T08:03:00Z"
lastmod = "2015-10-26T09:54:00Z"
weight = 46940
keywords = [ "dns" ]
aliases = [ "/questions/46940" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Test DNS Source Port Randomization](/questions/46940/test-dns-source-port-randomization)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46940-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to filter DNS traffic in a capture file based upon ip address and udp source port randomization. I tried multiple filter strings with tshark but have been unable to come up with a solution.</p><p>tshark -n -r capture.pcap -T fields -e ip.src -e udp.port|sort -u</p></div><div id="question-tags" class="tags-container tags">dns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '15, 08:03</strong></p><img src="https://secure.gravatar.com/avatar/68fb2c86dea789c3f0cfcc9e3ab1ab1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="m00p&#39;s gravatar image" /><p>m00p<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="m00p has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Oct '15, 08:26</p></div></div><div id="comments-container-46940" class="comments-container"></div><div id="comment-tools-46940" class="comment-tools"></div><div class="clear"></div><div id="comment-46940-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46946"></span>

<div id="answer-container-46946" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46946-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>What about this:</p><blockquote><p>tshark -nr capture.pcap -Y "dns" -T fields -e ip.src -e udp.sport</p></blockquote><p>BTW: What do you mean by "and udp source port randomization"?</p><p>Maybe I'm misunderstanding your question. If so, please add more information and probably a small example.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '15, 09:54</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-46946" class="comments-container"><span id="46951"></span><div id="comment-46951" class="comment"><div id="post-46951-score" class="comment-score"></div><div class="comment-text"><p>Kurt,</p><p>The filter string worked well with parsing the output. IRT Source Port Randomization, I am checking my DNS traffic to verify queries are using proper security measures. Thanks!</p><p>m00p</p></div><div id="comment-46951-info" class="comment-info"><span class="comment-age">(26 Oct '15, 12:49)</span> m00p</div></div><span id="46952"></span><div id="comment-46952" class="comment"><div id="post-46952-score" class="comment-score"></div><div class="comment-text"><p>good!</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-46952-info" class="comment-info"><span class="comment-age">(26 Oct '15, 13:00)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-46946" class="comment-tools"></div><div class="clear"></div><div id="comment-46946-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

