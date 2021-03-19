+++
type = "question"
title = "How to catch everything that goes through my wifi router?"
description = '''I read through the wireless capture and the other hub/switch/tap capturing, but I&#x27;m very confused.  What I want to do is capture all of the info from my wifi router from how ever many users are using it at that time. The router is sitting next to my laptop, so I have access to it. What do I have to ...'''
date = "2010-12-02T13:13:00Z"
lastmod = "2014-10-08T10:51:00Z"
weight = 1213
keywords = [ "capture", "switch", "wifi", "tap", "hub" ]
aliases = [ "/questions/1213" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [How to catch everything that goes through my wifi router?](/questions/1213/how-to-catch-everything-that-goes-through-my-wifi-router)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1213-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1213-score" class="post-score" title="current number of votes">0</div><span id="post-1213-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I read through the wireless capture and the other hub/switch/tap capturing, but I'm very confused.<br />
</p><p>What I want to do is capture all of the info from my wifi router from how ever many users are using it at that time. The router is sitting next to my laptop, so I have access to it. What do I have to buy?</p><p>I feel like simple is better and that there should be something I can connect to the router and connect that to my computer that will do the job. Any help is appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-switch" rel="tag" title="see questions tagged &#39;switch&#39;">switch</span> <span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span> <span class="post-tag tag-link-tap" rel="tag" title="see questions tagged &#39;tap&#39;">tap</span> <span class="post-tag tag-link-hub" rel="tag" title="see questions tagged &#39;hub&#39;">hub</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '10, 13:13</strong></p><img src="https://secure.gravatar.com/avatar/57ca9f4e4f4f585bf6010a6f86f94724?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neilk&#39;s gravatar image" /><p><span>neilk</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neilk has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-1213" class="comments-container"></div><div id="comment-tools-1213" class="comment-tools"></div><div class="clear"></div><div id="comment-1213-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

5 Answers:

</div>

</div>

<span id="1256"></span>

<div id="answer-container-1256" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1256-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1256-score" class="post-score" title="current number of votes">1</div><span id="post-1256-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Most simple IMO:</p><p>Download some bootable Linux-Live-whatever distro (Slitaz-AirCrack-NG f.e.) and throw your Laptop into wireless sniffing mode.</p><ul><li>Boot up Linux including AirCrack</li><li>run iwconfig to locate the name of your wireless NIC (typically wlan0, ath0 or sth. like that)</li><li>run 'airodump-ng wlan0' &lt;-- insert your NIC name instead of wlan0 if different</li><li>search the output for the channel and MAC address of your wireless AP</li><li>stop airodump by CTRL-C</li><li>restart it including filters for your AP and write to disk:</li><li>airodump-ng -c (channel number) -w /(saving folder and filename) --bssid (mac address of your AP) wlan0</li></ul><p>The whole scenario also works on a flashed linksys OpenWRT of course if you want to have a 24/7 sniffer</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Dec '10, 06:02</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p><span>Landi</span><br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Dec '10, 06:24</strong> </span></p></div></div><div id="comments-container-1256" class="comments-container"></div><div id="comment-tools-1256" class="comment-tools"></div><div class="clear"></div><div id="comment-1256-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1214"></span>

<div id="answer-container-1214" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1214-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1214-score" class="post-score" title="current number of votes">0</div><span id="post-1214-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Having access to the router is a start. However it is a low-end home-user router it is unlikely to have what is needed built-in - 99.9% of home users won't know how to use wireshark. If is more of an enterprise grade router it might have a packet capture function or port-mirroring function - check the manual.</p><p>Another option, is if your router can be changed to run a more open and flexible software stack like OpenWRT then you can do packet captures onboard with tcpdump.</p><p>If your router connects to Internet (or the rest of the network) via Ethernet then you can install a hub or cheap port-mirroring capable switch to copy that traffic to another port for Wireshark monitoring. For instance an HP ProCurve 1810G can do this. You might also find an old Ethernet hub (not switch) that will repeat traffic out of all ports to the same end.</p><p>Finally if you just want to capture the wireless traffic - you can use a laptop with Wireless to do this. Your wireless card and encryption method will help determine your success - and you can get some dedicated capture cards such as those from CACE that might be helpful</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '10, 14:50</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p><span>martyvis</span><br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-1214" class="comments-container"><span id="1222"></span><div id="comment-1222" class="comment"><div id="post-1222-score" class="comment-score"></div><div class="comment-text"><p>I read the stuff you are talking about and that is what confused me, because the setup I want should be simple. I don't mind buying a different router or re-flashing an old linksys, but after it is set up, I want it to be as simple as possible.</p><p>From what I read using a hub would drop packets and the wificard in another laptop would only pick out one user at a time plus the added bulk. I like simple lightweight things, what would do the job properly?</p></div><div id="comment-1222-info" class="comment-info"><span class="comment-age">(03 Dec '10, 01:29)</span> <span class="comment-user userinfo">neilk</span></div></div></div><div id="comment-tools-1214" class="comment-tools"></div><div class="clear"></div><div id="comment-1214-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1849"></span>

<div id="answer-container-1849" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1849-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1849-score" class="post-score" title="current number of votes">0</div><span id="post-1849-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>to sniff your router i have another way ... like buy a usb-wifi that knows AP mode and simulate a wifi router ( use the same name , channel etc like your normal wifi router ) after, u<code>ll have a new "virtual " network connection that u can sniff ( colasoft , search on google , it</code>s totaly free and very good prog ). You can see all the activity on your "wifi" . I like the OpenWRT ideea but it<code>s for advanced users, if someone didn</code>t see a linux console in his life it will be kindda complicated. this colasoft is better than whireshark, it has some filtering by default that can capture yahoo/im/etc converseations in text mode no decrytping packets and other complicated things. i hope i helped u.</p><p>p.s. the cost of the usb-wifi card is like 20-30 $ the software is free + time ( like 1h max ) i say is affordable :)</p><p>cya later alligator.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '11, 06:28</strong></p><img src="https://secure.gravatar.com/avatar/fe97f563f86d3faed2c52c5d8d73f462?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="colapsys&#39;s gravatar image" /><p><span>colapsys</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="colapsys has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Jan '11, 06:29</strong> </span></p></div></div><div id="comments-container-1849" class="comments-container"></div><div id="comment-tools-1849" class="comment-tools"></div><div class="clear"></div><div id="comment-1849-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6628"></span>

