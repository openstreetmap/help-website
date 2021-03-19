+++
type = "question"
title = "Capturing HTTP packets from other computers"
description = '''Hi I was wondering how you view HTTP packets from other computers that are on the same network as you. I&#x27;ve been reading around and can not figure it out. I can view my http traffic but not other computers. If you could respond back with an answer it would be greatly appreciated.'''
date = "2013-11-11T16:23:00Z"
lastmod = "2013-11-13T02:42:00Z"
weight = 26858
keywords = [ "https" ]
aliases = [ "/questions/26858" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing HTTP packets from other computers](/questions/26858/capturing-http-packets-from-other-computers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26858-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26858-score" class="post-score" title="current number of votes">0</div><span id="post-26858-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I was wondering how you view HTTP packets from other computers that are on the same network as you. I've been reading around and can not figure it out. I can view my http traffic but not other computers. If you could respond back with an answer it would be greatly appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Nov '13, 16:23</strong></p><img src="https://secure.gravatar.com/avatar/9837943c9432cc23c03847de491ab816?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brad&#39;s gravatar image" /><p><span>brad</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brad has no accepted answers">0%</span></p></div></div><div id="comments-container-26858" class="comments-container"></div><div id="comment-tools-26858" class="comment-tools"></div><div class="clear"></div><div id="comment-26858-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26870"></span>

<div id="answer-container-26870" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26870-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26870-score" class="post-score" title="current number of votes">1</div><span id="post-26870-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You'll need to read and understand how to setup your captures. Start at the Wiki page on <a href="http://wiki.wireshark.org/CaptureSetup">Capture Setup</a>, and then look at the page for the media type used by your network, most likely <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">Ethernet</a>.</p><p>Hint: You are likely to be using a switched network so you'll need to arrange for the switches to span or mirror traffic to your capture host.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '13, 02:06</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-26870" class="comments-container"><span id="26916"></span><div id="comment-26916" class="comment"><div id="post-26916-score" class="comment-score"></div><div class="comment-text"><p>how do I arrange for switches to span or mirror traffic. I went through capture setup and I think I completed it all but it still isn't working.</p></div><div id="comment-26916-info" class="comment-info"><span class="comment-age">(12 Nov '13, 18:43)</span> <span class="comment-user userinfo">brad</span></div></div><span id="26931"></span><div id="comment-26931" class="comment"><div id="post-26931-score" class="comment-score"></div><div class="comment-text"><p>You'll need access to whatever admin interface your switches provide and the knowledge on how to use that admin interface to span or mirror the ports. As such, this isn't really a question for Ask Wireshark, more for the support options for your particular switches.</p></div><div id="comment-26931-info" class="comment-info"><span class="comment-age">(13 Nov '13, 02:42)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-26870" class="comment-tools"></div><div class="clear"></div><div id="comment-26870-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

