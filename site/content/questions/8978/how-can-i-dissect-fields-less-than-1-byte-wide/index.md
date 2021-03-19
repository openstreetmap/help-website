+++
type = "question"
title = "How can I dissect fields less than 1-byte wide?"
description = '''I am working on a protocol dissector where some fields are comprised of fewer than 8 bits. For example, the first 4 bits identify the packet type, and the next 16 bits the length of following data. Can I dissect fields with length less than one byte, and how can I display them? '''
date = "2012-02-13T09:52:00Z"
lastmod = "2012-02-13T10:46:00Z"
weight = 8978
keywords = [ "development", "fields", "dissector" ]
aliases = [ "/questions/8978" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can I dissect fields less than 1-byte wide?](/questions/8978/how-can-i-dissect-fields-less-than-1-byte-wide)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8978-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am working on a protocol dissector where some fields are comprised of fewer than 8 bits. For example, the first 4 bits identify the packet type, and the next 16 bits the length of following data. Can I dissect fields with length less than one byte, and how can I display them?</p></div><div id="question-tags" class="tags-container tags">development fields dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '12, 09:52</strong></p><img src="https://secure.gravatar.com/avatar/d221d26845724614e25ab8e51887c4bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ashish_goel&#39;s gravatar image" /><p>ashish_goel<br />
<span class="score" title="15 reputation points">15</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ashish_goel has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Feb '12, 10:48</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-8978" class="comments-container"></div><div id="comment-tools-8978" class="comment-tools"></div><div class="clear"></div><div id="comment-8978-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8979"></span>

<div id="answer-container-8979" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8979-score" class="post-score" title="current number of votes">4</div></div></td><td><div class="item-right"><div class="answer-body"><p>Absolutely. You can do this by specifying a nonzero bitmask when defining your header fields like so:</p><pre><code>{ &amp;hf_packet_type,
{ &quot;type&quot;, &quot;myproto.type&quot;, FT_UINT8, BASE_DEC, NULL, 0xF0, &quot;Packet Type&quot;, HFILL }},
{ &amp;hf_packet_length,
{ &quot;length&quot;, &quot;myproto.length&quot;, FT_UINT24, BASE_DEC, NULL, 0x0FFFF0, &quot;Packet Length&quot;, HFILL }},</code></pre><p>Then, simply add them to the tree as you have done for your other protocol fields:</p><pre><code>proto_tree_add_item(my_tree, hf_packet_type, tvb, 0, 1, FALSE);
proto_tree_add_item(my_tree, hf_packet_length, tvb, 0, 3, FALSE);</code></pre><p>Doing it this way keeps most of the bit-twiddling out of your dissector code, but still allows you to add fields of arbitrary widths and continuities to your protocol.</p><p>Note that if you need to work with those bits directly you must extract them from the <code>tvb</code> yourself, just as you do for fields that are byte-bounded and sized in byte-increments, just using one of the <code>tvb_get_bits*</code> functions in stead of one of the other <code>tvb_get*</code> functions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '12, 10:46</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Feb '12, 10:50</p></div></div><div id="comments-container-8979" class="comments-container"><span id="8983"></span><div id="comment-8983" class="comment"><div id="post-8983-score" class="comment-score"></div><div class="comment-text"><p>See README.developer for proto_tree_add_bits_item() and tvb_get_bits...</p></div><div id="comment-8983-info" class="comment-info"><span class="comment-age">(13 Feb '12, 14:20)</span> Anders ♦</div></div></div><div id="comment-tools-8979" class="comment-tools"></div><div class="clear"></div><div id="comment-8979-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

