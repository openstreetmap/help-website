+++
type = "question"
title = "Missing bytes in Capture file"
description = '''Is it normal to see occasional missing bytes in capture file, TCP Acked Lost segment, while filtering through a TCP Stream?  The problem is resolved by reload the stream.'''
date = "2011-08-29T18:04:00Z"
lastmod = "2011-08-30T00:09:00Z"
weight = 5935
keywords = [ "bytes", "missing" ]
aliases = [ "/questions/5935" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Missing bytes in Capture file](/questions/5935/missing-bytes-in-capture-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5935-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it normal to see occasional missing bytes in capture file, TCP Acked Lost segment, while filtering through a TCP Stream?</p><p>The problem is resolved by reload the stream.</p></div><div id="question-tags" class="tags-container tags">bytes missing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Aug '11, 18:04</strong></p><img src="https://secure.gravatar.com/avatar/7fad942eca52b39316df3989023b87b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sharky7&#39;s gravatar image" /><p>Sharky7<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sharky7 has no accepted answers">0%</span></p></div></div><div id="comments-container-5935" class="comments-container"></div><div id="comment-tools-5935" class="comment-tools"></div><div class="clear"></div><div id="comment-5935-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5942"></span>

<div id="answer-container-5942" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5942-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, it is normal that sometimes not all packets that were on the wire are captured. This will result in "TCP acked Lost segment" messages. One common cause is port mirroring a full duplex port 100Mbit to a 100Mbit port, you can then have 200 Mbit of traffic, which obviously does not work on a 100Mbit port.</p><p>Another source of these problems is if your capturing device is unable to keep up with the data collection. If this is the case, make sure the device is not doing much other stuff than capturing. Don't run any other programs and disable "Show packets in real time". Or even better, you dumpcap instead of Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '11, 00:09</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5942" class="comments-container"></div><div id="comment-tools-5942" class="comment-tools"></div><div class="clear"></div><div id="comment-5942-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

