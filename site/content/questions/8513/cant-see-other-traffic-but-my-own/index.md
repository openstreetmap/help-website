+++
type = "question"
title = "Can&#x27;t see other traffic but my own"
description = '''As a note, I have been using Wireshark with a hub for years and it has always worked. Now I’m experiencing the weirdest issue, I can’t see other traffic that I need, such as the Print Raster data from another computer to a networked copier. I’ve spent almost two days on this, got cables and hubs eve...'''
date = "2012-01-20T10:12:00Z"
lastmod = "2012-01-22T21:06:00Z"
weight = 8513
keywords = [ "unicast", "raster", "smtp", "no" ]
aliases = [ "/questions/8513" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Can't see other traffic but my own](/questions/8513/cant-see-other-traffic-but-my-own)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8513-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>As a note, I have been using Wireshark with a hub for years and it has always worked. Now I’m experiencing the weirdest issue, I can’t see other traffic that I need, such as the Print Raster data from another computer to a networked copier. I’ve spent almost two days on this, got cables and hubs everywhere, I’ve been reading all the Help files from Wireshark online, trying everything possible. I’ve tried multiple PCs, I bought another new hub (Asante FH205P) to eliminate my existing hub (Netgear DS108) just in case it went bad. If the hubs were bad, I wouldn’t see anything most likely. I have the hub connected to our network and one cable to copier and one to my laptop. I’ve tried statically out of the network, etc… I can see all the data if it comes or goes to/from my laptop, but if I send a job from another PC, I don’t see that data, which in the past I did. If I scan to email from the copier, I used to see the requests to the email server, now I don’t see any SMTP traffic… Everyone I talke to says it should work like I have it. I’ve tried other programs such as Colasoft Capsa 7 Free and the older Etherreal. I’m out of options, this always worked in the past and it should work like I have it. Can I possibly have two bad hubs? What are the odds? I appreciate anyone's input.</p></div><div id="question-tags" class="tags-container tags">unicast raster smtp no</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jan '12, 10:12</strong></p><img src="https://secure.gravatar.com/avatar/0c63f56df7e2f2afe46e7fcd7df20cc7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SharpSBSMan&#39;s gravatar image" /><p>SharpSBSMan<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SharpSBSMan has no accepted answers">0%</span></p></div></div><div id="comments-container-8513" class="comments-container"></div><div id="comment-tools-8513" class="comment-tools"></div><div class="clear"></div><div id="comment-8513-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="8514"></span>

<div id="answer-container-8514" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8514-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Most common reasons to not see traffic on a wired network card when you are (pretty) sure that there is traffic coming in:</p><ol><li>Promiscuous mode is not enabled for the capture card. There is a setting in the Wireshark capture options that should always have a check mark.</li><li>VLAN tagged frames - a lot of NICs do not accept them by default. Some can be configured to pass them on, but some will never pass them on to Wireshark. By the way, Realtek cards seem to take no prisoners and always capture any frame you throw at them, including VLAN tags ;-)</li><li>Spanning Tree (yes, surprise!) - if your network is running spanning tree, you might have your capture point at a place where the tree does not forward any traffic (except BPDUs etc.), because it is using an alternate path with better costs.</li></ol><p>If I were you I'd try to remember what changed in the network setup since the last time it worked; very often coworkers do something that they didn't tell you about, and suddenly stuff that worked before doesn't.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '12, 12:31</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-8514" class="comments-container"><span id="8530"></span><div id="comment-8530" class="comment"><div id="post-8530-score" class="comment-score"></div><div class="comment-text"><p>Thanks guys. So after trying two laptops, I tried a third one, I asked someone to use theirs. And they can see everything through either hub. We have Dell D630s. So I swapped my HDD and put it in his and vice versa. Now none of the laptops would see all traffic. So I'm realizing that my NIC might have an issue even though it works fine for everyday usage. Also, we both have Office Scanner from Trend running, but my laptop had some filter that I couldnt disable. It was a list of like 20 protocols that were allowed. So I may have a software/hardware issue. I will get me another laptop from IT Dept and I should be fine. What are the odds that a couple laptops had the same symptoms... I have to comfirm the Office Scanner issue, but I'm guessing it has something to do with it. I tried to disable all the Scanner services and rebooted, but it turned itself on again, I'm sure it's forced as a domain service. Thanks again for all your tips, I do appreciate it. I'll get this thing yet!!! Note: I did have promiscuous mode on all the time. Also, i did get an Ethereal download but didn't work, but I submitted this post before i tried it by mistake, the download was corrupt so it didn't even install. And I do remember Ethereal changing to Wireshark. Thanks everyone!!!! Florin</p></div><div id="comment-8530-info" class="comment-info"><span class="comment-age">(20 Jan '12, 20:48)</span> SharpSBSMan</div></div></div><div id="comment-tools-8514" class="comment-tools"></div><div class="clear"></div><div id="comment-8514-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8524"></span>

<div id="answer-container-8524" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8524-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>(Note, BTW, that "the older Ethereal" isn't "[an]other program"; it's the same program as Wireshark - only the name changed, somewhere around the time of the 0.99.2 release of the program.)</p><p>I'm assuming you have a possibly-switched network, and have a cable going from one port on that network into the hub, another cable going from the hub to the printer, and a third cable going from the hub to the machine running the sniffer program.</p><p>If neither Ethereal/Wireshark nor Colasoft Capsa can see the traffic, it's almost certainly not a problem with the program. The DS108 is listed on <a href="http://wiki.wireshark.org/HubReference">the HubReference page of the Wireshark Wiki</a> as a true, but dual-speed, hub, so it should work <em>as long as all hosts plugged into the hub, including the host running the sniffer program, are running at the same network speed</em> (i.e, the host on the network talking to the printer, the printer, <em>and</em> the host running the sniffer either all need to be running at 10Mb/s or 100Mb/s). The HubReference page doesn't say anything about the FH205p, but I'm guessing it's a true dual-speed hub (so the same issues would apply to it).</p><p>I assume you probably were using promiscuous mode in the past when you <em>could</em> see traffic, so you know that you have to check it or leave it checked, so the first of Jasper's reasons <em>probably</em> isn't the problem. If this isn't a dual-speed problem, the two other issues Jasper mentioned are two things to check.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '12, 16:48</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-8524" class="comments-container"></div><div id="comment-tools-8524" class="comment-tools"></div><div class="clear"></div><div id="comment-8524-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8553"></span>

<div id="answer-container-8553" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8553-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I figured it out, it was the Trend Office Scan Firewall. Had to disable it, restarted and I can see everything again. thanks for all your help. Florin</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '12, 21:06</strong></p><img src="https://secure.gravatar.com/avatar/0c63f56df7e2f2afe46e7fcd7df20cc7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SharpSBSMan&#39;s gravatar image" /><p>SharpSBSMan<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SharpSBSMan has no accepted answers">0%</span></p></div></div><div id="comments-container-8553" class="comments-container"></div><div id="comment-tools-8553" class="comment-tools"></div><div class="clear"></div><div id="comment-8553-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

