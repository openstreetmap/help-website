+++
type = "question"
title = "Trying to read DHCP packets between clients and servers"
description = '''Hi all, Sory I&#x27;m new to this and I&#x27;m trying to analyse the DHCP packets between clients and the servers. I don&#x27;t have that much information on the whole network. Will using bootp filter helps me to put together the whole flow ?  I can see thet 192.168.70.x are coming form clients and 192.168.100.1 s...'''
date = "2016-11-05T08:39:00Z"
lastmod = "2016-11-06T23:09:00Z"
weight = 57013
keywords = [ "dhcp" ]
aliases = [ "/questions/57013" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Trying to read DHCP packets between clients and servers](/questions/57013/trying-to-read-dhcp-packets-between-clients-and-servers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57013-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, Sory I'm new to this and I'm trying to analyse the DHCP packets between clients and the servers. I don't have that much information on the whole network. Will using bootp filter helps me to put together the whole flow ?</p><p>I can see thet 192.168.70.x are coming form clients and 192.168.100.1 seems to be the DHCP server ?</p><p><img src="https://osqa-ask.wireshark.org/upfiles/wireshark-dhcp.jpg" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">dhcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Nov '16, 08:39</strong></p><img src="https://secure.gravatar.com/avatar/149d6f8eb0595bad31c406551c9654a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="doran_lum&#39;s gravatar image" /><p>doran_lum<br />
<span class="score" title="11 reputation points">11</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="doran_lum has no accepted answers">0%</span></p></img></div></div><div id="comments-container-57013" class="comments-container"></div><div id="comment-tools-57013" class="comment-tools"></div><div class="clear"></div><div id="comment-57013-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="57017"></span>

<div id="answer-container-57017" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57017-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's it.</p><p>You can just use the display filter: bootp</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Nov '16, 14:00</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-57017" class="comments-container"></div><div id="comment-tools-57017" class="comment-tools"></div><div class="clear"></div><div id="comment-57017-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="57018"></span>

<div id="answer-container-57018" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57018-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can see the DHCP messages:</p><p>DHCP Discover - Client to server</p><p>DHCP Inform - Client to server</p><p>DHCP ACK - Server to Client</p><p>Further infos you can find here: <a href="https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol">https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Nov '16, 15:20</strong></p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Christian_R has 25 accepted answers">16%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Nov '16, 15:21</p></div></div><div id="comments-container-57018" class="comments-container"></div><div id="comment-tools-57018" class="comment-tools"></div><div class="clear"></div><div id="comment-57018-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="57036"></span>

<div id="answer-container-57036" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57036-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can also add the ethernet address(eth.addr) of the client and using "bootp". This will be a better filter as your nic might also capture Dhcp messages of other devices in the network.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Nov '16, 23:09</strong></p><img src="https://secure.gravatar.com/avatar/ed73b970d0135dbac8294249cdadff66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="koundi&#39;s gravatar image" /><p>koundi<br />
<span class="score" title="97 reputation points">97</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="koundi has no accepted answers">0%</span></p></div></div><div id="comments-container-57036" class="comments-container"></div><div id="comment-tools-57036" class="comment-tools"></div><div class="clear"></div><div id="comment-57036-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

