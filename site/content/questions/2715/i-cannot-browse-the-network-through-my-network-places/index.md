+++
type = "question"
title = "I cannot browse the network through My Network Places"
description = '''When I try to browse my network through My Network Places I get the error that I do not have the permissions to do so. This has not been the case in the past. When I try to isolate the problem by disconnecting certain network switches, I am then able to browse the network and see the other computers...'''
date = "2011-03-08T13:38:00Z"
lastmod = "2011-03-09T02:10:00Z"
weight = 2715
keywords = [ "network" ]
aliases = [ "/questions/2715" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [I cannot browse the network through My Network Places](/questions/2715/i-cannot-browse-the-network-through-my-network-places)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2715-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I try to browse my network through My Network Places I get the error that I do not have the permissions to do so. This has not been the case in the past. When I try to isolate the problem by disconnecting certain network switches, I am then able to browse the network and see the other computers in the work group. I have it narrowed down to computers on one particular switch. When this part of the network is connected, the network browsing is no longer possible. What am I looking for in a capture with Wire Shark to diagnose this problem?</p></div><div id="question-tags" class="tags-container tags">network</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '11, 13:38</strong></p><img src="https://secure.gravatar.com/avatar/e269fcece82a14f3f029d4a7497090b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="servant&#39;s gravatar image" /><p>servant<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="servant has no accepted answers">0%</span></p></div></div><div id="comments-container-2715" class="comments-container"></div><div id="comment-tools-2715" class="comment-tools"></div><div class="clear"></div><div id="comment-2715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2721"></span>

<div id="answer-container-2721" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2721-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Since it's a permission issue, the thing in the capture that you will see are some packets that will basically tell you the same thing. This is not an issue you can solve at the network layer. You need to check the way your file-sharing has been set up. One thing that pops to my mind is that in Windows File sharing (on XP) you can select that it only accepts connections from the local subnet. So if the PC's on the particular switch are actually on another subnet, that might be your problem.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Mar '11, 02:10</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2721" class="comments-container"></div><div id="comment-tools-2721" class="comment-tools"></div><div class="clear"></div><div id="comment-2721-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

