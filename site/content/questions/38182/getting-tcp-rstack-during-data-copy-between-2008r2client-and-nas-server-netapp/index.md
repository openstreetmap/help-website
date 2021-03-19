+++
type = "question"
title = "Getting TCP RST/ACK during data copy between 2008R2(Client) and NAS server (NetApp))"
description = '''I keep getting the &quot;network error&quot; on windows2008 trying to copy data from mounted T: (net use T: and this is NetApp CIFS share). There are Kiwi syslog and application accessing the T: share the similar way using service start up with authenticated user. While I was copying data from T: to local sys...'''
date = "2014-11-26T11:43:00Z"
lastmod = "2014-11-27T07:23:00Z"
weight = 38182
keywords = [ "rst+ack", "tcp", "wireshark" ]
aliases = [ "/questions/38182" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Getting TCP RST/ACK during data copy between 2008R2(Client) and NAS server (NetApp))](/questions/38182/getting-tcp-rstack-during-data-copy-between-2008r2client-and-nas-server-netapp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38182-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38182-score" class="post-score" title="current number of votes">0</div><span id="post-38182-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><img src="https://osqa-ask.wireshark.org/upfiles/Screen_Shot_2014-11-26_at_11.25.36_AM.png" alt="alt text" />I keep getting the "network error" on windows2008 trying to copy data from mounted T: (net use T: and this is NetApp CIFS share). There are Kiwi syslog and application accessing the T: share the similar way using service start up with authenticated user. While I was copying data from T: to local system or to remote host, I am getting network error saying "The network drive location no longer available". (This is just split of second, and T: still showing mounted after error occurred under windows explorer)</p><p>Any help will be much appreciated!!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rst+ack" rel="tag" title="see questions tagged &#39;rst+ack&#39;">rst+ack</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Nov '14, 11:43</strong></p><img src="https://secure.gravatar.com/avatar/f261b2f4dbf5e65968cbc31e8c8900aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vincenthlo&#39;s gravatar image" /><p><span>vincenthlo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vincenthlo has no accepted answers">0%</span></p></img></div></div><div id="comments-container-38182" class="comments-container"><span id="38207"></span><div id="comment-38207" class="comment"><div id="post-38207-score" class="comment-score"></div><div class="comment-text"><p>Not possible to comment anything without actual pcap file.</p></div><div id="comment-38207-info" class="comment-info"><span class="comment-age">(27 Nov '14, 04:56)</span> <span class="comment-user userinfo">kishan pandey</span></div></div></div><div id="comment-tools-38182" class="comment-tools"></div><div class="clear"></div><div id="comment-38182-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38210"></span>

<div id="answer-container-38210" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38210-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38210-score" class="post-score" title="current number of votes">0</div><span id="post-38210-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think that the reset is part of the new session in the picture, because the SYN is for port 1161. The reset is on port 1160, which issues a close request/response pair in the old session, so it looks okay to me. But it is hard to say where the problem is without a capture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '14, 07:23</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-38210" class="comments-container"></div><div id="comment-tools-38210" class="comment-tools"></div><div class="clear"></div><div id="comment-38210-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

