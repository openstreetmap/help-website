+++
type = "question"
title = "RpCap 4.1.1 vs RpCap 4.1.2"
description = '''We utilize RpCapd –n on a regular basis in our Hospital Enterprise network of 5000 desktops, 68 wiring closets and over 250 switches and routers. We have been installing WinPcap 4.1.1 due to its ability to be ‘silently’ installed, versus 4.1.2 which as we understand can NOT be silently installed.  W...'''
date = "2010-11-09T08:00:00Z"
lastmod = "2010-11-11T06:24:00Z"
weight = 877
keywords = [ "rpcapd", "capture", "remote" ]
aliases = [ "/questions/877" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [RpCap 4.1.1 vs RpCap 4.1.2](/questions/877/rpcap-411-vs-rpcap-412)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-877-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We utilize RpCapd –n on a regular basis in our Hospital Enterprise network of 5000 desktops, 68 wiring closets and over 250 switches and routers. We have been installing WinPcap 4.1.1 due to its ability to be ‘silently’ installed, versus 4.1.2 which as we understand can NOT be silently installed.</p><p>We have not been able to remotely capture with Wireshark 1.4 on these remote devices after running a local batch file with PSExec to start RpCap –n on the remote device. We get an error that Wireshark cannot see any interfaces etc etc. When we install WinPcap 4.1.2 intrusively, RpCap and wireshark remote capture run perfectly.</p><p>We are curious to see if this is a known issue or are we doing something wrong. We have created an image with Wireshark 1.4 and WinPcap 4.1.2 on PCs dual attached to switches in our 68 disparate closets which allows us to remotely capture traffic through each of our closets and narrows time for locating areas of packet loss etc. We would really like to find a resolve for the remote silent install at the workstation level to further facilitate our investigations of application specific misbehaviors.</p></div><div id="question-tags" class="tags-container tags">rpcapd capture remote</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Nov '10, 08:00</strong></p><img src="https://secure.gravatar.com/avatar/8dcd2da497394e285a5e995a8e3ab1e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swglover&#39;s gravatar image" /><p>swglover<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swglover has no accepted answers">0%</span></p></div></div><div id="comments-container-877" class="comments-container"><span id="894"></span><div id="comment-894" class="comment"><div id="post-894-score" class="comment-score"></div><div class="comment-text"><p>This may be better posted in the WinPcap mailing list: http://www.winpcap.org/contact.htm</p></div><div id="comment-894-info" class="comment-info"><span class="comment-age">(10 Nov '10, 07:17)</span> Jaap ♦</div></div><span id="900"></span><div id="comment-900" class="comment"><div id="post-900-score" class="comment-score"></div><div class="comment-text"><p>Not really an answer from me, but I am interested in how you install rcapd silently. For a long time the only way I could figure out to make remote captures was by logging in with mstsc and install the complete wireshark suite. This meant the user had to log out, be warned he could log in again etc. Not very silent.</p><p>For more than a year now I am using the command line microsoft tool netcap. With psexec it is copied to the host and from there I run it. The capture files can be copied back to my own place and analysed with wireshark. Disadvantages are limited filter capacbilities and timestamps on packets are not great.</p><p>However, when needed I can make a snapshot trace on a remote host in about 5 minutes to see what is wrong and even remove all capture software. That is a great thing</p></div><div id="comment-900-info" class="comment-info"><span class="comment-age">(10 Nov '10, 11:27)</span> easterman</div></div></div><div id="comment-tools-877" class="comment-tools"></div><div class="clear"></div><div id="comment-877-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="908"></span>

<div id="answer-container-908" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-908-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>We have been doing the silent install of WinPcap (the version downloaded directly from WinPcap website) remotely for some time. it installs in the "C:Program Files WinPcap" directory. then from my machine I run the following *.bat file:</p><p>psexec \%1 "%Programfiles% Winpcap rpcapd.exe" -n pause</p><p>The %1 pauses the batch file and allows me to enter the devices ip address.</p><p>The latest version of WinPcap for some reason no longer allows silent install, so we have to actually remote to the suspect machine to install it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '10, 06:24</strong></p><img src="https://secure.gravatar.com/avatar/8dcd2da497394e285a5e995a8e3ab1e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="swglover&#39;s gravatar image" /><p>swglover<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="swglover has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Nov '10, 06:28</p></div></div><div id="comments-container-908" class="comments-container"></div><div id="comment-tools-908" class="comment-tools"></div><div class="clear"></div><div id="comment-908-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

