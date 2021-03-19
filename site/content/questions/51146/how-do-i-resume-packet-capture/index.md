+++
type = "question"
title = "How do I resume packet capture?"
description = '''I&#x27;m on ubuntu 14.04. &#x27;wireshark --version&#x27; report: &quot;wireshark: 4351&quot;. I start up wireshark, select an interface and begin to capture packets.  If I hit the stop button, I can&#x27;t start again. After stopping packet capture, if I hit the blue fin button (&quot;Start Capturing Packets&quot;) packet capture doesn&#x27;t...'''
date = "2016-03-24T03:28:00Z"
lastmod = "2016-03-24T04:22:00Z"
weight = 51146
keywords = [ "packet-capture" ]
aliases = [ "/questions/51146" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How do I resume packet capture?](/questions/51146/how-do-i-resume-packet-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51146-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51146-score" class="post-score" title="current number of votes">0</div><span id="post-51146-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm on ubuntu 14.04. 'wireshark --version' report: "wireshark: 4351".</p><p>I start up wireshark, select an interface and begin to capture packets. If I hit the stop button, I can't start again. After stopping packet capture, if I hit the blue fin button ("Start Capturing Packets") packet capture doesn't resume.</p><p>I can a notification at the bottom of the UI that says "No Interface Selected".</p><p>I haven't been able to figure out how to select an interface at this point.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packet-capture" rel="tag" title="see questions tagged &#39;packet-capture&#39;">packet-capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Mar '16, 03:28</strong></p><img src="https://secure.gravatar.com/avatar/391cee05e59f8a5dda13c4cf7c0734db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bobdobbs&#39;s gravatar image" /><p><span>bobdobbs</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bobdobbs has no accepted answers">0%</span></p></div></div><div id="comments-container-51146" class="comments-container"><span id="51147"></span><div id="comment-51147" class="comment"><div id="post-51147-score" class="comment-score"></div><div class="comment-text"><p>Your version number looks a bit odd, what does it show in Help -&gt; About Wireshark?</p></div><div id="comment-51147-info" class="comment-info"><span class="comment-age">(24 Mar '16, 03:57)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-51146" class="comment-tools"></div><div class="clear"></div><div id="comment-51146-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51148"></span>

<div id="answer-container-51148" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51148-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51148-score" class="post-score" title="current number of votes">1</div><span id="post-51148-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bobdobbs has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can't restart it once you stop. If you do that, you fundamentally break the packet trace. You can start a new capture after either saving or continuing without saving. If you go to capture options you'll be able to select the interface.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Mar '16, 04:22</strong></p><img src="https://secure.gravatar.com/avatar/a7ee4b7fed14f9a005b09517a80976a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="StuWhitby&#39;s gravatar image" /><p><span>StuWhitby</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="StuWhitby has one accepted answer">100%</span></p></div></div><div id="comments-container-51148" class="comments-container"></div><div id="comment-tools-51148" class="comment-tools"></div><div class="clear"></div><div id="comment-51148-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

