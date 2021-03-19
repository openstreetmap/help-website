+++
type = "question"
title = "Reassemble length"
description = '''Hi, Iam struggling withe reassembly for 1 week.  could you see what is wrong in my code?  guint8 flag,pf,stype,sflag,flag_sel,num_sel,i;   guint16 ns,nr;   guint32 rem_length;   guint8 save_fragmented;   const guint32 mte_seqid=0;   const void *data = NULL;   gboolean more_frags=TRUE;   proto_item *...'''
date = "2014-12-02T22:26:00Z"
lastmod = "2014-12-04T00:23:00Z"
weight = 38292
keywords = [ "reassembly", "length", "table" ]
aliases = [ "/questions/38292" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Reassemble length](/questions/38292/reassemble-length)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38292-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38292-score" class="post-score" title="current number of votes">0</div><span id="post-38292-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Iam struggling withe reassembly for 1 week.</p><p>could you see what is wrong in my code?</p><pre><code>            guint8 flag,pf,stype,sflag,flag_sel,num_sel,i;

            guint16 ns,nr;

            guint32 rem_length;

            guint8 save_fragmented;

            const guint32 mte_seqid=0;

            const void *data = NULL;

            gboolean more_frags=TRUE;

            proto_item *frag_tree_item;

           flag = (tvb_get_guint8(next_tvb, offset_payload) &amp; 0x80) &gt;&gt;7 ;   // Bit 8  to check i pdu /s pdu or sseg pdu

                                if (flag == 0x00){ // flag &quot;0&quot; is for i-pdu

                                poll = (tvb_get_guint8(next_tvb, offset_payload) &amp; 0x40) &gt;&gt;6 ; // Bit 7 pf
                                ns = (tvb_get_ntohs(next_tvb, offset_payload) &amp; 0x3ff0) &gt;&gt;4 ; // 10 Bits are ns
                                offset_payload +=1;
                                nr= (tvb_get_ntohs(next_tvb, offset_payload) &amp; 0x0ffc) &gt;&gt;2 ; // 10 bits are nr
                                offset_payload +=1;
                                stype = (tvb_get_guint8(next_tvb, offset_payload) &amp; 0x03) ; // 2 bits LSB are Stype
                                offset_payload -=2;

            FT_connPDU_item = proto_tree_add_text(tree, next_tvb, offset_payload, sdu_length, &quot;BCnPDU (Formatted) : Information, I flag = 0x%02x, Pf = 0x%02x, Ns = 0x%02x, Nr = 0x%02x &quot;, iflag,pf,ns,nr );

            FT_connPDU_tree = proto_item_add_subtree(FT_connPDU_item, ett_FT_BCnPDU);

            proto_tree_add_text(FT_connPDU_tree, next_tvb, offset_payload, 1, &quot; sdu_length: %d&quot;, sdu_length);

            proto_tree_add_text(FT_connPDU_tree, next_tvb, offset_payload, 1, &quot;flag : 0x%02x (%s)&quot;, iflag,val_to_str(iflag,true_false_vals,&quot;%s&quot;));

           proto_tree_add_text(FT_connPDU_tree, next_tvb, offset_payload, 1, &quot;Pf : 0x%02x (%d)&quot;, pf,pf);

          proto_tree_add_text(FT_connPDU_tree, next_tvb, offset_payload, 2, &quot;Ns : 0x%02x (%d)&quot;, ns,ns);

          offset_payload +=1;
          sdu_length-=1;

           proto_tree_add_text(FT_connPDU_tree, next_tvb, offset_payload, 2, &quot;Nr : 0x%02x (%d)&quot;, nr,nr);

         offset_payload +=1;

         sdu_length-=1;

         proto_tree_add_text(FT_connPDU_tree, next_tvb, offset_payload, 1, &quot;BConnSegType : 0x%02x (%s)&quot;, stype,val_to_str(stype,BCn_Seg_Type_vals,&quot;%s&quot;));

        offset_payload +=1;

       sdu_length-=1;

       switch (stype){

  case 0x00: // Continuation of Message

                                        sdu_length+=1;
rem_length = (guint32) sdu_length;

                                        proto_tree_add_text(FT_connPDU_tree, next_tvb, offset_payload, rem_length , &quot;PDU data : %d&quot;, rem_length);

offset_payload +=rem_length;
                                        sdu_length-=rem_length;

                                        proto_tree_add_text(FT_connPDU_tree, next_tvb, offset_payload, 1 , &quot;sdu_length: %d&quot;, sdu_length);

                                        save_fragmented = pinfo-&gt;fragmented;
                                        pinfo-&gt;fragmented = TRUE;

      mte_frag_msg = fragment_add_seq_next(&amp;mte_reassembly_table,next_tvb, offset_payload, pinfo, mte_seqid, NULL, rem_length, more_frags);
                                        pinfo-&gt;fragmented = save_fragmented;
                                            col_set_str(pinfo-&gt;cinfo, COL_INFO, &quot; mte segment of a reassembled PDU&quot;);

                                                if (sdu_length&gt;0){

                                        SIG_PDU(next_tvb, pinfo, tree);

                                                    }

break;

       case 0x01: // Beginning of Message

                                            BCnPDU_stype_item = proto_tree_add_text(FT_connPDU_tree, next_tvb, offset_payload, 1, &quot;%s&quot;,val_to_str(stype,BCn_Seg_Type_vals,&quot;%s&quot;));
                                            BCnPDU_stype_tree = proto_item_add_subtree(BCnPDU_stype_item, ett_BCnPDU_stype);

                                            BCnPDU_bom_item = proto_tree_add_text(BCnPDU_stype_tree, next_tvb, offset_payload, 1, &quot;MACSAPFLAGS&quot;);
                                            BCnPDU_bom_tree = proto_item_add_subtree(BCnPDU_bom_item, ett_BCnPDU_bom);

                                            temp_val = (tvb_get_guint8(next_tvb, offset_payload) &amp; 0x80) &gt;&gt;7 ; // Bit 8 - Flow Control
                                            proto_tree_add_text(BCnPDU_bom_tree, next_tvb, offset_payload, 1, &quot;Flow Control : 0x%02x (%s)&quot;, temp_val,val_to_str(temp_val, true_false_vals,&quot;%s&quot;));
                                            temp_val = (tvb_get_guint8(next_tvb, offset_payload) &amp; 0x40) &gt;&gt;6 ; // Bit 7 - Reserved l
                                            proto_tree_add_text(BCnPDU_bom_tree, next_tvb, offset_payload, 1, &quot;Reserved l : 0x%02x (%d)&quot;, temp_val,temp_val);
                                            temp_val = (tvb_get_guint8(next_tvb, offset_payload) &amp; 0x20) &gt;&gt;5 ; // Bit 6 - Expedited
                                            proto_tree_add_text(BCnPDU_bom_tree, next_tvb, offset_payload, 1, &quot;Expedited : 0x%02x (%s)&quot;, temp_val,val_to_str(temp_val, true_false_vals,&quot;%s&quot;));
                                            temp_val = (tvb_get_guint8(next_tvb, offset_payload) &amp; 0x10) &gt;&gt;4 ; // Bit 5 - OAM PDU Flag
                                            proto_tree_add_text(BCnPDU_bom_tree, next_tvb, offset_payload, 1, &quot;OAM PDU Flag : 0x%02x (%s)&quot;, temp_val,val_to_str(temp_val, true_false_vals,&quot;%s&quot;));
                                            temp_val = (tvb_get_guint8(next_tvb, offset_payload) &amp; 0x08) &gt;&gt;3 ; // Bit 4 - Reserved 2
                                            proto_tree_add_text(BCnPDU_bom_tree, next_tvb, offset_payload, 1, &quot;Reserved 2 : 0x%02x (%d)&quot;, temp_val,temp_val);
                                            pl_val = (tvb_get_ntohs(next_tvb, offset_payload) &amp; 0x07ff); // PDU Length - 11 Bits 
                                        proto_tree_add_text(BCnPDU_bom_tree, next_tvb, offset_payload, 2, &quot;PDU Length : 0x%02x (%d)&quot;, pl_val,pl_val);
                                            pl_val = (guint32)pl_val;
                                            fragment_set_tot_len(&amp;mte_reassembly_table, pinfo,mte_seqid, NULL, pl_val);
                                            offset_payload+=2;
                                            sdu_length+=2;
                                        proto_tree_add_text(BCnPDU_bom_tree, next_tvb, offset_payload, 1, &quot; sdu_length: %d&quot;, sdu_length);
                                            rem_length= (guint32) tvb_length_remaining(next_tvb, offset_payload);
                                            rem_length-=2;
                                        if (rem_length &gt;= pl_val){
                                        rem_length-=2;
                                    proto_tree_add_text(BCnPDU_bom_tree, next_tvb, offset_payload, rem_length, &quot;PDU data  : %d &quot;, rem_length);
                                            offset_payload+=sdu_length;
                                                } else {
                                                                                    proto_tree_add_text(BCnPDU_bom_tree, next_tvb, offset_payload, rem_length, &quot;PDU data  : %d &quot;, rem_length);
                                            offset_payload+=rem_length;
    }

                                            save_fragmented = pinfo-&gt;fragmented;
                                        pinfo-&gt;fragmented = TRUE;

                                        mte_frag_msg = fragment_add_seq_next(&amp;mte_reassembly_table, next_tvb, offset_payload, pinfo, mte_seqid, NULL, rem_length, more_frags);

 pinfo-&gt;fragmented = save_fragmented;

                                        col_set_str(pinfo-&gt;cinfo, COL_INFO, &quot; mte segment of a reassembled PDU &quot;);

                                        pinfo-&gt;fragmented = save_fragmented;

                                        break;

 case 0x02: // End of Message

                                        sdu_length+=2;
                                        more_frags=FALSE;

                                        rem_length = (guint32) sdu_length;
                                        rem_length-=2;

                                        proto_tree_add_text(FT_connPDU_tree, next_tvb, offset_payload, rem_length , &quot;PDU data : %d&quot;, rem_length);                                   offset_payload +=rem_length;
                                    disable_CRC=1;                              save_fragmented = pinfo-&gt;fragmented;                        
     pinfo-&gt;fragmented = TRUE;      
                                        mte_frag_msg = fragment_add_seq_next(&amp;mte_reassembly_table,next_tvb, offset_payload, pinfo, mte_seqid, NULL, rem_length, more_frags);                               mte_frag_msg = fragment_get_reassembled_id(&amp;mte_reassembly_table, pinfo, mte_seqid);

    //mte_tvb = tvb_new_chain(next_tvb, mte_frag_msg-&gt;tvb_data);
                                        mte_tvb = process_reassembled_data(next_tvb, offset_payload, pinfo, &quot;mte Reassembled PDU&quot;, mte_frag_msg, &amp;mte_frag_items, NULL, tree );

if (mte_tvb) { /* Reassembled */
                                                try_tvb=mte_tvb;
         col_append_str(pinfo-&gt;cinfo, COL_INFO,&quot;(Message reassembled) &quot;);
    add_new_data_source(pinfo, try_tvb, &quot;Reassembled mte&quot;);
                                                show_fragment_tree(mte_frag_msg, &amp;mte_frag_items,tree, pinfo, try_tvb, &amp;frag_tree_item);        
                                                    } else { /* Not last packet of reassembled message */

               col_append_str(pinfo-&gt;cinfo, COL_INFO,&quot;(Message fragment) &quot;);
                                                                }

                                                      pinfo-&gt;fragmented = save_fragmented;

                    if (mte_tvb){
        SIG_PDU(mte_tvb, pinfo, tree);
               } else {
                                            SIG_PDU(next_tvb, pinfo, tree);                 offset_payload+=sdu_length;

                                                                break;</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reassembly" rel="tag" title="see questions tagged &#39;reassembly&#39;">reassembly</span> <span class="post-tag tag-link-length" rel="tag" title="see questions tagged &#39;length&#39;">length</span> <span class="post-tag tag-link-table" rel="tag" title="see questions tagged &#39;table&#39;">table</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '14, 22:26</strong></p><img src="https://secure.gravatar.com/avatar/1339589a92af9455063c09e56bfc6299?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="umar&#39;s gravatar image" /><p><span>umar</span><br />
<span class="score" title="26 reputation points">26</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="umar has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Dec '14, 23:08</strong> </span></p></div></div><div id="comments-container-38292" class="comments-container"><span id="38293"></span><div id="comment-38293" class="comment"><div id="post-38293-score" class="comment-score"></div><div class="comment-text"><p>Some one please help!!</p></div><div id="comment-38293-info" class="comment-info"><span class="comment-age">(02 Dec '14, 22:26)</span> <span class="comment-user userinfo">umar</span></div></div><span id="38314"></span><div id="comment-38314" class="comment"><div id="post-38314-score" class="comment-score"></div><div class="comment-text"><p>Some one please help!!</p></div><div id="comment-38314-info" class="comment-info"><span class="comment-age">(04 Dec '14, 00:23)</span> <span class="comment-user userinfo">umar</span></div></div></div><div id="comment-tools-38292" class="comment-tools"></div><div class="clear"></div><div id="comment-38292-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

