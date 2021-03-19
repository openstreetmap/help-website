+++
type = "question"
title = "Lag network http/https?"
description = '''Hi, I was wondering if someone could assist me? So for the past month and could not decipher the issue that im having. Currently Running pfSense with OpenVPN, squid3, squidguard, Ntopng,Sarg, lightsquid, and WPAD. The internet service has 28mbps down and up 15mbps with ping 31ms Many users been comp...'''
date = "2016-09-07T17:53:00Z"
lastmod = "2016-09-07T17:53:00Z"
weight = 55387
keywords = [ "tcp_retransmission" ]
aliases = [ "/questions/55387" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lag network http/https?](/questions/55387/lag-network-httphttps)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55387-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55387-score" class="post-score" title="current number of votes">-1</div><span id="post-55387-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I was wondering if someone could assist me? So for the past month and could not decipher the issue that im having. Currently Running pfSense with OpenVPN, squid3, squidguard, Ntopng,Sarg, lightsquid, and WPAD. The internet service has 28mbps down and up 15mbps with ping 31ms Many users been complaining for the past weeks about slow lag internet I really did not notice until I tried navigating a few sites and all of sudden it would not load the website it would take maybe around 5 seconds which is not much but is not very acceptable when you have 28mbps. I want to first check if there is something wrong with the settings of Squid before seeing if there’s an issue with the cables or the switches. All the users are forcefully navigating though WPAD because I blocked them on ports 443-80 Without transparent proxy. See pictures. Also we have a SQL database(Virtual machine) which users go to the browser (192.168.1.206) and report information(MRP) but when they are going to report it, it get stuck showing as 0(packet loss not sending to the server 192.168.1.206), or times they say it won’t load the webpage (192.168.1.206) So im not sure if it’s the proxy itself of the WPAD or the switches? The VLAN That I created for the devices which is on 192.168.40.0/24, These devices only purpose is to connect only to 192.168.1.206 (via browser), I did this because thinking of arp congestion but still there complaining about it. And for the rest of the LAN 192.168.1.0/24 they mostly go to websites and at times there is lag. So then I had to check with wireshark. The packet capture was ran from pfSense (around 5mins) which I then downloaded to see what was going on. Which then I realized that there was massive amounts of TCP Retransmission, and 2 TCP zero windows (thinking might be the network card of pfSense) Now what I can’t determine is it the switch itself or the server? At one point thought it was the DNS but I saw that most DNS requests were less then 150ms.</p><p>Packet Capture (sorry it’s a tad bit heavy 136mb): <a href="https://mega.nz/#!RsAh1CKA!gxYChuCWavhXIe-C9oBD50SLuq7XGscR4tm0MRJhb_I">https://mega.nz/#!RsAh1CKA!gxYChuCWavhXIe-C9oBD50SLuq7XGscR4tm0MRJhb_I</a></p><p>Pictures:----<a href="http://postimg.org/gallery/2g022j18m/">http://postimg.org/gallery/2g022j18m/</a></p><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp_retransmission" rel="tag" title="see questions tagged &#39;tcp_retransmission&#39;">tcp_retransmission</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Sep '16, 17:53</strong></p><img src="https://secure.gravatar.com/avatar/dd2630227be6d715406847ade75c3d27?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="killmasta93&#39;s gravatar image" /><p><span>killmasta93</span><br />
<span class="score" title="-1 reputation points">-1</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="killmasta93 has no accepted answers">0%</span></p></div></div><div id="comments-container-55387" class="comments-container"></div><div id="comment-tools-55387" class="comment-tools"></div><div class="clear"></div><div id="comment-55387-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

