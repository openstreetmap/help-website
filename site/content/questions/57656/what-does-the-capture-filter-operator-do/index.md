+++
type = "question"
title = "what does the capture filter operator &gt;&gt; do?"
description = '''for example port 80 and tcp[((tcp[12:1] &amp;amp; 0xf0) &amp;gt;&amp;gt; 2):4] = 0x47455420'''
date = "2016-11-26T18:19:00Z"
lastmod = "2016-11-26T19:12:00Z"
weight = 57656
keywords = [ "capture-filter" ]
aliases = [ "/questions/57656" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [what does the capture filter operator &gt;&gt; do?](/questions/57656/what-does-the-capture-filter-operator-do)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57656-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count">2</div></div></td><td><div id="item-right"><div class="question-body"><p>for example</p><p>port 80 and tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2):4] = 0x47455420</p></div><div id="question-tags" class="tags-container tags">capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '16, 18:19</strong></p><img src="https://secure.gravatar.com/avatar/ab3e4e392c3eba03d2aceb465adad270?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vcossio&#39;s gravatar image" /><p>vcossio<br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vcossio has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Nov '16, 18:43</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-57656" class="comments-container"></div><div id="comment-tools-57656" class="comment-tools"></div><div class="clear"></div><div id="comment-57656-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57657"></span>

<div id="answer-container-57657" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57657-score" class="post-score" title="current number of votes">9</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's the "shift right" operator. See <a href="http://www.tcpdump.org/manpages/pcap-filter.7.html">the pcap-filter(4) man page</a>; look at the "expression" section, which describes the syntax of expressions like that. (The syntax is based on the C programming language syntax for expressions; a number of other languages use a similar syntax.)</p><p>But that doesn't explain how that filter expression works.</p><p><code>tcp[12:1]</code> fetches the value of the byte at an offset of 12 from the beginning of the TCP header. <a href="https://tools.ietf.org/html/rfc793">RFC 793</a> is the specification for TCP, and shows what the TCP header looks like. <a href="https://tools.ietf.org/html/rfc793#section-3.1">Section 3.1 of RFC 793</a> shows the header; the byte at an offset of 12 has, in the upper 4 bits, the "data offset", which indicates how long the TCP header is, in units of 4-byte words.</p><p><code>tcp[12:1] &amp; 0xf0</code> clears the lower 4 bits (<code>0xf0</code>, in the filter's C-style syntax, is the hex value F0, which has the upper 4 bits set - F being 15, which is 1111 in binary - and the lower 4 bits clear; <code>&amp;</code> is the "bitwise AND" operator, just as in C), so that's the "data offset" in the upper 4 bits.</p><p><code>(tcp[12:1] &amp; 0xf0) &gt;&gt; 2)</code> takes that value and shifts it right by 2 bits. To convert the value with the "data offset" and 4 bits of zero to a data offset in <em>bytes</em>, you would first shift it right 4 bits, to put the data offset in <em>4-byte words</em> in the lower 4 bits, and then multiply the result by 4 to convert it from a count of 4-byte words to a count of bytes.</p><p>But multiplying by 4 is, for an unsigned value (such as the byte in question), equivalent to shifting left by 2, so that's shifting it right 4 bits and then left by 2 bits. If the lower bits are all zero, that's equivalent to shifting right by 2 bits, so <code>(tcp[12:1] &amp; 0xf0) &gt;&gt; 2)</code> is calculating the length of the TCP header, in bytes.</p><p>So <code>tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2):4]</code> fetches the 4 bytes at an offset of "length of TCP header, in bytes" - i.e., the first 4 bytes <em>after</em> the TCP header - as a big-endian number. If those 4 bytes are, in order, the ASCII character "G", the ASCII character "E", the ASCII character "T", and the ASCII character " " (a space) - i.e., the first 4 bytes of an HTTP "GET" request" - those 4 bytes, as a big endian number, would be 0x47455420, so that's checking whether the TCP payload begins with "GET ".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '16, 19:12</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-57657" class="comments-container"><span id="57658"></span><div id="comment-57658" class="comment"><div id="post-57658-score" class="comment-score"></div><div class="comment-text"><p>impressive answer :-)</p></div><div id="comment-57658-info" class="comment-info"><span class="comment-age">(27 Nov '16, 03:16)</span> Jasper ♦♦</div></div><span id="57709"></span><div id="comment-57709" class="comment"><div id="post-57709-score" class="comment-score"></div><div class="comment-text"><p>So basically does this:</p><p>1111 0000 &gt;&gt; 2 becomes 0011 1100</p><p>the same as above but with hexadecimal numbers:</p><p>0xf0 &gt;&gt; 2 becomes 0x3C</p><p>Now I get it.</p><p>Thanks for your detailed response.</p></div><div id="comment-57709-info" class="comment-info"><span class="comment-age">(29 Nov '16, 08:41)</span> vcossio</div></div></div><div id="comment-tools-57657" class="comment-tools"></div><div class="clear"></div><div id="comment-57657-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

