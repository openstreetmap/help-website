+++
type = "question"
title = "How do you capture Serial (COM) communications?"
description = '''I want to wireshark the packets being sent and received via the serial port on my computer, it is a windows xp. How can I go about this?'''
date = "2013-07-22T10:30:00Z"
lastmod = "2017-02-28T07:51:00Z"
weight = 23243
keywords = [ "serial-port", "wireshark" ]
aliases = [ "/questions/23243" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [How do you capture Serial (COM) communications?](/questions/23243/how-do-you-capture-serial-com-communications)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23243-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to wireshark the packets being sent and received via the serial port on my computer, it is a windows xp. How can I go about this?</p></div><div id="question-tags" class="tags-container tags">serial-port wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jul '13, 10:30</strong></p><img src="https://secure.gravatar.com/avatar/e661c0281b898e9380a9d059c9c083bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="julianv23&#39;s gravatar image" /><p>julianv23<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="julianv23 has no accepted answers">0%</span></p></div></div><div id="comments-container-23243" class="comments-container"></div><div id="comment-tools-23243" class="comment-tools"></div><div class="clear"></div><div id="comment-23243-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="25780"></span>

<div id="answer-container-25780" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25780-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If the answer is still actual:</p><p>COM port sniffer for Windows - <a href="http://www.eltima.com/products/serial-port-monitor/">http://www.eltima.com/products/serial-port-monitor/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Oct '13, 00:52</strong></p><img src="https://secure.gravatar.com/avatar/c1e56d059f913f3cd73c1f844a4e6af6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DavidTurner&#39;s gravatar image" /><p>DavidTurner<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DavidTurner has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Oct '13, 00:53</p></div></div><div id="comments-container-25780" class="comments-container"></div><div id="comment-tools-25780" class="comment-tools"></div><div class="clear"></div><div id="comment-25780-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23251"></span>

<div id="answer-container-23251" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-23251-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can't capture traffic of a COM port (serial Port) on Windows with Wireshark, as the capturing library (WinPcap) does not support this.</p><p>What you need is a <strong>COM port sniffer for Windows</strong>. Please google that. You will find tools like these:</p><blockquote><p><a href="http://www.serial-port-monitor.com/">http://www.serial-port-monitor.com/</a><br />
<a href="http://technet.microsoft.com/en-us/sysinternals/bb896644.aspx">http://technet.microsoft.com/en-us/sysinternals/bb896644.aspx</a></p></blockquote><p>BTW: There seems to be a way to capture serial port traffic with Wireshark and named pipes. However, you would need a <strong>helper tool</strong>.</p><blockquote><p><a href="http://www.wireshark.org/lists/wireshark-dev/201003//msg00020.html">http://www.wireshark.org/lists/wireshark-dev/201003//msg00020.html</a></p></blockquote><p>I think it's easier to go for the COM port sniffers I mentioned first.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jul '13, 14:24</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-23251" class="comments-container"></div><div id="comment-tools-23251" class="comment-tools"></div><div class="clear"></div><div id="comment-23251-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="50939"></span>

<div id="answer-container-50939" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50939-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is a great product I've been using for years if you haven't already seen it <a href="http://www.stratusengineering.com/product/ez-tap-pro/">http://www.stratusengineering.com/product/ez-tap-pro/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '16, 11:36</strong></p><img src="https://secure.gravatar.com/avatar/5cf80f787a80f72f33f38ebeca4bf9bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mike2408&#39;s gravatar image" /><p>mike2408<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mike2408 has no accepted answers">0%</span></p></div></div><div id="comments-container-50939" class="comments-container"></div><div id="comment-tools-50939" class="comment-tools"></div><div class="clear"></div><div id="comment-50939-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="59730"></span>

<div id="answer-container-59730" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59730-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I capture any serial data with the software - <a href="http://www.eltima.com/products/serial-port-monitor/">http://www.eltima.com/products/serial-port-monitor/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '17, 07:51</strong></p><img src="https://secure.gravatar.com/avatar/900c1e543eeca6049a10bda28e475606?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MicF&#39;s gravatar image" /><p>MicF<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MicF has no accepted answers">0%</span></p></div></div><div id="comments-container-59730" class="comments-container"></div><div id="comment-tools-59730" class="comment-tools"></div><div class="clear"></div><div id="comment-59730-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

