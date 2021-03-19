+++
type = "question"
title = "iscsi Read Capacity 16 allocation length"
description = '''In an iscsi packet for scsi command READ CAPACITY (16), if I try to enter any value greater than 0xFFFFF, i.e. 1677215, wireshark isnt able to differentiate the iscsi packet from the overlying tcp packet which carries it. And the input is fine because the allocation length field is 4 bytes long and ...'''
date = "2014-09-16T01:16:00Z"
lastmod = "2014-10-23T06:31:00Z"
weight = 36353
keywords = [ "capture", "iscsi", "tcp" ]
aliases = [ "/questions/36353" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [iscsi Read Capacity 16 allocation length](/questions/36353/iscsi-read-capacity-16-allocation-length)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36353-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36353-score" class="post-score" title="current number of votes">0</div><span id="post-36353-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In an iscsi packet for scsi command READ CAPACITY (16), if I try to enter any value greater than 0xFFFFF, i.e. 1677215, wireshark isnt able to differentiate the iscsi packet from the overlying tcp packet which carries it. And the input is fine because the allocation length field is 4 bytes long and thus can accept maximum value of 0xFFFFFFFF.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-iscsi" rel="tag" title="see questions tagged &#39;iscsi&#39;">iscsi</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Sep '14, 01:16</strong></p><img src="https://secure.gravatar.com/avatar/32416fa523a730d77ac92ca1a77cdf29?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GauravOjha&#39;s gravatar image" /><p><span>GauravOjha</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GauravOjha has no accepted answers">0%</span></p></div></div><div id="comments-container-36353" class="comments-container"><span id="37303"></span><div id="comment-37303" class="comment"><div id="post-37303-score" class="comment-score"></div><div class="comment-text"><p>Can you provide sample captures which show this behavior? If you're quite certain the behavior is not correct, you could always open a bug report.</p></div><div id="comment-37303-info" class="comment-info"><span class="comment-age">(23 Oct '14, 02:33)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-36353" class="comment-tools"></div><div class="clear"></div><div id="comment-36353-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37309"></span>

<div id="answer-container-37309" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37309-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37309-score" class="post-score" title="current number of votes">2</div><span id="post-37309-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Bill Meier has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>(This question should have gotten an answer indicating that it was reported as a bug and that the bug was subsequently fixed: See Bug <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10469">Wireshark Bug #10469</a> ).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Oct '14, 06:31</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Oct '14, 06:38</strong> </span></p></div></div><div id="comments-container-37309" class="comments-container"></div><div id="comment-tools-37309" class="comment-tools"></div><div class="clear"></div><div id="comment-37309-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

