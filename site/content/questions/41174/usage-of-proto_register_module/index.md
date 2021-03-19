+++
type = "question"
title = "usage of proto_register_module"
description = '''I wanted to know the cases where I can use pref_register_module function can be used while writing a new dissector.'''
date = "2015-04-03T00:00:00Z"
lastmod = "2015-04-03T02:59:00Z"
weight = 41174
keywords = [ "definition" ]
aliases = [ "/questions/41174" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [usage of proto\_register\_module](/questions/41174/usage-of-proto_register_module)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41174-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I wanted to know the cases where I can use pref_register_module function can be used while writing a new dissector.</p></div><div id="question-tags" class="tags-container tags">definition</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Apr '15, 00:00</strong></p><img src="https://secure.gravatar.com/avatar/4175e12d54c0b11b1d8a5fb592555a63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lucky15&#39;s gravatar image" /><p>lucky15<br />
<span class="score" title="6 reputation points">6</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lucky15 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Apr '15, 02:07</p></div></div><div id="comments-container-41174" class="comments-container"><span id="41175"></span><div id="comment-41175" class="comment"><div id="post-41175-score" class="comment-score"></div><div class="comment-text"><p>Each post should have a clear, specific question in the title field. Please rephrase the title as a proper question.</p></div><div id="comment-41175-info" class="comment-info"><span class="comment-age">(03 Apr '15, 01:30)</span> Jaap ♦</div></div></div><div id="comment-tools-41174" class="comment-tools"></div><div class="clear"></div><div id="comment-41174-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41177"></span>

<div id="answer-container-41177" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41177-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at the documentation in the source code, in this case <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=doc/README.dissector">README.dissector</a> section 2.6, and existing dissectors are always a source of information.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Apr '15, 02:59</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-41177" class="comments-container"><span id="41281"></span><div id="comment-41281" class="comment"><div id="post-41281-score" class="comment-score"></div><div class="comment-text"><p>thank you for your suggestion.</p></div><div id="comment-41281-info" class="comment-info"><span class="comment-age">(08 Apr '15, 06:13)</span> lucky15</div></div></div><div id="comment-tools-41177" class="comment-tools"></div><div class="clear"></div><div id="comment-41177-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

