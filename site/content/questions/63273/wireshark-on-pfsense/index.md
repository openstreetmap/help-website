+++
type = "question"
title = "Wireshark on pfSense"
description = '''Hello, i have more problems with wireshark. On my network i have pfSense product and i want to install wireshark on pfSense? is it possible ? If possible,how can i do it? So one more, My pfsense products has 6 ports which i get from 2 ISP and i do load balancing and failover, is there anyway to use ...'''
date = "2017-07-31T23:54:00Z"
lastmod = "2017-08-01T00:59:00Z"
weight = 63273
keywords = [ "capture" ]
aliases = [ "/questions/63273" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark on pfSense](/questions/63273/wireshark-on-pfsense)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63273-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, i have more problems with wireshark. On my network i have pfSense product and i want to install wireshark on pfSense? is it possible ? If possible,how can i do it?</p><p>So one more, My pfsense products has 6 ports which i get from 2 ISP and i do load balancing and failover, is there anyway to use wireshark by install on a pc and connect it to port of pfsense and capture it ?</p></div><div id="question-tags" class="tags-container tags">capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jul '17, 23:54</strong></p><img src="https://secure.gravatar.com/avatar/4f4ad0afe443c29cea2e036509acb2d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Samann&#39;s gravatar image" /><p>Samann<br />
<span class="score" title="5 reputation points">5</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Samann has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Aug '17, 18:57</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-63273" class="comments-container"></div><div id="comment-tools-63273" class="comment-tools"></div><div class="clear"></div><div id="comment-63273-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63276"></span>

<div id="answer-container-63276" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63276-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I would recommend just using the packet capture feature on pfSense (in the "Diagnostics" menu, "Packet Capture") and download the capture file afterwards to look at it in Wireshark. You don't have a GUI in pfSense anyway, so I doubt you could install Wireshark.</p><p>The other option you have is to connect to the box via SSH (or locally) and use TCPdump.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '17, 00:59</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-63276" class="comments-container"></div><div id="comment-tools-63276" class="comment-tools"></div><div class="clear"></div><div id="comment-63276-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

