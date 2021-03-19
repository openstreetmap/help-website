+++
type = "question"
title = "How to fetch framelength of a frame using tshark commad ?"
description = '''Can you please suggest a code for fetching the frame length using tshark.'''
date = "2014-10-19T22:37:00Z"
lastmod = "2014-10-20T04:54:00Z"
weight = 37170
keywords = [ "framelength", "tshark" ]
aliases = [ "/questions/37170" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to fetch framelength of a frame using tshark commad ?](/questions/37170/how-to-fetch-framelength-of-a-frame-using-tshark-commad)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37170-score" class="post-score" title="current number of votes">0</div><span id="post-37170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can you please suggest a code for fetching the frame length using tshark.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-framelength" rel="tag" title="see questions tagged &#39;framelength&#39;">framelength</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '14, 22:37</strong></p><img src="https://secure.gravatar.com/avatar/fbfa082235ab499c4eb41ae3d8f6fe36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="udaya&#39;s gravatar image" /><p><span>udaya</span><br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="udaya has one accepted answer">100%</span></p></div></div><div id="comments-container-37170" class="comments-container"></div><div id="comment-tools-37170" class="comment-tools"></div><div class="clear"></div><div id="comment-37170-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37172"></span>

<div id="answer-container-37172" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37172-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37172-score" class="post-score" title="current number of votes">2</div><span id="post-37172-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="udaya has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you want just the length you can do:</p><pre><code> tshark -Tfields -e frame.len -r yourfile.pcapng</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '14, 01:23</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-37172" class="comments-container"><span id="37188"></span><div id="comment-37188" class="comment"><div id="post-37188-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jeff!!</p></div><div id="comment-37188-info" class="comment-info"><span class="comment-age">(20 Oct '14, 04:54)</span> <span class="comment-user userinfo">udaya</span></div></div></div><div id="comment-tools-37172" class="comment-tools"></div><div class="clear"></div><div id="comment-37172-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

