+++
type = "question"
title = "Windows 7 how to calculate window size in tcp"
description = '''can some one plese explain how to calculate TCP window size in windows 7 .is it depend on the initial link quality or does it calculate dyamicaly depend on the link quality .what are the parameters used ?'''
date = "2012-07-25T21:58:00Z"
lastmod = "2012-07-31T07:24:00Z"
weight = 13006
keywords = [ "syswan", "windows7", "tcp" ]
aliases = [ "/questions/13006" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Windows 7 how to calculate window size in tcp](/questions/13006/windows-7-how-to-calculate-window-size-in-tcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13006-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13006-score" class="post-score" title="current number of votes">0</div><span id="post-13006-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>can some one plese explain how to calculate TCP window size in windows 7 .is it depend on the initial link quality or does it calculate dyamicaly depend on the link quality .what are the parameters used ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-syswan" rel="tag" title="see questions tagged &#39;syswan&#39;">syswan</span> <span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jul '12, 21:58</strong></p><img src="https://secure.gravatar.com/avatar/1f2301919497d73359137f6a0b32c3f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gayandis&#39;s gravatar image" /><p><span>gayandis</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gayandis has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Jul '12, 22:16</strong> </span></p></div></div><div id="comments-container-13006" class="comments-container"></div><div id="comment-tools-13006" class="comment-tools"></div><div class="clear"></div><div id="comment-13006-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13188"></span>

<div id="answer-container-13188" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13188-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13188-score" class="post-score" title="current number of votes">0</div><span id="post-13188-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Initail values are "fixed" (actually configurable), but there is also a feature in TCP/IP Stack of Windows 7 called "TCP Receive Window Auto-Tuning".</p><blockquote><p>Take a look at these articles from "The Cable Guy"<br />
<code>http://technet.microsoft.com/en-us/magazine/2007.01.cableguy.aspx</code><br />
<code>http://technet.microsoft.com/en-us/library/bb878127.aspx</code><br />
</p></blockquote><p><span>@Landi</span> gave a presentation at Sharkfest 2012 about some issues with TCP receive window scaling.</p><blockquote><p><code>http://sharkfest.wireshark.org/sharkfest.12/</code><br />
</p></blockquote><p>Look for: "Effects of Receiver-Side Window Scaling on Enterprise Networks"</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jul '12, 07:24</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Jul '12, 07:33</strong> </span></p></div></div><div id="comments-container-13188" class="comments-container"></div><div id="comment-tools-13188" class="comment-tools"></div><div class="clear"></div><div id="comment-13188-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

