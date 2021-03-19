+++
type = "question"
title = "Help with spanning tree and Excessive ARP requests"
description = '''Hi, I am a new to wireshark and have trying to help my uncle with his internet troubles. I have seen Excessive ARP requests which I think its either the switch that cant find the mac address or the printers are auto searching. And the spanning tree im guessing there tracking cookies? not really sure...'''
date = "2014-09-02T09:47:00Z"
lastmod = "2014-09-02T11:05:00Z"
weight = 35932
keywords = [ "arp", "spanningtree", "excessive" ]
aliases = [ "/questions/35932" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Help with spanning tree and Excessive ARP requests](/questions/35932/help-with-spanning-tree-and-excessive-arp-requests)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35932-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am a new to wireshark and have trying to help my uncle with his internet troubles. I have seen Excessive ARP requests which I think its either the switch that cant find the mac address or the printers are auto searching. And the spanning tree im guessing there tracking cookies? not really sure. I would be really grateful if anyone could help me with this problem. I uploaded the test documented.</p><p><a href="https://app.box.com/s/r426ixoncpfoyz28t0cv">https://app.box.com/s/r426ixoncpfoyz28t0cv</a></p><p>Thank you</p></div><div id="question-tags" class="tags-container tags">arp spanningtree excessive</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Sep '14, 09:47</strong></p><img src="https://secure.gravatar.com/avatar/dd2630227be6d715406847ade75c3d27?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="killmasta93&#39;s gravatar image" /><p>killmasta93<br />
<span class="score" title="-1 reputation points">-1</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="killmasta93 has no accepted answers">0%</span></p></div></div><div id="comments-container-35932" class="comments-container"></div><div id="comment-tools-35932" class="comment-tools"></div><div class="clear"></div><div id="comment-35932-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35934"></span>

<div id="answer-container-35934" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35934-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Spanning tree looks fine to me, no topology change and BPDUs in normal quantities and timings. BTW Spanning tree has nothing to do with cookies - STP is a layer 2 protocol, while cookies are usually at layers above 4.</p><p>You've got about 13% ARP in the trace, which is not really good, but not critical either unless it takes away bandwith (which peaks at 2.5MBit/s in your case, so it really doesn't). What you can do is take some of the ARP requests, e.g. when 192.168.1.254 asks for the MAC of 192.168.1.5 (which happens a lot) and find out if that IP exists at all and if the request is answered. For that you need to capture the port of at least one of the hosts that hold those IP addresses.</p><p>What exactly is the "internet trouble" of your uncle? A more specific problem description would be helpful.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Sep '14, 11:05</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-35934" class="comments-container"><span id="35942"></span><div id="comment-35942" class="comment"><div id="post-35942-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper, Thank you so much for helping me out i really appreciate it. Around last week my uncle changed internet provider to get fiber optics to 20MBit/s download and upload. Since then many workers have complained that accessing a internet page would take forever. So today I thought of flushing the DNS and renewing the ip, which it did the trick. My other question would it be beneficial if i added static ip to the desktop computers? And would you recommend changing the DNS to the OPENDNS settings? And for some of the ARP requests once i found the port should i set it static within the switch? Also what was very odd but not sure if it has to do with the network i found adware webwise tracking cookies which my antivirus caught once i connected though LAN. The cookies were @doubleclick.net,@msnportal.112.207.net, and @orphancleanup. I found those many times in other computers when I started to clean the computers. I checked though google but did not really get a concrete answer if it was the network.</p><p>Thank you again for everything</p></div><div id="comment-35942-info" class="comment-info"><span class="comment-age">(02 Sep '14, 18:30)</span> killmasta93</div></div><span id="35947"></span><div id="comment-35947" class="comment"><div id="post-35947-score" class="comment-score"></div><div class="comment-text"><p>Static IPs for desktops have advantages and drawbacks. Advantage is that it is easier to identify which desktop an IP address belongs to, but the disadvantage is that it takes more administrative work to assign and maintain them (which is why desktops usually use DHCP)</p><p>You can use OpenDNS if you want, but usually the DNS of the internet provider is the best option because response times are faster than something further away.</p><p>You should not map static ARP anywhere, because if something moves from one port to the other it'll be hell to troubleshoot. So any static ARP stuff should only happen in really high security environments where changes don't happen often and are well tracked.</p><p>Adware cookies are everywhere - if you don't want them, use a cookie manager or tell your browser to forget them when you close it.</p></div><div id="comment-35947-info" class="comment-info"><span class="comment-age">(03 Sep '14, 01:49)</span> Jasper ♦♦</div></div><span id="36044"></span><div id="comment-36044" class="comment"><div id="post-36044-score" class="comment-score"></div><div class="comment-text"><p>Hi, Thank you again for helping me to understand.</p></div><div id="comment-36044-info" class="comment-info"><span class="comment-age">(06 Sep '14, 11:49)</span> killmasta93</div></div></div><div id="comment-tools-35934" class="comment-tools"></div><div class="clear"></div><div id="comment-35934-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

