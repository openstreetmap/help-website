+++
type = "question"
title = "Seeing traffic from other machines on a switched network"
description = '''Greetings to all, I&#x27;ve captured traffic on a machine, which is connected to a switch. I should see only my traffic, multicasts and broadcasts. I will occasionally see traffic conversation from two machines, neither of which is mine. I check MAC addresses and IP addresses to make sure the traffic is ...'''
date = "2012-02-13T06:10:00Z"
lastmod = "2012-02-13T07:21:00Z"
weight = 8975
keywords = [ "traffic", "network" ]
aliases = [ "/questions/8975" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Seeing traffic from other machines on a switched network](/questions/8975/seeing-traffic-from-other-machines-on-a-switched-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8975-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings to all, I've captured traffic on a machine, which is connected to a switch. I should see only my traffic, multicasts and broadcasts. I will occasionally see traffic conversation from two machines, neither of which is mine. I check MAC addresses and IP addresses to make sure the traffic is legit,and it is. Has anyone else seen this, and do you know why? Thanks, SteveO</p></div><div id="question-tags" class="tags-container tags">traffic network</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '12, 06:10</strong></p><img src="https://secure.gravatar.com/avatar/53c492253a49e67b88ada9e311a0d019?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SteveOPA&#39;s gravatar image" /><p>SteveOPA<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SteveOPA has no accepted answers">0%</span></p></div></div><div id="comments-container-8975" class="comments-container"></div><div id="comment-tools-8975" class="comment-tools"></div><div class="clear"></div><div id="comment-8975-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8976"></span>

<div id="answer-container-8976" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8976-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please see the answers on <a href="http://ask.wireshark.org/questions/268/seeing-unicast-traffic-on-a-switchport-without-spanning">this similar question</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '12, 06:18</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Feb '12, 01:07</p></div></div><div id="comments-container-8976" class="comments-container"></div><div id="comment-tools-8976" class="comment-tools"></div><div class="clear"></div><div id="comment-8976-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8977"></span>

<div id="answer-container-8977" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8977-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Set up a port span or mirror to look at traffic from the machine of interest. Remember that the base design of a switch isolates traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '12, 07:21</strong></p><img src="https://secure.gravatar.com/avatar/b119c1795a1d51f2d7d0aa7af9c54a9f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dixglata&#39;s gravatar image" /><p>dixglata<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dixglata has no accepted answers">0%</span></p></div></div><div id="comments-container-8977" class="comments-container"></div><div id="comment-tools-8977" class="comment-tools"></div><div class="clear"></div><div id="comment-8977-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

