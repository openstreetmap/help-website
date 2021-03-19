+++
type = "question"
title = "How to view iphone packets on the same network?"
description = '''I recently installed Wireshark on my Windows 7 PC and noticed that most of the packets were either broadcast, multicast, or to/from my own machine. I want to capture packets from my iPhone. My PC is connected to the same wi-fi network that my iPhone is. Is there any way to get wireshark to read pack...'''
date = "2017-01-01T06:23:00Z"
lastmod = "2017-01-01T10:37:00Z"
weight = 58449
keywords = [ "packets", "iphone", "capturing", "network" ]
aliases = [ "/questions/58449" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to view iphone packets on the same network?](/questions/58449/how-to-view-iphone-packets-on-the-same-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58449-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58449-score" class="post-score" title="current number of votes">0</div><span id="post-58449-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I recently installed Wireshark on my Windows 7 PC and noticed that most of the packets were either broadcast, multicast, or to/from my own machine. I want to capture packets from my iPhone. My PC is connected to the same wi-fi network that my iPhone is. Is there any way to get wireshark to read packets sent and received from another device on the same wireless network? Keep in mind I don't know a great deal of information about networking, so please explain how to do this in layman's terms.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-iphone" rel="tag" title="see questions tagged &#39;iphone&#39;">iphone</span> <span class="post-tag tag-link-capturing" rel="tag" title="see questions tagged &#39;capturing&#39;">capturing</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jan '17, 06:23</strong></p><img src="https://secure.gravatar.com/avatar/03239efd15857263b002268c972b987c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="orchface&#39;s gravatar image" /><p><span>orchface</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="orchface has no accepted answers">0%</span></p></div></div><div id="comments-container-58449" class="comments-container"><span id="58453"></span><div id="comment-58453" class="comment"><div id="post-58453-score" class="comment-score"></div><div class="comment-text"><p>Is your WIFI network listed in Windows as a "secure" one? If so, is it important to you that the iphone's traffic be captured in an unencrypted form?</p></div><div id="comment-58453-info" class="comment-info"><span class="comment-age">(01 Jan '17, 10:37)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-58449" class="comment-tools"></div><div class="clear"></div><div id="comment-58449-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58450"></span>

<div id="answer-container-58450" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58450-score" class="post-score" title="current number of votes">0</div><span id="post-58450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's complicated, especially on Windows, as you need to get the wireless interface into "Monitor Mode". See the wiki page on <a href="https://wiki.wireshark.org/CaptureSetup/WLAN">WLAN capture</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jan '17, 06:28</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-58450" class="comments-container"></div><div id="comment-tools-58450" class="comment-tools"></div><div class="clear"></div><div id="comment-58450-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

