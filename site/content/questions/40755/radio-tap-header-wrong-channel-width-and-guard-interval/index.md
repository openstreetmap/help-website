+++
type = "question"
title = "Radio tap header: wrong channel width and guard interval"
description = '''I have my own Atheros-chipset based 802.11n Access Point (AP) setup, where I can control what capabilities are advertised to the clients. I run a iperf session between the AP (hosted on a Laptop) and a 802.11n smartphone. Also, I capture a trace of all packets received at the AP (hosted on a Laptop)...'''
date = "2015-03-20T18:33:00Z"
lastmod = "2015-04-13T07:17:00Z"
weight = 40755
keywords = [ "iperf", "radiotap", "802.11n" ]
aliases = [ "/questions/40755" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Radio tap header: wrong channel width and guard interval](/questions/40755/radio-tap-header-wrong-channel-width-and-guard-interval)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40755-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40755-score" class="post-score" title="current number of votes">0</div><span id="post-40755-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have my own Atheros-chipset based 802.11n Access Point (AP) setup, where I can control what capabilities are advertised to the clients. I run a iperf session between the AP (hosted on a Laptop) and a 802.11n smartphone. Also, I capture a trace of all packets received at the AP (hosted on a Laptop) from the smartphone. I notice some discrepancies in the radio tap header reported by wireshark, in the captures packets. For example:</p><ol><li>If I fix the capability to 20MHz channel width with long guard interval, I still see some (around 10%) of the packets wtih 40MHz channel width and/or short guard interval.</li><li>If fix the capability to 40MHz channel width with long guard interval, I see almost all (around 85%) packets with 20MHz channel width.</li></ol><p>The reason I believe this is a wireshark bug is that the throughput reported by iperf in case 2, is higher that what is at all possible (even theoretically), if 85% of the packets are sent at 20MHz data rates. So, most likely wireshark is reporting the channel width incorrectly.</p><p>Is this a known problem? Has anybody else seen this issue before?</p><p>Has anybody experienced issues even remotely related to this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-iperf" rel="tag" title="see questions tagged &#39;iperf&#39;">iperf</span> <span class="post-tag tag-link-radiotap" rel="tag" title="see questions tagged &#39;radiotap&#39;">radiotap</span> <span class="post-tag tag-link-802.11n" rel="tag" title="see questions tagged &#39;802.11n&#39;">802.11n</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Mar '15, 18:33</strong></p><img src="https://secure.gravatar.com/avatar/5ecb914deab6a1663666cbe31b0eb8c2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="UBWiNS&#39;s gravatar image" /><p><span>UBWiNS</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="UBWiNS has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Apr '15, 17:22</strong> </span></p></div></div><div id="comments-container-40755" class="comments-container"><span id="41369"></span><div id="comment-41369" class="comment"><div id="post-41369-score" class="comment-score"></div><div class="comment-text"><p>What does tcpdump report? If it reports the same thing, it's probably a <em>driver</em> bug, with Wireshark and tcpdump both just reporting what they're told.</p></div><div id="comment-41369-info" class="comment-info"><span class="comment-age">(10 Apr '15, 19:59)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-40755" class="comment-tools"></div><div class="clear"></div><div id="comment-40755-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41406"></span>

<div id="answer-container-41406" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41406-score" class="post-score" title="current number of votes">0</div><span id="post-41406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hello UBWiNS - I have experienced something very similar to your observations regarding the radiotap parameters. I have observed incorrect radiotap settings using numerous WiFi adapters each using different drivers. Recently, I have experimented with analyzing 2.4GHz traffic to determine if the traffic is being sent is 802.11b-only, 802.11g-only or 802.11b/g mixed. The following radiotap headers can be used to distinguish between each traffic type: (1) 2 GHz spectrum channel and CCK channel = 802.11b (2) 2 GHz spectrum channel and OFDM channel = pure 802.11g, no 802.11b STA's present (3) 2 GHz spectrum channel and Dynamic CCK-OFDM channel = 802.11g traffic with 11b STA's present. I set-up a WLAN using 802.11b-only access. When I connected a STA and examined the radiotap parameters within WLAN frames from the STA to the AP and vice-versa I observed the following parameters set: a) 2GHz spectrum channel- as expected b) Most traffic was marked as OFDM. According to the IEEE 802.11-2012 specification, sections 16 and 17, 802.11b can only be transmitted using DSSS/CCK modultation. So the OFDM parameter was incorrectly being set. I also confirmed that all the traffic was sent at 11b rates (1, 2, 5.5 or 11Mbps). I think this is a driver issue because another WiFi adapter/driver combination had the correct settings.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Apr '15, 07:17</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-41406" class="comments-container"></div><div id="comment-tools-41406" class="comment-tools"></div><div class="clear"></div><div id="comment-41406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

