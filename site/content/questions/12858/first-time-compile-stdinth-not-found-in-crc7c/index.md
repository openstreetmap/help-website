+++
type = "question"
title = "First time compile: stdint.h not found in crc7.c"
description = '''Hello i&#x27;m compiling for the 1st time wireshark. I&#x27;ve followed the Win32 related part on the developers guide. Check with the verify_tools : OK distclean: OK nmake .... setup OK nmake .... all : fails because in the crc7.c the compiler find a reference to stdint.h file not found. I&#x27;m using VS2008EE T...'''
date = "2012-07-19T06:23:00Z"
lastmod = "2012-07-22T09:41:00Z"
weight = 12858
keywords = [ "crc7.c", "stdint.h" ]
aliases = [ "/questions/12858" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [First time compile: stdint.h not found in crc7.c](/questions/12858/first-time-compile-stdinth-not-found-in-crc7c)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12858-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12858-score" class="post-score" title="current number of votes">0</div><span id="post-12858-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello i'm compiling for the 1st time wireshark. I've followed the Win32 related part on the developers guide.</p><p>Check with the verify_tools : OK distclean: OK nmake .... setup OK</p><p>nmake .... all : fails because in the crc7.c the compiler find a reference to stdint.h file not found.</p><p>I'm using VS2008EE</p><p>Thanks,</p><p>Paolo</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-crc7.c" rel="tag" title="see questions tagged &#39;crc7.c&#39;">crc7.c</span> <span class="post-tag tag-link-stdint.h" rel="tag" title="see questions tagged &#39;stdint.h&#39;">stdint.h</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jul '12, 06:23</strong></p><img src="https://secure.gravatar.com/avatar/b3d577c5e496a0b6df7bfd59ff666858?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="villanip&#39;s gravatar image" /><p><span>villanip</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="villanip has no accepted answers">0%</span></p></div></div><div id="comments-container-12858" class="comments-container"></div><div id="comment-tools-12858" class="comment-tools"></div><div class="clear"></div><div id="comment-12858-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12859"></span>

<div id="answer-container-12859" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12859-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12859-score" class="post-score" title="current number of votes">0</div><span id="post-12859-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>OK, googling i've found that the stdint.h header file is missing in the C:\Program Files\Microsoft Visual Studio 9.0\VC\include directory.</p><p>I've looked for a copy of the ISO stdint.h header file (it contains definitions for integer standard sizes and types) and i placed it in the C:\Program Files\Microsoft Visual Studio 9.0\VC\include</p><p>Compiled everithing again and it seems it work.</p><p>Regards,</p><p>Paolo</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '12, 07:23</strong></p><img src="https://secure.gravatar.com/avatar/b3d577c5e496a0b6df7bfd59ff666858?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="villanip&#39;s gravatar image" /><p><span>villanip</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="villanip has no accepted answers">0%</span></p></div></div><div id="comments-container-12859" class="comments-container"><span id="12860"></span><div id="comment-12860" class="comment"><div id="post-12860-score" class="comment-score"></div><div class="comment-text"><p>Removal of the not needed includes Committed revision 43830.</p></div><div id="comment-12860-info" class="comment-info"><span class="comment-age">(19 Jul '12, 08:05)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="12895"></span><div id="comment-12895" class="comment"><div id="post-12895-score" class="comment-score"></div><div class="comment-text"><p>thanks! I had the same problem too</p></div><div id="comment-12895-info" class="comment-info"><span class="comment-age">(21 Jul '12, 13:13)</span> <span class="comment-user userinfo">ybitz</span></div></div><span id="12898"></span><div id="comment-12898" class="comment"><div id="post-12898-score" class="comment-score"></div><div class="comment-text"><p>Anders - change 43830 removed the includes from crc7.c. In order to get my windows build to work I also removed those includes from crc7.h... I must be missing something.</p></div><div id="comment-12898-info" class="comment-info"><span class="comment-age">(22 Jul '12, 08:22)</span> <span class="comment-user userinfo">MartinM</span></div></div><span id="12899"></span><div id="comment-12899" class="comment"><div id="post-12899-score" class="comment-score"></div><div class="comment-text"><p>I think it was I who missed something ;-)</p></div><div id="comment-12899-info" class="comment-info"><span class="comment-age">(22 Jul '12, 09:41)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-12859" class="comment-tools"></div><div class="clear"></div><div id="comment-12859-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

