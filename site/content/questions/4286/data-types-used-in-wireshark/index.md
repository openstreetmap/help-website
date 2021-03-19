+++
type = "question"
title = "data types used in wireshark."
description = '''where do i get to know abt the data types used in the wireshark development, like tvbuff, m getting confused with the unknown types, please help me. '''
date = "2011-05-30T05:29:00Z"
lastmod = "2011-05-30T06:50:00Z"
weight = 4286
keywords = [ "datatypes" ]
aliases = [ "/questions/4286" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [data types used in wireshark.](/questions/4286/data-types-used-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4286-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>where do i get to know abt the <em>data types</em> used in the wireshark development, like tvbuff, m getting confused with the unknown types, please help me.</p></div><div id="question-tags" class="tags-container tags">datatypes</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 May '11, 05:29</strong></p><img src="https://secure.gravatar.com/avatar/257c9f9e498193d7ddde57090efe094a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sagu072&#39;s gravatar image" /><p>sagu072<br />
<span class="score" title="35 reputation points">35</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sagu072 has no accepted answers">0%</span></p></div></div><div id="comments-container-4286" class="comments-container"></div><div id="comment-tools-4286" class="comment-tools"></div><div class="clear"></div><div id="comment-4286-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4287"></span>

<div id="answer-container-4287" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4287-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>When writing dissectors, most of the Wireshark internal structures, like tvbuff's, should be treated as opaque data types, so you really don't need to know or care about the internals, as the API provides all the accessor functions you need. However, if you want to learn about the internals anyway, then the <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/tvbuff-int.h?revision=37422&amp;view=markup">epan/tvbuff-int.h</a> file is probably the best place to look.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 May '11, 06:50</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-4287" class="comments-container"></div><div id="comment-tools-4287" class="comment-tools"></div><div class="clear"></div><div id="comment-4287-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

