+++
type = "question"
title = "Is my bandwidth being hogged? What is wrong? Please help."
description = '''Hello! I did a speed test which revealed that my particular device, at least, was getting 17 Mb/s download and ~30 Mb/s upload when the ISP is supposedly delivering 50/50. The other devices are not being currently used (at least by people) other than this computer right now. I looked on the IPv4 end...'''
date = "2017-06-17T08:01:00Z"
lastmod = "2017-06-17T09:35:00Z"
weight = 62072
keywords = [ "wireless", "bandwidth", "endpoints", "ipv4", "wireshark" ]
aliases = [ "/questions/62072" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Is my bandwidth being hogged? What is wrong? Please help.](/questions/62072/is-my-bandwidth-being-hogged-what-is-wrong-please-help)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62072-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello! I did a speed test which revealed that my particular device, at least, was getting 17 Mb/s download and ~30 Mb/s upload when the ISP is supposedly delivering 50/50. The other devices are not being currently used (at least by people) other than this computer right now. I looked on the IPv4 endpoints and I see a lot of IPs that a) are not on my router device list and b) do not follow the numbering schema of my router. While I am a fair hand around computers, I am new to the networking scene. (Lets say I have an introductory level understanding). Are these other IP's in the endpoints bandwidth hogs or some kind of invisible service? Is my ISP just not putting out what it should be?</p><p>Thanks.</p><p>Image is hosted here as the embed does not seem to work: <a href="http://imgur.com/a/pEFqM">http://imgur.com/a/pEFqM</a></p><p>Alternate: <a href="https://ibb.co/crzDhk">https://ibb.co/crzDhk</a></p><p>It is a comparison of my router device list with the IPv4 tab of the Wireshark Enpoints menu, sorted by Byte traffic.</p></div><div id="question-tags" class="tags-container tags">wireless bandwidth endpoints ipv4 wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jun '17, 08:01</strong></p><img src="https://secure.gravatar.com/avatar/2efb76be87a506d2ec6692e1d1b00f37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rye_Bread&#39;s gravatar image" /><p>Rye_Bread<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rye_Bread has no accepted answers">0%</span></p></div></div><div id="comments-container-62072" class="comments-container"><span id="62074"></span><div id="comment-62074" class="comment"><div id="post-62074-score" class="comment-score">1</div><div class="comment-text"><p>If you're wondering about the 'other IP addresses' you should start looking into IP addressing basics. IP address wise there's nothing out of the ordinary here.</p></div><div id="comment-62074-info" class="comment-info"><span class="comment-age">(17 Jun '17, 09:36)</span> Jaap ♦</div></div></div><div id="comment-tools-62072" class="comment-tools"></div><div class="clear"></div><div id="comment-62072-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62073"></span>

<div id="answer-container-62073" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-62073-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The IP addresses you've marked in the screen shot are normal 'special purpose' addresses:</p><ul><li>239.X.X.X and 224.X.X.X are multicast addresses (s. <a href="https://en.wikipedia.org/wiki/IP_multicast)">https://en.wikipedia.org/wiki/IP_multicast)</a></li><li>192.168.1.255 and 255.255.255.255 are broadcast addresses (s. <a href="https://en.wikipedia.org/wiki/Broadcast_address;">https://en.wikipedia.org/wiki/Broadcast_address;</a> assuming your netmask is 255.255.255.0)</li><li>169.254.X.X are link local addresses (s. <a href="https://en.wikipedia.org/wiki/Link-local_address);">https://en.wikipedia.org/wiki/Link-local_address);</a> also called APIPA</li></ul><p>Regarding the bandwidth: There are a lot of influencing factors which can affect the bandwidth (e.g. latency, window size, IPS peerings etc.). =&gt; Therefore more data is needed to make a point.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '17, 09:35</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p>Uli<br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-62073" class="comments-container"><span id="62077"></span><div id="comment-62077" class="comment"><div id="post-62077-score" class="comment-score"></div><div class="comment-text"><p>Ah, thanks. Latency is 10 ms. All windows (On this device) are generally 1920x1080 (native resoultion). I don't have a lot of tabs open that would chew up bandwidth either.</p><p>As for the IPS peerings I am not sure. I have fiber optics directly from Verizon and I haven't been able to dig up any information on how to view it it, or locate any information on if I can do this with wireshark itself.</p><p>So, I may be right in assuming the ISP is throttling us?</p></div><div id="comment-62077-info" class="comment-info"><span class="comment-age">(17 Jun '17, 10:47)</span> Rye_Bread</div></div><span id="62081"></span><div id="comment-62081" class="comment"><div id="post-62081-score" class="comment-score">1</div><div class="comment-text"><p>window size here has nothing to do with screen resolution and thus data volume; it is a property of network transport protocol called TCP which affects effective transmission speed. Combination of small window size (roughly the size of receiving buffer) and big delay on the path between endpoints makes transmission slow even if enough bandwidth is available.</p></div><div id="comment-62081-info" class="comment-info"><span class="comment-age">(17 Jun '17, 12:44)</span> sindy</div></div></div><div id="comment-tools-62073" class="comment-tools"></div><div class="clear"></div><div id="comment-62073-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

