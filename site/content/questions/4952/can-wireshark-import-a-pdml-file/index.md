+++
type = "question"
title = "Can Wireshark import a PDML file?"
description = '''I want to alter the xml/pdml file, and then reloaded it in wireshark and resave it as a pcap file. Is this at all possible?'''
date = "2011-07-08T07:11:00Z"
lastmod = "2011-07-08T08:11:00Z"
weight = 4952
keywords = [ "import" ]
aliases = [ "/questions/4952" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can Wireshark import a PDML file?](/questions/4952/can-wireshark-import-a-pdml-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4952-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to alter the xml/pdml file, and then reloaded it in wireshark and resave it as a pcap file. Is this at all possible?</p></div><div id="question-tags" class="tags-container tags">import</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jul '11, 07:11</strong></p><img src="https://secure.gravatar.com/avatar/779116af28645038c6697334d527eb10?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ROCKSTARARTIST&#39;s gravatar image" /><p>ROCKSTARARTIST<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ROCKSTARARTIST has no accepted answers">0%</span></p></div></div><div id="comments-container-4952" class="comments-container"></div><div id="comment-tools-4952" class="comment-tools"></div><div class="clear"></div><div id="comment-4952-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4955"></span>

<div id="answer-container-4955" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4955-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think it is possible with the Wireshark tools, but I might be mistaken.</p><p>But if you're trying to alter an xml/pdml file just to modify a pcap trace that you already have I would recommend avoiding the export to text and reimporting it - instead, I'd go for tools that can modify pcaps directly. I've shown a couple of tools in my talk on Sharkfest this year, so you can look the presentation (A-11) up in the review section here: <a href="http://sharkfest.wireshark.org/sharkfest.11/index.html">http://sharkfest.wireshark.org/sharkfest.11/index.html</a></p><p>If you're trying to modify layers beyond the transport layer those tools won't help you though; in that case you're probably going to have to edit them with a hex/text editor.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '11, 08:11</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jul '11, 08:13</p></div></div><div id="comments-container-4955" class="comments-container"><span id="4957"></span><div id="comment-4957" class="comment"><div id="post-4957-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your answer and in linking an informative presentation. Unfortunately I am trying to modify layers beyond TCP/IP, and the majority of the tools that I have found do not assist me in that regard, and I am trying to avoid the hex/text editor approach. I am taking at look at SCAPY, which is a python PCAP editor that allows you to describe your own layers... we will see how that goes.</p></div><div id="comment-4957-info" class="comment-info"><span class="comment-age">(08 Jul '11, 09:04)</span> ROCKSTARARTIST</div></div><span id="4972"></span><div id="comment-4972" class="comment"><div id="post-4972-score" class="comment-score"></div><div class="comment-text"><p>Besides <a href="http://www.secdev.org/projects/scapy/">scapy</a>, you might also want to look into <a href="http://netexpect.org/wiki">netexpect</a> and <a href="http://code.google.com/p/packetfu/">packetfu</a>. Packetfu was just presented at Sharkfest '11 by Tod Beardsley of the <a href="http://www.metasploit.com/">Metasploit</a> project. Tod's presentation is listed as the "<a href="http://prezi.com/mw0_9qfb2d6d/packetfu-by-example/">A-3 PacketFu by Example</a>" presentation at the Sharkfest '11 retrospective page that <a href="http://ask.wireshark.org/users/145/jasper/">Jasper</a> referenced above.</p></div><div id="comment-4972-info" class="comment-info"><span class="comment-age">(10 Jul '11, 17:06)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-4955" class="comment-tools"></div><div class="clear"></div><div id="comment-4955-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

