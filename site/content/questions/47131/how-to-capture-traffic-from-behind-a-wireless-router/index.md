+++
type = "question"
title = "how to capture traffic from behind a wireless router ?"
description = '''I have setup a lab environment my wireshark pc is at 172.16.1.2 my wireless router is at 172.16.0.3 and it has a nat network of 192.168.0.0/24 i have a apache server at 172.16.1.4 i want to catch http traffic from a device using 192.168.0.2 to my apache server at 172.16.1.4 im using mitm to route th...'''
date = "2015-11-01T05:11:00Z"
lastmod = "2015-11-02T04:08:00Z"
weight = 47131
keywords = [ "wireless", "router", "switch", "nat", "wireshark" ]
aliases = [ "/questions/47131" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to capture traffic from behind a wireless router ?](/questions/47131/how-to-capture-traffic-from-behind-a-wireless-router)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47131-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have setup a lab environment my wireshark pc is at 172.16.1.2 my wireless router is at 172.16.0.3 and it has a nat network of 192.168.0.0/24 i have a apache server at 172.16.1.4 i want to catch http traffic from a device using 192.168.0.2 to my apache server at 172.16.1.4 im using mitm to route the wireless routers traffic through my wireshark box to the gateway 172.16.1.1 but cant capture any http traffic between 192.168.0.2 and 172.16.1.4.How can i accomplish this ? Thanks for reading.</p></div><div id="question-tags" class="tags-container tags">wireless router switch nat wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Nov '15, 05:11</strong></p><img src="https://secure.gravatar.com/avatar/164e796c00b1488439efd3fb85210a48?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dantezyates&#39;s gravatar image" /><p>Dantezyates<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dantezyates has no accepted answers">0%</span></p></div></div><div id="comments-container-47131" class="comments-container"></div><div id="comment-tools-47131" class="comment-tools"></div><div class="clear"></div><div id="comment-47131-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47147"></span>

<div id="answer-container-47147" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-47147-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p><strong>im using mitm</strong> to route the wireless routers traffic through my wireshark box to the gateway 172.16.1.1 <strong>but cant capture any http traffic</strong></p></blockquote><p>Apparently your capture setup is faulty. Please read the Ethernet Capture Wiki to figure out how to capture that traffic.</p><blockquote><p><a href="https://wiki.wireshark.org/CaptureSetup/Ethernet">https://wiki.wireshark.org/CaptureSetup/Ethernet</a></p></blockquote><p>Most certainly, the best way would be to use a <a href="https://ask.wireshark.org/questions/13892/port-mirror-switch">cheap switch with port mirroring capabilities</a>, or to capture on one of the involved systems (192.168.0.2 or 172.16.1.4). If neither of these is an option for you, you'll have to figure out what's wrong with your MITM setup.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Nov '15, 04:08</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Nov '15, 04:08</p></div></div><div id="comments-container-47147" class="comments-container"><span id="47168"></span><div id="comment-47168" class="comment"><div id="post-47168-score" class="comment-score"></div><div class="comment-text"><p>im using ettercap with this command "ettercap -Tqi eth0 -M arp //172.16.1.1/ //172.16.1.3/" 1 is gateway and 3 is the wireless router that 192.168.0.2 is sitting behind</p></div><div id="comment-47168-info" class="comment-info"><span class="comment-age">(02 Nov '15, 11:35)</span> Dantezyates</div></div><span id="47174"></span><div id="comment-47174" class="comment"><div id="post-47174-score" class="comment-score">1</div><div class="comment-text"><p>This is the Wireshark Q&amp;A site. As your prolem is related to ettercap, you'd better ask the question in an ettercap forum, or a pentesting forum like: <a href="https://forums.kali.org/">https://forums.kali.org/</a></p><p>Just a brief hint: Maybe the wireless router and/or your gateway ignores your arp spoofing tricks (for whatever reason).</p></div><div id="comment-47174-info" class="comment-info"><span class="comment-age">(02 Nov '15, 16:09)</span> Kurt Knochner ♦</div></div><span id="47178"></span><div id="comment-47178" class="comment"><div id="post-47178-score" class="comment-score"></div><div class="comment-text"><p>well i can see all the traffic routing through my wireshark machine just not the http login</p></div><div id="comment-47178-info" class="comment-info"><span class="comment-age">(03 Nov '15, 01:02)</span> Dantezyates</div></div><span id="47181"></span><div id="comment-47181" class="comment"><div id="post-47181-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>just not the http login</p></blockquote><p>most certainly because the login is transmitted via https.</p></div><div id="comment-47181-info" class="comment-info"><span class="comment-age">(03 Nov '15, 04:34)</span> Kurt Knochner ♦</div></div><span id="47259"></span><div id="comment-47259" class="comment"><div id="post-47259-score" class="comment-score"></div><div class="comment-text"><p>how can they ? the site is http only its only a virtual ubuntu box running apache2 .</p></div><div id="comment-47259-info" class="comment-info"><span class="comment-age">(04 Nov '15, 12:47)</span> Dantezyates</div></div><span id="47295"></span><div id="comment-47295" class="comment not_top_scorer"><div id="post-47295-score" class="comment-score"></div><div class="comment-text"><p>I concluded that only from your statement.</p><blockquote><p>well <strong>i can see all the traffic</strong> routing through my wireshark machine <strong>just not the http login</strong></p></blockquote><p>If you can see ALL traffic (which includes HTTP in general), but not the 'HTTP login', I see the following possible reasons:</p><ul><li>the password is transmitted via HTTPS. Whether that's possible depends on the configuration of the server. I can't tell you.</li><li>the password gets transmitted in cleartext, but you can't find it. There are many reasons. I can't tell you without a pcap file and some description what you did to find the login/password/whatever you are looking for.</li><li>the password gets transmitted in an encoded form (e.g. done by Javascript)</li></ul><p>Without a pcap file and more details about the nature of the 'HTTP login' (is it a form based authentication, HTTP Basic authentication, etc.), it's impossible to tell you more that I did.</p></div><div id="comment-47295-info" class="comment-info"><span class="comment-age">(05 Nov '15, 08:47)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-47147" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-47147-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

