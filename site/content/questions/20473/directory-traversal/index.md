+++
type = "question"
title = "Directory Traversal"
description = '''hello how can I Find a host in a trace file that appears to be attempting Directory Traversal attack and get its IP address? tnx'''
date = "2013-04-16T09:02:00Z"
lastmod = "2013-04-16T13:52:00Z"
weight = 20473
keywords = [ "attack" ]
aliases = [ "/questions/20473" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Directory Traversal](/questions/20473/directory-traversal)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20473-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello how can I Find a host in a trace file that appears to be attempting Directory Traversal attack and get its IP address? tnx</p></div><div id="question-tags" class="tags-container tags">attack</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '13, 09:02</strong></p><img src="https://secure.gravatar.com/avatar/ecf971e045fa71b02ef5e460cd0b518a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="parna&#39;s gravatar image" /><p>parna<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="parna has no accepted answers">0%</span></p></div></div><div id="comments-container-20473" class="comments-container"></div><div id="comment-tools-20473" class="comment-tools"></div><div class="clear"></div><div id="comment-20473-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20478"></span>

<div id="answer-container-20478" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20478-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I would start with this display filter:</p><blockquote><p><code>http contains "../.."</code><br />
</p></blockquote><p>Then look at the source IP address column.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '13, 13:52</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-20478" class="comments-container"></div><div id="comment-tools-20478" class="comment-tools"></div><div class="clear"></div><div id="comment-20478-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

