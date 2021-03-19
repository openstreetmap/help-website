+++
type = "question"
title = "tcp ack clocking and delays"
description = '''Hello, i am doing some tests to observ the behavior of ack clocking in tcp. i understand that there are many reasons that affect ack clocking such as the presence of bottleneck and the presence of delayed ack , but i do not understand why or WHEN exactly it is affected, can anyone explain that to me...'''
date = "2015-07-12T04:56:00Z"
lastmod = "2015-07-12T22:18:00Z"
weight = 44078
keywords = [ "ack", "delays", "bottleneck", "tcp", "clock" ]
aliases = [ "/questions/44078" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tcp ack clocking and delays](/questions/44078/tcp-ack-clocking-and-delays)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44078-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44078-score" class="post-score" title="current number of votes">0</div><span id="post-44078-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, i am doing some tests to observ the behavior of ack clocking in tcp. i understand that there are many reasons that affect ack clocking such as the presence of bottleneck and the presence of delayed ack , but i do not understand why or WHEN exactly it is affected, can anyone explain that to me ??</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-delays" rel="tag" title="see questions tagged &#39;delays&#39;">delays</span> <span class="post-tag tag-link-bottleneck" rel="tag" title="see questions tagged &#39;bottleneck&#39;">bottleneck</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-clock" rel="tag" title="see questions tagged &#39;clock&#39;">clock</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jul '15, 04:56</strong></p><img src="https://secure.gravatar.com/avatar/890399e77f2c0c0ff2f75ea2f43d3ff8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yas1234&#39;s gravatar image" /><p><span>yas1234</span><br />
<span class="score" title="16 reputation points">16</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yas1234 has no accepted answers">0%</span></p></div></div><div id="comments-container-44078" class="comments-container"></div><div id="comment-tools-44078" class="comment-tools"></div><div class="clear"></div><div id="comment-44078-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44080"></span>

<div id="answer-container-44080" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44080-score" class="post-score" title="current number of votes">0</div><span id="post-44080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This question is difficult to understand but i think I would suggest you read / watch:</p><p><a href="https://en.wikipedia.org/wiki/Transmission_Control_Protocol#Data_transfer">https://en.wikipedia.org/wiki/Transmission_Control_Protocol#Data_transfer</a></p><p>Probably paying special attention to Flow and Congestion control. I may get shot for this, but I also found this page useful as it explains things fairly simply:</p><p><a href="http://www.tcpipguide.com/free/t_TCPReliabilityandFlowControlFeaturesandProtocolMod.htm">http://www.tcpipguide.com/free/t_TCPReliabilityandFlowControlFeaturesandProtocolMod.htm</a></p><p>AFTER reading these pages at least, you should watch this video: <a href="https://www.youtube.com/watch?v=Rj3RaEtVlVY">https://www.youtube.com/watch?v=Rj3RaEtVlVY</a></p><p>And now you should understand ACK Clocking and flow control. The basic answer is: pretty much always when more than one link type / speed is in use.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jul '15, 15:32</strong></p><img src="https://secure.gravatar.com/avatar/05ba95262a3352e3af4ba69c0ec0dff2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DarrenWright&#39;s gravatar image" /><p><span>DarrenWright</span><br />
<span class="score" title="216 reputation points">216</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DarrenWright has 5 accepted answers">26%</span></p></div></div><div id="comments-container-44080" class="comments-container"><span id="44081"></span><div id="comment-44081" class="comment"><div id="post-44081-score" class="comment-score"></div><div class="comment-text"><p>i do understand ack clocking ..but this is all theory.. my problem is when comparing theory to what happens in reality it is different ...i need to know this difference why is it caused or at least when it is caused..any help</p></div><div id="comment-44081-info" class="comment-info"><span class="comment-age">(12 Jul '15, 15:49)</span> <span class="comment-user userinfo">yas1234</span></div></div><span id="44083"></span><div id="comment-44083" class="comment"><div id="post-44083-score" class="comment-score"></div><div class="comment-text"><p>It would certainly help if you provide a packet capture that shows the scenario that you want explained. Can you upload an example to <a href="https://appliance.cloudshark.org/upload/">https://appliance.cloudshark.org/upload/</a> ?</p></div><div id="comment-44083-info" class="comment-info"><span class="comment-age">(12 Jul '15, 22:18)</span> <span class="comment-user userinfo">mrEEde</span></div></div></div><div id="comment-tools-44080" class="comment-tools"></div><div class="clear"></div><div id="comment-44080-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

