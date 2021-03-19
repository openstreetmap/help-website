+++
type = "question"
title = "Capturing a password from a printer using SMB"
description = '''Hi I&#x27;m trying to capture a password from a Utax printer/scanner, The account on the printer/scanner has a username , password and path to where the file should be scanned to on a server. I&#x27;ve set up a session on wireshark and added host 192.168.16.89 (ip address of scanner) and then did a few scans,...'''
date = "2011-02-10T02:25:00Z"
lastmod = "2011-02-10T02:33:00Z"
weight = 2265
keywords = [ "utax", "scanner", "smb" ]
aliases = [ "/questions/2265" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing a password from a printer using SMB](/questions/2265/capturing-a-password-from-a-printer-using-smb)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2265-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2265-score" class="post-score" title="current number of votes">0</div><span id="post-2265-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I'm trying to capture a password from a Utax printer/scanner, The account on the printer/scanner has a username , password and path to where the file should be scanned to on a server. I've set up a session on wireshark and added host 192.168.16.89 (ip address of scanner) and then did a few scans, but i can't seem to pick up any info from the printer. Should wireshark be able to catch a username and password from it, i'm not sure if the password is encrypted or plain text</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-utax" rel="tag" title="see questions tagged &#39;utax&#39;">utax</span> <span class="post-tag tag-link-scanner" rel="tag" title="see questions tagged &#39;scanner&#39;">scanner</span> <span class="post-tag tag-link-smb" rel="tag" title="see questions tagged &#39;smb&#39;">smb</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '11, 02:25</strong></p><img src="https://secure.gravatar.com/avatar/79aa90304fb9602e0a6f34cd023add67?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="okee&#39;s gravatar image" /><p><span>okee</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="okee has no accepted answers">0%</span></p></div></div><div id="comments-container-2265" class="comments-container"></div><div id="comment-tools-2265" class="comment-tools"></div><div class="clear"></div><div id="comment-2265-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2267"></span>

<div id="answer-container-2267" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2267-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2267-score" class="post-score" title="current number of votes">1</div><span id="post-2267-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I would assume, that user/pass are sent using LM or NTLM hashes</p><p>You can try filtering for smb2.cmd == 1 which will show Session Setup packets fpr SMB2 or alternatively</p><p>smb.cmd == 0x73 for Session Setup under SMB(1)</p><p>For cracking those hashes, google for yourself on howto do that if neccessary. This is not part of this forum's question range in my opinion.</p><p>Regards</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '11, 02:33</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p><span>Landi</span><br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div></div><div id="comments-container-2267" class="comments-container"></div><div id="comment-tools-2267" class="comment-tools"></div><div class="clear"></div><div id="comment-2267-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

