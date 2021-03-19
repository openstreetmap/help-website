+++
type = "question"
title = "Capture connected devices data and access point data"
description = '''Hi, We are running wireshark on a network switch that manages a WIFI network made out of several Access Points. We are interested in finding packets information on wireshark to allow us to trace the access point being used by each connected device. We are not interested in knowing the traffic they g...'''
date = "2017-02-15T22:08:00Z"
lastmod = "2017-02-16T03:22:00Z"
weight = 59461
keywords = [ "connected", "devices", "accesspoint" ]
aliases = [ "/questions/59461" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture connected devices data and access point data](/questions/59461/capture-connected-devices-data-and-access-point-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59461-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>We are running wireshark on a network switch that manages a WIFI network made out of several Access Points.</p><p>We are interested in finding packets information on wireshark to allow us to trace the access point being used by each connected device. We are not interested in knowing the traffic they generate, only which devices are connected, where and for how long.</p><p>We work in a large campus and the requirement is to find out where are people connected at any given time.</p><p>Thanks for your help.</p></div><div id="question-tags" class="tags-container tags">connected devices accesspoint</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Feb '17, 22:08</strong></p><img src="https://secure.gravatar.com/avatar/2726f9b4275eece61b48634fe61004f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Xavier&#39;s gravatar image" /><p>Xavier<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Xavier has no accepted answers">0%</span></p></div></div><div id="comments-container-59461" class="comments-container"></div><div id="comment-tools-59461" class="comment-tools"></div><div class="clear"></div><div id="comment-59461-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59464"></span>

<div id="answer-container-59464" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59464-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is best left to specific tools for the job, such as Cisco's <a href="http://www.cisco.com/c/en/us/products/cloud-systems-management/prime-infrastructure/index.html">Prime Infrastructure</a> software suite. Other large vendors have similar tools - try Aruba/HP's <a href="http://www.arubanetworks.com/products/networking/management/airwave/">Airwave</a> tool, or Extreme Networks <a href="http://www.extremenetworks.com/product/management-center/">Management Center</a>.<br />
</p><p>You don't describe the architecture so it really is not clear how you would deploy a packet sniffer solution to get at the information you need. At the lowest level, if they are just a bunch of standalone APs then you would need to capture data from each one - I guess you could link traffic to/from a particular AP based on physical port, so you might need one port mirror or tap per AP. Perhaps you are routing so would consider grabbing all the data to/from the router (say if you implemented a 'router on a stick' type network) but if these are just basic wireless bridges, you would lose which data came from which AP. I guess you could have separate VLANs for each AP and could track that way - with a different subnet/DHCP server on each vlan you would know then by DHCP logs who is where, but at this point you are just moving the problem. I have been to facilities with 1000's of APs - I would not enjoy setting up infrastructure in this way.<br />
</p><p>If you have a wireless controller (which you should really have if you have a large campus and more than a handful of access points), it may give you some of the information you are looking for already in the monitoring section of the config tool (maybe https or CLI based, whatever). Probably not as good or as rich of a data set as you get with the network managers, but still probably easier to implement than with a packet capture system. For instance, you can probably get which device is connected where at this instant, but there would no historical capability. With the management tools, they can can give you history so you can see number of devices, which band, how much throughput, etc., throughout a period of time. Quite valuable as a whole, and then of course you get the individual device level as well - what was the throughput, signal strength, connected AP, etc., for this specific device over the past 15 days? Helps with troubleshooting.<br />
</p><p>If you had a large campus, it is unlikely that each AP is terminated at the same switch. Usually cat5/6 cable run limits require that APs be placed on the edge, which would further complicate data gathering through a sniffer mechanism. I guess Remote SPAN and similar concepts could be used, but with the proliferation of 802.11ac technologies, at some point you will run out of wired bandwidth if you are going to tunnel all wifi traffic back to a single location.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '17, 03:22</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span> </br></br></p></div></div><div id="comments-container-59464" class="comments-container"><span id="59475"></span><div id="comment-59475" class="comment"><div id="post-59475-score" class="comment-score"></div><div class="comment-text"><p>The one thing that I would add: If you HAVE to use a packet capturing tool to determine the connected clients, I would recommend using dumpcap instead of Wireshark.</p><p><a href="https://www.wireshark.org/docs/man-pages/dumpcap.html">https://www.wireshark.org/docs/man-pages/dumpcap.html</a></p><p>When capturing large amounts of packets for an extended period time, there are some known limitations using Wireshark. In order to optimize system memory usage, the program tool dumpcap.exe, which accompanies the Wireshark installation, can be utilized.</p></div><div id="comment-59475-info" class="comment-info"><span class="comment-age">(16 Feb '17, 07:15)</span> Amato_C</div></div></div><div id="comment-tools-59464" class="comment-tools"></div><div class="clear"></div><div id="comment-59464-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

