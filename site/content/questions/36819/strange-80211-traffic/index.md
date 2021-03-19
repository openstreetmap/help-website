+++
type = "question"
title = "Strange 802.11 traffic"
description = '''Hey guys! I&#x27;m no expert in Wireshark or 802.11. But we have here a situation. Our Core (Catalyst 4507) is having high cpu all day. Cisco TAC says that some traffic with mac address 00:00:00:00:00:00 is hitting it&#x27;s CPU pretty hard (80-95%) and that traffic is coming from the port where the wireless ...'''
date = "2014-10-03T07:12:00Z"
lastmod = "2014-10-03T07:12:00Z"
weight = 36819
keywords = [ "high", "802.11", "cpu" ]
aliases = [ "/questions/36819" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Strange 802.11 traffic](/questions/36819/strange-80211-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36819-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey guys!</p><p>I'm no expert in Wireshark or 802.11. But we have here a situation. Our Core (Catalyst 4507) is having high cpu all day. Cisco TAC says that some traffic with mac address 00:00:00:00:00:00 is hitting it's CPU pretty hard (80-95%) and that traffic is coming from the port where the wireless controller (Cisco WLC 5508) is connected.</p><p>I sniffed the core interface where this WLC is connected during 10 minutes. I got 321213 packets and 53% of those packets are those with mac-address 00:00:00:00:00:00. Digged a little deep and found that they were something called Probe Request.</p><p><a href="https://www.cloudshark.org/captures/ded5da4f289c">I uploaded a sample capture of those probe requests do CloudShark</a></p><p>My questions are: 1- Is this probe request normal? 2- Is this supposed to make the CPU go that high?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">high 802.11 cpu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Oct '14, 07:12</strong></p><img src="https://secure.gravatar.com/avatar/6a24e499a575770e6ba8e4c74d822420?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rafaelbn&#39;s gravatar image" /><p>rafaelbn<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rafaelbn has no accepted answers">0%</span></p></div></div><div id="comments-container-36819" class="comments-container"></div><div id="comment-tools-36819" class="comment-tools"></div><div class="clear"></div><div id="comment-36819-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

