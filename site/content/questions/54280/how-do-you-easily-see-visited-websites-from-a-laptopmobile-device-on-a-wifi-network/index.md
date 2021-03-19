+++
type = "question"
title = "How do you easily see visited websites from a laptop/mobile device on a wifi network?"
description = '''I&#x27;m a newbie to this stuff and I was wondering if anybody could tell me how to simply track visited websites on computers and mobile devices using Wireshark. I&#x27;ve kinda figured out how to use the HTTP filter and Destination Addresses to see websites, but I&#x27;m really just making lucky guesses on how t...'''
date = "2016-07-24T21:48:00Z"
lastmod = "2016-07-25T09:55:00Z"
weight = 54280
keywords = [ "simple", "tracking", "beginner", "websites" ]
aliases = [ "/questions/54280" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do you easily see visited websites from a laptop/mobile device on a wifi network?](/questions/54280/how-do-you-easily-see-visited-websites-from-a-laptopmobile-device-on-a-wifi-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54280-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm a newbie to this stuff and I was wondering if anybody could tell me how to simply track visited websites on computers and mobile devices using Wireshark. I've kinda figured out how to use the HTTP filter and Destination Addresses to see websites, but I'm really just making lucky guesses on how to do things. I'm on a Windows laptop using a wireless network without a password. I know that Monitor Mode may be required but I don't know how to "turn it on" Any help is greatly appreciated! Thanks!</p></div><div id="question-tags" class="tags-container tags">simple tracking beginner websites</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jul '16, 21:48</strong></p><img src="https://secure.gravatar.com/avatar/361e988e74fc1ee72c3aaa44b64ac5f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Turpz&#39;s gravatar image" /><p>Turpz<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Turpz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Jul '16, 08:27</p></div></div><div id="comments-container-54280" class="comments-container"></div><div id="comment-tools-54280" class="comment-tools"></div><div class="clear"></div><div id="comment-54280-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54306"></span>

<div id="answer-container-54306" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54306-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Unless you are really lucky about your wireless hardware and driver, monitor mode on Windows is not much useful. Now as NPcap (and NDIS 6) is here, it does work in principle, but only with some chipsets and there are some limitations. But let's assume that you are lucky and could set your WiFi adaptor to monitoring mode using the <code>wlanhelper</code> utility from the npcap suite, after installing NPcap with the wireless capturing option.</p><p>Doing so will, at first place, prevent your PC from connection through that WiFi adaptor (because monitoring mode replaces the STA mode). So unless you are even more lucky and have an additional WiFi adaptor you could use, you'll be only able to capture WLAN traffic of other devices.</p><p>The next point is how "visiting a site" works. After you write an url to your browser's address field, the browser first asks a DNS subsystem to resolve the domain name part of it. If you have visited that page shortly before, the answer is available in the cache, so no DNS request is sent over the WLAN. But let's say it is, so it is the first bit of information you are interested in.</p><p>Next, the browser sends a http GET to one of the IPs from the DNS response. However, if the web server redirects the GET to an encrypted connection (https), you will only see the initial GET. If the user himself has opted for https, you won't be able to read even the contents of even the initial GET unless you have access to key dump from the browser. It is possible to decrypt https, but you need information about the keys from the browser, which only some browsers can provide.</p><p>From the DNS queries, you can see the domain names, but not the rest of the urls (the paths to files and eventual parameters). The complete url is only available in the payload of the http GET.</p><p>Next, a single html page may refer to many other urls (pictures, advertisements), many of them placed on other servers, so for a single web page visited, you may see several DNS requests and http sessions.</p><p>On the other hand, if the user clicks between several pages hosted on the same server, there may be just a single TCP session, as the browser doesn't close it immediately after receiving the response.</p><p>P.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jul '16, 09:55</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-54306" class="comments-container"></div><div id="comment-tools-54306" class="comment-tools"></div><div class="clear"></div><div id="comment-54306-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

