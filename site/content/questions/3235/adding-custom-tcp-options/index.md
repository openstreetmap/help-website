+++
type = "question"
title = "Adding custom TCP options"
description = '''How can I add labels for custom (unknown) TCP options?'''
date = "2011-03-30T13:03:00Z"
lastmod = "2011-03-30T23:17:00Z"
weight = 3235
keywords = [ "unknown", "options", "tcp", "custom" ]
aliases = [ "/questions/3235" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Adding custom TCP options](/questions/3235/adding-custom-tcp-options)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3235-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I add labels for custom (unknown) TCP options?</p></div><div id="question-tags" class="tags-container tags">unknown options tcp custom</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Mar '11, 13:03</strong></p><img src="https://secure.gravatar.com/avatar/f8df78a80d6737fcee51202492aaa236?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Demetris&#39;s gravatar image" /><p>Demetris<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Demetris has no accepted answers">0%</span></p></div></div><div id="comments-container-3235" class="comments-container"></div><div id="comment-tools-3235" class="comment-tools"></div><div class="clear"></div><div id="comment-3235-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3241"></span>

<div id="answer-container-3241" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3241-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You'll have to code it yourself, adding to the TCP dissector and compile it. Start by adding to <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/dissectors/packet-tcp.c?revision=36338&amp;view=markup#l3193">this options array</a> and work your way out. Look at the others for examples, it's fairly easy.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '11, 23:17</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-3241" class="comments-container"></div><div id="comment-tools-3241" class="comment-tools"></div><div class="clear"></div><div id="comment-3241-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

