+++
type = "question"
title = "Dynamically add subtrees"
description = '''I&#x27;m coding a dissector and want to dynamically add subtrees depending on number of parameters detected in the packet. Is there a way to do that? '''
date = "2013-07-04T04:59:00Z"
lastmod = "2013-07-09T05:09:00Z"
weight = 22641
keywords = [ "dissector", "1.10.0" ]
aliases = [ "/questions/22641" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Dynamically add subtrees](/questions/22641/dynamically-add-subtrees)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22641-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm coding a dissector and want to dynamically add subtrees depending on number of parameters detected in the packet. Is there a way to do that?</p></div><div id="question-tags" class="tags-container tags">dissector 1.10.0</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jul '13, 04:59</strong></p><img src="https://secure.gravatar.com/avatar/c9aa1d36ff8501f13272de4dafa34854?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrey&#39;s gravatar image" /><p>Andrey<br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrey has one accepted answer">50%</span></p></div></div><div id="comments-container-22641" class="comments-container"><span id="22642"></span><div id="comment-22642" class="comment"><div id="post-22642-score" class="comment-score"></div><div class="comment-text"><p>I'm not certain of your question, most dissectors do something like that anyway as they dissect the packet.</p><p>Can you explain with some more detail what you want to achieve?</p></div><div id="comment-22642-info" class="comment-info"><span class="comment-age">(04 Jul '13, 05:22)</span> grahamb ♦</div></div><span id="22643"></span><div id="comment-22643" class="comment"><div id="post-22643-score" class="comment-score"></div><div class="comment-text"><p>Packet from the application can have variable length and can accommodate from 0 to 255 parameters. I want my dissector to make a subtree for each parameter having subitems which split parameters into searchable fields.</p></div><div id="comment-22643-info" class="comment-info"><span class="comment-age">(04 Jul '13, 05:24)</span> Andrey</div></div><span id="22649"></span><div id="comment-22649" class="comment"><div id="post-22649-score" class="comment-score"></div><div class="comment-text"><p>This all seems very normal, just create subtrees as required and then populate them with data items.</p><p>Subtrees are for presentation layout in the packet details pane, the hf structures determine what is filterable.</p></div><div id="comment-22649-info" class="comment-info"><span class="comment-age">(04 Jul '13, 06:25)</span> grahamb ♦</div></div><span id="22651"></span><div id="comment-22651" class="comment"><div id="post-22651-score" class="comment-score"></div><div class="comment-text"><p>As I understood I have to define new proto_itme for each subtree. I can't understand how to get a new one in a loop, since I have same variable.</p></div><div id="comment-22651-info" class="comment-info"><span class="comment-age">(04 Jul '13, 06:36)</span> Andrey</div></div><span id="22652"></span><div id="comment-22652" class="comment"><div id="post-22652-score" class="comment-score"></div><div class="comment-text"><p>I just made an array of proto_item of size 255. Is it fine to do that?</p></div><div id="comment-22652-info" class="comment-info"><span class="comment-age">(04 Jul '13, 06:59)</span> Andrey</div></div><span id="22653"></span><div id="comment-22653" class="comment not_top_scorer"><div id="post-22653-score" class="comment-score"></div><div class="comment-text"><p>If it's on the stack, that'll be fine. If you allocate it some way then you'll have to make sure it's freed correctly.</p></div><div id="comment-22653-info" class="comment-info"><span class="comment-age">(04 Jul '13, 07:02)</span> grahamb ♦</div></div></div><div id="comment-tools-22641" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-22641-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22753"></span>

<div id="answer-container-22753" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22753-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Found a better solution. Moved recurrent dissection routine to dedicated function providing it the same tree and calling it in a variable loop (which depends on number it dissects earlier). In this case I don't have to keep handles for items in array.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jul '13, 05:09</strong></p><img src="https://secure.gravatar.com/avatar/c9aa1d36ff8501f13272de4dafa34854?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrey&#39;s gravatar image" /><p>Andrey<br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrey has one accepted answer">50%</span></p></div></div><div id="comments-container-22753" class="comments-container"></div><div id="comment-tools-22753" class="comment-tools"></div><div class="clear"></div><div id="comment-22753-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

