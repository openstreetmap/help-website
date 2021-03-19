+++
type = "question"
title = "Difference between proto_tree_add_item and proto_tree_add_uint"
description = '''Hi, I am writing a dissector in C and have a question in regards to what the differences are between proto_tree_add_item and proto_tree_add_uint. I have experiences Expert Info Warnings of &quot;Trying to fetch an unsigned integer with length --&quot; when using proto_tree_add_item with sizes above a certain ...'''
date = "2017-03-21T07:50:00Z"
lastmod = "2017-03-21T08:15:00Z"
weight = 60224
keywords = [ "proto_tree_add_item", "dissector", "c", "proto_tree_add_uint" ]
aliases = [ "/questions/60224" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Difference between proto\_tree\_add\_item and proto\_tree\_add\_uint](/questions/60224/difference-between-proto_tree_add_item-and-proto_tree_add_uint)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60224-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am writing a dissector in C and have a question in regards to what the differences are between proto_tree_add_item and proto_tree_add_uint. I have experiences Expert Info Warnings of "Trying to fetch an unsigned integer with length --" when using proto_tree_add_item with sizes above a certain amount. Switching this to proto_tree_add_uint results in these warnings disappearing. Under the hood, what is the difference between these two functions? This is the only conversation I've seen on the topic: <a href="https://www.wireshark.org/lists/wireshark-dev/201408/msg00296.html">https://www.wireshark.org/lists/wireshark-dev/201408/msg00296.html</a></p><p>[As reference I've including the functions as seen in proto.c]</p><pre><code>/* Add FT_CHAR or FT_UINT{8,16,24,32} to a proto_tree */

proto_item *

proto_tree_add_uint(proto_tree *tree, int hfindex, tvbuff_t *tvb, gint start,
            gint length, guint32 value)

{
    proto_item    *pi = NULL;

    header_field_info *hfinfo;

    CHECK_FOR_NULL_TREE(tree);

    TRY_TO_FAKE_THIS_ITEM(tree, hfindex, hfinfo);

    switch (hfinfo-&gt;type) {
        case FT_CHAR:
        case FT_UINT8:
        case FT_UINT16:
        case FT_UINT24:
        case FT_UINT32:
        case FT_FRAMENUM:
            pi = proto_tree_add_pi(tree, hfinfo, tvb, start, &amp;length);
            proto_tree_set_uint(PNODE_FINFO(pi), value);
            break;

        default:
            DISSECTOR_ASSERT_NOT_REACHED();
    }

    return pi;
}</code></pre><pre><code>proto_tree_add_item(proto_tree *tree, int hfindex, tvbuff_t *tvb,
            const gint start, gint length, const guint encoding)

{

    register header_field_info *hfinfo;

    PROTO_REGISTRAR_GET_NTH(hfindex, hfinfo);
    return proto_tree_add_item_new(tree, hfinfo, tvb, start, length, encoding);
}</code></pre></div><div id="question-tags" class="tags-container tags">proto_tree_add_item dissector c proto_tree_add_uint</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '17, 07:50</strong></p><img src="https://secure.gravatar.com/avatar/134bbb4fd9687f9718bb94d36c4b75fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brownfox&#39;s gravatar image" /><p>brownfox<br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brownfox has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Mar '17, 07:59</p></div></div><div id="comments-container-60224" class="comments-container"></div><div id="comment-tools-60224" class="comment-tools"></div><div class="clear"></div><div id="comment-60224-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="60228"></span>

