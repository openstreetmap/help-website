+++
type = "question"
title = "Tracking a conversation across a source port change"
description = '''I have a protocol in which the client changes source ports regularly (the server has a single well known port). I&#x27;m trying to maintain a single conversation through this (each host can only have a single instance of the client). For example, I would expect this kind of traffic (52230 is the well kno...'''
date = "2014-01-05T18:10:00Z"
lastmod = "2014-01-07T10:09:00Z"
weight = 28592
keywords = [ "conversation", "dissector" ]
aliases = [ "/questions/28592" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tracking a conversation across a source port change](/questions/28592/tracking-a-conversation-across-a-source-port-change)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28592-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28592-score" class="post-score" title="current number of votes">0</div><span id="post-28592-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a protocol in which the client changes source ports regularly (the server has a single well known port). I'm trying to maintain a single conversation through this (each host can only have a single instance of the client). For example, I would expect this kind of traffic (52230 is the well known port):</p><pre><code>client:12345 -&gt; server:52230
server:52230 -&gt; client:12345
client:23456 -&gt; server:52230
server:55230 -&gt; client:23456</code></pre><p>This is one conversation. I've been trying to build a dissector that will handle this, and expected <code>NO_PORT_B</code> to be exactly what I needed, but I haven't been able to get it to work. In its most basic form, I try finding the conversation this way:</p><pre><code>conversation_t *conversation = find_conversation(pinfo-&gt;fd-&gt;num,
                &amp;pinfo-&gt;src, &amp;pinfo-&gt;dst,
                pinfo-&gt;ptype, 
                pinfo-&gt;srcport, pinfo-&gt;destport, 
                NO_PORT_B);</code></pre><p>If it doesn't exist, I try creating it this way:</p><pre><code>    conversation = conversation_new(pinfo-&gt;fd-&gt;num,
                &amp;pinfo-&gt;src, &amp;pinfo-&gt;dst,
                pinfo-&gt;ptype, 
                pinfo-&gt;srcport, pinfo-&gt;destport,
                NO_PORT2);</code></pre><p>That leads to:</p><pre><code>first column: CONV + &quot;!&quot; if a conversation was not found and was created
second column: source
third column: destination
forth column: found conversation (possibly created)
fifth column: counter number attached to conversation conversation_add_proto_data

CONV!:  172.16.244.1:61661  -&gt;  172.16.244.160:52230    =&gt;  0x10cd02d68 1
CONV!:  172.16.244.160:52230    -&gt;  172.16.244.1:61661  =&gt;  0x10cd02fe8 2
CONV!:  172.16.244.1:61669  -&gt;  172.16.244.160:52230    =&gt;  0x10cd033c8 3
CONV!:  172.16.244.160:52230    -&gt;  172.16.244.1:61669  =&gt;  0x10cd03578 4
CONV:   172.16.244.1:61669  -&gt;  172.16.244.160:52230    =&gt;  0x10cd033c8 3
CONV:   172.16.244.160:52230    -&gt;  172.16.244.1:61669  =&gt;  0x10cd03578 4
CONV:   172.16.244.1:61669  -&gt;  172.16.244.160:52230    =&gt;  0x10cd033c8 3</code></pre><p>No wildcarding appears to be happening. It isn't even joining symmetric communications like the first two packets.</p><p>I've tried many other combinations, including passing 0 instead of the port, or passing 52230 as the srcport rather than pinfo-&gt;srcport. I've even played with CONVERSATION_TEMPLATE, but I'm not quite certain what it's doing. Every combination has created multiple conversations.</p><p>Below is my full test code. I can post a small pcap if that's helpful.</p><hr /><pre><code>#include &lt;stdio.h&gt;    
#include &lt;config.h&gt;
#include &lt;epan/packet.h&gt;
#include &lt;epan/conversation.h&gt;

#define AMP_PORT 52230

static dissector_handle_t amp_handle;

static int proto_amp = -1;
static gint ett_amp = -1;

static int counter = 1;

