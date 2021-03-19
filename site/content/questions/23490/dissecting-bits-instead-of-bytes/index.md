+++
type = "question"
title = "Dissecting bits instead of bytes"
description = '''I&#x27;m trying to get the first 4 bits and the last 4 bits of a byte. proto_tree_add_bits_item(tree, hf_capability, tvb, bit_offset, 4, ENC_BIG_ENDIAN); proto_tree_add_bits_item(tree, hf_capability, tvb, bit_offset+4, 4, ENC_BIG_ENDIAN);   { &amp;amp;hf_capability,  { &quot;Capabilities&quot;, &quot;status.capability&quot;,  F...'''
date = "2013-07-31T12:42:00Z"
lastmod = "2013-08-01T04:25:00Z"
weight = 23490
keywords = [ "custom", "dissector", "wireshark" ]
aliases = [ "/questions/23490" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Dissecting bits instead of bytes](/questions/23490/dissecting-bits-instead-of-bytes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23490-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to get the first 4 bits and the last 4 bits of a byte.</p><pre><code>proto_tree_add_bits_item(tree, hf_capability, tvb, bit_offset, 4, ENC_BIG_ENDIAN);
proto_tree_add_bits_item(tree, hf_capability, tvb, bit_offset+4, 4, ENC_BIG_ENDIAN);

    { &amp;hf_capability,
        { &quot;Capabilities&quot;, &quot;status.capability&quot;,
        FT_UINT8, BASE_DEC, 
        VALS(capabilitynames), 0x0,
        NULL, HFILL }
    },</code></pre><p>When I use this in wireshark, its clearly not happy.</p><pre><code>(lt-wireshark:18421): Pango-WARNING **: Invalid UTF-8 string passed to pango_layout_set_text()</code></pre><p>I think it's because its not a full 8 bits. Do I need to use a bitmask? How do I use a bitmask? I'm stumbling over syntax a lot, so please show me code examples of what I should do.</p><p>Here's where I'm mapping the integers to strings:</p><pre><code>static const value_string capabilitynames[] = {
    { 1, &quot;Switchable&quot; },
    { 2, &quot;Human&quot; },
    { 4, &quot;Mobile&quot; },
};</code></pre></div><div id="question-tags" class="tags-container tags">custom dissector wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jul '13, 12:42</strong></p><img src="https://secure.gravatar.com/avatar/477c22aa68350514a3d320929b588791?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arwen17&#39;s gravatar image" /><p>Arwen17<br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arwen17 has no accepted answers">0%</span></p></div></div><div id="comments-container-23490" class="comments-container"></div><div id="comment-tools-23490" class="comment-tools"></div><div class="clear"></div><div id="comment-23490-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23496"></span>

<div id="answer-container-23496" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23496-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>One problem is that the value string isn't terminated with { 0, NULL} see if that resolves the problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '13, 04:25</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-23496" class="comments-container"><span id="23502"></span><div id="comment-23502" class="comment"><div id="post-23502-score" class="comment-score"></div><div class="comment-text"><p>Thank you! That fixed it! I removed the { 0, NULL} a long time ago and it didn't give me any errors or warnings when I did so I assumed it was unnecessary. I only started getting an error when I started trying to work with bits instead of bytes.</p></div><div id="comment-23502-info" class="comment-info"><span class="comment-age">(01 Aug '13, 07:19)</span> Arwen17</div></div><span id="23562"></span><div id="comment-23562" class="comment"><div id="post-23562-score" class="comment-score"></div><div class="comment-text"><p>That would have been easily caught by running <code>tools/checkAPIs.pl epan/dissectors/packet-foo.c</code>. Incidentally, you've chosen quite a poor name for your display filter of "status.capability". Try running <code>tools/checkfiltername.pl</code>, and also <code>tools/checkhf.pl</code>. These handy scripts will help you find many common mistakes.</p></div><div id="comment-23562-info" class="comment-info"><span class="comment-age">(05 Aug '13, 07:46)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-23496" class="comment-tools"></div><div class="clear"></div><div id="comment-23496-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

