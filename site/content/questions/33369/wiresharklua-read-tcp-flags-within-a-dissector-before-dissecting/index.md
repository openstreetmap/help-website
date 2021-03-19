+++
type = "question"
title = "Wireshark=&gt;LUA=&gt; Read TCP flags within a dissector before dissecting?"
description = '''Hi there, I am trying to write a script for reassembing the application segments. When PSH flag is not set, write the the current buffer to a file, and display proper message to user to scroll to next packet. When the user reaches the last TCP ssegment, the PSH flag would be set, append this buf to ...'''
date = "2014-06-04T00:33:00Z"
lastmod = "2014-06-04T00:33:00Z"
weight = 33369
keywords = [ "tcpflags" ]
aliases = [ "/questions/33369" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark=&gt;LUA=&gt; Read TCP flags within a dissector before dissecting?](/questions/33369/wiresharklua-read-tcp-flags-within-a-dissector-before-dissecting)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33369-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33369-score" class="post-score" title="current number of votes">0</div><span id="post-33369-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there, I am trying to write a script for reassembing the application segments.</p><p>When PSH flag is not set, write the the current buffer to a file, and display proper message to user to scroll to next packet.</p><p>When the user reaches the last TCP ssegment, the PSH flag would be set, append this buf to the file and call the regular dissector function to user with proper tree for app specific data.</p><p>Please help me to achieve this task.</p><p>Thank you in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcpflags" rel="tag" title="see questions tagged &#39;tcpflags&#39;">tcpflags</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jun '14, 00:33</strong></p><img src="https://secure.gravatar.com/avatar/bf6c503d201b5a1c5818150736c5405f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="testcoder&#39;s gravatar image" /><p><span>testcoder</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="testcoder has no accepted answers">0%</span></p></div></div><div id="comments-container-33369" class="comments-container"></div><div id="comment-tools-33369" class="comment-tools"></div><div class="clear"></div><div id="comment-33369-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

