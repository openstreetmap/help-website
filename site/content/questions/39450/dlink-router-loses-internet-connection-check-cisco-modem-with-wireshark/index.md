+++
type = "question"
title = "Dlink-Router loses Internet-Connection, Check Cisco-modem with Wireshark"
description = '''Hi all, my d&#x27;link dir 652 router (behind a cisco modem) loses internet connection every 15-30 minutes. i checked the router protocol and it says something with WAN-timer. So I ran Wireshark on my laptop tonight, directly connected to my cisco-Modem to see, if the modem loses the connection, or if it...'''
date = "2015-01-28T01:10:00Z"
lastmod = "2015-01-28T04:35:00Z"
weight = 39450
keywords = [ "internet", "wireshark" ]
aliases = [ "/questions/39450" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Dlink-Router loses Internet-Connection, Check Cisco-modem with Wireshark](/questions/39450/dlink-router-loses-internet-connection-check-cisco-modem-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39450-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all,</p><p>my d'link dir 652 router (behind a cisco modem) loses internet connection every 15-30 minutes. i checked the router protocol and it says something with WAN-timer. So I ran Wireshark on my laptop tonight, directly connected to my cisco-Modem to see, if the modem loses the connection, or if it's only the router.</p><p>Now I got a large protocol of about 45 MB but I am not able to analyze it due to lack of knowledge. How is a interruption of internet connection logged in wireshark protocols? What is it I have to search for?`</p><p>I see lots of stuff like "who has [IP] Tell [IP]", "TCP Keep Alive" and other messages I can not understand. Of course, if the connection didn't break, I won't find anything. But I don't even know what to look for... hope someone can help :)</p><p>Thanks in advance, Daniel</p></div><div id="question-tags" class="tags-container tags">internet wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jan '15, 01:10</strong></p><img src="https://secure.gravatar.com/avatar/ec0a42a402f9e3fa81148c352449db95?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MikeTakrelyt&#39;s gravatar image" /><p>MikeTakrelyt<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MikeTakrelyt has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Jan '15, 01:13</p></div></div><div id="comments-container-39450" class="comments-container"></div><div id="comment-tools-39450" class="comment-tools"></div><div class="clear"></div><div id="comment-39450-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39452"></span>

<div id="answer-container-39452" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39452-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There will not be any packets/messages in the capture file that actively inform you that the link was down. You will need to deduct that from the traffic that you expect and is not there. The logging on the Cisco-Modem might have messages that tell you when it brought the connection down, so look in the logs on the router. Most routers will also tell you how long the connection has been up on the "Status" page, so have a look there too.</p><p>You could perform a ping test (to 8.8.8.8 for instance) from a system behind the router (if you use a windows system, make sure it keeps sending pings by adding the '-t' option). Then in the captured data, you can look for "ICMP echo requests" that do not have a matching "ICMP echo reply", by pressing "&lt;ctrl&gt;+F" (find) and then type the display filter "icmp.type == 8 and not icmp.resp_in". This will look for the next "ICMP echo request" packet for which wireshark has not seen a response.</p><p>Of course if the WAN link goes down after an idle timeout, performing the ping will keep the connection open.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jan '15, 04:35</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-39452" class="comments-container"><span id="39453"></span><div id="comment-39453" class="comment"><div id="post-39453-score" class="comment-score"></div><div class="comment-text"><p>Hi, thanks for the reply. I don't think it is an idle timeout causing the interruption, as it also happens while gaming via PS3 or surfing on my laptop.</p><p>In the router log I can see the problem (old example from Feb 26, but still the same):</p><pre><code>Feb 26 09:39:21 info    UDHCPD Inform: add_lease xxx.xxx.x.xxx
Feb 26 09:38:36 info    using nameserver xx.xx.xxx.xxx#53
Feb 26 09:38:36 info    using nameserver xx.xx.xxx.xxx#53
Feb 26 09:38:36 info    reading /etc/resolv.conf
Feb 26 09:38:29 info    wantimer: [Cable Connect, No IP]-&#39;[Cable Connect, Have IP]
Feb 26 09:38:28 debug   open bandwidth_tmp.txt fail
Feb 26 09:38:28 debug   No DHCP ACK with option OPTION_6RD
Feb 26 09:38:27 info    Lease of xxx.xxx.xx.xxx obtained, lease time 3600
Feb 26 09:38:27 debug   Sending select for xxx.xxx.xx.xxx...
Feb 26 09:38:27 debug   DHCPC get gateway = xxx.xxx.xx.x
Feb 26 09:38:27 info    Sending discover...
Feb 26 09:38:27 debug   Performing a DHCPC renew
Feb 26 09:38:27 debug   DHCPC Received SIGUSR1=&#39;DHCPC Renew
Feb 26 09:38:27 info    wantimer: [Cable Connect, No IP]
Feb 26 09:38:25 info    wantimer: [Cable Connect, No IP]
Feb 26 09:38:23 info    wantimer: [Cable Connect, No IP]
Feb 26 09:38:21 info    wantimer: [Cable Connect, No IP]
Feb 26 09:38:19 info    wantimer: [Cable Connect, No IP]
Feb 26 09:38:17 info    wantimer: [Cable Connect, No IP]
Feb 26 09:38:15 info    wantimer: [Cable Connect, No IP]
Feb 26 09:38:13 info    wantimer: [Cable Connect, No IP]
Feb 26 09:38:11 info    wantimer: [Cable Connect, No IP]
Feb 26 09:38:09 info    wantimer: [Cable Connect, No IP]
Feb 26 09:38:07 info    wantimer: [Cable Connect, No IP]
Feb 26 09:38:05 info    wantimer: [Cable DisConnect, Have IP] -&#39; [Cable Connect, No IP]
Feb 26 09:38:02 debug   Entering released state
Feb 26 09:38:02 info    DHCP Release WAN IP address = 0.0.0.0
Feb 26 09:38:02 debug   Sending release...
Feb 26 09:38:02 info    Unicasting a release of xxx.xxx.xx.xxx to xx.xxx.xx.x
Feb 26 09:38:02 debug   Performing a DHCPC release
Feb 26 09:38:02 debug   DHCPC Received SIGUSR2=&#39;DHCPC Release
Feb 26 09:38:02 info    wantimer: [Cable Connect, Have IP] or [Cable Disconnect, Have IP] -&#39; [Cable Disconnect, Have IP]
Feb 26 09:35:44 debug   Sending renew...
Feb 26 09:34:13 info    ath0: STA 20:64:32:3b:e3:2a WPA: received EAPOL-Key 2/2 Group with unexpected replay counter
Feb 26 09:34:13 info    ath0: STA 20:64:32:3b:e3:2a WPA: group key handshake completed (RSN)
Feb 26 09:34:13 debug   ath0: STA 20:64:32:3b:e3:2a WPA: received EAPOL-Key frame (2/2 Group)</code></pre><hr /><p>So I think I know that the connection gets lost when using the router. That's why I connected the laptop to my Cisco-modem directly to find out with Wireshark, if there are any disconnects, too. So I think I have to do the "ping-thing" that you requested and let wireshark run. Can you explain how to do this regular ping? Can I set this up to ping every 5 seconds or so? And does it have to be an existing external IP like google? 8.8.8.8 was just an not working example, right?</p><p>Thanks in advance, Daniel</p></div><div id="comment-39453-info" class="comment-info"><span class="comment-age">(28 Jan '15, 05:12)</span> MikeTakrelyt</div></div><span id="39454"></span><div id="comment-39454" class="comment"><div id="post-39454-score" class="comment-score"></div><div class="comment-text"><p>Your DHCP lease time seems to be 3600 seconds and most DHCP clients will renew their lease at half of the lease time. So that would mean every 30 min. It seems in sync with how often you experience a disconnect.</p><p>Usually an IP address is not released until a new lease has been received from the DHCP server. In your log however, it seems that the IP address is released before the new lease is given by the modem. This looks like a bug to me. Did you update your router to the latest firmware already? If not, I would try that first.</p><p>Pinging 8.8.8.8 was an example, you can ping any address as long as it is on the outside so it will pass your router and your modem. How to use ping differs depending on the OS. Type "ping /?" on windows for more info or "man ping" on OS/X, linux, *BSD, etc.</p></div><div id="comment-39454-info" class="comment-info"><span class="comment-age">(28 Jan '15, 05:31)</span> SYN-bit ♦♦</div></div><span id="39467"></span><div id="comment-39467" class="comment"><div id="post-39467-score" class="comment-score"></div><div class="comment-text"><p>I have recognized that lease time of 3600 before, too, but I didn't know if I can change that by myself, without destroying any other configuration. I updated the router to the latest firmware some time ago, which is 2.00 Rev. B, there is no newer firmware on the web so far.</p><p>Do you think I can just increase the lease time to lets say 28800, which will mean every 480 minutes/8 Hours, so the release/renew will be done by the router every 4 hours, which would be OK for me.</p><p>Or does the lease need to be synced to the time that the cisco modem performes a lease? I think I didn't understand all the "router-talks-to-modem"-thing :) Very complicated stuff.</p><p>Anyway I willm perform the ping test overnight with Wireshark when I have the time to.</p><p>Thanks man you are a really great helf after noone was able to help me with this (ISP, dlink, cisco...noone was able so far, very annoying)...</p><p>one more thing: just found that the Cisco has also something set with 3600 seconds on one of it's pages I was able to access, but it doesn't look like it's something that should be changed...mhhh: <img src="http://i.imgur.com/atAC77e.png" alt="alt text" /> Also this part of the log might be interesting: <img src="http://i.imgur.com/bhvyc4w.png" alt="alt text" /></p><p>Will try to get newer logs as well...</p></div><div id="comment-39467-info" class="comment-info"><span class="comment-age">(29 Jan '15, 00:30)</span> MikeTakrelyt</div></div></div><div id="comment-tools-39452" class="comment-tools"></div><div class="clear"></div><div id="comment-39452-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

