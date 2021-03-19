+++
type = "question"
title = "How to capture my Usb to lan and network card in the new version 2.0.3"
description = '''How can I capture my Usb to lan and network card in the new version 2.0.3. In the past I could choose from above menu capture, chose my network card, used a filter like udp port 123 and that&#x27;s it, but now I have USBcap1, 2 and 3 and can&#x27;t see witch device it is. And if I run it, can&#x27;t see my boardco...'''
date = "2016-06-06T07:40:00Z"
lastmod = "2016-06-06T08:41:00Z"
weight = 53238
keywords = [ "capture", "capture-filter", "networkinterfaces" ]
aliases = [ "/questions/53238" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture my Usb to lan and network card in the new version 2.0.3](/questions/53238/how-to-capture-my-usb-to-lan-and-network-card-in-the-new-version-203)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53238-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53238-score" class="post-score" title="current number of votes">0</div><span id="post-53238-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I capture my Usb to lan and network card in the new version 2.0.3. In the past I could choose from above menu capture, chose my network card, used a filter like udp port 123 and that's it, but now I have USBcap1, 2 and 3 and can't see witch device it is. And if I run it, can't see my boardcomputer data, it's something else. Please help, because I still want to use this tool.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-networkinterfaces" rel="tag" title="see questions tagged &#39;networkinterfaces&#39;">networkinterfaces</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jun '16, 07:40</strong></p><img src="https://secure.gravatar.com/avatar/24aee9d271342d9ee1f0b00e4ff668f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joffreyv&#39;s gravatar image" /><p><span>Joffreyv</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joffreyv has no accepted answers">0%</span></p></div></div><div id="comments-container-53238" class="comments-container"></div><div id="comment-tools-53238" class="comment-tools"></div><div class="clear"></div><div id="comment-53238-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53239"></span>

<div id="answer-container-53239" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53239-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53239-score" class="post-score" title="current number of votes">0</div><span id="post-53239-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Don't let the extended functionality confuse you. Since USBPcap has become part of Wireshark distribution, you can also capture USB communication, but you can still capture at the Ethernet interfaces, including the one of your USB-to-LAN card. So the USBpcap1, 2, 3 should be there <strong>in addition to</strong>, not <strong>instead of</strong>, the Ethernet interface(s), and they should definitely be listed <strong>below</strong> them.</p><p>If there are no other interfaces than USBpcap in your interface list, then there is something wrong with the WinPcap (or NPcap) installation or with the access privileges.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jun '16, 08:41</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-53239" class="comments-container"></div><div id="comment-tools-53239" class="comment-tools"></div><div class="clear"></div><div id="comment-53239-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

