+++
type = "question"
title = "Only capturing broadcasts?"
description = '''So Im using Kali linux, and when I want to use wireshark, the first this I do is start moniter mode with airmon-ng, which is then says the adapter is in moniter mode. It is Panda Ultra 150Mbps 802.11n USB Adapter which was advertised to have both moniter and injection modes. then, i use iwconfig to ...'''
date = "2015-08-24T12:07:00Z"
lastmod = "2015-08-25T03:57:00Z"
weight = 45324
keywords = [ "kali" ]
aliases = [ "/questions/45324" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Only capturing broadcasts?](/questions/45324/only-capturing-broadcasts)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45324-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45324-score" class="post-score" title="current number of votes">0</div><span id="post-45324-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>So Im using Kali linux, and when I want to use wireshark, the first this I do is start moniter mode with airmon-ng, which is then says the adapter is in moniter mode. It is Panda Ultra 150Mbps 802.11n USB Adapter which was advertised to have both moniter and injection modes.<img src="https://osqa-ask.wireshark.org/upfiles/Screenshot_from_2015-08-24_15:00:54_JNlHMcj.png" alt="alt text" /></p><p>then, i use iwconfig to confirm its in moniter mode<img src="https://osqa-ask.wireshark.org/upfiles/Screenshot_from_2015-08-24_15:03:45.png" alt="alt text" /></p><p>then, i start wireshark and capture on wlan3mon, and this is all I get. Any help?<img src="https://osqa-ask.wireshark.org/upfiles/Screenshot_from_2015-08-24_15:05:18.png" alt="alt text" /></p><p>edit: after trying your suggestion Amato_C, I captured more that broadcasts but I thought I was supposed to be getting http packets from other devices on the network. It just seems like im only getting traffic from myself.<img src="https://osqa-ask.wireshark.org/upfiles/Screenshot_from_2015-08-24_21:08:01.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-kali" rel="tag" title="see questions tagged &#39;kali&#39;">kali</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Aug '15, 12:07</strong></p><img src="https://secure.gravatar.com/avatar/61d1530fe638f0968bffe17618f6e8ef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="napzackz&#39;s gravatar image" /><p><span>napzackz</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="napzackz has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Aug '15, 21:19</strong> </span></p></div></div><div id="comments-container-45324" class="comments-container"><span id="45331"></span><div id="comment-45331" class="comment"><div id="post-45331-score" class="comment-score"></div><div class="comment-text"><p>Are you trying to capture WiFi traffic on wlan0? It appears that wlan0 and wlan3 are on the same laptop/PC. Did you try:</p><ol><li><p>Shutting down wlan0 on the PC that you are performing the capture</p></li><li><p>Capture WiFi traffic from another WLAN client using wlan3.</p></li></ol></div><div id="comment-45331-info" class="comment-info"><span class="comment-age">(24 Aug '15, 18:41)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="45332"></span><div id="comment-45332" class="comment"><div id="post-45332-score" class="comment-score"></div><div class="comment-text"><p>Wlan3 has stopped working since I posted this, but its the same exact thing happening when I try it with wlan0.</p></div><div id="comment-45332-info" class="comment-info"><span class="comment-age">(24 Aug '15, 19:03)</span> <span class="comment-user userinfo">napzackz</span></div></div><span id="45336"></span><div id="comment-45336" class="comment"><div id="post-45336-score" class="comment-score">1</div><div class="comment-text"><p>Are you using a <em>capture</em> filter?</p><p>Note that capture filters that look at IP (v4 or v6), TCP, UDP, etc. information, or even look at link-layer type information such as Ethernet types, will <strong><em>NOT</em></strong> work on "protected" networks, i.e. networks using WEP or WPA/WPA2 encryption, as, at the layer where the capture filter is checked, the packets are still encrypted, and the only non-encrypted parts are the 802.11 MAC addresses and other 802.11 frame header fields.</p></div><div id="comment-45336-info" class="comment-info"><span class="comment-age">(24 Aug '15, 21:33)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="45337"></span><div id="comment-45337" class="comment"><div id="post-45337-score" class="comment-score"></div><div class="comment-text"><p>nope, no filters</p></div><div id="comment-45337-info" class="comment-info"><span class="comment-age">(24 Aug '15, 21:47)</span> <span class="comment-user userinfo">napzackz</span></div></div><span id="45341"></span><div id="comment-45341" class="comment"><div id="post-45341-score" class="comment-score"></div><div class="comment-text"><p>What is the configuration of your WLAN? Is your WLAN configured for 40MHz operation while you are capturing at 20MHz?</p><p>It would be best if you could post a capture on Cloudshark or Google Drive that included Beacon frames and a device associating to the network (i.e., Association Request and Response frames).</p></div><div id="comment-45341-info" class="comment-info"><span class="comment-age">(25 Aug '15, 03:57)</span> <span class="comment-user userinfo">Amato_C</span></div></div></div><div id="comment-tools-45324" class="comment-tools"></div><div class="clear"></div><div id="comment-45324-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45333"></span>

<div id="answer-container-45333" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-45333-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-45333-score" class="post-score" title="current number of votes">0</div><span id="post-45333-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Let's try the following.</p><ol><li>Remove the Panda Ultra 150 USB stick and reboot the laptop/PC</li><li>Issue the command <strong><em>ifconfig</em></strong> You should only see wlan0 = the Atheros AR9565 adapter</li><li>Issue the command <strong><em>iwlist wlan0 scanning</em></strong> This command performs a scan and will report all the available networks along with their associated channels. This could take some time depending on your RF environment so be patient</li><li>Find the SSID and the associated channel. Remember the channel for the next step.</li><li>Issue the command <strong><em>airmon-ng start wlan0 (channel)</em></strong> where channel was determined from step #4. For example, if you determined the WLAN exists on channel 6, then issue the command <strong><em>airmon-ng start wlan0 6</em></strong></li><li>Start Wireshark</li><li>Select the interface <strong><em>mon0</em></strong> or whatever monitor interface exists, such as mon1 or mon2. Do not select wlan0</li><li>Begin your capture.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '15, 19:29</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></img></div></div><div id="comments-container-45333" class="comments-container"><span id="45335"></span><div id="comment-45335" class="comment"><div id="post-45335-score" class="comment-score"></div><div class="comment-text"><p>thanks for the answer amato_c, i've updated the question with more information about it.</p></div><div id="comment-45335-info" class="comment-info"><span class="comment-age">(24 Aug '15, 21:20)</span> <span class="comment-user userinfo">napzackz</span></div></div></div><div id="comment-tools-45333" class="comment-tools"></div><div class="clear"></div><div id="comment-45333-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

