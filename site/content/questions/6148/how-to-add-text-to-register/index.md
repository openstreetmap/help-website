+++
type = "question"
title = "How to add text to register"
description = '''I would like to have proto_tree_add_text() in static hf_register_info hf[] = {}... i.e. i would like to display the text in the pane2 as a column in pane1....'''
date = "2011-09-06T22:54:00Z"
lastmod = "2011-09-07T00:19:00Z"
weight = 6148
keywords = [ "dissector" ]
aliases = [ "/questions/6148" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to add text to register](/questions/6148/how-to-add-text-to-register)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6148-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to have proto_tree_add_text() in static hf_register_info hf[] = {}... i.e. i would like to display the text in the pane2 as a column in pane1....</p></div><div id="question-tags" class="tags-container tags">dissector</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Sep '11, 22:54</strong></p><img src="https://secure.gravatar.com/avatar/264adc05b644c1ab2d670b4773a12392?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flashkicker&#39;s gravatar image" /><p>flashkicker<br />
<span class="score" title="109 reputation points">109</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flashkicker has 5 accepted answers">41%</span></p></div></div><div id="comments-container-6148" class="comments-container"></div><div id="comment-tools-6148" class="comment-tools"></div><div class="clear"></div><div id="comment-6148-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6151"></span>

<div id="answer-container-6151" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6151-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>With proto_tree_add_text(), there is only a text label placed in pane2. If you want to use the data as a field (to be able to filter on it and add it as a column), you will need to use one of the other proto_tree_add_* functions (that do use a hf variable).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '11, 00:19</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-6151" class="comments-container"><span id="6152"></span><div id="comment-6152" class="comment"><div id="post-6152-score" class="comment-score"></div><div class="comment-text"><p>ya since we dont have hfindex in it we cant add it ...do we have a function where we can add hex elements into the pane1 i would like 16 bytes from the raw data to be separated by a single whitespace under a single name</p></div><div id="comment-6152-info" class="comment-info"><span class="comment-age">(07 Sep '11, 00:32)</span> flashkicker</div></div><span id="6155"></span><div id="comment-6155" class="comment"><div id="post-6155-score" class="comment-score"></div><div class="comment-text"><p>Have a look at all the proto_tree_add_* functions in epan/proto.h</p><p>I think proto_tree_add_bytesformat() would fit your need best.</p></div><div id="comment-6155-info" class="comment-info"><span class="comment-age">(07 Sep '11, 00:51)</span> SYN-bit ♦♦</div></div><span id="6159"></span><div id="comment-6159" class="comment"><div id="post-6159-score" class="comment-score"></div><div class="comment-text"><p>yes it does.... i'm now checking it out now.... :)...Thanks a lot</p></div><div id="comment-6159-info" class="comment-info"><span class="comment-age">(07 Sep '11, 01:10)</span> flashkicker</div></div><span id="6162"></span><div id="comment-6162" class="comment"><div id="post-6162-score" class="comment-score"></div><div class="comment-text"><p>Done its up and working</p></div><div id="comment-6162-info" class="comment-info"><span class="comment-age">(07 Sep '11, 01:33)</span> flashkicker</div></div></div><div id="comment-tools-6151" class="comment-tools"></div><div class="clear"></div><div id="comment-6151-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

