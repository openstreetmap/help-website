+++
type = "question"
title = "Basic Questions"
description = '''Hello, New to WS and TCP analysis and hoping someone can answer the following questions.  I&#x27;m using version 2.2.4 on Windows 10   I want to know if the application I&#x27;m using is single thread or multi thread and believe WS can help clarify this correct?   After the capture is done if I go up to stati...'''
date = "2017-02-14T08:53:00Z"
lastmod = "2017-02-14T09:59:00Z"
weight = 59409
keywords = [ "question", "basic" ]
aliases = [ "/questions/59409" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Basic Questions](/questions/59409/basic-questions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59409-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59409-score" class="post-score" title="current number of votes">0</div><span id="post-59409-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>New to WS and TCP analysis and hoping someone can answer the following questions.</p><p>I'm using version 2.2.4 on Windows 10</p><ol><li>I want to know if the application I'm using is single thread or multi thread and believe WS can help clarify this correct?</li><li><p>After the capture is done if I go up to statistics and conversations then TCP I saw only one conversations between the two IP addresses I am interested in. I only had one Instance of the application open does that mean it's a single thread? However, we could of opened up multiple instances of the application so does that mean it's multi-thread?</p></li><li><p>If I scroll through a capture and find a packet with the destination IP my application is talking to and right click and choose conversation filter and click on TCP. The next screen takes me to that ?? fill in the blank because when I click follow the TCP stream it's the same packets so what's the difference between stream and conversation if any?</p></li></ol><p>thanks for any help!</p><p>also, if you want to recommend any good books on WS for beginners or TCP for beginners let me know.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-question" rel="tag" title="see questions tagged &#39;question&#39;">question</span> <span class="post-tag tag-link-basic" rel="tag" title="see questions tagged &#39;basic&#39;">basic</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Feb '17, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/a6414c2ff8204ee9c4a3bc2a646c4644?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rock90&#39;s gravatar image" /><p><span>rock90</span><br />
<span class="score" title="21 reputation points">21</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rock90 has no accepted answers">0%</span></p></div></div><div id="comments-container-59409" class="comments-container"></div><div id="comment-tools-59409" class="comment-tools"></div><div class="clear"></div><div id="comment-59409-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="59411"></span>

<div id="answer-container-59411" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59411-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59411-score" class="post-score" title="current number of votes">1</div><span id="post-59411-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rock90 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>1 - Wireshark is unable to show how many threads are running in an application. You might be able to infer something from looking at the network traffic, but it would basically be a guess.</p><p>You can find the number of threads in use from Task Manager, select the Details tab, right click any of the column headers, click "Select Columns" and then check the Threads item. Note that a multithreaded application may still be using a single thread for network I/O (unlikely though).</p><p>2 - The conversations display shows a summary of the conversations between two endpoints, for TCP the endpoints are the source IP and port and destination IP and port. This has nothing to do with a single threaded or multithreaded application.</p><p>3 - A conversation includes all traffic between 2 endpoints, see item 2 above. A tcp stream is defined by the start, the initial SYN packet, and the end, the final FIN ACK packet. TCP conversations include all streams between those two endpoints. Your capture likely contains one conversation with a single stream hence the similarity of the results.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '17, 09:10</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-59411" class="comments-container"></div><div id="comment-tools-59411" class="comment-tools"></div><div class="clear"></div><div id="comment-59411-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="59410"></span>

<div id="answer-container-59410" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59410-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59410-score" class="post-score" title="current number of votes">1</div><span id="post-59410-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Welcome.</p><ol><li>No, it can't. Wireshark can look at network conversations, but it can't tell you details about application behavior on a computer - only what kind of packets/data it sends/receives.</li><li>No, see point 1. You can't deduct that from network behavior.</li><li>You filtered a TCP conversation, meaning all other packets will be hidden temporarily. If you only had one conversation visible before the filter won't do anything - you're hidding everything else, but there's nothing else. A stream and a conversation are basically the same thing in your case.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '17, 09:00</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-59410" class="comments-container"></div><div id="comment-tools-59410" class="comment-tools"></div><div class="clear"></div><div id="comment-59410-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="59414"></span>

<div id="answer-container-59414" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59414-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59414-score" class="post-score" title="current number of votes">1</div><span id="post-59414-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As for training material we have to refer to <a href="https://www.wireshark.org/docs/">all this material</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '17, 09:59</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-59414" class="comments-container"></div><div id="comment-tools-59414" class="comment-tools"></div><div class="clear"></div><div id="comment-59414-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

