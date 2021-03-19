+++
type = "question"
title = "Is there a way to only show streams?"
description = '''By default, Wireshark shows the entire packet breakdown in the order that it captured the packets split across three frames. Pretty much the only thing I ever do with Wireshark is reverse engineer captured HTTP requests. This basically amounts to Wireshark&#x27;s default UI getting in the way of seeing t...'''
date = "2013-05-31T08:14:00Z"
lastmod = "2013-05-31T08:19:00Z"
weight = 21666
keywords = [ "follow.tcp.stream" ]
aliases = [ "/questions/21666" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Is there a way to only show streams?](/questions/21666/is-there-a-way-to-only-show-streams)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21666-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>By default, Wireshark shows the entire packet breakdown in the order that it captured the packets split across three frames. Pretty much the only thing I ever do with Wireshark is reverse engineer captured HTTP requests. This basically amounts to Wireshark's default UI getting in the way of seeing the request and response - all three frames of the main UI are nearly useless to me.</p><p>Whenever I use Wireshark, I find myself constantly right-clicking on a TCP stream, selecting "Follow TCP Stream", closing the dialog box, clicking "Clear" on the filter, and repeating that process quite a few times. I would much prefer a view of all available streams and be able to single or double-click them to view the raw data. Is there such a view available?</p></div><div id="question-tags" class="tags-container tags">follow.tcp.stream</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 May '13, 08:14</strong></p><img src="https://secure.gravatar.com/avatar/d708722e89e964c809878826c78cc946?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gina_miller&#39;s gravatar image" /><p>gina_miller<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gina_miller has no accepted answers">0%</span></p></div></div><div id="comments-container-21666" class="comments-container"></div><div id="comment-tools-21666" class="comment-tools"></div><div class="clear"></div><div id="comment-21666-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21667"></span>

<div id="answer-container-21667" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21667-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Something 'similar' would be</p><blockquote><p><code>Statistics -&gt; Conversations -&gt; TCP</code><br />
</p></blockquote><p>Then select one conversation and click on <strong>Follow Stream</strong>. Check the data. Then go back to the conversations window and repeat that step. It's not <strong>exactly</strong> what you want (not possible with the current Wireshark GUI), but it may help to speed up your work a bit.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '13, 08:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-21667" class="comments-container"><span id="21675"></span><div id="comment-21675" class="comment"><div id="post-21675-score" class="comment-score"></div><div class="comment-text"><p>That is better than what I was doing. Since it is the only solution, I'll accept this as the answer. Thanks!</p></div><div id="comment-21675-info" class="comment-info"><span class="comment-age">(31 May '13, 09:06)</span> gina_miller</div></div></div><div id="comment-tools-21667" class="comment-tools"></div><div class="clear"></div><div id="comment-21667-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

