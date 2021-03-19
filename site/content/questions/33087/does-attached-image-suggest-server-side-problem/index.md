+++
type = "question"
title = "Does attached Image suggest Server Side problem?"
description = '''Hi, I&#x27;m trying to troubleshoot a problem with slow response times when accessing our Internal Intranet web based apps. I&#x27;ve run a WS capture from my machine to the server. My PC is 172.27.10.19 Web Server - 10.44.145.171 I&#x27;ve followed the tcp stream and displayed the time as &quot;seconds since previous ...'''
date = "2014-05-26T08:25:00Z"
lastmod = "2014-05-26T10:32:00Z"
weight = 33087
keywords = [ "slow" ]
aliases = [ "/questions/33087" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Does attached Image suggest Server Side problem?](/questions/33087/does-attached-image-suggest-server-side-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33087-score" class="post-score" title="current number of votes">0</div><span id="post-33087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm trying to troubleshoot a problem with slow response times when accessing our Internal Intranet web based apps. I've run a WS capture from my machine to the server. My PC is 172.27.10.19 Web Server - 10.44.145.171</p><p>I've followed the tcp stream and displayed the time as "seconds since previous displayed packet"</p><p>Does my attached show a possible issue on the server end? I can see it takes over 6 seconds at one point for my GET command to receive the first packet. I'm not 100% sure on reading the captures so any other things I should be looking out for would be greatly appreciated.</p><p>Thanks<img src="https://osqa-ask.wireshark.org/upfiles/Capture_1.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 May '14, 08:25</strong></p><img src="https://secure.gravatar.com/avatar/a28bceae0effe0ec1130bab7cb87a4e7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="exit12&#39;s gravatar image" /><p><span>exit12</span><br />
<span class="score" title="11 reputation points">11</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="exit12 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-33087" class="comments-container"></div><div id="comment-tools-33087" class="comment-tools"></div><div class="clear"></div><div id="comment-33087-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33089"></span>

<div id="answer-container-33089" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33089-score" class="post-score" title="current number of votes">0</div><span id="post-33089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's interesting that the ACK for the GET arrives in about 40 milliseconds, and then it takes 6 seconds before the content delivery starts. So yes, I'd say your server takes that much time to gather the web page contents. The TCP stack of that server is fast though, which you can tell from the ACK arriving in 40ms. So the server is not slow as a whole, but it's the application on the server that takes that long.</p><p>For a web page this can often be a problem of another server, because web servers not always also run the databases the page is created from. So you might want to check if there is a database server that takes a while to deliver the content that the web server needs to render the HTML page. Usually delays like this are a result of a lot of calculation going on before the page is complete, e.g. large database search requests or other intense things.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 May '14, 08:35</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-33089" class="comments-container"><span id="33091"></span><div id="comment-33091" class="comment"><div id="post-33091-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper,</p><p>Thanks for that. I do know the Server (.171) goes off to another server to authenticate my AD account I'm logged on with when I make a request for the URL. Potentially this is the cause of the problems. I'm guessing I'll need to run a trace on the actual server itself?</p></div><div id="comment-33091-info" class="comment-info"><span class="comment-age">(26 May '14, 09:46)</span> <span class="comment-user userinfo">exit12</span></div></div><span id="33093"></span><div id="comment-33093" class="comment"><div id="post-33093-score" class="comment-score"></div><div class="comment-text"><p>Yes, you need to track all connections that take place in the "backend" of the server while it is creating the web page. Find out what keeps it from delivering the page sooner - it's usually easy to tell what the server was waiting for if you capture at the server itself.</p></div><div id="comment-33093-info" class="comment-info"><span class="comment-age">(26 May '14, 10:32)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-33089" class="comment-tools"></div><div class="clear"></div><div id="comment-33089-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