static int
dissect_amp(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree) {
    col_set_str(pinfo-&gt; cinfo, COL_PROTOCOL, &quot;AMP&quot;);
    col_clear(pinfo-&gt;cinfo, COL_INFO);

    int newConv = 0;
    conversation_t *conversation = find_conversation(pinfo-&gt;fd-&gt;num,
                    &amp;pinfo-&gt;src, &amp;pinfo-&gt;dst,
                    pinfo-&gt;ptype, 
                    pinfo-&gt;srcport, pinfo-&gt;destport, 
                    NO_PORT_B);
    if (! conversation) {
        /* If we make a conversation, stick some unique data on it */
        newConv = 1;
        conversation = conversation_new(pinfo-&gt;fd-&gt;num,
                    &amp;pinfo-&gt;src, &amp;pinfo-&gt;dst,
                    pinfo-&gt;ptype, 
                    pinfo-&gt;srcport, pinfo-&gt;destport,
                    NO_PORT2);

        int *writeValue = malloc(sizeof(int));
        *writeValue = counter++;
        conversation_add_proto_data(conversation, proto_amp, writeValue);
        // conversation_set_dissector(conversation, amp_handle);
    }

    int *readValue = conversation_get_proto_data(conversation, proto_amp);

    printf(&quot;CONV%s:\t%s:%u\t-&gt;\t%s:%u\t=&gt;\t%p\t%d\n&quot;,
        newConv ? &quot;!&quot; : &quot;&quot;,
        ep_address_to_str(&amp;pinfo-&gt;src), 
        pinfo-&gt;srcport,
        ep_address_to_str(&amp;pinfo-&gt;dst),
        pinfo-&gt;destport,
        conversation,
        readValue ? *readValue : 0);

    return tvb_length(tvb);
}
void
proto_register_amp(void) {
    static hf_register_info hf_amp[] = {};
    static gint *ett_amp_arr[] = { &amp;ett_amp };

    proto_amp = proto_register_protocol(&quot;KACE Agent Messaging Protocol&quot;, &quot;AMP&quot;, &quot;amp&quot;);
    proto_register_field_array(proto_amp, hf_amp, array_length(hf_amp));
    proto_register_subtree_array(ett_amp_arr, array_length(ett_amp_arr));
}

void
proto_reg_handoff_amp(void)
{
    amp_handle = new_create_dissector_handle((new_dissector_t)dissect_amp, proto_amp);
    dissector_add_uint(&quot;tcp.port&quot;, AMP_PORT, amp_handle);
}</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-conversation" rel="tag" title="see questions tagged &#39;conversation&#39;">conversation</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jan '14, 18:10</strong></p><img src="https://secure.gravatar.com/avatar/ed9a0d8cd44b62539b141f6c10405db1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rob%20Napier&#39;s gravatar image" /><p><span>Rob Napier</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rob Napier has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Jan '14, 18:15</strong> </span></p></div></div><div id="comments-container-28592" class="comments-container"></div><div id="comment-tools-28592" class="comment-tools"></div><div class="clear"></div><div id="comment-28592-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28599"></span>

<div id="answer-container-28599" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28599-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28599-score" class="post-score" title="current number of votes">0</div><span id="post-28599-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Rob Napier has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Possible answer to my own question. Correct me if this is the hard way.</p><p>I believe I over-estimated the power of <code>NO_PORT_B</code>. This flag appears to mean exactly what it says. The second port is ignored, not "one of the ports" as I'd hoped. So the solution is to create the conversation such that the server is first, and always query it such that the server is first.</p><p>Since the server has a reliable port, this isn't too difficult. I can check <code>pinfo-&gt;srcport</code> and <code>pinfo-&gt;destport</code>, and whichever of them matches my well-known port, it goes as the "addr1/port1" parameters.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jan '14, 06:33</strong></p><img src="https://secure.gravatar.com/avatar/ed9a0d8cd44b62539b141f6c10405db1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rob%20Napier&#39;s gravatar image" /><p><span>Rob Napier</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rob Napier has one accepted answer">100%</span></p></div></div><div id="comments-container-28599" class="comments-container"><span id="28604"></span><div id="comment-28604" class="comment"><div id="post-28604-score" class="comment-score">1</div><div class="comment-text"><p>An alternative would be to do an exact match (i.e., pass 0 instead of <code>NO_PORT_B</code> to <code>find_conversation()</code> and 0 instead of <code>NO_PORT2</code> to <code>conversation_new()</code>) but replace the "non-well-known ports" with a constant value, such as 0. I'm not sure which method would be clearer and/or more efficient.</p></div><div id="comment-28604-info" class="comment-info"><span class="comment-age">(06 Jan '14, 08:32)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="28644"></span><div id="comment-28644" class="comment"><div id="post-28644-score" class="comment-score"></div><div class="comment-text"><p>I switched to the "0" port solution you mention. It seemed a bit more straightforward, and was successful. I haven't found a good harness for testing overall efficiency, though. Is there an established way to test dissector performance?</p></div><div id="comment-28644-info" class="comment-info"><span class="comment-age">(07 Jan '14, 10:09)</span> <span class="comment-user userinfo">Rob Napier</span></div></div></div><div id="comment-tools-28599" class="comment-tools"></div><div class="clear"></div><div id="comment-28599-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

