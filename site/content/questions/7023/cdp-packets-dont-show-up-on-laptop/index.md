+++
type = "question"
title = "cdp packets don&#x27;t show up on laptop"
description = '''Hi I&#x27;m trying to capture cdp and lldp packets from my cisco 2960 switch. This works just fine on a desktop computer but if i try to do the same thing on my laptop wireshark never gets the cdp packets at all. and i know it is being transmitted by the switch since my desktop works fine in the same net...'''
date = "2011-10-21T06:55:00Z"
lastmod = "2011-10-21T07:25:00Z"
weight = 7023
keywords = [ "switch", "laptop", "multicast", "cdp", "intel" ]
aliases = [ "/questions/7023" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [cdp packets don't show up on laptop](/questions/7023/cdp-packets-dont-show-up-on-laptop)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7023-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7023-score" class="post-score" title="current number of votes">0</div><span id="post-7023-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I'm trying to capture cdp and lldp packets from my cisco 2960 switch. This works just fine on a desktop computer but if i try to do the same thing on my laptop wireshark never gets the cdp packets at all.</p><p>and i know it is being transmitted by the switch since my desktop works fine in the same network port and is able to display the cdp packets.</p><p>The laptop is a hp 6930p with an intel network card, desktop is also an intel network card.</p><p>Is it possibel that the network card or drivers somehow filter out the cdp multicast traffic and never forward it? any advice on how to fix this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-switch" rel="tag" title="see questions tagged &#39;switch&#39;">switch</span> <span class="post-tag tag-link-laptop" rel="tag" title="see questions tagged &#39;laptop&#39;">laptop</span> <span class="post-tag tag-link-multicast" rel="tag" title="see questions tagged &#39;multicast&#39;">multicast</span> <span class="post-tag tag-link-cdp" rel="tag" title="see questions tagged &#39;cdp&#39;">cdp</span> <span class="post-tag tag-link-intel" rel="tag" title="see questions tagged &#39;intel&#39;">intel</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '11, 06:55</strong></p><img src="https://secure.gravatar.com/avatar/e495b06a4bc732e3eaa676408285777f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tobbe&#39;s gravatar image" /><p><span>tobbe</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tobbe has no accepted answers">0%</span></p></div></div><div id="comments-container-7023" class="comments-container"></div><div id="comment-tools-7023" class="comment-tools"></div><div class="clear"></div><div id="comment-7023-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7024"></span>

<div id="answer-container-7024" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7024-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7024-score" class="post-score" title="current number of votes">0</div><span id="post-7024-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I see no reason why the laptop should not show the CDP packets. Have you got VPN software installed? They are notorious for messing up capturing. Are you able to see other multcast traffic (HSRP for instance)?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '11, 07:12</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-7024" class="comments-container"><span id="7025"></span><div id="comment-7025" class="comment"><div id="post-7025-score" class="comment-score"></div><div class="comment-text"><p>thanks, i found the problem. mcafee host intrusion prevention software is interfering with the cdp packets. removing it makes the cdp packets show up correctly.</p><p>only vpn i have is the built in ms pptp.</p></div><div id="comment-7025-info" class="comment-info"><span class="comment-age">(21 Oct '11, 07:25)</span> <span class="comment-user userinfo">tobbe</span></div></div></div><div id="comment-tools-7024" class="comment-tools"></div><div class="clear"></div><div id="comment-7024-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

