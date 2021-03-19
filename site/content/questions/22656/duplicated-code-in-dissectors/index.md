+++
type = "question"
title = "Duplicated code in dissectors"
description = '''Hi. I have two custom dissectors that i have written. The two protocols i dissect have fields that are very similar to eachother. The headers are different and some other things, but 1 quite large part of the protocol is identical. In my code i have a quite big while-loop that extracts data and adds...'''
date = "2013-07-04T07:34:00Z"
lastmod = "2013-07-04T08:00:00Z"
weight = 22656
keywords = [ "dissector" ]
aliases = [ "/questions/22656" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Duplicated code in dissectors](/questions/22656/duplicated-code-in-dissectors)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22656-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. I have two custom dissectors that i have written. The two protocols i dissect have fields that are very similar to eachother. The headers are different and some other things, but 1 quite large part of the protocol is identical. In my code i have a quite big while-loop that extracts data and adds it to the proto tree, and this loop is identical in both dissectors.</p><p>Is there an easy way to avoid this duplicated code when writing dissectors?</p><p>/Kit</p></div><div id="question-tags" class="tags-container tags">dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jul '13, 07:34</strong></p><img src="https://secure.gravatar.com/avatar/b93cb303b8ca7bc14188730687491169?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kitg&#39;s gravatar image" /><p>Kitg<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kitg has no accepted answers">0%</span></p></div></div><div id="comments-container-22656" class="comments-container"></div><div id="comment-tools-22656" class="comment-tools"></div><div class="clear"></div><div id="comment-22656-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22657"></span>

<div id="answer-container-22657" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22657-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>In one dissector extract the loop into its own function, parametrise accordingly, and declare the function in a header file for that dissector. In the other dissector, include the header file from the first one and call the function with the appropriate parameters.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jul '13, 08:00</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-22657" class="comments-container"><span id="22659"></span><div id="comment-22659" class="comment"><div id="post-22659-score" class="comment-score"></div><div class="comment-text"><p>Thanks alot, will do that.</p></div><div id="comment-22659-info" class="comment-info"><span class="comment-age">(04 Jul '13, 08:06)</span> Kitg</div></div></div><div id="comment-tools-22657" class="comment-tools"></div><div class="clear"></div><div id="comment-22657-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

