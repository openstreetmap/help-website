+++
type = "question"
title = "Capturing TCP handshake but no data traffic"
description = '''I have an application that listens on port 6001. An interface will send something to the port and my software should acknowledge it via application layer protocol, but doesn&#x27;t. It works in my test environment, but doesn&#x27;t work at my client site. In wireshark at the client side, I see the tcp handsha...'''
date = "2015-08-12T17:09:00Z"
lastmod = "2015-08-12T20:13:00Z"
weight = 45028
keywords = [ "capture", "handshake", "tcp" ]
aliases = [ "/questions/45028" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing TCP handshake but no data traffic](/questions/45028/capturing-tcp-handshake-but-no-data-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45028-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45028-score" class="post-score" title="current number of votes">0</div><span id="post-45028-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an application that listens on port 6001. An interface will send something to the port and my software should acknowledge it via application layer protocol, but doesn't. It works in my test environment, but doesn't work at my client site. In wireshark at the client side, I see the tcp handshake but no data traffic. In the test environment, I see the tcp handshake but no data traffic. Any ideas?</p><p>I know Windows comes with a built-in tool called netsh. With netsh, you can capture traffic. I'm going to see if I see data packets in netsh using the following command while I wait for a response: “Netsh trace start scenario=NetConnection capture=yes report=yes persistent=no maxsize=1024 correlation=yes traceFile=C:\Logs\NetTrace.etl”</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-handshake" rel="tag" title="see questions tagged &#39;handshake&#39;">handshake</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Aug '15, 17:09</strong></p><img src="https://secure.gravatar.com/avatar/16cc2cfaa993762e4fff663f4e929893?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alan1337&#39;s gravatar image" /><p><span>alan1337</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alan1337 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>12 Aug '15, 20:09</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-45028" class="comments-container"></div><div id="comment-tools-45028" class="comment-tools"></div><div class="clear"></div><div id="comment-45028-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45031"></span>

<div id="answer-container-45031" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45031-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45031-score" class="post-score" title="current number of votes">0</div><span id="post-45031-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This sounds exactly like <a href="https://ask.wireshark.org/questions/7664/wont-capture-packets-that-i-know-are-there">the question to which your question was originally posted as a comment</a> (this is a Q&amp;A site, not a forum; each question should be asked separately, so users can search for it before asking questions themselves).</p><p>As per the answer to that question, "Sounds like <a href="http://wiki.wireshark.org/CaptureSetup/Offloading#TCP_Chimney">TCP Chimney</a> to me..." If TCP Chimney is on for the interface on which you're capturing, try turning it off.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Aug '15, 20:13</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-45031" class="comments-container"></div><div id="comment-tools-45031" class="comment-tools"></div><div class="clear"></div><div id="comment-45031-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

