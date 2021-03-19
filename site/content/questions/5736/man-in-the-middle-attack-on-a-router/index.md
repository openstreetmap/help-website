+++
type = "question"
title = "Man in the Middle attack on a Router?"
description = '''To keep it simple: I want to capture ethernet traffic on my LAN. Its a mansion that we are in and am the admin. All we have is a 5yr-old Netgear router. It has four output ports. I am connected in one of them. I have already gone through the wiki: http://wiki.wireshark.org/CaptureSetup/Ethernet. I g...'''
date = "2011-08-18T02:18:00Z"
lastmod = "2011-08-19T21:00:00Z"
weight = 5736
keywords = [ "router", "bandwidth", "mitm" ]
aliases = [ "/questions/5736" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Man in the Middle attack on a Router?](/questions/5736/man-in-the-middle-attack-on-a-router)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5736-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>To keep it simple: I want to capture ethernet traffic on my LAN. Its a mansion that we are in and am the admin. All we have is a 5yr-old Netgear router. It has four output ports. I am connected in one of them. I have already gone through the wiki: <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">http://wiki.wireshark.org/CaptureSetup/Ethernet</a>. I get what it says, but we dont use any switch or hub, and it doesn't mention any thing abt routers. Its just 4 of us connecting directly to the ADSL router. I wanna know who is using up the most bandwitdh. I cant afford to buy a switch or a hub. So, i was thinking abt the MITM attack.</p><p>But i have no idea, how any of these methods will work in case of a router, since i believe its more sophisticated and intelligent than a switch. So, need some advice or knowledge into this.</p><p>My objective is simple: I need to capture and explore the ethernet traffic on my LAN.</p><p>If MITM is not possible/suitable in my setup, please guide me to a more viable option.</p></div><div id="question-tags" class="tags-container tags">router bandwidth mitm</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '11, 02:18</strong></p><img src="https://secure.gravatar.com/avatar/07a159f31a976cf508a07f2d74200959?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nsantosh&#39;s gravatar image" /><p>nsantosh<br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nsantosh has no accepted answers">0%</span></p></div></div><div id="comments-container-5736" class="comments-container"></div><div id="comment-tools-5736" class="comment-tools"></div><div class="clear"></div><div id="comment-5736-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5737"></span>

<div id="answer-container-5737" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5737-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your referring to an ADSL router. Please be aware that this is more than an (IP network) <a href="http://en.wikipedia.org/wiki/Router_%28computing%29">router</a>. It is more a <a href="http://en.wikipedia.org/wiki/Residential_gateway">residential gateway</a>, which means that:</p><ul><li>It connects to the DSLAM in your local exchange</li><li>It performs NAT</li><li>It performs DHCP for your local network</li><li>It switches your local network</li><li>Might even do WiFi, VoIP, POTS, DECT (although that's in <a href="http://www.avm.de/en/Produkte/FRITZBox/FRITZ_Box_Fon_WLAN_7270/index.php">the newer models</a>)</li></ul><p>Note that these four connections are indeed switch ports. The other end of the switch is internal to the device, for it to provide DHCP, NAT and routing service over the DSL line.</p><p>So it's a question of can you manipulate the switch in your ADLS router? Does it allow 'ARP poisoning' or does it create havoc? You'll have to try out. Be aware that all traffic will be flowing through your connection and your platform, so this may offset/influence the very thing you want to measure.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Aug '11, 04:07</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-5737" class="comments-container"><span id="5738"></span><div id="comment-5738" class="comment"><div id="post-5738-score" class="comment-score"></div><div class="comment-text"><p>@Jaap: You are right! It is a residential gateway and it performs NAT, DHCP, etc. So how can you say if the switch in the router can be manipulated (ARP poisoning)? Is it something dependent on the router's model? Router's model is <strong>Netgear wgr614 v7</strong> btw.</p><p>And by "<strong><em>all traffic will be flowing through your connection and your platform</em></strong>", you mean it will flow thru the attacker's machine right? My machine in this case.</p></div><div id="comment-5738-info" class="comment-info"><span class="comment-age">(18 Aug '11, 04:45)</span> nsantosh</div></div><span id="5741"></span><div id="comment-5741" class="comment"><div id="post-5741-score" class="comment-score"></div><div class="comment-text"><p>Note, your reply above should have been a comment to Jaap's answer not a "new answer". (I converted it to a comment -Guy Harris)</p><p>Arp poisoning (or spoofing) means fooling a machine about the location of another machine and making it send packets to another place where they are intercepted.</p><p>See <a href="http://en.wikipedia.org/wiki/ARP_spoofing">here</a> for more info.</p></div><div id="comment-5741-info" class="comment-info"><span class="comment-age">(18 Aug '11, 08:18)</span> grahamb ♦</div></div></div><div id="comment-tools-5737" class="comment-tools"></div><div class="clear"></div><div id="comment-5737-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5776"></span>

<div id="answer-container-5776" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5776-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't know that Wireshark is the tool you want for this job. What you really want is a switch/router monitor application.</p><p>I'd recommend something like Fluke Networks' FREE Switch Port Monitor, available from <a href="http://networking.flukenetworks.com/?elqPURLPage=607">http://networking.flukenetworks.com/?elqPURLPage=607</a> - it talks SNMP, as do most DSL routers, and I've used it to track throughput on DSL routers from several different manufacturers.<br />
</p><p>If you're up for something a little more ambitious, you might also take a look at Multi-Router Traffic Grapher (MRTG), at http://oss.oetiker.ch/mrtg/ - this freeware product talks to a dizzying variety of network devices and produces very nice hourly/daily/weekly/monthly usage charts for each interface.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Aug '11, 21:00</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p>wesmorgan1<br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Aug '11, 21:05</p></div></div><div id="comments-container-5776" class="comments-container"><span id="5781"></span><div id="comment-5781" class="comment"><div id="post-5781-score" class="comment-score"></div><div class="comment-text"><p>If he ultimately wants statistics, yes, and the only thing he'll do with the traffic on the LAN is summarize it, Wireshark might not be the best tool.</p><p>If, however, he truly wants to "capture ethernet traffic on [his] LAN", and needs to see the traffic rather than just get summary statistics from it, the tools you mention don't look as if they'll help.</p></div><div id="comment-5781-info" class="comment-info"><span class="comment-age">(20 Aug '11, 12:01)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-5776" class="comment-tools"></div><div class="clear"></div><div id="comment-5776-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

