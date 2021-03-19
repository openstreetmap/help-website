+++
type = "question"
title = "EAPOL handshake, and then?"
description = '''Hi, I am only starting to use Wireshark on my MacbookPro, not so familiar with networking. I&#x27;m trying to spy on my home network, just for fun and as an exercise to learn about networks and hacking. I know Wireshark is supposed to be an appropriate tool for what I am trying to do, but I am still tryi...'''
date = "2015-11-28T08:42:00Z"
lastmod = "2015-11-28T10:08:00Z"
weight = 48044
keywords = [ "handshake", "wifi", "http", "monitor", "eapol" ]
aliases = [ "/questions/48044" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [EAPOL handshake, and then?](/questions/48044/eapol-handshake-and-then)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48044-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am only starting to use Wireshark on my MacbookPro, not so familiar with networking. I'm trying to spy on my home network, just for fun and as an exercise to learn about networks and hacking. I know Wireshark is supposed to be an appropriate tool for what I am trying to do, but I am still trying.... eheh. I capture with promiscuous mode and monitor mode enables, 802.11 plus radiotap header chosen, my wpa-psk and wpa-pwd keys provided to the Shark, and I managed to capture the 4 EAPOL packets from my cellphone and was able to get the HTTP packets I am looking for. So I guess it would work just the same with the other devices connected to my network (computers, other cellphones, etc.) My question is: Is there a way that I don't have to reset every devices every time I want to monitor my network's activity. That is not very convenient and I though Wireshark was the right tool to do exactly that (monitor a network's activity).</p><p>Maybe I got lost in the tutorials and there is an easier way to do what I wan't to do?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">handshake wifi http monitor eapol</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Nov '15, 08:42</strong></p><img src="https://secure.gravatar.com/avatar/59c88a2a6b37bab5dfbb493f83198cca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="p1020175&#39;s gravatar image" /><p>p1020175<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="p1020175 has no accepted answers">0%</span></p></div></div><div id="comments-container-48044" class="comments-container"></div><div id="comment-tools-48044" class="comment-tools"></div><div class="clear"></div><div id="comment-48044-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48045"></span>

<div id="answer-container-48045" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48045-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In simple words, the very purpose of encryption is that the wireless communication would not be easy to intercept. Use of a relatively short and fixed value encryption key (password) to encrypt a lot of data (i.e. for a long time) would make it way too easy for someone else to decipher it and use it to decrypt the communication. To prevent this, the keys used to encrypt the communication session are generated dynamically (and from time to time replaced by new ones during the session) and the static password is only used to encrypt their exchange between the parties when the communication is established - which is the EAPOL negotiation. So knowledge of the static password (the "WPA-PSK key") allows you to decrypt the whole communication, but only if you have access to the (recording of) this initial phase and can thus decipher the exchange between the parties of the encryption keys used later during communication.</p><p>A good news for you might be that to capture the EAPOL negotiation it should not be necessary to reboot the devices. Switching off and on their WiFi interfaces (or an attempt, even an unsuccessful one, to use another WiFi network, followed by re-connection to your own WiFi) should be enough.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Nov '15, 10:08</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-48045" class="comments-container"><span id="48047"></span><div id="comment-48047" class="comment"><div id="post-48047-score" class="comment-score"></div><div class="comment-text"><p>Shorter version: it's <em>deliberately designed</em> to be hard. :-)</p><p>But, yes, either turning the Wi-Fi on and off, or putting the machine to sleep and waking it up, should be sufficient.</p></div><div id="comment-48047-info" class="comment-info"><span class="comment-age">(28 Nov '15, 12:04)</span> Guy Harris ♦♦</div></div><span id="48049"></span><div id="comment-48049" class="comment"><div id="post-48049-score" class="comment-score"></div><div class="comment-text"><p>Thank you both for your answers! It's working! Now I still have to make sense of all the information, but that's a work in progress. :-)</p></div><div id="comment-48049-info" class="comment-info"><span class="comment-age">(28 Nov '15, 14:02)</span> p1020175</div></div></div><div id="comment-tools-48045" class="comment-tools"></div><div class="clear"></div><div id="comment-48045-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

