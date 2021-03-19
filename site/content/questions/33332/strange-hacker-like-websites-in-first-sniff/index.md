+++
type = "question"
title = "Strange &quot;Hacker-like&quot; Websites in First Sniff?"
description = '''Running WS for the first time on my own WLAN. After enabling WinCap via Run WS As Admin, I noticed many &quot;Hacker-like&quot; websites using DNS protocol.  Sites include: anonscm.Debian.org, home.regit.org, lunuxgurus.com, think-future.De, Linuxwireless.org, aircrack-ng.org, hpl.HP.com, osxdaily.com, 802.11...'''
date = "2014-06-02T22:54:00Z"
lastmod = "2014-06-05T13:19:00Z"
weight = 33332
keywords = [ "administrator", "dns", "hackers" ]
aliases = [ "/questions/33332" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Strange "Hacker-like" Websites in First Sniff?](/questions/33332/strange-hacker-like-websites-in-first-sniff)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33332-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Running WS for the first time on my own WLAN. After enabling WinCap via Run WS As Admin, I noticed many "Hacker-like" websites using DNS protocol. Sites include: anonscm.Debian.org, home.regit.org, lunuxgurus.com, think-future.De, Linuxwireless.org, aircrack-ng.org, hpl.HP.com, osxdaily.com, 802.11ninja.net, Virtualit.cc, fuellogix.com, both micro-logics and micro-logix.com, gravatar.com, Javascriptkit.com and others. My question is: Did I expose my system when Running WS As Admin or do sites like this just "roam" the internet looking for vulnerabilities? Or has my system been compromised in the past and I'm just seeing the traffic with WS?</p><p>Thanks for your advice,</p></div><div id="question-tags" class="tags-container tags">administrator dns hackers</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jun '14, 22:54</strong></p><img src="https://secure.gravatar.com/avatar/cd154fdb4776e5478bfeee3e93b50d6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SeaDude&#39;s gravatar image" /><p>SeaDude<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SeaDude has no accepted answers">0%</span></p></div></div><div id="comments-container-33332" class="comments-container"><span id="33372"></span><div id="comment-33372" class="comment"><div id="post-33372-score" class="comment-score"></div><div class="comment-text"><p>Not all of the sites you list are "hacker-like" in the <a href="https://en.wikipedia.org/wiki/Hacker_(computer_security)">"people who break into networks" sense of "hacker"</a>, although some could be considered "hacker-like" in the <a href="https://en.wikipedia.org/wiki/Hacker_(programmer_subculture)">"programmers writing cool software" sense of "hacker"</a>:</p><ul><li>hpl.hp.com is the domain name for HP Labs, and they're not "hacker-like" in the first sense, unless, for example, <a href="http://www.hpl.hp.com/techreports/2014/HPL-2014-16.html">optimizing optical waveguides</a> involves breaking into networks. :-)</li><li>linuxwireless.org is the web site for the people working on the 802.11 stack for Linux; I suppose Linux OS developers are "hackers" in the latter sense, but not necessarily in the former sense.</li></ul></div><div id="comment-33372-info" class="comment-info"><span class="comment-age">(04 Jun '14, 02:21)</span> Guy Harris ♦♦</div></div><span id="33384"></span><div id="comment-33384" class="comment"><div id="post-33384-score" class="comment-score"></div><div class="comment-text"><p>I apologize for the characterization of the sites I found while sniffing my home network. I visited most of the sites and was impressed by what I found. I just want to know why and how these "savvy programmers'" websites are somehow involved with my WLAN.</p></div><div id="comment-33384-info" class="comment-info"><span class="comment-age">(04 Jun '14, 07:56)</span> SeaDude</div></div></div><div id="comment-tools-33332" class="comment-tools"></div><div class="clear"></div><div id="comment-33332-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="33359"></span>

