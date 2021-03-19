+++
type = "question"
title = "url not working over site to site vpn"
description = '''we have site to site VPN office located at remote site and users accessing particular url from the office is getting request timedout.please help.'''
date = "2014-07-22T12:16:00Z"
lastmod = "2014-07-26T22:52:00Z"
weight = 34833
keywords = [ "vpn" ]
aliases = [ "/questions/34833" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [url not working over site to site vpn](/questions/34833/url-not-working-over-site-to-site-vpn)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34833-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>we have site to site VPN office located at remote site and users accessing particular url from the office is getting request timedout.please help.</p></div><div id="question-tags" class="tags-container tags">vpn</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jul '14, 12:16</strong></p><img src="https://secure.gravatar.com/avatar/8bbc1ee2b230a283a07ed85c0a7f8819?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kalyan&#39;s gravatar image" /><p>kalyan<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kalyan has no accepted answers">0%</span></p></div></div><div id="comments-container-34833" class="comments-container"><span id="34834"></span><div id="comment-34834" class="comment"><div id="post-34834-score" class="comment-score"></div><div class="comment-text"><p>i have added capture below</p></div><div id="comment-34834-info" class="comment-info"><span class="comment-age">(22 Jul '14, 12:29)</span> kalyan</div></div><span id="34841"></span><div id="comment-34841" class="comment"><div id="post-34841-score" class="comment-score"></div><div class="comment-text"><p>please post the capture file on google drive, dropbox or cloudshark.org and post the link here.</p></div><div id="comment-34841-info" class="comment-info"><span class="comment-age">(23 Jul '14, 00:23)</span> Kurt Knochner ♦</div></div><span id="34846"></span><div id="comment-34846" class="comment"><div id="post-34846-score" class="comment-score"></div><div class="comment-text"><p>source and destination ip address respectively 172.25.2.107 &amp;10.128.121.23 and the url which get stuck at initial screen as below</p><p><a href="http://ellipsis.i3global.net/timetracking/home.asp">http://ellipsis.i3global.net/timetracking/home.asp</a></p><p>Link to capture files</p><p><a href="https://www.dropbox.com/s/rrt1n7ps3ffd2x9/capture.zip">https://www.dropbox.com/s/rrt1n7ps3ffd2x9/capture.zip</a></p></div><div id="comment-34846-info" class="comment-info"><span class="comment-age">(23 Jul '14, 04:37)</span> kalyan</div></div><span id="34864"></span><div id="comment-34864" class="comment"><div id="post-34864-score" class="comment-score"></div><div class="comment-text"><p>could you please add a description for the three files in the ZIP?</p></div><div id="comment-34864-info" class="comment-info"><span class="comment-age">(23 Jul '14, 16:33)</span> Kurt Knochner ♦</div></div><span id="34867"></span><div id="comment-34867" class="comment"><div id="post-34867-score" class="comment-score"></div><div class="comment-text"><p>I could see that there is riverbed involved in this traffic flow and your netscreen device is stripping riverbed probes(Looking at NOP fields) which is essential for optimisation.I also see HTTP 404 unauthorised "access is denied to invalid credentials" error.</p></div><div id="comment-34867-info" class="comment-info"><span class="comment-age">(24 Jul '14, 00:37)</span> kishan pandey</div></div><span id="34873"></span><div id="comment-34873" class="comment not_top_scorer"><div id="post-34873-score" class="comment-score"></div><div class="comment-text"><p>could you please add a description for the three files in the ZIP?</p><p>Hi Kurt, all the files are captured from same user machine who cannot access the url but during different time stamps.</p><p>Thank You.</p></div><div id="comment-34873-info" class="comment-info"><span class="comment-age">(24 Jul '14, 04:22)</span> kalyan</div></div><span id="34874"></span><div id="comment-34874" class="comment not_top_scorer"><div id="post-34874-score" class="comment-score"></div><div class="comment-text"><p>Hi kishan ,</p><p>You are right there is a netscreen device and Riverbed device and the LAN is behind RB ,do you recommend any changes on netscreen device ?please suggest.</p><p>Thank You.</p></div><div id="comment-34874-info" class="comment-info"><span class="comment-age">(24 Jul '14, 04:26)</span> kalyan</div></div><span id="34876"></span><div id="comment-34876" class="comment not_top_scorer"><div id="post-34876-score" class="comment-score"></div><div class="comment-text"><p>Are you sure he is providing proper credentials/access rights because 404 error is suggesting that and to give detailed answer need capture from server end as well secondly can you provide capture from riverbed(both lan and wan interfaces).</p></div><div id="comment-34876-info" class="comment-info"><span class="comment-age">(24 Jul '14, 05:27)</span> kishan pandey</div></div></div><div id="comment-tools-34833" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-34833-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34928"></span>

<div id="answer-container-34928" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34928-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The problem might be due to Windows client not offering a MSS option in the 3-way handshake. The largest segment sent and received by the client is 536 bytes. This might break the optimizaiton logic in RB. Here is one example from your traces at <a href="https://www.cloudshark.org/captures/57ac844677dd">www.cloudshark.org</a></p><p>It looks like your large 'POST' requests never made it to the http server.</p><p>This problem was already discussed in thread <a href="http://ask.wireshark.org/questions/20917/tcp-mss-not-advertised-win2k8-r2-capture">tcp-mss-not-advertised-win2k8-r2-capture</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '14, 22:52</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Jul '14, 23:41</p></div></div><div id="comments-container-34928" class="comments-container"></div><div id="comment-tools-34928" class="comment-tools"></div><div class="clear"></div><div id="comment-34928-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

