+++
type = "question"
title = "High TCP ack from source machine  Wireshark captured"
description = '''Hi All, I am trying to analyze TCP agent based application that mostly using PSH flags. The application suffering fro some latencies that message should not exceed 50msec. Now as the agent is kind of interactive that change messages and not TCP buffered PSH flags nature its could be that communicati...'''
date = "2013-09-18T05:02:00Z"
lastmod = "2013-09-23T22:33:00Z"
weight = 24904
keywords = [ "latency" ]
aliases = [ "/questions/24904" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [High TCP ack from source machine Wireshark captured](/questions/24904/high-tcp-ack-from-source-machine-wireshark-captured)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24904-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24904-score" class="post-score" title="current number of votes">0</div><span id="post-24904-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I am trying to analyze TCP agent based application that mostly using PSH flags. The application suffering fro some latencies that message should not exceed 50msec. Now as the agent is kind of interactive that change messages and not TCP buffered PSH flags nature its could be that communication is idle to up to 5sec. The problem is that i can see that destination sometimes TCP ACK to source around 180~200msec , but i can see the same issue on the source where the Wireshark capture made ,and my question is what i can i understand from high values ACK 180~200 if its exist on the machine where capture taken should i treat such as pure network congestion or some kind of OS environmental issues like blocking antivirus etc.. Please advice Thanks<img src="https://osqa-ask.wireshark.org/upfiles/9-18-2013_14-52-08.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-latency" rel="tag" title="see questions tagged &#39;latency&#39;">latency</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Sep '13, 05:02</strong></p><img src="https://secure.gravatar.com/avatar/491b248bc5431fa4cfed4498e4633f51?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tbaror&#39;s gravatar image" /><p><span>tbaror</span><br />
<span class="score" title="10 reputation points">10</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tbaror has no accepted answers">0%</span></p></img></div></div><div id="comments-container-24904" class="comments-container"><span id="24907"></span><div id="comment-24907" class="comment"><div id="post-24907-score" class="comment-score"></div><div class="comment-text"><p>Please post the capture somewhere accessible to others, e.g. <a href="http://cloudshark.org">Cloudshark</a> or a file sharing service and posting the link back here. Diagnosing issues by looking at a screen capture is very difficult.</p><p>If you put the capture on Cloudshark, you can also add comments on the packets.</p></div><div id="comment-24907-info" class="comment-info"><span class="comment-age">(18 Sep '13, 05:22)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="24909"></span><div id="comment-24909" class="comment"><div id="post-24909-score" class="comment-score"></div><div class="comment-text"><p>Done uploaded to <a href="http://www.cloudshark.org/captures/2513a5cb618a">Cloudshark</a>.</p></div><div id="comment-24909-info" class="comment-info"><span class="comment-age">(18 Sep '13, 06:02)</span> <span class="comment-user userinfo">tbaror</span></div></div></div><div id="comment-tools-24904" class="comment-tools"></div><div class="clear"></div><div id="comment-24904-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25029"></span>

<div id="answer-container-25029" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25029-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25029-score" class="post-score" title="current number of votes">2</div><span id="post-25029-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tbaror has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please watch the following video. It pretty much explains what's going on in your sample capture file.</p><p>Wireshark Tutorial of TCP Nagle and Delayed Ack interaction<br />
</p><blockquote><p><a href="http://www.youtube.com/watch?v=2CMueBcQNtk">http://www.youtube.com/watch?v=2CMueBcQNtk</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '13, 06:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Sep '13, 06:53</strong> </span></p></div></div><div id="comments-container-25029" class="comments-container"><span id="25149"></span><div id="comment-25149" class="comment"><div id="post-25149-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt exactly the answer i was looking for. Thanks</p></div><div id="comment-25149-info" class="comment-info"><span class="comment-age">(23 Sep '13, 22:33)</span> <span class="comment-user userinfo">tbaror</span></div></div></div><div id="comment-tools-25029" class="comment-tools"></div><div class="clear"></div><div id="comment-25029-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

