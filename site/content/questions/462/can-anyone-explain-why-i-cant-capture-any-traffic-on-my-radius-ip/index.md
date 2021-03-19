+++
type = "question"
title = "Can anyone explain why I can&#x27;t capture any traffic on my Radius IP?"
description = '''I&#x27;m trying to evauluate some wimax products with a Wimax Base Station and various client radios. I want to capture traffic over my Radius IP to see if EAP-Tls authentication is taking place. (which it is not currently). When I set wireshark to capture over the specific IP, I literally get nothing. H...'''
date = "2010-10-08T10:32:00Z"
lastmod = "2010-10-11T23:54:00Z"
weight = 462
keywords = [ "radius" ]
aliases = [ "/questions/462" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can anyone explain why I can't capture any traffic on my Radius IP?](/questions/462/can-anyone-explain-why-i-cant-capture-any-traffic-on-my-radius-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-462-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to evauluate some wimax products with a Wimax Base Station and various client radios. I want to capture traffic over my Radius IP to see if EAP-Tls authentication is taking place. (which it is not currently). When I set wireshark to capture over the specific IP, I literally get nothing. Hopefully someone has some insight.</p></div><div id="question-tags" class="tags-container tags">radius</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Oct '10, 10:32</strong></p><img src="https://secure.gravatar.com/avatar/9f3d5f541fb31f08f98153703f9eb702?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johnOup&#39;s gravatar image" /><p>johnOup<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johnOup has no accepted answers">0%</span></p></div></div><div id="comments-container-462" class="comments-container"><span id="465"></span><div id="comment-465" class="comment"><div id="post-465-score" class="comment-score"></div><div class="comment-text"><p>How's your capture setup?</p></div><div id="comment-465-info" class="comment-info"><span class="comment-age">(08 Oct '10, 14:08)</span> Jaap ♦</div></div></div><div id="comment-tools-462" class="comment-tools"></div><div class="clear"></div><div id="comment-462-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="484"></span>

<div id="answer-container-484" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-484-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>My assumption would be that your radius traffic is forwarded on a specific vlan and that you are capturing on a vlan tagged interface. In which case you should use "vlan and host &lt;ip&gt;" instead of "host &lt;ip&gt;" for the capture filter.</p><p>Of course that is just an assumption, please provide more details on your capture setup if this is not the case.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '10, 23:54</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-484" class="comments-container"></div><div id="comment-tools-484" class="comment-tools"></div><div class="clear"></div><div id="comment-484-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

