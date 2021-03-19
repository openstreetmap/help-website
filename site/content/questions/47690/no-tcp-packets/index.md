+++
type = "question"
title = "NO TCP PACKETS"
description = '''I am running wireshark on a kali linux computer. I have an alfa usb wireless device. When I set my computer to run in monitor mode, wireshark does not see any tcp packets. I have been struggling with this for a few months now. When I first switched from a windows machine, I was seeing lots of tcp pa...'''
date = "2015-11-17T13:41:00Z"
lastmod = "2015-11-17T13:41:00Z"
weight = 47690
keywords = [ "packets", "tcp", "no" ]
aliases = [ "/questions/47690" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [NO TCP PACKETS](/questions/47690/no-tcp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47690-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am running wireshark on a kali linux computer. I have an alfa usb wireless device. When I set my computer to run in monitor mode, wireshark does not see any tcp packets. I have been struggling with this for a few months now. When I first switched from a windows machine, I was seeing lots of tcp packets. But it seems that over time I started seeing less and less. Now I see nothing. It doesn't make any sense at all to me. And I don't have any capture or display filters on.</p></div><div id="question-tags" class="tags-container tags">packets tcp no</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '15, 13:41</strong></p><img src="https://secure.gravatar.com/avatar/efddbf0ae6e0c4b1cd182c684814c087?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rlwhiterose&#39;s gravatar image" /><p>rlwhiterose<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rlwhiterose has no accepted answers">0%</span></p></div></div><div id="comments-container-47690" class="comments-container"><span id="47693"></span><div id="comment-47693" class="comment"><div id="post-47693-score" class="comment-score"></div><div class="comment-text"><p>Have you set the wlan card to the correct WI-FI channell? maybe this related question can give you a hint: <a href="https://ask.wireshark.org/questions/47226/capture-80211ac-frames-in-monitor-mode">https://ask.wireshark.org/questions/47226/capture-80211ac-frames-in-monitor-mode</a></p></div><div id="comment-47693-info" class="comment-info"><span class="comment-age">(17 Nov '15, 14:19)</span> Christian_R</div></div><span id="47712"></span><div id="comment-47712" class="comment"><div id="post-47712-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the tip. But I don't really want to sniff a specific channel. I want to sniff everything. I have to do some more testing today, but I may have come up with something that works, even though it doesn't make any sense to me. When it wasn't working I was setting my computer to monitor mode like this:</p><p><em>ifconfig wlan1 down<br />
iwconfig mode monitor<br />
ifconfig wlan1 up</em></p><p>It seems to work when I do it like this:</p><p><em>ifconfig wlan1 down<br />
iwconfig mode managed<br />
ifconfig wlan1 up<br />
ifconfig wlan1 down<br />
iwconfig mode monitor<br />
ifconfig wlan1 up</em></p><p>That was working great yesterday. Going to do some more testing today.</p></div><div id="comment-47712-info" class="comment-info"><span class="comment-age">(18 Nov '15, 05:48)</span> rlwhiterose</div></div><span id="47713"></span><div id="comment-47713" class="comment"><div id="post-47713-score" class="comment-score"></div><div class="comment-text"><p>If you want to capture on more than one channel you can find some info here: <a href="https://wiki.wireshark.org/CaptureSetup/WLAN/">https://wiki.wireshark.org/CaptureSetup/WLAN/</a> -&gt; Section: channel hopping</p></div><div id="comment-47713-info" class="comment-info"><span class="comment-age">(18 Nov '15, 06:04)</span> Christian_R</div></div><span id="48158"></span><div id="comment-48158" class="comment"><div id="post-48158-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the link Christian. I will check it out.</p></div><div id="comment-48158-info" class="comment-info"><span class="comment-age">(01 Dec '15, 12:58)</span> rlwhiterose</div></div></div><div id="comment-tools-47690" class="comment-tools"></div><div class="clear"></div><div id="comment-47690-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

