+++
type = "question"
title = "SMB2 stream being reset"
description = ''' Initiate file transfer between 2 Win2k8R2 servers (or windows 7) A TCP Stream, say Stream 0 is created and the file starts to transfer The Stream is reset A new stream is created, say stream 1, and the file copy picks up where it left off due to the more robust nature of SMB2 dialect 0x0210 and its...'''
date = "2014-02-28T12:30:00Z"
lastmod = "2014-02-28T22:58:00Z"
weight = 30285
keywords = [ "rst", "smb2", "stream" ]
aliases = [ "/questions/30285" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SMB2 stream being reset](/questions/30285/smb2-stream-being-reset)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30285-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30285-score" class="post-score" title="current number of votes">0</div><span id="post-30285-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><ol><li>Initiate file transfer between 2 Win2k8R2 servers (or windows 7)</li><li>A TCP Stream, say Stream 0 is created and the file starts to transfer</li><li>The Stream is reset</li><li>A new stream is created, say stream 1, and the file copy picks up where it left off due to the more robust nature of SMB2 dialect 0x0210 and its ability to recover from errors like a reset.</li><li>More of the file is copied and the current stream is reset</li><li>Repeat steps #4 &amp; #5 until file copy completes.</li></ol><p>This is a feature in this particular dialect and does not exist in previous versions of windows, hence why copying between servers that do not support 0x0210 fail and ones that do, work. So the $64 dollar question is, why are the streams being reset?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span> <span class="post-tag tag-link-smb2" rel="tag" title="see questions tagged &#39;smb2&#39;">smb2</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '14, 12:30</strong></p><img src="https://secure.gravatar.com/avatar/5d07ae33b7a45a3b422b2be2b70a88fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RTJ10&#39;s gravatar image" /><p><span>RTJ10</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RTJ10 has no accepted answers">0%</span></p></div></div><div id="comments-container-30285" class="comments-container"><span id="30303"></span><div id="comment-30303" class="comment"><div id="post-30303-score" class="comment-score"></div><div class="comment-text"><p>First question before the "why" is: Who is sending the reset? Is it the client or the server ore someone inbetween? Is it always the same amount of bytes that is getting through before the reset?</p><p>Without sample traces (on both client and server simultaneously) all we can do is just guess.</p></div><div id="comment-30303-info" class="comment-info"><span class="comment-age">(28 Feb '14, 22:58)</span> <span class="comment-user userinfo">mrEEde</span></div></div></div><div id="comment-tools-30285" class="comment-tools"></div><div class="clear"></div><div id="comment-30285-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

