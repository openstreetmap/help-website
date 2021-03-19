+++
type = "question"
title = "Limiting Packet Captures?"
description = '''Watching tutorials and reading Guides has helped much but I&#x27;ve noticed that the instructors on said tutorial/guide don&#x27;t capture as many packets as I do when I run my chosen Capture Interface. When I start Wireshark and go to the Capture Interface list it displays 1 single Interface, Assuming this i...'''
date = "2012-01-12T08:43:00Z"
lastmod = "2012-01-12T09:12:00Z"
weight = 8342
keywords = [ "filter", "help", "beginner" ]
aliases = [ "/questions/8342" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Limiting Packet Captures?](/questions/8342/limiting-packet-captures)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8342-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8342-score" class="post-score" title="current number of votes">0</div><span id="post-8342-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Watching tutorials and reading Guides has helped much but I've noticed that the instructors on said tutorial/guide don't capture as many packets as I do when I run my chosen Capture Interface. When I start Wireshark and go to the Capture Interface list it displays 1 single Interface, Assuming this is the one for me I instantly notice a difference between Theirs and Mine. Mine is already Capturing packets: the Packets column will continue to rise (Up to 26,00 captures) while the Packets/s will grow to 10 or so then drop back to 0. while I look on theirs they may have 10 or even none. When I select my Interface I get a over flow of capture packets which continues to capture more and more. Making it super difficult to weed out the useful stuff.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-help" rel="tag" title="see questions tagged &#39;help&#39;">help</span> <span class="post-tag tag-link-beginner" rel="tag" title="see questions tagged &#39;beginner&#39;">beginner</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jan '12, 08:43</strong></p><img src="https://secure.gravatar.com/avatar/a67f5a367b70747b2b4d4b9b01b7911a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n09a&#39;s gravatar image" /><p><span>n09a</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n09a has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Jan '12, 12:10</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-8342" class="comments-container"><span id="8345"></span><div id="comment-8345" class="comment"><div id="post-8345-score" class="comment-score"></div><div class="comment-text"><p>Further More, Most of what I'm capturing is "1514 Continuation Non-HTTP traffic" any suggestions?</p></div><div id="comment-8345-info" class="comment-info"><span class="comment-age">(12 Jan '12, 08:57)</span> <span class="comment-user userinfo">n09a</span></div></div><span id="8347"></span><div id="comment-8347" class="comment"><div id="post-8347-score" class="comment-score"></div><div class="comment-text"><p>(Converted to a comment in keeping with the way this site works. Please see the FAQ).</p></div><div id="comment-8347-info" class="comment-info"><span class="comment-age">(12 Jan '12, 09:01)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-8342" class="comment-tools"></div><div class="clear"></div><div id="comment-8342-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8346"></span>

<div id="answer-container-8346" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8346-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8346-score" class="post-score" title="current number of votes">0</div><span id="post-8346-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Welcome to the world of network analysis !<br />
</p><p>I remember being surprised at the sheer amount of stuff going on from/to my PC when I first did a capture.</p><p>Display (and Capture) filters can help you to filter out unwanted stuff so as to focus on the "useful stuff".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '12, 08:58</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Jan '12, 09:01</strong> </span></p></div></div><div id="comments-container-8346" class="comments-container"><span id="8348"></span><div id="comment-8348" class="comment"><div id="post-8348-score" class="comment-score"></div><div class="comment-text"><p>I've learned little with filtering. But I do know how to.. hehe. Any way I can filter through HTTP captures so I can only view Posts?</p></div><div id="comment-8348-info" class="comment-info"><span class="comment-age">(12 Jan '12, 09:01)</span> <span class="comment-user userinfo">n09a</span></div></div><span id="8349"></span><div id="comment-8349" class="comment"><div id="post-8349-score" class="comment-score"></div><div class="comment-text"><p>I suspect using a display filter like http.request.method=="POST" will work.</p><p>You can learn about possible field names to filter on by selecting a field in the "details" pane and then looking at the status line at the bottom of the Wireshark Window to see the name of the field.</p></div><div id="comment-8349-info" class="comment-info"><span class="comment-age">(12 Jan '12, 09:12)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-8346" class="comment-tools"></div><div class="clear"></div><div id="comment-8346-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

