+++
type = "question"
title = "Tshark and Dissector are in the same project when compiling?"
description = '''Hi all, I&#x27;m using both of tshark.c and dissector &quot;packet-camel.c&quot;. i wonder when gcc compiles tshark and Dissector, does it consider them as in the same project? Because when I try to use an extern variable for both of these files, the variable in different files are different. i think that the tsha...'''
date = "2013-10-02T02:02:00Z"
lastmod = "2013-10-02T02:38:00Z"
weight = 25496
keywords = [ "extern", "packet-camel", "tshark" ]
aliases = [ "/questions/25496" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Tshark and Dissector are in the same project when compiling?](/questions/25496/tshark-and-dissector-are-in-the-same-project-when-compiling)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25496-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I'm using both of <strong>tshark.c</strong> and dissector "<strong>packet-camel.c</strong>". i wonder when gcc compiles tshark and Dissector, does it consider them as in the same project? Because when I try to use an extern variable for both of these files, the variable in different files are different. i think that the <strong>tshark.c</strong> call dissector to do something so that it doesn't make sense if an extern variable in tshark.c has different value when it is called in dissector "<strong>packet-camel.c</strong>". Thanks for your help.</p></div><div id="question-tags" class="tags-container tags">extern packet-camel tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Oct '13, 02:02</strong></p><img src="https://secure.gravatar.com/avatar/824a7342f59ff90e6040505b38626416?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hoangsonk49&#39;s gravatar image" /><p>hoangsonk49<br />
<span class="score" title="81 reputation points">81</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hoangsonk49 has 2 accepted answers">28%</span></p></div></div><div id="comments-container-25496" class="comments-container"></div><div id="comment-tools-25496" class="comment-tools"></div><div class="clear"></div><div id="comment-25496-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25498"></span>

<div id="answer-container-25498" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25498-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>tshark.c is compiled as part of tshark, packet-camel.c is compiled as part of libwireshark which is linked to by tshark.</p><p>The variable will have to be declared and exported from one part and then extern'd from the other part. I would suggest that it would be best to be declared and exported from libwireshark and then extern'd in tshark as tshark has a dependency on libwireshark and not the other way around.</p><p>Note that to export symbols in a cross platform manner some hoops have to be jumped through, look at <code>ws_export_symbol.h</code> in the top level directory and the use of <code>WS_DLL_PUBLIC</code> elsewhere in the source code.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Oct '13, 02:38</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Oct '13, 03:27</p></div></div><div id="comments-container-25498" class="comments-container"><span id="25500"></span><div id="comment-25500" class="comment"><div id="post-25500-score" class="comment-score"></div><div class="comment-text"><p>Problem solved. Thanks for your idea, grahamb :-)</p></div><div id="comment-25500-info" class="comment-info"><span class="comment-age">(02 Oct '13, 02:49)</span> hoangsonk49</div></div><span id="25502"></span><div id="comment-25502" class="comment"><div id="post-25502-score" class="comment-score"></div><div class="comment-text"><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions</p></div><div id="comment-25502-info" class="comment-info"><span class="comment-age">(02 Oct '13, 04:41)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-25498" class="comment-tools"></div><div class="clear"></div><div id="comment-25498-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

