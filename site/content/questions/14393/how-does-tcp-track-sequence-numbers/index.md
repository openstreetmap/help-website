+++
type = "question"
title = "How does TCP track sequence numbers?"
description = '''Hey Guys, So, I&#x27;m developing a dissector for a custom protocol (let&#x27;s call it foo for now), part of that protocol is an incrementing sequence number, which we call a heartbeat, it&#x27;s synonymous with &quot;Packet Number&quot; (this hbt = last_hbt++, very simple to check to see if we missed a packet). I&#x27;ve been ...'''
date = "2012-09-20T06:34:00Z"
lastmod = "2012-09-20T10:09:00Z"
weight = 14393
keywords = [ "development", "dissector", "custom" ]
aliases = [ "/questions/14393" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How does TCP track sequence numbers?](/questions/14393/how-does-tcp-track-sequence-numbers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14393-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hey Guys,</p><p>So, I'm developing a dissector for a custom protocol (let's call it foo for now), part of that protocol is an incrementing sequence number, which we call a heartbeat, it's synonymous with "Packet Number" (this hbt = last_hbt++, very simple to check to see if we missed a packet).</p><p>I've been trying to get this working with the conversation interface, but I've run into an issue. I can't work out how to compare two adjacent packets' heartbeats.</p><p>Here's what I've got for the conversation code.</p><pre><code>struct _foo_conversation_info
{
    guint16  heartbeat;
};

