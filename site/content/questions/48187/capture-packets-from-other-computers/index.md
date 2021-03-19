+++
type = "question"
title = "Capture packets from other computers"
description = '''I can easily capture packets from my own laptop. However, I am facing some issues when trying to capture packets (my target is HTTP Protocol) for others who are in my network and in the same network address range. I read on some forums that I need to listen to a common denominator that these network...'''
date = "2015-12-02T04:26:00Z"
lastmod = "2015-12-02T04:46:00Z"
weight = 48187
keywords = [ "packets" ]
aliases = [ "/questions/48187" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture packets from other computers](/questions/48187/capture-packets-from-other-computers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48187-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48187-score" class="post-score" title="current number of votes">0</div><span id="post-48187-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I can easily capture packets from my own laptop. However, I am facing some issues when trying to capture packets (my target is HTTP Protocol) for others who are in my network and in the same network address range.</p><p>I read on some forums that I need to listen to a common denominator that these networks pass by and get their data to/from and the most logical place for that is the router, because all of them and me are connected to it and it is the point of server for all of us. It does both routing and switching.</p><p>However, whenever I point and filter the traffic that is coming and going through the router using ip.addr == 192.168.1.1 (which is the address of the router) I can not see anything.</p><p>What am I missing and how is possible to sniff packets in and out of other IP addresses in the same network as mine?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '15, 04:26</strong></p><img src="https://secure.gravatar.com/avatar/0339babf64d57456486611e63811231f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tonysoprano&#39;s gravatar image" /><p><span>tonysoprano</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tonysoprano has no accepted answers">0%</span></p></div></div><div id="comments-container-48187" class="comments-container"></div><div id="comment-tools-48187" class="comment-tools"></div><div class="clear"></div><div id="comment-48187-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48188"></span>

<div id="answer-container-48188" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48188-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48188-score" class="post-score" title="current number of votes">0</div><span id="post-48188-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You're likely running in a switched network, where the router is the switch. A switch ordinarily does not reflect traffic between two ports to another port, hence you can't see traffic between other devices on your switch port.</p><p>See the Wiki page on <a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">Ethernet</a> capture setup, in particular the information about switched networks. The page has some solutions to your capture issues.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '15, 04:46</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-48188" class="comments-container"></div><div id="comment-tools-48188" class="comment-tools"></div><div class="clear"></div><div id="comment-48188-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

