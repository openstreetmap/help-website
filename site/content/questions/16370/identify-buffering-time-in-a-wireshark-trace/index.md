+++
type = "question"
title = "Identify buffering time in a wireshark trace"
description = '''Hi All, I&#x27;m trying to use wireshark to check the buffering time for a youtube video. I was thinking that, the buffering time started from GET /watch?v=LNMWgmvdLws HTTP/1.1 but i cannot identify which message said the video start to play. I need help for that. Thanks in advance! BR'''
date = "2012-11-28T01:18:00Z"
lastmod = "2012-11-28T04:52:00Z"
weight = 16370
keywords = [ "analysis" ]
aliases = [ "/questions/16370" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Identify buffering time in a wireshark trace](/questions/16370/identify-buffering-time-in-a-wireshark-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16370-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I'm trying to use wireshark to check the buffering time for a youtube video. I was thinking that, the buffering time started from GET /watch?v=LNMWgmvdLws HTTP/1.1 but i cannot identify which message said the video start to play.</p><p>I need help for that. Thanks in advance!</p><p>BR</p></div><div id="question-tags" class="tags-container tags">analysis</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Nov '12, 01:18</strong></p><img src="https://secure.gravatar.com/avatar/e7aaa72d8005167a078f7736c39cf729?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Djo&#39;s gravatar image" /><p>Djo<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Djo has no accepted answers">0%</span></p></div></div><div id="comments-container-16370" class="comments-container"></div><div id="comment-tools-16370" class="comment-tools"></div><div class="clear"></div><div id="comment-16370-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="16372"></span>

<div id="answer-container-16372" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16372-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You won't be able to find that info in the network trace, as the buffering will be done by the YouTube app once the data comes in. It will then use a specific buffering time to make sure a constant video stream can be shown, even when there is a little jittering or packet-loss (resulting in retransmissions). How YouTube decides what time to use for the buffering, I don't know.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Nov '12, 02:18</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-16372" class="comments-container"></div><div id="comment-tools-16372" class="comment-tools"></div><div class="clear"></div><div id="comment-16372-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="16379"></span>

<div id="answer-container-16379" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16379-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>As @SYN-bit said, there is no good way to find that in the protocol, as it's one data stream. However, I asked myself, if there might be some pattern in the packet flow, that correspond with the buffer time and I believe I have found a <strong>weak</strong> relationship.</p><p>I started your video two times and measured the time it took to buffer (start the video) with a stop watch. Then I looked a the IO Stats for those connections and found this.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/youtube1_small.png" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/youtube3_small.png" alt="alt text" /></p><p>To me it looks like the player first (almost totally) fills to buffer and then it starts to play. The time where the packet rate drops (you can only see it in 0.01s resolution), matches <strong>more or less</strong> the time I measured with a stop watch. So, the start of the first large gap in the IO graph is more or less where the video starts to play.</p><p>As I don't know how the player works internally, I can only call this a <strong>weak</strong> sign for the initial buffer time, but that pattern repeats in all tests (so far).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Nov '12, 04:52</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 28 Nov '12, 04:59</p></div></div><div id="comments-container-16379" class="comments-container"><span id="16383"></span><div id="comment-16383" class="comment"><div id="post-16383-score" class="comment-score">1</div><div class="comment-text"><p>Nice one, Kurt!</p><p>(BTW, where do you find the time :-))</p></div><div id="comment-16383-info" class="comment-info"><span class="comment-age">(28 Nov '12, 05:38)</span> SYN-bit ♦♦</div></div><span id="16387"></span><div id="comment-16387" class="comment"><div id="post-16387-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Nice one, Kurt!</p></blockquote><p>thanks.</p><blockquote><p>(BTW, where do you find the time :-))</p></blockquote><p>I sleep only 2 hours per day ;-)) And for interesting problems, I always find some time :-)</p></div><div id="comment-16387-info" class="comment-info"><span class="comment-age">(28 Nov '12, 06:49)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-16379" class="comment-tools"></div><div class="clear"></div><div id="comment-16379-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

