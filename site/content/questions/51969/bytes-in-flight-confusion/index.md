+++
type = "question"
title = "Bytes in Flight confusion"
description = '''Hi all I am confused about my bytes in flight results. We are running sftp transfers (source is Europe and destination is in North America) and we are only able to get 400KB/s which is very slow for the user. So I did a wireshark of the session and am looking at the bytes-in-flight value.  Based on ...'''
date = "2016-04-26T12:53:00Z"
lastmod = "2016-04-26T13:00:00Z"
weight = 51969
keywords = [ "tcp-bytes-in-flight", "tcp", "sftp" ]
aliases = [ "/questions/51969" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Bytes in Flight confusion](/questions/51969/bytes-in-flight-confusion)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51969-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51969-score" class="post-score" title="current number of votes">0</div><span id="post-51969-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all</p><p>I am confused about my bytes in flight results.</p><p>We are running sftp transfers (source is Europe and destination is in North America) and we are only able to get 400KB/s which is very slow for the user. So I did a wireshark of the session and am looking at the bytes-in-flight value.</p><p>Based on the capture, my receiving server can handle 23168 bytes in flight at any given time (win siz 5792 with scaling of 4). From the packet, we never get more then 13032 bytes in flight at any given time.</p><p>Which, if I am understanding correctly, means we are not using the full BW and that there is packet loss somewhere forcing retransmission. Checking the steven's graph also shows a lot of retransmission. (Based on this video <a href="https://www.youtube.com/watch?v=sIxv3YO2eYw)">https://www.youtube.com/watch?v=sIxv3YO2eYw)</a></p><p>So I ran another test. I did sftp transfer from a laptop in North America to the server in North America. The throughput we get is about 10MB/s. Max bytes-in-flight possible is 23600 and the max un-ack bytes in flight from the trace is 13000. This is not what I expected. I thought, that given my higher throughput, I should be constantly hitting the max possible bytes-in-flight of 23600.</p><p>So now I am confused. Did I misunderstand anything?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp-bytes-in-flight" rel="tag" title="see questions tagged &#39;tcp-bytes-in-flight&#39;">tcp-bytes-in-flight</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-sftp" rel="tag" title="see questions tagged &#39;sftp&#39;">sftp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Apr '16, 12:53</strong></p><img src="https://secure.gravatar.com/avatar/0b6142cb5c6c09edcbe740b6ce3fb7f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jzoudavy&#39;s gravatar image" /><p><span>jzoudavy</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jzoudavy has no accepted answers">0%</span></p></div></div><div id="comments-container-51969" class="comments-container"></div><div id="comment-tools-51969" class="comment-tools"></div><div class="clear"></div><div id="comment-51969-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51970"></span>

<div id="answer-container-51970" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51970-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51970-score" class="post-score" title="current number of votes">0</div><span id="post-51970-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You need to keep a close eye on the Round Trip Time. The shorter the distance the faster you get your ACKs back, and fast ACKs mean less bytes in flight. So the closer you get the smaller your bytes in flight get, and the less window size you need for full performance.</p><p>Did you calculate the optimum window size for both connections? I recommend this <a href="https://www.youtube.com/watch?v=3aXSCIWty7o">Youtube Video</a> to learn why it matters.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Apr '16, 13:00</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-51970" class="comments-container"></div><div id="comment-tools-51970" class="comment-tools"></div><div class="clear"></div><div id="comment-51970-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

