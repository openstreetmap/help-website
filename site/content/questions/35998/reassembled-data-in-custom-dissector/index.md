+++
type = "question"
title = "Reassembled data in custom dissector"
description = '''Hi, Iam in the process of developing my custom dissector on top of UDP(wireshark).  I have a packet data spli in many packets and reassembled together when i get &quot;end of message&quot; key. I have 3 keys 1. beginning of message 2. continuation of message 3. end of message.  I have to display the data (rea...'''
date = "2014-09-04T03:52:00Z"
lastmod = "2014-09-22T05:49:00Z"
weight = 35998
keywords = [ "reassembled", "data" ]
aliases = [ "/questions/35998" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Reassembled data in custom dissector](/questions/35998/reassembled-data-in-custom-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35998-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Iam in the process of developing my custom dissector on top of UDP(wireshark).<br />
</p><p>I have a packet data spli in many packets and reassembled together when i get "end of message" key. I have 3 keys 1. beginning of message 2. continuation of message 3. end of message.</p><p>I have to display the data (reassembled ) in a seperate TAB. (only when i get end of message key i have to do this)</p><p>I have gone through the below code and could not understand</p><pre><code>              #include &lt;epan/reassemble.h&gt;
                ...
               save_fragmented = pinfo-&gt;fragmented;
            flags = tvb_get_guint8(tvb, offset); offset++;
            if (flags &amp; FL_FRAGMENT) { /* fragmented */
            tvbuff_t* new_tvb = NULL;
           fragment_data *frag_msg = NULL;
              guint16 msg_seqid = tvb_get_ntohs(tvb, offset); offset += 2;
              guint16 msg_num = tvb_get_ntohs(tvb, offset); offset += 2;
              pinfo-&gt;fragmented = TRUE;
               frag_msg = fragment_add_seq_check(tvb, offset, pinfo,
              msg_seqid, /* ID for fragments belonging together */
                  msg_fragment_table, /* list of message fragments */
                 msg_reassembled_table, /* list of reassembled messages */
                 msg_num, /* fragment sequence number */
                tvb_length_remaining(tvb, offset), /* fragment length - to the end */
                flags &amp; FL_FRAG_LAST); /* More fragments? */

                new_tvb = process_reassembled_data(tvb, offset, pinfo,&quot;Reassembled      Message&quot;, frag_msg, msg_frag_items,NULL, msg_tree);

       if (frag_msg) { /* Reassembled */
       col_append_str(pinfo-&gt;cinfo, COL_INFO,&quot; (Message Reassembled)&quot;);
       } else { /* Not last packet of reassembled Short Message */
       col_append_fstr(pinfo-&gt;cinfo, COL_INFO,
        &quot; (Message fragment %u)&quot;, msg_num);
                        }
      if (new_tvb) { /* take it all */
        next_tvb = new_tvb;
        } else { /* make a new subset */
        next_tvb = tvb_new_subset(tvb, offset, -1, -1);
          }
        }
              else { /* Not fragmented */
                      next_tvb = tvb_new_subset(tvb, offset, -1, -1);
                        }
                       .....
                      pinfo-&gt;fragmented = save_fragmented;</code></pre><p>Please suggest! Note: I do not have any seq number for each packet data..</p></div><div id="question-tags" class="tags-container tags">reassembled data</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Sep '14, 03:52</strong></p><img src="https://secure.gravatar.com/avatar/1339589a92af9455063c09e56bfc6299?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="umar&#39;s gravatar image" /><p>umar<br />
<span class="score" title="26 reputation points">26</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="umar has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Sep '14, 00:46</p></div></div><div id="comments-container-35998" class="comments-container"></div><div id="comment-tools-35998" class="comment-tools"></div><div class="clear"></div><div id="comment-35998-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="36148"></span>

<div id="answer-container-36148" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36148-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Go into epan/reassemble.h and epan/reassemble.c. There you'll find all the details in which you can reassemble fragments in a way suitable for your protocol.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '14, 04:12</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-36148" class="comments-container"><span id="36388"></span><div id="comment-36388" class="comment"><div id="post-36388-score" class="comment-score"></div><div class="comment-text"><p>Hi Jaap , Thanks for your reply. my requirement is , i have n number of frames and i have three different data .. 1. beginning of message 2. continuation of message 3, end of message. when beginning of message i have to store the data and continuation of message data alo be included and when it comes to end of data i have to display it in a separate tab (reassembled data and process it). i have gone through reassemble.c and could not understand. can you help me on this.</p><p>my packet dissection is byte by byte...</p><p>Thanks</p></div><div id="comment-36388-info" class="comment-info"><span class="comment-age">(16 Sep '14, 19:57)</span> umar</div></div></div><div id="comment-tools-36148" class="comment-tools"></div><div class="clear"></div><div id="comment-36148-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="36506"></span>

<div id="answer-container-36506" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36506-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>To reassemble your packets you need some information such as the ID of your fragment, the offset of the current segment in the reassembled packet, if it's the last fragment or not, and more (It depend on your protocol). All these information are passed to the fragment_add_seq_check() to attempt a reassembly.</p><p>You can also see exemple of reassemble interface in the epan/dissectors folder (packet-ipv6.c, packet-6lowpan.c, etc.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '14, 05:49</strong></p><img src="https://secure.gravatar.com/avatar/4ec6105789137df01b9abed5fcb9ab95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Afrim&#39;s gravatar image" /><p>Afrim<br />
<span class="score" title="160 reputation points">160</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Afrim has 2 accepted answers">22%</span></p></div></div><div id="comments-container-36506" class="comments-container"><span id="37028"></span><div id="comment-37028" class="comment"><div id="post-37028-score" class="comment-score"></div><div class="comment-text"><p>Hi Afrim ,</p><p>do i need to create ID on my own? because i have raw data which does not comes with ID . Can \you help me to explain step by step procedure. (define table, init table add data to reassemble data etc..) I tried to understand the existing code and could not understand.How to display the reassembled data in a separate tab ? below image for reference.</p><p>I have 3 diff type of packet pdu 1. beginning of message 2. continuation of message 3, end of message each type contain data in it. for example beginning of message got 20 octets and continuation of message got 10 octets and end of message got 15 octets. I need to reassemble all these 45 octets of data in End of message sequence. Please suggest</p><p>Thanks</p><p>RAj</p></div><div id="comment-37028-info" class="comment-info"><span class="comment-age">(14 Oct '14, 01:58)</span> umar</div></div><span id="37030"></span><div id="comment-37030" class="comment not_top_scorer"><div id="post-37030-score" class="comment-score"></div><div class="comment-text"><p><img src="https://osqa-ask.wireshark.org/upfiles/ws_qs.bmp" alt="alt text" /></p></div><div id="comment-37030-info" class="comment-info"><span class="comment-age">(14 Oct '14, 02:39)</span> umar</div></div><span id="37031"></span><div id="comment-37031" class="comment"><div id="post-37031-score" class="comment-score">1</div><div class="comment-text"><p>The ID is needed cause when you receive your packets in Wireshark they are not sorted by fragmentation order. For exemple you will not receive :<br />
Packet 1 : fragmentation, beginning of message<br />
Packet 2 : fragmentation, continuation of message<br />
Packet 3 : fragmentation, end of message<br />
</p><p>But it will be something like :<br />
Packet 1 : fragmentation, beginning of message<br />
Packet 2 : fragmentation, continuation of message<br />
Packet 3 : fragmentation, beginning of message<br />
Packet 4 : fragmentation, beginning of message<br />
Packet 5 : fragmentation, continuation of message<br />
Packet 6 : fragmentation, end of message<br />
etc...<br />
In this case you dont know if packet 6 is end of message of packet 5 or packet 2. Neither you know if packet 5 is continuation of packet 4 or 3. That's why we use IDs. But it realy depend on your protocol, if your protocol does not allow multiple "beginning of message" you can set ID to any value.</p><p>Then all what you need is to tell if there is more fragments(you have this information) to wait for this ID, if no the ressembly will occur. Ofc you have to tell the length of the fragment as the code of your first post says.</p></div><div id="comment-37031-info" class="comment-info"><span class="comment-age">(14 Oct '14, 03:04)</span> Afrim</div></div><span id="37032"></span><div id="comment-37032" class="comment not_top_scorer"><div id="post-37032-score" class="comment-score"></div><div class="comment-text"><p>Hi Afrim,</p><p>Thanks for the reply . Got it, Thanks. for my protocol only one beginning of message and may be multiple continuation of message and 1 end of message. Now i have gone through many protocols to understand how to add the data into reassemble table. As iam new to this , could you help me to guide step by step procedure to add data to table and display in a separate tab like in the image. when it comes to end of message!</p><pre><code>         Packet 1 : fragmentation,                         beginning of message

         Packet 23 : fragmentation, continuation of message
         Packet 44 : fragmentation, continuation of message
         Packet 57 : fragmentation, continuation of message
         Packet 69 : fragmentation,                           end of message</code></pre></div><div id="comment-37032-info" class="comment-info"><span class="comment-age">(14 Oct '14, 03:11)</span> umar</div></div><span id="37037"></span><div id="comment-37037" class="comment"><div id="post-37037-score" class="comment-score">1</div><div class="comment-text"><p>@mrajsekar</p><p>Unfortunately all the protocols that do reassembly in this way are somewhat complicated, if you search for all files in epan\dissectors that include <code>fragment_add_seq_next</code>, you will see all the current dissectors that use the method you need. Try looking at those, but be aware they are all likely to have a lot of "extras" that you'll have to work through.</p><p>You'll need to understand "conversations" (README.dissector sect 2.2) and reassembly (in epan\reassemble.h) to complete your dissector.</p><p>I think you need to use <code>fragment_add_seq_next</code> as you don't have a fragment id, so must assume all fragments come in order, first to last.</p></div><div id="comment-37037-info" class="comment-info"><span class="comment-age">(14 Oct '14, 05:27)</span> grahamb ♦</div></div><span id="37046"></span><div id="comment-37046" class="comment not_top_scorer"><div id="post-37046-score" class="comment-score"></div><div class="comment-text"><p>Thanks Grahamb!I will try this.</p></div><div id="comment-37046-info" class="comment-info"><span class="comment-age">(14 Oct '14, 18:49)</span> umar</div></div><span id="37326"></span><div id="comment-37326" class="comment not_top_scorer"><div id="post-37326-score" class="comment-score"></div><div class="comment-text"><p>Hi, What is the difference between conversation and reassembly and fragmentation???</p><p>for me iam developing dissector to ruunnning on top of UDP port XXXX and my PDU data comes in many packets..</p><p>Not from other destination port..</p><p>Can you please Clarify?</p><p>for me i have beginning of message in that i have a data length field : ex. 24 bytes in that beginning of message contains 15 Bytes pdu data</p><p>continuation of message contains 5 bytes and another continuaton of message contains 2 bytes and then End of Message contains 2 bytes.</p><p>How can i achieve this reassembly . using conversation or using reassembly??</p><p>i have gone through RTP and some other files but i get confuse with it. please help me on this</p><p>Thanks</p></div><div id="comment-37326-info" class="comment-info"><span class="comment-age">(24 Oct '14, 01:17)</span> umar</div></div><span id="37328"></span><div id="comment-37328" class="comment"><div id="post-37328-score" class="comment-score">1</div><div class="comment-text"><p>Fragmentation (and subsequent reassembly) occurs when an application pdu can be split across multiple transport layer segments, e.g. your pdu arrives split over multiple tcp segments. The application dissector can tell the tcp dissector how much data it needs (read from the application pdu header) and the tcp dissector then reassembles incoming data until it has enough to hand back to the application dissector. Wireshark has built-in support for tcp reassembly, for other transport protocols the application dissector will have to manage reassembly itself.</p><p>Conversation is where the application dissector may be interested in multiple application pdu's, e.g request\response.</p></div><div id="comment-37328-info" class="comment-info"><span class="comment-age">(24 Oct '14, 02:01)</span> grahamb ♦</div></div><span id="37331"></span><div id="comment-37331" class="comment not_top_scorer"><div id="post-37331-score" class="comment-score"></div><div class="comment-text"><p>Should i add id to each byte of the data ? please help me on this i really could not understand this. i got stuck in this for long time. i have completed 95% of the dissector and once i did this i can complete my work.</p></div><div id="comment-37331-info" class="comment-info"><span class="comment-age">(24 Oct '14, 02:42)</span> umar</div></div><span id="37368"></span><div id="comment-37368" class="comment not_top_scorer"><div id="post-37368-score" class="comment-score"></div><div class="comment-text"><p>Is this code will satisfy my requirement?<br />
</p><pre><code>      dissect_proto(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree) {
        while [bytes remain in tvb from offset]
            if [pdu length is unknown]
        found = fragment_get(pinfo, 0, fragment_table);
        if [fragment was found]
            [loop through found-&gt;next and add total_length and data]
            buffer = tvb_new_real_data(data, total_length, total_length);
        else
            buffer = tvb_new_subset(tvb, offset, ...);

        bytes_available = tvb_length(buffer);
        pdu_length = get_pdu_length(buffer, &amp;pdu_offset);
        if [pdu length is known and is smaller than bytes remaining]
            complete = TRUE;
        /* bytes_to_consume is min(pdu_length, bytes_available) */
        pinfo-&gt;fragmented = !complete;
        head = fragment_add(tvb, offset, pinfo, 0, fragment_table,
                offset, bytes_to_consume, !complete);
        next_tvb = process_reassembled_data(tvb, offset,                             pinfo, &quot;Reassembled packet&quot;, head, &amp;proto_frag_items, NULL, tree);
        offset += bytes_to_consume;</code></pre></div><div id="comment-37368-info" class="comment-info"><span class="comment-age">(26 Oct '14, 23:34)</span> umar</div></div><span id="37371"></span><div id="comment-37371" class="comment"><div id="post-37371-score" class="comment-score">1</div><div class="comment-text"><p>I don't really understand the purpose of your while loop and I think in your case you dont need conversation interface.So, as Grahamb said, assuming your data comes in order you dont need an ID, then use fragment_add_seq_next().<br />
</p><p>Here is the prototype of this function</p><pre><code>fragment_head 
fragment_add_seq_next(reassembly_table table, tvbuff_t tvb, const int offset,
              const packet_info pinfo, const guint32 id,
              const void *data, const guint32 frag_data_len,
              const gboolean more_frags);</code></pre><p>So you got the reassembly table, tvb buffer, the current offset, pinfo structure, as you dont need ID I would have set it to 0 (or any other value), set data* to NULL, frag_data_len is the length of your fragment and more_frag is a flag to tell if there is more fragment to wait. You got all these information so just fill in.</p></div><div id="comment-37371-info" class="comment-info"><span class="comment-age">(27 Oct '14, 04:25)</span> Afrim</div></div><span id="37424"></span><div id="comment-37424" class="comment not_top_scorer"><div id="post-37424-score" class="comment-score"></div><div class="comment-text"><p>Hi Afrim,</p><p>Thank you so much! This will be really helpful. I will Try this!</p><p>Thanks Grahamb!</p></div><div id="comment-37424-info" class="comment-info"><span class="comment-age">(28 Oct '14, 20:33)</span> umar</div></div><span id="37453"></span><div id="comment-37453" class="comment not_top_scorer"><div id="post-37453-score" class="comment-score"></div><div class="comment-text"><p>Hi Afrim grahamb,</p><p>Need your help.</p><pre><code>             process_reassembled_data( next_tvb, offset_payload, pinfo, &quot;Reassembled PDU&quot;, bgan_frag_msg,&amp;ALSIGPDU, NULL, FT_BCnPDU_tree );</code></pre><p>In this parameter 6 i need to pass a function ALSIG PDU How it is possible?</p><p>Those tvb i have reassemblesd had to be proceessed in ALSIG PDU function. Please suggest some idea,</p></div><div id="comment-37453-info" class="comment-info"><span class="comment-age">(29 Oct '14, 23:10)</span> umar</div></div><span id="37455"></span><div id="comment-37455" class="comment not_top_scorer"><div id="post-37455-score" class="comment-score"></div><div class="comment-text"><p>save_fragmented = pinfo-&gt;fragmented;</p><pre><code>                                        pinfo-&gt;fragmented = TRUE;

                                my_frag_msg = fragment_add_seq_check(&amp;my_reassembly_table,tvb, offset, pinfo, my_seqid, NULL,0, reassebled_data_total_length, more_frags);

                                    my_tvb = process_reassembled_data( tvb, offset, pinfo, &quot;Reassembled PDU&quot;, my_frag_msg,&amp;my_frag_items, NULL, FT_PDU_tree );

SIGPDU(my_tvb, pinfo, tree);</code></pre><p>What is wrong my reassembly not happening?</p></div><div id="comment-37455-info" class="comment-info"><span class="comment-age">(30 Oct '14, 01:15)</span> umar</div></div><span id="37456"></span><div id="comment-37456" class="comment not_top_scorer"><div id="post-37456-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>I have</p><p>beginning of the message (in this pdu i have info about total msg length) continuation of the message end of message</p><p>I have set a global variable to take the total length and substract it from pdu length of beginning of msg and continuation of message when it comes to end of message i have added the pdu data to the reassembled table and then used process_reassembled_data to process. But its not happening</p><p>beginning of message and continuation of message shows correct for me. I dont know whether reassembled table got data added or not. please suggest!</p><p>I have used</p><pre><code>           fragment_add_seq_next(&amp;bgan_reassembly_table,next_tvb, offset_payload, pinfo, bgan_seqid, NULL,reassebled_data_total_length, more_frags);</code></pre></div><div id="comment-37456-info" class="comment-info"><span class="comment-age">(30 Oct '14, 02:09)</span> umar</div></div><span id="37482"></span><div id="comment-37482" class="comment not_top_scorer"><div id="post-37482-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>My comple re assembly code is below</p><p>Please suggest what i have missed or issue</p><pre><code>        static reassembly_table mine_reassembly_table;

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

        ALSIGPDU(mine_tvb, pinfo, tree);</code></pre></div><div id="comment-37482-info" class="comment-info"><span class="comment-age">(30 Oct '14, 19:26)</span> umar</div></div><span id="37483"></span><div id="comment-37483" class="comment not_top_scorer"><div id="post-37483-score" class="comment-score"></div><div class="comment-text"><p>Also How to calculate the length of the reassembled table? because i have set a variable reassebled_data_total_length and get the total length. Then when beginning continuation of msg pdu data i hv substract the pdu data length from the total length. Here when i open wireshark and open the capture file, if i go directly to the end of message pdu reassebled_data_total_length it shows as zero. but if i open beginning of msg and then open end of msg pdu it shows corrrect. please help</p></div><div id="comment-37483-info" class="comment-info"><span class="comment-age">(30 Oct '14, 19:48)</span> umar</div></div><span id="39905"></span><div id="comment-39905" class="comment not_top_scorer"><div id="post-39905-score" class="comment-score"></div><div class="comment-text"><p>Hi Afrim and Grahamb,</p><p>Sorry . My message comes with sequence Number . based on the seq num i need to reassemble.</p><p>i have used fragment_add_seq_check but my fragment table itself always returning NULL.</p><p>Can i hae your mail id so that i can share my code. i think you can solve that in minute, please help</p><p>My latest question posted here</p><p><a href="https://ask.wireshark.org/questions/39824/fragmentation-error-status-access-violation">https://ask.wireshark.org/questions/39824/fragmentation-error-status-access-violation</a></p><p><a href="https://ask.wireshark.org/questions/39885/pdcp-layer-pdu-rfc-2507-arq-mechanism">https://ask.wireshark.org/questions/39885/pdcp-layer-pdu-rfc-2507-arq-mechanism</a></p></div><div id="comment-39905-info" class="comment-info"><span class="comment-age">(17 Feb '15, 00:47)</span> umar</div></div></div><div id="comment-tools-36506" class="comment-tools"><span class="comments-showing"> showing 5 of 18 </span> <a href="#" class="show-all-comments-link">show 13 more comments</a></div><div class="clear"></div><div id="comment-36506-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

