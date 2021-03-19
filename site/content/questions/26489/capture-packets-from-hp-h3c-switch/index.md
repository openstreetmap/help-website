+++
type = "question"
title = "Capture packets from HP H3C switch"
description = '''Hello, I want to configure a source port on a HP H3C switch and a destination port on a Cisco C60 endpoint to be able to capture packets with WireShark. Any ideas?'''
date = "2013-10-28T14:12:00Z"
lastmod = "2013-10-30T15:13:00Z"
weight = 26489
keywords = [ "packets" ]
aliases = [ "/questions/26489" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture packets from HP H3C switch](/questions/26489/capture-packets-from-hp-h3c-switch)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26489-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I want to configure a source port on a HP H3C switch and a destination port on a Cisco C60 endpoint to be able to capture packets with WireShark. Any ideas?</p></div><div id="question-tags" class="tags-container tags">packets</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Oct '13, 14:12</strong></p><img src="https://secure.gravatar.com/avatar/17c1c7fe5152970a2ac9b694abac733d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="willJ&#39;s gravatar image" /><p>willJ<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="willJ has no accepted answers">0%</span></p></div></div><div id="comments-container-26489" class="comments-container"></div><div id="comment-tools-26489" class="comment-tools"></div><div class="clear"></div><div id="comment-26489-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26555"></span>

<div id="answer-container-26555" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26555-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You need to configure port mirroring on your H3C switch</p><blockquote><p><a href="http://www.h3c.com/portal/Products___Solutions/Technology/LAN/Configuration_Example/200805/605777_57_0.htm">http://www.h3c.com/portal/Products___Solutions/Technology/LAN/Configuration_Example/200805/605777_57_0.htm</a></p></blockquote><p>Basically, you need to mirror the port of your C60 to the port of your Wireshark PC. If you don't know how to do that, please ask your local H3C guru.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Oct '13, 15:13</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-26555" class="comments-container"><span id="26562"></span><div id="comment-26562" class="comment"><div id="post-26562-score" class="comment-score"></div><div class="comment-text"><p>Thanks - I've added an entry for that to the <a href="http://wiki.wireshark.org/SwitchReference/HewlettPackard">SwitchReference/HewlettPackard</a> page in the Wireshark Wiki, and added a "see HP" note for H3C on the <a href="http://wiki.wireshark.org/SwitchReference">SwitchReference</a> page. Those pages are good references for port mirroring/spanning/whatever-the-vendor-calls-it for various switch types; it's a wiki, so feel free to add more information.</p></div><div id="comment-26562-info" class="comment-info"><span class="comment-age">(31 Oct '13, 00:36)</span> Guy Harris ♦♦</div></div><span id="26569"></span><div id="comment-26569" class="comment"><div id="post-26569-score" class="comment-score"></div><div class="comment-text"><blockquote><p>it's a wiki, so feel free to add more information.</p></blockquote><p>I did not realize that is an open Wiki. As most of the articles are from developers I kind of thought that access to the Wiki is limited to developers, thus I did not even try to add/modify something. Thanks for that hint.</p></div><div id="comment-26569-info" class="comment-info"><span class="comment-age">(31 Oct '13, 02:57)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-26555" class="comment-tools"></div><div class="clear"></div><div id="comment-26555-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

