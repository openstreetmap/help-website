+++
type = "question"
title = "TCP Flow-control questions that drives me mad."
description = '''Hi,  This is a capture of a TCP session when I was downloading 10Mb file from an FTP server. The server is has an ICW of 10x MSS, so this means that the server can initially send 10 segments without receiving an ACK from the client.  Being said that, every two segments has been ACKed in real-time, a...'''
date = "2016-09-26T05:33:00Z"
lastmod = "2016-09-26T05:33:00Z"
weight = 55830
keywords = [ "follow.tcp.stream" ]
aliases = [ "/questions/55830" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Flow-control questions that drives me mad.](/questions/55830/tcp-flow-control-questions-that-drives-me-mad)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55830-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55830-score" class="post-score" title="current number of votes">0</div><span id="post-55830-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>This is a capture of a TCP session when I was downloading 10Mb file from an FTP server. The server is has an ICW of 10x MSS, so this means that the server can initially send 10 segments without receiving an ACK from the client.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/FLOWCONTROL1_Yw1UZNK.jpg" alt="alt text" /></p><p>Being said that, every two segments has been ACKed in real-time, and the server has sent all the 10 segments to the client that has already ACKed all the segments. Now, the server waited from 15:40:31:864 to 15:40:31:901 for more than 50ms until it begin sending new segments.</p><p>I wonder, why the sever has paused sending more segments, although all the segments have already been ACKed? I know that it waited for the RTO value, but why would the server do this when all the ACKs have received?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-follow.tcp.stream" rel="tag" title="see questions tagged &#39;follow.tcp.stream&#39;">follow.tcp.stream</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '16, 05:33</strong></p><img src="https://secure.gravatar.com/avatar/8f9c62b95c07a830b431475668d329bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mohmkamal&#39;s gravatar image" /><p><span>mohmkamal</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mohmkamal has no accepted answers">0%</span></p></img></div></div><div id="comments-container-55830" class="comments-container"></div><div id="comment-tools-55830" class="comment-tools"></div><div class="clear"></div><div id="comment-55830-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

