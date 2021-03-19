+++
type = "question"
title = "How to filter packets by specific application in wireshark?"
description = '''I have captured the data/packets from a network now i don&#x27;t have an idea to filter this data by android application i.e. skype, instagram, soundcloud. please anyone tell me.'''
date = "2017-04-24T03:56:00Z"
lastmod = "2017-04-24T04:20:00Z"
weight = 61001
keywords = [ "packets" ]
aliases = [ "/questions/61001" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to filter packets by specific application in wireshark?](/questions/61001/how-to-filter-packets-by-specific-application-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61001-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have captured the data/packets from a network now i don't have an idea to filter this data by android application i.e. skype, instagram, soundcloud. please anyone tell me.</p></div><div id="question-tags" class="tags-container tags">packets</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Apr '17, 03:56</strong></p><img src="https://secure.gravatar.com/avatar/7140bad1442c62e2aeb2dfc2399e0c44?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Muhammad%20Juniad&#39;s gravatar image" /><p>Muhammad Juniad<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Muhammad Juniad has no accepted answers">0%</span></p></div></div><div id="comments-container-61001" class="comments-container"></div><div id="comment-tools-61001" class="comment-tools"></div><div class="clear"></div><div id="comment-61001-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61003"></span>

<div id="answer-container-61003" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61003-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is no direct method to do so as the sending application is not captured along with the traffic. Most applications do have a "signature" to their traffic e.g. by port use or specific data in each packet, and Wireshark uses this to perform dissection of the respective traffic.</p><p>However, it's likely that the traffic for the applications you have listed will be encrypted and as such it's very difficult to determine what application sent any specific encrypted packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Apr '17, 04:20</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-61003" class="comments-container"></div><div id="comment-tools-61003" class="comment-tools"></div><div class="clear"></div><div id="comment-61003-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

