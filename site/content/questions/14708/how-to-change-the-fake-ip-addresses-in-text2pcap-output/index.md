+++
type = "question"
title = "how to change the fake ip addresses in text2pcap output?"
description = '''Hi! I have an aplication level hex dump that I imported into wireshark successfully with text2pcap. I have what is sent and what is received, and I want to reflect that conversation in wireshark. So I created two hex dumps, one for reads and one for writes, and converted them to two pcap files, reve...'''
date = "2012-10-04T06:55:00Z"
lastmod = "2012-10-08T15:24:00Z"
weight = 14708
keywords = [ "text2pcap", "ip", "addresses", "fake" ]
aliases = [ "/questions/14708" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to change the fake ip addresses in text2pcap output?](/questions/14708/how-to-change-the-fake-ip-addresses-in-text2pcap-output)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14708-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi! I have an aplication level hex dump that I imported into wireshark successfully with text2pcap. I have what is sent and what is received, and I want to reflect that conversation in wireshark. So I created two hex dumps, one for reads and one for writes, and converted them to two pcap files, reversing the fake TCP port numbers.</p><p>But the problem I have is that text2pcap inserts 1.1.1.1 and 2.2.2.2 as origin and destination IP addresses, and I found no way to change this. I would need to reverse the IP addresses in the read hex dump import, or just use the same IP address for both origin and dest, as if the server and client are in the same machine.</p><p>Is there a way to change the fake ip addresses in text2pcap?</p><p>Thanks ! Best, Alf</p></div><div id="question-tags" class="tags-container tags">text2pcap ip addresses fake</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Oct '12, 06:55</strong></p><img src="https://secure.gravatar.com/avatar/3a67018c9712687f6a95da0887c6bd35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arpena&#39;s gravatar image" /><p>arpena<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arpena has no accepted answers">0%</span></p></div></div><div id="comments-container-14708" class="comments-container"></div><div id="comment-tools-14708" class="comment-tools"></div><div class="clear"></div><div id="comment-14708-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="14800"></span>

<div id="answer-container-14800" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14800-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You said "application-level dump", so I assume you used -u or -T to add a fake UDP orTCP header. Unfortunately, text2pcap doesn't have an option to control the assignment of fake IP addresses (and I checked the code - they're hardwired to 10.1.1.1 and 10.2.2.2), so there isn't a way to change the IP addresses it assigns.</p><p><a href="http://bittwist.sourceforge.net">Bittwist</a> might let you process the packets and rewrite the IP headers to have the same source and destination addresses.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '12, 15:24</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-14800" class="comments-container"><span id="14827"></span><div id="comment-14827" class="comment"><div id="post-14827-score" class="comment-score"></div><div class="comment-text"><p>Excellent recomendation. I was able to change the read-pcap file with this command: ./bittwiste -I database-read.pcap -O database-read-mod.pcap -T ip -s 2.2.2.2 -d 1.1.1.1</p></div><div id="comment-14827-info" class="comment-info"><span class="comment-age">(09 Oct '12, 12:04)</span> arpena</div></div></div><div id="comment-tools-14800" class="comment-tools"></div><div class="clear"></div><div id="comment-14800-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14786"></span>

<div id="answer-container-14786" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14786-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>text2pcap will add a dummy IP header (10.1.1.1 and 10.2.2.2) in these circumstances:</p><ol><li>you tell it to do so with option -i</li><li>if you add a SCTP header with option: -s/-S</li><li>if you add a UDP/TCP header with option: -u/-T</li></ol><p>So, without information how you called text2pcap, it's hard to say which of the above conditions apply.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '12, 12:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Oct '12, 12:06</p></div></div><div id="comments-container-14786" class="comments-container"></div><div id="comment-tools-14786" class="comment-tools"></div><div class="clear"></div><div id="comment-14786-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

