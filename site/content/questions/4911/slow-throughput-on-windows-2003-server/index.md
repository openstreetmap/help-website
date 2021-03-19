+++
type = "question"
title = "Slow throughput on Windows 2003 Server"
description = '''First, I am completely ignorant of all things wireshark, so please forgive me.  I have a windows 2003 that is slow when transferring files. I tested out another windows 2003 server that doesn&#x27;t exhibit the same issue. Here is one difference I found in wirehsark that may be the cause, but I really ha...'''
date = "2011-07-05T12:58:00Z"
lastmod = "2011-07-06T05:04:00Z"
weight = 4911
keywords = [ "windows", "2003", "smb" ]
aliases = [ "/questions/4911" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Slow throughput on Windows 2003 Server](/questions/4911/slow-throughput-on-windows-2003-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4911-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4911-score" class="post-score" title="current number of votes">0</div><span id="post-4911-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>First, I am completely ignorant of all things wireshark, so please forgive me.</p><p>I have a windows 2003 that is slow when transferring files. I tested out another windows 2003 server that doesn't exhibit the same issue. Here is one difference I found in wirehsark that may be the cause, but I really have no idea if it is or how to fix.</p><p>Slow Server: 163 0.000185 192.168.0.4 192.168.0.154 SMB 105 Write AndX Response, FID: 0x800e, 16580 bytes<br />
</p><p>Fast Server: 1974 0.000000 192.168.0.159 192.168.0.154 SMB 105 Write AndX Response, FID: 0x4000, 65536 bytes<br />
</p><p>There are tons of these entries (I assume that thats the file being written over the network. The different of course is the byte size of 16580 vs 65536.</p><p>Thanks in advance and let me know if you need more information.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-2003" rel="tag" title="see questions tagged &#39;2003&#39;">2003</span> <span class="post-tag tag-link-smb" rel="tag" title="see questions tagged &#39;smb&#39;">smb</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jul '11, 12:58</strong></p><img src="https://secure.gravatar.com/avatar/9e469f52ca136acc0d305ee8d35cd68b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thebigdog123&#39;s gravatar image" /><p><span>thebigdog123</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thebigdog123 has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-4911" class="comments-container"></div><div id="comment-tools-4911" class="comment-tools"></div><div class="clear"></div><div id="comment-4911-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4924"></span>

<div id="answer-container-4924" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4924-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4924-score" class="post-score" title="current number of votes">0</div><span id="post-4924-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Found my own answer! SMB signing was enabled, causing the max buffer to be ignored and reset to the default of 16580. I disabled SMB signing, and the throughput virtually quadrupled!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jul '11, 05:04</strong></p><img src="https://secure.gravatar.com/avatar/9e469f52ca136acc0d305ee8d35cd68b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thebigdog123&#39;s gravatar image" /><p><span>thebigdog123</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thebigdog123 has no accepted answers">0%</span></p></div></div><div id="comments-container-4924" class="comments-container"></div><div id="comment-tools-4924" class="comment-tools"></div><div class="clear"></div><div id="comment-4924-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

