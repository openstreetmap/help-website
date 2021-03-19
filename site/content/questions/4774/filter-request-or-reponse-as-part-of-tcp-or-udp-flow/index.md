+++
type = "question"
title = "Filter Request or Reponse as part of TCP or UDP Flow"
description = '''I have a large trace which only contains Radius Traffic (but could apply to any type of traffic) and would like to do a TCP / UDP filter such as filtering out radius Traffic using the following Analysis filter: radius.User_Name == &quot;UserID&quot; But I would also like to get the responses I get back from t...'''
date = "2011-06-27T14:57:00Z"
lastmod = "2011-06-27T16:55:00Z"
weight = 4774
keywords = [ "display-filter" ]
aliases = [ "/questions/4774" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Filter Request or Reponse as part of TCP or UDP Flow](/questions/4774/filter-request-or-reponse-as-part-of-tcp-or-udp-flow)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4774-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a large trace which only contains Radius Traffic (but could apply to any type of traffic) and<br />
would like to do a TCP / UDP filter such as filtering out radius Traffic using the following Analysis filter:</p><p>radius.User_Name == "UserID"</p><p>But I would also like to get the responses I get back from the destination server. Something like:</p><p>radius.User_Name == "UserID" and response</p><p>Would be exactly what I would be looking for to filter on.</p><p>This would be an extremely useful feature to be able to filter either on the source or destination flows such as being able to do:</p><p>radius.code == 3 and request</p><p>Or</p><p>http.response.code == 404 and request</p><p>So that way you could take a trace of all http traffic, and then filter on any 404 error messages you got, plus then also grab the request that was being made.</p><p>How difficult would this be to add into the analysis filter?</p></div><div id="question-tags" class="tags-container tags">display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jun '11, 14:57</strong></p><img src="https://secure.gravatar.com/avatar/784452c1e428cf9961e703e402cf666f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peter%20Lambrechtsen&#39;s gravatar image" /><p>Peter Lambre...<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peter Lambrechtsen has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>retagged 27 Jun '11, 19:11</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-4774" class="comments-container"></div><div id="comment-tools-4774" class="comment-tools"></div><div class="clear"></div><div id="comment-4774-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4777"></span>

<div id="answer-container-4777" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4777-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I've answered my own question.</p><p>Using MATE: http://wiki.wireshark.org/Mate/Examples#using_RADIUS_to_filter_SMTP_traffic_of_a_specific_user</p><p>This can do the matching of the source and destination traffic and we can filter on that.</p><p>mate.radius_ses.username == "UserName"</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '11, 16:55</strong></p><img src="https://secure.gravatar.com/avatar/784452c1e428cf9961e703e402cf666f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peter%20Lambrechtsen&#39;s gravatar image" /><p>Peter Lambre...<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peter Lambrechtsen has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Jun '11, 17:05</p></div></div><div id="comments-container-4777" class="comments-container"></div><div id="comment-tools-4777" class="comment-tools"></div><div class="clear"></div><div id="comment-4777-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

