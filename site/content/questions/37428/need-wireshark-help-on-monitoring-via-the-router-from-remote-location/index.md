+++
type = "question"
title = "Need Wireshark help on monitoring via the router from remote location"
description = '''hello and thank you for your help in advance. i have a home network with several iPhones and iPads using wifi from an apple airport extreme router.this router is connected directly to the fiber optic ethernet of the cable company for the internet and i have it configured for setup over WAN. on this ...'''
date = "2014-10-29T04:39:00Z"
lastmod = "2014-10-29T07:04:00Z"
weight = 37428
keywords = [ "remote-monitoring", "smsmonitor", "airport", "router", "extreme" ]
aliases = [ "/questions/37428" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Need Wireshark help on monitoring via the router from remote location](/questions/37428/need-wireshark-help-on-monitoring-via-the-router-from-remote-location)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37428-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello and thank you for your help in advance. i have a home network with several iPhones and iPads using wifi from an apple airport extreme router.this router is connected directly to the fiber optic ethernet of the cable company for the internet and i have it configured for setup over WAN. on this network i also have two iMac computers which connect to the internet via the wifi network from the airport extreme router, i think it is setup currently with WPA but not sure i know i can change that if i need to to get unencrypted data.</p><p>i have wireshark running on a mac pro on another location and i can access the router and the computers remotely at the home network.</p><p>i would like to monitor the wifi traffic on the home network and specifically sniff out passwords and or text messages and iMessages that are sent from the wireless clients to whomever via the wifi signal of the home network, also the web activity of the iMacs i can actually see by logging in directly from remote but i can not see passwords or anything else sent in packets thru the router, and i want to see that with wireshark</p><p>is this possible, ?? text messages specifically?? all are iPhones and all are using the wifi signal of my network to text and email etc</p><p>some emails are via web interface thru the wifi some ate smtp via wifi from apple mac mail platform so i have wireshark and have poked around in it but can not see how to choose a remote ip address to sniff traffic and not sure how to de-encrypt my network so that the info passwords etc can be viewed even if temporarily.</p><p>Thanks very much</p></div><div id="question-tags" class="tags-container tags">remote-monitoring smsmonitor airport router extreme</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Oct '14, 04:39</strong></p><img src="https://secure.gravatar.com/avatar/581069fe9d937cbaf5d6cd9f7470299f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="panicgolf&#39;s gravatar image" /><p>panicgolf<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="panicgolf has no accepted answers">0%</span></p></div></div><div id="comments-container-37428" class="comments-container"></div><div id="comment-tools-37428" class="comment-tools"></div><div class="clear"></div><div id="comment-37428-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37438"></span>

<div id="answer-container-37438" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37438-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>help on monitoring via the router from <strong>remote location</strong></p></blockquote><p>See the answer for a similar question:</p><blockquote><p><a href="https://ask.wireshark.org/questions/20771/need-to-capture-3-ip-address-at-remote-location">https://ask.wireshark.org/questions/20771/need-to-capture-3-ip-address-at-remote-location</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Oct '14, 07:04</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-37438" class="comments-container"><span id="37515"></span><div id="comment-37515" class="comment"><div id="post-37515-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the input, my situation is similar but i didn't share all details. i have a home network with a router that all wifi flows through, i can access that router remotely from another apple mac machine at a remote location, i dial into the router with the IP of the router, since the router is the wifi base also is that the iP i need to scrub for traffic? and do i run wireshark on the machine that is remote?</p><p>i can also connect to a machine on the network i am talking about and i can download wireshark onto the machine but that machine is not connected to the router but with a wifi signal, no ethernet. i could run WS from tat machine remotely but it would be the same as the original remote machine which is much easier....am i correct in this assumption??</p><p>i don't think any of the wifi devices flow through the machine i can access on the net work so i would not be capturing anything different.</p><p>now i do want to capture specific info from the machine on the network, so if running wireshark on that machine is better for that purpose that is an option.</p><p>i am specifically interested in a iPhone which connects to this home network often, that is the info i need also, texts, passwords etc if that can be seen with wireshark. if that can be seen with the access to the computer on the network then please let me know/ Thanks for your help</p><p>will wireshark work on a specific machine rather than sniffing a etowrk?? is there some port setting that i can just replicate on the machine in question to capture all the info i need? i own all the hardware and machines i am speaking of an have all authority to look for what i am . Thanks</p></div><div id="comment-37515-info" class="comment-info"><span class="comment-age">(31 Oct '14, 14:46)</span> panicgolf</div></div></div><div id="comment-tools-37438" class="comment-tools"></div><div class="clear"></div><div id="comment-37438-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

