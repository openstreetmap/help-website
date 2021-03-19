+++
type = "question"
title = "Decode telnet session information"
description = '''Hello, I am using Wireshark for couples weeks. As I learning and searching the possibility... I would like to know If I can capture the password for a user created from a telnet. Ok here is the scenario. I have modem/router doing test at home. I can login to the device via telnet and wireshark is ab...'''
date = "2012-12-30T11:12:00Z"
lastmod = "2013-01-03T21:48:00Z"
weight = 17319
keywords = [ "telnet" ]
aliases = [ "/questions/17319" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Decode telnet session information](/questions/17319/decode-telnet-session-information)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17319-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am using Wireshark for couples weeks. As I learning and searching the possibility... I would like to know If I can capture the password for a user created from a telnet.</p><p>Ok here is the scenario. I have modem/router doing test at home. I can login to the device via telnet and wireshark is able to find the username and password easily. After, I wanted to go furthers. If I create a new user for that device and with new password in the telnet session. Am I able to see the password.</p><p>For your information, I was able to the see the username and the password with asterix as I typed in telnet session.</p><p>I hope I am clear on my question. Let me know If you need more information. Thank you Binarylock</p></div><div id="question-tags" class="tags-container tags">telnet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Dec '12, 11:12</strong></p><img src="https://secure.gravatar.com/avatar/e14366120a1ed9a23dbdad73aeb3f652?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BinaryLock&#39;s gravatar image" /><p>BinaryLock<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BinaryLock has no accepted answers">0%</span></p></div></div><div id="comments-container-17319" class="comments-container"></div><div id="comment-tools-17319" class="comment-tools"></div><div class="clear"></div><div id="comment-17319-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="17366"></span>

<div id="answer-container-17366" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17366-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you're seeing asterisks in wireshark, it's probably because you're looking at what the server sent BACK to your telent client to display... Since most systems won't display a password for you as you type it (to prevent someone from looking over your shoulder and seeing it on the screen, etc), the server is sending you asterisks to display as you type the new password... for instance, if you wanted to set the password to "password", you would first send the letter 'p'. so you press 'p', it sends an asterisk. you press 'a' and it sends another, and so forth. To see the password, you'd look at the packets you send out, not the ones you get sent in return.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Dec '12, 17:10</strong></p><img src="https://secure.gravatar.com/avatar/8c8bb4331d25d8ed8241358cecc41b39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="W-George&#39;s gravatar image" /><p>W-George<br />
<span class="score" title="20 reputation points">20</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="W-George has no accepted answers">0%</span></p></div></div><div id="comments-container-17366" class="comments-container"></div><div id="comment-tools-17366" class="comment-tools"></div><div class="clear"></div><div id="comment-17366-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17322"></span>

<div id="answer-container-17322" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17322-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I would like to know If I can capture the password for a user created from a telnet.</p></blockquote><p>yes.</p><blockquote><p>wireshark is able to find the username and password easily.</p></blockquote><p>as you were able to capture the password yourself, what is your question?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Dec '12, 14:47</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Dec '12, 14:48</p></div></div><div id="comments-container-17322" class="comments-container"><span id="17358"></span><div id="comment-17358" class="comment"><div id="post-17358-score" class="comment-score"></div><div class="comment-text"><p>No. I mean after login to the telnet session. I create a new user. I would like to know if I can see the password for that new user at the same time.</p></div><div id="comment-17358-info" class="comment-info"><span class="comment-age">(31 Dec '12, 09:35)</span> BinaryLock</div></div></div><div id="comment-tools-17322" class="comment-tools"></div><div class="clear"></div><div id="comment-17322-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17360"></span>

<div id="answer-container-17360" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17360-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As you saw, Wireshark was able to capture and display your telnet session, so yes, you will be able to see the new username and password during the user account creation process when you type them in and they're transmitted across the network. Telnet sessions are not encrypted. You will be able to see everything that takes place during the Telnet session.</p><p>Is there more to your question? Because it seems like you could have answered this for yourself in a matter of seconds just by going ahead and creating the new user and observing the results in Wireshark. Are you really asking if <em>someone else</em> can sniff that password?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Dec '12, 10:07</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-17360" class="comments-container"><span id="17362"></span><div id="comment-17362" class="comment"><div id="post-17362-score" class="comment-score"></div><div class="comment-text"><p>Yes I did create a user and as I mention in my first question, I can see the new user name created in wireshark and but not the password (the password is display with asterix in wireshark log)</p></div><div id="comment-17362-info" class="comment-info"><span class="comment-age">(31 Dec '12, 10:26)</span> BinaryLock</div></div><span id="17363"></span><div id="comment-17363" class="comment"><div id="post-17363-score" class="comment-score">1</div><div class="comment-text"><p>How are you viewing this? Have you tried Follow TCP Stream?</p><p>The password characters you type are transmitted across the network, so they must be present in the Wireshark trace. If the remote system is echoing back asterisks, then the password characters might be alternating with the asterisk characters in the Wireshark trace.</p><p>The default view for Follow TCP Stream is to show the entire conversation, but you can switch that to show only traffic in one direction. It might help you find the password if you show only traffic from the client to the server.</p></div><div id="comment-17363-info" class="comment-info"><span class="comment-age">(31 Dec '12, 10:45)</span> Jim Aragon</div></div></div><div id="comment-tools-17360" class="comment-tools"></div><div class="clear"></div><div id="comment-17360-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17424"></span>

<div id="answer-container-17424" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17424-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hello. Finally I was able to see the password for the new user too. Simple I had choose the option to read an entire conversation when I click Follow Tcp Stream. I retry severely times and it works very well.</p><p>Thank for everyone for your help.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jan '13, 21:48</strong></p><img src="https://secure.gravatar.com/avatar/e14366120a1ed9a23dbdad73aeb3f652?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BinaryLock&#39;s gravatar image" /><p>BinaryLock<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BinaryLock has no accepted answers">0%</span></p></div></div><div id="comments-container-17424" class="comments-container"></div><div id="comment-tools-17424" class="comment-tools"></div><div class="clear"></div><div id="comment-17424-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

