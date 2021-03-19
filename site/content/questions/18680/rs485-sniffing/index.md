+++
type = "question"
title = "RS485 sniffing"
description = '''I have two pieces of equipment that communicate with each of other via two RS485 signals (one for each direction). Think of a small box with displays, buttons and rotary encoders controlling a microprocessor on the other end. I eventually want to be able to replace the box with a PC or other control...'''
date = "2013-02-17T07:30:00Z"
lastmod = "2016-09-28T05:46:00Z"
weight = 18680
keywords = [ "rs485" ]
aliases = [ "/questions/18680" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [RS485 sniffing](/questions/18680/rs485-sniffing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18680-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have two pieces of equipment that communicate with each of other via two RS485 signals (one for each direction). Think of a small box with displays, buttons and rotary encoders controlling a microprocessor on the other end. I eventually want to be able to replace the box with a PC or other controller box but first I need to read and log all of the data transmitted so I can emulate it.</p><p>How can Wireshark be interfaced to tap into those lines and store the data?</p><p>Thanks, JJ</p></div><div id="question-tags" class="tags-container tags">rs485</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Feb '13, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/de6b50126862e2e7ee1b2a4064ec3a3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johnjohns&#39;s gravatar image" /><p>johnjohns<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johnjohns has no accepted answers">0%</span></p></div></div><div id="comments-container-18680" class="comments-container"></div><div id="comment-tools-18680" class="comment-tools"></div><div class="clear"></div><div id="comment-18680-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18682"></span>

<div id="answer-container-18682" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18682-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Do you have a capture file of the data and only need wireshark to be able to read and dissect the RS485 protocol data inside the capture file? Or do you need wireshark to be able to capture from an RS485 interface as well?</p><p>If the latter, it would be hard. If your RS485 is coming in on a USB (ie, a RS485-USB dongle), you might be able to capture it as discussed on the <a href="http://wiki.wireshark.org/Tools#USB_capture">tools page</a>.</p><p>For just dissecting an already captured file, it depends on the file format - i.e, if wireshark can already read the file format. If not, then you'll have to create a file format reader, which is discussed in the <a href="http://anonsvn.wireshark.org/wireshark/trunk/wiretap/README.developer">README.developer page</a> in wiretap directory of the source code. Once you can load and read a file format in wireshark, you'll need to write a dissector for the protocol to display/filter/etc. the data you want. You can either do that in C code, as discussed in the <a href="http://anonsvn.wireshark.org/wireshark/trunk/doc/README.developer">README.developer page</a> in the doc directory of the source, or you can write it in a Lua script, as discussed in the <a href="http://wiki.wireshark.org/Lua">Wireshark Lua wiki</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '13, 08:10</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-18682" class="comments-container"></div><div id="comment-tools-18682" class="comment-tools"></div><div class="clear"></div><div id="comment-18682-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="55940"></span>

<div id="answer-container-55940" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55940-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You may try the software to monitor your ports. Really simple - see all the activity and log at you PC screen. I use this one <a href="http://www.eltima.com/rs485-sniffer.html,">http://www.eltima.com/rs485-sniffer.html,</a> but you may try the others.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '16, 05:46</strong></p><img src="https://secure.gravatar.com/avatar/b56d4e47b62e5d1d7e13b16f642c46b5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GordonNelson&#39;s gravatar image" /><p>GordonNelson<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GordonNelson has no accepted answers">0%</span></p></div></div><div id="comments-container-55940" class="comments-container"></div><div id="comment-tools-55940" class="comment-tools"></div><div class="clear"></div><div id="comment-55940-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