<div id="answer-container-6628" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6628-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6628-score" class="post-score" title="current number of votes">0</div><span id="post-6628-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is a much easier way. Although the thread is old I offer this in case anyone else is searching. Buy a router that is compatible with Gargoyle (http://www.gargoyle-router.com/). In my case I am using a Netgear WNDR3700v2. It works really well because you can install Gargoyle firmware right from the router's browser interface. Download the appropriate file from Gargoyle. In this case, gargoyle_1.4.2-ar71xx-wndr3700v2-squashfs-factory-NA.img (If you are in North America, otherwise use the other .img file.) Then open your browser and type in 192.168.1.1 to open your router's interface. Write down all your current browser settings (Isp, subnet mask, gateway, dns servers etc). You may have to manually reenter them in your upgraded browser. Then click on update software. You will have the option to choose a file. Choose the file you downloaded from Gargoyle. Click Install. The process will take less than three minutes and you will have a router with a MUCH faster interface that can log everything that goes through your router. You will be able to monitor everyone's activity or just the ones you select. It will record either IP addresses or domain names and will download them to a spreadsheet if you prefer. In addition, you will also be able to LOCK all users to the DNS server you prefer (in my case opendns). Then you can set different schedules for different users. It is the perfect tool for parents trying to monitor and/or control what their kids are doing online. Very nice GUI--not too much technical skill should be required.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '11, 12:35</strong></p><img src="https://secure.gravatar.com/avatar/d5feba12c457d9420829fdb55d5ac59a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="glnagrom&#39;s gravatar image" /><p><span>glnagrom</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="glnagrom has no accepted answers">0%</span></p></div></div><div id="comments-container-6628" class="comments-container"></div><div id="comment-tools-6628" class="comment-tools"></div><div class="clear"></div><div id="comment-6628-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="36930"></span>

<div id="answer-container-36930" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36930-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36930-score" class="post-score" title="current number of votes">0</div><span id="post-36930-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This worked for me. <a href="http://thatexplainsalot.com/blog/2010/11/use-wireshark-and-dd-wrt-router-firmware-to-imitate-port-monitoring-on-a-router-switch-port/">http://thatexplainsalot.com/blog/2010/11/use-wireshark-and-dd-wrt-router-firmware-to-imitate-port-monitoring-on-a-router-switch-port/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '14, 10:51</strong></p><img src="https://secure.gravatar.com/avatar/6efd135bf263ae3433d68b3d273d9506?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yardjockey&#39;s gravatar image" /><p><span>yardjockey</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yardjockey has no accepted answers">0%</span></p></div></div><div id="comments-container-36930" class="comments-container"></div><div id="comment-tools-36930" class="comment-tools"></div><div class="clear"></div><div id="comment-36930-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

