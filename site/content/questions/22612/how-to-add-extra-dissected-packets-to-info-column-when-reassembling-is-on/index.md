+++
type = "question"
title = "How to add extra dissected packets to info column when reassembling is on"
description = '''I would like to add all of the dissected messages&#x27;s type of my protocol Protoc to the Info column. I&#x27;m enabling reassembling of tcp packets. So sometimes, as you can see in the picture, there might be couple of messages of my protocol in one reassembled pdu. The problem is that only [TYPE A] is show...'''
date = "2013-07-03T07:57:00Z"
lastmod = "2013-07-03T08:24:00Z"
weight = 22612
keywords = [ "reassembly", "reassembled", "dissector", "wireshark", "col_info" ]
aliases = [ "/questions/22612" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to add extra dissected packets to info column when reassembling is on](/questions/22612/how-to-add-extra-dissected-packets-to-info-column-when-reassembling-is-on)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22612-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to add all of the dissected messages's type of my protocol <code>Protoc</code> to the <code>Info column</code>.</p><p>I'm enabling reassembling of tcp packets. So sometimes, as you can see in the picture, there might be couple of messages of my protocol in one reassembled pdu.</p><p>The problem is that only <code>[TYPE A]</code> is shown in the <code>Info column</code>. (I think wireshark.org cut it in this file, so believe me). I would like to put in the <code>Info column</code> something like: <code>[TYPE A][TYPE B][TYPE C]</code></p><p>Is it possible ?</p><p>In order to put the <code>[TYPE]</code> I use the following code in <code>dissect_PROTOC_message()</code>:</p><pre><code>col_clear(pinfo-&gt;cinfo,COL_INFO);
col_add_fstr(pinfo-&gt;cinfo, COL_INFO, &quot;%d &gt; %d [%s]&quot;,pinfo-&gt;srcport, pinfo-&gt;destport, val_to_str(packet_type, packettypenames, &quot;Unknown (0x%02x)&quot;));</code></pre><p>I know there is a problem, cause every time wireshark finds new messages of <code>PROTOC</code>, it do <code>col_clear()</code> again, and deletes all the past information.</p><p>I tried to get the PDU length and each time do <code>col_append_fstr()</code> myself. if I'm not exceeding the PDU length. but I think it doesn't work also, because of the same problem with <code>col_clear()</code>.</p><p>Help would be helpful, thanks.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/protoc_1.png" alt="alt text" /></p><p>------------------------------edit---------------------------------------</p><p>I tried to add <code>col_set_fence()</code>, but it still doesn't work. for the next code, I get the next picture. please tell me if you need and further information.</p><pre><code>static void dissect_protoc_message(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree)
{
/* my dissecting code */
guint32 packet_type = tvb_get_ntohl(tvb, 0);

col_set_str(pinfo-&gt;cinfo, COL_PROTOCOL, protoc_SHORT_NAME);
/* Clear out stuff in the info column */
col_clear(pinfo-&gt;cinfo,COL_INFO);
col_add_fstr(pinfo-&gt;cinfo, COL_INFO, &quot;%d &gt; %d &quot;,pinfo-&gt;srcport, pinfo-&gt;destport);
col_set_fence(pinfo-&gt;cinfo, COL_INFO); 
col_append_fstr(pinfo-&gt;cinfo, COL_INFO, &quot;[%s]&quot;, val_to_str(packet_type, packettypenames, &quot;Unknown (0x%02x)&quot;));

if (tree) { /* we are being asked for details */
    proto_item *ti          = NULL;
    proto_tree *protoc_tree         = NULL;
    proto_item *protoc_data         = NULL;
    proto_tree *protoc_data_tree    = NULL;
    guint32 type                = 0;
    guint32 length          = 0;
    gint offset                 = 0;

        ti = proto_tree_add_item(tree, proto_protoc, tvb, 0, -1, ENC_NA);
    proto_item_append_text(ti, &quot;, Type: %s&quot;, val_to_str(packet_type, packettypenames, &quot;Unknown (0x%02x)&quot;));
    protoc_tree = proto_item_add_subtree(ti, ett_protoc);

    //getting type
    type = tvb_get_ntohl(tvb, offset);
        proto_tree_add_item(protoc_tree, hf_protoc_pdu_type, tvb, 0, TYPE_SIZE, ENC_BIG_ENDIAN);
    offset += TYPE_SIZE;

    //getting length for the data length
    length = tvb_get_ntohl(tvb, offset);
    proto_tree_add_item(protoc_tree, hf_protoc_len, tvb, offset, LENGTH_SIZE, ENC_BIG_ENDIAN);
    offset += LENGTH_SIZE;
    proto_tree_add_item(protoc_tree, hf_protoc_contextid, tvb, offset, CONTEXT_ID_SIZE, ENC_BIG_ENDIAN);
    offset += CONTEXT_ID_SIZE;
    protoc_data = proto_tree_add_item(protoc_tree, hf_protoc_data, tvb, offset, length, FALSE);
    protoc_data_tree = proto_item_add_subtree(protoc_data, ett_protoc_data);

    switch (type) {
        case TRANSCODE_ID:
                    parse_transcode(protoc_data_tree, tvb, &amp;offset);
                    offset += length;
            break;
        case INPUTDATA_ID:
                    offset += length;
....
....
....</code></pre><p><img src="https://osqa-ask.wireshark.org/upfiles/protoc_2.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">reassembly reassembled dissector wireshark col_info</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jul '13, 07:57</strong></p><img src="https://secure.gravatar.com/avatar/b7ccaef1113111fc5cb2bb2a0d866a4e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hudac&#39;s gravatar image" /><p>hudac<br />
<span class="score" title="61 reputation points">61</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hudac has one accepted answer">50%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 04 Jul '13, 01:50</p></div></div><div id="comments-container-22612" class="comments-container"></div><div id="comment-tools-22612" class="comment-tools"></div><div class="clear"></div><div id="comment-22612-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22613"></span>

<div id="answer-container-22613" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22613-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at <code>col_set_fence()</code> as discussed in Sect 1.4.8 of <a href="http://anonsvn.wireshark.org/wireshark/trunk/doc/README.dissector">README.dissector</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '13, 08:24</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></img></div></div><div id="comments-container-22613" class="comments-container"><span id="22628"></span><div id="comment-22628" class="comment"><div id="post-22628-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I tried it now. But it still doesn't work. I'm not calling any subdissector - It's the same dissector. does it matter?</p></div><div id="comment-22628-info" class="comment-info"><span class="comment-age">(03 Jul '13, 22:06)</span> hudac</div></div><span id="22633"></span><div id="comment-22633" class="comment"><div id="post-22633-score" class="comment-score"></div><div class="comment-text"><p>It does work, I've used it in <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/dissectors/packet-dnp.c?revision=50355&amp;view=markup">packet-dnp.c</a>. There may be multiple DNP3 PDU's in a single TCP/UDP frame and the info column reflects the basic function of each of the PDU's in the frame.</p></div><div id="comment-22633-info" class="comment-info"><span class="comment-age">(04 Jul '13, 01:34)</span> grahamb ♦</div></div><span id="22635"></span><div id="comment-22635" class="comment"><div id="post-22635-score" class="comment-score"></div><div class="comment-text"><p>thanks, I'm looking at "packet-dnp.c", can you look into my edit?</p></div><div id="comment-22635-info" class="comment-info"><span class="comment-age">(04 Jul '13, 01:53)</span> hudac</div></div><span id="22636"></span><div id="comment-22636" class="comment"><div id="post-22636-score" class="comment-score"></div><div class="comment-text"><p>I can't see any real difference...</p></div><div id="comment-22636-info" class="comment-info"><span class="comment-age">(04 Jul '13, 02:03)</span> hudac</div></div><span id="22639"></span><div id="comment-22639" class="comment"><div id="post-22639-score" class="comment-score">1</div><div class="comment-text"><p>You are setting the fence after adding the "from &gt; to" info, so the packet type info isn't protected. I would have thought you would have seen multiple entries for the "from &gt; to" and only the last packet type string.</p><p>set_fence clearly works for my dissector and others, so you'll just have to debug your issues.</p></div><div id="comment-22639-info" class="comment-info"><span class="comment-age">(04 Jul '13, 03:13)</span> grahamb ♦</div></div></div><div id="comment-tools-22613" class="comment-tools"></div><div class="clear"></div><div id="comment-22613-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

