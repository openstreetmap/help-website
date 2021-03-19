+++
type = "question"
title = "Can anyone help me on Reassembly of PDU"
description = ''' Hi Iam developing custom dissector. I have almost Finished everything except this reassembly. I could not understand realy. The basic Scenario is for reassembly is  create table   fragment_add_seq_next and process  process_reassembled_data .  But my reassembly not happening?? Can anyone tell me wha...'''
date = "2014-11-24T01:13:00Z"
lastmod = "2014-11-24T01:13:00Z"
weight = 38093
keywords = [ "reassemble" ]
aliases = [ "/questions/38093" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can anyone help me on Reassembly of PDU](/questions/38093/can-anyone-help-me-on-reassembly-of-pdu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38093-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/reassmbly_ayAiQMr.JPG" alt="alt text" /></p><p>Hi Iam developing custom dissector. I have almost Finished everything except this reassembly.</p><p>I could not understand realy. The basic Scenario is for reassembly is</p><p>create table fragment_add_seq_next and process process_reassembled_data .</p><p>But my reassembly not happening?? Can anyone tell me what i have left and why my code not showing reassembly?</p><p>static reassembly_table mine_reassembly_table;</p><pre><code>static int hf_mine_fragments = -1;
static int hf_mine_fragment = -1;
static int hf_mine_fragment_overlap = -1;
static int hf_mine_fragment_overlap_conflicts = -1;
static int hf_mine_fragment_multiple_tails = -1;
static int hf_mine_fragment_too_long_fragment = -1;
static int hf_mine_fragment_error = -1;
static int hf_mine_fragment_count = -1;
static int hf_mine_reassembled_in = -1;
static int hf_mine_reassembled_length = -1;

static gint ett_mine_fragment = -1;
static gint ett_mine_fragments = -1;

static const fragment_items mine_frag_items = {
/* Fragment subtrees */
&amp;ett_mine_fragment,
&amp;ett_mine_fragments,
/* Fragment fields */
&amp;hf_mine_fragments,
&amp;hf_mine_fragment,
&amp;hf_mine_fragment_overlap,
&amp;hf_mine_fragment_overlap_conflicts,
&amp;hf_mine_fragment_multiple_tails,
&amp;hf_mine_fragment_too_long_fragment,
&amp;hf_mine_fragment_error,
&amp;hf_mine_fragment_count,
/* Reassembled in field */
&amp;hf_mine_reassembled_in,
/* Reassembled length field */
&amp;hf_mine_reassembled_length,
/* Reassembled data field */
NULL,
/* Tag */
&quot;mine fragments&quot;
};

static void mine_init_protocol(void)
    {

        /* fragment_table_init(&amp;mine_fragment_table); */
        /* reassembled_table_init(&amp;mine_reassembled_table); */
        reassembly_table_init(&amp;mine_reassembly_table, &amp;addresses_reassembly_table_functions);
    }

save_fragmented = pinfo-&gt;fragmented;

pinfo-&gt;fragmented = TRUE;

mine_frag_msg = fragment_add_seq_next(&amp;mine_reassembly_table,next_tvb, offset_payload, pinfo, mine_seqid, NULL,
                                             reassebled_data_total_length, more_frags);

mine_tvb = process_reassembled_data( next_tvb, offset_payload, pinfo, &quot;Reassembled PDU&quot;, mine_frag_msg,
    &amp;mine_frag_items, NULL, FT_BCnPDU_tree );

reassebled_data_total_length =0;

proto_tree_add_text(FT_BCnPDU_tree, mine_tvb, offset_payload, 1, &quot; reassebled data &quot;);

ALSIGPDU(mine_tvb, pinfo, tree);</code></pre></div><div id="question-tags" class="tags-container tags">reassemble</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Nov '14, 01:13</strong></p><img src="https://secure.gravatar.com/avatar/1339589a92af9455063c09e56bfc6299?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="umar&#39;s gravatar image" /><p>umar<br />
<span class="score" title="26 reputation points">26</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="umar has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 24 Nov '14, 01:59</p></div></div><div id="comments-container-38093" class="comments-container"></div><div id="comment-tools-38093" class="comment-tools"></div><div class="clear"></div><div id="comment-38093-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

