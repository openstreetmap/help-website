+++
type = "question"
title = "Howto Add Arbitrary Items to the Tree Structure in Dissector?"
description = '''I would like to add the following nodes to the tree structure in Wireshark in my dissectors code:  Node1 Node2 Node3 Node4 Node5 Node6   I know this would be accomplished through the dissect proto function, but I cannot figure out how to add nodes and set the text arbitrarily (totally independent of...'''
date = "2011-07-25T05:45:00Z"
lastmod = "2011-07-25T06:40:00Z"
weight = 5212
keywords = [ "node", "xml", "tree", "dll" ]
aliases = [ "/questions/5212" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Howto Add Arbitrary Items to the Tree Structure in Dissector?](/questions/5212/howto-add-arbitrary-items-to-the-tree-structure-in-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5212-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to add the following nodes to the tree structure in Wireshark in my dissectors code:</p><ul><li>Node1</li><li>Node2</li><ul><li>Node3</li><li>Node4</li><ul><li>Node5</li></ul></ul><li>Node6</li></ul><p>I know this would be accomplished through the dissect proto function, but I cannot figure out how to add nodes and set the text arbitrarily (totally independent of the data getting handed into my dissector).</p><p>I realize this is not quite how this is supposed to be used, but due to the nature of what I am doing, the actual conversion function (raw data to XML) is already done inside a DLL file. It works, we use it for other things, and I don't really want to attempt to incorporate that mess into my dissector. I wrote a C XML parser already since the DLL outputs an XML c string, so all i want to do at this point is take that XML file (which is inherently a tree structure already) and display it in wireshark.</p><p>If you could provide a small example to add the tree structure I gave above that would be amazing.</p><p>Thank you for your time, Brandon</p></div><div id="question-tags" class="tags-container tags">node xml tree dll</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jul '11, 05:45</strong></p><img src="https://secure.gravatar.com/avatar/b65eb296474b8a4c664c8f7bc0ba2234?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="officialhopsof&#39;s gravatar image" /><p>officialhopsof<br />
<span class="score" title="31 reputation points">31</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="officialhopsof has 2 accepted answers">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Jul '11, 05:48</p></div></div><div id="comments-container-5212" class="comments-container"></div><div id="comment-tools-5212" class="comment-tools"></div><div class="clear"></div><div id="comment-5212-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5218"></span>

<div id="answer-container-5218" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5218-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The function <code>proto_tree_add_text</code> is what you are looking for. You could probably do what you need something like this:</p><pre><code>//create a tvb over your xml string data
tvbuff_t *xmltvb = tvb_new_real_data(xml_data_as_string, number_xml_characters, number_xml_characters);
...
//add a text item to your tree
xml_tree_item = proto_tree_add_text(parent_tree_node, xmltvb, start_index, length, &quot;%*s&quot;, length, xml_data_as_string);</code></pre><p>You may even be able to skip creating a new <code>tvbuff_t</code> if your data is already present in the <code>tvb</code> you are dissecting.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jul '11, 06:40</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-5218" class="comments-container"><span id="5222"></span><div id="comment-5222" class="comment"><div id="post-5222-score" class="comment-score"></div><div class="comment-text"><p>multipleinterfaces: that is exactly what I needed, thanks!</p></div><div id="comment-5222-info" class="comment-info"><span class="comment-age">(25 Jul '11, 08:06)</span> officialhopsof</div></div></div><div id="comment-tools-5218" class="comment-tools"></div><div class="clear"></div><div id="comment-5218-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5217"></span>

<div id="answer-container-5217" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5217-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You add a subtree by using <code>proto_item_add_subtree()</code> that gets you a new tree that you can then add items to in a similar way to the tree originally handed in to your dissector.</p><p>See README.developer in the doc directory of the source.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jul '11, 06:28</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-5217" class="comments-container"></div><div id="comment-tools-5217" class="comment-tools"></div><div class="clear"></div><div id="comment-5217-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

