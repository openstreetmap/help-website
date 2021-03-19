+++
type = "question"
title = "tcp options"
description = '''I was wondering if there is some way to do this. 1. to decode the options part of tcp protocol or say dissect the options part of the tcp header. 2. once i decode the options part, get wireshark to do the rest of decoding as usual.'''
date = "2011-03-23T03:15:00Z"
lastmod = "2011-03-27T14:36:00Z"
weight = 3039
keywords = [ "tcp-options", "wireshark" ]
aliases = [ "/questions/3039" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tcp options](/questions/3039/tcp-options)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3039-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was wondering if there is some way to do this. 1. to decode the options part of tcp protocol or say dissect the options part of the tcp header. 2. once i decode the options part, get wireshark to do the rest of decoding as usual.</p></div><div id="question-tags" class="tags-container tags">tcp-options wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Mar '11, 03:15</strong></p><img src="https://secure.gravatar.com/avatar/46023e482c60329a251a137848f8f5f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="niks3089&#39;s gravatar image" /><p>niks3089<br />
<span class="score" title="21 reputation points">21</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="niks3089 has no accepted answers">0%</span></p></div></div><div id="comments-container-3039" class="comments-container"><span id="3052"></span><div id="comment-3052" class="comment"><div id="post-3052-score" class="comment-score">1</div><div class="comment-text"><p>I'm confused about the question - doesn't Wireshark do this by default? What are you looking for that you aren't seeing?</p></div><div id="comment-3052-info" class="comment-info"><span class="comment-age">(23 Mar '11, 12:54)</span> GeonJay</div></div><span id="3152"></span><div id="comment-3152" class="comment"><div id="post-3152-score" class="comment-score"></div><div class="comment-text"><p>There are certain options that wireshark shows as unknown. These contain some important info which my company has requested to dissect</p></div><div id="comment-3152-info" class="comment-info"><span class="comment-age">(27 Mar '11, 06:12)</span> niks3089</div></div><span id="3194"></span><div id="comment-3194" class="comment"><div id="post-3194-score" class="comment-score"></div><div class="comment-text"><p>RFC says to ignore TCP options if the the receiver doesn't know what it is. So many WAN accelerators use TCP options field to mark it as an "accelerator aware" packets.</p></div><div id="comment-3194-info" class="comment-info"><span class="comment-age">(28 Mar '11, 18:51)</span> hansangb</div></div></div><div id="comment-tools-3039" class="comment-tools"></div><div class="clear"></div><div id="comment-3039-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3163"></span>

<div id="answer-container-3163" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3163-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>See the answers to <a href="http://ask.wireshark.org/questions/3153/tcp-options-dissection">the other place where you asked the question</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '11, 14:36</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-3163" class="comments-container"></div><div id="comment-tools-3163" class="comment-tools"></div><div class="clear"></div><div id="comment-3163-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

