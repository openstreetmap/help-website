+++
type = "question"
title = "Ping test with high MS"
description = '''I have a porblem with my network. Whenever i ping from my computer to my router i get a 500 ms response time every minute or so. I uploaded the capture here: https://www.cloudshark.org/captures/8d99cc1d17e5 What could be wrong? My other PC has no such problem and when i use my external WLAN adapter ...'''
date = "2016-06-30T05:23:00Z"
lastmod = "2016-07-01T09:15:00Z"
weight = 53748
keywords = [ "capture", "spikes", "ping" ]
aliases = [ "/questions/53748" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Ping test with high MS](/questions/53748/ping-test-with-high-ms)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53748-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53748-score" class="post-score" title="current number of votes">0</div><span id="post-53748-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a porblem with my network. Whenever i ping from my computer to my router i get a 500 ms response time every minute or so. I uploaded the capture here: <a href="https://www.cloudshark.org/captures/8d99cc1d17e5">https://www.cloudshark.org/captures/8d99cc1d17e5</a></p><p>What could be wrong? My other PC has no such problem and when i use my external WLAN adapter and use my wifi the ping still spikes once a minute.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-spikes" rel="tag" title="see questions tagged &#39;spikes&#39;">spikes</span> <span class="post-tag tag-link-ping" rel="tag" title="see questions tagged &#39;ping&#39;">ping</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jun '16, 05:23</strong></p><img src="https://secure.gravatar.com/avatar/2c755775fdc4c94417715eff00531fe5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alexxjr&#39;s gravatar image" /><p><span>Alexxjr</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alexxjr has no accepted answers">0%</span></p></div></div><div id="comments-container-53748" class="comments-container"></div><div id="comment-tools-53748" class="comment-tools"></div><div class="clear"></div><div id="comment-53748-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53766"></span>

<div id="answer-container-53766" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53766-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53766-score" class="post-score" title="current number of votes">2</div><span id="post-53766-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It appears that each time the pings are (very) slow your computer had (just prior to the ping request) broadcast an SSDP M-SEARCH. It appears to take the router about 2 seconds to process and reply to this message and during that time it isn't replying to the ICMP.</p><p>This pattern wasn't too hard to find:</p><ol><li>Use a filter of <code>icmp.resptime &gt; 10</code></li><li>Select the first ICMP reply you see</li><li>Clear the filter and look what happened between (and a little before) the ICMP request and reply</li><li>Repeat for several other instances of the slow replies to see if the same thing happens each time</li></ol><p>Here's an example:</p><pre><code>No.     Time           Source                Destination           Protocol Length Info
    999 151.233509     192.168.0.12          239.255.255.250       SSDP     136    M-SEARCH * HTTP/1.1 
   1000 151.327558     192.168.0.12          192.168.0.1           ICMP     74     Echo (ping) request  id=0x0001, seq=1984/49159, ttl=128 (reply in 1017)
   1001 151.872915     192.168.0.12          40.113.87.220         TCP      66     50801 → 443 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 WS=256 SACK_PERM=1
   1002 151.872915     192.168.0.12          40.113.87.220         TCP      66     50800 → 443 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 WS=256 SACK_PERM=1
   1003 152.010902     192.168.0.12          192.168.0.255         UDP      305    54915 → 54915  Len=263
   1004 152.928330     173.112.255.173 192.168.0.12          TLSv1    107    Application Data
   1005 152.978607     192.168.0.12          173.112.255.173 TCP      54     50599 → 443 [ACK] Seq=1 Ack=319 Win=259 Len=0
   1006 153.013169     192.168.0.12          192.168.0.255         UDP      305    54915 → 54915  Len=263
   1007 153.234173     192.168.0.1           192.168.0.12          SSDP     284    HTTP/1.1 200 OK 
   1008 153.234270     192.168.0.1           192.168.0.12          SSDP     300    HTTP/1.1 200 OK 
   1009 153.234448     192.168.0.1           192.168.0.12          SSDP     296    HTTP/1.1 200 OK 
   1010 153.234532     192.168.0.1           192.168.0.12          SSDP     276    HTTP/1.1 200 OK 
   1011 153.234688     192.168.0.1           192.168.0.12          SSDP     356    HTTP/1.1 200 OK 
   1012 153.234806     192.168.0.1           192.168.0.12          SSDP     320    HTTP/1.1 200 OK 
   1013 153.234881     192.168.0.1           192.168.0.12          SSDP     350    HTTP/1.1 200 OK 
   1014 153.235066     192.168.0.1           192.168.0.12          SSDP     348    HTTP/1.1 200 OK 
   1015 153.235141     192.168.0.1           192.168.0.12          SSDP     352    HTTP/1.1 200 OK 
   1016 153.235325     192.168.0.1           192.168.0.12          SSDP     344    HTTP/1.1 200 OK 
   1017 153.239442     192.168.0.1           192.168.0.12          ICMP     74     Echo (ping) reply    id=0x0001, seq=1984/49159, ttl=64 (request in 1000)</code></pre><p>I can't say why that's happening (is the router really handling ICMPs at the same level as SSDP?) but it appears to be the cause.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '16, 06:42</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Jul '16, 06:43</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-53766" class="comments-container"><span id="53775"></span><div id="comment-53775" class="comment"><div id="post-53775-score" class="comment-score"></div><div class="comment-text"><p>Reinstalled my operating system and the problem dissappeared. Thanks for the analysis</p></div><div id="comment-53775-info" class="comment-info"><span class="comment-age">(01 Jul '16, 09:15)</span> <span class="comment-user userinfo">Alexxjr</span></div></div></div><div id="comment-tools-53766" class="comment-tools"></div><div class="clear"></div><div id="comment-53766-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

