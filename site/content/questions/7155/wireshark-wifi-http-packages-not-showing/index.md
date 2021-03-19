+++
type = "question"
title = "Wireshark wifi http packages not showing"
description = '''Hey guys. So I have for some time tried to get this working, and I feel like im close but just not there yet.  I&#x27;m using a broadcom wifi card... When I activate airmon-ng it creates a device called mon0. If I listen on the traffic using the wan0 (normal wifi) I get only very few packages and only ht...'''
date = "2011-10-30T05:38:00Z"
lastmod = "2011-10-30T05:51:00Z"
weight = 7155
keywords = [ "wifi", "broadcom", "wireshark" ]
aliases = [ "/questions/7155" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark wifi http packages not showing](/questions/7155/wireshark-wifi-http-packages-not-showing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7155-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey guys.</p><p>So I have for some time tried to get this working, and I feel like im close but just not there yet. I'm using a broadcom wifi card... When I activate airmon-ng it creates a device called mon0.</p><p>If I listen on the traffic using the wan0 (normal wifi) I get only very few packages and only http when I use the machine that is listening to browse some site... not from any other machine on the wifi network. When I switch to the mon0 device I suddenly get a lot more traffic. I see a lot of beacons from wifi networks all around me... here I thought I was home free... but I only see these broadcasts... no http etc. what so ever... only what seems to be the broadcast id's from the routeres near me...</p><p>Any ideas??</p></div><div id="question-tags" class="tags-container tags">wifi broadcom wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Oct '11, 05:38</strong></p><img src="https://secure.gravatar.com/avatar/24310b2487a9974340625edf3c3b2cf9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ronnie%20Jespersen&#39;s gravatar image" /><p>Ronnie Jespe...<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ronnie Jespersen has no accepted answers">0%</span></p></div></div><div id="comments-container-7155" class="comments-container"></div><div id="comment-tools-7155" class="comment-tools"></div><div class="clear"></div><div id="comment-7155-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7156"></span>

<div id="answer-container-7156" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7156-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Maybe you're just listening on the wrong channel, and on that channel only exist access points without active users, so you only see their "lonely" management traffic. Try listening to the other channels by adjusting your WiFi device with airmon-ng and you should find what you're looking for.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Oct '11, 05:51</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-7156" class="comments-container"><span id="7158"></span><div id="comment-7158" class="comment"><div id="post-7158-score" class="comment-score"></div><div class="comment-text"><p>That didn't help im afraid... I did sudo airmon-ng start wan0 6 And my router is using channel 6...</p><p>This is what I am being spammed with:</p><p>536 21.368621 Z-Com_75:90:c2 Broadcast 802.11 320 Beacon frame, SN=3351, FN=0, Flags=........, BI=100, SSID=TDC-7318</p><p>And then with a lot of different SSID's</p></div><div id="comment-7158-info" class="comment-info"><span class="comment-age">(30 Oct '11, 06:17)</span> Ronnie Jespe...</div></div><span id="7160"></span><div id="comment-7160" class="comment"><div id="post-7160-score" class="comment-score"></div><div class="comment-text"><p>Okay I know now that its not listening on channel 6... when I look at the channel it says -1 ?? Event though I start airmon-ng with channel...</p></div><div id="comment-7160-info" class="comment-info"><span class="comment-age">(30 Oct '11, 13:00)</span> Ronnie Jespe...</div></div></div><div id="comment-tools-7156" class="comment-tools"></div><div class="clear"></div><div id="comment-7156-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

