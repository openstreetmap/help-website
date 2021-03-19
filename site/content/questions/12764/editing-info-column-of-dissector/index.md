+++
type = "question"
title = "Editing info column of dissector"
description = '''I am trying to edit an existing dissector to make it display some values in the info column.  Currently, I am able to do this to a certain extent and display values that come from a value_string array, using the val_to_str function. However, now I want to be able to display other values that are con...'''
date = "2012-07-16T07:55:00Z"
lastmod = "2012-07-23T07:18:00Z"
weight = 12764
keywords = [ "dissector", "val_to_str" ]
aliases = [ "/questions/12764" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Editing info column of dissector](/questions/12764/editing-info-column-of-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12764-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to edit an existing dissector to make it display some values in the info column. Currently, I am able to do this to a certain extent and display values that come from a value_string array, using the val_to_str function. However, now I want to be able to display other values that are contained within an array of the type hf_register_info.</p><p>I am having trouble doing this with the val_to_str function and wondering if there is a different function I would have to use or if/how it can be done with val_to_str.</p><p>Here is part of the array I am trying to take the data from.</p><p>static hf_register_info hf[] = { { &amp;hf_pfcp_vc_base_port, { "PFCP VC Base Port", "pfcp.vc_base_port", FT_UINT16, BASE_DEC, NULL, 0, NULL, HFILL } } }</p><p>Thanks for any help.</p></div><div id="question-tags" class="tags-container tags">dissector val_to_str</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jul '12, 07:55</strong></p><img src="https://secure.gravatar.com/avatar/f930b778c54e8c2d76dbcc36f76087ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bball2601&#39;s gravatar image" /><p>bball2601<br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bball2601 has one accepted answer">50%</span></p></div></div><div id="comments-container-12764" class="comments-container"></div><div id="comment-tools-12764" class="comment-tools"></div><div class="clear"></div><div id="comment-12764-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12918"></span>

<div id="answer-container-12918" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12918-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What do you want to extract from the hf_ field? You might want to look at proto_tree_fill_label().</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '12, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-12918" class="comments-container"></div><div id="comment-tools-12918" class="comment-tools"></div><div class="clear"></div><div id="comment-12918-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

