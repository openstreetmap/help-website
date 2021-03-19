+++
type = "question"
title = "packets missing using pcap_open_live and also in wireshark"
description = '''I have to capture a data from FPGA Board which sends totally 15000 frames. Each frame consists of 514 bytes and each frame they are sending at a rate of 4usec. In my application I used pcap_open_live(devicename, 65536, 1, 1000, errbuf) and added filters to capture the data. I can able to receive aro...'''
date = "2014-09-25T00:22:00Z"
lastmod = "2014-09-25T00:27:00Z"
weight = 36581
keywords = [ "wireshark", "packets", "pcap_open_live", "missing" ]
aliases = [ "/questions/36581" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [packets missing using pcap\_open\_live and also in wireshark](/questions/36581/packets-missing-using-pcap_open_live-and-also-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36581-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have to capture a data from FPGA Board which sends totally 15000 frames. Each frame consists of 514 bytes and each frame they are sending at a rate of 4usec. In my application I used pcap_open_live(devicename, 65536, 1, 1000, errbuf) and added filters to capture the data. I can able to receive around 12500 packets only in my application. And also I checked in wire shark there also I can able to receive 13000 packets. The above one I tried in windows. In linux I used tcpdump, there I can receive all the packets correctly. Kindly suggest me why im missing the packets(windows)?</p></div><div id="question-tags" class="tags-container tags">wireshark packets pcap_open_live missing</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '14, 00:22</strong></p><img src="https://secure.gravatar.com/avatar/4cbb1f65ba1a6ff95e49802e0a31d131?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="paulraj85&#39;s gravatar image" /><p>paulraj85<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="paulraj85 has no accepted answers">0%</span></p></div></div><div id="comments-container-36581" class="comments-container"></div><div id="comment-tools-36581" class="comment-tools"></div><div class="clear"></div><div id="comment-36581-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36583"></span>

<div id="answer-container-36583" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36583-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>My guess is you're capturing with a normal PC and a normal NIC. You're lucky to capture as much as you do with that kind of timings - 4 µsec sending rate is too fast in most cases, and you'd loose tons of packets if you'd go for larger frame sizes I guess.</p><p>If you need to capture all packets you'll probably have to get a specialized capture card to be able to avoid drops (e.g. Napatech, Fiberblaze) - but that's gonna be expensive, and they don't see to market their cards towards single users, only capture system builders. You could also take a look at TurboCAP by Riverbed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '14, 00:27</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-36583" class="comments-container"><span id="36584"></span><div id="comment-36584" class="comment"><div id="post-36584-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jasper, But in Linux I can able to capture all data using tcpdump with this speed any reason?</p></div><div id="comment-36584-info" class="comment-info"><span class="comment-age">(25 Sep '14, 00:42)</span> paulraj85</div></div><span id="36585"></span><div id="comment-36585" class="comment"><div id="post-36585-score" class="comment-score"></div><div class="comment-text"><p>Possibly the Linux kernel and libpcap is more efficient than windows+ WinPcap. Or your linux Bix has ma better could and faster ram.</p></div><div id="comment-36585-info" class="comment-info"><span class="comment-age">(25 Sep '14, 00:50)</span> Anders ♦</div></div></div><div id="comment-tools-36583" class="comment-tools"></div><div class="clear"></div><div id="comment-36583-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

