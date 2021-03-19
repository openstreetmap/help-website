+++
type = "question"
title = "packet reassembly not succesful"
description = '''Hi  Whats wrong in my below code? Reassembly of packets not happening.i can able to build but its not processing any? iamn creating tvb mine_tvb whih is re assembled data and pass to a function.  please help.  static reassembly_table mine_reassembly_table;   static int hf_mine_fragments = -1;  stati...'''
date = "2014-11-19T19:40:00Z"
lastmod = "2014-11-19T19:40:00Z"
weight = 37987
keywords = [ "reassembly" ]
aliases = [ "/questions/37987" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [packet reassembly not succesful](/questions/37987/packet-reassembly-not-succesful)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37987-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>Whats wrong in my below code? Reassembly of packets not happening.i can able to build but its not processing any?</p><p>iamn creating tvb mine_tvb whih is re assembled data and pass to a function.</p><p>please help.</p><pre><code>    static reassembly_table mine_reassembly_table;

    static int hf_mine_fragments = -1;
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

    ALSIGPDU(mine_tvb, pinfo, tree);</code></pre><p>please help.</p><p>Thanks</p><p>Raj</p></div><div id="question-tags" class="tags-container tags">reassembly</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '14, 19:40</strong></p><img src="https://secure.gravatar.com/avatar/1339589a92af9455063c09e56bfc6299?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="umar&#39;s gravatar image" /><p>umar<br />
<span class="score" title="26 reputation points">26</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="umar has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Nov '14, 03:05</p></div></div><div id="comments-container-37987" class="comments-container"><span id="38097"></span><div id="comment-38097" class="comment"><div id="post-38097-score" class="comment-score">1</div><div class="comment-text"><p>Is your code compiling ? Show us your fragmentation function please cause I don't think the code above build successfully</p></div><div id="comment-38097-info" class="comment-info"><span class="comment-age">(24 Nov '14, 05:49)</span> Afrim</div></div><span id="38151"></span><div id="comment-38151" class="comment"><div id="post-38151-score" class="comment-score"></div><div class="comment-text"><p>hi afrim</p><p>My code is compiling without any error , but when end of message packet comes, it get crash.</p><p>only the above steps i have followed. what is the fragmentation function mean? what are the other steps there to complete the reassembly. Please help.</p><p>i have refered this and followed the steps. <a href="http://www.linuxtopia.org/online_books/network_security/wireshark_development_guide/wireshark_ChDissectReassemble.html">http://www.linuxtopia.org/online_books/network_security/wireshark_development_guide/wireshark_ChDissectReassemble.html</a></p></div><div id="comment-38151-info" class="comment-info"><span class="comment-age">(25 Nov '14, 22:50)</span> umar</div></div><span id="38158"></span><div id="comment-38158" class="comment not_top_scorer"><div id="post-38158-score" class="comment-score"></div><div class="comment-text"><p>If I copy/past your code above it definitely not work. I need to see your fragmentation function (there is no function in the code above).</p><p>Your function should return a new buffer with all data reassembled in "mine_tvb" if the reassembly is successfull. Otherwise you should call data dissector because the reassembly is unsuccessful (because it's not the last fragment or maybe wrong parameter is your fragment_add_seq_next() function)</p></div><div id="comment-38158-info" class="comment-info"><span class="comment-age">(26 Nov '14, 03:24)</span> Afrim</div></div><span id="38159"></span><div id="comment-38159" class="comment not_top_scorer"><div id="post-38159-score" class="comment-score"></div><div class="comment-text"><p>note : I have 3 type of frames in different packets. 1. Beginning of message 2. continuation of message 3. End of message.</p><p>I will have the information about total length of the PDU message in the Beginning of Messsage packet. and my messeges are coming in order ie. beginning message , continuation of the message (in other packet ) and end of message (here i should combine all data and reassemble).</p><p>Its look like some process iam missing out. please help!</p></div><div id="comment-38159-info" class="comment-info"><span class="comment-age">(26 Nov '14, 03:25)</span> umar</div></div><span id="38160"></span><div id="comment-38160" class="comment not_top_scorer"><div id="post-38160-score" class="comment-score"></div><div class="comment-text"><p>more_frags=0;</p><pre><code>                                        reas_tvb=tvb_new_subset(tvb, offset, sdu_length, -1);

                                        pinfo-&gt;fragmented = TRUE;

                                        mine_frag_msg = fragment_add_seq_next(&amp;_reassembly_table,
                                                        reas_tvb, offset, pinfo, mine_seqid, NULL,
                                                     frag_data_len, more_frags);

                                        save_fragmented = pinfo-&gt;fragmented;

                                        pinfo-&gt;fragmented = save_fragmented;</code></pre></div><div id="comment-38160-info" class="comment-info"><span class="comment-age">(26 Nov '14, 03:30)</span> umar</div></div><span id="38161"></span><div id="comment-38161" class="comment"><div id="post-38161-score" class="comment-score">1</div><div class="comment-text"><p>You'r creating a new buffer and passing this new buffer as a parameter to the fragment_add_seq_next() function. The real offset of your reas_tvb is 0 and the value of your offset is not 0.</p><p>Also, I dont know how your more_frags is created but it should be something like :</p><p>msg_type = 3 ? more_frags = 0:1</p></div><div id="comment-38161-info" class="comment-info"><span class="comment-age">(26 Nov '14, 03:48)</span> Afrim</div></div><span id="38192"></span><div id="comment-38192" class="comment not_top_scorer"><div id="post-38192-score" class="comment-score"></div><div class="comment-text"><p>Hi Afrim Thanks for your support!</p><p>I hope iam almost there i have corrected my code as below but end of message not showing as reassembled tab. is there any other step i should write to display the reassembled tvb in a seperate TAB??</p><p>my Code :<br />
</p><pre><code>guint32 rem_length;
gint frag_data_len=0;
guint8 save_fragmented;
const guint32 mine_seqid=0;
const void *data = NULL; 
gboolean more_frags=TRUE;

case 0x00: // Continuation of Message 
bctsdu_length+=1;   
rem_length = (guint32) tvb_length_remaining(next_tvb, offset_payload);
     rem_length-=2;
proto_tree_add_text(FT_BCnPDU_tree, next_tvb, offset_payload, rem_length , &quot;PDU data : %d&quot;, rem_length);
                                    offset_payload +=rem_length;
                                        bctsdu_length-=rem_length;
                                        ras_calc_length+=rem_length;
                                        pinfo-&gt;fragmented = TRUE;

     mine_frag_msg = fragment_add_seq_next(&amp;mine_reassembly_table, next_tvb, offset_payload, pinfo, mine_seqid, NULL, rem_length, more_frags);                          
     save_fragmented = pinfo-&gt;fragmented;

     pinfo-&gt;fragmented = save_fragmented;
     break;

case 0x01: // Beginning of Message

                ras_total_length=0; 
                                            proto_tree_add_text(BCnPDU_bom_tree, next_tvb, offset_payload, 2, &quot;PDU Length : 0x%02x (%d)&quot;,pl_val,pl_val);
    ras_total_length = (guint32)pl_val;
                                                     ras_calc_length = (guint32)pl_val;
                                            offset_payload+=2;
                                            bctsdu_length+=2;
                                            rem_length= (guint32) tvb_length_remaining(next_tvb, offset_payload);
                                            rem_length-=2;
                                            if (rem_length &gt;= ras_calc_length){

                                            rem_length-=2;
                                    proto_tree_add_text(BCnPDU_bom_tree, next_tvb, offset_payload, rem_length, &quot;PDU data (if) : %d &quot;, rem_length);
                                            offset_payload+=bctsdu_length;
                                        } else {
                                            proto_tree_add_text(BCnPDU_bom_tree, next_tvb, offset_payload, rem_length, &quot;PDU data (else) : %d &quot;, rem_length);                                offset_payload+=rem_length;                             }
                                            mine_init_protocol();
                                            save_fragmented = pinfo-&gt;fragmented;

      pinfo-&gt;fragmented = TRUE;
                                        ras_calc_length+=rem_length;
                                        proto_tree_add_text(BCnPDU_bom_tree, next_tvb, offset_payload, 1, &quot; ras_total_length : %d&quot;, ras_total_length);
                                        mine_frag_msg = fragment_add_seq_next(&amp;mine_reassembly_table,
                                            next_tvb, offset_payload, pinfo, mine_seqid, NULL,rem_length, more_frags);
pinfo-&gt;fragmented = TRUE;
                                    save_fragmented = pinfo-&gt;fragmented;
      break;

case 0x02: // End of Message 
                                        more_frags=FALSE;
     rem_length = (guint32) bctsdu_length;
                                        proto_tree_add_text(FT_BCnPDU_tree, next_tvb, offset_payload, rem_length , &quot;PDU data : %d&quot;, rem_length);

                                        offset_payload +=rem_length;
                                        ras_calc_length+=rem_length;
                                    disable_CRC=1;
                                        mine_frag_msg = fragment_add_seq_next(&amp;mine_reassembly_table,next_tvb, offset_payload, pinfo, mine_seqid, NULL, rem_length, more_frags);

      pinfo-&gt;fragmented = TRUE;
                                        save_fragmented = pinfo-&gt;fragmented;
mine_tvb = process_reassembled_data(next_tvb, offset_payload, pinfo, &quot;Reassembled PDU&quot;, mine_frag_msg, &amp;mine_frag_items, NULL, tree );                                      
     if (mine_tvb){
                                        pinfo-&gt;fragmented = TRUE;
                                        save_fragmented = pinfo-&gt;fragmented;
                                        offset_payload=0;
                                        ALSIGPDU(mine_tvb, pinfo, FT_BCnPDU_tree);
        }                           offset_payload+=bctsdu_length;
                                        ras_total_length=0;
                                        ras_calc_length=0;                                          
                                break;</code></pre></div><div id="comment-38192-info" class="comment-info"><span class="comment-age">(26 Nov '14, 20:43)</span> umar</div></div><span id="38201"></span><div id="comment-38201" class="comment not_top_scorer"><div id="post-38201-score" class="comment-score"></div><div class="comment-text"><p>Hi</p><p>Any one can help me on this?</p></div><div id="comment-38201-info" class="comment-info"><span class="comment-age">(27 Nov '14, 02:41)</span> umar</div></div><span id="38202"></span><div id="comment-38202" class="comment"><div id="post-38202-score" class="comment-score">1</div><div class="comment-text"><p>Well it's not the way you reassamble data. Did you take a look at an exemple of reassemble in epan directory ? Take a look at an exemple in epan/dissectors.</p><p>You don't need "case", the "mine_init_protocol()" function should not be called there. Try to look at a dissector in epan directory and keep the same code architecture for your dissector.</p></div><div id="comment-38202-info" class="comment-info"><span class="comment-age">(27 Nov '14, 02:55)</span> Afrim</div></div><span id="38203"></span><div id="comment-38203" class="comment not_top_scorer"><div id="post-38203-score" class="comment-score"></div><div class="comment-text"><p>Hi Afrim</p><p>you mean this? in reassemble.c ?</p><pre><code>  tvbuff_t *
 process_reassembled_data(tvbuff_t *tvb, const int offset,   packet_info *pinfo,
const char *name, fragment_head *fd_head, const fragment_items *fit,
gboolean *update_col_infop, proto_tree *tree)</code></pre><p>{ tvbuff_t <em>next_tvb; gboolean update_col_info; proto_item</em> frag_tree_item;</p><pre><code>if (fd_head != NULL &amp;&amp; pinfo-&gt;fd-&gt;num == fd_head-&gt;reassembled_in) {
    /*
     * OK, we&#39;ve reassembled this.
     * Is this something that&#39;s been reassembled from more
     * than one fragment?
     */
    if (fd_head-&gt;next != NULL) {
        /*
         * Yes.
         * Allocate a new tvbuff, referring to the
         * reassembled payload, and set
         * the tvbuff to the list of tvbuffs to which
         * the tvbuff we were handed refers, so it&#39;ll get
         * cleaned up when that tvbuff is cleaned up.
         */
        next_tvb = tvb_new_chain(tvb, fd_head-&gt;tvb_data);

        /* Add the defragmented data to the data source list. */
        add_new_data_source(pinfo, next_tvb, name);

        /* show all fragments */
        if (fd_head-&gt;flags &amp; FD_BLOCKSEQUENCE) {
            update_col_info = !show_fragment_seq_tree(
                fd_head, fit,  tree, pinfo, next_tvb, &amp;frag_tree_item);
        } else {
            update_col_info = !show_fragment_tree(fd_head,
                fit, tree, pinfo, next_tvb, &amp;frag_tree_item);
        }
    } else {
        /*
         * No.
         * Return a tvbuff with the payload.
         */
        next_tvb = tvb_new_subset_remaining(tvb, offset);
        pinfo-&gt;fragmented = FALSE;  /* one-fragment packet */
        update_col_info = TRUE;
    }
    if (update_col_infop != NULL)
        *update_col_infop = update_col_info;
} else {
    /*
     * We don&#39;t have the complete reassembled payload, or this
     * isn&#39;t the final frame of that payload.
     */
    next_tvb = NULL;

    /*
     * If we know what frame this was reassembled in,
     * and if there&#39;s a field to use for the number of
     * the frame in which the packet was reassembled,
     * add it to the protocol tree.
     */
    if (fd_head != NULL &amp;&amp; fit-&gt;hf_reassembled_in != NULL) {
        proto_tree_add_uint(tree,
            *(fit-&gt;hf_reassembled_in), tvb,
            0, 0, fd_head-&gt;reassembled_in);
    }
}
return next_tvb;</code></pre><p>}</p></div><div id="comment-38203-info" class="comment-info"><span class="comment-age">(27 Nov '14, 03:04)</span> umar</div></div><span id="38206"></span><div id="comment-38206" class="comment not_top_scorer"><div id="post-38206-score" class="comment-score"></div><div class="comment-text"><p>Disclaimer: I have not checked your code... Take a look at packet-sccp.c I think it has a pretty straight forward implementation of reassembly.</p></div><div id="comment-38206-info" class="comment-info"><span class="comment-age">(27 Nov '14, 04:44)</span> Anders ♦</div></div><span id="38220"></span><div id="comment-38220" class="comment not_top_scorer"><div id="post-38220-score" class="comment-score"></div><div class="comment-text"><p>Hi Anders i have followed thew same steps and i have a condition like</p><pre><code>    mte_frag_msg = fragment_add_seq_next(&amp;mte_reassembly_table,next_tvb, offset_payload, pinfo, mte_seqid, NULL, rem_length, more_frags);

                                        save_fragmented = pinfo-&gt;fragmented;
                                        pinfo-&gt;fragmented = TRUE;
    mte_tvb = process_reassembled_data(next_tvb, offset_payload, pinfo, &quot;mte Reassembled PDU&quot;, mte_frag_msg, &amp;mte_frag_items, NULL, FT_BCnPDU_tree );

    if (mte_frag_msg) { /* Reassembled */
                try_tvb=mte_tvb;
                col_append_str(pinfo-&gt;cinfo, COL_INFO,&quot;(Message reassembled) &quot;);
                    } else { /* Not last packet of reassembled message */
                            col_append_str(pinfo-&gt;cinfo, COL_INFO,&quot;(Message fragment) &quot;);
   }

    if (try_tvb){
     ALSIGPDU(try_tvb, pinfo, tree);
  } else {
  ALSIGPDU(next_tvb, pinfo, tree);
}</code></pre><p>Iam getting always Message Fragmented in col info. looks like Some thing wrong and a majot step i have missed. mte_frag_msg itself not succesful. is ther any steps for diplaying in seperate tab as Reassembled data ?? Please Help!</p></div><div id="comment-38220-info" class="comment-info"><span class="comment-age">(27 Nov '14, 19:59)</span> umar</div></div><span id="38221"></span><div id="comment-38221" class="comment not_top_scorer"><div id="post-38221-score" class="comment-score"></div><div class="comment-text"><p>Are you stepping the sequence number for each packet and setting more_fragments to false for the last packet?</p></div><div id="comment-38221-info" class="comment-info"><span class="comment-age">(27 Nov '14, 20:36)</span> Anders ♦</div></div><span id="38222"></span><div id="comment-38222" class="comment not_top_scorer"><div id="post-38222-score" class="comment-score"></div><div class="comment-text"><p>HI</p><p>My Sequence number set to 0 Zero. Because my packets messages always comes in order. More frags i have set to TRUE and in the last packet i made it FALSE.</p></div><div id="comment-38222-info" class="comment-info"><span class="comment-age">(27 Nov '14, 21:39)</span> umar</div></div><span id="38224"></span><div id="comment-38224" class="comment"><div id="post-38224-score" class="comment-score">1</div><div class="comment-text"><p>As you have first middle and last packet try setting the sequence number to 1 2 3 respectivly.</p></div><div id="comment-38224-info" class="comment-info"><span class="comment-age">(27 Nov '14, 22:32)</span> Anders ♦</div></div><span id="38226"></span><div id="comment-38226" class="comment not_top_scorer"><div id="post-38226-score" class="comment-score"></div><div class="comment-text"><p>one more doubt! my pdu length bit is 12 bit and when i stor in 32 bit gint. How one byte by byte the data stord in table? How does it copy the data into the table?</p></div><div id="comment-38226-info" class="comment-info"><span class="comment-age">(27 Nov '14, 23:56)</span> umar</div></div><span id="38260"></span><div id="comment-38260" class="comment not_top_scorer"><div id="post-38260-score" class="comment-score"></div><div class="comment-text"><p>Hi anyone help me on this please.</p></div><div id="comment-38260-info" class="comment-info"><span class="comment-age">(01 Dec '14, 11:27)</span> umar</div></div><span id="38271"></span><div id="comment-38271" class="comment not_top_scorer"><div id="post-38271-score" class="comment-score"></div><div class="comment-text"><p>Hi</p><p>Anders , ANyone Help Me please!</p><p>I Have tried setting up seq number 1,2,3 and tried . still same.</p><pre><code>     mte_frag_msg = fragment_add_seq_next(&amp;mte_reassembly_table,next_tvb, offset_payload, pinfo, mte_seqid, NULL, rem_length, more_frags);

    mte_tvb = process_reassembled_data(next_tvb, offset_payload, pinfo, &quot;mte Reassembled PDU&quot;, mte_frag_msg, &amp;mte_frag_items, NULL, FT_BCnPDU_tree );</code></pre><p>do i need to create GHASh Table ?</p><p>My table decleration is</p><pre><code>   static reassembly_table mte_reassembly_table;</code></pre><p>table init is</p><pre><code>    static void mte_init_protocol(void)
                                 {

             reassembly_table_init(&amp;mte_reassembly_table, &amp;addresses_reassembly_table_functions);
                        }</code></pre><p>please help.</p></div><div id="comment-38271-info" class="comment-info"><span class="comment-age">(01 Dec '14, 18:20)</span> umar</div></div><span id="38279"></span><div id="comment-38279" class="comment not_top_scorer"><div id="post-38279-score" class="comment-score"></div><div class="comment-text"><p>In my opinion you don't even need sequence number. i've done my own reassemble without sequence number. Btw if your col_info shows "Message reassembled" it mean that the reassemble was successfull so "mte_frag_msg" is not NULL.</p></div><div id="comment-38279-info" class="comment-info"><span class="comment-age">(02 Dec '14, 05:52)</span> Afrim</div></div><span id="38286"></span><div id="comment-38286" class="comment not_top_scorer"><div id="post-38286-score" class="comment-score"></div><div class="comment-text"><p>Hi I got the "message Fragmengted" in beginning of message and continuation of message. In end of message iam geting error "not reassembled" . I have the issue of counting the remaining length. In beginning of message iam haing the length of the PDU . the length iam passing to fragment_add_seq is guint 32</p><pre><code>                mte_frag_msg = fragment_add_seq_next(&amp;mte_reassembly_table,next_tvb, offset_payload, pinfo, mte_seqid, NULL, rem_length, more_frags);</code></pre><p>Is there any method to count in this value ? Iam not getting it.</p></div><div id="comment-38286-info" class="comment-info"><span class="comment-age">(02 Dec '14, 18:36)</span> umar</div></div><span id="38294"></span><div id="comment-38294" class="comment not_top_scorer"><div id="post-38294-score" class="comment-score"></div><div class="comment-text"><p>Hi Afrim,</p><p>iam not creating a tvb in beginning of message and continuation of message. Only in End of message (last message)i have created a tvb and proceess_reassemble. iam not getting message reassembled in colinfo.</p><p>Here i got problem. tvb itself not created because</p><p>my code like this</p><pre><code>         if (mte_tvb) { /* Reassembled */
col_append_str(pinfo-&gt;cinfo, COL_INFO,&quot;(Message reassembled) &quot;);             
       } else { /* Not successful reassembled message */
      col_append_str(pinfo-&gt;cinfo, COL_INFO,&quot;(Message fragment ) &quot;);
   }</code></pre><p>so tvb itself not created. please suggest.</p></div><div id="comment-38294-info" class="comment-info"><span class="comment-age">(02 Dec '14, 23:04)</span> umar</div></div></div><div id="comment-tools-37987" class="comment-tools"><span class="comments-showing"> showing 5 of 21 </span> <a href="#" class="show-all-comments-link">show 16 more comments</a></div><div class="clear"></div><div id="comment-37987-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

