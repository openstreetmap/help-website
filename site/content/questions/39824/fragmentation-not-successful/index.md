+++
type = "question"
title = "fragmentation not successful"
description = '''Why is my code below not working? The fragmentation itself not successful and thus reassembly not working. Please suggest! switch (stype) { case 0x00: // Continuation of Message  msg_seqid = 2;  rem_length = bctsdu_length;  proto_tree_add_text(FT_BCnPDU_tree, next_tvb, offset_payload, rem_length, &quot;P...'''
date = "2015-02-11T20:18:00Z"
lastmod = "2015-02-17T03:22:00Z"
weight = 39824
keywords = [ "reassembly", "fragmentation", "dissector" ]
aliases = [ "/questions/39824" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [fragmentation not successful](/questions/39824/fragmentation-not-successful)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39824-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Why is my code below not working? The fragmentation itself not successful and thus reassembly not working. Please suggest!</p><pre><code>switch (stype) {
case 0x00: // Continuation of Message
    msg_seqid = 2;
    rem_length = bctsdu_length;
    proto_tree_add_text(FT_BCnPDU_tree, next_tvb, offset_payload, rem_length, &quot;PDU data : %d&quot;, rem_length);
    break;
case 0x01: // Beginning of Message
    msg_seqid = 1;
    proto_tree_add_text(BCnPDU_bom_tree, next_tvb, offset_payload, 2, &quot;PDU Length : 0x%02x (%d)&quot;, pdu_len, pdu_len);
    rem_length = tvb_length_remaining(next_tvb, offset_payload);
    rem_length -= 2;
    proto_tree_add_text(BCnPDU_bom_tree, next_tvb, offset_payload, rem_length, &quot;PDU data  : %d &quot;, rem_length);

    break;
case 0x02: // End of Message
    msg_seqid = 3;
    bctsdu_length += 2;
    more_frags = FALSE;
    rem_length = bctsdu_length;
    rem_length -= 2;
    proto_tree_add_text(FT_BCnPDU_tree, next_tvb, offset_payload, rem_length, &quot;PDU data : %d&quot;, rem_length);
    disable_CRC = 1;
    break;
case 0x04: // Single Segment Message
    ---- // doesn&#39;t need fragment/reassembly
      break;
}

if (msg_seqid == 1 || msg_seqid == 2 || msg_seqid == 3) {
    save_fragmented = pinfo-&gt;fragmented;
    pinfo-&gt;fragmented = TRUE;
    frag_msg = fragment_add_seq_check(&amp;mns_reassembly_table,
                                      next_tvb,
                                      offset_payload,
                                      pinfo,
                                      mns_seqnum,
                                      NULL,
                                      mns_seqid,
                                      rem_length,
                                      more_frags);
    if (frag_msg) {
        col_append_fstr(pinfo-&gt;cinfo, COL_INFO, &quot; mns segment of a FRAGMENT PDU&quot;);
    } else {
        col_append_fstr(pinfo-&gt;cinfo, COL_INFO, &quot; FRAGMENT NOT DONE &quot;);
    }
}
if (more_frags == FALSE) {
    save_fragmented = pinfo-&gt;fragmented;
    pinfo-&gt;fragmented = FALSE;

    rass_tvb = process_reassembled_data(next_tvb,
                                        offset_payload,
                                        pinfo,
                                        &quot;Reassembled Message&quot;,
                                        frag_msg,
                                        &amp;mns_frag_items,
                                        NULL,
                                        FT_BCnPDU_tree);
    if (rass_tvb) {
        col_append_str(pinfo-&gt;cinfo, COL_INFO, &quot;(Message reassembled ) &quot;);
        ALSIGPDU(rass_tvb, pinfo, FT_BCnPDU_tree);
    }
}</code></pre><p>I am always getting the <code>FRAGMENT NOT DONE</code> error.</p></div><div id="question-tags" class="tags-container tags">reassembly fragmentation dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '15, 20:18</strong></p><img src="https://secure.gravatar.com/avatar/1339589a92af9455063c09e56bfc6299?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="umar&#39;s gravatar image" /><p>umar<br />
<span class="score" title="26 reputation points">26</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="umar has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Feb '15, 02:09</p></div></div><div id="comments-container-39824" class="comments-container"></div><div id="comment-tools-39824" class="comment-tools"></div><div class="clear"></div><div id="comment-39824-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39908"></span>

<div id="answer-container-39908" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39908-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>For reference, the answer was given in this wireshark-dev mailing list <a href="https://www.wireshark.org/lists/wireshark-dev/201502/msg00119.html">thread</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '15, 03:22</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Feb '15, 03:22</p></div></div><div id="comments-container-39908" class="comments-container"></div><div id="comment-tools-39908" class="comment-tools"></div><div class="clear"></div><div id="comment-39908-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

