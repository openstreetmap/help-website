+++
type = "question"
title = "Can I extract data from the tvb using a header field?"
description = '''Can I use a header field to extract data from a tvb? In an earlier question I was trying to extract data from a processed proto_item, which I was only able to solve with a hack. After looking through the latest tvbuff.h, proto.h, etc, I didn&#x27;t see any functions that looked like they performed this f...'''
date = "2015-01-23T10:04:00Z"
lastmod = "2015-01-24T16:50:00Z"
weight = 39366
keywords = [ "development", "dissector", "hf", "tvb" ]
aliases = [ "/questions/39366" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Can I extract data from the tvb using a header field?](/questions/39366/can-i-extract-data-from-the-tvb-using-a-header-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39366-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39366-score" class="post-score" title="current number of votes">0</div><span id="post-39366-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can I use a header field to extract data from a tvb?</p><p>In <a href="http://ask.wireshark.org/questions/7225" title="an earlier question">an earlier question</a> I was trying to extract data from a processed <code>proto_item</code>, which I was only able to solve with a hack. After looking through the latest <code>tvbuff.h</code>, <code>proto.h</code>, etc, I didn't see any functions that looked like they performed this function. I've drilled down through <code>proto_tree_add_item</code> to see how it is normally accomplished, and there appears to be a lot of machinery involved in picking a few bits out of the supplied <code>tvbuff_t</code>. I would rather avoid using the <code>tvb_get_bits</code> family of functions if possible to reduce the number of offset calculations performed within each dissector.</p><p><strong>Is there a way to use the <code>hfindex</code> populated by <code>proto_register_field_array</code> with a given offset and <code>tvbuff_t</code> to extract the data for use in dissector logic?</strong> You can assume that I don't need data wider than 32 bits, although a general solution is obviously welcome.</p><p>As an example, say a dissector has the following:</p><pre><code>static int hf_myBits = -1;
static hf_register_info hf[] = {
    {&amp;hf_myBits, {&quot;Some bits&quot;,
        &quot;my_proto.my_bits&quot;, FT_UINT16, BASE_HEX, NULL, 0xFFF0, &quot;Some important bits&quot;, HFILL}}
}</code></pre><p><code>hf</code> is then registered in <code>proto_register_my_proto</code>, and at some point in <code>dissect_my_proto</code>:</p><pre><code>static void dissect_my_proto(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
{
    //...
    proto_tree_add_item(pMyTree, hf_myBits, tvb, some_offset, 2, ENC_LITTLE_ENDIAN);

    my_bits_value = tvb_get_something(tvb, some_offset, hf_myBits); // !
    if(my_bits_value == SOME_IMPORTANT_VALUE)
    {
        //dissect the rest of the data as ABC
    } else {
        //dissect the rest of the data as XYZ
    }
    //...
}</code></pre><p>What function would I call on the line marked with <code>// !</code>?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-hf" rel="tag" title="see questions tagged &#39;hf&#39;">hf</span> <span class="post-tag tag-link-tvb" rel="tag" title="see questions tagged &#39;tvb&#39;">tvb</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jan '15, 10:04</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-39366" class="comments-container"></div><div id="comment-tools-39366" class="comment-tools"></div><div class="clear"></div><div id="comment-39366-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="39385"></span>

<div id="answer-container-39385" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39385-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39385-score" class="post-score" title="current number of votes">0</div><span id="post-39385-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there a way to use the hfindex populated by proto_register_field_array with a given offset and tvbuff_t to extract the data for use in dissector logic?</p></blockquote><p>Generally no, not easily. There are a couple of functions in <code>proto.h</code> that both set the tree item and retrieve the value: <code>proto_tree_add_bytes_item()</code> and <code>proto_tree_add_time_item()</code>. But most <code>proto.h</code> functions just set the tree item, and it's up to you to get the value separately if you need the value for dissector logic. In theory you could get the field's value, after setting the tree item for it, by looking up the hfindex in the tree and getting its type and calling fvalue_get_uinteger or whatever. But really it's faster, easier, and clearer to just get the value you need by using <code>tvb_get_guint16()</code> or <code>tvb_get_bits16()</code> or whatever.</p><p>So for your example code it could be something like this:</p><pre><code>my_bits_value = tvb_get_ntohs(tvb, some_offset);
if ((my_bits_value &amp; SOME_VALUE_MASK) == SOME_IMPORTANT_VALUE)
{
    //dissect the rest of the data as ABC
} else {
    //dissect the rest of the data as XYZ
}</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '15, 10:32</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-39385" class="comments-container"></div><div id="comment-tools-39385" class="comment-tools"></div><div class="clear"></div><div id="comment-39385-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39386"></span>

<div id="answer-container-39386" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39386-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39386-score" class="post-score" title="current number of votes">0</div><span id="post-39386-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What might be best would be a family of <code>proto_tree_add_</code> routines that take a <em>pointer</em> to a value as an argument, and return the value through that pointer <em>regardless</em> of whether anything was added to the protocol tree or not, e.g.</p><pre><code>proto_item *proto_tree_add_uint_get_value(proto_tree *tree, int hfindex, tvbuff_t *tvb, const gint start, gint length, const guint encoding, guint *value);</code></pre><p>However, those functions don't currently exist, so you'd have to fetch the value yourself, separately from putting it into the protocol tree.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '15, 16:50</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Jan '15, 17:04</strong> </span></p></div></div><div id="comments-container-39386" class="comments-container"></div><div id="comment-tools-39386" class="comment-tools"></div><div class="clear"></div><div id="comment-39386-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

