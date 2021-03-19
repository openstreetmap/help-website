+++
type = "question"
title = "Laptop Hardware Recommendations for running Wireshark"
description = '''Forum About a year ago, I purchased an HP gaming laptop based on its specs.. see below: Processor (Intel Core i7 - Q720 @ 1.6GHZ, 1600Mhz, 4 Core(s), 8 Logical Processors)  Memory - 6 G with lots of HDD space. I am not sure why, but I have been unsuccessful using WS for more than 10 minutes at a tim...'''
date = "2011-10-14T10:44:00Z"
lastmod = "2012-11-02T13:06:00Z"
weight = 6894
keywords = [ "hardware", "laptop" ]
aliases = [ "/questions/6894" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Laptop Hardware Recommendations for running Wireshark](/questions/6894/laptop-hardware-recommendations-for-running-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6894-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6894-score" class="post-score" title="current number of votes">0</div><span id="post-6894-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Forum</p><p>About a year ago, I purchased an HP gaming laptop based on its specs.. see below: Processor (Intel Core i7 - Q720 @ 1.6GHZ, 1600Mhz, 4 Core(s), 8 Logical Processors) Memory - 6 G with lots of HDD space.</p><p>I am not sure why, but I have been unsuccessful using WS for more than 10 minutes at a time before it shuts down/ locks up.</p><p>I need a reliable Laptop that I dont have to worry about WS crashing. Can anyone out there recommend good hardware for a laptop? Thanks in advance! KMNRuser</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-hardware" rel="tag" title="see questions tagged &#39;hardware&#39;">hardware</span> <span class="post-tag tag-link-laptop" rel="tag" title="see questions tagged &#39;laptop&#39;">laptop</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Oct '11, 10:44</strong></p><img src="https://secure.gravatar.com/avatar/9e96b23e3495316e470ba9b487b82a73?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kmnruser&#39;s gravatar image" /><p><span>kmnruser</span><br />
<span class="score" title="26 reputation points">26</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kmnruser has no accepted answers">0%</span></p></div></div><div id="comments-container-6894" class="comments-container"></div><div id="comment-tools-6894" class="comment-tools"></div><div class="clear"></div><div id="comment-6894-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6924"></span>

<div id="answer-container-6924" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6924-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6924-score" class="post-score" title="current number of votes">1</div><span id="post-6924-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm guessing that by "shuts down/locks up" you mean crashes/exits. Is this correct (or do you mean Wireshark hangs while using CPU) ?</p><p>Is there any message following the "shutdown/lockup" ?</p><p>Possibilities:</p><ol><li><p>There's a Wireshark bug (especially if Wireshark hangs while using CPU).</p></li><li><p>There's too much data.</p></li></ol><p>What is the speed of the network interface you are capturing from ?</p><p>In general, Wireshark cannot be used to capture an unlimited amount of data. Wireshark accumulates "state" information in memory as a capture proceeds and thus memory will at some point be exhausted as the capture proceeds. (If you use the "ring buffer" option with multiple files of a limited size, then the memory usage will be reset as each new file is opened).</p><p>See: <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">Out of Memory</a></p><p>Dumpcap (a program in the Wireshark suite) can be used to capture directly to a file (or set of files). Try using dumpcap and see what happens.</p><pre><code> 3. ??</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '11, 07:12</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div></div><div id="comments-container-6924" class="comments-container"><span id="15512"></span><div id="comment-15512" class="comment"><div id="post-15512-score" class="comment-score"></div><div class="comment-text"><p>Sorry i did not get back out here to thank you for the post.</p><p>The interface is a Gig interface. the LT is pretty beefy, but sometimes other apps crash on it as well.</p><p>I am going to get rid of it and get another one.</p><p>Take Care</p></div><div id="comment-15512-info" class="comment-info"><span class="comment-age">(02 Nov '12, 12:52)</span> <span class="comment-user userinfo">kmnruser</span></div></div><span id="15514"></span><div id="comment-15514" class="comment"><div id="post-15514-score" class="comment-score"></div><div class="comment-text"><p>I converted your "answer" to a comment as that's how this site works, please see the FAQ for more info.</p><p>If other apps are crashing it may mean a hardware issue. Have you run a memory test as that's easiest to swap out if it is faulty?</p></div><div id="comment-15514-info" class="comment-info"><span class="comment-age">(02 Nov '12, 13:06)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-6924" class="comment-tools"></div><div class="clear"></div><div id="comment-6924-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

