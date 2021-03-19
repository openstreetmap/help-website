+++
type = "question"
title = "Arithmetic Support in MATE?"
description = '''Hello, I have found MATE to be an incredibly useful tool (thanks for all the work on this!). I was wondering if there are any plans to add support for arithmetic operators? For example, it would be useful to be able to calculate such things as the number of retransmits or the total cumulative latenc...'''
date = "2016-05-11T07:07:00Z"
lastmod = "2016-05-13T08:30:00Z"
weight = 52431
keywords = [ "development", "mate" ]
aliases = [ "/questions/52431" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Arithmetic Support in MATE?](/questions/52431/arithmetic-support-in-mate)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52431-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52431-score" class="post-score" title="current number of votes">0</div><span id="post-52431-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have found MATE to be an incredibly useful tool (thanks for all the work on this!). I was wondering if there are any plans to add support for arithmetic operators? For example, it would be useful to be able to calculate such things as the number of retransmits or the total cumulative latency in a TCP connection.</p><p>If there are not currently plans for this, is there a specific reason? Has it just been a case of lack of resources, or has it been considered but decided it was too difficult for some reason?</p><p>Thanks, Ryan</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-mate" rel="tag" title="see questions tagged &#39;mate&#39;">mate</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 May '16, 07:07</strong></p><img src="https://secure.gravatar.com/avatar/ba1199f4d360c53a6cc8aa6aa5da37c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ryber&#39;s gravatar image" /><p><span>ryber</span><br />
<span class="score" title="146 reputation points">146</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ryber has one accepted answer">16%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 May '16, 07:25</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-52431" class="comments-container"></div><div id="comment-tools-52431" class="comment-tools"></div><div class="clear"></div><div id="comment-52431-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52445"></span>

<div id="answer-container-52445" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52445-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52445-score" class="post-score" title="current number of votes">0</div><span id="post-52445-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ryber has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, as with most things in Open Source, there isn't really a plan. People contribute what they need or find useful. Apparently no one has thus far had sufficient need for such a functionality so no one has worked on it.</p><p>Typically I'd consider using the IO Graph for the things you're talking about; I don't quite get how you'd intend to use them in MATE.</p><p>Anyway if you want to write up a detailed description of what you're looking for (possibly including example MATE configurations) you can always open an <a href="https://bugs.wireshark.org">enhancement request</a> in case someone picks the idea up and runs with it. (If you do, please report the number back here.) Of course, even better would be code to implement it. :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '16, 13:13</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-52445" class="comments-container"><span id="52516"></span><div id="comment-52516" class="comment"><div id="post-52516-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your response, Jeff.</p><p>What I would like to do is be able to easily identify (in a large pcap) TCP streams with a large number of some indicator of dysfunction. For example, any 4-tuples with a large number of TCP resets. Or streams with the most retransmits, etc. And possibly to be able to do some tracking of ack and seq numbers. I have found it to be very powerful in that it can determine whether something has occurred for a given stream, tuple, etc. but it would be even better if it could track the number of occurrences.</p><p>At the moment, I am finding that I can do this with Lua. But if I have some time I will try looking through the MATE source code and seeing if it is something I might be able to implement (if so I will certainly let you know :) )</p><p>Thanks, Ryan</p></div><div id="comment-52516-info" class="comment-info"><span class="comment-age">(13 May '16, 08:30)</span> <span class="comment-user userinfo">ryber</span></div></div></div><div id="comment-tools-52445" class="comment-tools"></div><div class="clear"></div><div id="comment-52445-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

