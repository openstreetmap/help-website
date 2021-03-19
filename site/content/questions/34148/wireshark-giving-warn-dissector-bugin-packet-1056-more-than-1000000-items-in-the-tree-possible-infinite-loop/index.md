+++
type = "question"
title = "wireshark giving Warn Dissector bug,in packet 1056: More than 1000000 items in the tree -- possible infinite loop"
description = '''Hi currently i&#x27;ve written code for own plugin for RRC Messages by taking existing code reference from existing wireshark e.g:packet-gsm_rlcmac.c and i&#x27;m using some API&#x27;s also from epan/dissectors,after a lot of struggle,i compiled my code and i&#x27;m facing this error Warn Dissector bug, protocol MY_PRO...'''
date = "2014-06-24T22:59:00Z"
lastmod = "2014-06-24T23:02:00Z"
weight = 34148
keywords = [ "giving", "warn", "dissector", "bug", "wireshark" ]
aliases = [ "/questions/34148" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark giving Warn Dissector bug,in packet 1056: More than 1000000 items in the tree -- possible infinite loop](/questions/34148/wireshark-giving-warn-dissector-bugin-packet-1056-more-than-1000000-items-in-the-tree-possible-infinite-loop)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34148-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi currently i've written code for own plugin for RRC Messages by taking existing code reference from existing wireshark e.g:packet-gsm_rlcmac.c and i'm using some API's also from epan/dissectors,after a lot of struggle,i compiled my code and i'm facing this error Warn Dissector bug, protocol MY_PROTO, in packet 1056: More than 1000000 items in the tree -- possible infinite loop,Here MY_PROTO is my protocol name,can any body help me to resolve this issue..</p></div><div id="question-tags" class="tags-container tags">giving warn dissector bug wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jun '14, 22:59</strong></p><img src="https://secure.gravatar.com/avatar/7596daf4fb3556a397822344b20e2362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sagar&#39;s gravatar image" /><p>sagar<br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sagar has no accepted answers">0%</span></p></div></div><div id="comments-container-34148" class="comments-container"><span id="34150"></span><div id="comment-34150" class="comment"><div id="post-34150-score" class="comment-score"></div><div class="comment-text"><p>sample of code :</p><pre><code>    csnStream_t  ar;
    //proto_item   *ti = NULL;
    //proto_tree   *rrc_tree = NULL;
    proto_item   *ti;
    proto_tree   *rrc_tree;
    guint8 bit_offset = 0;
    bit_length = tvb_length(tvb) * 8;
    data-&gt;u.MESSAGE_TYPE = tvb_get_bits8(tvb, bit_offset, 8);

    bit_offset = initial_bit_offset;

    ti = proto_tree_add_protocol_format(tree,proto_gmr3g_rrc,tvb,bit_offset &gt;&gt; 3,-1,&quot;RRC: %s (%d) (Uplink)&quot;,
                    val_to_str_ext(data-&gt;u.MESSAGE_TYPE, &amp;dl_rrc_message_type_vals_ext, &quot;Unknown Messsage Type&quot;),data-&gt;u.MESSAGE_TYPE);

    rrc_tree =  proto_item_add_subtree(ti,ett_rrc);

    /* Initialize the contexts */
    csnStreamInit(&amp;ar,bit_offset,bit_length-bit_offset);</code></pre><p>// ar.remaining_bits_len = bit_length-bit_offset; // ar.bit_offset = bit_offset;</p><pre><code>    switch (data-&gt;u.MESSAGE_TYPE)

    {

            case MT_SIGNALLING_RB_INFORMATION_SETUP:
                    {
                            csnStreamDissector(rrc_tree,&amp;ar,CSNDESCR(Packet_Signalling_Info_Setup_t),tvb,&amp;data-&gt;u.Packet_Signalling_Info_Setup,ett_rrc);
                            break;

                    }

            default:
                    break;</code></pre></div><div id="comment-34150-info" class="comment-info"><span class="comment-age">(24 Jun '14, 23:16)</span> sagar</div></div></div><div id="comment-tools-34148" class="comment-tools"></div><div class="clear"></div><div id="comment-34148-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34149"></span>

<div id="answer-container-34149" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34149-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As it says you probably have an infinite or long loop in your program, try running it under a debugger. Otherwise we need to see the code.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '14, 23:02</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-34149" class="comments-container"><span id="34156"></span><div id="comment-34156" class="comment"><div id="post-34156-score" class="comment-score"></div><div class="comment-text"><p>Hi i've added sample of code any body can verify it and let me know where exactly problem is ....</p></div><div id="comment-34156-info" class="comment-info"><span class="comment-age">(25 Jun '14, 02:48)</span> sagar</div></div><span id="34172"></span><div id="comment-34172" class="comment"><div id="post-34172-score" class="comment-score"></div><div class="comment-text"><p>The problem probably lies in your CSN.1 description for the message. There is no loop in the code sample you pasted (which seems partial as data-&gt;u.MESSAGE_TYPE is never initialized), so we cannot help you.</p></div><div id="comment-34172-info" class="comment-info"><span class="comment-age">(25 Jun '14, 09:06)</span> Pascal Quantin</div></div></div><div id="comment-tools-34149" class="comment-tools"></div><div class="clear"></div><div id="comment-34149-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

