+++
type = "question"
title = "Trying to capture traffic over local fiber metro e circuit?"
description = '''Hello - we are trying to capture traffic that passes over a Metro E circuit that connects two local offices on seperate networks (office1 is 192.168.1.xx and office2 is 192.168.10.xx). The Metro E circuit connects to an interface/port on a SonicWall router at each of the two respective locations.  W...'''
date = "2013-03-16T09:44:00Z"
lastmod = "2013-03-16T11:04:00Z"
weight = 19557
keywords = [ "e", "metro" ]
aliases = [ "/questions/19557" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Trying to capture traffic over local fiber metro e circuit?](/questions/19557/trying-to-capture-traffic-over-local-fiber-metro-e-circuit)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19557-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello - we are trying to capture traffic that passes over a Metro E circuit that connects two local offices on seperate networks (office1 is 192.168.1.xx and office2 is 192.168.10.xx). The Metro E circuit connects to an interface/port on a SonicWall router at each of the two respective locations.</p><p>We would like to configure Wireshark to capture packets over a 24 hour period of time so we can identify what IP addresses are generating the large intermittent packet fluctuations which are travelling over this Metro E circuit and exceed the designated bandwidth of the circuit.<br />
</p><p>Wireshark is curring installed on a server at office1 (192.168.1.xx) and when I try to create a remote interface to connect to a device at office2 (192.168.10.xx)I get the error message of: "Can't get a list of interfaces: the other host terminated the connection".<br />
</p><p>Can someone please advise? Many thanks in advance.<br />
</p></div><div id="question-tags" class="tags-container tags">e metro</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Mar '13, 09:44</strong></p><img src="https://secure.gravatar.com/avatar/9e14a6be3eb022df92a354b99f67abad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rainman13&#39;s gravatar image" /><p>Rainman13<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rainman13 has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-19557" class="comments-container"></div><div id="comment-tools-19557" class="comment-tools"></div><div class="clear"></div><div id="comment-19557-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19566"></span>

<div id="answer-container-19566" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19566-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Stop using Wireshark for long term capture. It's been said many times already, Wireshark builds up state from all traffic seen, eventually running out of memory.</p><p>There is a way do capture long term, by going for the dumpcap capture engine directly. It can capture and save multiple capture files until you exhaust your storage. It can trow away old captures as well, so this could run for ever.</p><p>Btw: the type of analysis you're trying to do is more suited for tools like <a href="http://www.riverbed.com/us/products/cascade/cascade_pilot.php">Pilot</a> from these guys ---&gt;&gt;</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Mar '13, 11:04</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span> </br></p></div></div><div id="comments-container-19566" class="comments-container"></div><div id="comment-tools-19566" class="comment-tools"></div><div class="clear"></div><div id="comment-19566-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19564"></span>

<div id="answer-container-19564" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19564-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>when I try to create a remote interface to connect to a device at office2 (192.168.10.xx)I get the error message of: "Can't get a list of interfaces: the other host terminated the connection".</p></blockquote><p>It sounds as if there's a problem with the rpcap server on the other host. You might want to run two instances of Wireshark on the server, and have the first one capture on whatever interface the server would use to talk to 192.168.10.xx (the device at office2) and, once that's capturing, try to create the remote interface and see what happens with the rpcap traffic to cause that error.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Mar '13, 10:51</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-19564" class="comments-container"><span id="19587"></span><div id="comment-19587" class="comment"><div id="post-19587-score" class="comment-score"></div><div class="comment-text"><p>Jaap - thanks for the info and will look into, but keep your patronizing attitude to yourself. This is a help forum.</p><p>Guy Harris - thanks as well I will look into that.</p></div><div id="comment-19587-info" class="comment-info"><span class="comment-age">(17 Mar '13, 08:53)</span> Rainman13</div></div></div><div id="comment-tools-19564" class="comment-tools"></div><div class="clear"></div><div id="comment-19564-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

