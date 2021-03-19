+++
type = "question"
title = "TCP Port numbers reused blast?"
description = '''Hey there, I am rather new to Wireshark and we are currently experiencing a problem where one of our HP Pro Curve 48 port switches is showing all solid lights. We have a rather large network over a small city and I&#x27;m having to find myself power cycle a firewall in order to have full connectivity for...'''
date = "2013-10-18T05:04:00Z"
lastmod = "2013-10-18T09:57:00Z"
weight = 26165
keywords = [ "reused", "port", "tcp", "wireshark" ]
aliases = [ "/questions/26165" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Port numbers reused blast?](/questions/26165/tcp-port-numbers-reused-blast)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26165-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey there,</p><p>I am rather new to Wireshark and we are currently experiencing a problem where one of our HP Pro Curve 48 port switches is showing all solid lights. We have a rather large network over a small city and I'm having to find myself power cycle a firewall in order to have full connectivity for only 3-4 hours until the problem persists. The funny part is when we go to run a capture while the switch is solid lights, I get a huge blast of [TCP Port numbers reused] packet errors to a point where Wireshark barely has time to keep up. I had the capture running for about 3-4 seconds and got 800,000 packets of this nature. Can anyone help me out to lead me in the right direction to fixing this?</p></div><div id="question-tags" class="tags-container tags">reused port tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '13, 05:04</strong></p><img src="https://secure.gravatar.com/avatar/c0eddfbd84e827362ef9e627f8aba102?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ineedamedic&#39;s gravatar image" /><p>Ineedamedic<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ineedamedic has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 18 Oct '13, 05:06</p></div></div><div id="comments-container-26165" class="comments-container"></div><div id="comment-tools-26165" class="comment-tools"></div><div class="clear"></div><div id="comment-26165-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="26166"></span>

<div id="answer-container-26166" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26166-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think that the reused TCP ports are your problem, it's probably a result of a much bigger issue. The scenario you describe sounds more like a layer 2 loop, where packets get duplicated while circling the net. Can you post a reasonable big sample capture on <a href="http://www.cloudshark.org">Cloudshark</a> (if not containing sensitive data)? If you can't post a capture maybe you can do a screen shot of a section that contains these reused port numbers?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '13, 06:55</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-26166" class="comments-container"><span id="26170"></span><div id="comment-26170" class="comment"><div id="post-26170-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately I can't post much. I'm seeing a certain subnet of our network hitting one particular IP address as the destination and this does not change. The interesting thing is that the IP Address is "as we know" turned off so it shouldn't be broadcasting anything at all. Essentially I have connectivity for all my users, they are just sending back high ping times... So I'm not totally disconnected from my network. I don't know if that helps or not.</p></div><div id="comment-26170-info" class="comment-info"><span class="comment-age">(18 Oct '13, 08:39)</span> Ineedamedic</div></div></div><div id="comment-tools-26166" class="comment-tools"></div><div class="clear"></div><div id="comment-26166-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26179"></span>

<div id="answer-container-26179" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26179-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I'm having to find myself <strong>power cycle a firewall</strong> in order <strong>to have full connectivity for only 3-4 hours</strong> until the problem persists.</p></blockquote><p>Sounds like a routing loop to me.</p><blockquote><p>I'm seeing a certain subnet of our network hitting one particular IP address as the destination and this does not change. The interesting thing is that the IP Address is "as we know" turned off.</p></blockquote><p>O.K. if it is a routing loop, it could be like this:</p><p>Firewall: host or subnet route for that 'dead' IP address (or subnet) to internal router R1<br />
R1: host or subnet route for that IP address (or subnet) to the firewall</p><p>The whole packet looping will start as soon as the first system tries to access the 'dead' IP address.</p><blockquote><p>I'm seeing a certain subnet of our network hitting one particular IP address as the destination and this does not change</p></blockquote><p>Please check if the IP TTL of those packets gets decreased constantly. If so, there is a route loop and then you need to check the routes on all involved systems. Start with the Firewall and work yourself further into the network.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '13, 09:57</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-26179" class="comments-container"></div><div id="comment-tools-26179" class="comment-tools"></div><div class="clear"></div><div id="comment-26179-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

