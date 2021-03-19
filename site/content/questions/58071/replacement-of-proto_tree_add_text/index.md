+++
type = "question"
title = "replacement of proto_tree_add_text()"
description = '''is there any function other than proto_tree_add_item() in the new API, which could easily be implemented as a replacement of proto_tree_add_text()? especially for printf style implementation of proto_tree_add_text()  for example : proto_tree_add_text(command_tree, tvb, 14, 1, &quot;Roof Shed:&#92;t&#92;t%s&quot;, try...'''
date = "2016-12-14T03:46:00Z"
lastmod = "2016-12-14T04:35:00Z"
weight = 58071
keywords = [ "development", "proto_tree_add_text", "dissector", "plugin" ]
aliases = [ "/questions/58071" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [replacement of proto\_tree\_add\_text()](/questions/58071/replacement-of-proto_tree_add_text)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58071-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>is there any function other than proto_tree_add_item() in the new API, which could easily be implemented as a replacement of proto_tree_add_text()? especially for printf style implementation of proto_tree_add_text() for example :</p><p><code>proto_tree_add_text(command_tree, tvb, 14, 1, "Roof Shed:\t\t%s", try_val_to_str(getbits(tvb_get_guint8(tvb, 14), 5, 2), discrete_status_var));</code></p></div><div id="question-tags" class="tags-container tags">development proto_tree_add_text dissector plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Dec '16, 03:46</strong></p><img src="https://secure.gravatar.com/avatar/a908c48c60a3ba8f08a762a9cb58268f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xaheen&#39;s gravatar image" /><p>xaheen<br />
<span class="score" title="71 reputation points">71</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xaheen has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Dec '16, 05:20</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-58071" class="comments-container"></div><div id="comment-tools-58071" class="comment-tools"></div><div class="clear"></div><div id="comment-58071-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58073"></span>

<div id="answer-container-58073" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58073-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>What's wrong with proto_tree_add_bits_item(command_tree, hf_roof_shed, tvb, 14&lt;&lt;3+5, 2, ENC_BIG_ENDIAN);</p><pre><code>{ &amp;hf_roof_shed, { &quot;Roof Shed&quot;, &quot;x.roof_shed&quot;, FT_UINT8, BASE_DEC, VALS(discrete_status_var), 0x0, NULL, HFILL }},</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '16, 04:35</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-58073" class="comments-container"><span id="58074"></span><div id="comment-58074" class="comment"><div id="post-58074-score" class="comment-score"></div><div class="comment-text"><p>Thanks. I will try it. But it seems almost similar to proto_tree_add_item.</p></div><div id="comment-58074-info" class="comment-info"><span class="comment-age">(14 Dec '16, 04:49)</span> xaheen</div></div><span id="59205"></span><div id="comment-59205" class="comment"><div id="post-59205-score" class="comment-score"></div><div class="comment-text"><p>@anders Could you please explain the reason for writing "14&lt;&lt;3+5, 2"? Thanks</p></div><div id="comment-59205-info" class="comment-info"><span class="comment-age">(01 Feb '17, 02:09)</span> xaheen</div></div><span id="59209"></span><div id="comment-59209" class="comment"><div id="post-59209-score" class="comment-score">1</div><div class="comment-text"><p>proto_tree_add_bits_item takas an offset and length in bits and not bytes.</p><p>So 14&lt;&lt;3+5 = 14*8+5 = 117 bits since the beginning of the tvb. 2 is the number of bits to be read from the offset.</p></div><div id="comment-59209-info" class="comment-info"><span class="comment-age">(01 Feb '17, 04:09)</span> Pascal Quantin</div></div><span id="59222"></span><div id="comment-59222" class="comment"><div id="post-59222-score" class="comment-score">1</div><div class="comment-text"><p>And that was a shot in the dark at what I assumed the previous code tried to do :-)</p></div><div id="comment-59222-info" class="comment-info"><span class="comment-age">(01 Feb '17, 07:16)</span> Anders ♦</div></div></div><div id="comment-tools-58073" class="comment-tools"></div><div class="clear"></div><div id="comment-58073-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

