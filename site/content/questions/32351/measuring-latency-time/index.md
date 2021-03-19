+++
type = "question"
title = "Measuring latency time"
description = '''Hi, I have a system that consists in a server and several equipaments. The server does a polling through each equipment, communicating with them all the time to check if they are ok, and it has a 1000ms limit for timeout, if the equipment does not respond in 1000ms the server will disable the equipm...'''
date = "2014-05-01T08:40:00Z"
lastmod = "2014-05-01T15:12:00Z"
weight = 32351
keywords = [ "latency" ]
aliases = [ "/questions/32351" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Measuring latency time](/questions/32351/measuring-latency-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32351-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32351-score" class="post-score" title="current number of votes">0</div><span id="post-32351-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a system that consists in a server and several equipaments. The server does a polling through each equipment, communicating with them all the time to check if they are ok, and it has a 1000ms limit for timeout, if the equipment does not respond in 1000ms the server will disable the equipment.</p><p>I am losing communication with the equipments with no reason and only the timeout alarme.</p><p>I was wondering if I could use wireshark to measure the communication latency between the server and a specific Ip equipment to be sure of the timeout problem.</p><p>How can I measure the latency communication with Wireshark?</p><p>Thank You,</p><p>Rafael Braga Campello TV GLOBO <span class="__cf_email__" data-cfemail="97e5f6f1f6f2fbb9f4f6fae7f2fbfbf8d7e3e1f0fbf8f5f8b9f4f8fab9f5e5">[email protected]</span> <span class="__cf_email__" data-cfemail="7705161116121b1c051137101a161e1b5914181a">[email protected]</span> +55 21 9 88730309 (mobile) +55 21 25403169 (office)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-latency" rel="tag" title="see questions tagged &#39;latency&#39;">latency</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 May '14, 08:40</strong></p><img src="https://secure.gravatar.com/avatar/fe86f355f8ab3e20bc43b548cda6bfa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="campello&#39;s gravatar image" /><p><span>campello</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="campello has no accepted answers">0%</span></p></div></div><div id="comments-container-32351" class="comments-container"></div><div id="comment-tools-32351" class="comment-tools"></div><div class="clear"></div><div id="comment-32351-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32353"></span>

<div id="answer-container-32353" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32353-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32353-score" class="post-score" title="current number of votes">1</div><span id="post-32353-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Filter out the TCP stream, then look at the DELTA times to see the response delay.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 May '14, 09:38</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p><span>Rooster_50</span><br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></div></div><div id="comments-container-32353" class="comments-container"><span id="32363"></span><div id="comment-32363" class="comment"><div id="post-32363-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much Rooster_50. It worked fine as I needed.</p></div><div id="comment-32363-info" class="comment-info"><span class="comment-age">(01 May '14, 14:08)</span> <span class="comment-user userinfo">campello</span></div></div><span id="32364"></span><div id="comment-32364" class="comment"><div id="post-32364-score" class="comment-score"></div><div class="comment-text"><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions.</p></div><div id="comment-32364-info" class="comment-info"><span class="comment-age">(01 May '14, 15:12)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-32353" class="comment-tools"></div><div class="clear"></div><div id="comment-32353-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

