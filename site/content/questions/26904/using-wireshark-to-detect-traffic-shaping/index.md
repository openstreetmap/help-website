+++
type = "question"
title = "Using Wireshark to detect traffic shaping"
description = '''i&#x27;m new to wireshark, i have a question for the wireshark pros: i believe that my provider slows down/shapes my download speed if i use certain services / ports. lets say if i use ftp i have full 18mb/s, if i try to download something from the usenet, it seesms that my max. speed is throttled to max...'''
date = "2013-11-12T13:37:00Z"
lastmod = "2013-11-14T01:47:00Z"
weight = 26904
keywords = [ "traffic", "shaping" ]
aliases = [ "/questions/26904" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Using Wireshark to detect traffic shaping](/questions/26904/using-wireshark-to-detect-traffic-shaping)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26904-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26904-score" class="post-score" title="current number of votes">0</div><span id="post-26904-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i'm new to wireshark, i have a question for the wireshark pros:</p><p>i believe that my provider slows down/shapes my download speed if i use certain services / ports.</p><p>lets say if i use ftp i have full 18mb/s, if i try to download something from the usenet, it seesms that my max. speed is throttled to max 10mb/s.</p><p>is there a difference how the packets look like when throttled/not throttled ? or is there any other way to collect evidence ?</p><p>thx in advance!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-shaping" rel="tag" title="see questions tagged &#39;shaping&#39;">shaping</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Nov '13, 13:37</strong></p><img src="https://secure.gravatar.com/avatar/e2c66bdf3ce94c5b2716cbf568768361?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="supreme&#39;s gravatar image" /><p><span>supreme</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="supreme has no accepted answers">0%</span></p></div></div><div id="comments-container-26904" class="comments-container"></div><div id="comment-tools-26904" class="comment-tools"></div><div class="clear"></div><div id="comment-26904-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26964"></span>

<div id="answer-container-26964" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26964-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26964-score" class="post-score" title="current number of votes">1</div><span id="post-26964-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="supreme has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"Traffic Shaping" is usually achieved by dropping packets to/from your IP address which then will trigger re-transmissions. So to answer your questions:</p><ul><li>Is there a difference how the packets look like when throttled/not throttled ?</li></ul><p>No</p><ul><li>is there any other way to collect evidence ?</li></ul><p>A higher than usual packet loss rate / re-transmissions. Of course, you need to have a basis to compare so maybe you can take another trace from a device that is not 'throttled' and see what's different.</p><p><strong><em>THE</em></strong> filter number 1 filter is probably just <strong>"expert"</strong><br />
The <strong>Statistics -&gt; FlowGraph</strong> will then give a nice overview on all suspicious packets.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Selection_123.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Nov '13, 13:09</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Nov '13, 22:20</strong> </span></p></div></div><div id="comments-container-26964" class="comments-container"><span id="26969"></span><div id="comment-26969" class="comment"><div id="post-26969-score" class="comment-score"></div><div class="comment-text"><p>can you please tell me what filters exactly i have to use to filter for the right informations ?</p></div><div id="comment-26969-info" class="comment-info"><span class="comment-age">(13 Nov '13, 14:56)</span> <span class="comment-user userinfo">supreme</span></div></div><span id="26982"></span><div id="comment-26982" class="comment"><div id="post-26982-score" class="comment-score">1</div><div class="comment-text"><p>I updated my answer with the information about the filter I'd get started with.</p></div><div id="comment-26982-info" class="comment-info"><span class="comment-age">(13 Nov '13, 22:22)</span> <span class="comment-user userinfo">mrEEde</span></div></div><span id="26986"></span><div id="comment-26986" class="comment"><div id="post-26986-score" class="comment-score"></div><div class="comment-text"><p>thx you for your help!</p></div><div id="comment-26986-info" class="comment-info"><span class="comment-age">(14 Nov '13, 01:47)</span> <span class="comment-user userinfo">supreme</span></div></div></div><div id="comment-tools-26964" class="comment-tools"></div><div class="clear"></div><div id="comment-26964-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

