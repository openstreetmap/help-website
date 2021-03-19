+++
type = "question"
title = "couple of messages in one frame"
description = '''I wrote a dissector, I found one packet which contains couple of different/indifferent messages inside it, Can someone point on the problem ? Is this even a problem ? I reassemble TCP packets... This is the function of dissection: (FRAME_HEADER_LEN = 8) static void dissect_PROTOC(tvbuff_t *tvb, pack...'''
date = "2013-02-25T06:18:00Z"
lastmod = "2013-02-25T11:00:00Z"
weight = 18849
keywords = [ "dissector", "wireshark" ]
aliases = [ "/questions/18849" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [couple of messages in one frame](/questions/18849/couple-of-messages-in-one-frame)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18849-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I wrote a dissector,</p><p>I found one packet which contains couple of different/indifferent messages inside it,</p><p>Can someone point on the problem ? Is this even a problem ?</p><p>I reassemble TCP packets...</p><p><strong>This is the function of dissection:</strong> (FRAME_HEADER_LEN = 8)</p><pre><code>static void
dissect_PROTOC(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
{
    //Reassembling TCP fragments
    tcp_dissect_pdus(tvb, pinfo, tree, TRUE, FRAME_HEADER_LEN,
                     get_PROTOC_message_len, dissect_PROTOC_message);

}

static guint get_PROTOC_message_len(packet_info *pinfo, tvbuff_t *tvb, int offset)
{
    /* the packet&#39;s size is &quot;length&quot; + 4bytes of TYPESIZE + 4bytes of LENGTHSIZE + 256bytes of CONTEXTIDSIZE */
    return (guint)(tvb_get_ntohl(tvb, offset + 4) + CONTEXT_ID_SIZE + TYPE_SIZE + LENGTH_SIZE); /* e.g. length is at offset 4 */
}

static void dissect_PROTOC_message(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
{
    /* my dissecting code */
    guint32 packet_type = tvb_get_ntohl(tvb, 0);

    col_set_str(pinfo-&gt;cinfo, COL_PROTOCOL, &quot;PROTOC&quot;);
    /* Clear out stuff in the info column */
    col_clear(pinfo-&gt;cinfo,COL_INFO);
    col_add_fstr(pinfo-&gt;cinfo, COL_INFO, &quot;%d &gt; %d [%s]&quot;,pinfo-&gt;srcport, pinfo-&gt;destport,
             val_to_str(packet_type, packettypenames, &quot;Unknown (0x%02x)&quot;));

    if (tree) { /* we are being asked for details */
        proto_item *ti              = NULL;
        proto_tree *PROTOC_tree         = NULL;
        proto_item *PROTOC_data         = NULL;
        proto_tree *PROTOC_data_tree    = NULL;
        guint32 type    = 0;
        guint32 length  = 0;
        gint offset     = 0;

        ti = proto_tree_add_item(tree, proto_PROTOC, tvb, 0, -1, ENC_NA);
        proto_item_append_text(ti, &quot;, Type: %s&quot;,
            val_to_str(packet_type, packettypenames, &quot;Unknown (0x%02x)&quot;));
        PROTOC_tree = proto_item_add_subtree(ti, ett_PROTOC);

        //getting type
        type = tvb_get_ntohl(tvb, offset);
        proto_tree_add_item(PROTOC_tree, hf_PROTOC_pdu_type, tvb, 0, TYPE_SIZE, ENC_BIG_ENDIAN);
        offset += TYPE_SIZE;

        //getting length for the data length
        length = tvb_get_ntohl(tvb, offset);
        proto_tree_add_item(PROTOC_tree, hf_PROTOC_len, tvb, offset, LENGTH_SIZE, ENC_BIG_ENDIAN);
        offset += LENGTH_SIZE;
        proto_tree_add_item(PROTOC_tree, hf_PROTOC_contextid, tvb, offset, CONTEXT_ID_SIZE, ENC_BIG_ENDIAN);
        offset += CONTEXT_ID_SIZE;
        PROTOC_data = proto_tree_add_item(PROTOC_tree, hf_PROTOC_data, tvb, offset, length, FALSE);
        PROTOC_data_tree = proto_item_add_subtree(PROTOC_data, ett_PROTOC_data);
        offset += length;

    }
}</code></pre></div><div id="question-tags" class="tags-container tags">dissector wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Feb '13, 06:18</strong></p><img src="https://secure.gravatar.com/avatar/b7ccaef1113111fc5cb2bb2a0d866a4e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hudac&#39;s gravatar image" /><p>hudac<br />
<span class="score" title="61 reputation points">61</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hudac has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Feb '13, 22:27</p></div></div><div id="comments-container-18849" class="comments-container"></div><div id="comment-tools-18849" class="comment-tools"></div><div class="clear"></div><div id="comment-18849-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18853"></span>

<div id="answer-container-18853" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18853-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You're using <code>tcp_dissect_pdus()</code>, so your protocol runs atop TCP. This means that there is no guarantee that packet boundaries for your protocol will correspond to TCP segment boundaries, so there's no guarantee that they will correspond to IP packet boundaries, so there's no guarantee that they will correspond to link-layer packet boundaries.</p><p>Thus, you may get multiple packets for your protocol in a single TCP segment, or you may get a packet for your protocol contained in more than one TCP segment, or you might get arbitrary combinations of those, for example, a TCP segment with two full packets for your protocol followed by the beginning of a third packet for your protocol, and the subsequent TCP segment containing the middle of the third packet, and the subsequent TCP segment containing the end of the third packet, two more full packets for your protocol, and the beginning of the sixth packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '13, 11:00</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-18853" class="comments-container"><span id="18854"></span><div id="comment-18854" class="comment"><div id="post-18854-score" class="comment-score"></div><div class="comment-text"><p>Thanks, but doesn't the wireshark suppose to separate in a situation like this?</p><p>In one reassembled packet (one line of the wireshark, one frame), I get 6 packets of my protocol.</p><h2 id="example">example:</h2><p>Frame ...</p><p>Ethernet ...</p><p>Internet protocol ...</p><p>Transmission control protocol ...</p><p>Hypertext transfer protocol ...</p><p>My protocol ...</p><p>My protocol ...</p><p>My protocol ...</p><p>My protocol ...</p><p>My protocol ...</p><p>My protocol ...</p><hr /><p>Did you mean like this, with your question ?</p><p>Thanks,</p></div><div id="comment-18854-info" class="comment-info"><span class="comment-age">(25 Feb '13, 11:13)</span> hudac</div></div><span id="18857"></span><div id="comment-18857" class="comment"><div id="post-18857-score" class="comment-score"></div><div class="comment-text"><p>I don't know what you mean by "separate", but, if your dissector is written correctly, Wireshark should display something similar what you show in your example.</p><p>However, I'm not sure why "Hypertext transfer protocol" is in there. Is that an HTTP CONNECT request, so that the TCP connection starts out as an HTTP connection, and then switches to a tunnel for your protocol?</p></div><div id="comment-18857-info" class="comment-info"><span class="comment-age">(25 Feb '13, 11:34)</span> Guy Harris ♦♦</div></div><span id="18906"></span><div id="comment-18906" class="comment"><div id="post-18906-score" class="comment-score"></div><div class="comment-text"><p>Separate: I mean that for each "My protocol" there will be a different frame, like this:</p><p>Frame 1702: ...</p><p>Ethernet II, ....</p><p>....</p><p>....</p><p>My protocol</p><hr /><p>Frame 1705: ...</p><p>Ethernet II, ....</p><p>....</p><p>....</p><p>My protocol</p><hr /><p>"Hypertext transfer protocol", that was an example, I'll give another one about the situation I'm talking about, in one frame, I have a lot of "My protocol", doesn't wireshark suppose to separate them into different frames?:</p><p>Frame 1702: ...</p><p>Ethernet II, ....</p><p>....</p><p>....</p><p>My protocol</p><p>My protocol</p><p>My protocol</p><p>My protocol</p><p>My protocol</p></div><div id="comment-18906-info" class="comment-info"><span class="comment-age">(26 Feb '13, 22:18)</span> hudac</div></div><span id="18914"></span><div id="comment-18914" class="comment"><div id="post-18914-score" class="comment-score">1</div><div class="comment-text"><p>No, Wireshark wouldn't do that, because there <em>aren't</em> separate frames. If, in a single Ethernet packet, there is a TCP segment containing multiple packets for your protocol, Wireshark cannot report multiple "Ethernet II" lines, as there's only one Ethernet header for all those packets. Wireshark is <em>NOT</em> supposed to separate them into different frames, because they're all in one frame.</p></div><div id="comment-18914-info" class="comment-info"><span class="comment-age">(27 Feb '13, 00:30)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-18853" class="comment-tools"></div><div class="clear"></div><div id="comment-18853-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

