+++
type = "question"
title = "How to find MAC Address of Default Gateway ?"
description = '''This is my first question here. I am on a LAN and I need to find the MAC Address for my default gateway. Googling out said that I have to use packet capture to do this, so I want to use Wireshark. Thanks.'''
date = "2014-04-04T04:26:00Z"
lastmod = "2014-04-04T04:37:00Z"
weight = 31505
keywords = [ "mac-address" ]
aliases = [ "/questions/31505" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to find MAC Address of Default Gateway ?](/questions/31505/how-to-find-mac-address-of-default-gateway)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31505-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This is my first question here. I am on a LAN and I need to find the MAC Address for my default gateway. Googling out said that I have to use packet capture to do this, so I want to use Wireshark. Thanks.</p></div><div id="question-tags" class="tags-container tags">mac-address</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Apr '14, 04:26</strong></p><img src="https://secure.gravatar.com/avatar/6ce37cc4d5a8f7cbbc0cc568576e8d8b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sreyan32&#39;s gravatar image" /><p>sreyan32<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sreyan32 has no accepted answers">0%</span></p></div></div><div id="comments-container-31505" class="comments-container"></div><div id="comment-tools-31505" class="comment-tools"></div><div class="clear"></div><div id="comment-31505-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31506"></span>

<div id="answer-container-31506" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31506-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>No need to use Wireshark, even though you could. It is usually much easier just to use a couple of system commands to find that one out.</p><p>E.g. on Windows, run "ipconfig /all" on a command line to see the IP address of your gateway. Then ping that IP. Finally, run "arp -a" and find the gateway IP. Next to it you'll see the MAC address.</p><p>If you want to do it with Wireshark, ping the gateway and capture the ICMP packets. Look at the ethernet layer for the echo request destination MAC.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Apr '14, 04:37</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-31506" class="comments-container"><span id="31507"></span><div id="comment-31507" class="comment"><div id="post-31507-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper</p></div><div id="comment-31507-info" class="comment-info"><span class="comment-age">(04 Apr '14, 04:42)</span> sreyan32</div></div></div><div id="comment-tools-31506" class="comment-tools"></div><div class="clear"></div><div id="comment-31506-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

