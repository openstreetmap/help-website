+++
type = "question"
title = "Copying displayed fields"
description = '''Hello Sir, I want to copy displayed fields e.g. time and packet length only. I want to use only these fields for further processing of my dataset. How can I do that?'''
date = "2012-04-08T10:12:00Z"
lastmod = "2012-04-09T23:16:00Z"
weight = 10015
keywords = [ "copying" ]
aliases = [ "/questions/10015" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Copying displayed fields](/questions/10015/copying-displayed-fields)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10015-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10015-score" class="post-score" title="current number of votes">0</div><span id="post-10015-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello Sir, I want to copy displayed fields e.g. time and packet length only. I want to use only these fields for further processing of my dataset. How can I do that?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-copying" rel="tag" title="see questions tagged &#39;copying&#39;">copying</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '12, 10:12</strong></p><img src="https://secure.gravatar.com/avatar/d16ada886677bcc37d4c25438e63d15b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chandu85420&#39;s gravatar image" /><p><span>chandu85420</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chandu85420 has no accepted answers">0%</span></p></div></div><div id="comments-container-10015" class="comments-container"></div><div id="comment-tools-10015" class="comment-tools"></div><div class="clear"></div><div id="comment-10015-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10030"></span>

<div id="answer-container-10030" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10030-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10030-score" class="post-score" title="current number of votes">1</div><span id="post-10030-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have you looked at tshark, the command line version of Wireshark? Using the options <code>-T fields -e frame.time_epoch -e frame.len</code> gives you output of the form <code>1330082384.015475000    64</code> which is the frame time in seconds since the epoch (00:00:00 1/1/1970) and the length (on the wire) of the frame.</p><p>You can use any filterable fields with <code>-e</code>, in the GUI just click on the relevant part of the protocol in the packet tree and the field description and more importantly name, will be displayed in the status bar at the bottom left.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Apr '12, 05:43</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-10030" class="comments-container"><span id="10036"></span><div id="comment-10036" class="comment"><div id="post-10036-score" class="comment-score"></div><div class="comment-text"><p><img src="https://osqa-ask.wireshark.org/upfiles/capturefile.png" alt="alt text" /></p><p>Actually I want to copy field values as shown in the figure below. Timing at which packet was seen and length. My objective is to collect time and packet size only so that I can make dataset comprising these field value and nothing else. please help.</p></div><div id="comment-10036-info" class="comment-info"><span class="comment-age">(09 Apr '12, 23:16)</span> <span class="comment-user userinfo">chandu85420</span></div></div></div><div id="comment-tools-10030" class="comment-tools"></div><div class="clear"></div><div id="comment-10030-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

