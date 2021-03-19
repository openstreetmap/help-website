+++
type = "question"
title = "Start button not appearing and can&#x27;t capture"
description = '''I have a HP Windows 8 comptuer running Wireshark 1.12.7 and Winpcap 4.1.3. When I start up wireshark, capture button is grayed out and no start button. Why is this happening? Am I missing a step or somthing?'''
date = "2015-09-04T08:58:00Z"
lastmod = "2015-09-08T15:53:00Z"
weight = 45634
keywords = [ "capture", "wireshark" ]
aliases = [ "/questions/45634" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Start button not appearing and can't capture](/questions/45634/start-button-not-appearing-and-cant-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45634-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45634-score" class="post-score" title="current number of votes">0</div><span id="post-45634-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a HP Windows 8 comptuer running Wireshark 1.12.7 and Winpcap 4.1.3. When I start up wireshark, capture button is grayed out and no start button. Why is this happening? Am I missing a step or somthing?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Sep '15, 08:58</strong></p><img src="https://secure.gravatar.com/avatar/5e2d0bcf9af1553c8973e72131205e5e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MTRGX3&#39;s gravatar image" /><p><span>MTRGX3</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MTRGX3 has no accepted answers">0%</span></p></div></div><div id="comments-container-45634" class="comments-container"></div><div id="comment-tools-45634" class="comment-tools"></div><div class="clear"></div><div id="comment-45634-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45682"></span>

<div id="answer-container-45682" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45682-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45682-score" class="post-score" title="current number of votes">1</div><span id="post-45682-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Why is this happening?</p></blockquote><p>Wireshark can't find any interfaces to capture from.</p><p>Possible Reasons:</p><ul><li>there are no interfaces that are detected by WinPcap (what is the output of <strong>dumpcap -D -M</strong>)</li><li>WinPcap is not installed properly (try to re-install WinPcap from winpcap.org)</li><li>The NPF service is not running (run the following command in an elevated DOS box: <strong>sc start npf</strong>)</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '15, 17:04</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-45682" class="comments-container"><span id="45708"></span><div id="comment-45708" class="comment"><div id="post-45708-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt. It worked. I reinstalled WinPcap and it work! :)KN</p></div><div id="comment-45708-info" class="comment-info"><span class="comment-age">(08 Sep '15, 09:15)</span> <span class="comment-user userinfo">MTRGX3</span></div></div><span id="45719"></span><div id="comment-45719" class="comment"><div id="post-45719-score" class="comment-score"></div><div class="comment-text"><p>Good!</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-45719-info" class="comment-info"><span class="comment-age">(08 Sep '15, 15:53)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-45682" class="comment-tools"></div><div class="clear"></div><div id="comment-45682-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

