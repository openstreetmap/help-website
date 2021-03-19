+++
type = "question"
title = "Wireshark crashes upon clicking on fields of expanded trees"
description = '''In 1.8.5, for custom Wimax-btsbts interface, wireshark crashes upon clicking on any of the field. Help.'''
date = "2013-09-27T02:28:00Z"
lastmod = "2013-09-27T05:29:00Z"
weight = 25304
keywords = [ "crash" ]
aliases = [ "/questions/25304" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark crashes upon clicking on fields of expanded trees](/questions/25304/wireshark-crashes-upon-clicking-on-fields-of-expanded-trees)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25304-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25304-score" class="post-score" title="current number of votes">0</div><span id="post-25304-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In 1.8.5, for custom Wimax-btsbts interface, wireshark crashes upon clicking on any of the field. Help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-crash" rel="tag" title="see questions tagged &#39;crash&#39;">crash</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Sep '13, 02:28</strong></p><img src="https://secure.gravatar.com/avatar/dd64de546bcf7652a4faed163ff02df0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sunshine&#39;s gravatar image" /><p><span>sunshine</span><br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sunshine has no accepted answers">0%</span></p></div></div><div id="comments-container-25304" class="comments-container"><span id="25306"></span><div id="comment-25306" class="comment"><div id="post-25306-score" class="comment-score"></div><div class="comment-text"><p>Can we have crash message ?</p></div><div id="comment-25306-info" class="comment-info"><span class="comment-age">(27 Sep '13, 03:13)</span> <span class="comment-user userinfo">Afrim</span></div></div><span id="25307"></span><div id="comment-25307" class="comment"><div id="post-25307-score" class="comment-score"></div><div class="comment-text"><p>Upon debugging through Visual C++,following error msg is dispalyed :</p><p>"Unhandled exception at 0x77c478ac in wireshark.exe: 0xC0000005: Access violation reading location 0x00000003."</p><p>Call stack location is somewhere in msvcrt.dll</p></div><div id="comment-25307-info" class="comment-info"><span class="comment-age">(27 Sep '13, 03:55)</span> <span class="comment-user userinfo">sunshine</span></div></div><span id="25308"></span><div id="comment-25308" class="comment"><div id="post-25308-score" class="comment-score"></div><div class="comment-text"><p><em>custom Wimax-btsbts interface</em> is it crashing when clicking fields dissected by the custom disector or any field? If the former it's probably a bug in the custom dissector. Probably something with the ett variables.</p></div><div id="comment-25308-info" class="comment-info"><span class="comment-age">(27 Sep '13, 04:03)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="25309"></span><div id="comment-25309" class="comment"><div id="post-25309-score" class="comment-score"></div><div class="comment-text"><p>Crashing occurs only upon clicking on the fields dissected by custom-dissector. I did check the ett variables thing, couldnt find any issue.</p></div><div id="comment-25309-info" class="comment-info"><span class="comment-age">(27 Sep '13, 04:27)</span> <span class="comment-user userinfo">sunshine</span></div></div><span id="25310"></span><div id="comment-25310" class="comment"><div id="post-25310-score" class="comment-score"></div><div class="comment-text"><p>Can you show us the code where you create the sub tree?</p></div><div id="comment-25310-info" class="comment-info"><span class="comment-age">(27 Sep '13, 04:30)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="25311"></span><div id="comment-25311" class="comment not_top_scorer"><div id="post-25311-score" class="comment-score"></div><div class="comment-text"><p>ti = proto_tree_add_protocol_format(ptree, proto_btsBts, tvb, offset, -1, "btsBts"); btsbts_tree = proto_item_add_subtree(ti, ett_btsbts_eap);</p><pre><code>//initialize btsbts_tree

//20130514 changed 0 to offset
msg_type = tvb_get_guint8(tvb, offset);

if (msg_type == M_LM_LVC_REQ || msg_type == M_LM_LVC_RSP || msg_type == M_LM_LCC_REQ || msg_type == M_LM_LCC_RSP )
{
if(check_col(pinfo-&gt;cinfo,COL_INFO))
{
col_clear(pinfo-&gt;cinfo,COL_INFO);

        col_add_fstr(pinfo-&gt;cinfo, COL_INFO, &quot;0x%x, %s, &quot;, msg_type,
            val_to_str(msg_type, msg_type_vals, &quot;Unknown (0x%04x)&quot;));

        col_set_fence(pinfo-&gt;cinfo, COL_INFO);
    }

    proto_tree_add_uint_format(btsbts_tree, hf_btsbts_msg_type, tvb, offset, 1, msg_type,
        &quot;messagetype: 0x%02X - %s&quot;, msg_type, val_to_str(msg_type, msg_type_vals, &quot;Unknown Message Type&quot;));

    offset++;

    switch (msg_type) 
    {
    case M_LM_LVC_REQ:
        proto_tree_add_item(btsbts_tree, hf_btsbts_client_btsid, tvb, offset, 6, FALSE );
        offset += 6;
        proto_tree_add_item(btsbts_tree, hf_btsbts_new_link_vers, tvb, offset, 4, FALSE );
        offset += 4;
        proto_tree_add_item(btsbts_tree, hf_btsbts_old_link_vers, tvb, offset, 4, FALSE );
        offset += 4;
        proto_tree_add_item(btsbts_tree, hf_btsbts_expected_server_btsid, tvb, offset, 8, FALSE );
        offset += 8;
        break;</code></pre></div><div id="comment-25311-info" class="comment-info"><span class="comment-age">(27 Sep '13, 04:36)</span> <span class="comment-user userinfo">sunshine</span></div></div><span id="25313"></span><div id="comment-25313" class="comment not_top_scorer"><div id="post-25313-score" class="comment-score"></div><div class="comment-text"><p>Try with if (tree) { ti = proto_tree_add_protocol_format(ptree, proto_btsBts, tvb, offset, -1, "btsBts"); btsbts_tree = proto_item_add_subtree(ti, ett_btsbts_eap); }</p><p>EDIT: You can try to debug your code and see where exactly the crash occur. Can we have more information about variables ? (ett, hf)</p></div><div id="comment-25313-info" class="comment-info"><span class="comment-age">(27 Sep '13, 05:29)</span> <span class="comment-user userinfo">Afrim</span></div></div></div><div id="comment-tools-25304" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-25304-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

