+++
type = "question"
title = "Firewall blocking packets"
description = '''Respected sir/ma&#x27;am We are developing our major project in our college on &quot;Designing detection and defense mechanism against DDos attacks&quot;. We have come up with the following problem : Our software is not detecting(sniffing) the ethernet packets when Windows Firewall is activated whereas Wireshark d...'''
date = "2016-01-24T00:53:00Z"
lastmod = "2016-01-24T03:13:00Z"
weight = 49488
keywords = [ "windows", "firewall" ]
aliases = [ "/questions/49488" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Firewall blocking packets](/questions/49488/firewall-blocking-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49488-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Respected sir/ma'am</p><p>We are developing our major project in our college on "Designing detection and defense mechanism against DDos attacks". We have come up with the following problem : Our software is not detecting(sniffing) the ethernet packets when Windows Firewall is activated whereas Wireshark detects. Can you help us with the problem?</p><p>Expecting your reply as soon as possible.</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">windows firewall</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jan '16, 00:53</strong></p><img src="https://secure.gravatar.com/avatar/5d2779cb5fb49714a66dd95965583381?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Shubham%20Agarwal&#39;s gravatar image" /><p>Shubham Agarwal<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Shubham Agarwal has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Jan '16, 06:45</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-49488" class="comments-container"></div><div id="comment-tools-49488" class="comment-tools"></div><div class="clear"></div><div id="comment-49488-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49489"></span>

<div id="answer-container-49489" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49489-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>To answer your basic question:</p><p>Wireshark's capturing engine, the WinPcap in case of Windows, gets access to incoming packets before the Windows firewall, which itself gets access to them before any application software.</p><p>While WinPcap does not affect the packets, just saves a copy of them, the Windows firewall is able to block them before they could reach the application software.</p><p>So to make your software see all incoming packets:</p><ul><li><p>the most straightforward way is to disable the Windows firewall completely so that you could concentrate on the development of the software's core functionality, and use some external firewall if you need to expose the development machine to the internet at some stage of project development,</p></li><li><p>the more complex way is to learn how to hook your software into the network stack at some point "closer to the wire" than the Windows firewall is hooked, or to use WinPcap as the network-facing part of your application, as you say that you only need to sniff the packets (i.e. you don't need to manipulate them).</p></li></ul><p>I would like to hear more about the "defense mechanism" part, though.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jan '16, 03:13</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Jan '16, 03:28</p></div></div><div id="comments-container-49489" class="comments-container"><span id="49490"></span><div id="comment-49490" class="comment"><div id="post-49490-score" class="comment-score">1</div><div class="comment-text"><p>A little side-note: sometimes, even WinPCAP can't capture everything. There are numerous questions on this Q&amp;A site where it turned out that personal firewalls, anti-virus or other security software prevented capturing at least some incoming packets</p></div><div id="comment-49490-info" class="comment-info"><span class="comment-age">(24 Jan '16, 03:48)</span> Jasper ♦♦</div></div><span id="49610"></span><div id="comment-49610" class="comment"><div id="post-49610-score" class="comment-score"></div><div class="comment-text"><p>Respected Sir/Mam, Thank You for your valuable reply.</p><p>Regarding our defense module we need to just drop the packets that we detect as malicious. Now the problem in this part is how can we actually drop or dump a packet once it is received or how can we actually hook our application before firewall so that we can then use the windows firewall as a filter.</p><p>Thank You.</p></div><div id="comment-49610-info" class="comment-info"><span class="comment-age">(28 Jan '16, 11:04)</span> Shubham Agarwal</div></div><span id="49611"></span><div id="comment-49611" class="comment"><div id="post-49611-score" class="comment-score"></div><div class="comment-text"><p>That is another topic which has nothing to do with Wireshark. You need to familiarize with the Windows network APIs I guess.</p></div><div id="comment-49611-info" class="comment-info"><span class="comment-age">(28 Jan '16, 11:13)</span> Jasper ♦♦</div></div><span id="49616"></span><div id="comment-49616" class="comment"><div id="post-49616-score" class="comment-score">1</div><div class="comment-text"><p>That is what I was afraid of:</p><blockquote><p>drop the packets that we detect as malicious</p><p>we can then use the windows firewall as a filter</p></blockquote><p>Leaving aside what kind of hooking to the kernel you'd have to use, which is definitely out of scope of this site as @Jasper has pointed out, have you ever thought through what a <strong>D</strong>DoS attack actually means?</p><p>As you've mentioned a Windows machine I assume your Ethernet card's maximum bitrate is 1 Gbit/s. As an attacker, I can easily take a battle unit of 2000 zombies (someone else's computers which I or someone else have previously infected with malware and thus made it possible for me to execute tasks on them remotely, without the owner noticing at least for some time) and make each of them send a packet flow of 500 kbit/s to your server.</p><p>This way, I will clog the full bandwidth of your server's Ethernet card, so the requests from real clients of your server application will hardly squeeze between the tons of the malicious ones. Therefore, your solution running at the target server may be dropping the packets from source IPs it has identified as malicious ones, but most of your clients will not be served anyway as most of their requests will not ever reach your server.</p></div><div id="comment-49616-info" class="comment-info"><span class="comment-age">(28 Jan '16, 19:32)</span> sindy</div></div></div><div id="comment-tools-49489" class="comment-tools"></div><div class="clear"></div><div id="comment-49489-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

