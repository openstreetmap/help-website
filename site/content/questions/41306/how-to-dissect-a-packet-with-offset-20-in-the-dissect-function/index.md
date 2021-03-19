+++
type = "question"
title = "how to dissect a packet with offset 20 in the dissect function"
description = '''I am new to this dissector coding.please help me in solving this.Here is my sample code.I wanted to dissect a 4 byte. By taking first 20 bits for i bit and next 12 bits for j bit.But I didnt get the correct value when printed in decimal. I tried using tvb_get_htonl function instead of tvb_get_guint8...'''
date = "2015-04-08T22:17:00Z"
lastmod = "2015-04-15T04:45:00Z"
weight = 41306
keywords = [ "proto_tree_add_unit" ]
aliases = [ "/questions/41306" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [how to dissect a packet with offset 20 in the dissect function](/questions/41306/how-to-dissect-a-packet-with-offset-20-in-the-dissect-function)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41306-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41306-score" class="post-score" title="current number of votes">0</div><span id="post-41306-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am new to this dissector coding.please help me in solving this.Here is my sample code.I wanted to dissect a 4 byte. By taking first 20 bits for i bit and next 12 bits for j bit.But I didnt get the correct value when printed in decimal.</p><p>I tried using tvb_get_htonl function instead of tvb_get_guint8 function in the below code.But I didnt get correct result.</p><p>Please let me know how to dissect this 4 byte data.</p><p>dissect() {</p><p>proto_tree_add_uint(tree, hf_i_bit,tvb,offset,4,(tvb_get_guint8( tvb,offset &amp; 0xFFFFF000) &gt;&gt; 12));</p><p>proto_tree_add_uint(tree,hf_ j_bit,tvb,offset,2,tvb_get_guint8(tvb,offset &amp;0x00000FFF)); }</p><p>proto_register{</p><p>{ &amp;hf_ i_bit,</p><p>{ "i bit", "x.i", FT_UINT32, BASE_DEC,NULL, 0, NULL, HFILL } },</p><p>{ &amp;hf_ j_bit,</p><p>{ "j bit", "x.j", FT_UINT16, BASE_DEC,NULL, 0, NULL, HFILL } }, }</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-proto_tree_add_unit" rel="tag" title="see questions tagged &#39;proto_tree_add_unit&#39;">proto_tree_add_unit</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '15, 22:17</strong></p><img src="https://secure.gravatar.com/avatar/a2e29df6af5eb33f09d1ed5321ea6586?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lakshmi&#39;s gravatar image" /><p><span>lakshmi</span><br />
<span class="score" title="16 reputation points">16</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lakshmi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Apr '15, 01:50</strong> </span></p></div></div><div id="comments-container-41306" class="comments-container"></div><div id="comment-tools-41306" class="comment-tools"></div><div class="clear"></div><div id="comment-41306-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41315"></span>

<div id="answer-container-41315" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41315-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41315-score" class="post-score" title="current number of votes">0</div><span id="post-41315-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="lakshmi has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your code cannot as tvb_get_guint8 only retrieves a single byte (as indicated in the documentation). You should try something like:</p><pre><code>dissect() {

proto_tree_add_item(tree, hf_i_bit,tvb,offset,4,ENC_BIG_ENDIAN);

proto_tree_add_uint(tree,hf_ j_bit,tvb,offset,2, ENC_BIG_ENDIAN); }

proto_register{

{ &amp;hf_ i_bit,

{ &quot;i bit&quot;, &quot;x.i&quot;, FT_UINT32, BASE_DEC,NULL, 0xFFFFF000, NULL, HFILL } },

{ &amp;hf_ j_bit,

{ &quot;j bit&quot;, &quot;x.j&quot;, FT_UINT16, BASE_DEC,NULL, 0x0FFF, NULL, HFILL } }, }</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Apr '15, 02:24</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-41315" class="comments-container"><span id="41449"></span><div id="comment-41449" class="comment"><div id="post-41449-score" class="comment-score"></div><div class="comment-text"><p>thanks,it worked..</p></div><div id="comment-41449-info" class="comment-info"><span class="comment-age">(15 Apr '15, 04:28)</span> <span class="comment-user userinfo">lakshmi</span></div></div><span id="41451"></span><div id="comment-41451" class="comment"><div id="post-41451-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-41451-info" class="comment-info"><span class="comment-age">(15 Apr '15, 04:45)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-41315" class="comment-tools"></div><div class="clear"></div><div id="comment-41315-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

