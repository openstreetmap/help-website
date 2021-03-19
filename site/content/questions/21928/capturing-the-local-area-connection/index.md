+++
type = "question"
title = "Capturing the Local Area Connection"
description = '''When I go to capture the &quot;Local Area Connection&quot;, it just says at the bottom.. &quot;capturing in progess..&quot;. It seems to take a very long time and I don&#x27;t see anything within the first 10 minutes. I am assuming it is really not capturing, correct? When I go to capture &quot;Wireless Connection&quot; it gives me d...'''
date = "2013-06-11T10:35:00Z"
lastmod = "2013-06-11T11:07:00Z"
weight = 21928
keywords = [ "capture-output" ]
aliases = [ "/questions/21928" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing the Local Area Connection](/questions/21928/capturing-the-local-area-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21928-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21928-score" class="post-score" title="current number of votes">0</div><span id="post-21928-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I go to capture the "Local Area Connection", it just says at the bottom.. "capturing in progess..". It seems to take a very long time and I don't see anything within the first 10 minutes. I am assuming it is really not capturing, correct?</p><p>When I go to capture "Wireless Connection" it gives me data right away.</p><p>Please advise.</p><p>Thank you, Peggy</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-output" rel="tag" title="see questions tagged &#39;capture-output&#39;">capture-output</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jun '13, 10:35</strong></p><img src="https://secure.gravatar.com/avatar/270d1bece8e25e2a946d124ff6fd250e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peggy&#39;s gravatar image" /><p><span>Peggy</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peggy has no accepted answers">0%</span></p></div></div><div id="comments-container-21928" class="comments-container"></div><div id="comment-tools-21928" class="comment-tools"></div><div class="clear"></div><div id="comment-21928-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21929"></span>

<div id="answer-container-21929" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21929-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21929-score" class="post-score" title="current number of votes">0</div><span id="post-21929-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your local area connection may be really busy which lots of incoming packets, which often leads to Wireshark reacting with delay to anything you do. In most cases it will not even update the packet list because the PC is too busy.</p><p>Your wireless link is probably less busy, so you can see the data passing by.</p><p>You could try running dumpcap on a command line to see if the local area connection is receiving packets at all. It has a nice packet counter that tells you how much packet it has picked up, and dumpcap is used by Wireshark anyway whenever you capture packets. I have created a small tutorial on how to use dumpcap in my <a href="http://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/">blog</a> (scroll down to "HowTo: dumpcap").</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '13, 10:41</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-21929" class="comments-container"><span id="21930"></span><div id="comment-21930" class="comment"><div id="post-21930-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your response.</p><p>Does it matter if I am on my PC and connected to the network or do I have to be connected to the switch, server??</p></div><div id="comment-21930-info" class="comment-info"><span class="comment-age">(11 Jun '13, 11:03)</span> <span class="comment-user userinfo">Peggy</span></div></div><span id="21931"></span><div id="comment-21931" class="comment"><div id="post-21931-score" class="comment-score"></div><div class="comment-text"><p>It depends on what you want to capture. Take a look at this Wiki page: <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a></p></div><div id="comment-21931-info" class="comment-info"><span class="comment-age">(11 Jun '13, 11:07)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-21929" class="comment-tools"></div><div class="clear"></div><div id="comment-21929-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

