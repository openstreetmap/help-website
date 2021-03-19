+++
type = "question"
title = "Windows 7 Ethernet Adapter broadcast to Linksys E300 router"
description = '''I am new to Wireshark. I keep getting this request from my Windows 7 Ethernet Adapter to the router. When running Wireshark, I filter eth.type == 0x0806, I see the following.  Number - 37932 Time - 17:16:41.240610 Source - AsustekC_f5:9d:a0 Destination - Broadcast Protocol - ARP Length - 42  Info - ...'''
date = "2011-08-02T15:28:00Z"
lastmod = "2011-08-10T20:12:00Z"
weight = 5409
keywords = [ "linksyse3000" ]
aliases = [ "/questions/5409" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Windows 7 Ethernet Adapter broadcast to Linksys E300 router](/questions/5409/windows-7-ethernet-adapter-broadcast-to-linksys-e300-router)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5409-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5409-score" class="post-score" title="current number of votes">0</div><span id="post-5409-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am new to Wireshark. I keep getting this request from my Windows 7 Ethernet Adapter to the router. When running Wireshark, I filter eth.type == 0x0806, I see the following.</p><p>Number - 37932 Time - 17:16:41.240610 Source - AsustekC_f5:9d:a0 Destination - Broadcast Protocol - ARP Length - 42<br />
Info - Who has 192.168.1.102? Tell 192.168.1.100</p><p>The IP address is my laptop. When the laptop is on, it is identified by mac address. When it is off, this request keeps asking who has this address. This does not happen to the other devices (laptop or printers) on my network when they are turned off. Any ideas on why this is happening?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-linksyse3000" rel="tag" title="see questions tagged &#39;linksyse3000&#39;">linksyse3000</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Aug '11, 15:28</strong></p><img src="https://secure.gravatar.com/avatar/20fc7876688f9ec45c550945ef7dc2fb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rattlesnake&#39;s gravatar image" /><p><span>Rattlesnake</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rattlesnake has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Aug '11, 15:29</strong> </span></p></div></div><div id="comments-container-5409" class="comments-container"><span id="5634"></span><div id="comment-5634" class="comment"><div id="post-5634-score" class="comment-score"></div><div class="comment-text"><p>I looked into what has been going on and found that someone had at one time had an HP printer directly hooked up to a wireless router. When the desktop was looking for a printer, the HP was available and was connected at IP address 192.168.1.102. This information was stored into the registry on the desktop. The printer was taken from the desktop and another laptop was added to the network at the same IP address. This was not known at the time of installation. We began to get weird responses on the laptop. We installed Wireshark and then we found that the network adapter on our desktop was broadcasting who is at IP address 192.168.1.102. I used the arp –a and –d commands as administrator. The problem when away for a week, but we kept being broadcast on another printer that was installed this week. It appears that our network is being spoofed. Any ideas on what software that can be used to detect what is going on.</p><p>Thanks</p></div><div id="comment-5634-info" class="comment-info"><span class="comment-age">(10 Aug '11, 15:59)</span> <span class="comment-user userinfo">Rattlesnake</span></div></div><span id="5638"></span><div id="comment-5638" class="comment"><div id="post-5638-score" class="comment-score"></div><div class="comment-text"><p>FYI I converted your answer to a comment.</p><p>Seems to me you might have trouble with duplicate IP addresses if I understand the setup correctly: if the printer was once hosted at the router and had the IP 192.168.1.102 the router might still be configured with that IP. The Desktop has the same IP, so that could be a problem. I'd check the router config to make sure this is not the case.</p><p>And I doubt the network is being spoofed, it is much more common to have some sort of a misconfiguration that is the reason for trouble. Keep in mind: ARP requests are broadcasts, ARP replies are unicast.</p></div><div id="comment-5638-info" class="comment-info"><span class="comment-age">(10 Aug '11, 20:12)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-5409" class="comment-tools"></div><div class="clear"></div><div id="comment-5409-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5410"></span>

<div id="answer-container-5410" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5410-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5410-score" class="post-score" title="current number of votes">4</div><span id="post-5410-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What you see are ARP requests, meaning that a device (in this case with the MAC adress AsustekC_f5:9d:a0 and the IP address 192.168.1.100) wants to know a MAC address for another IP, in this case 192.168.1.102. Network frames on ethernet networks need to be delivered to MAC addresses, and since the node with IP 192.168.1.100 wants to talk to 192.168.1.102 it needs to find out which MAC address the node with IP 192.168.1.100 actually has. This information is discarded every once in a while and a new question is send, in case the ethernet address (MAC) for the IP has changed in the meantime.</p><p>You should see ARP requests (ethertype 0x0806) like that for all IPs your PC is talking to and that it doesn't already know. If a device is turned of you might still see ARP requests for its IP address.</p><p>You can check your ARP cache on the command line using the command "arp -a", and clear it using "arp -d". On Windows 7 you might need elevated user rights to clear the arp cache though (meaning, you need to start the command line "as administrator").</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Aug '11, 16:50</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-5410" class="comments-container"></div><div id="comment-tools-5410" class="comment-tools"></div><div class="clear"></div><div id="comment-5410-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5416"></span>

<div id="answer-container-5416" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5416-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5416-score" class="post-score" title="current number of votes">2</div><span id="post-5416-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When you see ARP requests for an IP address which belongs to a system (your laptop in this case) that has been switched off, this means someone in the network still wants to communicate to the system that is switches off.</p><p>It could be that there were still open file shares or TCP connections to it when the system was taken of the network. Or maybe you have enabled some port forwarding rules on your router and someone from the Internet is trying to connect to one of the forwarded ports.</p><p>Have a look on the system that is arping to see what could be the reason. Also, when turning the system back on, you will see what kind of communication follows the ARP process, then you know what kind of traffic was causing the system to ARP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '11, 01:15</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5416" class="comments-container"></div><div id="comment-tools-5416" class="comment-tools"></div><div class="clear"></div><div id="comment-5416-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

