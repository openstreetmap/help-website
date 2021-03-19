+++
type = "question"
title = "how to dissect bit by bit and display"
description = '''Hi, Iam trying for custom dissector bit wise operation octet by octet. I have used   proto_tree_add_bits_item(my_sub_tree, hf_my_type, my_tvb, offset,6, TRUE);  This is 6 bit lenth.  ..00 0010 = Message Type : FWD_CNTRL (0x02)  I can able to get the bits properly. No issues on that. i want remove   ...'''
date = "2014-05-31T00:40:00Z"
lastmod = "2014-07-04T03:55:00Z"
weight = 33229
keywords = [ "how", "dissect", "display", "bit", "to" ]
aliases = [ "/questions/33229" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to dissect bit by bit and display](/questions/33229/how-to-dissect-bit-by-bit-and-display)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33229-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33229-score" class="post-score" title="current number of votes">0</div><span id="post-33229-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Iam trying for custom dissector bit wise operation octet by octet.</p><p>I have used</p><pre><code>   proto_tree_add_bits_item(my_sub_tree, hf_my_type, my_tvb, offset,6, TRUE);</code></pre><p>This is 6 bit lenth.</p><pre><code>           ..00 0010 = Message Type : FWD_CNTRL (0x02)</code></pre><p>I can able to get the bits properly. No issues on that. i want remove</p><pre><code>                          &quot;..00 0010= &quot; this PART and diplay only
                          Message Type : FWD_CNTRL (0x02)</code></pre><p>I have tried another method using MASK</p><pre><code>             proto_tree_add_item(my_sub_tree, hf_my_type, my_tvb, offset,6, ENC_LITTLE_ENDIAN);

             { &amp;hf_msg_typ,
             { &quot;Message Type &quot;, &quot;msg_type&quot;,FT_UINT8, BASE_HEX, VALS(msg_type_vals), 0x3f, NULL, HFILL }
             },</code></pre><p>This one also output as</p><pre><code>                           ..00 0010 = Message Type : FWD_CNTRL (0x02)</code></pre><p>How can i remove<br />
</p><pre><code>                           &quot;..00 0010= &quot; this PART and diplay only
                            Message Type : FWD_CNTRL (0x02)</code></pre><p>Please Help</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-how" rel="tag" title="see questions tagged &#39;how&#39;">how</span> <span class="post-tag tag-link-dissect" rel="tag" title="see questions tagged &#39;dissect&#39;">dissect</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span> <span class="post-tag tag-link-bit" rel="tag" title="see questions tagged &#39;bit&#39;">bit</span> <span class="post-tag tag-link-to" rel="tag" title="see questions tagged &#39;to&#39;">to</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 May '14, 00:40</strong></p><img src="https://secure.gravatar.com/avatar/1339589a92af9455063c09e56bfc6299?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="umar&#39;s gravatar image" /><p><span>umar</span><br />
<span class="score" title="26 reputation points">26</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="umar has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Jun '14, 02:59</strong> </span></p></div></div><div id="comments-container-33229" class="comments-container"><span id="33501"></span><div id="comment-33501" class="comment"><div id="post-33501-score" class="comment-score"></div><div class="comment-text"><p>IMHO removing ..00 0010 = Message Type : FWD_CNTRL (0x02) is a bad choice the former let you see exactly which bits are beeing dissected and the meaning of the bits. If the bits allways occure in the same Place using proto_add_item with a bit mask may be a better choice than proto_tree_add_bits_item(). Just my 2 cents.</p></div><div id="comment-33501-info" class="comment-info"><span class="comment-age">(06 Jun '14, 04:38)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-33229" class="comment-tools"></div><div class="clear"></div><div id="comment-33229-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33498"></span>

<div id="answer-container-33498" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33498-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33498-score" class="post-score" title="current number of votes">0</div><span id="post-33498-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have you looked at the <code>proto_tree_add_xxx_format()</code> or <code>proto_tree_add_xxx_format_value()</code> functions? They give you full control of the tree representation.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jun '14, 03:54</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-33498" class="comments-container"><span id="34376"></span><div id="comment-34376" class="comment"><div id="post-34376-score" class="comment-score"></div><div class="comment-text"><p>Hi I have tried</p><pre><code>                  proto_tree_add_xxx_format() or proto_tree_add_xxx_format_value()  both.

                  Rteurning error. How exactly i should use to remove 
                                        &quot;..00 0010= &quot; this PART and diplay only
                                        Message Type : FWD_CNTRL (0x02)</code></pre><p>Thanks in advance!</p></div><div id="comment-34376-info" class="comment-info"><span class="comment-age">(03 Jul '14, 02:13)</span> <span class="comment-user userinfo">umar</span></div></div><span id="34403"></span><div id="comment-34403" class="comment"><div id="post-34403-score" class="comment-score">1</div><div class="comment-text"><p>Just use <code>proto_tree_add_text()</code> then as that gives you full control of the tree representation, but note that the field won't be filterable.</p></div><div id="comment-34403-info" class="comment-info"><span class="comment-age">(04 Jul '14, 03:55)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-33498" class="comment-tools"></div><div class="clear"></div><div id="comment-33498-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

