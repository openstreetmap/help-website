+++
type = "question"
title = "proto_tree_add_text() flagged by checkAPIs tool as &quot;useless&quot;"
description = '''Trying to submit Control Techniques packet-ecmp.c dissector as a built-in. Wireshark team requested that I run the checkAPIs tool on the source file. It gave this result. $ checkAPIs.pl packet-ecmp.c packet-ecmp.c: found 324 useless add_text() vs. 119 add_&amp;lt;something else=&quot;&quot;&amp;gt;() calls (272.27%) ...'''
date = "2014-09-26T07:41:00Z"
lastmod = "2014-09-26T08:48:00Z"
weight = 36636
keywords = [ "proto_tree_add_text" ]
aliases = [ "/questions/36636" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [proto\_tree\_add\_text() flagged by checkAPIs tool as "useless"](/questions/36636/proto_tree_add_text-flagged-by-checkapis-tool-as-useless)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36636-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Trying to submit Control Techniques <strong>packet-ecmp.c</strong> dissector as a built-in. Wireshark team requested that I run the checkAPIs tool on the source file. It gave this result.</p><p><em>$ checkAPIs.pl packet-ecmp.c packet-ecmp.c: found 324 useless add_text() vs. 119 add_&lt;something else=""&gt;() calls (272.27%) $</em></p><p>Checked this with the Visual C++ editor and essentially all the flagged lines are references to proto_tree_add_text(...) source lines. Latest copy of README.dissector shows this proto_tree_add_text() function as legal and acceptable.</p><p><em>There are several functions that the programmer can use to add either protocol or field labels to the proto_tree: proto_item</em> proto_tree_add_item(tree, id, tvb, start, length, encoding); proto_item <em>proto_tree_add_text(tree, tvb, start, length, format, ...);</em></p><p>OK, what gives?</p></div><div id="question-tags" class="tags-container tags">proto_tree_add_text</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '14, 07:41</strong></p><img src="https://secure.gravatar.com/avatar/de90678c642298d64da5485408107dac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lynchzilla&#39;s gravatar image" /><p>lynchzilla<br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lynchzilla has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Sep '14, 08:47</p></div></div><div id="comments-container-36636" class="comments-container"></div><div id="comment-tools-36636" class="comment-tools"></div><div class="clear"></div><div id="comment-36636-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36637"></span>

<div id="answer-container-36637" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36637-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>proto_tree_add_text() has long been on the list of APIs to avoid and we've been slowly replacing most calls to it with better APIs (ones which make the field filterable). As README.dissector says (in master-1.12):</p><pre><code>This can (and should only) be used for items with subtrees, which may not
have values themselves - the items in the subtree are the ones with values.
In other words, if you&#39;re using proto_tree_add_text() and not using the
return value to build a new tree, you probably shouldn&#39;t be using this
function: you probably should be using proto_tree_add_item() instead.</code></pre><p>The current README.dissector (in master) doesn't even mention proto_tree_add_text() any more. (Keep in mind that new dissectors are submitted against master, not one of the release branches.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '14, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-36637" class="comments-container"></div><div id="comment-tools-36637" class="comment-tools"></div><div class="clear"></div><div id="comment-36637-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

