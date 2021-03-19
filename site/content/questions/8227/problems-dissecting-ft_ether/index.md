+++
type = "question"
title = "Problems dissecting FT_ETHER"
description = '''Hello, I need to dissect a MAC address, but the format FT_ETHER gives me a hard time. I looked into packet_eth.c and used this code: static int hf_mac = -1; static void dissect_xxx(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree) {  if (tree) {  const guint8 *address;  address = tvb_get_ptr(tvb,...'''
date = "2012-01-05T01:19:00Z"
lastmod = "2012-01-05T07:12:00Z"
weight = 8227
keywords = [ "dissector", "mac-address" ]
aliases = [ "/questions/8227" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Problems dissecting FT\_ETHER](/questions/8227/problems-dissecting-ft_ether)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8227-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I need to dissect a MAC address, but the format FT_ETHER gives me a hard time. I looked into packet_eth.c and used this code:</p><pre><code>static int hf_mac = -1;
static void dissect_xxx(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree) {
    if (tree) {
        const guint8 *address;
        address = tvb_get_ptr(tvb, 0, 6);

        proto_tree_add_ether(tree, hf_mac, tvb, 0, 6, address);
    }
}

void
proto_register_xxx(void) {
    static hf_register_info hf[] = {
        {&amp;hf_mac, 
            {&quot;MAC&quot;, &quot;xxx.mac&quot;, FT_ETHER, BASE_NONE, NULL, 0x00, NULL, HFILL}},
    };

    [...]
}</code></pre><p>When dissecting the packet, wireshark gives me this error:</p><blockquote><p>Expert Info (Error/Malformed): proto.c:2672: failed assertion "hfinfo-&gt;type == FT_ETHER"</p></blockquote><p>Why is that? I declared it as FT_ETHER...</p><p>Wireshark 1.6.4, dissector as a plugin.</p></div><div id="question-tags" class="tags-container tags">dissector mac-address</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jan '12, 01:19</strong></p><img src="https://secure.gravatar.com/avatar/5ee84a594a89fb598c3d1d18ddd0dbe6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nniico&#39;s gravatar image" /><p>nniico<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nniico has one accepted answer">100%</span></p></div></div><div id="comments-container-8227" class="comments-container"></div><div id="comment-tools-8227" class="comment-tools"></div><div class="clear"></div><div id="comment-8227-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8230"></span>

<div id="answer-container-8230" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8230-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>My mistake : I was compiling a plug-in with sources from 1.7 and using it with a downloaded stable 1.6.4. Works like a charm on a compiled 1.7.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jan '12, 07:12</strong></p><img src="https://secure.gravatar.com/avatar/5ee84a594a89fb598c3d1d18ddd0dbe6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nniico&#39;s gravatar image" /><p>nniico<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nniico has one accepted answer">100%</span></p></div></div><div id="comments-container-8230" class="comments-container"></div><div id="comment-tools-8230" class="comment-tools"></div><div class="clear"></div><div id="comment-8230-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

