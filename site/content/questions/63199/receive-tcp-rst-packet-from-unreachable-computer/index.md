+++
type = "question"
title = "Receive TCP RST packet from unreachable computer"
description = '''Today I had a opportunity to work with wireshark. I installed wireshark on my VMware and made some test on it. And I found a interesting thing. I sent the HTTP request to not exist computer and captured the all packet flow with wireshark. The first packet was SYN packet. And second one was re-transm...'''
date = "2017-07-28T00:48:00Z"
lastmod = "2017-07-28T01:32:00Z"
weight = 63199
keywords = [ "rst", "unreachable", "tcp", "wireshark" ]
aliases = [ "/questions/63199" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Receive TCP RST packet from unreachable computer](/questions/63199/receive-tcp-rst-packet-from-unreachable-computer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63199-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Today I had a opportunity to work with wireshark.</p><p>I installed wireshark on my VMware and made some test on it.</p><p>And I found a interesting thing.</p><p>I sent the HTTP request to not exist computer and captured the all packet flow with wireshark.</p><p>The first packet was SYN packet.</p><p>And second one was re-transmission packet.(for system hadn't received any response from target computer).</p><p>But surprisingly, RST packet from the target computer reached.</p><p>I couldn't understand where this packet came from.</p><p>I tested for 2 target computers, and in both case, I had the RST packet.</p><p>So are there anyone answer about those suspicious RST packets?</p><p>Thanks for reading.</p><p>Regards.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/img2_fpJSr9b.png" alt="alt text" /> <img src="https://osqa-ask.wireshark.org/upfiles/img3_Rxmvejp.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">rst unreachable tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jul '17, 00:48</strong></p><img src="https://secure.gravatar.com/avatar/15784d27665eb4346511164b3f34785e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Takuya%20Kimura&#39;s gravatar image" /><p>Takuya Kimura<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Takuya Kimura has no accepted answers">0%</span></p></img></div></div><div id="comments-container-63199" class="comments-container"></div><div id="comment-tools-63199" class="comment-tools"></div><div class="clear"></div><div id="comment-63199-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63202"></span>

<div id="answer-container-63202" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63202-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The most likely explanation is that a security device exists on the route towards the IP address of the non-existent computer, and that device forges the RST packet in the name of the nonexistent computer.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jul '17, 01:32</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></img></div></div><div id="comments-container-63202" class="comments-container"></div><div id="comment-tools-63202" class="comment-tools"></div><div class="clear"></div><div id="comment-63202-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

