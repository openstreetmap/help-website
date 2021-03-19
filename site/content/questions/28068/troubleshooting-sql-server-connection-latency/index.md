+++
type = "question"
title = "Troubleshooting SQL Server Connection Latency"
description = '''We have a web app that is connecting to a remote SQL Server DB and is experiencing performance issues. To narrow the culprit down, we ruled out the network from the client to the webserver (webapp) and we did a DB trace of a typical function in the web app where users were seeing delays of up to 1 m...'''
date = "2013-12-12T23:51:00Z"
lastmod = "2013-12-14T00:42:00Z"
weight = 28068
keywords = [ "application", "connection", "sql" ]
aliases = [ "/questions/28068" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Troubleshooting SQL Server Connection Latency](/questions/28068/troubleshooting-sql-server-connection-latency)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28068-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28068-score" class="post-score" title="current number of votes">0</div><span id="post-28068-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have a web app that is connecting to a remote SQL Server DB and is experiencing performance issues. To narrow the culprit down, we ruled out the network from the client to the webserver (webapp) and we did a DB trace of a typical function in the web app where users were seeing delays of up to 1 min -- and saw that the query only took 5 seconds once it was received by SQL Server.</p><p>This leaves the negotiation of the SQL Server connection itself. It's almost like it is trying to authenticate with the provided connection string but initially can't -- then it retries and eventually is successful and the transaction completes.</p><p>How can we use Wireshark to determine if this is indeed what's happening or if it's another kind of issue with establishing a connection to the DB?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-application" rel="tag" title="see questions tagged &#39;application&#39;">application</span> <span class="post-tag tag-link-connection" rel="tag" title="see questions tagged &#39;connection&#39;">connection</span> <span class="post-tag tag-link-sql" rel="tag" title="see questions tagged &#39;sql&#39;">sql</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Dec '13, 23:51</strong></p><img src="https://secure.gravatar.com/avatar/2cd1a9173d95b3ddebb0a94477495a10?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="idotta&#39;s gravatar image" /><p><span>idotta</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="idotta has no accepted answers">0%</span></p></div></div><div id="comments-container-28068" class="comments-container"></div><div id="comment-tools-28068" class="comment-tools"></div><div class="clear"></div><div id="comment-28068-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="28093"></span>

<div id="answer-container-28093" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28093-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28093-score" class="post-score" title="current number of votes">0</div><span id="post-28093-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What kind of negotiation is it that you're referring to? One way to confirm it on the wire would simply be to trace the traffic between the web/app server toward the database, and see how long it takes on the wire for that authentication to complete.</p><p>Ideally, you'd like to be able to get both the user to web/app server traffic and the web/app server to DB traffic in the same trace file, to see the whole call flow for a one-minute response to the user so that you can isolate what is taking so long. For example, does the query toward the DB take a minute after the user request to the web/app server (putting the blame on the web/app server in handling the request before talking to the DB), or is there a long one-minute authentication attempt takinig place between the web/app server and the DB (in which case, troubleshoot your authentication mechanism and application).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Dec '13, 21:58</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div></div><div id="comments-container-28093" class="comments-container"></div><div id="comment-tools-28093" class="comment-tools"></div><div class="clear"></div><div id="comment-28093-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28101"></span>

<div id="answer-container-28101" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28101-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28101-score" class="post-score" title="current number of votes">0</div><span id="post-28101-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'd start with an unfiltered trace on the DB server and see if there are any side steps like LDAP, reverse DNs lookups, CRL verifications etc ...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '13, 00:42</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-28101" class="comments-container"></div><div id="comment-tools-28101" class="comment-tools"></div><div class="clear"></div><div id="comment-28101-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

