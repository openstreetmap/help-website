+++
type = "question"
title = "if given an image size (in bytes), could you tell how many messages/packets the server would have to send"
description = '''Using wireshark, i was given an assignment to go to any webpage, right click on said image, goto properties and note the image size. Given this information, i used my browser to just request that one image. I was able to figure out how many packets it took for that image that was 6676 bytes. And if ...'''
date = "2011-11-14T20:47:00Z"
lastmod = "2011-11-14T23:28:00Z"
weight = 7435
keywords = [ "given", "packets", "image", "determine", "size" ]
aliases = [ "/questions/7435" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [if given an image size (in bytes), could you tell how many messages/packets the server would have to send](/questions/7435/if-given-an-image-size-in-bytes-could-you-tell-how-many-messagespackets-the-server-would-have-to-send)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7435-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Using wireshark, i was given an assignment to go to any webpage, right click on said image, goto properties and note the image size. Given this information, i used my browser to just request that one image. I was able to figure out how many packets it took for that image that was 6676 bytes. And if i did Wireshark correctly, i found that this image took 19 messages/packets to download.</p><p>So my question: "If i told you a given image was a certain size, could you tell me how many messages the server would have to send for that image?"</p><p>Please help!! Thank you in advance<br />
</p></div><div id="question-tags" class="tags-container tags">given packets image determine size</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '11, 20:47</strong></p><img src="https://secure.gravatar.com/avatar/bb40817ea7eb562720a2d8465df11201?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Justin%20Lien&#39;s gravatar image" /><p>Justin Lien<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Justin Lien has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-7435" class="comments-container"></div><div id="comment-tools-7435" class="comment-tools"></div><div class="clear"></div><div id="comment-7435-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7436"></span>

<div id="answer-container-7436" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7436-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That is virtually impossible to do. It depends on the (static) configuration of both sender and receiver TCP stack. Then it involves the implemented window scale / slow start / congestion avoidance options. And on top of that the path behavior, like packet loss and MTU limitations, influence what happens.</p><p>With so many unknowns it's impossible to accurately predict what will happen.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '11, 23:28</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-7436" class="comments-container"></div><div id="comment-tools-7436" class="comment-tools"></div><div class="clear"></div><div id="comment-7436-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

