+++
type = "question"
title = "Learning to hack my own network"
description = '''I honestly am completely new to this, I want to learn and this was my first project.  How do I know which packets are important to me? This is a WEPA2 Secure network with a complex random password. '''
date = "2013-12-17T19:07:00Z"
lastmod = "2013-12-24T21:16:00Z"
weight = 28226
keywords = [ "password", "network" ]
aliases = [ "/questions/28226" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Learning to hack my own network](/questions/28226/learning-to-hack-my-own-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28226-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I honestly am completely new to this, I want to learn and this was my first project.</p><p>How do I know which packets are important to me? This is a WEPA2 Secure network with a complex random password.</p></div><div id="question-tags" class="tags-container tags">password network</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Dec '13, 19:07</strong></p><img src="https://secure.gravatar.com/avatar/a1f52f6dd314c98054bf7e77030712b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Takashi%20Hand&#39;s gravatar image" /><p>Takashi Hand<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Takashi Hand has no accepted answers">0%</span></p></div></div><div id="comments-container-28226" class="comments-container"></div><div id="comment-tools-28226" class="comment-tools"></div><div class="clear"></div><div id="comment-28226-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="28228"></span>

<div id="answer-container-28228" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28228-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Do you mean WEP, or WPA2? Cracking WEP is easy, and there are lots of tutorials you can google for that. Cracking WPA2 with a preshared key... that's not usually so easy. I would start with WEP if you're just looking for a 'secure' wireless network to break into.</p><p>For WPA, the only method I know is kind of lame. With a relatively weak eight-character passphrase (not out of the norm for many Wifi networks), if you intercept a valid WPA handshake from another device you can effectively do a dictionary attack against the key hash (use a tool or script to create a key hash based on a password guess and compare it to what you intercepted), or you might be able to use a precomputed hash table if the network is using a well-known SSID. Long, complex passphrases with an uncommon SSID make a WPA2 PSK network pretty hard to break to my knowledge, though I haven't followed this space for a few years now.</p><p>For a practical guide to breaking into Wifi networks, one of my favourite books on it would be: <a href="http://www.amazon.com/Wi-Foo-The-Secrets-Wireless-Hacking/dp/0321202171/ref=sr_sp-atf_image_1_1?ie=UTF8&amp;qid=1387342762&amp;sr=8-1&amp;keywords=wifoo">http://www.amazon.com/Wi-Foo-The-Secrets-Wireless-Hacking/dp/0321202171/ref=sr_sp-atf_image_1_1?ie=UTF8&amp;qid=1387342762&amp;sr=8-1&amp;keywords=wifoo</a></p><p>That's old, but it was a great overall reference guide for when I was studying this area, practically 10 years ago now. Wow.</p><p>Anyway, my advice is to read up on the subject and theory of how those networks work. I like to think of "Hacking" as Bart Simpson in that episode where Lisa was his babysitter, and when told to "go to bed" he went to his parent's room, as she failed to specify <em>which</em> bed. That is, hacking is really about exploiting or manipulating the rules of the protocol or security mechanism in use rather than actually breaking the rules, so you should learn the rules in play before figuring out how to best go about taking advantage of them or ultimately bypassing them.</p><p>Edit: I got carried away there a bit, but to answer on point the packets to care about for WPA2 are those of the four-way handshake from a valid host. That's if you're using the dictionary attack method against the passphrase.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '13, 21:14</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Dec '13, 21:23</p></div></div><div id="comments-container-28228" class="comments-container"></div><div id="comment-tools-28228" class="comment-tools"></div><div class="clear"></div><div id="comment-28228-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28378"></span>

<div id="answer-container-28378" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28378-score" class="post-score" title="current number of votes">-1</div></div></td><td><div class="item-right"><div class="answer-body"><p>youtube dot com</p><p>Learn how to filter out known good traffic</p><p>Download sample traces, sans have them etc</p><p>Best advice just start drilling down and understand what your seeing. It seems daunting at first but once you start looking you will begin to see. There is just to many ways to answer this question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Dec '13, 21:16</strong></p><img src="https://secure.gravatar.com/avatar/e5d5ba5d8ba47e0415a52577bf7bcc4a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rayyai%20beach&#39;s gravatar image" /><p>rayyai beach<br />
<span class="score" title="40 reputation points">40</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rayyai beach has no accepted answers">0%</span></p></div></div><div id="comments-container-28378" class="comments-container"></div><div id="comment-tools-28378" class="comment-tools"></div><div class="clear"></div><div id="comment-28378-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

