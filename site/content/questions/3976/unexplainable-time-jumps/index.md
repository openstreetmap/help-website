+++
type = "question"
title = "unexplainable time jumps"
description = '''The sniff file has the right timestamp in the file name and on the OS after writing.  But in the sniff file ever 20 min. the time jump back. The OS has the right time. There is no NTP how change time or make trouble. Ideas?'''
date = "2011-05-06T05:46:00Z"
lastmod = "2011-07-29T08:06:00Z"
weight = 3976
keywords = [ "time" ]
aliases = [ "/questions/3976" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [unexplainable time jumps](/questions/3976/unexplainable-time-jumps)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3976-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3976-score" class="post-score" title="current number of votes">0</div><span id="post-3976-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The sniff file has the right timestamp in the file name and on the OS after writing. But in the sniff file ever 20 min. the time jump back. The OS has the right time. There is no NTP how change time or make trouble. Ideas?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 May '11, 05:46</strong></p><img src="https://secure.gravatar.com/avatar/e2a9cb2a37313a877072f0d2584fe1e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chofmann&#39;s gravatar image" /><p><span>chofmann</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chofmann has no accepted answers">0%</span></p></div></div><div id="comments-container-3976" class="comments-container"><span id="5361"></span><div id="comment-5361" class="comment"><div id="post-5361-score" class="comment-score"></div><div class="comment-text"><p>Do you know the hardware time source being used by the OS? The TSC time source with some CPU implementations is known to have unacceptable clock drift rates up in the OS...google "hardware time source tsc"</p></div><div id="comment-5361-info" class="comment-info"><span class="comment-age">(29 Jul '11, 08:06)</span> <span class="comment-user userinfo">ivanh</span></div></div></div><div id="comment-tools-3976" class="comment-tools"></div><div class="clear"></div><div id="comment-3976-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5359"></span>

<div id="answer-container-5359" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5359-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5359-score" class="post-score" title="current number of votes">0</div><span id="post-5359-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>-the DNS-Server work right<br />
-no NTP server installed<br />
-no other program is installed how use the winpcap library<br />
-OS time is right<br />
-latest wireshark and winpcap program is installed</p><p>Maybe its a winpcap bug.<br />
A new trace file created with "Mircosoft Network Monitor 3.3" on the same server has no time jumps.<br />
Under specific circumstances this phenomenon appears on a win server.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jul '11, 06:36</strong></p><img src="https://secure.gravatar.com/avatar/e2a9cb2a37313a877072f0d2584fe1e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chofmann&#39;s gravatar image" /><p><span>chofmann</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chofmann has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>29 Jul '11, 08:22</strong> </span></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p><span>joke</span><br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span></br></p></div></div><div id="comments-container-5359" class="comments-container"></div><div id="comment-tools-5359" class="comment-tools"></div><div class="clear"></div><div id="comment-5359-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

