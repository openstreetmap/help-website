+++
type = "question"
title = "Monitor mode and packet error rate?"
description = '''Here&#x27;s my setup: 1) MacBook Pro in monitor mode with Wireshark installed. 2) A WiFi router connected to the internet 3) An iPhone, connected to the WiFi router via WPA2 I start a streaming video on the iPhone so there&#x27;s data moving to the iPhone from the WiFi router. I fire up Wireshark on the MacBo...'''
date = "2017-05-24T15:12:00Z"
lastmod = "2017-05-26T04:07:00Z"
weight = 61610
keywords = [ "packetloss", "packet", "monitor-mode", "error" ]
aliases = [ "/questions/61610" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Monitor mode and packet error rate?](/questions/61610/monitor-mode-and-packet-error-rate)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61610-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Here's my setup:</p><p>1) MacBook Pro in monitor mode with Wireshark installed. 2) A WiFi router connected to the internet 3) An iPhone, connected to the WiFi router via WPA2</p><p>I start a streaming video on the iPhone so there's data moving to the iPhone from the WiFi router.</p><p>I fire up Wireshark on the MacBook Pro.</p><p>I wrap the iPhone in aluminum foil and place it in a metal filing cabinet. I wait several seconds, take it out, unwrap the foil from the phone, wait a few seconds and then stop the Wireshark recording.</p><p>Now, what I need to do with the data is figure out how bad the signal got through the ordeal. I know while the phone was in the cabinet, it stopped communicating with the router, as there's an obvious gap in the timestamps for the packet flow. But I'd like a little bit more detail. I'd like the packet error rate as well. Can Wireshark supply this information through one of the Statistics windows and I'm just not seeing it?</p></div><div id="question-tags" class="tags-container tags">packetloss packet monitor-mode error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 May '17, 15:12</strong></p><img src="https://secure.gravatar.com/avatar/a2c66d73f30877b343f5b8a332860d06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="briank&#39;s gravatar image" /><p>briank<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="briank has no accepted answers">0%</span></p></div></div><div id="comments-container-61610" class="comments-container"></div><div id="comment-tools-61610" class="comment-tools"></div><div class="clear"></div><div id="comment-61610-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61640"></span>

<div id="answer-container-61640" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61640-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is an interesting test, and Wireshark can likely provide at least some more information. A couple of ideas:</p><p>1.</p><p>You could evaluate changes in signal strength (RSSI) as you manipulate the DuT (device under test). Have a look at the SSI signal field in the Radiotap header from the frames transmitted by the DuT. You could use a filter such as</p><pre><code>wlan.ta == (mac address of DuT)</code></pre><p>and then review the radiotap header:</p><pre><code>Radiotap Header v0, Length 20
    Header revision: 0
    Header pad: 0
    Header length: 20
    Present flags
    Flags: 0x10
    Data Rate: 12.0 Mb/s
    Channel frequency: 2412 [BG 1]
    Channel flags: 0x00c0, Orthogonal Frequency-Division Multiplexing (OFDM), 2 GHz spectrum
    **SSI Signal: -57 dBm**
    SSI Noise: -100 dBm
    Signal Quality: 75
    Antenna: 0
    SSI Signal: 43 dB</code></pre><p>In this case, focus on SSI Signal, and how it changes as you manipulate the device. You can add this as a column in the packet view, or even graph it (graph in the Qt version as the GTK version does not handle negative numbers gracefully).</p><p>2.</p><p>Evaluate retries - as communication degrades, the number of retries will likely increase. I would graph this, and we could do something like this filter:</p><pre><code>wlan.addr == (mac address of DuT) and wlan.fc.retry == 1</code></pre><p>While conditions are poor, there should be more retries.</p><p>3.</p><p>Evaluate Datarate - as communication degrades, datarate often does as well. You could graph min/max/avg datarates to/from the DuT. Something like this field name for the Y field in the graph tool, and then do a Display filter for the DuT. An example set of config items:</p><pre><code>Y field: wlan_radio.data_rate
Display Filter:  wlan.ta == (mac address of DuT)
Y Axis: AVG(Y field)</code></pre><p>4.</p><p>Evaluate bad frames - as communication degrades, perhaps the number of bad frames does as well. Check for FCS field and see if the number of bad frames increases to/from the DuT while communication is impaired.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 May '17, 04:07</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 May '17, 04:09</p></div></div><div id="comments-container-61640" class="comments-container"></div><div id="comment-tools-61640" class="comment-tools"></div><div class="clear"></div><div id="comment-61640-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

