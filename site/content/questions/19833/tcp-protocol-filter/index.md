+++
type = "question"
title = "TCP protocol filter"
description = '''In order to capture the start and end packets (the SYN and FIN packets) of each TCP conversation, the following TCP filter is applied - tcp[tcpflags] &amp;amp; (tcp-syn|tcp-fin) = 1 . Hopefully the above is in fact correct. What is the purpose of the [tcpflags] in the filter ? Is it simply part of the s...'''
date = "2013-03-26T03:22:00Z"
lastmod = "2013-03-26T04:10:00Z"
weight = 19833
keywords = [ "tcpflags", "capture-filter", "tcp", "bpf" ]
aliases = [ "/questions/19833" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [TCP protocol filter](/questions/19833/tcp-protocol-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19833-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In order to capture the start and end packets (the SYN and FIN packets) of each TCP conversation, the following TCP filter is applied - <strong>tcp[tcpflags] &amp; (tcp-syn|tcp-fin) = 1</strong> .</p><p>Hopefully the above is in fact correct.</p><p>What is the purpose of the [tcpflags] in the filter ? Is it simply part of the syntax and thus a must-have whenever a filter concerning tcp flags are used ?</p></div><div id="question-tags" class="tags-container tags">tcpflags capture-filter tcp bpf</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Mar '13, 03:22</strong></p><img src="https://secure.gravatar.com/avatar/9b52984d9786885d47fe81e43d8591ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dinged&#39;s gravatar image" /><p>Dinged<br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dinged has no accepted answers">0%</span></p></div></div><div id="comments-container-19833" class="comments-container"></div><div id="comment-tools-19833" class="comment-tools"></div><div class="clear"></div><div id="comment-19833-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19834"></span>

<div id="answer-container-19834" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19834-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>The "tcpflags" in tcp[tcpflags] is just a static offset into the tcp header structure. It points to the 13th octet, which contains the TCP flags.</p><p>When you compare against two flags, you can't use "= x" in your filter, as you do not know which of the flags will match. You can however use "!= 0" (not equal) to test whether any of them were set. So your filter will be:</p><pre><code>tcp[tcpflags] &amp; (tcp-syn|tcp-fin) != 0</code></pre><p>Or without using the symbolic names:</p><pre><code>tcp[13] &amp; 3 != 0</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '13, 04:10</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-19834" class="comments-container"><span id="19837"></span><div id="comment-19837" class="comment"><div id="post-19837-score" class="comment-score"></div><div class="comment-text"><p>Oh thanks for the clarification regarding the use of ! and != . Which flag does the '3' represent ? I tried googling, but there's no information on which bit represent which TCP flag..</p></div><div id="comment-19837-info" class="comment-info"><span class="comment-age">(26 Mar '13, 05:26)</span> Dinged</div></div><span id="19838"></span><div id="comment-19838" class="comment"><div id="post-19838-score" class="comment-score">2</div><div class="comment-text"><p>The 3 is an logical or of the first two bits which represent tcp-syn and tcp-fin. So your "(tcp-syn|tcp-fin)" actually means "(2|1)" and this results in "3".</p><p>(for the TCP flags, see <a href="http://en.wikipedia.org/wiki/Transmission_Control_Protocol#TCP_segment_structure)">http://en.wikipedia.org/wiki/Transmission_Control_Protocol#TCP_segment_structure)</a></p></div><div id="comment-19838-info" class="comment-info"><span class="comment-age">(26 Mar '13, 05:42)</span> SYN-bit ♦♦</div></div><span id="19839"></span><div id="comment-19839" class="comment"><div id="post-19839-score" class="comment-score"></div><div class="comment-text"><p>Oh the bits are counted backwards from FIN ? I was counting from NS. Thanks alot. But in one example I found in a book, tcp[13] &amp; 8 == 8 represents packets with PSH flags. Shouldn't it be tcp[13] &amp; 4 == 4 ?</p></div><div id="comment-19839-info" class="comment-info"><span class="comment-age">(26 Mar '13, 05:56)</span> Dinged</div></div><span id="19848"></span><div id="comment-19848" class="comment"><div id="post-19848-score" class="comment-score">2</div><div class="comment-text"><p>Yes, bits are counted from the least significant bit (LSB), so the book is correct:</p><ul><li>FIN is the 0th bit, so its value is 2^0=1</li><li>SYN is the 1st bit, so its value is 2^1=2</li><li>RST is the 2nd bit, so its value is 2^2=4</li><li>PSH is the 3rd bit, so its value is 2^3=8</li></ul><p>etc.</p></div><div id="comment-19848-info" class="comment-info"><span class="comment-age">(26 Mar '13, 12:03)</span> SYN-bit ♦♦</div></div><span id="19858"></span><div id="comment-19858" class="comment"><div id="post-19858-score" class="comment-score"></div><div class="comment-text"><p>^ Thanks for the clear explanation. My knowledge of bits is sadly lacking. Kudos.</p></div><div id="comment-19858-info" class="comment-info"><span class="comment-age">(26 Mar '13, 18:48)</span> Dinged</div></div></div><div id="comment-tools-19834" class="comment-tools"></div><div class="clear"></div><div id="comment-19834-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

