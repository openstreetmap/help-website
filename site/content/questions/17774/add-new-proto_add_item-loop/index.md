+++
type = "question"
title = "Add New proto_add_item Loop:"
description = '''My Packet Data: 04 1A 0C 68 00 01 00 00 4D 15 00 04 9D F6 10 3A | 9E 0E 95 34 9E 33 38 D3 75 31 74 63 5E 07: Node: 04 1A Counter: 0C 68 Type: 00 01 Channel: 00 00 RTU: 4D 15 Number of Register(s): 00 04 Register: 9D F6 Register Data: 10 3A I need my Dissector to loop through and add the below until ...'''
date = "2013-01-18T05:54:00Z"
lastmod = "2013-01-18T15:21:00Z"
weight = 17774
keywords = [ "proto_tree_add_item", "dissector", "loop" ]
aliases = [ "/questions/17774" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Add New proto\_add\_item Loop:](/questions/17774/add-new-proto_add_item-loop)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17774-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My Packet Data: 04 1A 0C 68 00 01 00 00 4D 15 00 04 9D F6 10 3A | 9E 0E 95 34 9E 33 38 D3 75 31 74 63 5E 07:</p><p>Node: 04 1A Counter: 0C 68 Type: 00 01 Channel: 00 00 RTU: 4D 15 Number of Register(s): 00 04 Register: 9D F6 Register Data: 10 3A</p><p>I need my Dissector to loop through and add the below until the total Number of Register(s) 00 04 is satisfied: "proto_tree_add_item(ar_tree, hf_ar_reg, tvb, MSG_REG_OS, MSG_REG_SZ, ENC_NA );" &amp; "proto_tree_add_item(ar_tree, hf_ar_regdata, tvb, MSG_REGDATA_OS, MSG_REGDATA_SZ, ENC_NA );"</p><p>Thoughts?</p></div><div id="question-tags" class="tags-container tags">proto_tree_add_item dissector loop</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jan '13, 05:54</strong></p><img src="https://secure.gravatar.com/avatar/1f51b148d3f1f063aa95114ceea3b70f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jballard1979&#39;s gravatar image" /><p>jballard1979<br />
<span class="score" title="20 reputation points">20</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jballard1979 has no accepted answers">0%</span></p></div></div><div id="comments-container-17774" class="comments-container"></div><div id="comment-tools-17774" class="comment-tools"></div><div class="clear"></div><div id="comment-17774-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17782"></span>

<div id="answer-container-17782" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17782-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Trick is to get the value out of the TVB:</p><pre><code>    guint16 num_of_registers = tvb_get_ntohs(tvb, offset);</code></pre>where offset is the offset in the TVB where this count can be found (MSG_NUM_REG_OS ?). Now loop, call proto_tree_add_item() and advance the offset while you go:<pre><code>    offset = MSG_REG_OS;
    for (i=0; i&lt;num_of_registers; i++)
    {
        proto_tree_add_item(ar_tree, hf_ar_reg, tvb, offset, MSG_REG_SZ, ENC_NA);
        offset += MSG_REG_SZ;
        proto_tree_add_item(ar_tree, hf_ar_regdata, tvb, offset, MSG_REGDATA_SZ, ENC_NA);
        offset += MSG_REGDATA_SZ;
    }</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jan '13, 15:21</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Jan '13, 15:22</p></div></div><div id="comments-container-17782" class="comments-container"><span id="17783"></span><div id="comment-17783" class="comment"><div id="post-17783-score" class="comment-score"></div><div class="comment-text"><p>AWESOME... Worked like a charm. Thanks :)</p></div><div id="comment-17783-info" class="comment-info"><span class="comment-age">(18 Jan '13, 16:23)</span> jballard1979</div></div></div><div id="comment-tools-17782" class="comment-tools"></div><div class="clear"></div><div id="comment-17782-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

