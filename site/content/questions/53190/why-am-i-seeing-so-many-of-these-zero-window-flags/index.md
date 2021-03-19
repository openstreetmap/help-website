+++
type = "question"
title = "Why am i seeing so many Of these Zero Window flags?"
description = '''I&#x27;m not seeing any reason why i should be getting these?  The Application i am using to grab data from an sql server seems sluggish at times and during initialization  seems to freeze. At the times where this latency happens i see alot of Window Update and Zero Window flags. https://www.cloudshark.o...'''
date = "2016-06-03T16:36:00Z"
lastmod = "2016-06-04T00:58:00Z"
weight = 53190
keywords = [ "tcpwindowfull", "zero-window" ]
aliases = [ "/questions/53190" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why am i seeing so many Of these Zero Window flags?](/questions/53190/why-am-i-seeing-so-many-of-these-zero-window-flags)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53190-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53190-score" class="post-score" title="current number of votes">0</div><span id="post-53190-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm not seeing any reason why i should be getting these? The Application i am using to grab data from an sql server seems sluggish at times and during initialization seems to freeze. At the times where this latency happens i see alot of Window Update and Zero Window flags.</p><p><a href="https://www.cloudshark.org/captures/b68f6cd0086b">https://www.cloudshark.org/captures/b68f6cd0086b</a></p><p>It's difficult for me to confirm whether or not the issue starts with my server or my client?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcpwindowfull" rel="tag" title="see questions tagged &#39;tcpwindowfull&#39;">tcpwindowfull</span> <span class="post-tag tag-link-zero-window" rel="tag" title="see questions tagged &#39;zero-window&#39;">zero-window</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jun '16, 16:36</strong></p><img src="https://secure.gravatar.com/avatar/8a5bcc1a75e2568c2b44e090c175a5c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Juxtapositioned0110&#39;s gravatar image" /><p><span>Juxtapositio...</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Juxtapositioned0110 has no accepted answers">0%</span></p></div></div><div id="comments-container-53190" class="comments-container"><span id="53196"></span><div id="comment-53196" class="comment"><div id="post-53196-score" class="comment-score"></div><div class="comment-text"><p>The capture you've posted only shows one direction (the ACKs from the client to the server), and it is really not easy to find out what is going on from such a short capture and one direction. As the session establishment phase is missing, it is unclear even how big the window actually is, because the windows scaling factor information is missing. So the "256" may be 256 bytes or 65536 bytes or even more.</p><p>So please start capturing before starting the application and capture both directions. Then, if you have privacy concerns, use Tracewrangler to wipe out the payload and keep only the TCP overhead information, and post that modified capture (or post it as-is to exclude one possible source of errors if you don't).</p></div><div id="comment-53196-info" class="comment-info"><span class="comment-age">(04 Jun '16, 00:58)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-53190" class="comment-tools"></div><div class="clear"></div><div id="comment-53190-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53192"></span>

<div id="answer-container-53192" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53192-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53192-score" class="post-score" title="current number of votes">1</div><span id="post-53192-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, problem is from 192.168.1.71 i.e client.... Receive buffer is getting exhausted....</p><p>Mostly bellow said solutions may solve the problem 1) While sending the data enable PUSH flag in TCP .... 2) Enable nagle's algorithm for more info <a href="https://en.wikipedia.org/wiki/Nagle&#39;s_algorithm">https://en.wikipedia.org/wiki/Nagle's_algorithm</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jun '16, 20:07</strong></p><img src="https://secure.gravatar.com/avatar/ce1843f92a1c18db26bc79b3afa9bd50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srinu_bel&#39;s gravatar image" /><p><span>srinu_bel</span><br />
<span class="score" title="20 reputation points">20</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srinu_bel has no accepted answers">0%</span></p></div></div><div id="comments-container-53192" class="comments-container"></div><div id="comment-tools-53192" class="comment-tools"></div><div class="clear"></div><div id="comment-53192-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

