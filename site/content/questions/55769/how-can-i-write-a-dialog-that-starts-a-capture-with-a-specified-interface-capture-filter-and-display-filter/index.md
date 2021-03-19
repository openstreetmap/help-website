+++
type = "question"
title = "How can I write a dialog that starts a capture with a specified interface, capture filter, and display filter?"
description = '''I have added one button into wireshark using GTK2 APIs.(wireshark-1.10.1) When this button is pressed, pop-up dialog of capture + display filter appears to user. User selects capture filter, display filter and interface. Now, when OK button is pressed, the wireshark should start capturing with both ...'''
date = "2016-09-22T23:42:00Z"
lastmod = "2016-09-30T06:28:00Z"
weight = 55769
keywords = [ "capture", "gui" ]
aliases = [ "/questions/55769" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I write a dialog that starts a capture with a specified interface, capture filter, and display filter?](/questions/55769/how-can-i-write-a-dialog-that-starts-a-capture-with-a-specified-interface-capture-filter-and-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55769-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55769-score" class="post-score" title="current number of votes">0</div><span id="post-55769-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have added one button into wireshark using GTK2 APIs.(wireshark-1.10.1)</p><p>When this button is pressed, pop-up dialog of capture + display filter appears to user.</p><p>User selects capture filter, display filter and interface.</p><p>Now, when OK button is pressed, the wireshark should start capturing with both selected capture and display filters.</p><p>I have already developed GUI part.</p><p>I don't know how to fire action event when OK is pressed ? I mean how to start capturing with selected filter ?</p><p>Regards,</p><p>Mehul</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-gui" rel="tag" title="see questions tagged &#39;gui&#39;">gui</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Sep '16, 23:42</strong></p><img src="https://secure.gravatar.com/avatar/fd87937fa1e60718c6ab880174ea3539?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mehul28&#39;s gravatar image" /><p><span>Mehul28</span><br />
<span class="score" title="0 reputation points">0</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mehul28 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>23 Sep '16, 01:46</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-55769" class="comments-container"></div><div id="comment-tools-55769" class="comment-tools"></div><div class="clear"></div><div id="comment-55769-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56015"></span>

<div id="answer-container-56015" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56015-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56015-score" class="post-score" title="current number of votes">0</div><span id="post-56015-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi,</p><p>I have gone through wireshark GTK code and done development of my requirement.</p><p>I have added a new button on GUI. Clicking on this button will open pop-up dialog box of interface, capture filter, and display filter. Selecting relevant parameters and clicking ok will start capture with selected capture + display filters.</p><p>Closing this thread.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '16, 06:28</strong></p><img src="https://secure.gravatar.com/avatar/fd87937fa1e60718c6ab880174ea3539?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mehul28&#39;s gravatar image" /><p><span>Mehul28</span><br />
<span class="score" title="0 reputation points">0</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mehul28 has no accepted answers">0%</span></p></div></div><div id="comments-container-56015" class="comments-container"></div><div id="comment-tools-56015" class="comment-tools"></div><div class="clear"></div><div id="comment-56015-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

