+++
type = "question"
title = "AIRPCAP and URL Viewing"
description = '''Hi, I am pretty new to all of this, so not sure if what I am trying to do is possible. My end goal is to see the URLs visited from each computer/phone that hits my WiFi at home. I have used OpenDNS which is fine for the domain name, but I want more detail. I downloaded wireshark and tested it out. I...'''
date = "2015-10-12T03:44:00Z"
lastmod = "2015-10-12T10:51:00Z"
weight = 46465
keywords = [ "airpcap", "wireshark" ]
aliases = [ "/questions/46465" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [AIRPCAP and URL Viewing](/questions/46465/airpcap-and-url-viewing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46465-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am pretty new to all of this, so not sure if what I am trying to do is possible. My end goal is to see the URLs visited from each computer/phone that hits my WiFi at home. I have used OpenDNS which is fine for the domain name, but I want more detail.</p><p>I downloaded wireshark and tested it out. I was able to successfully see every URL the computer hit over the capture period. Now I want to see that same info on other devices. I am running Windows. From reading here, it looks like I need to buy AIRPCAP in order to do this. However, I haven't been able to find a straight answer on whether it will get the URLs.</p><p>Can someone please provide a straight answer to the following?</p><p>If I purchase AIRPCAP and run it with wireshark, will I be able to see every URL that other devices on my WiFi hit? In particular, there is only 1 device I am most concerned with, so I can filter the capture to only hit that one device. I just really want to know whether I will be able to see the full URL.</p><p>When I was capturing on my computer, I was able to see the full link, and could click on it to go to the exact page that the computer was on. That is what I want to be able to do for other devices (really just 1 in particular.)</p></div><div id="question-tags" class="tags-container tags">airpcap wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Oct '15, 03:44</strong></p><img src="https://secure.gravatar.com/avatar/51e5a23097a0b3079b90d07fcd4adc1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="questions123&#39;s gravatar image" /><p>questions123<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="questions123 has no accepted answers">0%</span></p></div></div><div id="comments-container-46465" class="comments-container"><span id="46467"></span><div id="comment-46467" class="comment"><div id="post-46467-score" class="comment-score"></div><div class="comment-text"><p>What's the status on WiFi encryption?</p><p>What's happening when HTTPS access is used?</p></div><div id="comment-46467-info" class="comment-info"><span class="comment-age">(12 Oct '15, 04:02)</span> Jaap ♦</div></div></div><div id="comment-tools-46465" class="comment-tools"></div><div class="clear"></div><div id="comment-46465-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46469"></span>

<div id="answer-container-46469" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46469-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The answer to your question is YES - if you capture the WiFi frames, you will be able to view the URL.</p><p>Now, as @Jaap has eluded to, there are many assumptions that are made here:</p><ol><li>Can the AIRPCAP device properly capture the WiFi frames on your network? For example, AIRPCAP only supports 11n and if your network supports 11ac, then you might not be able to capture the data frames - which contains the information you are looking for.</li><li>Have you properly captured the EAP exchange between device and the AP? If not, you will not be able to decrypt the data and see the URL.</li></ol><p>So yes, AIRPCAP can work. But it is an expensive solution ($700 for a WiFi adapter!!!). There are other cheaper and IMHO better ways than using AIRPCAP to capture WiFi frames.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Oct '15, 10:51</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-46469" class="comments-container"></div><div id="comment-tools-46469" class="comment-tools"></div><div class="clear"></div><div id="comment-46469-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

