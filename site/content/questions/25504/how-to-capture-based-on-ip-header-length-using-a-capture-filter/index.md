+++
type = "question"
title = "How to capture based on IP header length using a capture filter?"
description = '''how to this Display filter syntax convert Capture filter syntax ip.hdr_len &amp;gt;= 20 '''
date = "2013-10-02T05:41:00Z"
lastmod = "2013-10-02T08:48:00Z"
weight = 25504
keywords = [ "ip", "capture-filter", "syntax" ]
aliases = [ "/questions/25504" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to capture based on IP header length using a capture filter?](/questions/25504/how-to-capture-based-on-ip-header-length-using-a-capture-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25504-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how to this Display filter syntax convert Capture filter syntax</p><p><strong>ip.hdr_len &gt;= 20</strong></p></div><div id="question-tags" class="tags-container tags">ip capture-filter syntax</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Oct '13, 05:41</strong></p><img src="https://secure.gravatar.com/avatar/37ca2e5611f06fb91521aabe9f1546ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stih&#39;s gravatar image" /><p>stih<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stih has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Oct '13, 08:50</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-25504" class="comments-container"></div><div id="comment-tools-25504" class="comment-tools"></div><div class="clear"></div><div id="comment-25504-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25531"></span>

<div id="answer-container-25531" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25531-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>The following capture filter should give you what you asked for:</p><p><code>     ip[0]&amp;0x0f &gt;= 5</code></p><p>For more information on capture filter syntax, refer to the <a href="http://www.tcpdump.org/manpages/pcap-filter.7.html">pcap-filter</a> man page. They even provide the following very similar example:</p><p><em>The expression <code>'ip[0] &amp; 0xf != 5'</code> catches all IPv4 packets with options.</em></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Oct '13, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-25531" class="comments-container"><span id="25576"></span><div id="comment-25576" class="comment"><div id="post-25576-score" class="comment-score"></div><div class="comment-text"><p>thank you for answer . i have one more question . please explain each part mean</p><p>ip[0]&amp;0x0f &gt;= 5</p></div><div id="comment-25576-info" class="comment-info"><span class="comment-age">(02 Oct '13, 23:54)</span> stih</div></div><span id="25583"></span><div id="comment-25583" class="comment"><div id="post-25583-score" class="comment-score">1</div><div class="comment-text"><p>ip[0] is the first (well zeroeth) byte of the ip part of the frame. &amp; means to do a bitwise AND operation, using 0xf (hexadecimal for binary 00001111) as the other operand. So the result of "ip[0] &amp; 0xf" is just the lowest (rightmost) 4 bits. We then return true is the result is greater than or equal to 5. The 4 bit header length field is in units of 4 octets, and 4 x 5 = 20 (which is the length you were comparing for in the display filter string).</p></div><div id="comment-25583-info" class="comment-info"><span class="comment-age">(03 Oct '13, 04:50)</span> martyvis</div></div><span id="25646"></span><div id="comment-25646" class="comment"><div id="post-25646-score" class="comment-score"></div><div class="comment-text"><p>This question is starting to feel more and more like a homework assignment to me, because you obviously haven't read the <a href="http://www.tcpdump.org/manpages/pcap-filter.7.html">pcap-filter</a> man page. If you had, you would find your answer rather easily. And you might want to also reference <a href="http://tools.ietf.org/html/rfc791#section-3.1">RFC 791</a> to have a better understanding of the IP header fields.</p></div><div id="comment-25646-info" class="comment-info"><span class="comment-age">(04 Oct '13, 08:36)</span> cmaynard ♦♦</div></div><span id="25649"></span><div id="comment-25649" class="comment"><div id="post-25649-score" class="comment-score"></div><div class="comment-text"><p>Oops, sorry @cmaynard, I already converted his comment to a <a href="http://ask.wireshark.org/questions/25645/what-is-the-capture-filter-equivalent-of-the-display-filter-ipfrag_offset-0?page=1&amp;focusedAnswerId=25647#25647">new question</a>.</p></div><div id="comment-25649-info" class="comment-info"><span class="comment-age">(04 Oct '13, 08:42)</span> SYN-bit ♦♦</div></div><span id="25650"></span><div id="comment-25650" class="comment"><div id="post-25650-score" class="comment-score"></div><div class="comment-text"><p>You made it too easy ;) Oh well.</p></div><div id="comment-25650-info" class="comment-info"><span class="comment-age">(04 Oct '13, 08:44)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-25531" class="comment-tools"></div><div class="clear"></div><div id="comment-25531-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

