+++
type = "question"
title = "https client changing from TLSv1.2 to TLSv1 while loading webpage"
description = '''Analyzing a capture of an https client talking to a server (A10 load balancer in this case), where the client is experiencing an SSL timeout issue, and the site fails to load. This happens at a random interval, and appears dependent on the current load the A10 is handling. Looking at the capture, I ...'''
date = "2015-10-24T22:05:00Z"
lastmod = "2015-10-24T22:05:00Z"
weight = 46910
keywords = [ "tls", "sslv3" ]
aliases = [ "/questions/46910" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [https client changing from TLSv1.2 to TLSv1 while loading webpage](/questions/46910/https-client-changing-from-tlsv12-to-tlsv1-while-loading-webpage)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46910-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46910-score" class="post-score" title="current number of votes">0</div><span id="post-46910-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Analyzing a capture of an https client talking to a server (A10 load balancer in this case), where the client is experiencing an SSL timeout issue, and the site fails to load. This happens at a random interval, and appears dependent on the current load the A10 is handling.</p><p>Looking at the capture, I see the client, for no reason I can find, change from TLSv1.2, and then the next request is for TLSv1. It will pass data with TLSv1 for a few sessions, and then eventually the client tries to connect via SSLv3, and never receives a response from the server (and it's not supposed to). When the client switches to SSLv3 is when the website times out with an SSL error.</p><p>What causes the client to change the TLS version while communicating with the same website?<br />
</p><p>Could previous Secure Session information from the server be telling the client to build future sessions at a lower version?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tls" rel="tag" title="see questions tagged &#39;tls&#39;">tls</span> <span class="post-tag tag-link-sslv3" rel="tag" title="see questions tagged &#39;sslv3&#39;">sslv3</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Oct '15, 22:05</strong></p><img src="https://secure.gravatar.com/avatar/00046957707ae6b5433354401f11ccd0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bagurdes&#39;s gravatar image" /><p><span>Bagurdes</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bagurdes has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-46910" class="comments-container"></div><div id="comment-tools-46910" class="comment-tools"></div><div class="clear"></div><div id="comment-46910-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

