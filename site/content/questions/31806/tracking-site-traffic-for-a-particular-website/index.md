+++
type = "question"
title = "Tracking site traffic for a particular website"
description = '''I am investigating a ticket which requires a particular website to be tracked for handful of users. What&#x27;s happening is that the website works for few users and not for all. I have checked proxy settings and found them to be different for impacted group. The group is not able to access the website a...'''
date = "2014-04-14T14:44:00Z"
lastmod = "2014-04-15T01:44:00Z"
weight = 31806
keywords = [ "website", "traffic" ]
aliases = [ "/questions/31806" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tracking site traffic for a particular website](/questions/31806/tracking-site-traffic-for-a-particular-website)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31806-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am investigating a ticket which requires a particular website to be tracked for handful of users. What's happening is that the website works for few users and not for all. I have checked proxy settings and found them to be different for impacted group. The group is not able to access the website and before attributing the cause to proxy servers, I want to track what happens to the website when user types in the address, where it goes and what is returned to user's machine. Is it possible using Wireshark?</p></div><div id="question-tags" class="tags-container tags">website traffic</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Apr '14, 14:44</strong></p><img src="https://secure.gravatar.com/avatar/20ff09c5ee4c97be957f54c22a5fc41e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="strike3test&#39;s gravatar image" /><p>strike3test<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="strike3test has no accepted answers">0%</span></p></div></div><div id="comments-container-31806" class="comments-container"></div><div id="comment-tools-31806" class="comment-tools"></div><div class="clear"></div><div id="comment-31806-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31830"></span>

<div id="answer-container-31830" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31830-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is it possible using Wireshark?</p></blockquote><p>yes. Just install Wireshark on the affected clients and start it (see the docs how to do that). Then, after you have recreated the problem, stop Wireshark and look into the HTTP requests. You should see either direct requests (IP address of the web server) or proxy requests (IP address of the proxy), depending on the proxy settings in the browser.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '14, 01:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-31830" class="comments-container"></div><div id="comment-tools-31830" class="comment-tools"></div><div class="clear"></div><div id="comment-31830-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

