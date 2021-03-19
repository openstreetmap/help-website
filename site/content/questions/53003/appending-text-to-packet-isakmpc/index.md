+++
type = "question"
title = "Appending Text to packet-isakmp.c"
description = '''I&#x27;m in the process of migrating a custom Wireshark from 1.2.6 to 2.0.3. Yes, I know a huge leap.  I&#x27;m trying to figure out use 3 format strings in proto_tree_append_text(), however when compiling wireshark doesn&#x27;t like it.  The old code is:  case MY_DECODED_ID: attr_str = decoder (tvb, offset + 4, l...'''
date = "2016-05-27T08:01:00Z"
lastmod = "2016-05-28T04:06:00Z"
weight = 53003
keywords = [ "isakmp", "proto_tree_add_item", "proto_tree_add_text", "custom_attributes", "attribute-value-pair" ]
aliases = [ "/questions/53003" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Appending Text to packet-isakmp.c](/questions/53003/appending-text-to-packet-isakmpc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53003-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53003-score" class="post-score" title="current number of votes">0</div><span id="post-53003-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I'm in the process of migrating a custom Wireshark from 1.2.6 to 2.0.3. Yes, I know a huge leap.</p><p>I'm trying to figure out use 3 format strings in <code>proto_tree_append_text()</code>, however when compiling wireshark doesn't like it.</p><p>The old code is:</p><pre><code>case MY_DECODED_ID:
attr_str = decoder (tvb, offset + 4, len); /* Refers back to the customer decoder function I have */
proto_tree_add_text(tree, tvb, offset, pack_len, &quot;%s %u %s&quot;, str, type, attr_str);</code></pre><p>This code addresses a value in the transform attributes. <code>attr_str</code> is listed in the function variables as <code>const char *attr_str</code>. When this information was decoded in wireshark 1.2.6, it showed the attribute and a 6 digit number for the value (i.e., Decoder ID: 123456).</p><p>Currently, the new code is located in the <code>dissect_transform_..._attributes</code>. I've put the <code>const gchar *attr_str</code> into the function variables again. So then the new code I have as:</p><pre><code>case MY_DECODER_ID:
proto_tree_add_item(sub_transform_attr_type_tree, hf_isakmp_ike_attr_decoder_id, tvb. offset, optlen, ENC_NA);
attr_str = decoder_id(tvb, offset + 4, len);
proto_tree_append_text(transform_attr_type_item, &quot;%s %u %s&quot;, val_to_str(tvb_get_ntohs(tvb, offset), str, type, attr_str, &quot;Unknown %d&quot;));</code></pre><p>I have tried the <code>proto_tree_add_string()</code>, but that didn't help any. I'm looking for some ideas. PS, I am far from being an expert in programming, so if I'm way out of line, it's OK to let me know.</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-isakmp" rel="tag" title="see questions tagged &#39;isakmp&#39;">isakmp</span> <span class="post-tag tag-link-proto_tree_add_item" rel="tag" title="see questions tagged &#39;proto_tree_add_item&#39;">proto_tree_add_item</span> <span class="post-tag tag-link-proto_tree_add_text" rel="tag" title="see questions tagged &#39;proto_tree_add_text&#39;">proto_tree_add_text</span> <span class="post-tag tag-link-custom_attributes" rel="tag" title="see questions tagged &#39;custom_attributes&#39;">custom_attributes</span> <span class="post-tag tag-link-attribute-value-pair" rel="tag" title="see questions tagged &#39;attribute-value-pair&#39;">attribute-value-pair</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 May '16, 08:01</strong></p><img src="https://secure.gravatar.com/avatar/9638449aebfb48e8c6f5b1770f1298fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ladyslinger&#39;s gravatar image" /><p><span>ladyslinger</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ladyslinger has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 May '16, 08:29</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-53003" class="comments-container"><span id="53005"></span><div id="comment-53005" class="comment"><div id="post-53005-score" class="comment-score"></div><div class="comment-text"><p>And what error did you get?</p></div><div id="comment-53005-info" class="comment-info"><span class="comment-age">(27 May '16, 08:29)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="53008"></span><div id="comment-53008" class="comment"><div id="post-53008-score" class="comment-score"></div><div class="comment-text"><p>The error I get is "too many arguments in function 'val_to_str'"</p></div><div id="comment-53008-info" class="comment-info"><span class="comment-age">(27 May '16, 10:19)</span> <span class="comment-user userinfo">ladyslinger</span></div></div></div><div id="comment-tools-53003" class="comment-tools"></div><div class="clear"></div><div id="comment-53003-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53026"></span>

<div id="answer-container-53026" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53026-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53026-score" class="post-score" title="current number of votes">1</div><span id="post-53026-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The prototype for <code>val_to_str()</code> is:</p><pre><code>val_to_str(const guint32 val, const value_string *vs, const char *fmt)</code></pre><p>But in your code you have:</p><pre><code>val_to_str(tvb_get_ntohs(tvb, offset), str, type, attr_str, &quot;Unknown %d&quot;)</code></pre><p>i.e. 5 parameters instead of the expected 3. It's not entirely clear from the minimal context you've provided exactly what you're trying to do, so you'll have to work out exactly what you should be passing to <code>val_to_str()</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 May '16, 04:06</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-53026" class="comments-container"></div><div id="comment-tools-53026" class="comment-tools"></div><div class="clear"></div><div id="comment-53026-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

