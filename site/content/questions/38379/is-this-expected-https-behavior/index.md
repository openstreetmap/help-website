+++
type = "question"
title = "Is this expected HTTPS behavior?"
description = '''Hello, I&#x27;m getting a timeout/&quot;web page unavailable&quot; on a network device i should be able to login via HTTPS. That port is open and I can telnet to 443, so I did a trace. I&#x27;ve attached a trace file. I am the .160 address and the network device is the .115 address (I&#x27;ve anonymized the trace). I really...'''
date = "2014-12-05T15:36:00Z"
lastmod = "2014-12-29T14:27:00Z"
weight = 38379
keywords = [ "https" ]
aliases = [ "/questions/38379" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Is this expected HTTPS behavior?](/questions/38379/is-this-expected-https-behavior)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38379-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38379-score" class="post-score" title="current number of votes">0</div><span id="post-38379-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm getting a timeout/"web page unavailable" on a network device i should be able to login via HTTPS. That port is open and I can telnet to 443, so I did a trace. I've attached a trace file. I am the .160 address and the network device is the .115 address (I've anonymized the trace). I really don't understand why the FIN is coming from my machine at packet 6...</p><p>Here is the trace file: <a href="https://drive.google.com/file/d/0B8-kDu5JM-P2NmxPWDltX3Y5dkk/view?usp=sharing">https://drive.google.com/file/d/0B8-kDu5JM-P2NmxPWDltX3Y5dkk/view?usp=sharing</a></p><p>Thanks in advance for any help.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '14, 15:36</strong></p><img src="https://secure.gravatar.com/avatar/4a4df10c701372e5dbbb8015a1d6b67b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="patrick_harrold&#39;s gravatar image" /><p><span>patrick_harrold</span><br />
<span class="score" title="36 reputation points">36</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="patrick_harrold has no accepted answers">0%</span></p></div></div><div id="comments-container-38379" class="comments-container"></div><div id="comment-tools-38379" class="comment-tools"></div><div class="clear"></div><div id="comment-38379-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="38411"></span>

<div id="answer-container-38411" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38411-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38411-score" class="post-score" title="current number of votes">1</div><span id="post-38411-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="patrick_harrold has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As <span>@mrEEDE</span> said unless you create another capture containing all the traffic (did you sanitise the first in some way by chopping bytes?) it's hard to tell what's going on.</p><p>My guess is that the server doesn't properly handle something in the client hello, e.g. SSL protocol level or cipher choice, and instead if returning a sensible response, or closing the connection itself, it just isn't responding leading the client to timeout and close the connection.</p><p>Try making the client use a different ssl level, e.g. drop down if currently using TLS 1.2, or move up if using SSL 3.0.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '14, 05:59</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-38411" class="comments-container"><span id="38772"></span><div id="comment-38772" class="comment"><div id="post-38772-score" class="comment-score"></div><div class="comment-text"><p>Apologies for the late reply. Thank you both for the help.</p></div><div id="comment-38772-info" class="comment-info"><span class="comment-age">(29 Dec '14, 14:27)</span> <span class="comment-user userinfo">patrick_harrold</span></div></div></div><div id="comment-tools-38411" class="comment-tools"></div><div class="clear"></div><div id="comment-38411-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38407"></span>

<div id="answer-container-38407" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38407-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38407-score" class="post-score" title="current number of votes">0</div><span id="post-38407-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You did not trace the full packets so it's hard to comment based on ip/tcp headers only . If the client's 211 bytes is a ClientHello then the server should respond with a ServerHello, which it doesn't. If this is not a ClientHello then the server is right in not responding...</p><p>Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '14, 02:32</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-38407" class="comments-container"></div><div id="comment-tools-38407" class="comment-tools"></div><div class="clear"></div><div id="comment-38407-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

