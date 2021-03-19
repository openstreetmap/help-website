+++
type = "question"
title = "Location Of PC Running WireShark: Affects What I See?"
description = '''Within my home LAN&#x27;s topology, does the location of the PC running WireShark affect what WireShark sees? My agenda is that I just installed a VOIP gateway (IP addr 10.0.0.4) and, with WireShark running, expected to see a flurry of packets from 10.0.0.4 to somewhere outside of the LAN (the SIP). But ...'''
date = "2011-02-20T12:27:00Z"
lastmod = "2011-02-20T13:18:00Z"
weight = 2439
keywords = [ "basic" ]
aliases = [ "/questions/2439" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Location Of PC Running WireShark: Affects What I See?](/questions/2439/location-of-pc-running-wireshark-affects-what-i-see)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2439-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Within my home LAN's topology, does the location of the PC running WireShark affect what WireShark sees?</p><p>My agenda is that I just installed a VOIP gateway (IP addr 10.0.0.4) and, with WireShark running, expected to see a flurry of packets from 10.0.0.4 to somewhere outside of the LAN (the SIP).</p><p>But I see nothing.</p><p>Said VOIP gateway is connected directly to the only router - which is connected to a FIOS internet connection. Everything else, including the PC running WireShark, is connected to switches which, in turn, are connected to the router.</p></div><div id="question-tags" class="tags-container tags">basic</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Feb '11, 12:27</strong></p><img src="https://secure.gravatar.com/avatar/8bde5a113e61480e8111dcc2e49409f8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PeteCress&#39;s gravatar image" /><p>PeteCress<br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PeteCress has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Feb '11, 12:50</p></div></div><div id="comments-container-2439" class="comments-container"></div><div id="comment-tools-2439" class="comment-tools"></div><div class="clear"></div><div id="comment-2439-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2440"></span>

<div id="answer-container-2440" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2440-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>It is quite normal that you don't see anything of the VOIP gateway since it is connected to the router through a switch. Switches connect devices "directly", meaning that other devices on other ports will not see anything that goes on (which was what Hubs used to do: flood all packets to all ports).</p><p>If you want to capture the traffic of your VOIP gateway you have to "get into" the communication flow. This is usually done either by inserting a hub (or tap if you want to go Pro) into it's switch link, or by using a monitor port (which, unfortunately, is only an option if your switch is manageable). With a Monitor port you can tell the switch to send a copy of the communication between router and VOIP gateway to your PC, which is then capturing it using Wireshark.</p><p>If you have neither hub/tap nor monitor port option you're kinda out of luck, unless your VOIP gateway or router have capabilities to capture traffic themselves.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Feb '11, 13:18</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-2440" class="comments-container"><span id="2443"></span><div id="comment-2443" class="comment"><div id="post-2443-score" class="comment-score">1</div><div class="comment-text"><p>You can have a look at the <a href="http://wiki.wireshark.org/CaptureSetup">wireshark wiki</a> for more info on the placement of wireshark.</p></div><div id="comment-2443-info" class="comment-info"><span class="comment-age">(20 Feb '11, 14:03)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-2440" class="comment-tools"></div><div class="clear"></div><div id="comment-2440-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

