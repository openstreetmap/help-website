+++
type = "question"
title = "How to store data in conversations via dissector"
description = '''Greetings, I am building a plugin dissector that decompresses packets from a conversation for which a compression flag can be set either via a byte set on the first compressed subsequent segment or a string definition on its first segment. Subsequent segments afterwards do not have the byte set that...'''
date = "2016-04-04T20:08:00Z"
lastmod = "2016-04-05T04:46:00Z"
weight = 51406
keywords = [ "dissector", "decompression", "compressed", "decompress", "plugin" ]
aliases = [ "/questions/51406" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to store data in conversations via dissector](/questions/51406/how-to-store-data-in-conversations-via-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51406-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings, I am building a plugin dissector that decompresses packets from a conversation for which a compression flag can be set either via a byte set on the first compressed subsequent segment or a string definition on its first segment. Subsequent segments afterwards do not have the byte set that flags a compressed stream. I've tried either finding the conversation or creating one if not found, but I need a mechanism for depicting if a packet found from a conversation has been set to "Compressed". Here is my code:</p><hr /><pre><code>        /* First check that data is compressed */
    tvbuff_t *newBuf;
    guint8 bits1 = tvb_get_guint8(tvb, offset);
    guint8 bits2 = tvb_get_guint8(tvb, offset + 1);
    if ((bits1 == 200) &amp;&amp; (bits2 == 300)) {
        m_IsCompressed = TRUE;
    }

    /* Next check if this is a new stream or it&#39;s part of a CPOF conversation. */
    conversation_t *conversation = find_conversation(pinfo-&gt;fd-&gt;num, &amp;pinfo-&gt;src, &amp;pinfo-&gt;dst,
        pinfo-&gt;ptype, pinfo-&gt;srcport, pinfo-&gt;destport, 0);

    // first segment to process for this side of the stream?
    if (conversation == NULL){
            // Create new conversation to track
        conversation = conversation_new(pinfo-&gt;fd-&gt;num, &amp;pinfo-&gt;src, &amp;pinfo-&gt;dst,
            pinfo-&gt;ptype, pinfo-&gt;srcport, pinfo-&gt;destport, 0);

    /* Compression flag also gets set when &quot;Compressing&quot; string is found.  Other systems in conversation can also converse compressed, yet not have bytes-set flag. */
        gint newLen = tvb_reported_length_remaining(tvb, offset);
        guint8* buff_str = tvb_get_string_enc(pool, tvb, offset, newLen, ENC_ASCII | ENC_NA);
        gchar* str = convert(buff_str, strlen);
        check_compression_string_flag(str);
        newBuf = tvb_new_subset_remaining(tvb, offset);
                    if (m_IsCompressed)
                           conversation_add_proto_data(conversation, proto_tag, &quot;Compressed&quot;);
    }
    else {
                    char* state = (char*) conversation_get_proto_data(conversation, proto_tag);
                    IsCompressed = m_IsCompressed || (state || strncmp(state, &quot;Compressed&quot;, 10) == 0);
        if (m_IsCompressed) {
            /* the remainder of the packet is compressed, decompress the payload */
            newBuf = tvb_uncompress(tvb, offset, tvb_captured_length_remaining(tvb, offset + 2));

            /* Check the return code and add a expert info warning if an error
            * occurred. The dissector continues trying to add the payload,
            * however the returned size should be 0. */
            if (newBuf) {
                /* Now re-setup the tvb buffer to have the new data */
                tvb_set_child_real_data_tvbuff(tvb, newBuf);
                add_new_data_source(pinfo, newBuf, &quot;Decompressed Data&quot;);
            }
            else {
                /* attempt to process it as uncompressed */
                newBuf = tvb_new_subset_remaining(tvb, offset);
            }
        }
        else {
                /* process new uncompressed buffer */
            newBuf = tvb_new_subset_remaining(tvb, offset);
        }
    }
    /* process newBuf from here on */
    offset = 0;</code></pre><hr /><p>Could I store a Boolean into a conversation that I can access and use to determine if associated/follow-on packets need decompression? A single static boolean doesn't seem to do the trick for me.</p><p>Thanks in advanced.</p></div><div id="question-tags" class="tags-container tags">dissector decompression compressed decompress plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Apr '16, 20:08</strong></p><img src="https://secure.gravatar.com/avatar/bfa53b64ea6967e45a614981c461a638?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="coloncm&#39;s gravatar image" /><p>coloncm<br />
<span class="score" title="76 reputation points">76</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="coloncm has 2 accepted answers">66%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Apr '16, 12:42</p></div></div><div id="comments-container-51406" class="comments-container"></div><div id="comment-tools-51406" class="comment-tools"></div><div class="clear"></div><div id="comment-51406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51414"></span>

<div id="answer-container-51414" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51414-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>conversation_new() should be inside the if (conversation == NULL) block, otherwise the conversation will never exist.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '16, 04:46</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-51414" class="comments-container"><span id="51428"></span><div id="comment-51428" class="comment"><div id="post-51428-score" class="comment-score"></div><div class="comment-text"><p>Changed the question after suggested fix did not change outcome to the underlying problem.</p></div><div id="comment-51428-info" class="comment-info"><span class="comment-age">(05 Apr '16, 16:35)</span> coloncm</div></div><span id="51434"></span><div id="comment-51434" class="comment"><div id="post-51434-score" class="comment-score">1</div><div class="comment-text"><p>See README.dissector 2.2.1.5 The conversation_add_proto_data function.</p></div><div id="comment-51434-info" class="comment-info"><span class="comment-age">(06 Apr '16, 04:33)</span> Jaap ♦</div></div><span id="51445"></span><div id="comment-51445" class="comment"><div id="post-51445-score" class="comment-score"></div><div class="comment-text"><p>Thanks, Jaap. The mechanism seems to work except I'm not sure if I'm getting back what I'm putting in form a found conversation, e.g., gboolen values appear to be random positive or negative values instead of 1 or 0 as previously set. But, that's another question, I guess, and your comment surely answers this question.</p></div><div id="comment-51445-info" class="comment-info"><span class="comment-age">(06 Apr '16, 18:31)</span> coloncm</div></div></div><div id="comment-tools-51414" class="comment-tools"></div><div class="clear"></div><div id="comment-51414-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

