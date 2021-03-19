+++
type = "question"
title = "Wireshark Opening Ports?"
description = '''Hi, I have an unusual issue on one of our servers. The server (Windows 2008 R2) is running Digital Radio Software that logs everything that occurs on the Digital Radio Network. It appears that the packets are randomly dropped at random times - which leads to conversations being lost and other stats/...'''
date = "2015-08-31T16:50:00Z"
lastmod = "2015-08-31T17:12:00Z"
weight = 45554
keywords = [ "server2008", "radio", "wireshark" ]
aliases = [ "/questions/45554" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Opening Ports?](/questions/45554/wireshark-opening-ports)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45554-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have an unusual issue on one of our servers.</p><p>The server (Windows 2008 R2) is running Digital Radio Software that logs everything that occurs on the Digital Radio Network. It appears that the packets are randomly dropped at random times - which leads to conversations being lost and other stats/incidents.</p><p>For some strange reason when Wireshark is opened on this server, the packet loss ceases and everything runs fine.</p><p>I am at a loss as to why this would happen? I was under the impression that Wireshark doesn't open any ports and only listened to the traffic that came through the NIC?</p><p>If someone may be able to shed some light on this that would be appreciated.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">server2008 radio wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Aug '15, 16:50</strong></p><img src="https://secure.gravatar.com/avatar/84345ac508d543308f52acfde4579c78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="began&#39;s gravatar image" /><p>began<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="began has no accepted answers">0%</span></p></div></div><div id="comments-container-45554" class="comments-container"></div><div id="comment-tools-45554" class="comment-tools"></div><div class="clear"></div><div id="comment-45554-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45555"></span>

<div id="answer-container-45555" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45555-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark doesn't open any ports (except when checking for an update). My guess is that you have some layer 2 trouble where the radio packets are sent to the wrong MAC address at the random times you mention. Since Wireshark puts the interface into promiscuous mode it'll accept now packets that do not have the MAC of the interface. That way the packets with the wrong MAC are accepted, and there is no "loss".</p><p>You need to investigate your MAC addresses. My guess is that they change sometimes for whatever reason, so that when Wireshark is not running the connection is lost. Find out when that happens and what the changed MAC is/where it belongs, and you should be able to find the cause.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Aug '15, 17:12</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-45555" class="comments-container"><span id="45556"></span><div id="comment-45556" class="comment"><div id="post-45556-score" class="comment-score">1</div><div class="comment-text"><p>Try capturing in Wireshark <em>without</em> turning promiscuous mode on. If you see the packet drops when Wireshark is running without turning promiscuous mode on, then it's probably as Jasper described.</p></div><div id="comment-45556-info" class="comment-info"><span class="comment-age">(31 Aug '15, 17:58)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-45555" class="comment-tools"></div><div class="clear"></div><div id="comment-45555-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

