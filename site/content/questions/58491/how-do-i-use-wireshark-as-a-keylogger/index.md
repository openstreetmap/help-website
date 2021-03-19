+++
type = "question"
title = "How do I use Wireshark as a keylogger?"
description = '''I&#x27;m very new to this software but because of some recent discoveries about our daughter&#x27;s internet use, we are very suspicious. We would like to extend some freedom to her and have agreed on the &quot;trust but monitor&quot; tactic. Can someone point me in the right direction for learning how to use Wireshark...'''
date = "2017-01-03T18:03:00Z"
lastmod = "2017-01-04T02:20:00Z"
weight = 58491
keywords = [ "keylogger", "key" ]
aliases = [ "/questions/58491" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do I use Wireshark as a keylogger?](/questions/58491/how-do-i-use-wireshark-as-a-keylogger)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58491-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm very new to this software but because of some recent discoveries about our daughter's internet use, we are very suspicious. We would like to extend some freedom to her and have agreed on the "trust but monitor" tactic. Can someone point me in the right direction for learning how to use Wireshark as a keylogger?</p></div><div id="question-tags" class="tags-container tags">keylogger key</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jan '17, 18:03</strong></p><img src="https://secure.gravatar.com/avatar/a0c28238846ba197b92f0ec0a652a139?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="djattracta&#39;s gravatar image" /><p>djattracta<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="djattracta has no accepted answers">0%</span></p></div></div><div id="comments-container-58491" class="comments-container"></div><div id="comment-tools-58491" class="comment-tools"></div><div class="clear"></div><div id="comment-58491-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="58494"></span>

<div id="answer-container-58494" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58494-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark can only act as a keylogger, in the sense of a program that monitors <em>keystrokes</em>, if the keyboard being used is a hardware keyboard that connects to a host over a network that Wireshark can sniff.</p><p>If the keyboard you're trying to monitor is a software keyboard on a smartphone or tablet, that won't work.</p><p>If it's a USB keyboard plugged into a personal computer, that'd work only if you could tap the USB connection, which can currently be done by Wireshark only by running it on the personal computer; that currently only works if the machine is running Linux or Windows. Furthermore, you may get a lot of USB traffic that's not relevant to the keyboard.</p><p>If it's a wireless Bluetooth keyboard, that'd work only if you could tap the Bluetooth connection, which would only work on Linux and only work if you ran Wireshark on the machine to which the keyboard is communicating, or if you could do Bluetooth passive sniffing, which could only be done with Ubertooth hardware.</p><p>So that's going to be difficult at best and impossible at worst.</p><p>If, however, you want to watch the <em>network</em> traffic to and from her machine, see Jaap's comment; you <em>might</em> be able to limit the traffic by finding out the MAC address of her machine, so you would only see that traffic. As for encryption, you would probably be able to decrypt traffic that's encrypted at the Wi-Fi level, by supplying the password for the network, <strong><em>IF</em></strong> you happen to capture the initial connection of her machine to the network. Capturing that would be tricky, though, if you didn't have the ability to turn the machine on and off.</p><p>If the machine is portable, such as a smartphone, tablet, or laptop, the <em>only</em> way you're going to be able to completely monitor its use would be by installing a program on the machine and having it run continuously, capturing traffic while it's running. That won't be possible on an Apple iPhone or iPad or iPod touch (Wireshark doesn't work on them, for various technical and Apple policy reasons, and neither do other sniffer programs). It <em>might</em> be possible on a laptop, but, in any case, you're going to need some way to grab the capture files from the machine.</p><p>And, in both that case and the other "capture network traffic" case, that won't be enough to decrypt encrypted Web traffic; there will probably be a <em>lot</em> of that, and it's tricky, at best, to decrypt.</p><p>So this isn't necessarily going to be easy to do with Wireshark, if it's doable at all. A lot of networking technologies (such as SSL/TLS, as used for encrypted Web traffic) were deliberately <em>designed</em> to make it hard to do what you want to do....</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '17, 02:20</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-58494" class="comments-container"></div><div id="comment-tools-58494" class="comment-tools"></div><div class="clear"></div><div id="comment-58494-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="58493"></span>

<div id="answer-container-58493" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58493-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Don't go there. Wireshark is a network analyser, not the monitor tool you seek. You'll be swamped in other network traffic and most, if not all, data you seek will be encrypted on the network anyway, out of your reach.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jan '17, 00:38</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-58493" class="comments-container"></div><div id="comment-tools-58493" class="comment-tools"></div><div class="clear"></div><div id="comment-58493-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

