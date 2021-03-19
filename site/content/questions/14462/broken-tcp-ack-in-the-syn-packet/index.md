+++
type = "question"
title = "Broken TCP ACK in the SYN Packet"
description = '''The SYN packet is reporting a broken TCP. Why does this being reported in the SYN and if there&#x27;s any possible issue for the rest of the connections?'''
date = "2012-09-23T07:59:00Z"
lastmod = "2012-09-23T17:28:00Z"
weight = 14462
keywords = [ "brokentcp" ]
aliases = [ "/questions/14462" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Broken TCP ACK in the SYN Packet](/questions/14462/broken-tcp-ack-in-the-syn-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14462-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The SYN packet is reporting a broken TCP. Why does this being reported in the SYN and if there's any possible issue for the rest of the connections?</p></div><div id="question-tags" class="tags-container tags">brokentcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Sep '12, 07:59</strong></p><img src="https://secure.gravatar.com/avatar/9d629f265392eaf7b61f921e25f9f730?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ws2006&#39;s gravatar image" /><p>ws2006<br />
<span class="score" title="1 reputation points">1</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ws2006 has no accepted answers">0%</span></p></div></div><div id="comments-container-14462" class="comments-container"><span id="14467"></span><div id="comment-14467" class="comment"><div id="post-14467-score" class="comment-score"></div><div class="comment-text"><p>You may be referring to the fact that ACK field is <em>not</em> set, and yet the ACK <em>field</em> is non-zero. Is that the error message you're getting?</p></div><div id="comment-14467-info" class="comment-info"><span class="comment-age">(23 Sep '12, 17:05)</span> hansangb</div></div><span id="14469"></span><div id="comment-14469" class="comment"><div id="post-14469-score" class="comment-score"></div><div class="comment-text"><blockquote><p>ACK field is <em>not</em> set, and yet the ACK <em>field</em> is non-zero</p></blockquote><p>Presumably "ACK <em>flag</em> is <em>not</em> set"?</p></div><div id="comment-14469-info" class="comment-info"><span class="comment-age">(23 Sep '12, 17:10)</span> Guy Harris ♦♦</div></div><span id="14473"></span><div id="comment-14473" class="comment"><div id="post-14473-score" class="comment-score"></div><div class="comment-text"><p>Yes. "Acknowledgement Number: 0xa300898e [should be 0x00000000 because Ack flag is not set." The acknowledge field is non-zero while the ACK flag is not set.</p></div><div id="comment-14473-info" class="comment-info"><span class="comment-age">(23 Sep '12, 17:58)</span> ws2006</div></div></div><div id="comment-tools-14462" class="comment-tools"></div><div class="clear"></div><div id="comment-14462-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14472"></span>

<div id="answer-container-14472" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14472-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>"Broken TCP" Expert Infos messages refer to a packet that does not comply with some aspect of the TCP specification, but that doesn't necessarily mean that there will be a problem with the communication. If would be helpful if you gave the entire error message. Are you seeing this one:</p><p>"Acknowledgment number: Broken TCP. The acknowledge field is nonzero while the ACK flag is not set" ?</p><p>In a TCP packet, when the ACK bit is not set, the Acknowledgment Number field is supposed to be set to zero. This error message means that the packet violates that rule: The ACK bit is <em>not</em> set, but the Acknowledgment Number field is <em>not</em> zero.</p><p>The very first packet of a TCP three-way handshake will not have the ACK bit set because the system sending the SYN packet has not heard from the other system yet. It isn't acknowledging any data, and it doesn't know the other system's initial sequence number yet, so it can't calculate a valid ACK number.</p><p>In this circumstance, the Acknowledgment Number field SHOULD be set to zero, but I've captured some traces where that isn't the case. Although it's non-compliant, this doesn't necessarily cause a problem when it's in the SYN packet. Because the ACK bit is not set, the receiving system will usually ignore the contents of the Acknowledgment Number field, so it won't be aware of the error.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Sep '12, 17:28</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-14472" class="comments-container"><span id="14474"></span><div id="comment-14474" class="comment"><div id="post-14474-score" class="comment-score"></div><div class="comment-text"><p>Hmm. I don't see anything in <a href="http://tools.ietf.org/html/rfc793">RFC 793</a> or <a href="http://tools.ietf.org/html/rfc1122">RFC 1122</a> about the acknowledgment number field having to be zero if the ACK flag isn't set, so this might be an indication of a TCP stack that forgot to set the ACK bit on a packet, but it's not an actual violation of the TCP specification. Perhaps the check we're doing should just check for non-initial-SYN packets without ACK.</p></div><div id="comment-14474-info" class="comment-info"><span class="comment-age">(23 Sep '12, 19:04)</span> Guy Harris ♦♦</div></div><span id="14475"></span><div id="comment-14475" class="comment"><div id="post-14475-score" class="comment-score"></div><div class="comment-text"><p>Now that I look, I can't find anything in the RFCs either. I did find an Internet draft titled "Normalization in the unused header fields of TCP/IP" that says "When the ACK bit is not set, the value of the acknowledgement field MUST be normalized. It must be set to some predefined value." However, it looks like this draft expired without ever becoming an RFC.</p></div><div id="comment-14475-info" class="comment-info"><span class="comment-age">(23 Sep '12, 19:44)</span> Jim Aragon</div></div><span id="14483"></span><div id="comment-14483" class="comment"><div id="post-14483-score" class="comment-score"></div><div class="comment-text"><p>Without any intention to start a discussion about RFC interpretation:</p><p>RFC793 states:</p><pre><code>Acknowledgment Number:  32 bits

    If the ACK control bit is set this field contains the value of the
    next sequence number the sender of the segment is expecting to
    receive.  Once a connection is established this is always sent.</code></pre><p>Does that mean, that the ACK number is unset (0) if the ACK bit is <strong>not</strong> set, if applying 'boolean logic' to that statement?</p></div><div id="comment-14483-info" class="comment-info"><span class="comment-age">(24 Sep '12, 11:57)</span> Kurt Knochner ♦</div></div><span id="14484"></span><div id="comment-14484" class="comment"><div id="post-14484-score" class="comment-score"></div><div class="comment-text"><p>Not necessarily - it could also mean "this field's contents are only to be looked at if the ACK bit is set; its contents are meaningless if it's not set".</p></div><div id="comment-14484-info" class="comment-info"><span class="comment-age">(24 Sep '12, 12:05)</span> Guy Harris ♦♦</div></div><span id="14490"></span><div id="comment-14490" class="comment"><div id="post-14490-score" class="comment-score"></div><div class="comment-text"><p>well, yes it could mean that. The RFC lacks a definition of how to handle the field if the ACK bit is not set. I guess that 'most implementations' set it to 0, following 'good programming style' by initializing variables at the start of the code.</p></div><div id="comment-14490-info" class="comment-info"><span class="comment-age">(24 Sep '12, 15:47)</span> Kurt Knochner ♦</div></div><span id="14513"></span><div id="comment-14513" class="comment not_top_scorer"><div id="post-14513-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the replies.</p></div><div id="comment-14513-info" class="comment-info"><span class="comment-age">(25 Sep '12, 08:23)</span> ws2006</div></div></div><div id="comment-tools-14472" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-14472-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

