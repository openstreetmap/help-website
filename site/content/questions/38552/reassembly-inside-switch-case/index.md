+++
type = "question"
title = "reassembly inside switch case"
description = '''Hi  My reassembly is not working . Iam using switch case for  beginning of message  continuation of message  end of message  my code i not working . is it because of switch case ? please help.  switch (msg_type){   case 0x00: // Continuation of Message   msg_seqid=1;   pdu_length+=1;   rem_length = ...'''
date = "2014-12-14T06:15:00Z"
lastmod = "2014-12-14T06:15:00Z"
weight = 38552
keywords = [ "case", "reassembly", "switch", "in" ]
aliases = [ "/questions/38552" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [reassembly inside switch case](/questions/38552/reassembly-inside-switch-case)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38552-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi My reassembly is not working . Iam using switch case for beginning of message continuation of message end of message</p><p>my code i not working . is it because of switch case ? please help.</p><pre><code>    switch (msg_type){

            case 0x00: // Continuation of Message 
                                        msg_seqid=1;

                                        pdu_length+=1;

                                        rem_length = pdu_length;
            proto_tree_add_text(FT_BCnPDU_tree, next_tvb, offset_payload, rem_length , &quot;PDU data : %d&quot;, rem_length);

                                        pdu_length-=rem_length;

                                        if (pf ==0x00){
                                        save_fragmented = pinfo-&gt;fragmented;    
                                        pinfo-&gt;fragmented = TRUE;

                                        frag_msg = fragment_add_seq_check(&amp;mte_reassembly_table,
                                              next_tvb,
                                              offset_payload,
                                              pinfo,
                                              msg_seqid, /* ID for fragments belonging together */
                                              NULL,
                                              mte_seqid, /* fragment sequence number */
                                              rem_length,  /* fragment length - to the end */
                                              more_frags); /* More fragments? */

                                        save_fragmented = pinfo-&gt;fragmented;

                                        offset_payload+=rem_length;

                                        if (frag_msg != NULL){
                                        col_append_fstr(pinfo-&gt;cinfo, COL_INFO, &quot; mte segment of a reassembled PDU&quot;);
                                                            }

                                        }

                        break;

            case 0x01: // Beginning of Message 
                                            msg_seqid=0;

                                            BCnPDU_bom_item = proto_tree_add_text(BCnPDU_stype_tree, next_tvb, offset_payload, 1, &quot;MACSAPFLAGS&quot;);
                                            BCnPDU_bom_tree = proto_item_add_subtree(BCnPDU_bom_item, ett_BCnPDU_bom);

                                            pdu_len = (tvb_get_ntohl(next_tvb, offset_payload) &amp; 0x07ff0000) &gt;&gt;16; // PDU Length - 11 Bits  pdu_len is guint32 32 bit variable

                                            proto_tree_add_text(BCnPDU_bom_tree, next_tvb, offset_payload, 2, &quot;PDU Length : 0x%02x (%d)&quot;, pdu_len,pdu_len);

                                            offset_payload+=2;

                                            rem_length=  tvb_length_remaining(next_tvb, offset_payload);
                                            rem_length-=2;

                                            proto_tree_add_text(BCnPDU_bom_tree, next_tvb, offset_payload, rem_length, &quot;PDU data (else) : %d &quot;, rem_length);

                                           save_fragmented = pinfo-&gt;fragmented;    
                                            pinfo-&gt;fragmented = TRUE;

                                            fragment_set_tot_len(&amp;mte_reassembly_table, pinfo, msg_seqid, NULL, pdu_len);

                                          frag_msg = fragment_add_seq_check(&amp;mte_reassembly_table,
                                              next_tvb,
                                              offset_payload,
                                              pinfo,
                                              msg_seqid, /* ID for fragments belonging together */
                                              NULL,
                                              mte_seqid, /* fragment sequence number */
                                              rem_length,  /* fragment length - to the end */
                                              more_frags); /* More fragments? */

                                              pinfo-&gt;fragmented = save_fragmented;

                                        offset_payload+=rem_length;

                                        if (frag_msg != NULL){                                      
                                                col_append_fstr(pinfo-&gt;cinfo, COL_INFO, &quot; Fragmented &quot;);

                                                    }else{

                                                        col_append_fstr(pinfo-&gt;cinfo, COL_INFO, &quot; SOmthing wrong &quot;);
                                                    }                       
                                            }

                            break;

        case 0x02: // End of Message

                                    msg_seqid=2;
                                        pdu_length+=2;
                                        more_frags=FALSE;

                                        rem_length =  pdu_length;
                                        rem_length-=2;

                                        proto_tree_add_text(FT_BCnPDU_tree, next_tvb, offset_payload, rem_length , &quot;PDU data : %d&quot;, rem_length);

                                        disable_CRC=1;
                                        save_fragmented = pinfo-&gt;fragmented;

                                        pinfo-&gt;fragmented = FALSE;

                                        frag_msg = fragment_add_seq_check(&amp;mte_reassembly_table,
                                              next_tvb,
                                              offset_payload,
                                              pinfo,
                                              msg_seqid, /* ID for fragments belonging together */
                                              NULL,
                                              mte_seqid, /* fragment sequence number */
                                              rem_length,  /* fragment length - to the end */
                                              more_frags); /* More fragments? */

                                        save_fragmented = pinfo-&gt;fragmented;

                                         rass_tvb = process_reassembled_data(next_tvb,
                                               offset_payload,
                                               pinfo,
                                               &quot;Reassembled Message&quot;,
                                               frag_msg,
                                               &amp;mte_frag_items,
                                               NULL,
                                               FT_BCnPDU_tree);

                                if (frag_msg != NULL) { /* Reassembled */
                                    //rass_tvb=try_tvb;
                                    add_new_data_source(pinfo, rass_tvb, &quot;Reassembled mte&quot;);
                                    show_fragment_tree(frag_msg, &amp;mte_frag_items,FT_BCnPDU_tree, pinfo, rass_tvb, &amp;frag_tree_item);
                                    col_append_str(pinfo-&gt;cinfo, COL_INFO,&quot;(Message reassemble progress) &quot;);

                                                    }else { /* Not last packet of reassembled message */
                                                            col_append_str(pinfo-&gt;cinfo, COL_INFO,&quot;(Message fragment) &quot;);
                                                                            }

                                    if (rass_tvb){
                                                offset_payload=0;
                                                col_append_str(pinfo-&gt;cinfo, COL_INFO,&quot;(Message reassembled ) &quot;);
                                                SIGPDU(rass_tvb, pinfo, FT_BCnPDU_tree);
                                                    }

                                                    reassembly_table_destroy(&amp;mte_reassembly_table);

                                                    break;</code></pre></div><div id="question-tags" class="tags-container tags">case reassembly switch in</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Dec '14, 06:15</strong></p><img src="https://secure.gravatar.com/avatar/1339589a92af9455063c09e56bfc6299?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="umar&#39;s gravatar image" /><p>umar<br />
<span class="score" title="26 reputation points">26</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="umar has no accepted answers">0%</span></p></div></div><div id="comments-container-38552" class="comments-container"><span id="38554"></span><div id="comment-38554" class="comment"><div id="post-38554-score" class="comment-score"></div><div class="comment-text"><p>I have used fragmentation out of this switch case and tried</p><p>my frag_msg is always returning NULL Value . I believe something wrong with my reassembly table.</p><p>i have tried many</p><p>fragment_add_seq_check fragment_add_seq_next</p><p>i have 3 diff message 1. beginning 2 continuation 3 end of message</p><p>and my msg_seq id i set to 0,1,2</p><p>and mte seq number i get from pdu . (message belongs to mte_seq id 3 will assemble together) sometimes my data is not comes in order,</p><p>please help</p></div><div id="comment-38554-info" class="comment-info"><span class="comment-age">(14 Dec '14, 06:50)</span> umar</div></div></div><div id="comment-tools-38552" class="comment-tools"></div><div class="clear"></div><div id="comment-38552-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

