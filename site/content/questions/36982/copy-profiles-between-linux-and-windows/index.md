+++
type = "question"
title = "Copy Profiles between linux and windows"
description = '''I have a set of profiles on my Windows Box. I want them copied to Linux. I can copy them between windows boxes and all is good. I put them in my Linux folder and the profiles appear in the menu. But as soon as I try to switch to one of tem, I just get a grey window and after 60 seconds or so wiresha...'''
date = "2014-10-12T10:11:00Z"
lastmod = "2014-10-16T12:14:00Z"
weight = 36982
keywords = [ "profile", "linux" ]
aliases = [ "/questions/36982" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Copy Profiles between linux and windows](/questions/36982/copy-profiles-between-linux-and-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36982-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36982-score" class="post-score" title="current number of votes">0</div><span id="post-36982-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a set of profiles on my Windows Box. I want them copied to Linux. I can copy them between windows boxes and all is good. I put them in my Linux folder and the profiles appear in the menu. But as soon as I try to switch to one of tem, I just get a grey window and after 60 seconds or so wireshark crashes..Any Ideas?</p><p>This should be possible..</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-profile" rel="tag" title="see questions tagged &#39;profile&#39;">profile</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Oct '14, 10:11</strong></p><img src="https://secure.gravatar.com/avatar/05ba95262a3352e3af4ba69c0ec0dff2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarrenWright&#39;s gravatar image" /><p><span>DarrenWright</span><br />
<span class="score" title="216 reputation points">216</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarrenWright has 5 accepted answers">26%</span></p></div></div><div id="comments-container-36982" class="comments-container"><span id="36983"></span><div id="comment-36983" class="comment"><div id="post-36983-score" class="comment-score"></div><div class="comment-text"><p>already cleared all the c: and d: paths and updated the capture devices.. naja. manual copy time..</p></div><div id="comment-36983-info" class="comment-info"><span class="comment-age">(12 Oct '14, 10:39)</span> <span class="comment-user userinfo">DarrenWright</span></div></div><span id="36989"></span><div id="comment-36989" class="comment"><div id="post-36989-score" class="comment-score"></div><div class="comment-text"><p>If you get a core dump on Linux, please install a debugger, get a stack trace, and report a bug on <a href="http://bugs.wireshark.org">the Wireshark Bugzilla</a>. Wireshark is <em>not</em> supposed to crash (other than "running out of memory", and it'd be nice if we could handle <em>that</em> better), so a crash due to a profile copied from another machine is a bug and needs to be fixed.</p></div><div id="comment-36989-info" class="comment-info"><span class="comment-age">(12 Oct '14, 14:35)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="37117"></span><div id="comment-37117" class="comment"><div id="post-37117-score" class="comment-score"></div><div class="comment-text"><p>Core Dump.. naja not sure about that, it just disappears and I have to restart it. I will run it through tomorrow and see if I can get a trace. Unfortunately I am not exactly the Linux expert so it may not go stunningly well :D</p></div><div id="comment-37117-info" class="comment-info"><span class="comment-age">(16 Oct '14, 12:14)</span> <span class="comment-user userinfo">DarrenWright</span></div></div></div><div id="comment-tools-36982" class="comment-tools"></div><div class="clear"></div><div id="comment-36982-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36988"></span>

<div id="answer-container-36988" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36988-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36988-score" class="post-score" title="current number of votes">1</div><span id="post-36988-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="DarrenWright has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You need to convert all the files in the profiles folder using dos2unix Regards Matthias</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Oct '14, 14:28</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-36988" class="comments-container"></div><div id="comment-tools-36988" class="comment-tools"></div><div class="clear"></div><div id="comment-36988-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

