+++
type = "question"
title = "Why does the &quot;decode as&quot; dialog only shows entrys for link layer."
description = '''I am working on different plugin dissectors to dissect following Protocol stack: Ethernet -&amp;gt; ProtoA -&amp;gt; ProtoB or C. In the proto_register_a() funktion i call:  register_dissector_table(&quot;a.next&quot;,&quot;A next protocol&quot;, FT_UINT16, BASE_HEX); In the proto_reg_handoff_a() funktion i call: dissector_add...'''
date = "2013-02-22T06:35:00Z"
lastmod = "2013-02-22T08:36:00Z"
weight = 18814
keywords = [ "development", "decode_as", "dissector", "plugin" ]
aliases = [ "/questions/18814" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why does the "decode as" dialog only shows entrys for link layer.](/questions/18814/why-does-the-decode-as-dialog-only-shows-entrys-for-link-layer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18814-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am working on different plugin dissectors to dissect following Protocol stack: Ethernet -&gt; ProtoA -&gt; ProtoB or C.</p><p>In the <code>proto_register_a()</code> funktion i call:</p><p><code>register_dissector_table("a.next","A next protocol", FT_UINT16, BASE_HEX);</code></p><p>In the <code>proto_reg_handoff_a()</code> funktion i call:</p><p><code>dissector_add("ethertype", ETHERTYPE_A, a_handle);</code></p><p>In the <code>proto_reg_handoff_b()</code> funktion i call:</p><p><code>dissector_add("a.next", A_NEXT_VALUE_B, b_handle);</code></p><p>In the <code>proto_reg_handoff_c()</code> funktion i call:</p><p><code>dissector_add("a.next", A_NEXT_VALUE_C, c_handle);</code></p><p>Everything is decoded just fine, but still if i open the decode as dialog only the link layer dissectors are shown and i cant choose to decode ProtocolB as ProtocolC.</p><p>What do I miss?</p></div><div id="question-tags" class="tags-container tags">development decode_as dissector plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Feb '13, 06:35</strong></p><img src="https://secure.gravatar.com/avatar/185083c8db06582884d278234f8997df?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andreas%20Wilkes&#39;s gravatar image" /><p>Andreas Wilkes<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andreas Wilkes has no accepted answers">0%</span></p></div></div><div id="comments-container-18814" class="comments-container"></div><div id="comment-tools-18814" class="comment-tools"></div><div class="clear"></div><div id="comment-18814-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18815"></span>

<div id="answer-container-18815" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18815-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Adding a dissector table dosen not automatically add it to "decode as", isn't there any indication in proto A to say if the payload is B or C?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Feb '13, 08:36</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-18815" class="comments-container"><span id="18826"></span><div id="comment-18826" class="comment"><div id="post-18826-score" class="comment-score">1</div><div class="comment-text"><p>I.e., at least currently, "decode as" is not a general UI mechanism for all dissector tables, it has a small number of dissector tables (Ethertype, TCP/UDP/etc. ports, DCE RPC) wired into it.</p></div><div id="comment-18826-info" class="comment-info"><span class="comment-age">(22 Feb '13, 15:18)</span> Guy Harris ♦♦</div></div><span id="18919"></span><div id="comment-18919" class="comment"><div id="post-18919-score" class="comment-score"></div><div class="comment-text"><p>Good to know that the decode as does not automatically works for plugins. @Anders There is an indication which protocol follows but the reason i wanted the decode as functionality is to be able to decode something what is indicated to be B as C (i.e. if the next field in A is filled with the wrong value.)</p></div><div id="comment-18919-info" class="comment-info"><span class="comment-age">(27 Feb '13, 02:14)</span> Andreas Wilkes</div></div><span id="18920"></span><div id="comment-18920" class="comment"><div id="post-18920-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Good to know that the decode as does not automatically works for plugins.</p></blockquote><p>"Decode as" doesn't automatically work for arbitrary dissector tables, regardless of whether the dissector table was created by a plugin or a built-in dissector; this problem would exist even if Wireshark didn't support plugins.</p></div><div id="comment-18920-info" class="comment-info"><span class="comment-age">(27 Feb '13, 02:24)</span> Guy Harris ♦♦</div></div><span id="18921"></span><div id="comment-18921" class="comment"><div id="post-18921-score" class="comment-score"></div><div class="comment-text"><blockquote><p>There is an indication which protocol follows but the reason i wanted the decode as functionality is to be able to decode something what is indicated to be B as C (i.e. if the next field in A is filled with the wrong value.)</p></blockquote><p>You could try adding a preference to the protocol A dissector to specify that it should, for example, treat a next-protocol value of B as if it were C. ("Decode as", even if and when it supports arbitrary dissector tables, wouldn't let you specify this on a per-packet basis - the whole point is to override the dissector choice for <em>all</em> packets with a given value.)</p></div><div id="comment-18921-info" class="comment-info"><span class="comment-age">(27 Feb '13, 02:26)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-18815" class="comment-tools"></div><div class="clear"></div><div id="comment-18815-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

