+++
type = "question"
title = "How to implement collapsed subtrees in Wireshark?"
description = '''Hi there, I&#x27;m implementing a dissector. Whenever, I add a subtree by using proto_item_add_subtree() to my protocol tree, It appears in the GUI interface of wireshark expanded by default. I&#x27;ve noticed this not the case with the others dissectors such as SSL for example ( Its subtrees are collapsed by...'''
date = "2014-12-02T21:08:00Z"
lastmod = "2014-12-02T22:14:00Z"
weight = 38289
keywords = [ "development", "dissector", "subtrees", "wireshark" ]
aliases = [ "/questions/38289" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to implement collapsed subtrees in Wireshark?](/questions/38289/how-to-implement-collapsed-subtrees-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38289-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>I'm implementing a dissector. Whenever, I add a subtree by using <strong>proto_item_add_subtree()</strong> to my protocol tree, It appears in the GUI interface of wireshark expanded by default. I've noticed this not the case with the others dissectors such as SSL for example ( Its subtrees are collapsed by default). I want my subtrees to look collapsed by default also but I'm not sure how! Any help,hints would be appreciated.... thanks.</p></div><div id="question-tags" class="tags-container tags">development dissector subtrees wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '14, 21:08</strong></p><img src="https://secure.gravatar.com/avatar/5642d9fe33d29ee47043f7e5796e67aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flora&#39;s gravatar image" /><p>flora<br />
<span class="score" title="156 reputation points">156</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flora has 2 accepted answers">100%</span></p></div></div><div id="comments-container-38289" class="comments-container"></div><div id="comment-tools-38289" class="comment-tools"></div><div class="clear"></div><div id="comment-38289-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38291"></span>

<div id="answer-container-38291" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38291-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You are probably using the same ett_ variable for all your subtrees, leading to this behavior. Use a different ett_ variable per subtree type and they will appear collapsed. The opened one will be remembered when you change the packet viewed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '14, 22:14</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-38291" class="comments-container"><span id="38307"></span><div id="comment-38307" class="comment"><div id="post-38307-score" class="comment-score"></div><div class="comment-text"><p>This works for me. I was using the same tree type for all of my subtrees. Thanks!</p></div><div id="comment-38307-info" class="comment-info"><span class="comment-age">(03 Dec '14, 08:58)</span> flora</div></div></div><div id="comment-tools-38291" class="comment-tools"></div><div class="clear"></div><div id="comment-38291-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

