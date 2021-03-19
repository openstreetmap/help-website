+++
type = "question"
title = "Login &amp; Authenticating Issue"
description = '''A desktop application is authenticating from my PC to a server over the internet  with username &amp;amp; password. I always get the message that says &quot;Authorization Failed. Please check email and password values.&quot;. Now the vendor is saying it is my  software firewall that s causing this to which I disa...'''
date = "2011-02-05T07:21:00Z"
lastmod = "2011-02-06T05:32:00Z"
weight = 2166
keywords = [ "authenticating", "login", "logon", "http", "httpconnect" ]
aliases = [ "/questions/2166" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Login & Authenticating Issue](/questions/2166/login-authenticating-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2166-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2166-score" class="post-score" title="current number of votes">0</div><span id="post-2166-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>A desktop application is authenticating from my PC to a server over the internet with username &amp; password. I always get the message that says "Authorization Failed. Please check email and password values.". Now the vendor is saying it is my software firewall that s causing this to which I disagree, as other services are running perfectly on my machine. How can I use Wireshark to troubleshoot and find this out?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-authenticating" rel="tag" title="see questions tagged &#39;authenticating&#39;">authenticating</span> <span class="post-tag tag-link-login" rel="tag" title="see questions tagged &#39;login&#39;">login</span> <span class="post-tag tag-link-logon" rel="tag" title="see questions tagged &#39;logon&#39;">logon</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-httpconnect" rel="tag" title="see questions tagged &#39;httpconnect&#39;">httpconnect</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Feb '11, 07:21</strong></p><img src="https://secure.gravatar.com/avatar/62ec4e0e4cdd8f09b723ffc6d8feb139?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alexander%20Haynes&#39;s gravatar image" /><p><span>Alexander Ha...</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alexander Haynes has no accepted answers">0%</span></p></div></div><div id="comments-container-2166" class="comments-container"></div><div id="comment-tools-2166" class="comment-tools"></div><div class="clear"></div><div id="comment-2166-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2167"></span>

<div id="answer-container-2167" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2167-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2167-score" class="post-score" title="current number of votes">0</div><span id="post-2167-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Alexander Haynes has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I doubt it's your software firewall, but you never know. You can use Wireshark to capture the network data your PC is sending. Best would be from a second PC as a passive/neutral recording device if possible, but if you can't do that you can try with Wireshark on the affected PC as well. I'd consider disabling the software firewall as well, but that is only advisable if the PC is not directly connected to the internet (for example, if there is a router, too).</p><p>You need to identify the TCP flow that carries the authentication process. A good way to do that is to find out the IP addresses of client and server (you can use nslookup to get the one for the server if you know the dns name, and ipconfig/ifconfig for your PC), and then using the conversation statistics to find all flows that match. "Follow TCP stream" can help if you have a clear text protocol asking for authentication; otherwise it is a little difficult to find the login data.</p><p>Ususally you'll see your PC being asked for the login details and after it sends it you'll get a result. If you see that (login credentals as well as the authentication failure result) you know that the vendor is wrong. If you don't see the authentication details and results you have a local problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '11, 11:42</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2167" class="comments-container"><span id="2169"></span><div id="comment-2169" class="comment"><div id="post-2169-score" class="comment-score"></div><div class="comment-text"><p>I think you may have a great answer.</p><p>Since I am a bit new to Wireshark is it possible to do some screenshots or a video and post on either dropbox.com (screenshots) or screencast.com (video)?</p></div><div id="comment-2169-info" class="comment-info"><span class="comment-age">(05 Feb '11, 15:00)</span> <span class="comment-user userinfo">Alexander Ha...</span></div></div><span id="2173"></span><div id="comment-2173" class="comment"><div id="post-2173-score" class="comment-score">1</div><div class="comment-text"><p>Just had a quick look here, http://www.youtube.com/watch?v=NHLTa29iovU , and it seems to good screencast intro for using Wireshark to capture web browser traffic.</p></div><div id="comment-2173-info" class="comment-info"><span class="comment-age">(05 Feb '11, 16:37)</span> <span class="comment-user userinfo">martyvis</span></div></div><span id="2176"></span><div id="comment-2176" class="comment"><div id="post-2176-score" class="comment-score"></div><div class="comment-text"><p>Thx martyvis, good find. It's a good intro to start with and should give the right ideas. Alexander, let us know if you need further help.</p></div><div id="comment-2176-info" class="comment-info"><span class="comment-age">(06 Feb '11, 05:32)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-2167" class="comment-tools"></div><div class="clear"></div><div id="comment-2167-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