/* Code to actually dissect the packets */
static void
dissect_foo(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
{

/* some variables are omitted for brevity */

conversation_t *htbt_conv;
guint16     last_heartbeat;
struct _foo_conversation_info *proto_data;

/* Some function code is omitted for brevity */

SET_ADDRESS(&amp;null_addr, AT_NONE, 0, NULL);
htbt_conv = find_conversation(pinfo-&gt;fd-&gt;num, &amp;pinfo-&gt;src,
    &amp;null_addr, pinfo-&gt;ptype, pinfo-&gt;destport, 0x0,
    NO_ADDR2|NO_PORT2);
if(!htbt_conv){
    htbt_conv = conversation_new(pinfo-&gt;fd-&gt;num, &amp;pinfo-&gt;src,
    &amp;null_addr, pinfo-&gt;ptype, pinfo-&gt;destport, 0x0,
    NO_ADDR2|NO_PORT2);
}

proto_data  = conversation_get_proto_data(htbt_conv, proto_foo);

if(!proto_data){
    proto_data = se_alloc0(sizeof(struct _foo_conversation_info));
    conversation_add_proto_data(htbt_conv, proto_foo,
        proto_data);

    last_heartbeat  = 0;
    proto_data-&gt;heartbeat = tvb_get_ntohs(tvb, 1);
    col_set_str(pinfo-&gt;cinfo, COL_INFO, &quot;FOO&quot;);
}else{

    last_heartbeat  = proto_data-&gt;heartbeat;
    proto_data-&gt;heartbeat = tvb_get_ntohs(tvb, 1);

    if((proto_data-&gt;heartbeat - last_heartbeat) != 1){
        col_set_str(pinfo-&gt;cinfo, COL_INFO, &quot;FOO - Skipped Heartbeat!&quot;);
    }else{
        col_set_str(pinfo-&gt;cinfo, COL_INFO, &quot;FOO&quot;);
    }
}</code></pre><p>Every packet in the packet list is marked "Skipped Heartbeat!", when it really shouldn't be (I have a packet generator with a switch so I can inject bad packets BTW).</p><p>I guess this is because the dissector isn't being passed the packets in order, as I would expect, so my next step was to look at TCP to see how it does it(packet-tcp.c &amp; packet-tcp.h), but I just can't follow it, there are whole function chains which seem to go nowhere, so, how the hell do I step through the conversation chain and test for no sequential packets??</p><p>Thanks in advance,</p><p>Craig.</p></div><div id="question-tags" class="tags-container tags">development dissector custom</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Sep '12, 06:34</strong></p><img src="https://secure.gravatar.com/avatar/7f557535084abef24cd30661f9daefad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CTNOBLE&#39;s gravatar image" /><p>CTNOBLE<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CTNOBLE has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Sep '12, 07:01</p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-14393" class="comments-container"></div><div id="comment-tools-14393" class="comment-tools"></div><div class="clear"></div><div id="comment-14393-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="14394"></span>

<div id="answer-container-14394" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14394-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The problem is that Wireshark will run through the packets once sequentially, but also goes through the packets at random to create the protocol tree to display.</p><p>Every frame will be marked "visited" on the first run, so you can use this to flag to do the dissection of each frame. If your dissection depends on the order of frames, use the following macro:</p><pre><code>if (!PINFO_FD_VISITED(pinfo)) {
    &lt;your code here&gt;
}</code></pre><p>Also make sure that you need to save your dissection results that are sequence dependent in "per packet data" in the conversation table. See "2.5 Per-packet information." in doc/README.developer. For more details :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '12, 07:07</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-14394" class="comments-container"><span id="14395"></span><div id="comment-14395" class="comment"><div id="post-14395-score" class="comment-score"></div><div class="comment-text"><p>Thanks for posting an answer, I do appreciate it, but I need some more info please.</p><p>My question my have been a bit vague on exactly what I wanted to know.</p><p>I was aware that Wireshark will run through sequentially the first time and then might run through at random on any subsiquent runs.</p><p>Which is what the conversation is for, I was under the impression that the "find_conversation()" function would return a different per-packet data structure based on the frame number (first argument to that function), is that true? That said your "visited" macro looks more robust, so I'll go with that.</p></div><div id="comment-14395-info" class="comment-info"><span class="comment-age">(20 Sep '12, 07:25)</span> CTNOBLE</div></div><span id="14396"></span><div id="comment-14396" class="comment"><div id="post-14396-score" class="comment-score"></div><div class="comment-text"><p><strong>not enough chars for full comment</strong></p><p>If I was to call find_conversation(pinfo-&gt;fd-&gt;num--, ...) would that return the information from the previous frame in my stream or are the frame numbers not necessarily continuous? Would using a simple global variable be safe enough?</p><p>Basically how do I get data from the previous frame dissection into the current one?</p><p>Cheers, Craig.</p></div><div id="comment-14396-info" class="comment-info"><span class="comment-age">(20 Sep '12, 07:26)</span> CTNOBLE</div></div><span id="14398"></span><div id="comment-14398" class="comment"><div id="post-14398-score" class="comment-score"></div><div class="comment-text"><p>find_conversation() will just give you the index to the conversation data based on addresses, ports and frame_number (as there might be more conversations with the same addresses/ports credentials).</p><p>A global variable will not do and neither will data inside your conversation data object, as you need to have the history at hand when your dissector is called for a specific frame.</p><p>You need to use the per-packet data to store states per packet.</p><p>So, please read the before mentioned paragraph of README.developer, which kind of explains this in more detail.</p></div><div id="comment-14398-info" class="comment-info"><span class="comment-age">(20 Sep '12, 08:01)</span> SYN-bit ♦♦</div></div><span id="14400"></span><div id="comment-14400" class="comment"><div id="post-14400-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the clarification, on conversations.</p><p>So here's some psudo code for what I think I need to do:</p><pre><code>if(packet not seen before){
    per-packet.lastheartbeat   &lt;- conversation.lastheartbeat
    conversation.lastheartbeat &lt;- heartbeat
}else{
    lastheartbeat &lt;- per-packet.lastheartbeat

    if(heartbeat-lastheartbeat != 1)
    {
        do some error stuff
    }
}</code></pre><p>I'll keep experimenting and post back here next week with the actual code just in case anyone else wants to see how I ended up solving this.</p><p>Cheers, Craig.</p></div><div id="comment-14400-info" class="comment-info"><span class="comment-age">(20 Sep '12, 09:44)</span> CTNOBLE</div></div><span id="14402"></span><div id="comment-14402" class="comment"><div id="post-14402-score" class="comment-score"></div><div class="comment-text"><p>Not exactly, the only time to detect if a heartbeat was lost is in the sequential run, so the check whether a heartbeat was lost should be done in the "packet not seen" block. The result should be stored in the per-packet information.</p></div><div id="comment-14402-info" class="comment-info"><span class="comment-age">(20 Sep '12, 10:04)</span> SYN-bit ♦♦</div></div><span id="14403"></span><div id="comment-14403" class="comment not_top_scorer"><div id="post-14403-score" class="comment-score"></div><div class="comment-text"><p>Something like this:</p><pre><code>if(packet not seen before){
    if( packet.heartbeat - conversation.lastheartbeat != 1)
        per-packet.skippedheartbeat = TRUE
    } else {
        per-packet.skippedheartbeat = FALSE
    }
    conversation.lastheartbeat = packet.heartbeat
}

if ( tree ) {
    ...
    get-per-packet-information()
    if( per-packet.skippedheartbeat ) {
       show-error-in-tree()
    }
    ...
}</code></pre></div><div id="comment-14403-info" class="comment-info"><span class="comment-age">(20 Sep '12, 10:05)</span> SYN-bit ♦♦</div></div><span id="14405"></span><div id="comment-14405" class="comment not_top_scorer"><div id="post-14405-score" class="comment-score"></div><div class="comment-text"><p>Ahhhh, this just showed up when I hit OK for my code below.</p><p>I guess not retesting everytime might reduce the processing power needed, but wouldn't this be functionally equivalent code?</p><p>Good practice is always worth the effort - I'll change it next week and edit my answer post.</p><p>Thanks again!</p></div><div id="comment-14405-info" class="comment-info"><span class="comment-age">(20 Sep '12, 10:11)</span> CTNOBLE</div></div></div><div id="comment-tools-14394" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-14394-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14404"></span>

<div id="answer-container-14404" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14404-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>OK, So I was able to get this working a lot faster than I thought. Here's my code.</p><pre><code>    SET_ADDRESS(&amp;null_addr, AT_NONE, 0, NULL);

        pcket_data = p_get_proto_data(pinfo-&gt;fd, proto_foo);

        if (!(pinfo-&gt;fd-&gt;flags.visited)){
            if(!pcket_data){
                pcket_data = se_alloc(sizeof(struct _foo_packet_info));
                p_add_proto_data(pinfo-&gt;fd, proto_foo, pcket_data);
            }

            htbt_conv = find_conversation(pinfo-&gt;fd-&gt;num, &amp;pinfo-&gt;src,
                &amp;null_addr, pinfo-&gt;ptype, pinfo-&gt;destport, 0x0,
                NO_ADDR2|NO_PORT2);

            if(!htbt_conv){
                htbt_conv = conversation_new(pinfo-&gt;fd-&gt;num, &amp;pinfo-&gt;src,
                &amp;null_addr, pinfo-&gt;ptype, pinfo-&gt;destport, 0x0,
                NO_ADDR2|NO_PORT2);
            }

            proto_data  = conversation_get_proto_data(htbt_conv, proto_foo);

            if(!proto_data){
                proto_data = se_alloc0(sizeof(struct _foo_conversation_info));
                conversation_add_proto_data(htbt_conv, proto_foo,
                    proto_data);

                last_heartbeat  = 0;
            }

            this_heartbeat = tvb_get_ntohs(tvb, 2);
            last_heartbeat = proto_data-&gt;heartbeat;
            proto_data-&gt;heartbeat = this_heartbeat;
            pcket_data-&gt;last_heartbeat = last_heartbeat;
        }

        last_heartbeat  = pcket_data-&gt;last_heartbeat;
        this_heartbeat = tvb_get_ntohs(tvb, 2);

        col_clear(pinfo-&gt;cinfo, COL_INFO);

        if((this_heartbeat - last_heartbeat) != 1){
            col_set_str(pinfo-&gt;cinfo, COL_INFO, &quot;foo Aurora Packet - Skipped Heartbeat!&quot;);
        }else{          
            col_set_str(pinfo-&gt;cinfo, COL_INFO, &quot;foo Aurora Packet&quot;);
        }</code></pre><p>If anyone has comments on the style or safety of my code then that would be appreciated, otherwise I'm going to mark this as the answer early next week.</p><p>Thankyou SYN-bit for your help and guidance.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '12, 10:09</strong></p><img src="https://secure.gravatar.com/avatar/7f557535084abef24cd30661f9daefad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CTNOBLE&#39;s gravatar image" /><p>CTNOBLE<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CTNOBLE has no accepted answers">0%</span></p></div></div><div id="comments-container-14404" class="comments-container"></div><div id="comment-tools-14404" class="comment-tools"></div><div class="clear"></div><div id="comment-14404-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

