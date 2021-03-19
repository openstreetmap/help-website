+++
type = "question"
title = "TCP Window value"
description = '''Hi All, I am having difficulties getting the TCP Window value using below: struct tcp_analysis *tcpd=NULL; tcpd=get_tcp_conversation_data(conversation,pinfo); tcpd-&amp;gt;stream - This works as I get the stream index number tcpd-&amp;gt;fwd-&amp;gt;window or tcpd-&amp;gt;rev-&amp;gt;window - This comes back with -1 Is...'''
date = "2014-12-07T07:48:00Z"
lastmod = "2014-12-07T13:23:00Z"
weight = 38413
keywords = [ "tcpd" ]
aliases = [ "/questions/38413" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Window value](/questions/38413/tcp-window-value)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38413-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38413-score" class="post-score" title="current number of votes">0</div><span id="post-38413-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I am having difficulties getting the TCP Window value using below:</p><p>struct tcp_analysis *tcpd=NULL;</p><p>tcpd=get_tcp_conversation_data(conversation,pinfo);</p><p>tcpd-&gt;stream - This works as I get the stream index number</p><p>tcpd-&gt;fwd-&gt;window or tcpd-&gt;rev-&gt;window - This comes back with -1</p><p>Is the correct approach or am I doing something wrong?</p><p>Much appreciated.</p><p>Version 1.11.3 (SVN Rev 54962 from /trunk) Windows XP MS Visual C++ 10.0 build 40219</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcpd" rel="tag" title="see questions tagged &#39;tcpd&#39;">tcpd</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Dec '14, 07:48</strong></p><img src="https://secure.gravatar.com/avatar/df3883c2c65a6be2ba9d90d73edc7f13?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DennisVecchio&#39;s gravatar image" /><p><span>DennisVecchio</span><br />
<span class="score" title="36 reputation points">36</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DennisVecchio has one accepted answer">100%</span></p></div></div><div id="comments-container-38413" class="comments-container"></div><div id="comment-tools-38413" class="comment-tools"></div><div class="clear"></div><div id="comment-38413-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38421"></span>

<div id="answer-container-38421" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38421-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38421-score" class="post-score" title="current number of votes">0</div><span id="post-38421-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kurt Knochner has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I had 'analyze tcp sequence number' in tcp protocol preference disabled. I enabled it and all is good.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '14, 13:23</strong></p><img src="https://secure.gravatar.com/avatar/df3883c2c65a6be2ba9d90d73edc7f13?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DennisVecchio&#39;s gravatar image" /><p><span>DennisVecchio</span><br />
<span class="score" title="36 reputation points">36</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DennisVecchio has one accepted answer">100%</span> </br></p></div></div><div id="comments-container-38421" class="comments-container"></div><div id="comment-tools-38421" class="comment-tools"></div><div class="clear"></div><div id="comment-38421-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

