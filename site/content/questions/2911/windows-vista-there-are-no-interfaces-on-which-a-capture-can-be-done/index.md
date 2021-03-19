+++
type = "question"
title = "Windows Vista : There are no interfaces on which a capture can be done"
description = '''I got the follovwing matter under windows Vista with Wireshark 1.4.4 : &quot;There are no interfaces on which a capture can be done&quot; The computer has WinPcap 4.1.2 installed and i have admin rights and i have an ethernet device (i&#x27;m currently using it to post this message !)'''
date = "2011-03-17T15:05:00Z"
lastmod = "2011-03-17T19:49:00Z"
weight = 2911
keywords = [ "capture", "interfaces", "no", "wireshark", "error" ]
aliases = [ "/questions/2911" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Windows Vista : There are no interfaces on which a capture can be done](/questions/2911/windows-vista-there-are-no-interfaces-on-which-a-capture-can-be-done)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2911-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2911-score" class="post-score" title="current number of votes">0</div><span id="post-2911-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I got the follovwing matter under windows Vista with Wireshark 1.4.4 : "There are no interfaces on which a capture can be done"</p><p>The computer has WinPcap 4.1.2 installed and i have admin rights and i have an ethernet device (i'm currently using it to post this message !)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-interfaces" rel="tag" title="see questions tagged &#39;interfaces&#39;">interfaces</span> <span class="post-tag tag-link-no" rel="tag" title="see questions tagged &#39;no&#39;">no</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Mar '11, 15:05</strong></p><img src="https://secure.gravatar.com/avatar/1a0e0fa7336ebdd9af8edd238c8e1961?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="muird&#39;s gravatar image" /><p><span>muird</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="muird has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Mar '11, 15:05</strong> </span></p></div></div><div id="comments-container-2911" class="comments-container"></div><div id="comment-tools-2911" class="comment-tools"></div><div class="clear"></div><div id="comment-2911-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2919"></span>

<div id="answer-container-2919" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2919-score" class="post-score" title="current number of votes">0</div><span id="post-2919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>... i have admin rights and i have an ethernet device ...</p></blockquote><p>Please see http://wiki.wireshark.org/CaptureSetup/CapturePrivileges.</p><p>I suspect that you are running Wireshark without elevated privileges (which is the safest way). (This is the default unless you use "run as administrator" to start Wireshark (not recommended)).</p><p>I also suspect that the NPF (Winpcap) driver is not running.</p><p>As noted in the above link the NPF driver needs to be started/running before trying to use Wireshark without elevated privileges.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Mar '11, 19:49</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Mar '11, 19:51</strong> </span></p></div></div><div id="comments-container-2919" class="comments-container"></div><div id="comment-tools-2919" class="comment-tools"></div><div class="clear"></div><div id="comment-2919-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

