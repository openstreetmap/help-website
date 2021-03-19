+++
type = "question"
title = "Why does Wireshark cause my network to collapse?"
description = '''I have a local network that I am trying to capture traffic on. Every time I start Wireshark and point it at that network, all the devices loose connection to each other. As soon as I stop Wireshark the problem goes away.'''
date = "2017-03-01T12:08:00Z"
lastmod = "2017-03-21T04:55:00Z"
weight = 59778
keywords = [ "down", "network" ]
aliases = [ "/questions/59778" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why does Wireshark cause my network to collapse?](/questions/59778/why-does-wireshark-cause-my-network-to-collapse)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59778-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59778-score" class="post-score" title="current number of votes">0</div><span id="post-59778-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a local network that I am trying to capture traffic on. Every time I start Wireshark and point it at that network, all the devices loose connection to each other. As soon as I stop Wireshark the problem goes away.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-down" rel="tag" title="see questions tagged &#39;down&#39;">down</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Mar '17, 12:08</strong></p><img src="https://secure.gravatar.com/avatar/60d3041356b2a3356f716657e51142cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pabeader&#39;s gravatar image" /><p><span>pabeader</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pabeader has no accepted answers">0%</span></p></div></div><div id="comments-container-59778" class="comments-container"><span id="59812"></span><div id="comment-59812" class="comment"><div id="post-59812-score" class="comment-score"></div><div class="comment-text"><p>What type of network? Ethernet? Wi-Fi? Other?</p></div><div id="comment-59812-info" class="comment-info"><span class="comment-age">(02 Mar '17, 13:38)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="59825"></span><div id="comment-59825" class="comment"><div id="post-59825-score" class="comment-score"></div><div class="comment-text"><p>Wired Ethernet. 192.168. network with 8 different devices all talking to each other. The effect is almost immediate.</p></div><div id="comment-59825-info" class="comment-info"><span class="comment-age">(03 Mar '17, 04:40)</span> <span class="comment-user userinfo">pabeader</span></div></div><span id="59836"></span><div id="comment-59836" class="comment"><div id="post-59836-score" class="comment-score"></div><div class="comment-text"><p>So does that network use a switch or a non-switching hub? Are you running Wireshark on one of those 8 devices, or on a separate device you've plugged into the network?</p></div><div id="comment-59836-info" class="comment-info"><span class="comment-age">(03 Mar '17, 12:02)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="59838"></span><div id="comment-59838" class="comment"><div id="post-59838-score" class="comment-score"></div><div class="comment-text"><p>There are multiple switches all ganged together. I am plugging into an available port on one of them. Wireshark on my laptop.</p></div><div id="comment-59838-info" class="comment-info"><span class="comment-age">(03 Mar '17, 13:26)</span> <span class="comment-user userinfo">pabeader</span></div></div><span id="59839"></span><div id="comment-59839" class="comment"><div id="post-59839-score" class="comment-score"></div><div class="comment-text"><p>Does this happen only when Wireshark is capturing in promiscuous mode, or does it even happen when you try capturing with promiscuous mode turned off?</p><p>What operating system is your laptop running?</p></div><div id="comment-59839-info" class="comment-info"><span class="comment-age">(03 Mar '17, 13:36)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="59890"></span><div id="comment-59890" class="comment not_top_scorer"><div id="post-59890-score" class="comment-score"></div><div class="comment-text"><p>Promiscuous on or off.</p><p>It has stopped killing the network. Now I can't see the traffic I used to. I'm trying to capture tcp traffic for port:2001 Now I don't see any of this traffic at all. It seems that every time I start Wireshark it seems to act differently. Is there a different program that is simpler?</p></div><div id="comment-59890-info" class="comment-info"><span class="comment-age">(07 Mar '17, 08:47)</span> <span class="comment-user userinfo">pabeader</span></div></div><span id="59896"></span><div id="comment-59896" class="comment not_top_scorer"><div id="post-59896-score" class="comment-score"></div><div class="comment-text"><p><em>Is there a different program</em></p><p>A number of other packet capture programs/tools exist. You can peruse the <a href="https://wiki.wireshark.org/Tools">Tools</a> page for some possibilities, or just perform an online search and I'm sure you'll discover some.</p></div><div id="comment-59896-info" class="comment-info"><span class="comment-age">(07 Mar '17, 10:31)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="60220"></span><div id="comment-60220" class="comment not_top_scorer"><div id="post-60220-score" class="comment-score"></div><div class="comment-text"><p>Go ahead and close this thread. I gave up and quit trying to figure out the issue.</p></div><div id="comment-60220-info" class="comment-info"><span class="comment-age">(21 Mar '17, 04:55)</span> <span class="comment-user userinfo">pabeader</span></div></div></div><div id="comment-tools-59778" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-59778-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60212"></span>

<div id="answer-container-60212" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60212-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60212-score" class="post-score" title="current number of votes">0</div><span id="post-60212-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Where are you writing the captured WireShark files to?</p><p>If you're saving the capture on the local machine where WireShark is located you shouldn't experience this problem.</p><p>But if you're attempting to write the packets to a shared server drive remotely, that will cause a massive influx of traffic which might overload your network.</p><p>Cheers,</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '17, 23:52</strong></p><img src="https://secure.gravatar.com/avatar/6c8f0de8cb4ef9ad7093eefe24030e4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wbenton&#39;s gravatar image" /><p><span>wbenton</span><br />
<span class="score" title="29 reputation points">29</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wbenton has no accepted answers">0%</span></p></div></div><div id="comments-container-60212" class="comments-container"></div><div id="comment-tools-60212" class="comment-tools"></div><div class="clear"></div><div id="comment-60212-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

