+++
type = "question"
title = "Jitter for RTP stream shown as 0"
description = '''The captured RTP stream&#x27;s analysis shows the following: Max delta = 0.00 ms at packet no. 0  Max jitter = 0.00 ms. Mean jitter = 0.00 ms. Max skew = 0.00 ms.  Do you think this is wrong? How can I verify the jitter by looking at the individual packet latencies? '''
date = "2010-11-27T23:24:00Z"
lastmod = "2010-12-06T10:41:00Z"
weight = 1142
keywords = [ "stream", "rtp", "analysis" ]
aliases = [ "/questions/1142" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Jitter for RTP stream shown as 0](/questions/1142/jitter-for-rtp-stream-shown-as-0)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1142-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1142-score" class="post-score" title="current number of votes">0</div><span id="post-1142-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The captured RTP stream's analysis shows the following:</p><pre><code>Max delta = 0.00 ms at packet no. 0 
Max jitter = 0.00 ms. Mean jitter = 0.00 ms.
Max skew = 0.00 ms.</code></pre><p>Do you think this is wrong? How can I verify the jitter by looking at the individual packet latencies?<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span> <span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Nov '10, 23:24</strong></p><img src="https://secure.gravatar.com/avatar/da051abac41879aed4060d544d37fd6f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="skypemesm&#39;s gravatar image" /><p><span>skypemesm</span><br />
<span class="score" title="46 reputation points">46</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="skypemesm has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-1142" class="comments-container"></div><div id="comment-tools-1142" class="comment-tools"></div><div class="clear"></div><div id="comment-1142-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="1220"></span>

<div id="answer-container-1220" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1220-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1220-score" class="post-score" title="current number of votes">0</div><span id="post-1220-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This looks wrong to me if you have valid RTP (delta would be non-zero). Care to put up a sample?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '10, 23:18</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p><span>martyvis</span><br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-1220" class="comments-container"></div><div id="comment-tools-1220" class="comment-tools"></div><div class="clear"></div><div id="comment-1220-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1225"></span>

<div id="answer-container-1225" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1225-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1225-score" class="post-score" title="current number of votes">0</div><span id="post-1225-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Check if you have "Incorrect timestamp" messages in status field. For dynamic payload types Wireshark is unable to calculate jitter etc., because it does not know the sampling frequency of codec used.</p><p>In order for Wireshark to work with dynamic payload types someone must implement either manual setting of sampling frequency or parsing SDP files.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '10, 02:47</strong></p><img src="https://secure.gravatar.com/avatar/d7db360cd13297a4ae76510d1b91edb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kamokr&#39;s gravatar image" /><p><span>kamokr</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kamokr has no accepted answers">0%</span></p></div></div><div id="comments-container-1225" class="comments-container"><span id="1241"></span><div id="comment-1241" class="comment"><div id="post-1241-score" class="comment-score"></div><div class="comment-text"><p>Reading the sampling rate is implemented in trunk, i don't remember if it made it into 1.4.</p></div><div id="comment-1241-info" class="comment-info"><span class="comment-age">(03 Dec '10, 23:41)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="1252"></span><div id="comment-1252" class="comment"><div id="post-1252-score" class="comment-score"></div><div class="comment-text"><p>Tried trunk, rev. 35106, does not work. Are you sure it is fully implemented?</p></div><div id="comment-1252-info" class="comment-info"><span class="comment-age">(06 Dec '10, 00:47)</span> <span class="comment-user userinfo">kamokr</span></div></div></div><div id="comment-tools-1225" class="comment-tools"></div><div class="clear"></div><div id="comment-1225-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1259"></span>

<div id="answer-container-1259" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1259-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1259-score" class="post-score" title="current number of votes">0</div><span id="post-1259-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have you just filtered down to the one particular RTP conversation in one direction? If so, you can add a frame delta time column and increase the precision. I would use this technique to validate you 0.00% jitter. It could be that the jitter is present, but below 0.005% and is rounded down. Just a thought.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Dec '10, 10:41</strong></p><img src="https://secure.gravatar.com/avatar/e62501f00394530927e4b0c9e86bfb46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Stewart&#39;s gravatar image" /><p><span>Paul Stewart</span><br />
<span class="score" title="301 reputation points">301</span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Stewart has 3 accepted answers">6%</span></p></div></div><div id="comments-container-1259" class="comments-container"></div><div id="comment-tools-1259" class="comment-tools"></div><div class="clear"></div><div id="comment-1259-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