<div id="answer-container-33359" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33359-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds like your wlan is open to everybody.</p><p>Some questions:</p><ul><li>is your wlan encrypted? If so, how: WEP, WPA, WPA2?</li><li>Do you have to enter a passphrase to connect to the wlan? If so: Is it a strong passphrase (i.e. test, 12345, john, dude, etc. are <strong>not</strong> strong passphrases)</li><li>Do you regularly surf to websites that have a lot of ads in them?</li></ul><p>Regards<br />
Kurt</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jun '14, 14:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Jun '14, 14:43</p></div></div><div id="comments-container-33359" class="comments-container"><span id="33362"></span><div id="comment-33362" class="comment"><div id="post-33362-score" class="comment-score"></div><div class="comment-text"><p>Kurt,</p><ul><li>Yes WLAN is encrypted with WPA2</li><li>Yes have to enter a PSK (pre-shared key) to access. The password could be a bit stronger.</li><li>I'd consider myself a pro-surfer (don't click anything; only download what i'm looking for; no porn, etc)</li></ul><p>I live in a single family residential area (no apts, condo's, etc). I can't imagine there is a large enough population to have multiple people accessing my WLAN. I will start WS and change the password on the WLAN to see if the DNS messages cease. Any further thoughts?</p></div><div id="comment-33362-info" class="comment-info"><span class="comment-age">(03 Jun '14, 15:14)</span> SeaDude</div></div><span id="33365"></span><div id="comment-33365" class="comment"><div id="post-33365-score" class="comment-score"></div><div class="comment-text"><p>Changed my WLAN PW to something ridiculously hard. Took a capture of before/during/after. Didn't see anymore "suspicious" (to the untrained eye) activity.</p><p>Any further thoughts on this? I'm a bit stunned that my network was cracked/hacked/etc.</p></div><div id="comment-33365-info" class="comment-info"><span class="comment-age">(03 Jun '14, 19:09)</span> SeaDude</div></div><span id="33368"></span><div id="comment-33368" class="comment"><div id="post-33368-score" class="comment-score"></div><div class="comment-text"><p>Did you see those requests from your own IP address or from another IP address? Can you post the capture file at Google drive, dropbox or cloudshark.org?</p></div><div id="comment-33368-info" class="comment-info"><span class="comment-age">(03 Jun '14, 22:45)</span> Kurt Knochner ♦</div></div><span id="33410"></span><div id="comment-33410" class="comment"><div id="post-33410-score" class="comment-score"></div><div class="comment-text"><p>Kurt, here (<a href="https://www.dropbox.com/s/4czrum0bj7p5cjc/FirstSniff)">https://www.dropbox.com/s/4czrum0bj7p5cjc/FirstSniff)</a> is the WLAN grab. It was my first, pardon the format. If you search the text for "DNS" and FindNext, you will see the sites I mentioned. I have the grab that I captured before/during/after router password reset. I didn't see any suspicious activity during that time.</p></div><div id="comment-33410-info" class="comment-info"><span class="comment-age">(04 Jun '14, 15:08)</span> SeaDude</div></div></div><div id="comment-tools-33359" class="comment-tools"></div><div class="clear"></div><div id="comment-33359-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="33469"></span>

<div id="answer-container-33469" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33469-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are only DNS requests for "Hacker" sites from the following IP address: 192.168.2.12</p><pre><code>  25029 1745.774340000 192.168.2.12          192.168.2.1           DNS      80     Standard query 0xd2d7  A blog.aircrack-ng.org
  25030 1745.774562000 192.168.2.12          192.168.2.1           DNS      84     Standard query 0x8bb8  A download.aircrack-ng.org
  25031 1745.774945000 192.168.2.12          192.168.2.1           DNS      80     Standard query 0x0502  AAAA blog.aircrack-ng.org
  25032 1745.774992000 192.168.2.12          192.168.2.1           DNS      81     Standard query 0xc4ea  A forum.aircrack-ng.org
  25033 1745.775039000 192.168.2.12          192.168.2.1           DNS      84     Standard query 0x6f4c  AAAA download.aircrack-ng.org
  25034 1745.775323000 192.168.2.12          192.168.2.1           DNS      81     Standard query 0x3437  AAAA forum.aircrack-ng.org
  23832 1680.741756000 192.168.2.12          192.168.2.1           DNS      74     Standard query 0xada8  A www.mocavo.com
  23833 1680.742217000 192.168.2.12          192.168.2.1           DNS      74     Standard query 0x3418  AAAA www.mocavo.com</code></pre><p>Is 192.168.2.12 the IP address of your PC? Please check the MAC address and compare it to the value in the capture output.</p><blockquote><p><strong>ipconfig /all</strong> (find 192.168.2.12) and the MAC address of that interface<br />
compare it to <strong>9c:d2:1e:61:c0:f3</strong></p></blockquote><p>If the MAC address is yours, you must have been surfing to those sites. If that IP address is not yours, you should check who else on your network could have access the internet (wife, spouse, kids, granny, pets, etc.).</p><p>BTW: There are only 3 IP addresses in the capture output</p><p>192.168.2.12: requested all those "Hacker" sites (maybe your own PC)<br />
192.168.2.11: did almost nothing. The system announced itself as Victoria-PC<br />
192.168.2.1: your Belking Router<br />
</p><p>There have been ARP requests to two other IP addresses, but they did not reply (maybe smartphones, once connected to the network).</p><blockquote><p>192.168.2.5<br />
192.168.2.8</p></blockquote><p>So, to me it looks like you were surfing to those web sites yourself, maybe without knowing it. If you go to one of those sites that are heavily loaded with ads, you would see that access pattern, because every embedded ad will trigger a DNS request and the download of some content (images, html, css, etc.).</p><p>I don't think your WLAN has been hacked. Why the whole thing stopped after you reset the wlan password, remains unclear.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jun '14, 13:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-33469" class="comments-container"><span id="33487"></span><div id="comment-33487" class="comment"><div id="post-33487-score" class="comment-score"></div><div class="comment-text"><p>Kurt,</p><p>Thanks for spending the time to look through that text file and find this information.</p><p>Yes, the MAC address and IP address are of my computer. I have never visited those sights nor was I surfing them while capturing the packets with WS. I installed WireShark, turned on CPF (in the vulnurable "Run As Administrator" style), saw these sites being accessed, and visited ask.wireshark.com to create this thread.</p><ol><li>Has my system been compromised?</li><li>How can my computer surf sites without me (ha, wow that sounds funny).</li></ol></div><div id="comment-33487-info" class="comment-info"><span class="comment-age">(05 Jun '14, 15:48)</span> SeaDude</div></div><span id="33488"></span><div id="comment-33488" class="comment"><div id="post-33488-score" class="comment-score"></div><div class="comment-text"><blockquote><p>turned on CPF</p></blockquote><p>what is CPF?</p><blockquote><p>Has my system been compromised?</p></blockquote><p>I don't know. Maybe you should run some malware scanner on that system.</p><blockquote><p>How can my computer surf sites without me (ha, wow that sounds funny).</p></blockquote><p>maybe it was bored and needed some distraction ;-))</p></div><div id="comment-33488-info" class="comment-info"><span class="comment-age">(05 Jun '14, 16:33)</span> Kurt Knochner ♦</div></div><span id="33535"></span><div id="comment-33535" class="comment"><div id="post-33535-score" class="comment-score"></div><div class="comment-text"><p>I meant NPF driver. I started it by running WS as administrator which is supposedly risky.</p><p>I'll run a malware scanner.</p><p>This machine is NOT bored! HA!</p><p>Well, this has been a very strange event indeed. To see such activity on my WLAN without an explanation is unnerving. I'd hate to go through an entire refresh of my laptop. BOo.</p></div><div id="comment-33535-info" class="comment-info"><span class="comment-age">(06 Jun '14, 20:07)</span> SeaDude</div></div></div><div id="comment-tools-33469" class="comment-tools"></div><div class="clear"></div><div id="comment-33469-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

