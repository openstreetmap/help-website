+++
type = "question"
title = "t-shark throwing error message:CaptureChild-WARNING"
description = '''Hi all, I tried executing the command tshark -qz hosts to retrieve all the IPtoHOST pertaining to a particular web click. I got the information i am looking for and at the same time i am seeing following error message: (tshark.exe:1204): CaptureChild-WARNING : sync_pipe_stop: forcing child to exit**...'''
date = "2013-03-15T22:36:00Z"
lastmod = "2013-03-18T00:25:00Z"
weight = 19552
keywords = [ "tshark" ]
aliases = [ "/questions/19552" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [t-shark throwing error message:CaptureChild-WARNING](/questions/19552/t-shark-throwing-error-messagecapturechild-warning)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19552-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19552-score" class="post-score" title="current number of votes">0</div><span id="post-19552-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>I tried executing the command tshark -qz hosts to retrieve all the IPtoHOST pertaining to a particular web click.</p><p>I got the information i am looking for and at the same time i am seeing following error message:</p><p><strong>(tshark.exe:1204): CaptureChild-WARNING</strong> : sync_pipe_stop: forcing child to exit**</p><p>If possible please let me know the reason behind this error message.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Mar '13, 22:36</strong></p><img src="https://secure.gravatar.com/avatar/2b038237e64839261fcc88e9fdef2b68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krishnayeddula&#39;s gravatar image" /><p><span>krishnayeddula</span><br />
<span class="score" title="629 reputation points">629</span><span title="35 badges"><span class="badge1">●</span><span class="badgecount">35</span></span><span title="41 badges"><span class="silver">●</span><span class="badgecount">41</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krishnayeddula has 3 accepted answers">6%</span></p></div></div><div id="comments-container-19552" class="comments-container"></div><div id="comment-tools-19552" class="comment-tools"></div><div class="clear"></div><div id="comment-19552-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19553"></span>

<div id="answer-container-19553" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19553-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19553-score" class="post-score" title="current number of votes">0</div><span id="post-19553-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Looking at <a href="http://anonsvn.wireshark.org/viewvc/trunk-1.8/capture_sync.c?revision=43286&amp;view=markup">the source code</a>, this message is generated when tshark (on Windows) tried to terminate the capture process gracefully, but failed within 500ms and therefor tshark terminates the capture process the hard way and logs this message.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Mar '13, 01:37</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-19553" class="comments-container"><span id="19603"></span><div id="comment-19603" class="comment"><div id="post-19603-score" class="comment-score"></div><div class="comment-text"><p>SYN-bit,thanks for the reply.This message is happening at the middle of the output which is little distracting.Will logging a bug makes sense?</p></div><div id="comment-19603-info" class="comment-info"><span class="comment-age">(17 Mar '13, 22:32)</span> <span class="comment-user userinfo">krishnayeddula</span></div></div><span id="19605"></span><div id="comment-19605" class="comment"><div id="post-19605-score" class="comment-score"></div><div class="comment-text"><p>What was your complete tshark command? And could it be that tshark ran out of memory while capturing? How long was tshark capturing and what was the bandwidth on the interface?</p></div><div id="comment-19605-info" class="comment-info"><span class="comment-age">(18 Mar '13, 00:25)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-19553" class="comment-tools"></div><div class="clear"></div><div id="comment-19553-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

