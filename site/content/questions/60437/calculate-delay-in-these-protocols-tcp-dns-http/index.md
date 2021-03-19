+++
type = "question"
title = "calculate delay in these protocols TCP, DNS, HTTP"
description = '''Hello! I want to know guys how to calculate a delay for TCP, DNS, HTTP. And how much delay is too much? I know that not all delays are that important, I&#x27;m talking about the ones that really matters.'''
date = "2017-03-30T03:04:00Z"
lastmod = "2017-03-30T07:27:00Z"
weight = 60437
keywords = [ "http", "dns", "tcp" ]
aliases = [ "/questions/60437" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [calculate delay in these protocols TCP, DNS, HTTP](/questions/60437/calculate-delay-in-these-protocols-tcp-dns-http)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60437-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60437-score" class="post-score" title="current number of votes">0</div><span id="post-60437-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello! I want to know guys how to calculate a delay for TCP, DNS, HTTP. And how much delay is too much? I know that not all delays are that important, I'm talking about the ones that really matters.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Mar '17, 03:04</strong></p><img src="https://secure.gravatar.com/avatar/a9c1c21541914db2579666156c4521ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Faiz&#39;s gravatar image" /><p><span>Faiz</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Faiz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Mar '17, 09:45</strong> </span></p></div></div><div id="comments-container-60437" class="comments-container"></div><div id="comment-tools-60437" class="comment-tools"></div><div class="clear"></div><div id="comment-60437-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60442"></span>

<div id="answer-container-60442" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60442-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60442-score" class="post-score" title="current number of votes">3</div><span id="post-60442-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For TCP: in the packet details pane, right-click on the "Transmission Control Protocol" section then select "Protocol Preferences" and check "Calculate Conversation Timestamps." You can then scroll to the bottom of the TCP section in the packet details pane to the "Timestamps" area, right-click on "Time since previous frame..." and select "Apply as column." This will give you a column of TCP Delta times which represent delay.</p><p>For DNS, you can create a column using dns.time for a similar setup as the TCP example above.</p><p>HTTP can typically use the TCP Delta, but there is also an http.time filter.</p><p>This information can be input into advanced IO graphs for further analysis.</p><p>From there, you will need to analyze the capture to determine which delays matter. I typically look for any delays over .5 second, but that might even be too long depending on your application. Delay during the handshake will give an indication of overall latency or problems if it's too high. Generally, I ignore long delays on RST and FIN packets at the end of a conversation. Analyzing delay can be somewhat of an art form at times. Obviously, long delays that line up with complaints or log files can be easy to spot. Other times, it takes patience, experience, and trial and error.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '17, 07:27</strong></p><img src="https://secure.gravatar.com/avatar/37aeac42341cc42e5d10656094aa9139?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="csereno&#39;s gravatar image" /><p><span>csereno</span><br />
<span class="score" title="69 reputation points">69</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="csereno has one accepted answer">25%</span></p></div></div><div id="comments-container-60442" class="comments-container"></div><div id="comment-tools-60442" class="comment-tools"></div><div class="clear"></div><div id="comment-60442-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

