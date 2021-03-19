+++
type = "question"
title = "acking each tcp packet"
description = '''Hi Everyone, We have two unix(a &amp;amp; b) servers communicating with each other,basically &quot;a&quot; is application server who sends authentication request to server &quot;b&quot;.I can see that both are acking each packet with some data in it.This both servers are across different location and communicating through ...'''
date = "2013-08-22T02:22:00Z"
lastmod = "2013-08-23T05:28:00Z"
weight = 23944
keywords = [ "tcp" ]
aliases = [ "/questions/23944" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [acking each tcp packet](/questions/23944/acking-each-tcp-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23944-score" class="post-score" title="current number of votes">0</div><span id="post-23944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Everyone, We have two unix(a &amp; b) servers communicating with each other,basically "a" is application server who sends authentication request to server "b".I can see that both are acking each packet with some data in it.This both servers are across different location and communicating through wan link and due to this frequent ack behaviour it is taking long time to login.Any inputs please.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Aug '13, 02:22</strong></p><img src="https://secure.gravatar.com/avatar/6f9cdab5081b4272d1abf703a2689372?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kishan%20pandey&#39;s gravatar image" /><p><span>kishan pandey</span><br />
<span class="score" title="221 reputation points">221</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kishan pandey has 2 accepted answers">28%</span></p></div></div><div id="comments-container-23944" class="comments-container"></div><div id="comment-tools-23944" class="comment-tools"></div><div class="clear"></div><div id="comment-23944-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23976"></span>

<div id="answer-container-23976" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23976-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23976-score" class="post-score" title="current number of votes">0</div><span id="post-23976-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I can see that both are acking each packet with some data in it. due to this frequent ack behaviour it is taking long time to login</p></blockquote><p>" ... with some data in it" - So the client sends a request and gets a response back. And it takes some time (RTT) over the WAN. "... taking a long time to login" - assuming there is only 1 request per login, a single end user should not be waiting too long, <em>unless</em> those authentication requests (or their responses) are queueing up.</p><p>Looks like the (auth)-client is serializing all those requests and you suffer from the (longer) latency over the WAN. Maybe Nagle plays a role here also. But I think unless you can change to parallel requests sent to the server, latency will always play a dominant factor here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Aug '13, 05:28</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-23976" class="comments-container"></div><div id="comment-tools-23976" class="comment-tools"></div><div class="clear"></div><div id="comment-23976-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

