+++
type = "question"
title = "Why can&#x27;t I capture data packets in monitor mode?"
description = '''Hello everyone. I have question about capturing WiFi data packet by using following device and driver.  DWA-182 Wireless AC1200 Dual Band USB Adapter.  Acrylic Free WLAN NDIS driver -&amp;gt; Let DWA-182 turn on monitor mode and capture packet on window 7.  wireshark 2.0.4 (64bits). I want to catch pack...'''
date = "2016-07-29T01:53:00Z"
lastmod = "2016-07-29T02:50:00Z"
weight = 54433
keywords = [ "monitor-mode" ]
aliases = [ "/questions/54433" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why can't I capture data packets in monitor mode?](/questions/54433/why-cant-i-capture-data-packets-in-monitor-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54433-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello everyone. I have question about capturing WiFi data packet by using following device and driver. DWA-182 Wireless AC1200 Dual Band USB Adapter. Acrylic Free WLAN NDIS driver -&gt; Let DWA-182 turn on monitor mode and capture packet on window 7. wireshark 2.0.4 (64bits).</p><p>I want to catch packet in and out from a particular client. So I set display filter like this: wlan.sa == xx:xx:xx:xx:xx:xx || wlan.da == xx:xx:xx:xx:xx:xx After I start capture packet, I turn on the client. I can catch probe_request, probe_response, 4 EAPOL, null function data frame and Qos null function data frame. But I can't catch data or Qos data frame even I remove display filter. I find out that all packets I catch are malformed packet except of null function data frame and Qos null function data frame. Is this a point? Anyone has idea? Please help. Thanks.</p></div><div id="question-tags" class="tags-container tags">monitor-mode</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jul '16, 01:53</strong></p><img src="https://secure.gravatar.com/avatar/3f7cf2b19487bae37621af08812c570d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frazier&#39;s gravatar image" /><p>Frazier<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frazier has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Jul '16, 02:44</p></div></div><div id="comments-container-54433" class="comments-container"></div><div id="comment-tools-54433" class="comment-tools"></div><div class="clear"></div><div id="comment-54433-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54437"></span>

<div id="answer-container-54437" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54437-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Capturing WiFi traffic can be complex. You need to have the right hardware and software which supports the traffic you are trying to capture.</p><p>Specifically, the capture device needs to be able to capture frames that are in the RF environment. There are many different permutations of capabilities, especially when it comes to 802.11n or 802.11ac support. Your capture adapter needs to be able to match settings, such as:</p><ul><li>Frequency, i.e. 2.4 or 5 GHz</li><li>Bandwidth, 20/40/80 MHz</li><li>Spatial streams, up to 4 now on the market (?)</li><li>Guard interval, long or short</li><li>LDPC support Frame aggregation</li><li>MCS Index (implicit, can be derived from ther parameters mentioned)</li><li>... I am missing some...</li></ul><p>What you will find is that 'overhead' traffic like probes, ACKs, RTS/CTS, etc., usually go at relatively low data rates, so you might pick those up easily. However, under good conditions, data frames (type data or QoS-data) would go at full speed so this is where you need to have good capture capability. Another big issue with WiFi is not being in promiscuous mode, but based on your description that appears to not be an issue here - that would only show broadcast/multicast traffic even if other capabilities exist.</p><p>To test out your capture environment, turn 802.11n and/or 802.11ac capability off. Do you see all the traffic you expect? Then turn it back on and look for the differences in traffic flow under same test conditions. Review the capabilities of the WiFi system under test - the beacons, probe requests/responses, and association requests/responses will all give information as to the capabilities of the client and AP. You can check for things like 802.11ac vs 802.11n, spatial streams, guard interval, etc. Once you know the capabilities of the test system, compare to your capture system. What can it do? This may take reverse engineering, google search, or even a little trick - connect the capture adapter to the same test AP and inspect the same frames for what it's capabilities are, and compare. Also note just because a specific device may support a set of parameters in managed does not automatically mean it will support the same set in monitor mode.<br />
</p><p>In the end, you may need to purchase new hardware to sniff what you want. Amazon.com is a great place to purchase some low cost USB adapters to use for sniffing. Linux is a huge help as well, as you will not be limited to Acrylic's drivers.</p><p>Another option is OmniPeek with their capture adapters. That's a commercial system of HW/SW designed for WiFi capture. Many professionals use this, and this is what I recommend for those who need a Windows platform to capture WiFi traffic that is anything more capable than 802.11abg. At the lower end the AirPcap adapters are ok, but for 802.11n they are not good enough, even the AirPcap Nx device, which claims n support.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jul '16, 02:50</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p>Bob Jones<br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Jul '16, 04:23</p></div></div><div id="comments-container-54437" class="comments-container"><span id="54490"></span><div id="comment-54490" class="comment"><div id="post-54490-score" class="comment-score"></div><div class="comment-text"><p>Thanks for telling me lots of information about WiFi capturing, Bob Jones. I will try then.</p></div><div id="comment-54490-info" class="comment-info"><span class="comment-age">(01 Aug '16, 23:25)</span> Frazier</div></div></div><div id="comment-tools-54437" class="comment-tools"></div><div class="clear"></div><div id="comment-54437-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

