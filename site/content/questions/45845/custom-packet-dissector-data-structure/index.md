+++
type = "question"
title = "Custom packet dissector data structure"
description = '''Suppose I have a custom protocol called cust_prot. One of the field is of 4 bytes length and has a flag bit as follows:  The 5th bit of the 2nd byte of this field is a flag variable.  So, I wanted to know what will be the data structure. I have made the following structure but am not sure whether we...'''
date = "2015-09-15T04:29:00Z"
lastmod = "2015-09-15T18:49:00Z"
weight = 45845
keywords = [ "dissector", "tshark", "packet", "wireshark" ]
aliases = [ "/questions/45845" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Custom packet dissector data structure](/questions/45845/custom-packet-dissector-data-structure)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45845-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45845-score" class="post-score" title="current number of votes">0</div><span id="post-45845-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Suppose I have a custom protocol called cust_prot. One of the field is of 4 bytes length and has a flag bit as follows:</p><pre><code>      The 5th bit of the 2nd byte of this field is a flag variable.</code></pre><p>So, I wanted to know what will be the data structure. I have made the following structure but am not sure whether we need to do masking or not.</p><pre><code>     .
     .
     { &amp;hf_cust_prot_skip5,
         { &quot;CUST PROT SKIP5&quot;, &quot;cust_prot.skip5&quot;,
         FT_UINT32, BASE_DEC,
         NULL, 0x0,
         NULL, HFILL }
     },
     { &amp;hf_cust_prot_cap1,
         { &quot;CUST PROT CAP1&quot;, &quot;cust_prot.skip5.cap1&quot;,
         FT_BOOLEAN, BASE_DEC,
         NULL, 0x0,               /*Confused about this mask field*/
         NULL, HFILL }
     },
     .
     .</code></pre><p>Also if someone can provide the way to display that flag bit, it will be very useful.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Sep '15, 04:29</strong></p><img src="https://secure.gravatar.com/avatar/5c6557bd7c8696a17e1c44bae9cd4217?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="samprit&#39;s gravatar image" /><p><span>samprit</span><br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="samprit has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Sep '15, 04:41</strong> </span></p></div></div><div id="comments-container-45845" class="comments-container"></div><div id="comment-tools-45845" class="comment-tools"></div><div class="clear"></div><div id="comment-45845-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45848"></span>

<div id="answer-container-45848" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45848-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45848-score" class="post-score" title="current number of votes">1</div><span id="post-45848-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><pre><code> { &amp;hf_cust_prot_cap1,
     { &quot;CUST PROT CAP1&quot;, &quot;cust_prot.skip5.cap1&quot;,
     FT_BOOLEAN, 32,
     NULL, 0x080000,               /*&quot;5th bit&quot; of 2nd byte counting from the left ? */
     NULL, HFILL }
 },</code></pre><p>Use the usual <code>proto_tree_add_item(...)</code> to display the field.</p><p>Note that the exact format of the display of the field can be varied by changing the field width (32) and bit mask and using the correct <code>offset</code> in the proto_tree_add_item()` call.</p><p>E.G.,: usimg 8 as the field width, a bit mask of 0x08 and an offset of 1 from will display the field as 1 bit in 8 bits.</p><p>Try experimenting with different values.</p><p>This is all explained in doc/README.dissector.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '15, 05:47</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Sep '15, 05:48</strong> </span></p></div></div><div id="comments-container-45848" class="comments-container"><span id="45867"></span><div id="comment-45867" class="comment"><div id="post-45867-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-45867-info" class="comment-info"><span class="comment-age">(15 Sep '15, 18:49)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-45848" class="comment-tools"></div><div class="clear"></div><div id="comment-45848-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

