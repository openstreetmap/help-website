+++
type = "question"
title = "I want to hide ICMP"
description = '''Hello there, Is there any possibilities to hide this ICMP? I just only to see syslog on my screen. One more thing is there any fastest way to save this syslog? via text file, notepad, Ms word etc. Its urgent please do help. Thank you.'''
date = "2013-01-19T06:25:00Z"
lastmod = "2013-01-19T16:36:00Z"
weight = 17789
keywords = [ "icmp" ]
aliases = [ "/questions/17789" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [I want to hide ICMP](/questions/17789/i-want-to-hide-icmp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17789-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello there,</p><p>Is there any possibilities to hide this ICMP? I just only to see syslog on my screen.</p><p>One more thing is there any fastest way to save this syslog? via text file, notepad, Ms word etc. Its urgent please do help.</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">icmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Jan '13, 06:25</strong></p><img src="https://secure.gravatar.com/avatar/ee02cd89c18de063cbaca8d3df7d394a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FirstSystems&#39;s gravatar image" /><p>FirstSystems<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FirstSystems has no accepted answers">0%</span></p></div></div><div id="comments-container-17789" class="comments-container"></div><div id="comment-tools-17789" class="comment-tools"></div><div class="clear"></div><div id="comment-17789-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17794"></span>

<div id="answer-container-17794" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17794-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>And to <em>capture</em> only non-ICMP traffic, use the capture filter "not icmp".</p><p>To capture only syslog traffic, you'd have to base that on the port number.</p><p>For the traditional syslog-over-UDP, as described in <a href="http://tools.ietf.org/html/rfc5426">RFC 5426</a>, "udp port syslog" would work on most systems, and, on those that don't, "udp port 514" would work.</p><p>For syslog-over-TCP, as described in <a href="http://tools.ietf.org/html/rfc3195">RFC 3195</a>, "tcp port syslog-conn" would work, at least if it's using the standard port, on most systems, and, on those where it doesn't work, "tcp port 601" would work. Wireshark <em>can</em> dissect that, but you'd need to use "Decode As...".</p><p>For syslog-over-TLS, as described in <a href="http://tools.ietf.org/html/rfc5425">RFC 5425</a>, use "tcp port 6514", but I'm not sure Wireshark dissects that (even if you have the certificates necessary to decrypt it).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jan '13, 16:36</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-17794" class="comments-container"></div><div id="comment-tools-17794" class="comment-tools"></div><div class="clear"></div><div id="comment-17794-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17793"></span>

<div id="answer-container-17793" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17793-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>To exclude ICMP traffic from the Wireshark display, apply the display filter "!icmp".</p><p>To show only syslog traffic, and hide all other traffic, use the display filter "syslog".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jan '13, 14:10</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-17793" class="comments-container"></div><div id="comment-tools-17793" class="comment-tools"></div><div class="clear"></div><div id="comment-17793-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

