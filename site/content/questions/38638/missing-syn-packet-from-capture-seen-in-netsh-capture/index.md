+++
type = "question"
title = "Missing SYN packet from capture, seen in NETSH capture"
description = '''Greetings, in recent tshooting of a web application I have come across an issue where I do not see the SYN packet in the wireshark capture. In netstat I see the connection as Syn_Sent, however I don&#x27;t see the packet in the wireshark capture. I do however see the capture in a netsh trace. Any idea wh...'''
date = "2014-12-19T10:57:00Z"
lastmod = "2014-12-27T08:38:00Z"
weight = 38638
keywords = [ "syn" ]
aliases = [ "/questions/38638" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Missing SYN packet from capture, seen in NETSH capture](/questions/38638/missing-syn-packet-from-capture-seen-in-netsh-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38638-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings, in recent tshooting of a web application I have come across an issue where I do not see the SYN packet in the wireshark capture. In netstat I see the connection as Syn_Sent, however I don't see the packet in the wireshark capture. I do however see the capture in a netsh trace. Any idea why the packet isn't being captured with wireshark? Thanks in advance!</p></div><div id="question-tags" class="tags-container tags">syn</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Dec '14, 10:57</strong></p><img src="https://secure.gravatar.com/avatar/700c3d847f93cb9934f2d4f92a3073b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ziggy&#39;s gravatar image" /><p>Ziggy<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ziggy has no accepted answers">0%</span></p></div></div><div id="comments-container-38638" class="comments-container"><span id="38648"></span><div id="comment-38648" class="comment"><div id="post-38648-score" class="comment-score"></div><div class="comment-text"><p>I have had this on Windows 7 when the local firewall was dropping packets silently. Try looking there (would probably be the same on linux)</p></div><div id="comment-38648-info" class="comment-info"><span class="comment-age">(20 Dec '14, 14:46)</span> DarrenWright</div></div><span id="38688"></span><div id="comment-38688" class="comment"><div id="post-38688-score" class="comment-score"></div><div class="comment-text"><p>I actually first suspected windows firewall but I have turned it off in all network profiles with the same result. Thanks!</p></div><div id="comment-38688-info" class="comment-info"><span class="comment-age">(23 Dec '14, 16:29)</span> Ziggy</div></div></div><div id="comment-tools-38638" class="comment-tools"></div><div class="clear"></div><div id="comment-38638-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38736"></span>

<div id="answer-container-38736" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38736-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please read the questions with the following tags:</p><p><strong>outgoing</strong> or <strong>outbound</strong></p><blockquote><p><a href="http://ask.wireshark.org/tags/outgoing/">http://ask.wireshark.org/tags/outgoing/</a></p></blockquote><p>Usually the reason for this is some software on the capturing system (Enpoint Security, VPN, IPS, etc.) that prevents Wireshark from seeing outgoing/outbound packets. You'll find all the details in the other questions and answers.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Dec '14, 08:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-38736" class="comments-container"></div><div id="comment-tools-38736" class="comment-tools"></div><div class="clear"></div><div id="comment-38736-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

