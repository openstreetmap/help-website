+++
type = "question"
title = "custom dissector loop tree till packet data end"
description = '''Hi, I have a 3 parent trees  tree1  sub-tree of tree1   tree 2   sub-tree of tree2  tree 3  sub-tree of tree3  Now after processing my packet data of 1 frame , still i hae remaining data to be processed and which i have to call tree 1 again. How do i do this? I have implemented tree1 a function tree...'''
date = "2014-07-15T19:40:00Z"
lastmod = "2014-07-15T19:40:00Z"
weight = 34697
keywords = [ "tree", "loopback" ]
aliases = [ "/questions/34697" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [custom dissector loop tree till packet data end](/questions/34697/custom-dissector-loop-tree-till-packet-data-end)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34697-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a 3 parent trees</p><pre><code>                     tree1
                          sub-tree of tree1 
                     tree 2 
                          sub-tree of tree2
                     tree 3
                          sub-tree of tree3</code></pre><p>Now after processing my packet data of 1 frame , still i hae remaining data to be processed and which i have to call tree 1 again.</p><p>How do i do this? I have implemented tree1 a function tree 2 as a seperate function and tree3 as a seperate function.</p><p>how do i loop back whithout tvb offset. Is it possible for a function to return TVB and offset and length.</p><p>please suggest! Thanks in advance!</p></div><div id="question-tags" class="tags-container tags">tree loopback</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '14, 19:40</strong></p><img src="https://secure.gravatar.com/avatar/1339589a92af9455063c09e56bfc6299?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="umar&#39;s gravatar image" /><p>umar<br />
<span class="score" title="26 reputation points">26</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="umar has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Jul '14, 19:41</p></div></div><div id="comments-container-34697" class="comments-container"></div><div id="comment-tools-34697" class="comment-tools"></div><div class="clear"></div><div id="comment-34697-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

