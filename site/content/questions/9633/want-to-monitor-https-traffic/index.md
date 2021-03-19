+++
type = "question"
title = "Want to monitor https traffic."
description = '''hi, i would like to monitor the traffic on my client , to whome i have asked to open the fireall for port 55443 . the client is saying that it has opened the firewall port 55443, but my application is still failing . how can i check from the client side that my requests are comming to its server fro...'''
date = "2012-03-20T04:42:00Z"
lastmod = "2012-03-22T07:24:00Z"
weight = 9633
keywords = [ "55443" ]
aliases = [ "/questions/9633" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Want to monitor https traffic.](/questions/9633/want-to-monitor-https-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9633-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9633-score" class="post-score" title="current number of votes">0</div><span id="post-9633-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi,</p><p>i would like to monitor the traffic on my client , to whome i have asked to open the fireall for port 55443 .</p><p>the client is saying that it has opened the firewall port 55443, but my application is still failing . how can i check from the client side that my requests are comming to its server from my location from a forworded port 55443. I have checked wireshark on the client server but unable to find ant particular entry &amp; unable to find single 55443 hit in the capture.</p><p>How exactly can i check it ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-55443" rel="tag" title="see questions tagged &#39;55443&#39;">55443</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Mar '12, 04:42</strong></p><img src="https://secure.gravatar.com/avatar/b37f2a40f19b3eb483589d05f6180bc7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="paree&#39;s gravatar image" /><p><span>paree</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="paree has no accepted answers">0%</span></p></div></div><div id="comments-container-9633" class="comments-container"></div><div id="comment-tools-9633" class="comment-tools"></div><div class="clear"></div><div id="comment-9633-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9634"></span>

<div id="answer-container-9634" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9634-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9634-score" class="post-score" title="current number of votes">1</div><span id="post-9634-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could use a display filter like <strong>tcp.port==55443</strong>. If no packets are shown you know that there was no communication on that port (unless your capture strategy is flawed and the packets were there, bypassing your Wireshark - which should not be the case if you capture ON the server).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '12, 04:52</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-9634" class="comments-container"><span id="9635"></span><div id="comment-9635" class="comment"><div id="post-9635-score" class="comment-score"></div><div class="comment-text"><p>I have already tried tcp.port==55443 but it shows not a single packet is flowing and the client is saying that , he has opened the particular port . I am generated the traffic from my server to the ip of the client on port 55443 , but still no activity on wireshark installed on the client server.</p></div><div id="comment-9635-info" class="comment-info"><span class="comment-age">(20 Mar '12, 05:26)</span> <span class="comment-user userinfo">paree</span></div></div><span id="9636"></span><div id="comment-9636" class="comment"><div id="post-9636-score" class="comment-score">1</div><div class="comment-text"><p>Do you have multiple NICs? Maybe the traffic is bypassing the adapter you capture on... are you sure that the connection is established at all? You could do <strong>netstat -an</strong> on both client and server to check that.</p></div><div id="comment-9636-info" class="comment-info"><span class="comment-age">(20 Mar '12, 05:47)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="9698"></span><div id="comment-9698" class="comment"><div id="post-9698-score" class="comment-score"></div><div class="comment-text"><p>sorry the remote client is not available for testing ; i will update you in couple of days about the testings. Anyways thank you very much for the suggestions.</p></div><div id="comment-9698-info" class="comment-info"><span class="comment-age">(22 Mar '12, 07:24)</span> <span class="comment-user userinfo">paree</span></div></div></div><div id="comment-tools-9634" class="comment-tools"></div><div class="clear"></div><div id="comment-9634-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

