+++
type = "question"
title = "Offline use for wireshark?"
description = '''Hello, I&#x27;ve been trying to figure out the best way to do this. I am currently trying to use wireshark offline and wasn&#x27;t sure if this was possible? I am staying disconnected from the internet while attempting to run some dangerous scripts to isolate what protocols it is using and where it is trying ...'''
date = "2016-08-11T08:05:00Z"
lastmod = "2016-08-13T20:58:00Z"
weight = 54750
keywords = [ "virus", "offline" ]
aliases = [ "/questions/54750" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Offline use for wireshark?](/questions/54750/offline-use-for-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54750-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54750-score" class="post-score" title="current number of votes">0</div><span id="post-54750-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I've been trying to figure out the best way to do this. I am currently trying to use wireshark offline and wasn't sure if this was possible? I am staying disconnected from the internet while attempting to run some dangerous scripts to isolate what protocols it is using and where it is trying to go out to. The reason this is offline is because I don't want this to get onto my network so I want to keep it isolated. Is there a way to do this, or does wireshark have to be online?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-virus" rel="tag" title="see questions tagged &#39;virus&#39;">virus</span> <span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Aug '16, 08:05</strong></p><img src="https://secure.gravatar.com/avatar/ceb3a031f7fa7ca27a82cc139bd8d99f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wireshark_Noob890&#39;s gravatar image" /><p><span>Wireshark_No...</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wireshark_Noob890 has no accepted answers">0%</span></p></div></div><div id="comments-container-54750" class="comments-container"></div><div id="comment-tools-54750" class="comment-tools"></div><div class="clear"></div><div id="comment-54750-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="54752"></span>

<div id="answer-container-54752" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54752-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54752-score" class="post-score" title="current number of votes">2</div><span id="post-54752-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark itself can be used offline to open and analyze packet capture files you already have. If you want to watch live traffic you need to have a network connection, otherwise the malware you're looking at will not have a path for communication and won't be able to send anything. Which means that you cannot record anything.</p><p>You might want to take a look at tools that can simulate networks, e.g. <a href="https://practicalmalwareanalysis.com/fakenet/">https://practicalmalwareanalysis.com/fakenet/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Aug '16, 08:10</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-54752" class="comments-container"></div><div id="comment-tools-54752" class="comment-tools"></div><div class="clear"></div><div id="comment-54752-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="54785"></span>

<div id="answer-container-54785" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54785-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54785-score" class="post-score" title="current number of votes">0</div><span id="post-54785-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to capture live traffic, your network interface card needs to be in an up-link status.</p><p>But that doesn't mean you need to connect that machine to your live network, just connect the Wireshark machine to any stand-alone hub with nothing else connected to it (almost like offline). That will cause the NIC to go into up-link status.</p><p>FWIW</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Aug '16, 20:58</strong></p><img src="https://secure.gravatar.com/avatar/6c8f0de8cb4ef9ad7093eefe24030e4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wbenton&#39;s gravatar image" /><p><span>wbenton</span><br />
<span class="score" title="29 reputation points">29</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wbenton has no accepted answers">0%</span></p></div></div><div id="comments-container-54785" class="comments-container"></div><div id="comment-tools-54785" class="comment-tools"></div><div class="clear"></div><div id="comment-54785-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

