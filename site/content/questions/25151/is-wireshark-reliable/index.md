+++
type = "question"
title = "is wireshark reliable"
description = '''I have written a code in a device that sends ARP request to get the MAC address of PC and then communicates with it through UDP.  I have an application that makes this happen in a loop.(open the port; ARP request + UDP data packets(few packets); then close the port). the loop is mainly to know the r...'''
date = "2013-09-24T02:24:00Z"
lastmod = "2013-09-24T06:51:00Z"
weight = 25151
keywords = [ "arp", "udp", "wireshark" ]
aliases = [ "/questions/25151" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [is wireshark reliable](/questions/25151/is-wireshark-reliable)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25151-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have written a code in a device that sends ARP request to get the MAC address of PC and then communicates with it through UDP.</p><p>I have an application that makes this happen in a loop.(open the port; ARP request + UDP data packets(few packets); then close the port). the loop is mainly to know the reliability of the device to communicate.</p><p>My problem is, I am supposed to get an ARP request continuously. but it is not happening all times..</p><p>I want to know is it possible that Wireshark could have missed to show us these packets, even if the device has sent.. because I am pretty sure that the device goes to the state where it sends ARP request.</p><p>thanks in advance</p></div><div id="question-tags" class="tags-container tags">arp udp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Sep '13, 02:24</strong></p><img src="https://secure.gravatar.com/avatar/14ae6741f009eb9551c897744110e25f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Raja%20Balaji&#39;s gravatar image" /><p>Raja Balaji<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Raja Balaji has no accepted answers">0%</span></p></div></div><div id="comments-container-25151" class="comments-container"></div><div id="comment-tools-25151" class="comment-tools"></div><div class="clear"></div><div id="comment-25151-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25153"></span>

<div id="answer-container-25153" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25153-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If the packets were captured Wireshark will show them, unless you have a filter applied that hides them. If you are missing a couple of packets then maybe they just weren't recorded in the first place. If you're capturing on a SPAN port for example it is possible that the monitor port is oversubscribed and drops a couple of frames every once in a while. If you need to be absolutely sure that the packet was there you'll need to capture using a full duplex tap - which is a more complex setup.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Sep '13, 03:05</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-25153" class="comments-container"></div><div id="comment-tools-25153" class="comment-tools"></div><div class="clear"></div><div id="comment-25153-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="25158"></span>

<div id="answer-container-25158" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25158-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>My problem is, I am supposed to get an ARP request continuously. but it is not happening all times..</p><p>I want to know <strong>is it possible that Wireshark could have missed to show us these packets</strong>, even if the device has sent.. because I am pretty sure that the device goes to the state where it sends ARP request.</p></blockquote><p>it may be possible that there is a bug in Wireshark or any other problem that prevents it to see the packets (i.e. wrong checksum --&gt; system driver drops the packet).</p><p><strong>However</strong>, and please don't get me wrong (really no offense!!): If I look at the history of your questions and network problems, I don't think the problem is with Wireshark, but rather with your LabView application or the code on the arduino controller (see your other questions).</p><blockquote><p>My problem is, I am supposed to get an ARP request continuously. but it is not happening all times..</p></blockquote><p>Maybe the LabView code interacts with the OS IP stack in a way you don't know and that prevents the ARP request from being sent (at least sometimes). Same, if you send the ARP request from the arduino controller.</p><p>So, do you see the OS interface counters go up if you send the ARP requests? That would be a first hint if the ARP packet was dropped by the OS.</p><p><strong>++UPDATE++</strong><br />
To answer your question:</p><blockquote><p>is wireshark reliable</p></blockquote><p>In general yes. In your special case, I'm pretty sure it's not a problem with Wireshark, as it show most of the ARP requests. Only a few are missing. The chances that this is a bug in Wireshark are pretty low, so I tend to say, it must be related with your software (most likely), the OS or the network itself.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Sep '13, 06:51</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Sep '13, 02:28</p></div></div><div id="comments-container-25158" class="comments-container"></div><div id="comment-tools-25158" class="comment-tools"></div><div class="clear"></div><div id="comment-25158-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

