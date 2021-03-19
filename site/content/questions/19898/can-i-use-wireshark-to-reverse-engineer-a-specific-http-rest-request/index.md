+++
type = "question"
title = "can i use wireshark to reverse engineer a specific http REST request?"
description = '''the original question is asked here: http://stackoverflow.com/questions/15679883/how-to-reverse-engineer-an-http-api-call-using-rest-console but basically i was wondering if wireshark would give me more information than chrome rest console does?  thanks!'''
date = "2013-03-28T05:23:00Z"
lastmod = "2013-03-28T15:14:00Z"
weight = 19898
keywords = [ "api", "http", "rest" ]
aliases = [ "/questions/19898" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [can i use wireshark to reverse engineer a specific http REST request?](/questions/19898/can-i-use-wireshark-to-reverse-engineer-a-specific-http-rest-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19898-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>the original question is asked here: <a href="http://stackoverflow.com/questions/15679883/how-to-reverse-engineer-an-http-api-call-using-rest-console">http://stackoverflow.com/questions/15679883/how-to-reverse-engineer-an-http-api-call-using-rest-console</a></p><p>but basically i was wondering if wireshark would give me more information than chrome rest console does?<br />
</p><p>thanks!</p></div><div id="question-tags" class="tags-container tags">api http rest</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Mar '13, 05:23</strong></p><img src="https://secure.gravatar.com/avatar/209015517962ecc597f62380b9e27128?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="abbood&#39;s gravatar image" /><p>abbood<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="abbood has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-19898" class="comments-container"></div><div id="comment-tools-19898" class="comment-tools"></div><div class="clear"></div><div id="comment-19898-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19904"></span>

<div id="answer-container-19904" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19904-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yep, it would, because if you capture the full communication you'll see everything that is going back and forth.</p><p>What I usually do if I'm trying to mimic application behavior is that I do a capture of the original request and use that to compare subsequent requests that I do with my own software. You can quite easily see what parts are different when you have to packets containing the requests.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '13, 06:35</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-19904" class="comments-container"></div><div id="comment-tools-19904" class="comment-tools"></div><div class="clear"></div><div id="comment-19904-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19919"></span>

<div id="answer-container-19919" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19919-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>i was wondering if wireshark would give me more information than chrome rest console does?</p></blockquote><p>No it won't.</p><p>Your problem is the lack of an authenticated session, as already mentioned on stackoverflow.</p><p>After your authentication in the browser (login form), you received a rather long session cookie, and that information is already shown by chrome console. Wireshark will not show any more information in your case. Unless you send a valid session cookie alongside with your "hand crafted POST request", you will not get a valid answer from the server, as it will be unable to identify the user session within the application.</p><p>You should check their API documentation to figure out how to access the data on their site.</p><blockquote><p><code>http://www.zoominfo.com/business/products/zoominfo-api</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Mar '13, 15:14</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Mar '13, 15:19</p></div></div><div id="comments-container-19919" class="comments-container"></div><div id="comment-tools-19919" class="comment-tools"></div><div class="clear"></div><div id="comment-19919-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

