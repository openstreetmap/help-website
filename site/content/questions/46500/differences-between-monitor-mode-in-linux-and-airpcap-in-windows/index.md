+++
type = "question"
title = "Differences between Monitor mode in linux and Airpcap in windows"
description = '''Hi I need to sniff WiFi packets, can anyone tell what is the difference between using Monitor mode and Aircrack-ng in linux and using the Airpcap in windows? there is any kind of data that can be extracted from one method but not from the other? what is the better way to sniff WiFi packets? Thanks!'''
date = "2015-10-13T08:08:00Z"
lastmod = "2015-10-13T18:20:00Z"
weight = 46500
keywords = [ "wifi" ]
aliases = [ "/questions/46500" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Differences between Monitor mode in linux and Airpcap in windows](/questions/46500/differences-between-monitor-mode-in-linux-and-airpcap-in-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46500-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I need to sniff WiFi packets, can anyone tell what is the difference between using Monitor mode and Aircrack-ng in linux and using the Airpcap in windows? there is any kind of data that can be extracted from one method but not from the other? what is the better way to sniff WiFi packets?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">wifi</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Oct '15, 08:08</strong></p><img src="https://secure.gravatar.com/avatar/23b3c363f5c5e0f67ef1e05377ef76e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MichaelB&#39;s gravatar image" /><p>MichaelB<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MichaelB has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Oct '15, 16:04</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-46500" class="comments-container"></div><div id="comment-tools-46500" class="comment-tools"></div><div class="clear"></div><div id="comment-46500-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="46542"></span>

<div id="answer-container-46542" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46542-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>IMHO, go with the Linux solution and stay away from AirPCAP! Reasons:</p><ol><li><p>Economical = AIRPCAP want $700 for a WiFi adapter.</p></li><li><p>Technical:</p></li></ol><p>a. Lack of 11ac support</p><p>b. I cannot find any documentation in which AirPCAP supports LDPC coding. Unfortunately, all the new 11n and all the 11ac adapters support LDPC. If your WiFi capturing adapter does not support LDPC, then you cannot capture data packets between the AP/wireless router and the WiFi client.</p><p>I have asked a similar question on other communities (my question was related to the preferred WiFi capturing tool/software) and all the WiFi developers came back with the same answer: use Linux and get a WiFi card that supports the features you need.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '15, 18:20</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-46542" class="comments-container"><span id="46565"></span><div id="comment-46565" class="comment"><div id="post-46565-score" class="comment-score">1</div><div class="comment-text"><p>UPDATE: The AirPcap Nx WiFi adapter uses the the AR9170 WiFi chipset from Qualcomm-Atheros. The AR9170 chipset does not support LDPC coding which means that the AirPcap Nx adapter also does not support LDPC coding.</p><p>If the WLAN being monitored (Access Point and client) uses LDPC coding, then the WiFi adapter used for capturing WiFi frames must also support LDPC coding too. Otherwise, packets sent at HT or VHT rates in one or both directions will be missing or damaged. Since LDPC coding occurs at the hardware level, a firmware upgrade cannot provide LDPC coding to the WiFi adapter.</p></div><div id="comment-46565-info" class="comment-info"><span class="comment-age">(15 Oct '15, 07:08)</span> Amato_C</div></div></div><div id="comment-tools-46542" class="comment-tools"></div><div class="clear"></div><div id="comment-46542-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46516"></span>

<div id="answer-container-46516" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46516-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>what is the difference between using Monitor mode and Aircrack-ng in linux and using the Airpcap in windows?</p></blockquote><p>I'd say not much. In both cases you will see WLAN/Wifi frames of other stations, besides your own frames.</p><p>The main reason why you need Airpcap on Windows, is because you can't (easily) put a wlan/wifi card in monitor mode on Windows, at least not with WinPcap.<br />
</p><blockquote><p>there is any kind of data that can be extracted from one method but not from the other?</p></blockquote><p>Airpcap will probably report signal strength and similar HW related values, which your wifi card on Linux might or might not report (depends on the card and the driver).</p><blockquote><p>what is the better way to sniff WiFi packets?</p></blockquote><p>Better in terms of what? Both methods will deliver wlan/wifi frames. I don't see a way to do that 'better'.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Oct '15, 13:52</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-46516" class="comments-container"></div><div id="comment-tools-46516" class="comment-tools"></div><div class="clear"></div><div id="comment-46516-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

