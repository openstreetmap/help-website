+++
type = "question"
title = "capture on vpn tunnel nic"
description = '''hi all, In my company we have some sort of pre-configured labs that can be deployed within minutes for learning / testing purposes. I&#x27;m in the need to simulate a scenario where a client will connect to corporate network via VPN. I&#x27;ve deployed the lab consisting of two domains each running Exchange. ...'''
date = "2015-12-15T12:32:00Z"
lastmod = "2015-12-17T04:19:00Z"
weight = 48544
keywords = [ "vpn", "tap", "tun" ]
aliases = [ "/questions/48544" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [capture on vpn tunnel nic](/questions/48544/capture-on-vpn-tunnel-nic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48544-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48544-score" class="post-score" title="current number of votes">0</div><span id="post-48544-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi all,</p><p>In my company we have some sort of pre-configured labs that can be deployed within minutes for learning / testing purposes. I'm in the need to simulate a scenario where a client will connect to corporate network via VPN. I've deployed the lab consisting of two domains each running Exchange. I've selected on of the machines and installed openvpn and coofiguered it. each of this machines has an internal IP from 192.x.x.x range and an "external" ip 10.x.x.x. on my laptop istalled vmware workstation with an Windows OS and configured openvpn accordingly. the server running openvpn is getting an ip of 10.8.0.1 and the client (inside vmware workstation) 10.8.0.6 i can ping both ip i can access the admin share on both hosts. What i don't uderstand why i cannot select the nic on the client that is created as part of openvpn i can only see my LAN NIC and when i did a trace it establishes the connectio from it;s ip to th;e servers external ip . . . how would i be able to join the domain when they only talk over 10.8.x.x but i cannot ping the "internal" ip of the server ?</p><p>probably this does make sense but let's try :/</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-vpn" rel="tag" title="see questions tagged &#39;vpn&#39;">vpn</span> <span class="post-tag tag-link-tap" rel="tag" title="see questions tagged &#39;tap&#39;">tap</span> <span class="post-tag tag-link-tun" rel="tag" title="see questions tagged &#39;tun&#39;">tun</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Dec '15, 12:32</strong></p><img src="https://secure.gravatar.com/avatar/2b3f26f3a24449776af62dd8cca7715a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adasko&#39;s gravatar image" /><p><span>adasko</span><br />
<span class="score" title="86 reputation points">86</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adasko has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Dec '15, 05:35</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-48544" class="comments-container"><span id="48562"></span><div id="comment-48562" class="comment"><div id="post-48562-score" class="comment-score"></div><div class="comment-text"><p>Sorry, this isn't a Wireshark question.</p></div><div id="comment-48562-info" class="comment-info"><span class="comment-age">(16 Dec '15, 03:58)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="48569"></span><div id="comment-48569" class="comment"><div id="post-48569-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span>, I think it is a Wireshark question, as the actual question hidden in the noise is "why I cannot capture at TUN (or TAP) virtual interface because Wireshark doesn't even show it in the interface list". If you say "not a Wireshark question" because it is actually a WinPcap question, you're definitely right formally, but for most users Wireshark on Windows includes WinPcap.</p><p>I was hesitant to answer "it is because the TUN/TAP driver does not provide an API to which WinPcap could hook" because I am not sure it is true, but nevertheless I think it is not an off-topic question.</p></div><div id="comment-48569-info" class="comment-info"><span class="comment-age">(16 Dec '15, 05:02)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="48570"></span><div id="comment-48570" class="comment"><div id="post-48570-score" class="comment-score"></div><div class="comment-text"><p><span>@sindy</span>,</p><p>Poor reading on my part. I've reopened it.</p></div><div id="comment-48570-info" class="comment-info"><span class="comment-age">(16 Dec '15, 05:34)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-48544" class="comment-tools"></div><div class="clear"></div><div id="comment-48544-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48571"></span>

<div id="answer-container-48571" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48571-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48571-score" class="post-score" title="current number of votes">0</div><span id="post-48571-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As per the comment from <span>@sindy</span>, it's likely because WinPCap doesn't see the TAP adaptor created by OpenVPN.</p><p>Can you see the adaptor listed in the output of <code>tshark -D</code>?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Dec '15, 05:51</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-48571" class="comments-container"><span id="48603"></span><div id="comment-48603" class="comment"><div id="post-48603-score" class="comment-score"></div><div class="comment-text"><p>hi guys,</p><p>i can see only my LAN NIC <img src="https://osqa-ask.wireshark.org/upfiles/tshark.jpg" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/2nic.jpg" alt="alt text" /></p><p>BR</p><p>Adam</p></div><div id="comment-48603-info" class="comment-info"><span class="comment-age">(17 Dec '15, 02:21)</span> <span class="comment-user userinfo">adasko</span></div></div><span id="48606"></span><div id="comment-48606" class="comment"><div id="post-48606-score" class="comment-score"></div><div class="comment-text"><p>Ok, so your version of WinPCap doesn't see that adaptor. On Win 8.1, I have the same tap adaptor for an SSL VPN in the exact same state as your adaptor, and WinPCap can see it.</p><p>What's your OS, and WinPCap version? The WinPCap version can be seen in the Help -&gt; About dialog of Wireshark (in the running on ... bit).</p></div><div id="comment-48606-info" class="comment-info"><span class="comment-age">(17 Dec '15, 03:08)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="48609"></span><div id="comment-48609" class="comment"><div id="post-48609-score" class="comment-score"></div><div class="comment-text"><p>OS is W2K8 R2 Enterprise SP1 WinPcap version 4.1.3 (packet .dll Version 4.1.0.2980)</p><p>But I'm able to see the the adaptor when running same Wiershark version on Windows 7 Enterprise SP1 host ...</p><p><img src="https://osqa-ask.wireshark.org/upfiles/tap.jpg" alt="alt text" /></p></div><div id="comment-48609-info" class="comment-info"><span class="comment-age">(17 Dec '15, 04:10)</span> <span class="comment-user userinfo">adasko</span></div></div><span id="48610"></span><div id="comment-48610" class="comment"><div id="post-48610-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately I'm out of ideas why WinPcap on your Server 2K8 can't see the NIC, whereas the two client OS's discussed can.</p></div><div id="comment-48610-info" class="comment-info"><span class="comment-age">(17 Dec '15, 04:19)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-48571" class="comment-tools"></div><div class="clear"></div><div id="comment-48571-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

