+++
type = "question"
title = "Visited Websites"
description = '''How do I view visited websites from a computer on my network. I would like to see what websites my children are viewing. I&#x27;m able to start a capture, but the results do not produce website names or URL addresses.'''
date = "2013-07-09T18:19:00Z"
lastmod = "2013-07-10T00:49:00Z"
weight = 22779
keywords = [ "visited", "websites" ]
aliases = [ "/questions/22779" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Visited Websites](/questions/22779/visited-websites)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22779-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22779-score" class="post-score" title="current number of votes">0</div><span id="post-22779-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do I view visited websites from a computer on my network. I would like to see what websites my children are viewing. I'm able to start a capture, but the results do not produce website names or URL addresses.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-visited" rel="tag" title="see questions tagged &#39;visited&#39;">visited</span> <span class="post-tag tag-link-websites" rel="tag" title="see questions tagged &#39;websites&#39;">websites</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '13, 18:19</strong></p><img src="https://secure.gravatar.com/avatar/793c5ff6ef380bb9b2fa837c335c0557?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="deweywoods&#39;s gravatar image" /><p><span>deweywoods</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="deweywoods has no accepted answers">0%</span></p></div></div><div id="comments-container-22779" class="comments-container"></div><div id="comment-tools-22779" class="comment-tools"></div><div class="clear"></div><div id="comment-22779-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22785"></span>

<div id="answer-container-22785" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22785-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22785-score" class="post-score" title="current number of votes">0</div><span id="post-22785-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can print the URLs with tshark. You need to capture the traffic first with Wireshark or dumpcap and write it to input.pcap.</p><blockquote><p><code>tshark -nr input.cap -R http.request -T fields -e frame.time -e ip.src -e http.request.full_uri</code><br />
</p></blockquote><p>However, Wireshark is a network troubleshooting system. It's <strong>not</strong> a good solution for long term monitoring or as a parental control system.</p><p>I suggest to buy some software that logs and restricts access to the internet if you want to protect your kiddies. Please google for: parental control software</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '13, 00:49</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-22785" class="comments-container"></div><div id="comment-tools-22785" class="comment-tools"></div><div class="clear"></div><div id="comment-22785-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

