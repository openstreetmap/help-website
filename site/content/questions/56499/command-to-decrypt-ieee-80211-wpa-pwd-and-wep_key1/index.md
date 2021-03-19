+++
type = "question"
title = "command to decrypt IEEE 80211 wpa-pwd and wep_key1"
description = '''Hi, Please help me to decrypt IEEE 80211 wpa-pwd using command prompt. I am using the below command but it is not enabling decrypt option and not adding keys. tshark -nr snifferFile.pcapng -o wlan.enable_decryption:TRUE -o &quot;uat:80211_keys:&#92;&quot;wpa-pwd&#92;&quot;,&#92;&quot;123456789:e1vcc_BANQSPRPC01_Ssid24&#92;&quot;&quot; -w sniffe...'''
date = "2016-10-19T00:31:00Z"
lastmod = "2016-10-19T03:01:00Z"
weight = 56499
keywords = [ "ieeedecryption" ]
aliases = [ "/questions/56499" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [command to decrypt IEEE 80211 wpa-pwd and wep\_key1](/questions/56499/command-to-decrypt-ieee-80211-wpa-pwd-and-wep_key1)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56499-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Please help me to decrypt IEEE 80211 wpa-pwd using command prompt. I am using the below command but it is not enabling decrypt option and not adding keys.</p><p>tshark -nr snifferFile.pcapng -o wlan.enable_decryption:TRUE -o "uat:80211_keys:\"wpa-pwd\",\"123456789:e1vcc_BANQSPRPC01_Ssid24\"" -w snifferFile_decryptFile.pcapng</p><p>Wireshark and tshark version used is 1.10.3. Even the same command is not working in Linux Ubuntu 14.04 as well. Please help.</p></div><div id="question-tags" class="tags-container tags">ieeedecryption</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '16, 00:31</strong></p><img src="https://secure.gravatar.com/avatar/d011d9c0d1f8ed56e0bf62dd8d6936c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KBKrishnan&#39;s gravatar image" /><p>KBKrishnan<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KBKrishnan has no accepted answers">0%</span></p></div></div><div id="comments-container-56499" class="comments-container"></div><div id="comment-tools-56499" class="comment-tools"></div><div class="clear"></div><div id="comment-56499-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56503"></span>

<div id="answer-container-56503" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56503-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I can't help with the tshark command, but when I need to decrypt wireless traffic from CLI I use this tool:</p><p><a href="http://www.aircrack-ng.org/doku.php?id=airdecap-ng">http://www.aircrack-ng.org/doku.php?id=airdecap-ng</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '16, 03:01</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div></div><div id="comments-container-56503" class="comments-container"></div><div id="comment-tools-56503" class="comment-tools"></div><div class="clear"></div><div id="comment-56503-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

