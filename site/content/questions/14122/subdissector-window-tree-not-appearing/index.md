+++
type = "question"
title = "subdissector window tree not appearing"
description = '''Greetings, I have two protocols that are encapsulated like so: TCP or UDP -&amp;gt; proto1 -&amp;gt; proto2.  I have created a heuristic dissector for proto1 that is registered to TCP or UDP (my protocols can run over either). This works fine, and in the Wireshark GUI I see proto1 being dissected, with its ...'''
date = "2012-09-07T08:12:00Z"
lastmod = "2012-09-07T13:21:00Z"
weight = 14122
keywords = [ "tree", "subdissector", "sub-dissector" ]
aliases = [ "/questions/14122" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [subdissector window tree not appearing](/questions/14122/subdissector-window-tree-not-appearing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14122-score" class="post-score" title="current number of votes">0</div><span id="post-14122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings,</p><p>I have two protocols that are encapsulated like so: TCP or UDP -&gt; proto1 -&gt; proto2.<br />
</p><p>I have created a heuristic dissector for proto1 that is registered to TCP or UDP (my protocols can run over either). This works fine, and in the Wireshark GUI I see proto1 being dissected, with its tree information being populated appropriately. I then created a subdissector proto2, that is registered to proto1. Through the debug window I can see control being passed from proto1 to proto2 for an applicable packet, and furthermore, proto2 is updating the 'Protocol' field in the Wireshark GUI of its abbreviated protocol name. However, proto2's tree information is not showing up in the GUI.<br />
</p><p>Through debugging I have verified that the tree is being passed correctly from proto1 to proto2, that the applicable tree parameters inside proto2 are not NULL and do not have -1 values. I've even restructured proto2 to be a heuristic dissector for TCP or UDP and in this case, the tree information is present in the Wireshark GUI. My hypothesis is that I am missing something between the call to the subdissector, as in something isnt being saved or passed correctly. One concern I have is that proto2's abbreviated name is in the syntax proto_2 with the underscore, filenames, variable/method declarations all use the underscore for the protocols abbreviation - could this be an issue? (clearly I'm exhausted on ideas)<br />
Any help is appreciated.<br />
</p><p>Code Snippets:<br />
</p><pre><code>    PROTO1 CODE:
proto_register_proto1: 
    static hf_register_info hf[] = {
    ...
    { &amp;hf_proto1_prot_id,
        { &quot;Protocol Identifier&quot;, &quot;proto1.prot_id&quot;, FT_UINT16, BASE_HEX, VALS(0x1022), 0x0, 
        &quot;Protocol Identifier&quot;, HFILL } }
    ...
    };
    ...
    subdissector_table = register_dissector_table(&quot;proto1.prot_id&quot;, 
        &quot;Protocol Identifier&quot;, FT_UINT16, BASE_HEX);

dissect_proto1:
...

if (proto2_handoff){
    tvbuff_t *next_tvb;
gint len, reported_len;

len = tvb_length_remaining(tvb, 4);
reported_len = tvb_reported_length_remaining(tvb, PROTO1_HDR_LEN);
next_tvb = tvb_new_subset(tvb, PROTO1_HDR_LEN, len, reported_len);
    dissector_try_uint(subdissector_table, 0x1022, next_tvb, pinfo, tree);
}
...

PROTO2 CODE:
proto_reg_handoff_proto2:
...
ptoto2_handle = find_dissector(&quot;proto2&quot;);
dissector_add(&quot;proto1.prot_id&quot;, 0x1022, proto2_handle);
data_handle = find_dissector(&quot;data&quot;)
...
proto_register_proto2:
proto_proto2 = proto_register_protocol (&quot;PROTO2 Protocol&quot;, &quot;PROTO2&quot;, &quot;proto2&quot;);

proto_register_field_array(proto_proto2, hf_proto2, array_length (hf_proto2));
proto_register_subtree_array (ett_proto2, array_length (ett_proto2));
register_dissector(&quot;proto2&quot;, dissect_proto2, proto_proto2);
...
dissect_proto2:
if (check_col(pinfo-&gt;cinfo, COL_PROTOCOL))
    col_set_str(pinfo-&gt;cinfo, COL_PROTOCOL, PROTO_TAG_PROTO2); /* this works... */
if (tree) { /* we are being asked for details */
    guint32 offset = 0;
    guint32 length = 0;
/* through debugs I see control being passed here, tree != NULL and has the same value from when it was in proto1 */
proto2_item = proto_tree_add_item(tree, proto_proto2, tvb, 0, -1, FALSE);
    proto2_tree = proto_item_add_subtree(proto2_item, ett_proto2);
/* this appears to be the break, where these calls do not update the tree structure in the GUI */
}</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tree" rel="tag" title="see questions tagged &#39;tree&#39;">tree</span> <span class="post-tag tag-link-subdissector" rel="tag" title="see questions tagged &#39;subdissector&#39;">subdissector</span> <span class="post-tag tag-link-sub-dissector" rel="tag" title="see questions tagged &#39;sub-dissector&#39;">sub-dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Sep '12, 08:12</strong></p><img src="https://secure.gravatar.com/avatar/6a3f842d129da9eb3306c08fe798d456?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iggy114&#39;s gravatar image" /><p><span>iggy114</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iggy114 has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-14122" class="comments-container"></div><div id="comment-tools-14122" class="comment-tools"></div><div class="clear"></div><div id="comment-14122-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14124"></span>

<div id="answer-container-14124" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14124-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14124-score" class="post-score" title="current number of votes">0</div><span id="post-14124-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You might try some of the following changes:</p><p><code>dissect_proto1:</code></p><pre><code>if (proto2_handoff) {
    tvbuff_t *next_tvb;
    gint reported_len;

    /* Before calling proto2, verify reported_len &gt; 0.
       Also, be sure call_dissector() is not encapsulated within an if (tree) {...} block. */
    reported_len = tvb_reported_length_remaining(tvb, PROTO1_HDR_LEN);
    if (reported_len &gt; 0) {
        next_tvb = tvb_new_subset(tvb, PROTO1_HDR_LEN, -1, reported_len);
        call_dissector(proto2_handle, next_tvb, pinfo, tree);
    }  
}</code></pre><p><code>proto_register_proto1:</code></p><pre><code>/* Delete this:
subdissector_table = register_dissector_table(&quot;proto1.port_id&quot;, 
    &quot;Protocol Identifier&quot;, FT_UINT16, BASE_HEX);
*/</code></pre><p><code>proto_reg_handoff_proto1:</code></p><pre><code>proto2_handle = find_dissector(&quot;proto2&quot;);</code></pre><p><code>dissect_proto2:</code></p><pre><code>if (tree) {
    /* Change FALSE to ENC_NA */
    proto2_item = proto_tree_add_item(tree, proto_proto2, tvb, 0, -1, ENC_NA);
    proto2_tree = proto_item_add_subtree(proto2_item, ett_proto2);

    /* 
       Now add stuff to proto2_tree, favoring proto_tree_add_item() and avoiding 
       proto_tree_add_text() for the most part, but don&#39;t put stuff in here that isn&#39;t
       allowed to be encapsulated within the if (tree) {...} block.
       Refer to doc/README.developer skeleton code for more details ...
     */
}</code></pre><p><code>proto_reg_handoff_proto2:</code></p><pre><code>/* Delete all this:
   ptoto2_handle = find_dissector(&quot;proto2&quot;);
   dissector_add(&quot;proto1.prot_id&quot;, 0x1022, proto2_handle);
   data_handle = find_dissector(&quot;data&quot;)
*/</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '12, 11:32</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span> </br></br></p></div></div><div id="comments-container-14124" class="comments-container"><span id="14127"></span><div id="comment-14127" class="comment"><div id="post-14127-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your quick response.<br />
I've implemented the changes you've suggested but am getting the same results. I've even gone as far to add an item to the proto2 tree thinking that it wont print to screen unless its populated but this has failed to render the tree as well.<br />
Do you know if there is any legitimacy my concern over the naming syntax of proto2?<br />
One thing I've noticed through my debugging is that<br />
</p><pre><code>proto2_item = proto_tree_add_item(tree, proto_proto2, tvb, 0, -1, ENC_NA);</code></pre><p>seems to not always return the same structure for each packet. Sometimes it will, sometimes it won't - any concern here?</p></div><div id="comment-14127-info" class="comment-info"><span class="comment-age">(07 Sep '12, 12:56)</span> <span class="comment-user userinfo">iggy114</span></div></div><span id="14128"></span><div id="comment-14128" class="comment"><div id="post-14128-score" class="comment-score"></div><div class="comment-text"><p>The naming syntax of <code>proto2</code> should be fine, although on a somewhat related note, you might want to run your dissector through the <code>tools/checkfiltername.pl</code> script. Actually, you should run your dissector through all <code>tools/check*.pl</code> scripts.</p><p>How are you determining <code>if (proto2_handoff)</code>? Is it correct?</p><p>Does your proto1 happen to be over TCP? If so, look into using <code>dissect_pdus()</code> for TCP reassembly. You'll have to determine TCP vs. UDP, but there are examples for this. Temporarily, you might also want to change any <code>if (tree)</code> to <code>if (1)</code> to be sure <code>call_dissector()</code> isn't in one.</p></div><div id="comment-14128-info" class="comment-info"><span class="comment-age">(07 Sep '12, 13:17)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="14129"></span><div id="comment-14129" class="comment"><div id="post-14129-score" class="comment-score"></div><div class="comment-text"><p>If you still require further assistance, I'd recommend moving this discussion to the Wireshark developer's mailing list. As the <a href="http://ask.wireshark.org/faq/">FAQ</a> states, this is a Q&amp;A site, and not a discussion forum. I think the developer's mailing list would work better here.</p></div><div id="comment-14129-info" class="comment-info"><span class="comment-age">(07 Sep '12, 13:21)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-14124" class="comment-tools"></div><div class="clear"></div><div id="comment-14124-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

