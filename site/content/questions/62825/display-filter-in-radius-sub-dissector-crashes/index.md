+++
type = "question"
title = "display filter in RADIUS sub-dissector crashes"
description = '''Hi, I am working on proprietary RADIUS protocol dissection. I have created 3 sub-dissectors within wireshark which are called from packet-radius.c I want to add one custom display filter in sub-dissector. I am using call_dissector_with_data API in dissect_radius to call my sub-dissector. I am passin...'''
date = "2017-07-17T07:07:00Z"
lastmod = "2017-08-03T05:05:00Z"
weight = 62825
keywords = [ "subdissector", "radius", "display-filter" ]
aliases = [ "/questions/62825" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [display filter in RADIUS sub-dissector crashes](/questions/62825/display-filter-in-radius-sub-dissector-crashes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62825-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am working on proprietary RADIUS protocol dissection. I have created 3 sub-dissectors within wireshark which are called from packet-radius.c</p><p>I want to add one custom display filter in sub-dissector.</p><p>I am using <code>call_dissector_with_data</code> API in <code>dissect_radius</code> to call my sub-dissector. I am passing tree pointer in this API.</p><p>When I use <code>proto_tree_add_uint</code> API by passing this tree pointer and appropriate 32-bit value, wireshark is getting crashed with an error message,</p><pre><code>Unhandled exception at 0x00007FF94DED4B07 (libwireshark.dll) in Wireshark.exe: 0xC0000005: Access violation reading location 0xFFFFFFFFFFFFFFFF.</code></pre><p>In packet-radius.c,</p><pre><code>rad_handle = find_dissector(&quot;radius_display&quot;);

if (rad_handle ) {

    /* Call to sub-dissector */
    call_dissector_with_data(rad_handle , tvb, pinfo, tree, NULL);
}</code></pre><p>In packet-radius-display.c,</p><pre><code>static int hf_radius_resp_time = -1;

dissect_radius_display(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree, void *data _U_)
{
    guint32 resptime = 0;
    proto_item *item;

    resptime = calc_resp_time(pinfo); // custom function to calculate response time

        if (tree) {

        item = proto_tree_add_uint(tree, hf_radius_resp_time, NULL, 0, 0, resptime);
        PROTO_ITEM_SET_HIDDEN(item);
    }
}

void proto_register_radius_display(void)
{
    int proto_radius_display = -1;

    hf_register_info hf[] = {
        { &amp;hf_radius_resp_time,
        { &quot;Response Time&quot;, &quot;radius.resptime&quot;, FT_UINT32, BASE_DEC, NULL, 0,
        &quot;The time between the request and the response, in ms&quot;, HFILL } }
    };

    proto_radius_display = proto_register_protocol(&quot;RADIUS Protocol Display&quot;, &quot;RADIUS Display&quot;, &quot;radius_display&quot;);

    proto_register_field_array(proto_radius_display, hf, array_length(hf));

    register_dissector(&quot;radius_display&quot;, dissect_radius_display, proto_radius_display);
}</code></pre></div><div id="question-tags" class="tags-container tags">subdissector radius display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jul '17, 07:07</strong></p><img src="https://secure.gravatar.com/avatar/fd87937fa1e60718c6ab880174ea3539?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mehul28&#39;s gravatar image" /><p>Mehul28<br />
<span class="score" title="0 reputation points">0</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mehul28 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Jul '17, 22:45</p></div></div><div id="comments-container-62825" class="comments-container"><span id="62829"></span><div id="comment-62829" class="comment"><div id="post-62829-score" class="comment-score"></div><div class="comment-text"><p>We need to see an abstract of your code to see what's wrong.</p></div><div id="comment-62829-info" class="comment-info"><span class="comment-age">(17 Jul '17, 11:47)</span> Anders ♦</div></div><span id="62832"></span><div id="comment-62832" class="comment"><div id="post-62832-score" class="comment-score"></div><div class="comment-text"><p>Ok. I have added the code snippet.</p></div><div id="comment-62832-info" class="comment-info"><span class="comment-age">(17 Jul '17, 22:46)</span> Mehul28</div></div><span id="62967"></span><div id="comment-62967" class="comment"><div id="post-62967-score" class="comment-score"></div><div class="comment-text"><p>Sure it's not crashing in calc_resp_time() ?</p></div><div id="comment-62967-info" class="comment-info"><span class="comment-age">(21 Jul '17, 02:27)</span> Anders ♦</div></div><span id="62968"></span><div id="comment-62968" class="comment"><div id="post-62968-score" class="comment-score"></div><div class="comment-text"><p>No. calc_resp_time is a function which simply does some arithmetic operation. Wireshark is getting crashed on proto_tree_add_uint call...</p></div><div id="comment-62968-info" class="comment-info"><span class="comment-age">(21 Jul '17, 02:41)</span> Mehul28</div></div><span id="62993"></span><div id="comment-62993" class="comment"><div id="post-62993-score" class="comment-score"></div><div class="comment-text"><p>So if you know that it's crashing in <code>proto_tree_add_uint()</code>, you have a stack trace showing <code>proto_tree_add_uint()</code>; what does the stack trace say?</p></div><div id="comment-62993-info" class="comment-info"><span class="comment-age">(21 Jul '17, 21:49)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-62825" class="comment-tools"></div><div class="clear"></div><div id="comment-62825-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="62834"></span>

<div id="answer-container-62834" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62834-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>proto_tree_add_uint() may not be used with tvb = NULL and length = 0 from what I can see.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jul '17, 02:02</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-62834" class="comments-container"><span id="62835"></span><div id="comment-62835" class="comment"><div id="post-62835-score" class="comment-score"></div><div class="comment-text"><p>One can use this, for just developing display filter. There are other packet dissections which have done the same in wireshark.</p><p>The following code works,</p><pre><code>   item = proto_tree_add_uint(tree, hf_radius_resp_time, NULL, 0, 0, resptime);
   PROTO_ITEM_SET_HIDDEN(item)</code></pre><p>whien I insert it in dissect_radius function of packet-radius.c</p></div><div id="comment-62835-info" class="comment-info"><span class="comment-age">(18 Jul '17, 02:08)</span> Mehul28</div></div><span id="62959"></span><div id="comment-62959" class="comment"><div id="post-62959-score" class="comment-score"></div><div class="comment-text"><p>I don't know why it's getting crashed when I use the proto_tree_add_uint API with radius_tree in my sub-dissector?</p></div><div id="comment-62959-info" class="comment-info"><span class="comment-age">(21 Jul '17, 01:53)</span> Mehul28</div></div><span id="62963"></span><div id="comment-62963" class="comment"><div id="post-62963-score" class="comment-score"></div><div class="comment-text"><p>What does your debugger say?</p></div><div id="comment-62963-info" class="comment-info"><span class="comment-age">(21 Jul '17, 02:19)</span> Jaap ♦</div></div><span id="62970"></span><div id="comment-62970" class="comment"><div id="post-62970-score" class="comment-score"></div><div class="comment-text"><p>Access violation reading location 0xFFFFFFFFFFFFFFFF.</p></div><div id="comment-62970-info" class="comment-info"><span class="comment-age">(21 Jul '17, 02:42)</span> Mehul28</div></div><span id="62982"></span><div id="comment-62982" class="comment"><div id="post-62982-score" class="comment-score"></div><div class="comment-text"><p>That looks like a -1 to me, are you absolutely sure that <code>hf_radius_resp_time</code> is being initialised by <code>proto_register_radius_display()</code>? Is the latter being called?</p><p>Also, <code>int proto_radius_display = -1;</code> should really be a <code>static int int proto_radius_display = -1;</code> at file level, not in <code>proto_register_radius_display()</code>.</p></div><div id="comment-62982-info" class="comment-info"><span class="comment-age">(21 Jul '17, 08:24)</span> grahamb ♦</div></div><span id="62991"></span><div id="comment-62991" class="comment not_top_scorer"><div id="post-62991-score" class="comment-score"></div><div class="comment-text"><blockquote><p>proto_tree_add_uint() may not be used with tvb = NULL and length = 0 from what I can see.</p></blockquote><p>If you're referring to the line</p><pre><code>DISSECTOR_ASSERT(tvb != NULL || *length == 0);</code></pre><p>in <code>get_hfi_length()</code>, that says that it may not be used with tvb = NULL and length <em>not</em> equal to 0; a null tvb pointer is ok <em>IF</em> the length is 0.</p><p>So</p><pre><code>item = proto_tree_add_uint(tree, hf_radius_resp_time, NULL, 0, 0, resptime);</code></pre><p>shouldn't crash with <em>that</em> assertion failure.</p></div><div id="comment-62991-info" class="comment-info"><span class="comment-age">(21 Jul '17, 21:36)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-62834" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-62834-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="63371"></span>

<div id="answer-container-63371" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63371-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>This is resolved by registering filter variable hf_radius_resp_time using wmem and epan_scope.</p><pre><code>hf = wmem_array_new(wmem_epan_scope(), sizeof(hf_register_info));</code></pre><p>Previously, I was registering it statically.</p><p>Thanks</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '17, 05:05</strong></p><img src="https://secure.gravatar.com/avatar/fd87937fa1e60718c6ab880174ea3539?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mehul28&#39;s gravatar image" /><p>Mehul28<br />
<span class="score" title="0 reputation points">0</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mehul28 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Aug '17, 05:06</p></div></div><div id="comments-container-63371" class="comments-container"><span id="63384"></span><div id="comment-63384" class="comment"><div id="post-63384-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/24633/mehul28">@Mehul28</a>, this site has a mechanism of marking questions as usefully answered. If an Answer has usefully answered a Question, the author of the Question (and nobody else) has the possibility to mark it as the correct answer by clicking the checkmark icon next to it. By doing so you change the colour of the Question in the list to green, indicating it as usefully answered to others. There is nothing wrong about marking your own Answer as the correct one.</p></div><div id="comment-63384-info" class="comment-info"><span class="comment-age">(03 Aug '17, 06:12)</span> sindy</div></div><span id="63387"></span><div id="comment-63387" class="comment"><div id="post-63387-score" class="comment-score"></div><div class="comment-text"><blockquote><p>registering filter variable hf_radius_resp_time using wmem and epan_scope.</p></blockquote><p>Presumably you mean "<em>allocating</em> filter variable..." - you <em>register</em> it in the <code>proto_register_field_array()</code> call.</p><p>Are you modifying <code>hf</code> after you initialize it? If not, then it shouldn't matter where it's located in the address space, so it shouldn't matter whether you allocate it statically or dynamically.</p></div><div id="comment-63387-info" class="comment-info"><span class="comment-age">(03 Aug '17, 10:51)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-63371" class="comment-tools"></div><div class="clear"></div><div id="comment-63371-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

