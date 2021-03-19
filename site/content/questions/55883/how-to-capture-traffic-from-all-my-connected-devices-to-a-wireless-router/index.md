+++
type = "question"
title = "How to capture traffic from all my connected devices to a wireless router?"
description = '''Hi, I want to capture all the network traffic from all my devices connected to the router. Currently my desktop and mobile are connected to router. Whenever I browse network using my mobile, these packets are not shown in wireshark interface. only the packets captured through my desktop are visible....'''
date = "2016-09-26T15:37:00Z"
lastmod = "2016-09-26T15:37:00Z"
weight = 55883
keywords = [ "capture", "wi-fi", "mode", "promiscous" ]
aliases = [ "/questions/55883" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture traffic from all my connected devices to a wireless router?](/questions/55883/how-to-capture-traffic-from-all-my-connected-devices-to-a-wireless-router)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55883-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I want to capture all the network traffic from all my devices connected to the router. Currently my desktop and mobile are connected to router. Whenever I browse network using my mobile, these packets are not shown in wireshark interface. only the packets captured through my desktop are visible. I turned on promiscous mode also but still my mobile traffic is not showing up.</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">capture wi-fi mode promiscous</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '16, 15:37</strong></p><img src="https://secure.gravatar.com/avatar/fed3630d08110f9a121043ff2ffd146c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dpc813&#39;s gravatar image" /><p>dpc813<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dpc813 has no accepted answers">0%</span></p></div></div><div id="comments-container-55883" class="comments-container"><span id="55884"></span><div id="comment-55884" class="comment"><div id="post-55884-score" class="comment-score"></div><div class="comment-text"><p>How do you capture? Wireless? What OS is the device running that is doing the capture?</p></div><div id="comment-55884-info" class="comment-info"><span class="comment-age">(26 Sep '16, 16:20)</span> Jasper ♦♦</div></div><span id="55886"></span><div id="comment-55886" class="comment"><div id="post-55886-score" class="comment-score"></div><div class="comment-text"><p>Yeah wireless capture and I am using Windows 8.1</p></div><div id="comment-55886-info" class="comment-info"><span class="comment-age">(26 Sep '16, 17:33)</span> dpc813</div></div><span id="55887"></span><div id="comment-55887" class="comment"><div id="post-55887-score" class="comment-score"></div><div class="comment-text"><p>Search for questions using "monitoring" as search keyword (or find user Bob Jones and look at the questions he has answered). As you use Windows, the first step has to be to install NPcap with wireless monitoring support instead of WinPcap, yet the result depends on your wireless card manufacturer.</p></div><div id="comment-55887-info" class="comment-info"><span class="comment-age">(26 Sep '16, 21:48)</span> sindy</div></div><span id="55895"></span><div id="comment-55895" class="comment"><div id="post-55895-score" class="comment-score"></div><div class="comment-text"><p>From what I have found about monitor mode says that "monitor mode is used to capture all the packets in air without connecting to any access point(router)" while promiscous mode is used to get the information about packets(all connected devices traffic) flowing through an access point(router). Please correct me if i am wrong.</p></div><div id="comment-55895-info" class="comment-info"><span class="comment-age">(27 Sep '16, 02:57)</span> dpc813</div></div><span id="55896"></span><div id="comment-55896" class="comment"><div id="post-55896-score" class="comment-score"></div><div class="comment-text"><p>There's also the Wiki page on <a href="https://wiki.wireshark.org/CaptureSetup/WLAN">Wirelesss Capture</a> that might be some help.</p><p>Note in particular the section about capturing wireless traffic on <a href="https://wiki.wireshark.org/CaptureSetup/WLAN#Windows">Windows</a> and the issues caused by many wireless adaptor drivers.</p></div><div id="comment-55896-info" class="comment-info"><span class="comment-age">(27 Sep '16, 03:33)</span> grahamb ♦</div></div></div><div id="comment-tools-55883" class="comment-tools"></div><div class="clear"></div><div id="comment-55883-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

