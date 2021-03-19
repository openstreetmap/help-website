+++
type = "question"
title = "proto_tree_add_text() proper replacemnt"
description = '''Tag= tvb_get_guint8(tvb,offset);  offset++; dataType = tvb_get_guint8(tvb,offset); offset++; value = tvb_get_guint8(tvb,offset);  cmdBodyNode = proto_tree_add_text(header_tree, tvb, startValue, 3, &quot;%s: %d&quot;, val_to_str(Tag, Tag_array, &quot;Unknown Tag:(0x%02x)&quot;),value);  proto_tree_add_text(my_child, tvb...'''
date = "2017-05-02T22:07:00Z"
lastmod = "2017-05-03T03:56:00Z"
weight = 61178
keywords = [ "proto_tree_add_text", "dissector", "proto_tree_add_item" ]
aliases = [ "/questions/61178" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [proto\_tree\_add\_text() proper replacemnt](/questions/61178/proto_tree_add_text-proper-replacemnt)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61178-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>Tag= tvb_get_guint8(tvb,offset);    
offset++;
dataType = tvb_get_guint8(tvb,offset);
offset++;
value = tvb_get_guint8(tvb,offset);

cmdBodyNode = proto_tree_add_text(header_tree, tvb, startValue, 3, &quot;%s: %d&quot;, val_to_str(Tag,  Tag_array, &quot;Unknown Tag:(0x%02x)&quot;),value);

proto_tree_add_text(my_child, tvb, startValue++, 1, &quot;DataType: %s&quot;, val_to_str(dataType, dataType_array, &quot;Unknown datatype:(0x%02x)&quot;));</code></pre><p>How to replace the above expression to new add_item () for wire shark 2.2.6 without changing the representation output.</p><p>I have used the <code>convert_proto_tree_add_text.pl</code> file for conversion but output is not as per expected. Can anyone explain how to convert the above proto_tree_add_text() function to any alternative function to be replaced?</p><p>output using <code>convert_proto_tree_add_text.pl</code> Perl script:</p><pre><code>/* Generated from convert_proto_tree_add_text.pl */
static int hf_vrs_s = -1;
static int hf_vrs_datatype = -1;

/* Generated from convert_proto_tree_add_text.pl */
{ &amp;hf_vrs_s, { &quot;s&quot;, &quot;vrs.s&quot;, FT_UINT24, BASE_HEX, VALS(VALS(value_string_array)), 0x0, NULL, HFILL }},
{ &amp;hf_vrs_datatype, { &quot;DataType&quot;, &quot;vrs.datatype&quot;, FT_UINT8, BASE_HEX, VALS(VALS(dataType_array)), 0x0, NULL, HFILL }},

/* Generated from convert_proto_tree_add_text.pl */
cmdBodyNode = proto_tree_add_item(vrs_header_tree, hf_vrs_%s, tvb, startValue, 3, ENC_NA);
proto_tree_add_item(vrs_child, hf_vrs_datatype, tvb, startValue++, 1, ENC_NA);</code></pre></div><div id="question-tags" class="tags-container tags">proto_tree_add_text dissector proto_tree_add_item</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '17, 22:07</strong></p><img src="https://secure.gravatar.com/avatar/dd3150a05afbc3bd37fe041a2541f609?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="a6mishra&#39;s gravatar image" /><p>a6mishra<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="a6mishra has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 May '17, 03:05</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-61178" class="comments-container"></div><div id="comment-tools-61178" class="comment-tools"></div><div class="clear"></div><div id="comment-61178-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61189"></span>

<div id="answer-container-61189" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61189-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As you have noted the perl script does not handle the way this dissector is coded. You will have to do the conversion by hand. The main reason for removing proto_tree_add_text() is to enforce the use of hf variables to facilitate filtering which is one of the main features of Wireshark. It will be difficult to not "changing the representation output". But changing it will actually improve the dissector in my opinion. For the example above I'd define 3 hf variables "tag" "datatype" and "value" and just do proto_tree_add_item() for each one of them. As an alternative you can use proto_tree_add_subtree_format() but that would defy the purpose of removing proto_tree_add_text().</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '17, 03:56</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-61189" class="comments-container"></div><div id="comment-tools-61189" class="comment-tools"></div><div class="clear"></div><div id="comment-61189-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

