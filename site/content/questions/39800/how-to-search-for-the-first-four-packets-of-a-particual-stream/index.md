+++
type = "question"
title = "How to search for the first four packets of a particual stream"
description = '''Hi guys, I have an issue where randomly I see the following flow:  - SYN  - SYN+ ACK  - RST+ACK  - ACK I want to know how is possible to find in a capture just those four packets, in other words, I want a filter that scan the first with a SYN flag, then search the second packet for a SYN+ACK, then t...'''
date = "2015-02-11T08:39:00Z"
lastmod = "2015-02-11T14:12:00Z"
weight = 39800
keywords = [ "filter", "packet" ]
aliases = [ "/questions/39800" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to search for the first four packets of a particual stream](/questions/39800/how-to-search-for-the-first-four-packets-of-a-particual-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39800-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys, I have an issue where randomly I see the following flow: - SYN - SYN+ ACK - RST+ACK - ACK</p><p>I want to know how is possible to find in a capture just those four packets, in other words, I want a filter that scan the first with a SYN flag, then search the second packet for a SYN+ACK, then the third packet for a RST+ACK and finally the fourth packet should be an ACK</p></div><div id="question-tags" class="tags-container tags">filter packet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '15, 08:39</strong></p><img src="https://secure.gravatar.com/avatar/6dbb44bb9791e51f8acb17390326ad5f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ventiz&#39;s gravatar image" /><p>ventiz<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ventiz has no accepted answers">0%</span></p></div></div><div id="comments-container-39800" class="comments-container"><span id="39813"></span><div id="comment-39813" class="comment"><div id="post-39813-score" class="comment-score"></div><div class="comment-text"><p>Jasper and Kurt thank you for your tips they really help me to find very fast the stream of the packets I was looking for, it's sad that wireshark can find yet packet dependencies but definitely would be a great feature. Thx again</p></div><div id="comment-39813-info" class="comment-info"><span class="comment-age">(11 Feb '15, 14:22)</span> ventiz</div></div></div><div id="comment-tools-39800" class="comment-tools"></div><div class="clear"></div><div id="comment-39800-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="39801"></span>

<div id="answer-container-39801" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39801-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's not really possible to filter on packet dependencies with Wireshark. But what I get from your problem description you're basically looking for a connection reset after the three way handshake is almost complete. For that it should be possible to look for reset flags where the relative sequence number is 1 (0 would be the SYN, so the next packet following it must have sequence number of 1)</p><p>Maybe that's good enough?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '15, 08:54</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-39801" class="comments-container"><span id="39840"></span><div id="comment-39840" class="comment"><div id="post-39840-score" class="comment-score"></div><div class="comment-text"><p>Thank you Jasper and Kurt, it's sad that cannot filter via dependencies but would be great to have that feature</p></div><div id="comment-39840-info" class="comment-info"><span class="comment-age">(12 Feb '15, 13:10)</span> ventiz</div></div></div><div id="comment-tools-39801" class="comment-tools"></div><div class="clear"></div><div id="comment-39801-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39809"></span>

<div id="answer-container-39809" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39809-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This sounds similar to the following question:</p><blockquote><p><a href="https://ask.wireshark.org/questions/10640/how-to-find-syn-not-followed-by-a-synack">https://ask.wireshark.org/questions/10640/how-to-find-syn-not-followed-by-a-synack</a></p></blockquote><p>I'll update my answer to this:</p><ul><li>set a display filter for RST+ACK</li><li>then: Statistics -&gt; Conversations</li><li>Select the option "Limit to display filter" (at the bottom)</li><li>Select the tab TCP</li><li>Sort the output by "Packets".</li></ul><p>Those connections with 3-4 packet are likely the connections you are looking for.</p><ul><li>Select one of them and then "Follow Stream".</li><li>Repeat that method for all stream you want to check.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '15, 14:12</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-39809" class="comments-container"></div><div id="comment-tools-39809" class="comment-tools"></div><div class="clear"></div><div id="comment-39809-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

