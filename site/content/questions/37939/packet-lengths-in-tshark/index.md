+++
type = "question"
title = "Packet Lengths in Tshark"
description = '''How do I view the packet lengths report in TShark. I.e the one via &#x27;Statistics / Packet Lengths&#x27; in Wireshark. Thanks,'''
date = "2014-11-18T01:32:00Z"
lastmod = "2014-11-19T09:31:00Z"
weight = 37939
keywords = [ "tshark" ]
aliases = [ "/questions/37939" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Packet Lengths in Tshark](/questions/37939/packet-lengths-in-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37939-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do I view the packet lengths report in TShark. I.e the one via 'Statistics / Packet Lengths' in Wireshark.</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags">tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '14, 01:32</strong></p><img src="https://secure.gravatar.com/avatar/22baebd906c29ccfcb5b2aeb350b22fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bart80&#39;s gravatar image" /><p>bart80<br />
<span class="score" title="11 reputation points">11</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bart80 has no accepted answers">0%</span></p></div></div><div id="comments-container-37939" class="comments-container"></div><div id="comment-tools-37939" class="comment-tools"></div><div class="clear"></div><div id="comment-37939-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37973"></span>

<div id="answer-container-37973" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37973-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can try the following command</p><blockquote><p>tshark -nr input.pcap -q -z plen,tree</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Nov '14, 09:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-37973" class="comments-container"></div><div id="comment-tools-37973" class="comment-tools"></div><div class="clear"></div><div id="comment-37973-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

