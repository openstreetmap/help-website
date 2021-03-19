+++
type = "question"
title = "How can I examine the actual value of a proto_item?"
description = '''How can I examine the actual value of a proto_item in my dissector? I thought something like this would work: ... {&amp;amp;hf_pfield,  {&quot;ProtoField&quot;, &quot;proto.field&quot;, FT_UINT32, BASE_HEX,  VALS(ProtoFieldValueString),  ProtoFieldBitmask, &quot;Proto Field&quot;, HFILL}} ... void dissect_proto(tvbuff_t *tvb, packet...'''
date = "2011-11-03T15:57:00Z"
lastmod = "2011-11-09T11:09:00Z"
weight = 7225
keywords = [ "development", "ftypes", "proto_item", "proto_tree" ]
aliases = [ "/questions/7225" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I examine the actual value of a proto\_item?](/questions/7225/how-can-i-examine-the-actual-value-of-a-proto_item)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7225-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7225-score" class="post-score" title="current number of votes">1</div><span id="post-7225-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I examine the actual value of a <code>proto_item</code> in my dissector? I thought something like this would work:</p><pre><code>...
{&amp;hf_pfield,
    {&quot;ProtoField&quot;, &quot;proto.field&quot;, FT_UINT32, BASE_HEX,
      VALS(ProtoFieldValueString),
      ProtoFieldBitmask, &quot;Proto Field&quot;, HFILL}}
...
void dissect_proto(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree) {
    proto_item *p_item = NULL;
    guint32 guint32_value = 0;
    ...
    if(tree) {
        p_item = ptvcursor_add(cursor, hf_pfield, 4, endianness);
        guint32_value = fvalue_get_uinteger(&amp;(item-&gt;finfo-&gt;value)); /*Crash*/
        ...
    }
    ...</code></pre><p>...but this pretty handily kills Wireshark every time, resulting in an uninformative "The application has requested the Runtime to terminate in an unusual way" dialog. (I think it's tripping an assertion somewhere, but I haven't been able to track it down yet). How can I access the data referenced by a <code>proto_item</code> without extracting it from the <code>tvb</code> again?</p><p><strong>Edit</strong>: I know the <code>tree</code> is valid since the line in question is inside <code>if(tree) {...}</code>. In this case, is it even possible to examine the <code>fvalue_t</code> inside <code>item-&gt;finfo</code>? Alternatively, can I use the header field to extract the field value directly, rather than adding it to the tree first?</p><p><strong>Edit</strong>: I've managed to track down the assetion that is failing, and it confuses me more. In <code>fvalue_get_uinteger</code> in <code>epan/ftypes/ftypes.c</code>:</p><pre><code>guint32
fvalue_get_uinteger(fvalue_t *fv)
{
    g_assert(fv-&gt;ftype-&gt;get_value_uinteger);
    return fv-&gt;ftype-&gt;get_value_uinteger(fv);
}</code></pre><p>When control reaches this from my dissector, <code>fv-&gt;ftype-&gt;get_value_uinteger</code> is <code>0x0</code>, and <code>fv-&gt;ftype</code> seems to be a <code>FT_PROTOCOL</code> --except that the field, <code>hf_pfield</code>, indexes a <code>FT_UINT32</code> field. Can anyone explain why the <code>proto_item</code> does not seem to hold the correct value type?</p><p><strong>Edit Again</strong>: I have stepped through the entire dissection process for a single packet of my protocol. It turns out that the first time the line is reached (during the second pass, when <code>tree</code> is not <code>NULL</code>), <code>p_item-&gt;finfo</code> is correctly a <code>FT_UINT32</code>, and the correct value is, indeed, extracted. However, on the next pass (anyone know where I can find out what each pass is --I thought there were only two?), it is <code>FT_PROTOCOL</code>. It does not appear that I have overstepped any buffers, since <em>all</em> of the interceding canary checks come out just fine. It also does not appear that <code>hf_pfield</code> has been invalidated or corrupted, as it has the same value as during the first two passes. Can anyone shed some light on this for me?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-ftypes" rel="tag" title="see questions tagged &#39;ftypes&#39;">ftypes</span> <span class="post-tag tag-link-proto_item" rel="tag" title="see questions tagged &#39;proto_item&#39;">proto_item</span> <span class="post-tag tag-link-proto_tree" rel="tag" title="see questions tagged &#39;proto_tree&#39;">proto_tree</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Nov '11, 15:57</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Nov '11, 14:08</strong> </span></p></div></div><div id="comments-container-7225" class="comments-container"></div><div id="comment-tools-7225" class="comment-tools"></div><div class="clear"></div><div id="comment-7225-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7330"></span>

<div id="answer-container-7330" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7330-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7330-score" class="post-score" title="current number of votes">1</div><span id="post-7330-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>While I am still a little confused, I have found a fairly reasonable workaround for now.</p><pre><code>if(tree)
{
    if(item-&gt;finfo-&gt;value.ftype-&gt;get_value_uinteger)
    {
        guint32_value = fvalue_get_uinteger(&amp;(item-&gt;finfo-&gt;value));
        /* Do work with value */
    }
}</code></pre><p>This appears to work, but I am still confused about why the <code>ftype</code> is different than what it is declared as sometimes. I think it would stand to reason that if a header field is registered as <code>FT_UINT32</code> that I should be able to safely get a <code>uinteger</code> value from any <code>proto_item</code> for that field.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '11, 11:09</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-7330" class="comments-container"></div><div id="comment-tools-7330" class="comment-tools"></div><div class="clear"></div><div id="comment-7330-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7227"></span>

<div id="answer-container-7227" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7227-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7227-score" class="post-score" title="current number of votes">0</div><span id="post-7227-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is no guarantee that there <em>is</em> an item! If the <code>tree</code> argument to <code>dissect_proto()</code> is null, no protocol tree will be constructed, hence no item from the tree.</p><p>Unfortunately, there's no good idiom for that other than extracting it from the <code>tvbuff</code> again. Perhaps there should be <code>ptvcursor_add_and_return_uint()</code>, <code>ptvcursor_add_and_return_ipv4()</code>, <code>ptvcursor_add_and_return_string()</code> and so on, which return the item value through a pointer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Nov '11, 18:08</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-7227" class="comments-container"><span id="7237"></span><div id="comment-7237" class="comment"><div id="post-7237-score" class="comment-score"></div><div class="comment-text"><p>You are correct, although I should have said that the lines in question are within an <code>if(tree) { ... }</code> block. I'll update my question.</p></div><div id="comment-7237-info" class="comment-info"><span class="comment-age">(04 Nov '11, 06:08)</span> <span class="comment-user userinfo">multipleinte...</span></div></div></div><div id="comment-tools-7227" class="comment-tools"></div><div class="clear"></div><div id="comment-7227-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

