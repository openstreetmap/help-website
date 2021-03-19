+++
type = "question"
title = "Missing IP"
description = '''Hi I have a PC with Wireshark installed, the program starts and runs OK but only sees a few IP addresses on the network - there are 1000 public &amp;amp; private IP addresses. Am I missing something fundamental?'''
date = "2012-01-12T11:55:00Z"
lastmod = "2012-01-12T12:08:00Z"
weight = 8353
keywords = [ "ip" ]
aliases = [ "/questions/8353" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Missing IP](/questions/8353/missing-ip)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8353-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I have a PC with Wireshark installed, the program starts and runs OK but only sees a few IP addresses on the network - there are 1000 public &amp; private IP addresses. Am I missing something fundamental?</p></div><div id="question-tags" class="tags-container tags">ip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jan '12, 11:55</strong></p><img src="https://secure.gravatar.com/avatar/11776f84d6e8d1f0bd2c24fd9c1bf602?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stevewarden0&#39;s gravatar image" /><p>stevewarden0<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stevewarden0 has no accepted answers">0%</span></p></div></div><div id="comments-container-8353" class="comments-container"></div><div id="comment-tools-8353" class="comment-tools"></div><div class="clear"></div><div id="comment-8353-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8355"></span>

<div id="answer-container-8355" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8355-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yep: :)</p><p>Undoubtedly, your PC is on a switch which will send to your PC only packets addressed to your PC (and also broadcasts).</p><p>For more info see:</p><p><a href="http://wiki.wireshark.org/CaptureSetup">http://wiki.wireshark.org/CaptureSetup</a></p><p><a href="http://www.wireshark.org/faq.html#promiscsniff">http://www.wireshark.org/faq.html#promiscsniff</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '12, 12:05</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Jan '12, 12:10</p></div></div><div id="comments-container-8355" class="comments-container"></div><div id="comment-tools-8355" class="comment-tools"></div><div class="clear"></div><div id="comment-8355-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8356"></span>

<div id="answer-container-8356" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8356-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You are probably behind a switch of some sort within your network. You should read the <a href="http://wiki.wireshark.org/CaptureSetup" title="CaptureSetup">Capture Setup</a> article on the <a href="http://wiki.wireshark.org/" title="http://wiki.wireshark.org/">Wireshark wiki</a>; specifically try to understand the <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet#Switched_Ethernet">Switched Ethernet</a> section. Additionally, you may want to look at the <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet#Switched_Ethernet">Wireshark User's Guide</a> for more information.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jan '12, 12:08</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-8356" class="comments-container"></div><div id="comment-tools-8356" class="comment-tools"></div><div class="clear"></div><div id="comment-8356-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

