+++
type = "question"
title = "Why am I not seeing any activity to or from my handheld device?"
description = '''I asked this here: http://stackoverflow.com/questions/15259602/why-am-i-seeing-no-conversations-between-my-desktop-and-my-handheld-apps-with-wi Basically: my handheld device (the app in question is a Windows CE/Compact Framework .Net 1.1 C# app) is physically attached to my desktop via usb cable; on...'''
date = "2013-03-06T15:05:00Z"
lastmod = "2013-03-06T15:14:00Z"
weight = 19249
keywords = [ "windows-ce", "handheld" ]
aliases = [ "/questions/19249" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why am I not seeing any activity to or from my handheld device?](/questions/19249/why-am-i-not-seeing-any-activity-to-or-from-my-handheld-device)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19249-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19249-score" class="post-score" title="current number of votes">0</div><span id="post-19249-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I asked this here: <a href="http://stackoverflow.com/questions/15259602/why-am-i-seeing-no-conversations-between-my-desktop-and-my-handheld-apps-with-wi">http://stackoverflow.com/questions/15259602/why-am-i-seeing-no-conversations-between-my-desktop-and-my-handheld-apps-with-wi</a></p><p>Basically: my handheld device (the app in question is a Windows CE/Compact Framework .Net 1.1 C# app) is physically attached to my desktop via usb cable; on the desktop, a "server" app (Windows Forms, .NET 4) is running. They communicate with each other, but Wireshark seems to be oblivious to this (no packets passed to or from the handheld device are shown). Why would that be? What must I do to get Wireshark to recognize the handheld?</p><p>To get the IP addresses so that I can filter on them in the capture, I used the old "ipconfig" trick at the command prompt (on both the desktop machine and the handheld device). I see traffic to and from the desktop's IP address, but nothing to/from the handheld device...???</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows-ce" rel="tag" title="see questions tagged &#39;windows-ce&#39;">windows-ce</span> <span class="post-tag tag-link-handheld" rel="tag" title="see questions tagged &#39;handheld&#39;">handheld</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '13, 15:05</strong></p><img src="https://secure.gravatar.com/avatar/317f4b62da2b0186feac9b6209793505?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Clay%20Shannon&#39;s gravatar image" /><p><span>Clay Shannon</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Clay Shannon has no accepted answers">0%</span></p></div></div><div id="comments-container-19249" class="comments-container"></div><div id="comment-tools-19249" class="comment-tools"></div><div class="clear"></div><div id="comment-19249-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19251"></span>

<div id="answer-container-19251" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19251-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19251-score" class="post-score" title="current number of votes">0</div><span id="post-19251-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark captures data of network interface cards, so I doubt that your USB cable qualifies as valid source for captured data packets - at least on Windows boxes. I don't think Wireshark is the right tool for what you want to do. You probably need some kind of USB communication monitoring tool.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '13, 15:14</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-19251" class="comments-container"></div><div id="comment-tools-19251" class="comment-tools"></div><div class="clear"></div><div id="comment-19251-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

