+++
type = "question"
title = "error C2017: illegal escape sequence"
description = '''Compilor is showing &quot;error C2017: illegal escape sequence&quot; to this part of my code.(It&#x27;s inside Header file and showing error everywhere this macro is being called).   #define PROTO_TREE_ADD_HEADER( ife_tree, ife_command, element_start, element_length, proto_item_ti ) &#92;  proto_tree *sub_tree = proto...'''
date = "2016-12-14T08:59:00Z"
lastmod = "2016-12-14T10:11:00Z"
weight = 58085
keywords = [ "dissector", "updateplugin" ]
aliases = [ "/questions/58085" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [error C2017: illegal escape sequence](/questions/58085/error-c2017-illegal-escape-sequence)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58085-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Compilor is showing "error C2017: illegal escape sequence" to this part of my code.(It's inside Header file and showing error everywhere this macro is being called).</p><pre><code> #define PROTO_TREE_ADD_HEADER( ife_tree, ife_command, element_start, element_length, proto_item_ti )                                         \
    proto_tree *sub_tree = proto_tree_add_subtree_format(ife_tree, tvb, element_start, ife_numberOfElements*(element_length),             \
    ett_cidsifecmd_tree, &amp;proto_item_ti, &quot; %s ( %u entries ) &quot;, try_val_to_str( (ife_command),command_name_var ),ife_numberOfElements      \
    );</code></pre><p>what could be the reason? thanks</p></div><div id="question-tags" class="tags-container tags">dissector updateplugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Dec '16, 08:59</strong></p><img src="https://secure.gravatar.com/avatar/a908c48c60a3ba8f08a762a9cb58268f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xaheen&#39;s gravatar image" /><p>xaheen<br />
<span class="score" title="71 reputation points">71</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xaheen has one accepted answer">50%</span></p></div></div><div id="comments-container-58085" class="comments-container"></div><div id="comment-tools-58085" class="comment-tools"></div><div class="clear"></div><div id="comment-58085-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58088"></span>

<div id="answer-container-58088" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58088-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Ensure that you have no trailing space or tab after the \ character.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '16, 10:11</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-58088" class="comments-container"><span id="58158"></span><div id="comment-58158" class="comment"><div id="post-58158-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot :)</p></div><div id="comment-58158-info" class="comment-info"><span class="comment-age">(16 Dec '16, 00:49)</span> xaheen</div></div></div><div id="comment-tools-58088" class="comment-tools"></div><div class="clear"></div><div id="comment-58088-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

