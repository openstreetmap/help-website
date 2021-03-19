+++
type = "question"
title = "Filter for Multicast"
description = '''Hi All, I have checked and filter for Multicast is as follows eth.dst[0] &amp;amp; 1 and understand that this corresponds to checking least significant bit of first address byte set. But I do not understand the capture syntax. 1)What is eth.dst[0] &amp;amp; 1 What I can interpret is to check [0]--&amp;gt;Least ...'''
date = "2015-12-05T11:01:00Z"
lastmod = "2015-12-05T11:18:00Z"
weight = 48294
keywords = [ "multicast" ]
aliases = [ "/questions/48294" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Filter for Multicast](/questions/48294/filter-for-multicast)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48294-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I have checked and filter for Multicast is as follows eth.dst[0] &amp; 1 and understand that this corresponds to checking least significant bit of first address byte set.</p><p>But I do not understand the capture syntax.</p><p>1)What is eth.dst[0] &amp; 1 What I can interpret is to check [0]--&gt;Least significant bit What is the filter &amp; 1 mean ( &amp; is ??)</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">multicast</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '15, 11:01</strong></p><img src="https://secure.gravatar.com/avatar/6c685868d46cd97a6a734504d69f5373?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rakeshreddy&#39;s gravatar image" /><p>rakeshreddy<br />
<span class="score" title="5 reputation points">5</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rakeshreddy has no accepted answers">0%</span></p></div></div><div id="comments-container-48294" class="comments-container"></div><div id="comment-tools-48294" class="comment-tools"></div><div class="clear"></div><div id="comment-48294-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48295"></span>

<div id="answer-container-48295" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48295-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p><code>eth.dst</code> is the full MAC address.<br />
<code>eth.dst[0]</code> is its most significant (first from the left in usual notation) byte.<br />
&amp; is a "bitwise and" used to mask out the interesting bit(s) out of a byte (while &amp;&amp; is a "logical and" used to group together conditions which both have to be met in order that the whole expression is true.</p><p>And the whole expression has a value of 0 if the least significant bit of the least significant byte is 0, which is interpreted as "false" and so packets with this (multicast) bit not set to 1 are not shown; the whole expression has a value of 1, which is interpreted as "true" and so the packets with this bit set to 1 are shown.</p><p>Edit: taking up here a link to <a href="https://packetsdropped.wordpress.com/2011/01/13/mac-address-universally-or-locally-administered-bit-and-individualgroup-bit/">an article explaining the role of U/L and I/G bits</a> from @rakeshreddy's comment below.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '15, 11:18</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Dec '15, 14:36</p></div></div><div id="comments-container-48295" class="comments-container"><span id="48296"></span><div id="comment-48296" class="comment"><div id="post-48296-score" class="comment-score"></div><div class="comment-text"><p>Hi Sindy,</p><p>Just one more question. I am a bit confused.</p><p>Say we have the mac address as 00:e0:52:00:00:00</p><p>From the above, can we say that this is not multicast as MSB is 0?</p><p>Thanks</p></div><div id="comment-48296-info" class="comment-info"><span class="comment-age">(05 Dec '15, 12:24)</span> rakeshreddy</div></div><span id="48297"></span><div id="comment-48297" class="comment"><div id="post-48297-score" class="comment-score"></div><div class="comment-text"><blockquote><p>can we say that this is not multicast as MSB is 0?<br />
</p></blockquote><p>Yes. In more detail, it is not a multicast MAC because bit 0 (the least significant <em>bit</em>) of its MSB (most significant <em>byte</em>) is 0, and it is a vendor-assigned address because bit 1 of the MSB is also 0.</p><p>What is the subject of your confusion?</p><p>(btw, off topic, thank you for giving me extra points for the answer, but to mark it as accepted for the sake of others asking a similar question, the "checkmark" icon is the right one to click. If you do that, the colour of the question in the list changes to indicate that it has at least one answer which was useful)</p></div><div id="comment-48297-info" class="comment-info"><span class="comment-age">(05 Dec '15, 12:31)</span> sindy</div></div><span id="48305"></span><div id="comment-48305" class="comment"><div id="post-48305-score" class="comment-score"></div><div class="comment-text"><p>Hi Sindy,</p><p>Thanks for your answer.</p><p>With Example I found Below in case others look up on the same issue.</p><p><a href="https://packetsdropped.wordpress.com/2011/01/13/mac-address-universally-or-locally-administered-bit-and-individualgroup-bit/">https://packetsdropped.wordpress.com/2011/01/13/mac-address-universally-or-locally-administered-bit-and-individualgroup-bit/</a></p><p>Thanks</p></div><div id="comment-48305-info" class="comment-info"><span class="comment-age">(05 Dec '15, 14:17)</span> rakeshreddy</div></div></div><div id="comment-tools-48295" class="comment-tools"></div><div class="clear"></div><div id="comment-48295-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

