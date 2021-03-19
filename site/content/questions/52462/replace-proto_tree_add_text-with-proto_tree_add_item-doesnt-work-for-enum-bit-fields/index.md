+++
type = "question"
title = "Replace proto_tree_add_text with proto_tree_add_item doesn&#x27;t work for Enum Bit Fields"
description = '''Hi I have an requirement in which 1 byte is splited to two fileds each of 4 bits and in which enumeration is defined. Earlier i used to use proto_tree_add_text to perform these operation. but where as now proto_tree_add_item won&#x27;t allow to show the exact 4bit value. (Because of HF_TYPE or HF_Value) ...'''
date = "2016-05-12T03:04:00Z"
lastmod = "2016-05-13T06:30:00Z"
weight = 52462
keywords = [ "proto_tree_add_text", "protocol", "bit_enumeration", "wireshark" ]
aliases = [ "/questions/52462" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Replace proto\_tree\_add\_text with proto\_tree\_add\_item doesn't work for Enum Bit Fields](/questions/52462/replace-proto_tree_add_text-with-proto_tree_add_item-doesnt-work-for-enum-bit-fields)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52462-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I have an requirement in which 1 byte is splited to two fileds each of 4 bits and in which enumeration is defined. Earlier i used to use proto_tree_add_text to perform these operation. but where as now proto_tree_add_item won't allow to show the exact 4bit value. (Because of HF_TYPE or HF_Value)</p><h2 id="example">Example:</h2><p>--------------Master Field: 0x40 [Parent Tree]</p><p>1.) First Bit Field - 0x8 (Eight Bit Data enum) [Subtree data for parent tree]</p><p>2.) Second Bit - 0x32 (ThirtyTwo Bit Data enum) [Subtree data for parent tree]</p><p>Based on those two values 0x8 and 0x32, i have to perform operation on the below upcoming fileds.</p><h2 id="code-snippet">code snippet:</h2><pre><code>/* Old Wireshar Version 1.12.7 */
main_tree_value = tvb_get_guint8(tvb, offset);
if(parent_tree) {
    item = proto_tree_add_uint(parent_tree, hf_main_tree, tvb,
            offset, 1, main_tree_value);

    main_tree = proto_item_add_subtree(item, ett_main_tree);
}

second_bit_value = tvb_get_bits8(tvb, (offset*8),4);
first_bit_value = tvb_get_bits8(tvb, ((offset*8)+4),4);
if(main_tree) {
proto_tree_add_text(main_tree, tvb, offset, 1,
            &quot;First Bit Field   : %u (%s)&quot;,
            first_bit_value,
            val_to_str(first_bit_value, first_bit_value_enum_flag, &quot;Unknown&quot;));
}
if(main_tree) {
proto_tree_add_text(main_tree, tvb, offset, 1,
            &quot;Second Bit Field   : %u (%s)&quot;,
            second_bit_value,
            val_to_str(second_bit_value, second_bit_value_enum_flag, &quot;Unknown&quot;));
}
offset = offset + 1;

/*  Wireshark Version 2.0.3 */
main_tree_value = tvb_get_guint8(tvb, offset);
if(parent_tree) {
    item = proto_tree_add_uint(parent_tree, hf_main_tree, tvb,
            offset, 1, main_tree_value);
    main_tree = proto_item_add_subtree(item, ett_main_tree);
}

second_bit_value = tvb_get_bits8(tvb, (offset*8),4);
first_bit_value = tvb_get_bits8(tvb, ((offset*8)+4),4);
if(main_tree) {
            enum_tree = proto_tree_add_item(main_tree, hf_first_bit_field, tvb, offset, 1, FALSE);
            proto_item_append_text (enum_tree, &quot; (%s)&quot;, val_to_str(first_bit_value, first_bit_value_enum_flag, &quot;Unknown&quot;));
}
if(main_tree) {
            enum_tree = proto_tree_add_item(main_tree, hf_second_bit_field, tvb, offset, 1, FALSE);
            proto_item_append_text (enum_tree, &quot; (%s)&quot;, val_to_str(second_bit_value, second_bit_value_enum_flag, &quot;Unknown&quot;));
}
offset = offset + 1;</code></pre><p>Please suggest me, how i can define HF_TYPE or HF_VALUE or if any other.</p><p>Regards</p><p>Dinesh Sadu</p></div><div id="question-tags" class="tags-container tags">proto_tree_add_text protocol bit_enumeration wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 May '16, 03:04</strong></p><img src="https://secure.gravatar.com/avatar/04334c27cb629065a13d61a61b611038?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dinesh%20Babu%20Sadu&#39;s gravatar image" /><p>Dinesh Babu ...<br />
<span class="score" title="16 reputation points">16</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dinesh Babu Sadu has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 May '16, 08:50</p></div></div><div id="comments-container-52462" class="comments-container"></div><div id="comment-tools-52462" class="comment-tools"></div><div class="clear"></div><div id="comment-52462-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52507"></span>

<div id="answer-container-52507" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52507-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>What you've got looks like a good start. Next steps should be to:</p><ol><li>Don't bother calling <code>tvb_get_bits8()</code>: you won't need it.</li><li>Remove the <code>proto_tree_append_text()</code> calls; you won't need them.</li><li>Set the BITFIELD part of <code>hf_*_bit_field</code> appropriately; looks like it should be 0xf0 for the first bitfield and 0x0f for the second bitfield.</li><li>Put <code>VALS(*_bit_value_enum_flag)</code> in the FIELDCONVERT sections of the two bit_field hf's.</li><li>Make sure the offset is correct in the two <code>proto_tree_add_item()</code> calls.</li></ol><p>If that doesn't work another way would be to use <code>proto_tree_add_uint(main_tree, hf_first_bit_field, tvb, offset, 1, first_bit_value)</code> and then put <code>VALS(first_bit_value_enum_flag)</code> in the FIELDCONVERT section of <code>hf_first_bit_field</code> (thus avoiding the use of <code>proto_item_append_text()</code>).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '16, 06:30</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-52507" class="comments-container"></div><div id="comment-tools-52507" class="comment-tools"></div><div class="clear"></div><div id="comment-52507-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

