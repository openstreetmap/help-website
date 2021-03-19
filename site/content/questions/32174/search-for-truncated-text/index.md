+++
type = "question"
title = "search for truncated text"
description = '''OK, sometimes when I search for packets which contain text data I find that the text data is truncated. How do I set the filter to find only truncated text data (if it is possible)?  I tried something like this:  data-text-lines contains &quot;truncated&quot; , but didn&#x27;t get any result.'''
date = "2014-04-25T05:33:00Z"
lastmod = "2014-04-26T11:30:00Z"
weight = 32174
keywords = [ "truncated" ]
aliases = [ "/questions/32174" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [search for truncated text](/questions/32174/search-for-truncated-text)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32174-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>OK, sometimes when I search for packets which contain text data I find that the text data is truncated. How do I set the filter to find only truncated text data (if it is possible)? I tried something like this: data-text-lines contains "truncated" , but didn't get any result.</p></div><div id="question-tags" class="tags-container tags">truncated</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Apr '14, 05:33</strong></p><img src="https://secure.gravatar.com/avatar/412b10652e55b9c4d3cc5243b7b58d0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="myrddin&#39;s gravatar image" /><p>myrddin<br />
<span class="score" title="11 reputation points">11</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="myrddin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Apr '14, 05:33</p></div></div><div id="comments-container-32174" class="comments-container"></div><div id="comment-tools-32174" class="comment-tools"></div><div class="clear"></div><div id="comment-32174-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32192"></span>

<div id="answer-container-32192" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32192-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>How do I set the filter to find only truncated text data (if it is possible)?</p></blockquote><p>You can't because "truncated" only has a meaning in the human brain, as you can detect that something in a text is probably missing. There is no way to do that with Wireshark, and it's a pretty hard AI problem (artificial intelligence) to detect such a thing in general.</p><p>But maybe I misunderstand your definition of "truncated data". If so, please add more details or even better a sample capture file with truncated data/text and one without.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Apr '14, 11:30</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-32192" class="comments-container"><span id="32223"></span><div id="comment-32223" class="comment"><div id="post-32223-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer. Yes I think you understood well, I just wanted to search all Line-based text data fields (data-text-lines) of captured packets and to filter only those that have [truncated] in them (in front of some text). Something like [truncated] some text</p><p>OK it doesn't matter, I asked this more out of curiosity as I tried to filter them out, but couldn't. Thanks again, bye</p></div><div id="comment-32223-info" class="comment-info"><span class="comment-age">(27 Apr '14, 12:58)</span> myrddin</div></div><span id="32224"></span><div id="comment-32224" class="comment"><div id="post-32224-score" class="comment-score"></div><div class="comment-text"><p>wait a moment... Is <strong>[truncated]</strong> a text pattern in your data, or something you see in the Wireshark GUI (which does exist in some situations)?</p><p>Example: if a HTTP request is too long, it will be shown as</p><blockquote><p>[truncated] GET /some_very_very_very_very_very_very_very_very_</p></blockquote><p>If it's that you are asking for, the answer to your question is: You cannot filter for those '[truncated]' messages, as that's just a marker in the GUI to tell the user that there was a very long string that did not fit into some internal buffer.</p><p>That's nothing you need to be worried about. It's just a limitation in displaying data in some situations. Nothing in the frame itself will be truncated in any way.</p></div><div id="comment-32224-info" class="comment-info"><span class="comment-age">(27 Apr '14, 13:08)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-32192" class="comment-tools"></div><div class="clear"></div><div id="comment-32192-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

