+++
type = "question"
title = "SMB troubleshooting: CreateOptions in SMB CreateAndx request"
description = '''While accessing a folder in a share, the CreateOptions field in the SMB CREATE ANDX request has value of 64(0x00000040) i.e the Non directory bit is set.  The response has NT Status: STATUS_SUCCESS (0x00000000) with &#x27;file attribute&#x27; having the Directory bit as set. So, is CreateOptions used only whe...'''
date = "2015-03-16T23:52:00Z"
lastmod = "2015-03-24T14:08:00Z"
weight = 40628
keywords = [ "network", "smb", "cifs" ]
aliases = [ "/questions/40628" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SMB troubleshooting: CreateOptions in SMB CreateAndx request](/questions/40628/smb-troubleshooting-createoptions-in-smb-createandx-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40628-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40628-score" class="post-score" title="current number of votes">0</div><span id="post-40628-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>While accessing a folder in a share, the CreateOptions field in the SMB CREATE ANDX request has value of 64(0x00000040) i.e the Non directory bit is set. The response has NT Status: STATUS_SUCCESS (0x00000000) with 'file attribute' having the Directory bit as set.</p><p>So, is CreateOptions used only when a file/directory is being created and not when its opened?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span> <span class="post-tag tag-link-smb" rel="tag" title="see questions tagged &#39;smb&#39;">smb</span> <span class="post-tag tag-link-cifs" rel="tag" title="see questions tagged &#39;cifs&#39;">cifs</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Mar '15, 23:52</strong></p><img src="https://secure.gravatar.com/avatar/bc1e7422b9e06f3c3d9d6f68a870c202?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xerocool&#39;s gravatar image" /><p><span>xerocool</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xerocool has no accepted answers">0%</span></p></div></div><div id="comments-container-40628" class="comments-container"></div><div id="comment-tools-40628" class="comment-tools"></div><div class="clear"></div><div id="comment-40628-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40821"></span>

<div id="answer-container-40821" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40821-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40821-score" class="post-score" title="current number of votes">0</div><span id="post-40821-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Not really a Wireshark question, but if I think about it logically, there can not be a directory and file with the same name in one directory, so when opening a file with a certain name with the field set or not would still point to the same file, it is the response that is important. As it is by then that it is known whether the directory entry points to a file or directory.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Mar '15, 14:08</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-40821" class="comments-container"></div><div id="comment-tools-40821" class="comment-tools"></div><div class="clear"></div><div id="comment-40821-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

