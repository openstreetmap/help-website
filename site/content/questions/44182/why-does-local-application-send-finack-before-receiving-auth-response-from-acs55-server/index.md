+++
type = "question"
title = "Why Does Local Application Send FIN/ACK Before Receiving Auth Response From ACS5.5 Server?"
description = '''I&#x27;m wondering why the local application appears to be closing the tcp session before receiving the authentication response. I&#x27;ve run pcaps on multiple points in the network and getting the same results. The DSView(local) app sends a FIN/ACK but no trace of a FIN being sent. DSView application initia...'''
date = "2015-07-15T11:25:00Z"
lastmod = "2015-07-15T11:25:00Z"
weight = 44182
keywords = [ "finack", "time_wait", "tcp" ]
aliases = [ "/questions/44182" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why Does Local Application Send FIN/ACK Before Receiving Auth Response From ACS5.5 Server?](/questions/44182/why-does-local-application-send-finack-before-receiving-auth-response-from-acs55-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44182-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44182-score" class="post-score" title="current number of votes">0</div><span id="post-44182-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm wondering why the local application appears to be closing the tcp session before receiving the authentication response. I've run pcaps on multiple points in the network and getting the same results. The DSView(local) app sends a FIN/ACK but no trace of a FIN being sent. DSView application initiates the connection, makes the query for authentication and then after the ACS server ACKs, DSView sends a FIN/ACK, subsequently the ACS server sends the authentication response, but, the session is closed and TACACS authentication fails for the DSView application.</p><p>This is the result of a netstat from the DSview server immediately after attempting to authenticate: TCP 10.65.0.95:52685 10.65.12.12:49 TIME_WAIT</p><p>I've contacted the vendor and have yet to receive any feedback. It doesn't appear to be an issue inside our network.</p><p>Thank you in advance for your thoughts on this scenario</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-finack" rel="tag" title="see questions tagged &#39;finack&#39;">finack</span> <span class="post-tag tag-link-time_wait" rel="tag" title="see questions tagged &#39;time_wait&#39;">time_wait</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '15, 11:25</strong></p><img src="https://secure.gravatar.com/avatar/c313558b3ce8ceb18b82b937bb983793?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mduck2217&#39;s gravatar image" /><p><span>mduck2217</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mduck2217 has no accepted answers">0%</span></p></div></div><div id="comments-container-44182" class="comments-container"></div><div id="comment-tools-44182" class="comment-tools"></div><div class="clear"></div><div id="comment-44182-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

