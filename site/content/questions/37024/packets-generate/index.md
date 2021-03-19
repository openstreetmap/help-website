+++
type = "question"
title = "Packets generate"
description = '''Hi Guys, I met a requirement from customer. they have several network elements which couldn&#x27;t send out the Netflow packets, but the traffic monitoring tool in their network want to fetch Netflow packet for analysis. so they are searching a tool to capture the original packets from Switch mirror port...'''
date = "2014-10-13T22:09:00Z"
lastmod = "2014-10-19T07:55:00Z"
weight = 37024
keywords = [ "netflows", "generate" ]
aliases = [ "/questions/37024" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Packets generate](/questions/37024/packets-generate)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37024-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37024-score" class="post-score" title="current number of votes">0</div><span id="post-37024-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Guys,</p><p>I met a requirement from customer.</p><p>they have several network elements which couldn't send out the Netflow packets, but the traffic monitoring tool in their network want to fetch Netflow packet for analysis. so they are searching a tool to capture the original packets from Switch mirror port and then convert to Netflow format packets.</p><p>the main idea as below: Step 1, the Tool receive original packets from switch mirror port; Step 2, the Tool read the original packets and write the packet header information to txt file with netflow format; Step 3, the Tool generate NETFLOW format packets based on the above txt file, and send out to the traffic monitoring tool.</p><p>I am thinking about the above methond but NOT sure if it is feasible. Hope to get some advices/suggestions for you.</p><p>Looking forward to your response.</p><p>thanks a lot.</p><p>Regards, Sam</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-netflows" rel="tag" title="see questions tagged &#39;netflows&#39;">netflows</span> <span class="post-tag tag-link-generate" rel="tag" title="see questions tagged &#39;generate&#39;">generate</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Oct '14, 22:09</strong></p><img src="https://secure.gravatar.com/avatar/e9d668dd28830dd8f79d4dbb56e5f2bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sam&#39;s gravatar image" /><p><span>Sam</span><br />
<span class="score" title="51 reputation points">51</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sam has no accepted answers">0%</span></p></div></div><div id="comments-container-37024" class="comments-container"></div><div id="comment-tools-37024" class="comment-tools"></div><div class="clear"></div><div id="comment-37024-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="37025"></span>

<div id="answer-container-37025" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37025-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37025-score" class="post-score" title="current number of votes">0</div><span id="post-37025-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think Wireshark or tshark are much help here, unless you want to spend a lot of effort on the steps 2 and 3, which you'd need to build yourself.</p><p>If they really want to do what you say they should look for Netflow probes, e.g. <a href="http://www.ntop.org/products/nprobe/">nProbe</a> or other "capture packets and send results as Netflow" solutions. I have tested commercial solutions like <a href="https://www.invea.com/en/products-and-services/flowmon/flowmon-probes">FlowMon Probe</a> myself, and they work as they should (but some cost money, of course :-))</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Oct '14, 01:08</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-37025" class="comments-container"><span id="37160"></span><div id="comment-37160" class="comment"><div id="post-37160-score" class="comment-score"></div><div class="comment-text"><p>thanks for your advice,Jasper. I am going to try the FlowMon, will get back to you.</p></div><div id="comment-37160-info" class="comment-info"><span class="comment-age">(19 Oct '14, 07:51)</span> <span class="comment-user userinfo">Sam</span></div></div></div><div id="comment-tools-37025" class="comment-tools"></div><div class="clear"></div><div id="comment-37025-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="37026"></span>

<div id="answer-container-37026" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37026-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37026-score" class="post-score" title="current number of votes">0</div><span id="post-37026-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Could <a href="https://code.google.com/p/softflowd/">this</a> be of help?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Oct '14, 01:18</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-37026" class="comments-container"><span id="37161"></span><div id="comment-37161" class="comment"><div id="post-37161-score" class="comment-score"></div><div class="comment-text"><p>softflowd is a nice and usefull tool. Softflowd can capture the original packets and to analyis them then output the netflow records. but how to generate the netflow records out to another tool which used to analysis netflow packets? by the way, what's that mean about the command 'softflowctl send-template'? where i can see the result if 'template' sent out?</p></div><div id="comment-37161-info" class="comment-info"><span class="comment-age">(19 Oct '14, 07:55)</span> <span class="comment-user userinfo">Sam</span></div></div></div><div id="comment-tools-37026" class="comment-tools"></div><div class="clear"></div><div id="comment-37026-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

