+++
type = "question"
title = "Explantion of wireshark trace"
description = '''Hello, I &#x27;ve been trying to get trace in a network where we exchange SNMP messages between a server and a PC! In some SNMP messages that are sent by the Server and never reach the PC - while other do -, I am seeing a bad checksum message on the wireshark analysis! I also have a print screen of this ...'''
date = "2011-01-14T03:01:00Z"
lastmod = "2011-01-18T10:01:00Z"
weight = 1747
keywords = [ "checksum", "bad", "snmp" ]
aliases = [ "/questions/1747" ]
osqa_answers = 6
osqa_accepted = false
+++

<div class="headNormal">

# [Explantion of wireshark trace](/questions/1747/explantion-of-wireshark-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1747-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I 've been trying to get trace in a network where we exchange SNMP messages between a server and a PC! In some SNMP messages that are sent by the Server and never reach the PC - while other do -, I am seeing a bad checksum message on the wireshark analysis! I also have a print screen of this capture! Can anybody advise on this!</p><p>Regards</p></div><div id="question-tags" class="tags-container tags">checksum bad snmp</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jan '11, 03:01</strong></p><img src="https://secure.gravatar.com/avatar/213f6d179e8b8d5f0bee6a66ae6815b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mariolis&#39;s gravatar image" /><p>Mariolis<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mariolis has no accepted answers">0%</span></p></div></div><div id="comments-container-1747" class="comments-container"></div><div id="comment-tools-1747" class="comment-tools"></div><div class="clear"></div><div id="comment-1747-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

6 Answers:

</div>

</div>

<span id="1748"></span>

<div id="answer-container-1748" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1748-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Okay, first of it is important to know where you are capturing the data. If you're capturing either on the server or the PC your checksum errors are most likely caused by the checksum offloading mechanism of your network card, and not a real error. There are tons of questions in this board where you can look that one up in greater detail.</p><p>If, on the other hand, the frames with checksum errors are exactly those SNMP messages that do not reach the PC you have a problem where some device damages frames somewhere in your network. That could be caused by a faulty network interface, a bad cable, strong interference and (sadly enough, I have to say, but very rare) by a network aggregation tap. So if I were you I'd determine if the checksum errors correlate to the missing SNMP messages, and if so, find the source of the damaged transmission (check CRC error counters on your switches/routers).</p><p>If you have checksum errors on packets that DO get received you can probably rule checksum errors out as a cause. In that case you'll have to move your Wireshark box(es) along the communication path and track down the location where the frames go in but not out on the other side. Best way to do this is doing a simultaneous capture on both sides to have something to compare. It can be a very tedious process, but usually there's no way around it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '11, 04:07</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-1748" class="comments-container"></div><div id="comment-tools-1748" class="comment-tools"></div><div class="clear"></div><div id="comment-1748-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1769"></span>

<div id="answer-container-1769" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1769-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I can verify that it does not seem like just a problem of false alarms. I have checked both Server and Client PC and in all the cases which I have checked when the checksum error occured then there was no message reaching the client PC. If it was the first case where the checksum is caused by the offloading mechanisms, wouldn't I get the message on the other side? Also I need to add that this Server transmits in several Client PCs and not all of the experience this malfunction and even among the ones that do not correctly get their messages not all of them have this behavior all the time! Any ideas?</p><p>Regards</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jan '11, 03:08</strong></p><img src="https://secure.gravatar.com/avatar/213f6d179e8b8d5f0bee6a66ae6815b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mariolis&#39;s gravatar image" /><p>Mariolis<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mariolis has no accepted answers">0%</span></p></div></div><div id="comments-container-1769" class="comments-container"></div><div id="comment-tools-1769" class="comment-tools"></div><div class="clear"></div><div id="comment-1769-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1770"></span>

<div id="answer-container-1770" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1770-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, you are correct, if offloading would cause the CRC errors you'd still see the same packets but with valid CRCs on the recipient side. So I guess we can rule that out.</p><p>Okay, before we go into the quite annoying option to track down a packet "destroyer" on the network - have you checked if the clients that do not receive the packets have no local firewall software running that blocks them? I would probably verify that the frame never gets to the client at all by tapping into it's cable directly and capture with a passive Wireshark PC just to make sure, but first I'd try to turn of any personal firewall on the client and see if the packets get through.</p><p>The other possibility is a device on the path from server to client is sometimes damaging packets. If you say it doesn't happen to all clients you can try to identify what the affected clients have in common (same physical path?). Check all switches and routers for their error counters over a period of time and investigate if they go up, and maybe that even corresponds to the lost messages. If you can't do that it gets tricky, because then you have to track down the location where the packets get corrupted yourself. I usually do that by capturing on both sides of <strong>each</strong> device in the path from sender to receiver until I find the device where the packet goes in okay and comes out damaged (or even lost, so no coming out at all). This is usually very time consuming work and no fun at all.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jan '11, 05:24</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-1770" class="comments-container"></div><div id="comment-tools-1770" class="comment-tools"></div><div class="clear"></div><div id="comment-1770-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1781"></span>

<div id="answer-container-1781" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1781-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Jasper thank you very much for your answer!</p><p>I can verify that all the recipients "wear" the same software! And we are not talking about 1-2 PCs but more like 200! On which I can experience this faulty behavior on 20 of them overall! And there is no firewall set on those machines! So it seems like a network issue rather than anything else from what we've been talking about!</p><p>Regards</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jan '11, 00:05</strong></p><img src="https://secure.gravatar.com/avatar/213f6d179e8b8d5f0bee6a66ae6815b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mariolis&#39;s gravatar image" /><p>Mariolis<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mariolis has no accepted answers">0%</span></p></div></div><div id="comments-container-1781" class="comments-container"></div><div id="comment-tools-1781" class="comment-tools"></div><div class="clear"></div><div id="comment-1781-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1786"></span>

<div id="answer-container-1786" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1786-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Agreed, this looks like a network issue. I think either some device is damaging packets or you might have a congested link somewhere that results in your SNMP packets being dropped due to performance reasons. They are usually the first to get axed because they're UDP and low priority anyway. Maybe you even have strict QoS settings that are a reason for it. Good luck tracking it down, and let me/us know if you have further questions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jan '11, 02:50</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-1786" class="comments-container"></div><div id="comment-tools-1786" class="comment-tools"></div><div class="clear"></div><div id="comment-1786-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1791"></span>

<div id="answer-container-1791" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1791-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>SNMP is UDP so the delivery is best effort.</p><p>Try a continuous PING from client to server and see if any ICMP packets are dropped.</p><p>Is this a Network Monitor of some type, PRTG, MRTG Orion etc?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jan '11, 10:01</strong></p><img src="https://secure.gravatar.com/avatar/d5aa09edfeeb0600f74a72e63806f227?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="erics&#39;s gravatar image" /><p>erics<br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="erics has no accepted answers">0%</span></p></div></div><div id="comments-container-1791" class="comments-container"></div><div id="comment-tools-1791" class="comment-tools"></div><div class="clear"></div><div id="comment-1791-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

