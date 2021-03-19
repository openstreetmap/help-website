+++
type = "question"
title = "Recursively dissect data fields"
description = '''I&#x27;m writing a dissector for what is essentially a Google Protocol Buffers message. The details aren&#x27;t important; I end up with a number of fields of bytes. All this is working well. Now, sometimes, and not intrinsically recognizable from the data, a field of bytes may itself be a full message. Is it...'''
date = "2013-05-22T06:27:00Z"
lastmod = "2013-05-22T12:45:00Z"
weight = 21372
keywords = [ "decode_as", "dissector" ]
aliases = [ "/questions/21372" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Recursively dissect data fields](/questions/21372/recursively-dissect-data-fields)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21372-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm writing a dissector for what is essentially a <a href="https://developers.google.com/protocol-buffers/docs/encoding">Google Protocol Buffers</a> message. The details aren't important; I end up with a number of fields of bytes. All this is working well.</p><p>Now, sometimes, and not intrinsically recognizable from the data, a field of bytes may itself be a full message. Is it possible to register the dissector so that I can select just the one data field and say "Decode as..." and interpret the field as another message?</p><pre><code>proto_item *i = proto_tree_add_text(tree, tvb, offset, pre_len + data_len,
                                    &quot;Length-prefixed Data&quot;);
proto_tree *t = proto_item_add_subtree(i, ett_protobuf);

proto_tree_add_text(t, tvb, offset, pre_len, &quot;Len: %llu&quot;, pre_len);
proto_tree_add_bytes(t, hf_protobuf_nested_type, tvb, offset + pre_len, data_len,
                     tvb_get_ptr(tvb, offset + pre_len, data_len));</code></pre><p>(Background: While Protocol Buffer messages contain enough information to describe how <em>long</em> each field is, there is no information on what the field <em>means</em>. It may be just a string of data, <em>or</em> it may be a nested message. That's why there cannot be any other sensible default action that treat a field as an opaque byte string. Only the human operator, who can consult the out-of-band schema, can decide whether the byte string is actually supposed to be a nested message.)</p></div><div id="question-tags" class="tags-container tags">decode_as dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 May '13, 06:27</strong></p><img src="https://secure.gravatar.com/avatar/3dcd36f51cf45ba2e5cfd351cbcf7127?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LouisDx&#39;s gravatar image" /><p>LouisDx<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LouisDx has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 May '13, 06:47</p></div></div><div id="comments-container-21372" class="comments-container"></div><div id="comment-tools-21372" class="comment-tools"></div><div class="clear"></div><div id="comment-21372-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21379"></span>

<div id="answer-container-21379" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21379-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is it possible to register the dissector so that I can select just the one data field and say "Decode As..."</p></blockquote><p>Currently, "Decode As..." is not a general mechanism for which arbitrary dissectors can register a table (so that, for a packet containing the protocol the dissector handles, you can choose to decode something carried by that protocol as some other protocol) and arbitrary dissectors can register in that table (so that they can be chosen with "Decode As...".</p><p>You <em>could</em> create a preference in your dissector to let you select a protocol to decode the payload as.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 May '13, 12:45</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-21379" class="comments-container"><span id="21403"></span><div id="comment-21403" class="comment"><div id="post-21403-score" class="comment-score"></div><div class="comment-text"><p>I understand. Thanks for clarifying!</p></div><div id="comment-21403-info" class="comment-info"><span class="comment-age">(23 May '13, 04:59)</span> LouisDx</div></div></div><div id="comment-tools-21379" class="comment-tools"></div><div class="clear"></div><div id="comment-21379-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21373"></span>

<div id="answer-container-21373" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21373-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It might be possible, but that would be really hard to implement.</p><p>Why not heuristically look at the data bytes. If you assume it is nested, you can extract the length field from the data bytes and then compare that to the actual length of the data bytes. If it matches, you can assume that it is indeed nested. If not, you must assume it is just a data field.</p><p>And maybe there are other constraints in the formatting of the data field that you could use to strengthen the heuristics.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 May '13, 08:01</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-21373" class="comments-container"><span id="21375"></span><div id="comment-21375" class="comment"><div id="post-21375-score" class="comment-score"></div><div class="comment-text"><p>I don't like heuristics in that case. You can always cook up an actually intended string that just happens to <em>look</em> like a message... and you wouldn't know if it was an actual message until you parsed the <em>whole</em> thing. Can you run a dissector tenatively and see if it succeeds?</p></div><div id="comment-21375-info" class="comment-info"><span class="comment-age">(22 May '13, 08:35)</span> LouisDx</div></div><span id="21377"></span><div id="comment-21377" class="comment"><div id="post-21377-score" class="comment-score"></div><div class="comment-text"><p>You would need a routine that just checks whether the tvb contains a valid "Google Protocol Buffer".</p><p>If it returns true, create a new tvb with the string data and recursively call your dissector on it. If not, just display the string data as string. Actually, I would always display the string and use a subtree when the string can be interpreted as an embedded message.</p></div><div id="comment-21377-info" class="comment-info"><span class="comment-age">(22 May '13, 09:36)</span> SYN-bit ♦♦</div></div><span id="21378"></span><div id="comment-21378" class="comment"><div id="post-21378-score" class="comment-score"></div><div class="comment-text"><p>Yeah, I see. I was hoping I could have a UI action such as "decode as" that the user could trigger, without the need for looking ahead and attempting to parse... thanks anyway!</p></div><div id="comment-21378-info" class="comment-info"><span class="comment-age">(22 May '13, 12:32)</span> LouisDx</div></div></div><div id="comment-tools-21373" class="comment-tools"></div><div class="clear"></div><div id="comment-21373-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

