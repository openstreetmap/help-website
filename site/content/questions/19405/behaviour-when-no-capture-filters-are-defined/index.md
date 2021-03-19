+++
type = "question"
title = "Behaviour when no capture filters are defined."
description = '''Question: If I delete all Capture Filters from Wireshark and then start a Capture session, will Wireshark log all network interactions or none at all? Thanks'''
date = "2013-03-12T13:22:00Z"
lastmod = "2013-03-12T13:40:00Z"
weight = 19405
keywords = [ "capture-filter" ]
aliases = [ "/questions/19405" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Behaviour when no capture filters are defined.](/questions/19405/behaviour-when-no-capture-filters-are-defined)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19405-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Question: If I delete all Capture Filters from Wireshark and then start a Capture session, will Wireshark log all network interactions or none at all?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Mar '13, 13:22</strong></p><img src="https://secure.gravatar.com/avatar/8ab4fd06f562c76bc0da96bbe4dc0c0a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John%20Goldorak&#39;s gravatar image" /><p>John Goldorak<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John Goldorak has no accepted answers">0%</span></p></div></div><div id="comments-container-19405" class="comments-container"></div><div id="comment-tools-19405" class="comment-tools"></div><div class="clear"></div><div id="comment-19405-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19406"></span>

<div id="answer-container-19406" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19406-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It will capture everything. Filters mean "leave something out", so if there's no filter, Wireshark will capture it all.</p><p>Hint: why ask when you can just try? Run Wireshark, start a capture without a filter, check out what the result is. Easy.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '13, 13:40</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-19406" class="comments-container"><span id="19408"></span><div id="comment-19408" class="comment"><div id="post-19408-score" class="comment-score"></div><div class="comment-text"><p>How would you know it captured everything? You can't see missing packets :-)</p></div><div id="comment-19408-info" class="comment-info"><span class="comment-age">(12 Mar '13, 16:17)</span> grahamb ♦</div></div><span id="19409"></span><div id="comment-19409" class="comment"><div id="post-19409-score" class="comment-score"></div><div class="comment-text"><p>at least you could see the drop count and know that it didn't ;-)</p><p>Drops at SPAN port etc. are another story though...</p></div><div id="comment-19409-info" class="comment-info"><span class="comment-age">(12 Mar '13, 16:26)</span> Jasper ♦♦</div></div><span id="19454"></span><div id="comment-19454" class="comment"><div id="post-19454-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper. That's what I thought. I did try it and notice the same behaviour but I wasn't sure if something (not immediately apparent) would be left out.</p><p>I appreciate the time that you took to answer my question. Thank you.</p></div><div id="comment-19454-info" class="comment-info"><span class="comment-age">(13 Mar '13, 07:56)</span> John Goldorak</div></div><span id="19455"></span><div id="comment-19455" class="comment"><div id="post-19455-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-19455-info" class="comment-info"><span class="comment-age">(13 Mar '13, 08:00)</span> grahamb ♦</div></div><span id="19457"></span><div id="comment-19457" class="comment"><div id="post-19457-score" class="comment-score"></div><div class="comment-text"><p>@John Goldorak: sure, no problem - in that case verification makes sense. Keep asking and we'll try to help :-)</p></div><div id="comment-19457-info" class="comment-info"><span class="comment-age">(13 Mar '13, 08:29)</span> Jasper ♦♦</div></div></div><div id="comment-tools-19406" class="comment-tools"></div><div class="clear"></div><div id="comment-19406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

