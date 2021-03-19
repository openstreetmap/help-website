+++
type = "question"
title = "SIP Session-ID is undecoded"
description = '''Hello, I have captured traffic from IMS Core of Ericsson and Wireshark is unable to decode Session-ID in an INVITE packet. This field is defined in the RFC 7329. It is a mistake of me or this field is not supported for the moment ? Here is the error :  Expert Info (Note/Undecoded): Unrecognised SIP ...'''
date = "2015-05-19T07:36:00Z"
lastmod = "2015-05-19T12:25:00Z"
weight = 42539
keywords = [ "sip", "wireshark" ]
aliases = [ "/questions/42539" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SIP Session-ID is undecoded](/questions/42539/sip-session-id-is-undecoded)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42539-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have captured traffic from IMS Core of Ericsson and Wireshark is unable to decode Session-ID in an INVITE packet. This field is defined in the RFC 7329.</p><p>It is a mistake of me or this field is not supported for the moment ?</p><p>Here is the error :</p><pre><code>Expert Info (Note/Undecoded): Unrecognised SIP header (Session-ID)</code></pre><p>Thank you and best regard.</p><p>Gremaudc</p></div><div id="question-tags" class="tags-container tags">sip wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '15, 07:36</strong></p><img src="https://secure.gravatar.com/avatar/654ab8fdc6b89430a5baeadb3a39195a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gremaudc&#39;s gravatar image" /><p>gremaudc<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gremaudc has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 May '15, 07:37</p></div></div><div id="comments-container-42539" class="comments-container"></div><div id="comment-tools-42539" class="comment-tools"></div><div class="clear"></div><div id="comment-42539-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42559"></span>

<div id="answer-container-42559" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42559-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The header <strong>Session-ID</strong> is not defined in the code, so it's not yet supported.</p><p>See <strong>packet-sip.c</strong>:</p><pre><code>static const sip_header_t sip_headers[] = {</code></pre><p>If you need this, please file an enhancement bug at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '15, 12:25</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 May '15, 12:27</p></div></div><div id="comments-container-42559" class="comments-container"><span id="42609"></span><div id="comment-42609" class="comment"><div id="post-42609-score" class="comment-score"></div><div class="comment-text"><p>Added to trunk in <a href="https://code.wireshark.org/review/#/c/8581/">https://code.wireshark.org/review/#/c/8581/</a></p></div><div id="comment-42609-info" class="comment-info"><span class="comment-age">(22 May '15, 03:20)</span> Anders ♦</div></div></div><div id="comment-tools-42559" class="comment-tools"></div><div class="clear"></div><div id="comment-42559-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

