+++
type = "question"
title = "Post a solution"
description = '''Like a tab &quot;Ask a question&quot; we have here there should be one more available with &quot;Post a solution&quot; like i am doing today with my troubleshooting experience with wirehsark,which otherwise would have been very difficult to solve.The issue i&#x27;m mentioning was going on from more than a month and it took ...'''
date = "2013-05-20T09:59:00Z"
lastmod = "2013-05-20T11:38:00Z"
weight = 21320
keywords = [ "troubleshooting" ]
aliases = [ "/questions/21320" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Post a solution](/questions/21320/post-a-solution)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21320-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21320-score" class="post-score" title="current number of votes">0</div><span id="post-21320-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Like a tab "Ask a question" we have here there should be one more available with "Post a solution" like i am doing today with my troubleshooting experience with wirehsark,which otherwise would have been very difficult to solve.The issue i'm mentioning was going on from more than a month and it took less than some 2 hourse to solve with wireshark, Few days back i got an issue where we have 2 servers behind netscaler loadbalancer and they were working fine but the moment the user was adding 3rd server all request to that server was getting rejected(as per application log on that 3rd server).Then we started capturing traffic on both server and Loadbalancer simultaneously,and found that when a client is intiating a request to loadbalancer virtual ip, it was getting forwarded to that3rd app server with destination mac say "b"(app server mac) but what odd we found on loadbalancer capture was while replying servers mac was different than what the request was sent on(ideally it should be "b" but it was showing "c").While checking server network config we found that it was configured with dual stack (both ipv4 &amp; ipv6 add) and that mac address was associated with ipv6 address.(actually ipv6 was enabled due to autoconfiguration).After some googling i found that "When the destination host can understand either protocol, IPv6 should be the preferred protocol. If the attempt at IPv6 fails, then IPv4 will be used instead. Dual stack hosts query DNS servers for both A records and AAAA records (AAAA should be preferred).</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-troubleshooting" rel="tag" title="see questions tagged &#39;troubleshooting&#39;">troubleshooting</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 May '13, 09:59</strong></p><img src="https://secure.gravatar.com/avatar/6f9cdab5081b4272d1abf703a2689372?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kishan%20pandey&#39;s gravatar image" /><p><span>kishan pandey</span><br />
<span class="score" title="221 reputation points">221</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kishan pandey has 2 accepted answers">28%</span></p></div></div><div id="comments-container-21320" class="comments-container"><span id="21321"></span><div id="comment-21321" class="comment"><div id="post-21321-score" class="comment-score"></div><div class="comment-text"><p>After removing ipv6 config it started working fine.</p></div><div id="comment-21321-info" class="comment-info"><span class="comment-age">(20 May '13, 10:02)</span> <span class="comment-user userinfo">kishan pandey</span></div></div><span id="21322"></span><div id="comment-21322" class="comment"><div id="post-21322-score" class="comment-score"></div><div class="comment-text"><p>Well, it's called a "question and answer" site, so....</p><p>Presumably "a solution" is a solution to "a problem"; if you have a problem <em>and</em> its solution, you could post the problem first, as a question, and immediately afterwards post the solution, as an answer. (Yes, you are allowed to answer your own question!)</p><p>So what you should do here is cut the "solution" part out of the question (use the "edit" item) and post it as an answer.</p></div><div id="comment-21322-info" class="comment-info"><span class="comment-age">(20 May '13, 10:26)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="21324"></span><div id="comment-21324" class="comment"><div id="post-21324-score" class="comment-score"></div><div class="comment-text"><p>and don't forget to adjust the title and the tags of the question.</p></div><div id="comment-21324-info" class="comment-info"><span class="comment-age">(20 May '13, 11:38)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-21320" class="comment-tools"></div><div class="clear"></div><div id="comment-21320-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

