+++
type = "question"
title = "problem converting proto_tree_add_text"
description = '''I am upgrading the plugin for 2.2 from 1.6. I am having Trouble with the conversion of proto_tree_add_text to proto_tree_add_item for such cases. How do I write the hf variable for the following case :  proto_tree_add_text(command_tree, tvb, 7, 1, &quot;Direct PA:&#92;t&#92;t%s&quot;, match_strval(getbits(tvb_get_gui...'''
date = "2017-02-01T03:24:00Z"
lastmod = "2017-02-01T04:13:00Z"
weight = 59208
keywords = [ "proto_tree_add_item", "dissector", "proto_tree_add_text", "updateplugin", "plugin" ]
aliases = [ "/questions/59208" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [problem converting proto\_tree\_add\_text](/questions/59208/problem-converting-proto_tree_add_text)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59208-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am upgrading the plugin for 2.2 from 1.6. I am having Trouble with the conversion of proto_tree_add_text to proto_tree_add_item for such cases. How do I write the hf variable for the following case :</p><pre><code>proto_tree_add_text(command_tree, tvb,  7, 1, &quot;Direct PA:\t\t%s&quot;, match_strval(getbits(tvb_get_guint8(tvb, 7), 1, 2), discrete_status_var));</code></pre><p>From the example souce codes, It seems to me that it should be like this:</p><pre><code>static int hf_cidsifecmd_direct_pa = -1;
{&amp;hf_cidsifecmd_direct_pa, { &quot;Direct PA:&quot;, &quot;cidsifecmd_direct.pa&quot;, FT_UINT8, BASE_DEC, VALS (discrete_status_var), 0x0, NULL, HFILL}},
  proto_tree_add_item(command_tree, hf_direct_pa, tvb, offset, msg_length, ENC_BIG_ENDIAN);</code></pre><p>is this correct way to do it? I cant understand how "match_strval()" is going to work on this. Thanks.</p></div><div id="question-tags" class="tags-container tags">proto_tree_add_item dissector proto_tree_add_text updateplugin plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Feb '17, 03:24</strong></p><img src="https://secure.gravatar.com/avatar/a908c48c60a3ba8f08a762a9cb58268f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xaheen&#39;s gravatar image" /><p>xaheen<br />
<span class="score" title="71 reputation points">71</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xaheen has one accepted answer">50%</span></p></div></div><div id="comments-container-59208" class="comments-container"></div><div id="comment-tools-59208" class="comment-tools"></div><div class="clear"></div><div id="comment-59208-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59210"></span>

<div id="answer-container-59210" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59210-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Previous code was fetching 2 bits only, so use a bitmask in your hf_cidsifecmd_direct_pa declaration:</p><pre><code>{&amp;hf_cidsifecmd_direct_pa, { &quot;Direct PA&quot;, &quot;cidsifecmd_direct.pa&quot;, FT_UINT8, BASE_DEC, VALS (discrete_status_var), 0x60, NULL, HFILL}},
proto_tree_add_item(command_tree, hf_cidsifecmd_direct_pa, tvb, 7, 1, ENC_BIG_ENDIAN);</code></pre><p>Or use proto_tree_add_bits_item like in your <a href="https://ask.wireshark.org/questions/58071/replacement-of-proto_tree_add_text">previous question</a>:</p><pre><code>{&amp;hf_cidsifecmd_direct_pa, { &quot;Direct PA&quot;, &quot;cidsifecmd_direct.pa&quot;, FT_UINT8, BASE_DEC, VALS (discrete_status_var), 0x0, NULL, HFILL}},
proto_tree_add_bits_item(command_tree, hf_cidsifecmd_direct_pa, tvb, 7&lt;&lt;3+1, 2, ENC_BIG_ENDIAN);</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Feb '17, 04:13</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-59210" class="comments-container"><span id="59211"></span><div id="comment-59211" class="comment"><div id="post-59211-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot :)</p></div><div id="comment-59211-info" class="comment-info"><span class="comment-age">(01 Feb '17, 04:30)</span> xaheen</div></div><span id="59214"></span><div id="comment-59214" class="comment"><div id="post-59214-score" class="comment-score"></div><div class="comment-text"><p>@Pascal Quantin in the previous code, (as I have understood seeing the real wireshark output)</p><p>match_strval(getbits(tvb_get_guint8(tvb, 7), 1, 2), discrete_status_var));</p><p>makes sure that the value taken from two bits are compared with the index of "discrete_status_var" to Output the desired value from "discrete_status_var".</p><p>How is that done in the new code? Thanks</p></div><div id="comment-59214-info" class="comment-info"><span class="comment-age">(01 Feb '17, 05:08)</span> xaheen</div></div><span id="59216"></span><div id="comment-59216" class="comment"><div id="post-59216-score" class="comment-score">1</div><div class="comment-text"><p>Have a look at proto_tree_add_item() and proto_tree_add_bit_item() source code (more specifically the proto_tree_add_uint() and fill_label_number() sub functions). fill_label_number() takes care of the value_string search.</p></div><div id="comment-59216-info" class="comment-info"><span class="comment-age">(01 Feb '17, 05:23)</span> Pascal Quantin</div></div><span id="59217"></span><div id="comment-59217" class="comment"><div id="post-59217-score" class="comment-score"></div><div class="comment-text"><p>Thanks :) will do</p></div><div id="comment-59217-info" class="comment-info"><span class="comment-age">(01 Feb '17, 05:35)</span> xaheen</div></div></div><div id="comment-tools-59210" class="comment-tools"></div><div class="clear"></div><div id="comment-59210-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

