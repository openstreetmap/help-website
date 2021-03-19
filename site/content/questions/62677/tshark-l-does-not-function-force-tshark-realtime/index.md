+++
type = "question"
title = "TShark -l does not function. Force TShark Realtime?"
description = '''The -l argument for tshark is supposed to display the dissection data immediately. However, it has no effect. I have a custom dissector sending data to another program. The other program is currently receiving it in bursts at about 2 times a second. This is far to slow. If -l does not work is there ...'''
date = "2017-07-11T11:52:00Z"
lastmod = "2017-07-12T06:40:00Z"
weight = 62677
keywords = [ "-l", "tshark", "command-line", "realtime" ]
aliases = [ "/questions/62677" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TShark -l does not function. Force TShark Realtime?](/questions/62677/tshark-l-does-not-function-force-tshark-realtime)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62677-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62677-score" class="post-score" title="current number of votes">0</div><span id="post-62677-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The -l argument for tshark is supposed to display the dissection data immediately. However, it has no effect. I have a custom dissector sending data to another program. The other program is currently receiving it in bursts at about 2 times a second. This is far to slow. If -l does not work is there anyway to force wireshark or tshark to make these bursts happen more frequently? Currently none of the preferences I have toyed with have made an impact, including buffer size.</p><p>Thank You</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link--l" rel="tag" title="see questions tagged &#39;-l&#39;">-l</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-command-line" rel="tag" title="see questions tagged &#39;command-line&#39;">command-line</span> <span class="post-tag tag-link-realtime" rel="tag" title="see questions tagged &#39;realtime&#39;">realtime</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jul '17, 11:52</strong></p><img src="https://secure.gravatar.com/avatar/a526f7caccd56a1978ad128830e65c22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="afay&#39;s gravatar image" /><p><span>afay</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="afay has no accepted answers">0%</span></p></div></div><div id="comments-container-62677" class="comments-container"></div><div id="comment-tools-62677" class="comment-tools"></div><div class="clear"></div><div id="comment-62677-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62681"></span>

<div id="answer-container-62681" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62681-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62681-score" class="post-score" title="current number of votes">0</div><span id="post-62681-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In this case it's dumpcap that is the source of the delay: it only sends packets up to tshark once every 500msec (twice a second). <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=2874">Bug 2874</a> contains some details.</p><p>It seems the solution is to have tshark read from a pipe instead of from dumpcap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jul '17, 15:06</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-62681" class="comments-container"><span id="62683"></span><div id="comment-62683" class="comment"><div id="post-62683-score" class="comment-score"></div><div class="comment-text"><p>Thank You!</p></div><div id="comment-62683-info" class="comment-info"><span class="comment-age">(11 Jul '17, 15:11)</span> <span class="comment-user userinfo">afay</span></div></div><span id="62702"></span><div id="comment-62702" class="comment"><div id="post-62702-score" class="comment-score"></div><div class="comment-text"><p>You're welcome. BTW this is a Q&amp;A site so please be sure to Accept the answer (assuming it answers your question) by clicking on the checkmark next to the answer. That way the question won't show up as "unanswered."</p></div><div id="comment-62702-info" class="comment-info"><span class="comment-age">(12 Jul '17, 06:40)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-62681" class="comment-tools"></div><div class="clear"></div><div id="comment-62681-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

