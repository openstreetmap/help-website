+++
type = "question"
title = "Can Wireshark monitor database request and response times?"
description = '''Hi All, I have an application written in &quot;Progress-4GL&quot;. It gets connected to Progress DB whenever a request is raised through the application. I want to do performance testing on this request response chain. Performance in the sense, if 10 users are accessing the DB then what will be the throughput...'''
date = "2013-03-14T21:45:00Z"
lastmod = "2013-03-15T02:21:00Z"
weight = 19524
keywords = [ "databaseperformance" ]
aliases = [ "/questions/19524" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can Wireshark monitor database request and response times?](/questions/19524/can-wireshark-monitor-database-request-and-response-times)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19524-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I have an application written in "Progress-4GL". It gets connected to Progress DB whenever a request is raised through the application. I want to do performance testing on this request response chain. Performance in the sense, if 10 users are accessing the DB then what will be the throughput. If the number of users is increased to 50 then what will be the throughput.</p><p>Can I do the the above performance testing using WireShark?</p></div><div id="question-tags" class="tags-container tags">databaseperformance</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '13, 21:45</strong></p><img src="https://secure.gravatar.com/avatar/4ffea5f26eb511f27e9790e9cc0f63d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jayanth&#39;s gravatar image" /><p>Jayanth<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jayanth has no accepted answers">0%</span></p></div></div><div id="comments-container-19524" class="comments-container"></div><div id="comment-tools-19524" class="comment-tools"></div><div class="clear"></div><div id="comment-19524-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19530"></span>

<div id="answer-container-19530" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19530-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sure, you can do that kind of testing with Wireshark. The only (small) problem is that I don't think Wireshark has decodes for Progress-4GL, so everything after the TCP layer will be more or less "unreadable". This means that you'll have to guess what the purpose of the packets are, if that is of any relevance in your test.</p><p>Usually you can try to do a time limited test of 10 users, having them all start at the same time doing something according to a test plan, and then go through all the statistics you need to see what happened. Conversation statistics, Summary statistics and I/O graph could be the most interesting ones. You could also test just one connection and base line that first, to see if it scales.</p><p>In my experience (I used to work for Progress Germany for a few years) most database transactions are pretty small when it comes to packet sizes, unless you're transferring huge tables worth of data in each connection. Database performance felt by the users is usually more depending on low latency connections than high bandwidth, so if I were you I'd also check how long certain user activities take to complete.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '13, 02:21</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-19530" class="comments-container"></div><div id="comment-tools-19530" class="comment-tools"></div><div class="clear"></div><div id="comment-19530-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

