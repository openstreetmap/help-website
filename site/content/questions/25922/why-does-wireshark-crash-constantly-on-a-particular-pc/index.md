+++
type = "question"
title = "why does wireshark crash constantly on a particular PC?"
description = '''Hello, I use wireshark on several computers, and for some reason I can&#x27;t get it to work for more than a few minutes on a particular PC running XP, service pack 3. I tried 1.66 and today I installed 1.10.2, with the same results. Thanks, Victor'''
date = "2013-10-11T14:49:00Z"
lastmod = "2013-10-14T08:13:00Z"
weight = 25922
keywords = [ "wireshark_crashed" ]
aliases = [ "/questions/25922" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [why does wireshark crash constantly on a particular PC?](/questions/25922/why-does-wireshark-crash-constantly-on-a-particular-pc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25922-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I use wireshark on several computers, and for some reason I can't get it to work for more than a few minutes on a particular PC running XP, service pack 3. I tried 1.66 and today I installed 1.10.2, with the same results.</p><p>Thanks, Victor</p></div><div id="question-tags" class="tags-container tags">wireshark_crashed</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '13, 14:49</strong></p><img src="https://secure.gravatar.com/avatar/f33e881bbed7595a48ffe2c9226ca461?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vsabino&#39;s gravatar image" /><p>vsabino<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vsabino has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 11 Oct '13, 14:50</p></div></div><div id="comments-container-25922" class="comments-container"><span id="25926"></span><div id="comment-25926" class="comment"><div id="post-25926-score" class="comment-score"></div><div class="comment-text"><p>Crashes when you capture? Crashes when you open trace files? Crash if you just <em>open</em> wireshark? I guess I would start by removing all vestiges of Wireshark (registry, profiles etc). Or create a new user and see if that helps. rule out the easier ones first before tackling NIC drivers etc.</p></div><div id="comment-25926-info" class="comment-info"><span class="comment-age">(11 Oct '13, 17:54)</span> hansangb</div></div><span id="25939"></span><div id="comment-25939" class="comment"><div id="post-25939-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I use wireshark on several computers, and for some reason I can't get it to work for more than a few minutes on a particular PC</p></blockquote><p>O.K. so, what is different with that PC? Different software on it (Firewall, Endpoint Security, AV, etc.), different set of malware infections, different set of drivers, etc. What can you rule out and what remains then?</p></div><div id="comment-25939-info" class="comment-info"><span class="comment-age">(12 Oct '13, 10:34)</span> Kurt Knochner ♦</div></div><span id="25951"></span><div id="comment-25951" class="comment"><div id="post-25951-score" class="comment-score"></div><div class="comment-text"><p>Looks like another "it keeps crashing on capture" question to me.</p></div><div id="comment-25951-info" class="comment-info"><span class="comment-age">(13 Oct '13, 22:28)</span> Jasper ♦♦</div></div><span id="25966"></span><div id="comment-25966" class="comment"><div id="post-25966-score" class="comment-score"></div><div class="comment-text"><p>Hi all,</p><p>some info on the PC (all the PCs I ran it on are configured the same way):</p><p>windows XP prof 2002 service pack 3</p><p>Microsoft security essentials: Antimalware Client Version: 4.1.522.0 Engine Version: 1.1.9901.0 Antivirus definition: 1.159.2116.0 Antispyware definition: 1.159.2116.0</p><p>Intel Xeon, 2.33 GHz, 2GB RAM</p><p>it is at a remote location, I VPN into it. generally wireshark runs for about 15 - 45 minutes before crashing.</p><p>I'm not logging tremendous amount of traffic. There are a few packets per second, and bursts of maybe 20 packets per second when we collect data every 5 - 10 minutes.</p></div><div id="comment-25966-info" class="comment-info"><span class="comment-age">(14 Oct '13, 07:41)</span> vsabino</div></div></div><div id="comment-tools-25922" class="comment-tools"></div><div class="clear"></div><div id="comment-25922-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25969"></span>

<div id="answer-container-25969" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25969-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Intel Xeon, 2.33 GHz, <strong>2GB RAM</strong><br />
it is at a remote location, I VPN into it. generally <strong>wireshark runs</strong> for <strong>about 15 - 45 minutes</strong> before crashing.</p></blockquote><p>O.K. 2 GByte is not much, especially if you connect via RDP (through the VPN tunnel) and don't add a capture filter to ignore the RDP traffic (Capture filter: not port 3389).<br />
</p><p>The RDP screen updates will create a feed-back loop like this: Wireshark screen gets updated due to new packets, this creates RDP traffic (screen update), which creates new packets, which creates Wireshark screen updates, and so on.</p><p>Same, if you use any other remote Desktop solution.</p><p>See the many other questions about RAM problems and the solutions.</p><blockquote><p><a href="http://ask.wireshark.org/questions/25343/wireshark-takes-all-ram">http://ask.wireshark.org/questions/25343/wireshark-takes-all-ram</a><br />
<a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">http://wiki.wireshark.org/KnownBugs/OutOfMemory</a><br />
<a href="http://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/">http://blog.packet-foo.com/2013/05/the-notorious-wireshark-out-of-memory-problem/</a></p></blockquote><p>General soultion: Use dumpcap instead of Wireshark to capture traffic (see the links above).</p><p><strong>++ UPDATE ++</strong></p><blockquote><p>I'm <strong>not logging tremendous amount of traffic</strong>. There are a few packets per second, and bursts of maybe 20 packets per second when we collect data every 5 - 10 minutes.</p></blockquote><p>Did you check the RDP feedback problem I mentioned above. Maybe that's much more traffic than you expect.</p><blockquote><p>it is at a <strong>remote location, I VPN into it</strong>.</p></blockquote><p>But maybe you get hit by a GTK problem (possibly in conjunction with RDP)</p><blockquote><p><a href="http://ask.wireshark.org/questions/19852/wireshark-eats-up-memory-at-an-alarming-rate-for-version-after-165">http://ask.wireshark.org/questions/19852/wireshark-eats-up-memory-at-an-alarming-rate-for-version-after-165</a><br />
<a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8281">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8281</a></p></blockquote><p>Can you please try the latest development build and report back the results?</p><blockquote><p><a href="http://www.wireshark.org/download/automated/win32/Wireshark-win32-1.11.0-SVN-52597.exe">http://www.wireshark.org/download/automated/win32/Wireshark-win32-1.11.0-SVN-52597.exe</a></p></blockquote><p>Or if that does not help, you could try to run <strong>Wireshark 1.6.5</strong> (not 1.6.6) as there is a comment in bug 8281:</p><p>Cite:</p><pre><code>Additional evidence that this is a GTK bug: I tried back releases of Wireshark.  The problem appears to have started with Wireshark release 1.6.6.  Release 1.6.6 was the first to use GTK 2.24.10.  Wireshark release 1.6.5 does not have this problem.  It uses GTK 2.22.1.</code></pre><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Oct '13, 08:13</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Oct '13, 08:52</p></div></div><div id="comments-container-25969" class="comments-container"><span id="26008"></span><div id="comment-26008" class="comment"><div id="post-26008-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt,</p><p>I tried dumpcap, and so far it works!! For some reason on this particular PC the regular wireshark does not work, but dumpcap did the job! I left the regular wireshark running overnight on one PC and the dumpcap on another, checked this morning and both were still running.</p><p>To respond to your comments on the RDP feed-back loop, i don't have the VPN and RDP sessions continously. I only VPN and then RDP once in a while when I want to check things. I always found that wireshark had crashed before I logged in.</p><p>Anyway, thanks for your suggestion on dumpcap!!</p><p>Victor</p></div><div id="comment-26008-info" class="comment-info"><span class="comment-age">(15 Oct '13, 08:04)</span> vsabino</div></div></div><div id="comment-tools-25969" class="comment-tools"></div><div class="clear"></div><div id="comment-25969-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

