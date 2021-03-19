+++
type = "question"
title = "Slow responses between 2 servers"
description = '''Hi All, We have web server x that talks to domain controller y to authenticate a user constantly over a 2 hours period What we are finding is that like clockwork every 5 minutes we are getting high response times for a short period What I have also noticed is the trace is adding entries multiple tim...'''
date = "2016-12-06T07:00:00Z"
lastmod = "2016-12-13T07:24:00Z"
weight = 57901
keywords = [ "dup-ack", "retransmissions", "previous" ]
aliases = [ "/questions/57901" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Slow responses between 2 servers](/questions/57901/slow-responses-between-2-servers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57901-score" class="post-score" title="current number of votes">0</div><span id="post-57901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>We have web server <strong>x</strong> that talks to domain controller <strong>y</strong> to authenticate a user constantly over a 2 hours period What we are finding is that like clockwork every 5 minutes we are getting high response times for a short period</p><p>What I have also noticed is the trace is adding entries multiple times a second but when I notice the lag there are time gaps within wireshark until it passes</p><p>I ran wireshark on both servers and around the time we get a lot of TCP errors on the DC side</p><p>What is the best way to upload the trace, its a TXT file</p><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dup-ack" rel="tag" title="see questions tagged &#39;dup-ack&#39;">dup-ack</span> <span class="post-tag tag-link-retransmissions" rel="tag" title="see questions tagged &#39;retransmissions&#39;">retransmissions</span> <span class="post-tag tag-link-previous" rel="tag" title="see questions tagged &#39;previous&#39;">previous</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Dec '16, 07:00</strong></p><img src="https://secure.gravatar.com/avatar/3387b00b609b80c0568bfc516f1c0208?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="foowish&#39;s gravatar image" /><p><span>foowish</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="foowish has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Dec '16, 07:02</strong> </span></p></div></div><div id="comments-container-57901" class="comments-container"><span id="57902"></span><div id="comment-57902" class="comment"><div id="post-57902-score" class="comment-score"></div><div class="comment-text"><p>Much prefer a Wireshark capture file, either pcap or pcapng at a file sharing service, e.g. <a href="https://cloudshark.org">CloudShark</a>, Google Drive, Dropbox etc.</p></div><div id="comment-57902-info" class="comment-info"><span class="comment-age">(06 Dec '16, 07:14)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="57903"></span><div id="comment-57903" class="comment"><div id="post-57903-score" class="comment-score"></div><div class="comment-text"><p>Hi thanks for the response. I can upload but I need to omit all ip address information for security reasons</p></div><div id="comment-57903-info" class="comment-info"><span class="comment-age">(06 Dec '16, 07:16)</span> <span class="comment-user userinfo">foowish</span></div></div><span id="57904"></span><div id="comment-57904" class="comment"><div id="post-57904-score" class="comment-score"></div><div class="comment-text"><p>Then see <a href="https://www.tracewrangler.com/">TraceWrangler</a> that can anonymise captures.</p></div><div id="comment-57904-info" class="comment-info"><span class="comment-age">(06 Dec '16, 07:19)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="57907"></span><div id="comment-57907" class="comment"><div id="post-57907-score" class="comment-score"></div><div class="comment-text"><p>Thanks Graham ive upload it using the following link</p><p><a href="https://drive.google.com/open?id=0B1EcZKOSIZVUelhka2RFejFRRTQ">https://drive.google.com/open?id=0B1EcZKOSIZVUelhka2RFejFRRTQ</a></p></div><div id="comment-57907-info" class="comment-info"><span class="comment-age">(06 Dec '16, 07:51)</span> <span class="comment-user userinfo">foowish</span></div></div><span id="57910"></span><div id="comment-57910" class="comment"><div id="post-57910-score" class="comment-score"></div><div class="comment-text"><p>It is not much worth from my point of view. Segemntation offload is enabled. We can´t see what really happens at the network.</p></div><div id="comment-57910-info" class="comment-info"><span class="comment-age">(06 Dec '16, 12:04)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="57920"></span><div id="comment-57920" class="comment not_top_scorer"><div id="post-57920-score" class="comment-score"></div><div class="comment-text"><p>What do you suggest I do to get a better capture. I can run my script to reproduce the lag at 5 minute intervals</p><p>Really stuck on this issue Help is definitely appreciated</p></div><div id="comment-57920-info" class="comment-info"><span class="comment-age">(07 Dec '16, 00:48)</span> <span class="comment-user userinfo">foowish</span></div></div><span id="57923"></span><div id="comment-57923" class="comment not_top_scorer"><div id="post-57923-score" class="comment-score"></div><div class="comment-text"><p>Either capture elsewhere than the client, e.g. a switch span or mirror port or a tap, or turn off segmentation offload on the capture system.</p></div><div id="comment-57923-info" class="comment-info"><span class="comment-age">(07 Dec '16, 02:38)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="57956"></span><div id="comment-57956" class="comment not_top_scorer"><div id="post-57956-score" class="comment-score"></div><div class="comment-text"><p>This is a very poor quality capture. The sniffer dropped 680KB of packets or around 85%. Further, it is only 20 secs long. If I were capturing, I'd try to collect equal times of "good" and "bad" behaviours.</p></div><div id="comment-57956-info" class="comment-info"><span class="comment-age">(08 Dec '16, 04:08)</span> <span class="comment-user userinfo">Philst</span></div></div><span id="57958"></span><div id="comment-57958" class="comment not_top_scorer"><div id="post-57958-score" class="comment-score"></div><div class="comment-text"><p>Hi, thanks for the reply. I think I'm closer. I ran a trace on one of the affected destination addresses and around the time of the lag we have a couple of SQL servers hammering out DC....then we notice TCP gets messed up with unack packets retransmits etc so it's like it's doing a DOS attack. Now I need to work out what is going on on these source addresses. There does seem to be a pattern</p></div><div id="comment-57958-info" class="comment-info"><span class="comment-age">(08 Dec '16, 04:19)</span> <span class="comment-user userinfo">foowish</span></div></div></div><div id="comment-tools-57901" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-57901-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58047"></span>

<div id="answer-container-58047" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58047-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58047-score" class="post-score" title="current number of votes">0</div><span id="post-58047-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi worked out what it was in the end. Was our monitoring service hammering LDAP queries at our dc</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Dec '16, 07:24</strong></p><img src="https://secure.gravatar.com/avatar/3387b00b609b80c0568bfc516f1c0208?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="foowish&#39;s gravatar image" /><p><span>foowish</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="foowish has no accepted answers">0%</span></p></div></div><div id="comments-container-58047" class="comments-container"></div><div id="comment-tools-58047" class="comment-tools"></div><div class="clear"></div><div id="comment-58047-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

