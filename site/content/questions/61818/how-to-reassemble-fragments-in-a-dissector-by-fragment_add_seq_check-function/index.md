+++
type = "question"
title = "How to Reassemble fragments in a dissector by fragment_add_seq_check function"
description = '''hi, i have a protocol that is layered on top of UDP that splits up its own data stream. If a packet is bigger than some given size, it will be split into chunks. A flag byte that signals the presence of a multi-packet sequence and also the last packet, followed by an ID of the sequence and a packet ...'''
date = "2017-06-07T00:01:00Z"
lastmod = "2017-06-14T11:04:00Z"
weight = 61818
keywords = [ "fragment_add", "reassembly" ]
aliases = [ "/questions/61818" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to Reassemble fragments in a dissector by fragment\_add\_seq\_check function](/questions/61818/how-to-reassemble-fragments-in-a-dissector-by-fragment_add_seq_check-function)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61818-score" class="post-score" title="current number of votes">1</div><span id="post-61818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi, i have a protocol that is layered on top of UDP that splits up its own data stream. If a packet is bigger than some given size, it will be split into chunks. A flag byte that signals the presence of a multi-packet sequence and also the last packet, followed by an ID of the sequence and a packet sequence number. i do step by step like <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChDissectReassemble.html">1</a> but, the fragment_add_seq_check function always return 0. what is the problem? can any one help me? anything should be added to this example for reassemble correctly? my code is here:</p><pre><code>    #include &quot;epan/packet.h&quot;
    #include &quot;epan/reassemble.h&quot;
    #define FOO_PORT 1234
    static int proto_foo = -1;
    static int hf_foo_fragmentation = -1;
    static int hf_foo_morefrag = -1;
    static int hf_foo_sequenceno = -1;
    static int hf_foo_sequenceid = -1;
    static reassembly_table msg_reassembly_table;
    static gint ett_foo = -1;
    static int hf_msg_fragments = -1;
    static int hf_msg_fragment = -1;
    static int hf_msg_fragment_overlap = -1;
    static int hf_msg_fragment_overlap_conflicts = -1;
    static int hf_msg_fragment_multiple_tails = -1;
    static int hf_msg_fragment_too_long_fragment = -1;
    static int hf_msg_fragment_error = -1;
    static int hf_msg_fragment_count = -1;
    static int hf_msg_reassembled_in = -1;
    static int hf_msg_reassembled_length = -1;
    static int hf_msg_reassembled_data=-1;
    static gint ett_msg_fragment = -1;
    static gint ett_msg_fragments = -1;
    static const fragment_items msg_frag_items = {
        /* Fragment subtrees */
        &amp;ett_msg_fragment,
        &amp;ett_msg_fragments,
        /* Fragment fields */
        &amp;hf_msg_fragments,
        &amp;hf_msg_fragment,
        &amp;hf_msg_fragment_overlap,
        &amp;hf_msg_fragment_overlap_conflicts,
        &amp;hf_msg_fragment_multiple_tails,
        &amp;hf_msg_fragment_too_long_fragment,
        &amp;hf_msg_fragment_error,
        &amp;hf_msg_fragment_count,
        &amp;hf_msg_reassembled_in,
        /* Reassembled length field */
        &amp;hf_msg_reassembled_length,
        &amp;hf_msg_reassembled_data,
        &quot;Message fragments&quot;
    };
    static int
    dissect_foo(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree, void *data _U_)
    {
    gint offset = 0;
        col_set_str(pinfo-&gt;cinfo, COL_PROTOCOL, &quot;FOO&quot;);
        col_clear(pinfo-&gt;cinfo,COL_INFO);
        proto_item *ti = proto_tree_add_item(tree, proto_foo, tvb, 0, -1, ENC_NA);
        proto_tree *foo_tree = proto_item_add_subtree(ti, ett_foo);
        guint8 fragmentation=tvb_get_guint8(tvb,offset);
        proto_tree_add_item(foo_tree, hf_foo_fragmentation, tvb, offset, 1, ENC_BIG_ENDIAN);
        offset += 1;
        guint8 morefrag=tvb_get_guint8(tvb,offset);
        proto_tree_add_item(foo_tree, hf_foo_morefrag, tvb, offset, 1, ENC_BIG_ENDIAN);
        offset += 1;
        guint8 sequenceno=tvb_get_guint8(tvb,offset);
        proto_tree_add_item(foo_tree, hf_foo_sequenceno, tvb, offset, 1, ENC_BIG_ENDIAN);
        offset += 1;
        guint8 sequenceid=tvb_get_guint8(tvb,offset);
        proto_tree_add_item(foo_tree, hf_foo_sequenceid, tvb, offset, 1, ENC_BIG_ENDIAN);
        offset += 1;
    gboolean save_fragmented = pinfo-&gt;fragmented;
    tvbuff_t *next_tvb;
    if (fragmentation) 
    {       tvbuff_t* new_tvb = NULL;
        fragment_head *frag_msg = NULL;
        pinfo-&gt;fragmented = TRUE;
        frag_msg = fragment_add_seq_check(&amp;msg_reassembly_table,
            tvb, offset, pinfo,
            sequenceid, NULL, 
            sequenceno, 
            tvb_captured_length_remaining(tvb, offset),
            morefrag);
            new_tvb = process_reassembled_data(tvb, offset, pinfo,
            &quot;Reassembled Message&quot;, frag_msg, &amp;msg_frag_items,
            NULL, foo_tree);
        if (frag_msg) { /* Reassembled */
            col_append_str(pinfo-&gt;cinfo, COL_INFO,
                    &quot; (Message Reassembled)&quot;);
        } else { /* Not last packet of reassembled Short Message */
            col_append_fstr(pinfo-&gt;cinfo, COL_INFO,
                    &quot; (Message fragment %u)&quot;, foo_tree);
        }
        if (new_tvb) { /* take it all */
            next_tvb = new_tvb;
        } else { /* make a new subset */
            next_tvb = tvb_new_subset_remaining(tvb, offset);
        }
    }
    else { /* Not fragmented */
        next_tvb = tvb_new_subset_remaining(tvb, offset);
    }
    pinfo-&gt;fragmented = save_fragmented;
        return tvb_captured_length(tvb);
    }
    void
    proto_register_foo(void)
    {
        static hf_register_info hf[] = {
                { &amp;hf_foo_fragmentation,
                { &quot;FOO PDU Fragmentation&quot;, &quot;foo.fragmentation&quot;,
                FT_UINT8, BASE_HEX,
                NULL, 0x0,
                NULL, HFILL }
            },

               { &amp;hf_foo_morefrag,
                { &quot;FOO PDU MoreFrag&quot;, &quot;foo.more.frag&quot;,
                FT_UINT8, BASE_HEX,
                NULL, 0x0,
                NULL, HFILL }
            },

            { &amp;hf_foo_sequenceno,
                { &quot;FOO PDU Sequence Number&quot;, &quot;foo.seqn&quot;,
                FT_UINT8, BASE_DEC,
                NULL, 0x0,
                NULL, HFILL }
            },

                { &amp;hf_foo_sequenceid,
                { &quot;FOO PDU Sequence ID&quot;, &quot;foo.seqn.id&quot;,
                FT_UINT8, BASE_DEC,
                NULL, 0x0,
                NULL, HFILL }
            },
            {&amp;hf_msg_fragments,
        {&quot;Message fragments&quot;, &quot;msg.fragments&quot;,
        FT_NONE, BASE_NONE, NULL, 0x00, NULL, HFILL } },
    {&amp;hf_msg_fragment,
        {&quot;Message fragment&quot;, &quot;msg.fragment&quot;,
        FT_FRAMENUM, BASE_NONE, NULL, 0x00, NULL, HFILL } },
    {&amp;hf_msg_fragment_overlap,
        {&quot;Message fragment overlap&quot;, &quot;msg.fragment.overlap&quot;,
        FT_BOOLEAN, 0, NULL, 0x00, NULL, HFILL } },
    {&amp;hf_msg_fragment_overlap_conflicts,
        {&quot;Message fragment overlapping with conflicting data&quot;,
        &quot;msg.fragment.overlap.conflicts&quot;,
        FT_BOOLEAN, 0, NULL, 0x00, NULL, HFILL } },
    {&amp;hf_msg_fragment_multiple_tails,
        {&quot;Message has multiple tail fragments&quot;,
        &quot;msg.fragment.multiple_tails&quot;,
        FT_BOOLEAN, 0, NULL, 0x00, NULL, HFILL } },
    {&amp;hf_msg_fragment_too_long_fragment,
        {&quot;Message fragment too long&quot;, &quot;msg.fragment.too_long_fragment&quot;,
        FT_BOOLEAN, 0, NULL, 0x00, NULL, HFILL } },
    {&amp;hf_msg_fragment_error,
        {&quot;Message defragmentation error&quot;, &quot;msg.fragment.error&quot;,
        FT_FRAMENUM, BASE_NONE, NULL, 0x00, NULL, HFILL } },
    {&amp;hf_msg_fragment_count,
        {&quot;Message fragment count&quot;, &quot;msg.fragment.count&quot;,
        FT_UINT32, BASE_DEC, NULL, 0x00, NULL, HFILL } },
    {&amp;hf_msg_reassembled_in,
        {&quot;Reassembled in&quot;, &quot;msg.reassembled.in&quot;,
        FT_FRAMENUM, BASE_NONE, NULL, 0x00, NULL, HFILL } },
    {&amp;hf_msg_reassembled_length,
        {&quot;Reassembled length&quot;, &quot;msg.reassembled.length&quot;,
        FT_UINT32, BASE_DEC, NULL, 0x00, NULL, HFILL } },
    { &amp;hf_msg_reassembled_data,
            { &quot;Reassembled FOO Data&quot;, &quot;foo.reassembled.data&quot;, FT_BYTES, BASE_NONE, NULL, 0x0,
                &quot;The reassembled payload&quot;, HFILL }},


        };
        /* Setup protocol subtree array */
        static gint *ett[] = {
            &amp;ett_foo,
            &amp;ett_msg_fragment,
            &amp;ett_msg_fragments
        };

        proto_foo = proto_register_protocol (
            &quot;FOO Protocol&quot;, /* name       */
            &quot;FOO&quot;,      /* short name */
            &quot;foo&quot;       /* abbrev     */
            );
       proto_register_field_array(proto_foo, hf, array_length(hf));
        proto_register_subtree_array(ett, array_length(ett));


        reassembly_table_register(&amp;msg_reassembly_table,
            &amp;addresses_ports_reassembly_table_functions);

    }
    void
    proto_reg_handoff_foo(void)
    {
        static dissector_handle_t foo_handle;

        foo_handle = create_dissector_handle(dissect_foo, proto_foo);
        dissector_add_uint(&quot;udp.port&quot;, FOO_PORT, foo_handle);
    }</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fragment_add" rel="tag" title="see questions tagged &#39;fragment_add&#39;">fragment_add</span> <span class="post-tag tag-link-reassembly" rel="tag" title="see questions tagged &#39;reassembly&#39;">reassembly</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jun '17, 00:01</strong></p><img src="https://secure.gravatar.com/avatar/0b6bdfea45d7093830a2a0638a758239?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hhw&#39;s gravatar image" /><p><span>hhw</span><br />
