+++
type = "question"
title = "Illegal Message fragment"
description = '''Hello to all, I write a dissector for my protocol that reassebles multiple fragmet packets of 60 Kbytes each. For each fragment, a message (Message Reassembled) appears in the info column of Wireshark. For the last fragment (the reassebled packet) in info column the text [Illegal Message fragment] (...'''
date = "2012-06-07T08:10:00Z"
lastmod = "2012-06-07T08:10:00Z"
weight = 11740
keywords = [ "reassembly" ]
aliases = [ "/questions/11740" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Illegal Message fragment](/questions/11740/illegal-message-fragment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-11740-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello to all,</p><p>I write a dissector for my protocol that reassebles multiple fragmet packets of 60 Kbytes each. For each fragment, a message (Message Reassembled) appears in the info column of Wireshark. For the last fragment (the reassebled packet) in info column the text [Illegal Message fragment] (Message Reassembled) appears. Here I have to note that the message is correctly reassebled. Obviously the reassebly routine runs before if (tree).</p><p>Diging more the error flags of the fragment I found that 1 error occurs (FD_TOOLONGFRAGMENT) even in very small reassebled messages.</p><p>Example with 3 fragments:</p><p>1: Fragment ID = 1, Sequence number = 1, Last fragment flag = 0</p><p>2: Fragment ID = 1, Sequence number = 2, Last fragment flag = 0</p><p>3: Fragment ID = 1, Sequence number = 0, Last fragment flag = 1</p><p>My questions:</p><p>1) For every fragment the message (Message Reassembled) in the info column is correct?</p><p>2) Why the message [Illegal Message fragment] (Message Reassembled) appears for the last fragment?</p><p>3) Why FD_TOOLONGFRAGMENT error occurs in reassebly?</p><p>Here is a snapshot of my code</p><pre><code>    if (fragment == FRAME_FRAGMENT) 
    { /* fragmented */

        tvbuff_t* new_tvb = NULL;
        fragment_data *frag_msg  = NULL;

        // Read the packet id
        msg_seqid = tvb_get_letohs(tvb, offset); 
        offset += 2;

        // Read the fragment id
        msg_num = tvb_get_letohs(tvb, offset); 
        offset += 2;

        fragment_length = tvb_get_letohl(tvb, offset) &amp; 0xFFFFFFF;
        offset += 4;

        pinfo-&gt;fragmented = TRUE;

        if ((flags &amp; FRAME_LAST_FRAG) == FRAME_LAST_FRAG)
            last_fragment = TRUE;
        else
            last_fragment = FALSE;

        // The current reassembly functions has deep rooted assumptions that the
        // first fragment of a packet has sequence number (msg_num) = 0
        // In PCAP file you must first write all the fragments of the packets and
        // finally the 1st fragment of the packet. The 1st fragment of the packet (last 
        // in the PCAP file) should have msg_num = 0 and last_fragment = TRUE
        // Check if this is the last fragment (last_fragment == TRUE and msg_nub == 0)
        frag_msg = fragment_add_seq_check(tvb, offset, pinfo,
            msg_seqid,                          /* ID for fragments belonging together */
            fragment_table,                 /* list of message fragments */
            reassembled_table,              /* list of reassembled messages */
            msg_num,                            /* fragment sequence number */
            tvb_length_remaining(tvb, offset),  /* fragment length - to the end */
            !last_fragment);                        /* More fragments? */

        new_tvb = process_reassembled_data(tvb, offset, pinfo, &quot;Reassembled Message&quot;, frag_msg, &amp;msg_frag_items, NULL, pvs_frame_tree);

        if (frag_msg) 
        { /* Reassembled */
            col_append_str(pinfo-&gt;cinfo, COL_INFO, &quot; (Message Reassembled)&quot;);
        } 
        else 
        { /* Not last packet of reassembled Short Message */
            col_append_fstr(pinfo-&gt;cinfo, COL_INFO, &quot; (Message fragment %u)&quot;, msg_num);
        }

        if (new_tvb) 
        { /* take it all */
            next_tvb = new_tvb;
        } 
        else 
        { /* make a new subset */
            next_tvb = tvb_new_subset(tvb, offset, -1, -1);
        }
    }
    else 
    { /* Not fragmented */
        next_tvb = tvb_new_subset(tvb, 0, -1, -1);
    }

    pinfo-&gt;fragmented = save_fragmented;</code></pre></div><div id="question-tags" class="tags-container tags">reassembly</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jun '12, 08:10</strong></p><img src="https://secure.gravatar.com/avatar/a316969e99cc919815d47ae1fc022a55?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andapo&#39;s gravatar image" /><p>andapo<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andapo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Jun '12, 08:22</p></div></div><div id="comments-container-11740" class="comments-container"></div><div id="comment-tools-11740" class="comment-tools"></div><div class="clear"></div><div id="comment-11740-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

