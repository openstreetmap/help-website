+++
type = "question"
title = "What is the difference between RST and RST,ACK?"
description = '''I&#x27;ve always wondered: What is the difference between a TCP RST and a RST,ACK? thanks, Geoff'''
date = "2013-02-26T11:15:00Z"
lastmod = "2013-02-26T11:34:00Z"
weight = 18886
keywords = [ "rst", "ack", "packet-capture" ]
aliases = [ "/questions/18886" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [What is the difference between RST and RST,ACK?](/questions/18886/what-is-the-difference-between-rst-and-rstack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18886-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've always wondered: What is the difference between a TCP RST and a RST,ACK?</p><p>thanks,</p><p>Geoff</p></div><div id="question-tags" class="tags-container tags">rst ack packet-capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Feb '13, 11:15</strong></p><img src="https://secure.gravatar.com/avatar/a00c3e32ea96f4989d9360937a93c73f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeoffP&#39;s gravatar image" /><p>GeoffP<br />
<span class="score" title="40 reputation points">40</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeoffP has no accepted answers">0%</span></p></div></div><div id="comments-container-18886" class="comments-container"></div><div id="comment-tools-18886" class="comment-tools"></div><div class="clear"></div><div id="comment-18886-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18890"></span>

<div id="answer-container-18890" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18890-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm trying to refrain myself from answering with just "The ACK"...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Feb '13, 11:34</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-18890" class="comments-container"><span id="18891"></span><div id="comment-18891" class="comment"><div id="post-18891-score" class="comment-score">1</div><div class="comment-text"><p>OK, I guess I failed at that ;-)</p><p>When I read the RFC, it seems to me that each RST should follow the normal acknowledgement rules. However, the sequence number is more important as to know whether or not the RST should be accepted by the receiving end.</p><p>See also the paragraph "Reset Generation" on p36 of <a href="https://tools.ietf.org/html/rfc793">RFC 793</a></p></div><div id="comment-18891-info" class="comment-info"><span class="comment-age">(26 Feb '13, 11:42)</span> SYN-bit ♦♦</div></div><span id="18892"></span><div id="comment-18892" class="comment"><div id="post-18892-score" class="comment-score">1</div><div class="comment-text"><p>well actually it's the ACK <strong>and</strong> the comma! ;-)</p><p>Honestly: There are so many rules when to use what in RFC 793, so there is no simple rule. Search for these strings in the RFC to find all occurrences:</p><blockquote><p><code>&lt;CTL=RST&gt;</code><br />
<code>&lt;CTL=RST,ACK</code></p></blockquote></div><div id="comment-18892-info" class="comment-info"><span class="comment-age">(26 Feb '13, 11:43)</span> Kurt Knochner ♦</div></div><span id="18894"></span><div id="comment-18894" class="comment"><div id="post-18894-score" class="comment-score"></div><div class="comment-text"><p>Thanks guys for the quick response. I know what SYN,ACKs are and RSTs.</p><p>I'm looking at a packet capture and I'm seeing RSTs and then moments later the same host is sending RST,ACKs. Hence leading to some confusion for me. After reading the RFC ("Reset Generation" section) above, it makes some more sense now.</p></div><div id="comment-18894-info" class="comment-info"><span class="comment-age">(26 Feb '13, 11:52)</span> GeoffP</div></div><span id="18895"></span><div id="comment-18895" class="comment"><div id="post-18895-score" class="comment-score"></div><div class="comment-text"><p>If you can post the capture file somewhere, we may (or may not) be able to give an explanation for that behavior.</p></div><div id="comment-18895-info" class="comment-info"><span class="comment-age">(26 Feb '13, 11:58)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-18890" class="comment-tools"></div><div class="clear"></div><div id="comment-18890-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

