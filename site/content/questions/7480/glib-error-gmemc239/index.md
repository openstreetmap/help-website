+++
type = "question"
title = "GLib-ERROR **: gmem.c:239"
description = '''At monitoring of interfaces (use multiple files) the size of a file 200МB. Through time there is an error: GLib-ERROR **: gmem.c:239: failed to allocate 8388608 bytes. Email: alexander.kurtukov@services.nsn.com'''
date = "2011-11-17T03:43:00Z"
lastmod = "2012-07-11T02:05:00Z"
weight = 7480
keywords = [ "failed", "allocate", "to" ]
aliases = [ "/questions/7480" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [GLib-ERROR \*\*: gmem.c:239](/questions/7480/glib-error-gmemc239)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7480-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7480-score" class="post-score" title="current number of votes">0</div><span id="post-7480-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>At monitoring of interfaces (use multiple files) the size of a file 200МB. Through time there is an error: GLib-ERROR **: gmem.c:239: failed to allocate 8388608 bytes. Email: <span class="__cf_email__" data-cfemail="afcec3cad7cec1cbcadd81c4dadddbdac4c0d9efdccaddd9c6cccadc81c1dcc181ccc0c2">[email protected]</span></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-failed" rel="tag" title="see questions tagged &#39;failed&#39;">failed</span> <span class="post-tag tag-link-allocate" rel="tag" title="see questions tagged &#39;allocate&#39;">allocate</span> <span class="post-tag tag-link-to" rel="tag" title="see questions tagged &#39;to&#39;">to</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '11, 03:43</strong></p><img src="https://secure.gravatar.com/avatar/3c51c7809256aeb6bd6a42d09ff0c2d0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amrel&#39;s gravatar image" /><p><span>Amrel</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amrel has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Nov '11, 09:44</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-7480" class="comments-container"></div><div id="comment-tools-7480" class="comment-tools"></div><div class="clear"></div><div id="comment-7480-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7491"></span>

<div id="answer-container-7491" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7491-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7491-score" class="post-score" title="current number of votes">0</div><span id="post-7491-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>On 32-bit platforms, the address space size limits the amount of memory Wireshark can allocate; on all platforms, the amount of swap space (swap partition or partitions, pagefiles/swap files, etc.) limits it. On large files, Wireshark can run out of memory; see <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">KnownBugs/OutOfMemory on the Wireshark Wiki</a> for information on this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '11, 09:48</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-7491" class="comments-container"><span id="12593"></span><div id="comment-12593" class="comment"><div id="post-12593-score" class="comment-score"></div><div class="comment-text"><p>Wireshark crashes showing the following error message "GLib Error**: gmem.c.230: failed to allocate 256 bytes" and then Wireshark is displaying Visual C++ error message. Is this the same problem?</p><p>Manohar, Trainer, <a href="http://www.joera.in">http://www.joera.in</a></p></div><div id="comment-12593-info" class="comment-info"><span class="comment-age">(11 Jul '12, 01:57)</span> <span class="comment-user userinfo">joera</span></div></div><span id="12594"></span><div id="comment-12594" class="comment"><div id="post-12594-score" class="comment-score"></div><div class="comment-text"><p>It could be the same problem.</p></div><div id="comment-12594-info" class="comment-info"><span class="comment-age">(11 Jul '12, 02:05)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-7491" class="comment-tools"></div><div class="clear"></div><div id="comment-7491-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

