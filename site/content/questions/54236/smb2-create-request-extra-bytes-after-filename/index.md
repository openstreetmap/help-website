+++
type = "question"
title = "SMB2 Create request: Extra bytes after Filename"
description = '''Hi, I&#x27;m trying to develop a snort rule that identifies exact filenames in a SMB2 Create Request. This can be anything from &quot;1&quot; to something like &quot;thisfile.exe&quot;. Although it&#x27;s easy to place a pointer at the beginning of the filename buffer, so you can start searching a regex from that point forward, ...'''
date = "2016-07-22T05:36:00Z"
lastmod = "2016-07-22T05:59:00Z"
weight = 54236
keywords = [ "smb2" ]
aliases = [ "/questions/54236" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SMB2 Create request: Extra bytes after Filename](/questions/54236/smb2-create-request-extra-bytes-after-filename)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54236-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54236-score" class="post-score" title="current number of votes">0</div><span id="post-54236-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm trying to develop a snort rule that identifies exact filenames in a SMB2 Create Request. This can be anything from "1" to something like "thisfile.exe". Although it's easy to place a pointer at the beginning of the filename buffer, so you can start searching a regex from that point forward, it's a problem to find a boundary at the the end of the filename. I'm trying to match the beginning of the ExtraInfo buffer, but I've found a case where there seems to be a couple of bytes (|65 00| between after the filename and before the ExtraInfo, which wireshark doesn't recognize as part of the packet. I've searched the protocol definition and can't find anything about what these bytes can be. So, a couple of questions: 1) any idea what these bytes can be? 2) any tip on how to achieve a rule like this, that is able to match exactly a boundary after the filename, to use in a pcre expression?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-smb2" rel="tag" title="see questions tagged &#39;smb2&#39;">smb2</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jul '16, 05:36</strong></p><img src="https://secure.gravatar.com/avatar/0e9ef9ae5a9174369651d9cd86106a9f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BadlyDrawnBoy&#39;s gravatar image" /><p><span>BadlyDrawnBoy</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BadlyDrawnBoy has no accepted answers">0%</span></p></div></div><div id="comments-container-54236" class="comments-container"></div><div id="comment-tools-54236" class="comment-tools"></div><div class="clear"></div><div id="comment-54236-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54238"></span>

<div id="answer-container-54238" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54238-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54238-score" class="post-score" title="current number of votes">0</div><span id="post-54238-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This would be better posted to the <a href="https://www.snort.org/community">snort community</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '16, 05:59</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-54238" class="comments-container"></div><div id="comment-tools-54238" class="comment-tools"></div><div class="clear"></div><div id="comment-54238-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

