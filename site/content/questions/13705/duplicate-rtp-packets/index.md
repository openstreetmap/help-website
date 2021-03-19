+++
type = "question"
title = "Duplicate RTP packets"
description = '''I have a customer trace that is showing duplicate RTP packets (lost RTP packets shows a negative number). My span session on a Cisco 2940 is only spanning the interface, not the VLAN and is correct:- monitor session 1 source interface fa0/1 monitor session 1 destination interface fa0/8 encaps dot1q ...'''
date = "2012-08-17T07:32:00Z"
lastmod = "2012-08-17T09:48:00Z"
weight = 13705
keywords = [ "span", "rtp" ]
aliases = [ "/questions/13705" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Duplicate RTP packets](/questions/13705/duplicate-rtp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13705-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a customer trace that is showing duplicate RTP packets (lost RTP packets shows a negative number). My span session on a Cisco 2940 is only spanning the interface, not the VLAN and is correct:-</p><p>monitor session 1 source interface fa0/1</p><p>monitor session 1 destination interface fa0/8 encaps dot1q</p><p>However, after taking the trace I found that both data &amp; voice all use the same VLAN (OK poor network design).</p><p>Is it possible to build a display filter to show the duplicate packets, so as I can set up a color filter to show them?</p></div><div id="question-tags" class="tags-container tags">span rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Aug '12, 07:32</strong></p><img src="https://secure.gravatar.com/avatar/030196d67dc4e2b8f4ecff65eefdb63e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KeithFrench&#39;s gravatar image" /><p>KeithFrench<br />
<span class="score" title="121 reputation points">121</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KeithFrench has no accepted answers">0%</span></p></div></div><div id="comments-container-13705" class="comments-container"></div><div id="comment-tools-13705" class="comment-tools"></div><div class="clear"></div><div id="comment-13705-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13708"></span>

<div id="answer-container-13708" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13708-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You will need to find a criteria you can filter on. It should be one value for the "originals" and another for the duplicates. If you don't have exact byte-by-byte duplicates this should be possible; often you can use the VLAN ID (if you have duplicate packets on different VLANs) or the TTL (which is usually 1 less after the packet was routed). If you can find a criteria that works for you just right click on the field in the decode and select "Apply as Filter -&gt; selected" to filter the packets. You get the other half by negating the filter.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Aug '12, 09:48</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-13708" class="comments-container"></div><div id="comment-tools-13708" class="comment-tools"></div><div class="clear"></div><div id="comment-13708-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

