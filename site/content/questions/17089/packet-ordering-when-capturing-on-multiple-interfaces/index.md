+++
type = "question"
title = "Packet ordering when capturing on multiple interfaces"
description = '''A colleague asked and I didn&#x27;t really know the answer: When capturing on multiple interfaces which is the preferred sorting order so that packets are displayed in order of arrival at the capturing machine? Sorting by time appears to give the best results, sorting by Frame No. leads to inconsistent r...'''
date = "2012-12-20T03:43:00Z"
lastmod = "2012-12-20T06:44:00Z"
weight = 17089
keywords = [ "capture", "multiple-interfaces", "order" ]
aliases = [ "/questions/17089" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Packet ordering when capturing on multiple interfaces](/questions/17089/packet-ordering-when-capturing-on-multiple-interfaces)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17089-score" class="post-score" title="current number of votes">0</div><span id="post-17089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>A colleague asked and I didn't really know the answer:</p><p>When capturing on multiple interfaces which is the preferred sorting order so that packets are displayed in order of arrival at the capturing machine? Sorting by time appears to give the best results, sorting by Frame No. leads to inconsistent results.</p><p>If sorting by time is best, is even that guaranteed to display the packets in arrival order, or are there "oddities" in the capturing mechanisms that could give errant results?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-multiple-interfaces" rel="tag" title="see questions tagged &#39;multiple-interfaces&#39;">multiple-interfaces</span> <span class="post-tag tag-link-order" rel="tag" title="see questions tagged &#39;order&#39;">order</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Dec '12, 03:43</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-17089" class="comments-container"><span id="17091"></span><div id="comment-17091" class="comment"><div id="post-17091-score" class="comment-score"></div><div class="comment-text"><blockquote><p>sorting by Frame No. leads to inconsistent results.</p></blockquote><p>inconsistent? In terms of what?</p></div><div id="comment-17091-info" class="comment-info"><span class="comment-age">(20 Dec '12, 03:52)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="17093"></span><div id="comment-17093" class="comment"><div id="post-17093-score" class="comment-score"></div><div class="comment-text"><p>The packet order in Wireshark relative to what is actually seen by the receiving application as determined from application log files and the timestamps in Wireshark are not in increasing order.</p></div><div id="comment-17093-info" class="comment-info"><span class="comment-age">(20 Dec '12, 04:11)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-17089" class="comment-tools"></div><div class="clear"></div><div id="comment-17089-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17099"></span>

<div id="answer-container-17099" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17099-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17099-score" class="post-score" title="current number of votes">2</div><span id="post-17099-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="grahamb has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>My personal experience with capturing on multiple interfaces has been that sorting on time worked best (this is, I believe, what the new 'reordercap' utility was designed for).</p><p>But I found that annoying so what I ended up doing (since I was using Linux) was capturing on the 'any' pseudo-device and using capture filters to filter out traffic on the (one or two) interfaces I wasn't interested in.</p><p><strong>Some background:</strong> while Wireshark (1.8.0+) now supports capturing on multiple interfaces simultaneously it does this by spawning off multiple threads (one per interface). Of course, due to the vagaries of OS (thread) scheduling, it's possible that packets that arrive on 2 different interfaces very close in time may arrive in the capture file out of order.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Dec '12, 06:44</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-17099" class="comments-container"></div><div id="comment-tools-17099" class="comment-tools"></div><div class="clear"></div><div id="comment-17099-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

