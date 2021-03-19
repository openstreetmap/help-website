+++
type = "question"
title = "Dumpcap memory issue in Linux"
description = '''When running dump cap with the -B option, in Linux (Dumpcap v1.8.10 on CentOS release 6.5), the allocated memory seems to be twice what it is requested, i.e. if I run  dumpcap -B 100 I see that 206684MB are allocated to dumpcap, i.e. output of  ps aux | grep dump cap is  root 7758 2.0 0.3 237384 206...'''
date = "2014-07-04T03:26:00Z"
lastmod = "2014-07-04T03:26:00Z"
weight = 34401
keywords = [ "memory", "dumpcap", "linux" ]
aliases = [ "/questions/34401" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Dumpcap memory issue in Linux](/questions/34401/dumpcap-memory-issue-in-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34401-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34401-score" class="post-score" title="current number of votes">0</div><span id="post-34401-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When running dump cap with the -B option, in Linux (Dumpcap v1.8.10 on CentOS release 6.5), the allocated memory seems to be twice what it is requested, i.e. if I run dumpcap -B 100 I see that 206684MB are allocated to dumpcap, i.e. output of ps aux | grep dump cap is root 7758 2.0 0.3 237384 206684 pts/0 S+ 11:05 0:00 dumpcap -B 100 This however does not seem to be the case for windows 7. Can anyone explain why this is so? Thanks, Nuno</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-memory" rel="tag" title="see questions tagged &#39;memory&#39;">memory</span> <span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jul '14, 03:26</strong></p><img src="https://secure.gravatar.com/avatar/43d5a8313f315b245c51ea9d4c22be94?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ncat&#39;s gravatar image" /><p><span>ncat</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ncat has no accepted answers">0%</span></p></div></div><div id="comments-container-34401" class="comments-container"></div><div id="comment-tools-34401" class="comment-tools"></div><div class="clear"></div><div id="comment-34401-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

