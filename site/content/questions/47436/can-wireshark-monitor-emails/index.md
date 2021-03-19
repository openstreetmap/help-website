+++
type = "question"
title = "Can Wireshark monitor emails"
description = '''i would like to know if wireshark can monitor email that pass through my network, store it and notify me. is wireshark for mac available Also i would like to know if wireshark is a server-side or server-client side thanks.'''
date = "2015-11-09T12:40:00Z"
lastmod = "2015-11-09T18:29:00Z"
weight = 47436
keywords = [ "monitoring", "storage", "email", "notification" ]
aliases = [ "/questions/47436" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Can Wireshark monitor emails](/questions/47436/can-wireshark-monitor-emails)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47436-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i would like to know if wireshark can monitor email that pass through my network, store it and notify me. is wireshark for mac available</p><p>Also i would like to know if wireshark is a server-side or server-client side</p><p>thanks.</p></div><div id="question-tags" class="tags-container tags">monitoring storage email notification</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Nov '15, 12:40</strong></p><img src="https://secure.gravatar.com/avatar/289be086e5699d942335d3a9a9543e5b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yhomiid&#39;s gravatar image" /><p>yhomiid<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yhomiid has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Nov '15, 12:40</p></div></div><div id="comments-container-47436" class="comments-container"></div><div id="comment-tools-47436" class="comment-tools"></div><div class="clear"></div><div id="comment-47436-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="47443"></span>

<div id="answer-container-47443" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47443-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, it can, but in the form of network packets. You can reassemble them (manually) and store them. Notification - nope.</p><p>Wireshark is either side - doesn't matter if client, server or (best case) 3rd device in the middle.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '15, 15:05</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-47443" class="comments-container"></div><div id="comment-tools-47443" class="comment-tools"></div><div class="clear"></div><div id="comment-47443-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47444"></span>

<div id="answer-container-47444" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47444-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>i would like to know if wireshark can monitor email that pass through my network,</p></blockquote><p>Yes.</p><blockquote><p>store it</p></blockquote><p>Yes, with some extra manual work</p><blockquote><p>and notify me.</p></blockquote><p>No. Wireshark is a network troublshooting tool, not a network monitoring tool.</p><blockquote><p>is wireshark for mac available</p></blockquote><p>Yes. <a href="https://www.wireshark.org/#download">https://www.wireshark.org/#download</a></p><blockquote><p>Also i would like to know if wireshark is a server-side or server-client side</p></blockquote><p>Not sure what you are asking for! Wireshark is a piece of software that can be installed on any supported OS. As such, it's neither client- nor server-side. It's just software that you can install on a client system and/or on a server system.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '15, 15:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-47444" class="comments-container"></div><div id="comment-tools-47444" class="comment-tools"></div><div class="clear"></div><div id="comment-47444-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="47446"></span>

<div id="answer-container-47446" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47446-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>i would like to know if wireshark can monitor email that pass through my network,</p></blockquote><p>Its understanding of email is limited - it understands some e-mail protocols, and understands HTTP and HTTP2 so it can understand webmail to some degree, and understands some information about mail formats, but it's not designed as an e-mail monitoring program, so there's limits to what it can easily determine about the mail.</p><p>It's a passive sniffer program, so mail on your system doesn't pass <em>through</em> it, so it can't stop mail or modify it in flight, and if it can't keep up with network traffic, it won't see all the mail passing through your system.</p><blockquote><p>store it</p></blockquote><p>It's a sniffer, so what it captures is raw network traffic; that's what it stores, not e-mails.</p><blockquote><p>and notify me.</p></blockquote><p>It <em>might</em> be possible to write a Lua script that runs while Wireshark is running and sends notifications when it detects things in the packets it sees, but that would involve having the script look at raw network packet fields.</p><blockquote><p>is wireshark for mac available</p></blockquote><p>Yes, it runs on OS X, as well as a number of other OSes. The OS X versions are available from the Wireshark Web site.</p><blockquote><p>Also i would like to know if wireshark is a server-side or server-client side</p></blockquote><p>As it's a passive network sniffer, it can run on <em>any</em> machine that can see network traffic, whether it's the server, the client, or some third-party machine running in promiscuous or monitor mode, so the question doesn't apply. As I said above, it's not something that's in the data flow path for e-mail or any other form of network traffic - think of it as being like a phone tap where somebody can listen to your phone conversation.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '15, 18:29</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-47446" class="comments-container"></div><div id="comment-tools-47446" class="comment-tools"></div><div class="clear"></div><div id="comment-47446-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

