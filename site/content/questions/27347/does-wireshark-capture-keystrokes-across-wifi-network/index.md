+++
type = "question"
title = "Does Wireshark capture keystrokes across wifi network"
description = '''Can wireshark be used as a keystroke logger for devices connected by wifi across the network'''
date = "2013-11-25T06:34:00Z"
lastmod = "2013-11-25T06:53:00Z"
weight = 27347
keywords = [ "keystroke" ]
aliases = [ "/questions/27347" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Does Wireshark capture keystrokes across wifi network](/questions/27347/does-wireshark-capture-keystrokes-across-wifi-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27347-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Can wireshark be used as a keystroke logger for devices connected by wifi across the network</p></div><div id="question-tags" class="tags-container tags">keystroke</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '13, 06:34</strong></p><img src="https://secure.gravatar.com/avatar/1f8411569073904dcb2570bc2786b012?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nathaniel&#39;s gravatar image" /><p>nathaniel<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nathaniel has no accepted answers">0%</span></p></div></div><div id="comments-container-27347" class="comments-container"></div><div id="comment-tools-27347" class="comment-tools"></div><div class="clear"></div><div id="comment-27347-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="27352"></span>

<div id="answer-container-27352" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27352-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Keystrokes are primarily transmitted between your keyboard and the chipset on your motherboard (keyboard controller).</p><p>There are only a few protocols where you actually transmit <strong>keystrokes</strong> over the network. That's mainly remote access methods where you actually log into a remote system, like telnet, ssh, RDP, etc. In those cases, you will be able to record the traffic that transmits the keystrokes but most of the protocols use encryption (except telnet), so you won't be able to identify single keystrokes, as you won't be able to decrypt the traffic (in most of the cases).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '13, 06:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Nov '13, 10:53</p></div></div><div id="comments-container-27352" class="comments-container"></div><div id="comment-tools-27352" class="comment-tools"></div><div class="clear"></div><div id="comment-27352-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

