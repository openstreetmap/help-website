+++
type = "question"
title = "SMB Troubleshooting STATUS_LOCK_NOT_GRANTED"
description = '''Hi, I am just trying to troubleshoot some SMB Slowness, My Filter i&#x27;m running is smb2.nt_status &amp;gt; 0 or smb.nt_status &amp;gt; 0 and obviously we are getting some results. Locking AndX Response, FID: 0xc036, Error: STATUS_LOCK_NOT_GRANTED You get a couple of these and just wondering how you would trou...'''
date = "2014-11-13T04:56:00Z"
lastmod = "2014-11-14T00:59:00Z"
weight = 37818
keywords = [ "smb2", "smb", "troubleshooting" ]
aliases = [ "/questions/37818" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SMB Troubleshooting STATUS\_LOCK\_NOT\_GRANTED](/questions/37818/smb-troubleshooting-status_lock_not_granted)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37818-score" class="post-score" title="current number of votes">0</div><span id="post-37818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I am just trying to troubleshoot some SMB Slowness, My Filter i'm running is smb2.nt_status &gt; 0 or smb.nt_status &gt; 0 and obviously we are getting some results.</p><p>Locking AndX Response, FID: 0xc036, Error: STATUS_LOCK_NOT_GRANTED</p><p>You get a couple of these and just wondering how you would troubleshoot this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-smb2" rel="tag" title="see questions tagged &#39;smb2&#39;">smb2</span> <span class="post-tag tag-link-smb" rel="tag" title="see questions tagged &#39;smb&#39;">smb</span> <span class="post-tag tag-link-troubleshooting" rel="tag" title="see questions tagged &#39;troubleshooting&#39;">troubleshooting</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Nov '14, 04:56</strong></p><img src="https://secure.gravatar.com/avatar/0ee9adb52e8cd87b7d2b656b598a7cc5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlexYoungZ&#39;s gravatar image" /><p><span>AlexYoungZ</span><br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlexYoungZ has no accepted answers">0%</span></p></div></div><div id="comments-container-37818" class="comments-container"></div><div id="comment-tools-37818" class="comment-tools"></div><div class="clear"></div><div id="comment-37818-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37846"></span>

<div id="answer-container-37846" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37846-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37846-score" class="post-score" title="current number of votes">1</div><span id="post-37846-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not too good on SMB 1 but I'll give it a go. You'll need a trace of traffic in and out of the file server; a trace from the PC having the problem won't contain what you need.</p><p>The client is using a Locking AndX Request to attempt to lock a range of bytes in a file. It seems another client already has a lock on bytes within that range. Look at the file id value in the SMB header of the failing request. Wireshark should give you the name of the file. If it doesn't the trace probably wasn't started early enough. Wireshark will get the details when the file was opened with an NT Create AndX Request.</p><p>Do you expect many processes or clients to share that file?</p><p>To find who has a lock on the file, filter for Locking AndX Requests. Do you have other clients (identified by IP address and port number) locking against the same file? Note to check the file by name as the file id for an open file on one SMB session won't be the same as that on another.</p><p>If you need share information for the file, check the tree id value. Again Wireshark should give you the share name from the Tree Connect.</p><p>Best regards...Paul</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Nov '14, 15:38</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p><span>PaulOfford</span><br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-37846" class="comments-container"><span id="37853"></span><div id="comment-37853" class="comment"><div id="post-37853-score" class="comment-score"></div><div class="comment-text"><p>Brilliant thank you i'll give it a go</p></div><div id="comment-37853-info" class="comment-info"><span class="comment-age">(14 Nov '14, 00:59)</span> <span class="comment-user userinfo">AlexYoungZ</span></div></div></div><div id="comment-tools-37846" class="comment-tools"></div><div class="clear"></div><div id="comment-37846-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

