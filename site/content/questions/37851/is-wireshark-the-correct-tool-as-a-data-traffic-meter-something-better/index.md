+++
type = "question"
title = "Is Wireshark the correct tool as a data (traffic) meter? Something better?"
description = '''My household is allotted 250 gigabytes per month. Someone in my family is using-up all the data. The &quot;traffic meter&quot; on my router (WNDR3700) only tells me total data usage. I want to break it down by MAC address (or some other identifiable way). Is Wireshark the correct tool to do this or do i need ...'''
date = "2014-11-13T23:09:00Z"
lastmod = "2014-11-14T02:04:00Z"
weight = 37851
keywords = [ "router", "wireshark", "networking", "linux" ]
aliases = [ "/questions/37851" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Is Wireshark the correct tool as a data (traffic) meter? Something better?](/questions/37851/is-wireshark-the-correct-tool-as-a-data-traffic-meter-something-better)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37851-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37851-score" class="post-score" title="current number of votes">0</div><span id="post-37851-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My household is allotted 250 gigabytes per month. Someone in my family is using-up all the data. The "traffic meter" on my router (WNDR3700) only tells me total data usage. I want to break it down by MAC address (or some other identifiable way). Is Wireshark the correct tool to do this or do i need something different? (Lubuntu compatible please.)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-router" rel="tag" title="see questions tagged &#39;router&#39;">router</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-networking" rel="tag" title="see questions tagged &#39;networking&#39;">networking</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Nov '14, 23:09</strong></p><img src="https://secure.gravatar.com/avatar/650c29ba862fdc8ce081bd8b446b7d3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shiny%20Toaster&#39;s gravatar image" /><p><span>Shiny Toaster</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shiny Toaster has no accepted answers">0%</span></p></div></div><div id="comments-container-37851" class="comments-container"></div><div id="comment-tools-37851" class="comment-tools"></div><div class="clear"></div><div id="comment-37851-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37854"></span>

<div id="answer-container-37854" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37854-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37854-score" class="post-score" title="current number of votes">0</div><span id="post-37854-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Shiny Toaster has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You request sounds like you want to use Wireshark/tshark as a (real time, long term) network monitoring solution (monitoring 250 Gbyte of traffic for a month). That won't work, as neither Wireshark nor tshark have been developed with that goal in mind. There are well known problems (ever increasing memory usage and others), that will create problems if you run tshark/wireshark for a longer period of time (see other questions).</p><p>I suggest to install <a href="https://openwrt.org/">OpenWRT</a>, <a href="http://www.dd-wrt.com/site/index">DD-WRT</a> or <a href="https://www.gargoyle-router.com/">Gargoyle</a> (or any other supported OS, like Tomato, etc.) on your WNDR3700 and then do some traffic accounting there, as those Linux Distributions offer far better tools than the standard Netgear firmware. Please ask in one of those forums how to do traffic accounting.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '14, 02:04</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-37854" class="comments-container"></div><div id="comment-tools-37854" class="comment-tools"></div><div class="clear"></div><div id="comment-37854-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