<div id="answer-container-60228" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60228-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark version?</p><p>Are you correctly matching the <code>FT_XXX</code> type in the hfindex structure with the length you're passing into the <code>proto_xxx</code> call? That is, for <code>FT_CHAR</code>, <code>FT_UINT8</code>, <code>FT_UINT16</code>, <code>FT_UINT24</code> and <code>FT_UINT32</code> length has to be 1, 1, 2, 3, or 4 respectively. For <code>FT_UINT40</code>, <code>FT_UINT48</code>, <code>FT_UINT56</code> and <code>FT_UINT64</code> the length has to be 5, 6, 7 or 8 respectively.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '17, 08:15</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-60228" class="comments-container"><span id="60229"></span><div id="comment-60229" class="comment"><div id="post-60229-score" class="comment-score"></div><div class="comment-text"><p>I'm using version 2.3.0.</p><p>For example, one of my packets in the capture file contains a 32-byte SHA256 hash.</p><p>Here's the corresponding code:</p><p>proto_tree_add_uint(proto_tree, hf_proto_config_sha256_hash_frame, tvb, offset, CONFIG_SHA256_HASH_FRAME_LEN, ENC_LITTLE_ENDIAN); offset += CONFIG_SHA256_HASH_FRAME_LEN;</p><p>{&amp;hf_proto_config_sha256_hash_frame, {"Config SHA256 Hash This Frame", "proto.config_sha256_hash_frame", FT_UINT16, BASE_DEC, NULL, 0, NULL, HFILL }</p><p>As a side note, there's an issue with the display in Wireshark using BASE_DEC but I believe that is due to a mistake in the generated capture file not being little endian.</p></div><div id="comment-60229-info" class="comment-info"><span class="comment-age">(21 Mar '17, 08:33)</span> brownfox</div></div><span id="60230"></span><div id="comment-60230" class="comment"><div id="post-60230-score" class="comment-score"></div><div class="comment-text"><p>And what's the <code>hfproto_config_sha256_hash_frame</code> declaration?</p><p>Note that it doesn't make sense (to me at least) to show a SHA256 hash as a <code>FT_UINTXX</code> value, especially as a uint is limited to 8 bytes. You could use a <code>FT_NONE</code> type as is done for hashes in SSL, e.g. packet-ssl-utils.c function <code>ssl_dissect_hnd_finished()</code> with <code>ssl_hfs.hs_sha_hash</code> (declared in packet-ssl.c), passing in 32 for the length.</p><p>I would actually argue that hashes should be using <code>FT_BYTES</code> rather than <code>FT_NONE</code> as that's what they are, a sequence of bytes with arbitrary values.</p></div><div id="comment-60230-info" class="comment-info"><span class="comment-age">(21 Mar '17, 09:38)</span> grahamb ♦</div></div><span id="60232"></span><div id="comment-60232" class="comment"><div id="post-60232-score" class="comment-score"></div><div class="comment-text"><p>My hf_proto_config_sha256_hash_frame is now</p><p>{"Config SHA256 Hash This Frame", "proto.config_sha256_hash_frame", FT_BYTES, BASE_NONE, NULL, 0x0, NULL, HFILL }<br />
</p><p>as you suggested. It works without error so thank you for that. I had initially chosen to display the hash as FT_UINT16 just as a placeholder before seeing how it was done in other protocols - thanks for the reference to SSL.</p><p>I think this is the solution though I'll try to fix the other fields first.</p></div><div id="comment-60232-info" class="comment-info"><span class="comment-age">(21 Mar '17, 10:12)</span> brownfox</div></div></div><div id="comment-tools-60228" class="comment-tools"></div><div class="clear"></div><div id="comment-60228-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="60226"></span>

<div id="answer-container-60226" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60226-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The proto_tree_add functions perform the essential function of populating the tree with fields from the data packet at hand. The function which supports the most common operations in one is proto_tree_add_item(). It helps to do the following:</p><ul><li>Retrieve the relevant value from the tvb (as defined by the header field used)</li><li>Add a tree item (when needed)</li><li>Highlight the data in the bytes pane</li></ul><p>So basically all common functions are wrapped into one. The header field is important here, it defines much of the retrieval and representation of the value. It provides a lot of flexibility for most common situations.</p><p>But sometimes this is not enough. Sometimes you want more control over the actual value used for this field, which somehow cannot be provided by the functionality of the header field. Then you can resort to proto_tree_add_uint(). This does the same, but for value retrieval, that value is now passed via the function interface.</p><p>You say you run into trouble when using certain lengths, but not when using proto_tree_add_uint(). This for sure comes from the fact that the header field is no longer used for value retrieval, just highlighting.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '17, 08:06</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span> </br></p></div></div><div id="comments-container-60226" class="comments-container"></div><div id="comment-tools-60226" class="comment-tools"></div><div class="clear"></div><div id="comment-60226-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

