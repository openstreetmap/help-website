+++
type = "question"
title = "Why was the IP fragment size required to be a multiple of 8 bytes?"
description = '''In order to calculate Fragment Offset we need to divide the data block by 8. How we landed up on the digit 8? Is it total length of packet &amp;lt;2 to the power 16&amp;gt; (divided by) fragment offset &amp;lt;2 to the power 13&amp;gt; gives us 8  (or) Is it 2 to the power 16(total packet length) divided by 8 gives...'''
date = "2013-03-14T00:29:00Z"
lastmod = "2013-03-14T05:34:00Z"
weight = 19489
keywords = [ "ipfragmentaion" ]
aliases = [ "/questions/19489" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Why was the IP fragment size required to be a multiple of 8 bytes?](/questions/19489/why-was-the-ip-fragment-size-required-to-be-a-multiple-of-8-bytes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19489-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In order to calculate Fragment Offset we need to divide the data block by 8.</p><p>How we landed up on the digit 8?</p><p>Is it total length of packet &lt;2 to the power 16&gt; (divided by) fragment offset &lt;2 to the power 13&gt; gives us 8</p><p>(or)</p><p>Is it 2 to the power 16(total packet length) divided by 8 gives 2 to the power 13(fragment offset length)</p><p>which one came first?</p></div><div id="question-tags" class="tags-container tags">ipfragmentaion</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '13, 00:29</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p>krishnayeddula<br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Mar '13, 10:57</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-19489" class="comments-container"></div><div id="comment-tools-19489" class="comment-tools"></div><div class="clear"></div><div id="comment-19489-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19499"></span>

<div id="answer-container-19499" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19499-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I can't look into the minds of the people who wrote the <a href="http://tools.ietf.org/html/rfc791">IPv4 RFC</a> in 1981. But I suspect they decided to use 16 bits in the header for IP fragmentation purposes and then used 3 bits for flags and then used the remaining 13 bits for the offset. Resulting in an acceptable size of a multiple of 8 for the fragments.</p><p>I'm wondering why you'd like to know which came first?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Mar '13, 05:34</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-19499" class="comments-container"><span id="19521"></span><div id="comment-19521" class="comment"><div id="post-19521-score" class="comment-score"></div><div class="comment-text"><p>An example for IP Message of 12,000 bytes [where the Payload is 11,980].MTU is 1500.The data blocks[Application data + TCP Header] before dividing by 8 {0-1479;1480-2959;2960-4439;4440-5919;5920-7399;7400-8879;8880-10359;10360-11839;11840-11979} up to 8192 we can fit in 13 bit when it exceeds 8192 fragmentation offset will spill over from 13 bit so there is a need to condense the data block.As the maximum length of IP Packet is 65536 and dividing 65536 by 8 gives 8192 because of which our fragment offset never exceeds 13bit.</p><p>Little confused at this coincidence and hence my question/</p></div><div id="comment-19521-info" class="comment-info"><span class="comment-age">(14 Mar '13, 14:11)</span> krishnayeddula</div></div><span id="19525"></span><div id="comment-19525" class="comment"><div id="post-19525-score" class="comment-score">1</div><div class="comment-text"><p>It's not a coincidence. If the maximum IP packet size, in bytes, fits in 16 bits (so it's 2^16-1), and the maximum fragment offset is 13 bits (so it's 2^13-1), then the units of the fragment offset need to fit in (2^16-1)/(2^13-1). Throwing the -1 away doesn't really matter, so it's 2^16/2^13, which is 2^(16-13), or 2^3, or 8.</p><p>That's what SYN-bit was saying - if they picked a 13-bit fragment offset, and had a 16-bit packet size, the fragment offset would have to be in units of 8 bytes.</p></div><div id="comment-19525-info" class="comment-info"><span class="comment-age">(14 Mar '13, 22:17)</span> Guy Harris ♦♦</div></div><span id="25326"></span><div id="comment-25326" class="comment"><div id="post-25326-score" class="comment-score"></div><div class="comment-text"><p>nice explanation thanx man it helps</p></div><div id="comment-25326-info" class="comment-info"><span class="comment-age">(27 Sep '13, 15:10)</span> Rummy Khan</div></div></div><div id="comment-tools-19499" class="comment-tools"></div><div class="clear"></div><div id="comment-19499-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

