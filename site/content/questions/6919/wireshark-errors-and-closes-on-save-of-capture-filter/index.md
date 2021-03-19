+++
type = "question"
title = "Wireshark errors and closes on save of capture filter?"
description = '''Running v1.6.2 - often when I &quot;save as&quot; a capture to my WindowsXP workstations, I get an error saying that Wireshark has encountered an error and has to close. The file appears to be saved intact but there is no &quot;recollection&quot; by Wireshark in the recent files list.  I have never encountered this wit...'''
date = "2011-10-17T06:12:00Z"
lastmod = "2011-10-17T07:45:00Z"
weight = 6919
keywords = [ "save", "error" ]
aliases = [ "/questions/6919" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark errors and closes on save of capture filter?](/questions/6919/wireshark-errors-and-closes-on-save-of-capture-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6919-score" class="post-score" title="current number of votes">0</div><span id="post-6919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Running v1.6.2 - often when I "save as" a capture to my WindowsXP workstations, I get an error saying that Wireshark has encountered an error and has to close. The file appears to be saved intact but there is no "recollection" by Wireshark in the recent files list.</p><p>I have never encountered this with previous versions of Wireshark. Has anyone else had this problem, and if so is there a solution or work-around?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-save" rel="tag" title="see questions tagged &#39;save&#39;">save</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Oct '11, 06:12</strong></p><img src="https://secure.gravatar.com/avatar/f79f7a1a3ae3d1a2cf23a74f3756c7ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BobD8487&#39;s gravatar image" /><p><span>BobD8487</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BobD8487 has no accepted answers">0%</span></p></div></div><div id="comments-container-6919" class="comments-container"></div><div id="comment-tools-6919" class="comment-tools"></div><div class="clear"></div><div id="comment-6919-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6926"></span>

<div id="answer-container-6926" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6926-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6926-score" class="post-score" title="current number of votes">0</div><span id="post-6926-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=1710">Bug 1710</a>? To be solved in 1.6.3.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '11, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6926" class="comments-container"><span id="6927"></span><div id="comment-6927" class="comment"><div id="post-6927-score" class="comment-score"></div><div class="comment-text"><p>I'm not sure this is the same problem as reported by Bug 1710. The capture is not live in my case. I run a capture, stop it, then attempt to save the capture file using "save as". I give it a filename and click Save, then Windows generates the error (not Wireshark) saying Wireshark has encountered an error and has to close. It then affords me the opportunity to send a report to Microsoft.</p></div><div id="comment-6927-info" class="comment-info"><span class="comment-age">(17 Oct '11, 07:45)</span> <span class="comment-user userinfo">BobD8487</span></div></div></div><div id="comment-tools-6926" class="comment-tools"></div><div class="clear"></div><div id="comment-6926-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

