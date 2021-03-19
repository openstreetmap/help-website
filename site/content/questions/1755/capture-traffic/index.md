+++
type = "question"
title = "Capture traffic"
description = '''I have 2 PC&#x27;s set up to use Wireshark. Each PC has a different version of wireshark. I have set the ports up to be monitor ports. I have set up what vlans I want to capture. I only see broadcast traffic being captured. The interface on the switch shows unicast traffic going out the port toward the P...'''
date = "2011-01-14T14:40:00Z"
lastmod = "2011-01-15T09:06:00Z"
weight = 1755
keywords = [ "captures" ]
aliases = [ "/questions/1755" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture traffic](/questions/1755/capture-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1755-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have 2 PC's set up to use Wireshark. Each PC has a different version of wireshark. I have set the ports up to be monitor ports. I have set up what vlans I want to capture. I only see broadcast traffic being captured. The interface on the switch shows unicast traffic going out the port toward the PC running wireshark. I never get it. I have no filters of any kind capture or display filters being used. Does anyone have any thoughts on this. The switch type is Cisco Nexus 7k</p></div><div id="question-tags" class="tags-container tags">captures</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jan '11, 14:40</strong></p><img src="https://secure.gravatar.com/avatar/cff03c8ec6b43500789c5ce75e7c5690?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hotchilidog&#39;s gravatar image" /><p>hotchilidog<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hotchilidog has no accepted answers">0%</span></p></div></div><div id="comments-container-1755" class="comments-container"></div><div id="comment-tools-1755" class="comment-tools"></div><div class="clear"></div><div id="comment-1755-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1761"></span>

<div id="answer-container-1761" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1761-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is a little confusing - you have one switch, and two PCs? Our are there two switches, each with one PC connected to a monitor port? And have you created a monitor session with the VLAN as source and the monitor port as destination?</p><p>Anyway, if you're trying to capture VLANs you need to keep a few things in mind. First of all, you might need to tell the switch that you want to include the VLAN tags in the mirror session (on Cisco there should be an "encapsulation" option when setting the monitor session) - otherwise the switch will strip the tags and you might have problems to identify where the frames are coming from.</p><p>And second, and that is something tricky: the network cards in the Wireshark PCs must be capable of handling VLAN tagged frames. I had that problem with a couple of IBM Thinkpads a few years back: they did get the VLAN tagged frames but discarded it, and Wireshark never saw them. I tried all NIC parameters but I couldn't get them to forward the frames - the solution was to use an add on PCMCIA card (the good old Xircom Ethercard), and suddenly the frames where captured. Now, everytime I get a new notebook I check if it can handle VLAN tagged frames before going out to capture at customer sites :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jan '11, 09:06</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-1761" class="comments-container"><span id="1765"></span><div id="comment-1765" class="comment"><div id="post-1765-score" class="comment-score"></div><div class="comment-text"><p>The topology is 2 Cisco 7K's and 4-6500 switches. Each switch has a port Channel to each nexus 7K switch. This is why you have to have a monitor session set up on each Cisco 7K. The ports between the 2 6500 also have GLBP running for each VLAN. I can see the GLBP IP of each switch.</p><p>The purpose of this exercise is to have an audiolog record specific VOIP conversations. UDP/RTP Traffic. You mentioned a PCMCIA add on. Do you mean buy an external card that plugs into the USB port or is there an add on in the software?</p></div><div id="comment-1765-info" class="comment-info"><span class="comment-age">(16 Jan '11, 09:26)</span> hotchilidog</div></div><span id="1767"></span><div id="comment-1767" class="comment"><div id="post-1767-score" class="comment-score"></div><div class="comment-text"><p>I meant a 32bit PCMCIA hardware card that can be plugged into a notebook featuring a PCMCIA slot. Those are getting pretty rare today as most notebook manufacturers do not put them into their products anymore. If you want to see if the network card is the reason why you see no unicast traffic you should try to find PCs/notebooks with other NICs built in to check if they can capture those. In my experience Intel Pro cards should work fine. If two or three different cards still show no frames I bet the problem is not in the card but with the capture session.</p></div><div id="comment-1767-info" class="comment-info"><span class="comment-age">(16 Jan '11, 14:55)</span> Jasper ♦♦</div></div></div><div id="comment-tools-1761" class="comment-tools"></div><div class="clear"></div><div id="comment-1761-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

