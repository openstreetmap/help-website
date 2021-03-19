+++
type = "question"
title = "Detecting Network Issue - Help"
description = '''Hi, Im new to this network analyzing and am trying to understand it more. I have a network issue on the company network that im trying to troubleshoot without much luck at the moment. Im hoping someone on here may be able to point me in the right direction so I can find the cause. The issue we have ...'''
date = "2010-09-20T04:44:00Z"
lastmod = "2010-10-12T06:24:00Z"
weight = 226
keywords = [ "devices", "ping", "network", "timeout" ]
aliases = [ "/questions/226" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Detecting Network Issue - Help](/questions/226/detecting-network-issue-help)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-226-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-226-score" class="post-score" title="current number of votes">0</div><span id="post-226-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Im new to this network analyzing and am trying to understand it more. I have a network issue on the company network that im trying to troubleshoot without much luck at the moment. Im hoping someone on here may be able to point me in the right direction so I can find the cause.</p><p>The issue we have is as soon as a network device is turned on it causes network timeouts (tested using "ping" to multiple devices, get timeouts to all devices pinged except switches). It can be a PC or Printer. As im sure you can imagine this causes big problems, the network may only drop for one second but its enough to cause problems. This becomes a nightmare when people come in and start their PC's in the morning.</p><p>I can easily replicate the problem by simply turning a device off then back on so that should make the troubleshooting easier, I just need to know what to look for and what to ignor.</p><p>Any help would be greatly appreciated.</p><p>Thanks Dan</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-devices" rel="tag" title="see questions tagged &#39;devices&#39;">devices</span> <span class="post-tag tag-link-ping" rel="tag" title="see questions tagged &#39;ping&#39;">ping</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span> <span class="post-tag tag-link-timeout" rel="tag" title="see questions tagged &#39;timeout&#39;">timeout</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Sep '10, 04:44</strong></p><img src="https://secure.gravatar.com/avatar/74453d122addabfa22a05c7f76da93d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xiztrn&#39;s gravatar image" /><p><span>xiztrn</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xiztrn has no accepted answers">0%</span></p></div></div><div id="comments-container-226" class="comments-container"></div><div id="comment-tools-226" class="comment-tools"></div><div class="clear"></div><div id="comment-226-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="229"></span>

<div id="answer-container-229" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-229-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-229-score" class="post-score" title="current number of votes">1</div><span id="post-229-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>So only your switch remains up, while all active devices on it's connected ports drop off? I would take a very serious look at that switch. Spanning Tree problems? Someone looped back a switch port to another?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '10, 08:40</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-229" class="comments-container"><span id="440"></span><div id="comment-440" class="comment"><div id="post-440-score" class="comment-score"></div><div class="comment-text"><p>I agree with xiztrn. I would also take a hard look at the hardware itself. You could easily have a corrupt flash or the switch may simply be dying. Can you provide details on make model and OS?</p></div><div id="comment-440-info" class="comment-info"><span class="comment-age">(06 Oct '10, 07:25)</span> <span class="comment-user userinfo">blacknight</span></div></div><span id="487"></span><div id="comment-487" class="comment"><div id="post-487-score" class="comment-score"></div><div class="comment-text"><p>Please provide more detail regarding the device and how it's connected to upstream network devices (switch, routers, firewall, etc). Spanning Tree can be confusing and difficult to diagnose. Also check out VTP, if it's in use, to see if the new switch is trying to push a conflicting vlan database.</p></div><div id="comment-487-info" class="comment-info"><span class="comment-age">(12 Oct '10, 06:24)</span> <span class="comment-user userinfo">GeonJay</span></div></div></div><div id="comment-tools-229" class="comment-tools"></div><div class="clear"></div><div id="comment-229-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

