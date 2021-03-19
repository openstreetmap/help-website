+++
type = "question"
title = "Tshark with WPA2 - Resulting Data not readable"
description = '''Hi there! I am capturing in monitor mode. I created the file 80211_keys in ~/.wireshark with content &quot;wpa-pwd&quot;,&quot;mypwd:myssid&quot;. I capture via: sudo tshark -i mon0 -w out.pcap -o wlan.enable_decryption:TRUE (I know I shouldn&#x27;t use root here, will change it as soon it works) When I import the pcap into...'''
date = "2014-03-17T20:17:00Z"
lastmod = "2014-03-17T20:17:00Z"
weight = 30908
keywords = [ "wpa2", "tshark", "monitor-mode" ]
aliases = [ "/questions/30908" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark with WPA2 - Resulting Data not readable](/questions/30908/tshark-with-wpa2-resulting-data-not-readable)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30908-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there!</p><p>I am capturing in monitor mode. I created the file <strong>80211_keys</strong> in <em>~/.wireshark</em> with content <strong>"wpa-pwd","mypwd:myssid"</strong>.</p><p>I capture via: <strong>sudo tshark -i mon0 -w out.pcap -o wlan.enable_decryption:TRUE</strong> (I know I shouldn't use root here, will change it as soon it works)</p><p>When I import the pcap into wireshark I only get entries of protocol 802.11 (Beacon Frames etc), but no eapol nor http traffic.</p><p>Do I forget a step to encrypt WPA2 or is my problem not related to WPA2 decryption?</p><p>Thanks for help!</p></div><div id="question-tags" class="tags-container tags">wpa2 tshark monitor-mode</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Mar '14, 20:17</strong></p><img src="https://secure.gravatar.com/avatar/b97f6d2d52bff3777f77d8207e9ccd88?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Motzart&#39;s gravatar image" /><p>Motzart<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Motzart has no accepted answers">0%</span></p></div></div><div id="comments-container-30908" class="comments-container"><span id="30917"></span><div id="comment-30917" class="comment"><div id="post-30917-score" class="comment-score"></div><div class="comment-text"><p>Are you seeing any data frames (as opposed to management frames such as Beacon frames)?</p></div><div id="comment-30917-info" class="comment-info"><span class="comment-age">(18 Mar '14, 01:29)</span> Guy Harris ♦♦</div></div><span id="30929"></span><div id="comment-30929" class="comment"><div id="post-30929-score" class="comment-score"></div><div class="comment-text"><p>Honestly I don't know the other type of frames. In the info section I see "QoS Data", "Acknowledgement", "Request-to-send", "Clear-to-send", "802.11 Block Ack" and "Null function(No data)". Oh and probe responses.</p></div><div id="comment-30929-info" class="comment-info"><span class="comment-age">(18 Mar '14, 05:57)</span> Motzart</div></div></div><div id="comment-tools-30908" class="comment-tools"></div><div class="clear"></div><div id="comment-30908-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

