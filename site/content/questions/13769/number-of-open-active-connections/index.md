+++
type = "question"
title = "Number of open (active) connections"
description = '''Hi all, Don&#x27;t eat me alive please, I&#x27;m a total noob to this area of computing. My ISP has informed me that his firewall resets a customer&#x27;s broadband if the customer opens more than 30 connections. This is to prevent file-sharing causing contention issues apparently. My problem is that I have no ide...'''
date = "2012-08-20T11:01:00Z"
lastmod = "2012-08-20T13:45:00Z"
weight = 13769
keywords = [ "connections", "active", "open" ]
aliases = [ "/questions/13769" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Number of open (active) connections](/questions/13769/number-of-open-active-connections)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13769-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, Don't eat me alive please, I'm a total noob to this area of computing. My ISP has informed me that his firewall resets a customer's broadband if the customer opens more than 30 connections. This is to prevent file-sharing causing contention issues apparently. My problem is that I have no idea how many connections the two PCs here at home have open (or active?) at any one time. He has told me to download WireShark and use it to find this information out. The problem is that I have no clue how to use WireShark and while I am trying to read up on it, some of the terminology is beyond me. So to my question: Can Wireshark show me how many connections I have open on both PCs here at home? (I don't need the total number of connections opened, I need the current number of open connections, and a min &amp; max number would be great also). If so, can you explain to me how to do it please? If you need further info please just ask. Thanks.</p></div><div id="question-tags" class="tags-container tags">connections active open</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Aug '12, 11:01</strong></p><img src="https://secure.gravatar.com/avatar/f69cc8dd6c16badc8af11ca7a528368b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="r011ingthunder&#39;s gravatar image" /><p>r011ingthunder<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="r011ingthunder has no accepted answers">0%</span></p></div></div><div id="comments-container-13769" class="comments-container"></div><div id="comment-tools-13769" class="comment-tools"></div><div class="clear"></div><div id="comment-13769-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13772"></span>

<div id="answer-container-13772" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13772-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>It might be possible to beat it into doing so, but it'd be difficult - you'd have to track TCP connection opens and closes. (I'm assuming here that "connections" refers to TCP connections.)</p><p>If you're willing to try the command line, the <code>netstat</code> command, on most if not all of the OSes running on PCs, may be the best tool to use. See <a href="http://en.wikipedia.org/wiki/Netstat">the Wikipedia page for it</a>.</p><p><code>netstat -p tcp</code> should, on most operating systems, including Windows, report all the "active" TCP connections. When I tried it on my Windows XP (virtual) machine, it listed some connections to "localhost", which are connections from the machine to itself rather than to a machine on the Internet, so not all of the connections it lists will necessarily count against the 30-connection limit (ignore the ones that mention "localhost").</p><p><code>netstat -sp tcp</code> will, at least on Windows, list connection statistics; on my XP machine, it has a "Current Connections" count (which would probably include "localhost" connections), but has no "maximum number of connections that have ever been open simultaneously" count (the minimum would probably be 0 on most if not all machines, given that, when the machine boots, it has no connections open, so that's probably not a useful number).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '12, 13:45</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Aug '12, 13:46</p></div></div><div id="comments-container-13772" class="comments-container"><span id="13776"></span><div id="comment-13776" class="comment"><div id="post-13776-score" class="comment-score"></div><div class="comment-text"><p>Thanks! The <strong>netstat -sp tcp</strong> does exactly what I want. It doesn't give a running total unfortunately, but I can keep trying it at peak times on both machines. Just from initial viewings it would seem I'm nowhere near the 30 limit. Is it normal for ISPs to throttle broadband that way? Oh and yes, of course a minimum number would be useless, sorry about that! Thanks again. For info above works on Vista too.</p></div><div id="comment-13776-info" class="comment-info"><span class="comment-age">(20 Aug '12, 14:50)</span> r011ingthunder</div></div></div><div id="comment-tools-13772" class="comment-tools"></div><div class="clear"></div><div id="comment-13772-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