<span class="score" title="10 reputation points">10</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hhw has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Jun '17, 16:54</strong> </span></p></div></div><div id="comments-container-61818" class="comments-container"><span id="61853"></span><div id="comment-61853" class="comment"><div id="post-61853-score" class="comment-score">2</div><div class="comment-text"><p>It would be useful to know how <code>fragment_add_seq_check()</code> is being called. In particular it would be useful to know what the values of the following parameters are for each call up to the final fragment (i.e., when reassembly should complete):</p><ul><li><code>id</code></li><li><code>frag_number</code></li><li><code>more_frags</code></li></ul><p>IIRC you really want to see something like:</p><ol><li>id=x,frag_number=0,more_frags=1</li><li>id=x,frag_number=1,more_frags=1</li><li>id=x,frag_number=2,more_frags=0 &lt;-- this should complete reassembly</li></ol></div><div id="comment-61853-info" class="comment-info"><span class="comment-age">(07 Jun '17, 19:02)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="61958"></span><div id="comment-61958" class="comment"><div id="post-61958-score" class="comment-score">2</div><div class="comment-text"><p>What is the value of morefrag when there are more fragments?</p></div><div id="comment-61958-info" class="comment-info"><span class="comment-age">(12 Jun '17, 12:51)</span> <span class="comment-user userinfo">jpetersen</span></div></div><span id="61974"></span><div id="comment-61974" class="comment"><div id="post-61974-score" class="comment-score"></div><div class="comment-text"><p>morefrag when there are more fragments is 1. if i have 3 packet the values are :</p><blockquote><p>id=10,frag_number=1,more_frags=1</p><p>id=10,frag_number=2,more_frags=1</p><p>id=10,frag_number=3,more_frags=0 (&lt;-- this should complete reassembly)</p></blockquote></div><div id="comment-61974-info" class="comment-info"><span class="comment-age">(12 Jun '17, 23:59)</span> <span class="comment-user userinfo">hhw</span></div></div></div><div id="comment-tools-61818" class="comment-tools"></div><div class="clear"></div><div id="comment-61818-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61982"></span>

