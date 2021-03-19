+++
type = "question"
title = "[closed] DNS / two NIC&#x27;s"
description = '''hi guys, first of all, I&#x27;m not sure whether this is the right place to ask but let my ask the question anyway. i use VMware ESXi host to build my lab. in vSphere i&#x27;ve created two separate networks 10.0.0.0/8 192.168.0.0 /24 both are internal networks without internet access. between both i have a Vy...'''
date = "2015-04-18T09:08:00Z"
lastmod = "2015-04-18T09:08:00Z"
weight = 41555
keywords = [ "dns" ]
aliases = [ "/questions/41555" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] DNS / two NIC's](/questions/41555/dns-two-nics)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41555-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi guys,</p><p>first of all, I'm not sure whether this is the right place to ask but let my ask the question anyway. i use VMware ESXi host to build my lab. in vSphere i've created two separate networks 10.0.0.0/8 192.168.0.0 /24 both are internal networks without internet access. between both i have a VyOs VM as a virtual router to connect both networks. in each site i have a DC and Exchange - mail between both domains working just fine. when i add on any of those VM's a second NIC (internet facing ) mails are not getting delivered. i'm not even ping the other domain at this time. i think that as soon the second NIC is up each single DNS query is processed by the DNS server obtained by DHCP. now when i do route print inside the VM i see two route entries pointing to the default route 0.0.0.0 , one pointing to the "internet" NIC with a metric of 50 and the other pointing to the "internal"interface with a metric of 266. i know that my Exchange is not configure to receive / send mails to the outside world because of missing MX etc. but just to have it still working internally while the "internet" NIC is also up would it be enough to change the metric the other way around ?</p><p>thank you very much !</p><p>regards</p><p>ADam</p></div><div id="question-tags" class="tags-container tags">dns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '15, 09:08</strong></p><img src="https://secure.gravatar.com/avatar/2b3f26f3a24449776af62dd8cca7715a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adasko&#39;s gravatar image" /><p>adasko<br />
<span class="score" title="86 reputation points">86</span><span title="34 badges"><span class="badge1">●</span><span class="badgecount">34</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adasko has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>closed 18 Apr '15, 12:15</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-41555" class="comments-container"><span id="41556"></span><div id="comment-41556" class="comment"><div id="post-41556-score" class="comment-score"></div><div class="comment-text"><p>but even if i do so i would probably loss internet connectivity ...<br />
</p></div><div id="comment-41556-info" class="comment-info"><span class="comment-age">(18 Apr '15, 09:09)</span> adasko</div></div><span id="41562"></span><div id="comment-41562" class="comment"><div id="post-41562-score" class="comment-score"></div><div class="comment-text"><p>ok i got it solved :)</p><p>regards</p><p>Adam</p></div><div id="comment-41562-info" class="comment-info"><span class="comment-age">(18 Apr '15, 11:02)</span> adasko</div></div></div><div id="comment-tools-41555" class="comment-tools"></div><div class="clear"></div><div id="comment-41555-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Question is off-topic or not relevant" by grahamb 18 Apr '15, 12:15

</div>

</div>

</div>

