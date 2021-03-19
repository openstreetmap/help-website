+++
type = "question"
title = "Capturing Packets Between 2 Remote Systems"
description = '''Is is possible to capture TCP packets traveling between two remote systems that are not directed to the Wireshark host computer? I need to intercept traffic between an old Redhat Linux 2.4 computer and a discontinued 20-year-old machine that is controlled via TCP/IP in order to analyze it&#x27;s communic...'''
date = "2017-10-19T09:55:00Z"
lastmod = "2017-10-19T10:33:00Z"
weight = 64029
keywords = [ "remote" ]
aliases = [ "/questions/64029" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing Packets Between 2 Remote Systems](/questions/64029/capturing-packets-between-2-remote-systems)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64029-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is is possible to capture TCP packets traveling between two remote systems that are not directed to the Wireshark host computer?</p><p>I need to intercept traffic between an old Redhat Linux 2.4 computer and a discontinued 20-year-old machine that is controlled via TCP/IP in order to analyze it's communication protocol so I can control it with a modern computer. All systems are connected via a legacy Netgear Hub. I am able to open a Telnet connection and capture packets between the Wireshark computer and the machine, but I cannot see any traffic traveling directly between the Redhat Linux computer and the machine.</p><p>The IP addresses are as follows:</p><p>Wireshark Computer (Windows 10) - 192.168.200.68</p><p>3rd Party Equipment (Not a Computer) - 192.168.200.63, 192.168.200.64, 192.168.200.65</p><p>Redhad Linux 2.4 Computer - Unknown, Probably something like 192.168.200.67</p><p>Is there a way to do this?</p></div><div id="question-tags" class="tags-container tags">remote</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '17, 09:55</strong></p><img src="https://secure.gravatar.com/avatar/84e4e0eca8f98b778f0b41fec5db25f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dcs&#39;s gravatar image" /><p>dcs<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dcs has no accepted answers">0%</span></p></div></div><div id="comments-container-64029" class="comments-container"></div><div id="comment-tools-64029" class="comment-tools"></div><div class="clear"></div><div id="comment-64029-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="64030"></span>

<div id="answer-container-64030" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64030-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Capturing packets requires access to the physical connection the packets travel trough. They won't take a detour to your Wireshark PC, you have to put your Wireshark were they are visible. In your case the hub would be a perfect spot, but you need to be connected directly to it and it really needs to be a hub (some "hubs" are switches in reality, and you won't see the packets).</p><p>For more information on capture setups, check the following links:</p><p><a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">https://wiki.wireshark.org/CaptureSetup/Ethernet</a></p><p><a href="https://blog.packet-foo.com/2016/10/the-network-capture-playbook-part-1-ethernet-basics/">https://blog.packet-foo.com/2016/10/the-network-capture-playbook-part-1-ethernet-basics/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '17, 10:15</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-64030" class="comments-container"><span id="64032"></span><div id="comment-64032" class="comment"><div id="post-64032-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the quick answers.</p><p>To Jasper, I am connected to the Hub and I can intercept traffic if I communicated directly to the machine with the Wireshark Windows computer. The HUB is a real HUB, not a switch. I will review your links.</p><p>To Jaap, how do I learn about setting up the SSH connectin? This is a very old version of Redhat.</p></div><div id="comment-64032-info" class="comment-info"><span class="comment-age">(19 Oct '17, 10:44)</span> dcs</div></div><span id="64040"></span><div id="comment-64040" class="comment"><div id="post-64040-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-64040-info" class="comment-info"><span class="comment-age">(19 Oct '17, 23:30)</span> Jaap ♦</div></div></div><div id="comment-tools-64030" class="comment-tools"></div><div class="clear"></div><div id="comment-64030-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="64031"></span>

<div id="answer-container-64031" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-64031-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Provided that:</p><ol><li>You have SSH access to the Redhat box</li><li>There's tcpdump installed in that box</li></ol><p>You can use the remote capture options of Wireshark, which allows you to capture traffic through an SSH tunnel.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '17, 10:33</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-64031" class="comments-container"></div><div id="comment-tools-64031" class="comment-tools"></div><div class="clear"></div><div id="comment-64031-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

