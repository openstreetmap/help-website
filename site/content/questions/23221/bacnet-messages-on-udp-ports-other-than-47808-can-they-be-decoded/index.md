+++
type = "question"
title = "BACnet messages on UDP ports other than 47808, can they be decoded?"
description = '''We have BACnet system configured using ports 47811. While using wireshark for analysis, we found BACnet messages on port 47811 is not recognized.'''
date = "2013-07-22T04:39:00Z"
lastmod = "2013-07-22T05:22:00Z"
weight = 23221
keywords = [ "bacnet", "udp", "ports" ]
aliases = [ "/questions/23221" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [BACnet messages on UDP ports other than 47808, can they be decoded?](/questions/23221/bacnet-messages-on-udp-ports-other-than-47808-can-they-be-decoded)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23221-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We have BACnet system configured using ports 47811. While using wireshark for analysis, we found BACnet messages on port 47811 is not recognized.</p></div><div id="question-tags" class="tags-container tags">bacnet udp ports</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jul '13, 04:39</strong></p><img src="https://secure.gravatar.com/avatar/2316851967e2bd6a203db14ebd777e26?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RP_1985&#39;s gravatar image" /><p>RP_1985<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RP_1985 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jul '13, 06:04</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-23221" class="comments-container"></div><div id="comment-tools-23221" class="comment-tools"></div><div class="clear"></div><div id="comment-23221-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="23224"></span>

<div id="answer-container-23224" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23224-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>Jasper is close, but the packets have to be UDP, and then you can select the BVLC (BACNet Virtual Link Control) protocol.</p><p>BVLC also has preferences for additional UDP ports, so you can add another port there so you don't need to "Decode As" for each new capture.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '13, 05:22</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-23224" class="comments-container"><span id="23226"></span><div id="comment-23226" class="comment"><div id="post-23226-score" class="comment-score"></div><div class="comment-text"><p>I tried it on TCP and UDP, but didn't know about it being called "BVLC" :)</p></div><div id="comment-23226-info" class="comment-info"><span class="comment-age">(22 Jul '13, 06:10)</span> Jasper ♦♦</div></div><span id="23227"></span><div id="comment-23227" class="comment"><div id="post-23227-score" class="comment-score"></div><div class="comment-text"><p>I had to look at the code to find out.</p></div><div id="comment-23227-info" class="comment-info"><span class="comment-age">(22 Jul '13, 06:12)</span> grahamb ♦</div></div><span id="23312"></span><div id="comment-23312" class="comment"><div id="post-23312-score" class="comment-score"></div><div class="comment-text"><p>Thanks, grahamb,,,that's right...</p></div><div id="comment-23312-info" class="comment-info"><span class="comment-age">(23 Jul '13, 21:59)</span> RP_1985</div></div><span id="23315"></span><div id="comment-23315" class="comment"><div id="post-23315-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-23315-info" class="comment-info"><span class="comment-age">(23 Jul '13, 23:18)</span> grahamb ♦</div></div></div><div id="comment-tools-23224" class="comment-tools"></div><div class="clear"></div><div id="comment-23224-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23223"></span>

<div id="answer-container-23223" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23223-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Usually I'd say you should try to use the popup menu on a packet that is not recognized and use the "Decode As" option to tell Wireshark how to decode the packet. But when I tested this I haven't seen anything called "BACnet", and it isn't listed in the protocol section of the preferences either. Maybe you can spot the correct protocol name though, in case it is not exactly called "BACnet".</p><p>Other than that it is possible that Wireshark does not decode your protocol at all, or have you seen it work on other ports?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '13, 05:08</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jul '13, 05:09</p></div></div><div id="comments-container-23223" class="comments-container"></div><div id="comment-tools-23223" class="comment-tools"></div><div class="clear"></div><div id="comment-23223-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

