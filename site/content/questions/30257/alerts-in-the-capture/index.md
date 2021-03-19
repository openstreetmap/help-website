+++
type = "question"
title = "Alerts in the capture"
description = '''I have a capture of a website called www.mir3.com  And the users are complaining that the application Is running slow, in the capture i see a lot of application alerts and  Encryptions alerts. Can someone shed some light on this issue for me please, can that application TTL (ALERTS) cause a website ...'''
date = "2014-02-27T20:34:00Z"
lastmod = "2014-03-04T19:22:00Z"
weight = 30257
keywords = [ "issues", "alert" ]
aliases = [ "/questions/30257" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Alerts in the capture](/questions/30257/alerts-in-the-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30257-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30257-score" class="post-score" title="current number of votes">0</div><span id="post-30257-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a capture of a website called www.mir3.com And the users are complaining that the application Is running slow, in the capture i see a lot of application alerts and Encryptions alerts.</p><p>Can someone shed some light on this issue for me please, can that application TTL (ALERTS) cause a website perform poorly? T Users are used to 12s second delay, now they say it takes about I 15-20sec to go from one page to another or simply to open a page.</p><p>I have a provide a copy or the www.mir3.com capture if that will help thanks in advance</p><p><a href="https://www.cloudshark.org/captures/040e6dbaeddc">https://www.cloudshark.org/captures/040e6dbaeddc</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-issues" rel="tag" title="see questions tagged &#39;issues&#39;">issues</span> <span class="post-tag tag-link-alert" rel="tag" title="see questions tagged &#39;alert&#39;">alert</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Feb '14, 20:34</strong></p><img src="https://secure.gravatar.com/avatar/530b55f3fcb17b760aabdf113d9318aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ejohnson7&#39;s gravatar image" /><p><span>ejohnson7</span><br />
<span class="score" title="11 reputation points">11</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ejohnson7 has no accepted answers">0%</span></p></div></div><div id="comments-container-30257" class="comments-container"></div><div id="comment-tools-30257" class="comment-tools"></div><div class="clear"></div><div id="comment-30257-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="30316"></span>

<div id="answer-container-30316" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30316-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30316-score" class="post-score" title="current number of votes">1</div><span id="post-30316-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ejohnson7 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are two flavours of TLS alerts in this trace.</p><ul><li>Alert (Level: Warning, Description: Unrecognized Name)</li><li>Encrypted Alert</li></ul><p>The Encrypted Alerts are normal to see before a SSL session comes down. They contain an encrypted Close_Notify that flows when the server issued a <a href="https://www.openssl.org/docs/ssl/SSL_shutdown.html">SSL-Shutdown</a>.</p><p>The TLS alerts indicating that an "Unrecognized Name" was received in the ClientHello are certainly not helping to speed up things here. The Client Hello includes server_name extension wih a TLS Server Name of aig.mir3.com which the server doesn't like.</p><p>I don't think however that those are the only reason for the poor performance of the web server as they do not delay the session that much.<br />
</p><p>I started a https session from my firefox to aig.mir3.com to see the behaviour of the site without a proxy and the response times are not very impressing there either. Also here the Client Hello contained Warning Alerts in all sessions. Shift-Ctrl-Q shows the following Statistics: <img src="https://osqa-ask.wireshark.org/upfiles/Selection_041.png" alt="alt text" /><br />
So telling from the colours in the time line , this looks like a server problem to me <img src="https://osqa-ask.wireshark.org/upfiles/Selection_042.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '14, 23:12</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Mar '14, 22:44</strong> </span></p></div></div><div id="comments-container-30316" class="comments-container"><span id="30336"></span><div id="comment-30336" class="comment"><div id="post-30336-score" class="comment-score"></div><div class="comment-text"><p>So do you think it is an issue with the server because the network is fine from what I can see or is it the client?</p></div><div id="comment-30336-info" class="comment-info"><span class="comment-age">(02 Mar '14, 21:12)</span> <span class="comment-user userinfo">ejohnson7</span></div></div><span id="30367"></span><div id="comment-30367" class="comment"><div id="post-30367-score" class="comment-score"></div><div class="comment-text"><p>go to <a href="https://www.mir3.com/">https://www.mir3.com/</a> and click on any of the links (Products, Contact us, whatever) and you'll get</p><pre><code>Not Found

The requested URL /intelligent-notification/ was not found on this server.
Apache/2.2.15 (CentOS) Server at www.mir3.com Port 443</code></pre><p>I guess the 'intelligent' notification did not work for their own server ;-))</p><p>Looks like they have some problems with their tech equipment. So, it could be the server(s) or the network/environment where the servers are located!</p></div><div id="comment-30367-info" class="comment-info"><span class="comment-age">(03 Mar '14, 15:35)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="30377"></span><div id="comment-30377" class="comment"><div id="post-30377-score" class="comment-score"></div><div class="comment-text"><p>Thanks so much Kurt that really help me out a lot What type of analyzer are you using, that could help me out big-time Once again thanks</p></div><div id="comment-30377-info" class="comment-info"><span class="comment-age">(03 Mar '14, 20:14)</span> <span class="comment-user userinfo">ejohnson7</span></div></div><span id="30381"></span><div id="comment-30381" class="comment"><div id="post-30381-score" class="comment-score"></div><div class="comment-text"><p>Kurt you think the google safebrowsing has somthing to do with the slow response just a thought</p></div><div id="comment-30381-info" class="comment-info"><span class="comment-age">(03 Mar '14, 21:44)</span> <span class="comment-user userinfo">ejohnson7</span></div></div><span id="30382"></span><div id="comment-30382" class="comment"><div id="post-30382-score" class="comment-score"></div><div class="comment-text"><blockquote><p>What type of analyzer are you using,</p></blockquote><p>It's called: Good old Brain 1.0. ;-)</p><p>I don't think safebrowsing has an effect here.</p></div><div id="comment-30382-info" class="comment-info"><span class="comment-age">(03 Mar '14, 22:45)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="30396"></span><div id="comment-30396" class="comment not_top_scorer"><div id="post-30396-score" class="comment-score"></div><div class="comment-text"><p>you serious GOOD old Brain really :-)</p></div><div id="comment-30396-info" class="comment-info"><span class="comment-age">(04 Mar '14, 07:42)</span> <span class="comment-user userinfo">ejohnson7</span></div></div></div><div id="comment-tools-30316" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-30316-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30426"></span>

<div id="answer-container-30426" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30426-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30426-score" class="post-score" title="current number of votes">0</div><span id="post-30426-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I need to find a goid analyze</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Mar '14, 19:22</strong></p><img src="https://secure.gravatar.com/avatar/530b55f3fcb17b760aabdf113d9318aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ejohnson7&#39;s gravatar image" /><p><span>ejohnson7</span><br />
<span class="score" title="11 reputation points">11</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ejohnson7 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-30426" class="comments-container"></div><div id="comment-tools-30426" class="comment-tools"></div><div class="clear"></div><div id="comment-30426-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

