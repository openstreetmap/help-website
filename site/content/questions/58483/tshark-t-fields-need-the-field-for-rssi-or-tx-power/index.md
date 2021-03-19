+++
type = "question"
title = "tshark -T fields (need the field for rssi or tx-power)"
description = '''Hello, I&#x27;m new with tshark and I&#x27;m trying to use tshark to see MAC addresses and their rssi or tx power, but can&#x27;t seem to find the proper field name: the command I&#x27;m using is: sudo tshark -S -l -i wlan1 -Y &#x27;wlan.fc.type_subtype eq 4&#x27; -T fields -E header=y -e frame.time -e wlan.sa -e wlan.sa_resolve...'''
date = "2017-01-03T09:48:00Z"
lastmod = "2017-01-03T10:02:00Z"
weight = 58483
keywords = [ "-t", "tshark", "fields" ]
aliases = [ "/questions/58483" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark -T fields (need the field for rssi or tx-power)](/questions/58483/tshark-t-fields-need-the-field-for-rssi-or-tx-power)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58483-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I'm new with tshark and I'm trying to use tshark to see MAC addresses and their rssi or tx power, but can't seem to find the proper field name: the command I'm using is: sudo tshark -S -l -i wlan1 -Y 'wlan.fc.type_subtype eq 4' -T fields -E header=y -e frame.time -e wlan.sa -e wlan.sa_resolved -e wlan_mgt.ssid And I get: frame.time wlan.sa wlan.sa_resolved wlan_mgt.ssid Jan 3, 2017 12:25:03.048773000 EST b8:27:eb:1a:d3:2f Raspberr_1a:d3:2f<br />
Jan 3, 2017 12:25:03.069641000 EST b8:27:eb:1a:d3:2f Raspberr_1a:d3:2f<br />
Jan 3, 2017 12:25:03.092482000 EST b8:27:eb:1a:d3:2f Raspberr_1a:d3:2f<br />
Jan 3, 2017 12:25:03.155865000 EST b8:27:eb:1a:d3:2f Raspberr_1a:d3:2f<br />
Jan 3, 2017 12:25:03.362698000 EST b8:27:eb:1a:d3:2f Raspberr_1a:d3:2f<br />
Jan 3, 2017 12:25:03.383152000 EST b8:27:eb:1a:d3:2f Raspberr_1a:d3:2f<br />
Jan 3, 2017 12:25:03.426263000 EST b8:27:eb:1a:d3:2f Raspberr_1a:d3:2f<br />
Jan 3, 2017 12:25:03.496762000 EST b8:27:eb:1a:d3:2f Raspberr_1a:d3:2f<br />
Jan 3, 2017 12:25:03.517186000 EST b8:27:eb:1a:d3:2f Raspberr_1a:d3:2f<br />
</p><p>I've tried: (with no luck) chan.chan_tx_pow wlan.dbm_antsignal wlan.antenna wlan.normrssi_antsignal wlan.rawrssi_antsignal wlan.signal_strength wlancap.dbm_antsignal wlancap.ssi_signal<br />
</p><p>Could anyone help me out?</p></div><div id="question-tags" class="tags-container tags">-t tshark fields</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jan '17, 09:48</strong></p><img src="https://secure.gravatar.com/avatar/0a19ae1162099570766548d6bb2dd589?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tonny_vivas&#39;s gravatar image" /><p>tonny_vivas<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tonny_vivas has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-58483" class="comments-container"></div><div id="comment-tools-58483" class="comment-tools"></div><div class="clear"></div><div id="comment-58483-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58484"></span>

<div id="answer-container-58484" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58484-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you don't know the name of a filter, you can try searching for it on Wireshark's online <a href="https://www.wireshark.org/docs/dfref/"><strong>Display Filter Reference</strong></a> page or perusing the Wireshark <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChWorkFilterAddExpressionSection.html">Filter Expression dialog</a> for fields of interest.</p><p>Another tip is to open the capture file in Wireshark and find a packet that contains the field of interest. When you select it, Wireshark will display the field name in the status bar for you.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jan '17, 10:02</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Jan '17, 10:04</p></div></div><div id="comments-container-58484" class="comments-container"></div><div id="comment-tools-58484" class="comment-tools"></div><div class="clear"></div><div id="comment-58484-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

