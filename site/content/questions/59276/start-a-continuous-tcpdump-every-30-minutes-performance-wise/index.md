+++
type = "question"
title = "Start a continuous tcpdump every 30 Minutes (Performance wise)"
description = '''Dears, I&#x27;m having HP proliant Gen 9 server with 32G memory and I&#x27;m using CentOS 7, performance wise is it okay to start a continuous tcpdump on that server every 30 Minutes as well as after the file is ready i will do some analysis on it using tshark? Is that will affect the performance of the serve...'''
date = "2017-02-09T04:18:00Z"
lastmod = "2017-02-11T00:03:00Z"
weight = 59276
keywords = [ "tcpdump", "tshark" ]
aliases = [ "/questions/59276" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Start a continuous tcpdump every 30 Minutes (Performance wise)](/questions/59276/start-a-continuous-tcpdump-every-30-minutes-performance-wise)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59276-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59276-score" class="post-score" title="current number of votes">0</div><span id="post-59276-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dears, I'm having HP proliant Gen 9 server with 32G memory and I'm using CentOS 7, performance wise is it okay to start a continuous tcpdump on that server every 30 Minutes as well as after the file is ready i will do some analysis on it using tshark? Is that will affect the performance of the server? taking into considerations that I will use delete jobs to delete files older than two days because of storage limitations.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Feb '17, 04:18</strong></p><img src="https://secure.gravatar.com/avatar/4f4c71038b481a1afd55727cf2fcc885?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MYK&#39;s gravatar image" /><p><span>MYK</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MYK has no accepted answers">0%</span></p></div></div><div id="comments-container-59276" class="comments-container"></div><div id="comment-tools-59276" class="comment-tools"></div><div class="clear"></div><div id="comment-59276-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59292"></span>

<div id="answer-container-59292" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59292-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59292-score" class="post-score" title="current number of votes">0</div><span id="post-59292-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You might as well use dumpcap (the capture engine of Wireshark/Tshark) directly instead of tcpdump if you are not interested in real-time dissection. This just writes out the file (without dissection, but allows for capture filtering, just as tcpdump) so should be suitable for your use case. Generated load depends on network traffic density and disk IO performance.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '17, 07:44</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-59292" class="comments-container"><span id="59344"></span><div id="comment-59344" class="comment"><div id="post-59344-score" class="comment-score"></div><div class="comment-text"><p>We've found that the impact on CPU of tcpdump and dumpcap is minimal- you probably wouldn't even be able to measure it. Memory usage depends on the buffer setting for dumpcap and it's very small for tcpdump.</p><p>It's disk that gets hit hard. So the best thing to do is direct the output to a "quiet" or dedicated disk - we sometimes use USB disks wbich work well.</p><p>There's quite a lot of info on this subject in the Network Trace Capture section of the TribeLab site - see <a href="https://community.tribelab.com/course/view.php?id=10">https://community.tribelab.com/course/view.php?id=10</a></p></div><div id="comment-59344-info" class="comment-info"><span class="comment-age">(11 Feb '17, 00:03)</span> <span class="comment-user userinfo">PaulOfford</span></div></div></div><div id="comment-tools-59292" class="comment-tools"></div><div class="clear"></div><div id="comment-59292-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

