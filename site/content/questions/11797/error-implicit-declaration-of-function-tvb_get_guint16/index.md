+++
type = "question"
title = "error: implicit declaration of function &#x27;tvb_get_guint16&#x27;"
description = '''Getting following error while make :  error: implicit declaration of function &#x27;tvb_get_guint16&#x27; error: implicit declaration of function &#x27;tvb_get_guint24&#x27; What library i will have to include to fix this ?'''
date = "2012-06-10T09:10:00Z"
lastmod = "2012-06-10T10:32:00Z"
weight = 11797
keywords = [ "dissector", "wireshark" ]
aliases = [ "/questions/11797" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [error: implicit declaration of function 'tvb\_get\_guint16'](/questions/11797/error-implicit-declaration-of-function-tvb_get_guint16)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11797-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Getting following error while make :</p><p>error: implicit declaration of function 'tvb_get_guint16'</p><p>error: implicit declaration of function 'tvb_get_guint24'</p><p>What library i will have to include to fix this ?</p></div><div id="question-tags" class="tags-container tags">dissector wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jun '12, 09:10</strong></p><img src="https://secure.gravatar.com/avatar/d15cd2870e25518ba76d2eb42f56bbcb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yogeshg&#39;s gravatar image" /><p>yogeshg<br />
<span class="score" title="41 reputation points">41</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yogeshg has no accepted answers">0%</span></p></div></div><div id="comments-container-11797" class="comments-container"></div><div id="comment-tools-11797" class="comment-tools"></div><div class="clear"></div><div id="comment-11797-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11799"></span>

<div id="answer-container-11799" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11799-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You are calling a function that does not exist, hence the error message. In tvbuff.c only <strong><code>tvb_get_guint8()</code></strong> is defined.</p><p>What are you trying to do? Please post the part of your code, where you call those functions.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jun '12, 10:32</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-11799" class="comments-container"><span id="11800"></span><div id="comment-11800" class="comment"><div id="post-11800-score" class="comment-score"></div><div class="comment-text"><p>actually i was trying to read 16 bits or 24 bits , and i googled and found these functions used in some dissector by someone. Anyways i have fixed it now , i am using "tvb_get_ntohs" and "tvb_get_ntoh24". Anyways thanks for reply.</p></div><div id="comment-11800-info" class="comment-info"><span class="comment-age">(10 Jun '12, 10:42)</span> yogeshg</div></div><span id="11802"></span><div id="comment-11802" class="comment"><div id="post-11802-score" class="comment-score"></div><div class="comment-text"><p>Yes. For an 8-bit quantity, "big-endian" ("host byte order") and "little-endian" are the same, but for any integral quantity bigger than 8 bits, the byte order matters. If there were <code>tvb_get_guint16()</code> or <code>tvb_get_guint24()</code> or... routines, they would have to take an argument specifying the byte order; Wireshark, instead, has separate routines to fetch big-endian (tvb_getntoh...) and little-endian (tvb_getletoh...) values.</p></div><div id="comment-11802-info" class="comment-info"><span class="comment-age">(10 Jun '12, 15:02)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-11799" class="comment-tools"></div><div class="clear"></div><div id="comment-11799-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

