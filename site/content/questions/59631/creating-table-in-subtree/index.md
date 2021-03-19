+++
type = "question"
title = "Creating Table in subtree"
description = '''I have been trying to update a plugin(from 1.6 to 2.2). In the previous plugin, the following code was used to create a table data. for (row = 0; row &amp;lt; 10; row++) {  proto_tree_add_text(command_tree, tvb, FIRSTELEMENT_START + 2*row, ELEMENT_LENGTH, &quot;PA%u&#92;t%s&#92;t%s&#92;t%s %s %u&quot;,  row + 1,  try_val_to_...'''
date = "2017-02-23T07:10:00Z"
lastmod = "2017-02-24T01:59:00Z"
weight = 59631
keywords = [ "table", "proto_tree_add_text", "subtree", "updateplugin" ]
aliases = [ "/questions/59631" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Creating Table in subtree](/questions/59631/creating-table-in-subtree)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59631-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have been trying to update a plugin(from 1.6 to 2.2). In the previous plugin, the following code was used to create a table data.</p><pre><code>for (row = 0; row &lt; 10; row++) {
                proto_tree_add_text(command_tree, tvb, FIRSTELEMENT_START + 2*row, ELEMENT_LENGTH,    &quot;PA%u\t%s\t%s\t%s %s %u&quot;,
                        row + 1,
                        try_val_to_str(pa_array[row][0], discrete_status_var),
                        try_val_to_str(pa_array[row][1], discrete_status_var),
                        try_val_to_str(pa_array[row][2], source_deck_var),
                        try_val_to_str(pa_array[row][3], source_type_var),
                        pa_array[row][4]
                );
            }</code></pre><p>I have been trying to replace the proto_tree_add_text by proto_tree_add_item to achieve the same result, but without any success. Can someone please help me? Thanks a lot.</p></div><div id="question-tags" class="tags-container tags">table proto_tree_add_text subtree updateplugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Feb '17, 07:10</strong></p><img src="https://secure.gravatar.com/avatar/a908c48c60a3ba8f08a762a9cb58268f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xaheen&#39;s gravatar image" /><p>xaheen<br />
<span class="score" title="71 reputation points">71</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xaheen has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Feb '17, 08:10</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-59631" class="comments-container"></div><div id="comment-tools-59631" class="comment-tools"></div><div class="clear"></div><div id="comment-59631-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59655"></span>

<div id="answer-container-59655" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59655-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use proto_tree_add_XXX_format() functions but combining several values on the same line defeats the possibility to filter individual items, so it is not encouraged.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Feb '17, 01:59</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-59655" class="comments-container"><span id="59672"></span><div id="comment-59672" class="comment"><div id="post-59672-score" class="comment-score">1</div><div class="comment-text"><p>What they <em>could</em> do is create a top-level item with multiple values and then put each of the individual values as named fields underneath that top-level item.</p></div><div id="comment-59672-info" class="comment-info"><span class="comment-age">(24 Feb '17, 13:46)</span> Guy Harris ♦♦</div></div><span id="59703"></span><div id="comment-59703" class="comment"><div id="post-59703-score" class="comment-score"></div><div class="comment-text"><p>Could you please tell me where I can find some example use of proto_tree_add_XXX_format()? Thanks @Pascal Quantin @Guy Harris</p></div><div id="comment-59703-info" class="comment-info"><span class="comment-age">(27 Feb '17, 02:07)</span> xaheen</div></div><span id="59947"></span><div id="comment-59947" class="comment"><div id="post-59947-score" class="comment-score"></div><div class="comment-text"><p>Proto_tree_add_string_format works perfectly! :D</p></div><div id="comment-59947-info" class="comment-info"><span class="comment-age">(09 Mar '17, 00:41)</span> xaheen</div></div></div><div id="comment-tools-59655" class="comment-tools"></div><div class="clear"></div><div id="comment-59655-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