<div id="answer-container-61982" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61982-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61982-score" class="post-score" title="current number of votes">1</div><span id="post-61982-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hhw has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>[What happened to the earlier comment that had the more_frag output? It seems to have disappeared...]</p><p>Anyway, I missed this earlier, but just now I noticed that your frag_number starts at 1. According to the docs for <code>fragment_add_seq()</code>:</p><pre><code>/*
 * Like fragment_add, but fragments have a block sequence number starting from
 * zero (for the first fragment of each datagram). This differs from
 * fragment_add for which the fragment may start at any offset.</code></pre><p>where <code>fragment_add_seq_check()</code> (which is what you're using) says:</p><pre><code>/*
 * Like fragment_add_seq, but maintains a table for completed reassemblies
 * just like fragment_add_check.</code></pre><p>IOW I think you either need to subtract one from your frag_numbers (so they start at 0) or you need to use <code>fragment_add_check()</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '17, 06:11</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-61982" class="comments-container"><span id="61998"></span><div id="comment-61998" class="comment"><div id="post-61998-score" class="comment-score"></div><div class="comment-text"><p>ok, thank you very much, my fragment may start at any offset so i can't subtract one from frag_numbers, i use <code>fragment_add_check()</code>, but it doesn't work. can you help me.</p><pre><code>id=10,frag_number=10,more_frags=1
id=10,frag_number=11,more_frags=1
id=10,frag_number=12,more_frags=0 (&lt;-- this should complete reassembly)</code></pre></div><div id="comment-61998-info" class="comment-info"><span class="comment-age">(14 Jun '17, 01:09)</span> <span class="comment-user userinfo">hhw</span></div></div><span id="62029"></span><div id="comment-62029" class="comment"><div id="post-62029-score" class="comment-score"></div><div class="comment-text"><p>please look at (<a href="https://ask.wireshark.org/questions/62028/difference-between-fragment_add_check-and-fragment_add_seq_check)">https://ask.wireshark.org/questions/62028/difference-between-fragment_add_check-and-fragment_add_seq_check)</a> to understand my problem</p></div><div id="comment-62029-info" class="comment-info"><span class="comment-age">(14 Jun '17, 11:04)</span> <span class="comment-user userinfo">hhw</span></div></div></div><div id="comment-tools-61982" class="comment-tools"></div><div class="clear"></div><div id="comment-61982-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

