+++
type = "question"
title = "Not capturing any data packets in monitor mode"
description = '''When I capture using Wireshark 2.0.1 in monitor mode, I only see WLAN control packets (clear-to-send, request-to-send, beacons, etc.) but not the TCP/UDP packets I&#x27;m sending and receiving. I so no packets relating to data except &quot;QoS Data&quot;. I added my network&#x27;s WPA-PSK key to the 802.11 preferences....'''
date = "2016-01-28T16:41:00Z"
lastmod = "2016-01-29T02:17:00Z"
weight = 49615
keywords = [ "capture", "data", "monitor", "wlan" ]
aliases = [ "/questions/49615" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Not capturing any data packets in monitor mode](/questions/49615/not-capturing-any-data-packets-in-monitor-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49615-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I capture using Wireshark 2.0.1 in monitor mode, I only see WLAN control packets (clear-to-send, request-to-send, beacons, etc.) but not the TCP/UDP packets I'm sending and receiving. I so no packets relating to data except "QoS Data". I added my network's WPA-PSK key to the 802.11 preferences.</p><p>Should I expect to be able to see data packets as well as control packets? I'm running OS X 10.11.2 (El Capitan) on a Macbook Pro with a built-in Airport Extreme Wi-Fi card.</p></div><div id="question-tags" class="tags-container tags">capture data monitor wlan</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jan '16, 16:41</strong></p><img src="https://secure.gravatar.com/avatar/cd79355789b7535d2a7c4661c7d3b22c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="freyr&#39;s gravatar image" /><p>freyr<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="freyr has no accepted answers">0%</span></p></div></div><div id="comments-container-49615" class="comments-container"></div><div id="comment-tools-49615" class="comment-tools"></div><div class="clear"></div><div id="comment-49615-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49621"></span>

<div id="answer-container-49621" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49621-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Should I expect to be able to see data packets as well as control packets?</p><p>Yes. Did you read the following wiki page?<a href="https://wiki.wireshark.org/HowToDecrypt802.11">https://wiki.wireshark.org/HowToDecrypt802.11</a></p><p>Some common mistakes are:</p><ol><li>Not capturing all 4 EAPOL frames. To do this, you need to capture frames when the client first associates to the WLAN</li><li>Not enabling the WLAN decryption option in Wireshark</li><li>Toggling the decryption option on to off then back on again.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '16, 02:17</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p>Amato_C<br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-49621" class="comments-container"><span id="49631"></span><div id="comment-49631" class="comment"><div id="post-49631-score" class="comment-score"></div><div class="comment-text"><p>Amato, thanks for your suggestions. I initially was having trouble capturing the EAPOL frames because I thought they needed to be sent between the router and my capture device (i.e., my laptop), and I couldn't get my laptop to associate with the WLAN if I was already in monitor mode. But then I tried connecting another device (phone) and captured 4 eapol frames.</p><p>I now seem to be getting decrypted TCP and UDP packets (although they are all red text on a black background, indicating a malformed packet).</p></div><div id="comment-49631-info" class="comment-info"><span class="comment-age">(29 Jan '16, 13:02)</span> freyr</div></div><span id="49632"></span><div id="comment-49632" class="comment"><div id="post-49632-score" class="comment-score"></div><div class="comment-text"><p>Could share us the trace or at least a screenshot?</p></div><div id="comment-49632-info" class="comment-info"><span class="comment-age">(29 Jan '16, 13:18)</span> Christian_R</div></div><span id="49637"></span><div id="comment-49637" class="comment"><div id="post-49637-score" class="comment-score"></div><div class="comment-text"><p>I would recommend you post a new question to the Wireshark community about this new problem you are experiencing. This will allow other experts to view the problem also. As Christian_R has suggested, post a trace on Google Drive or Cloudshark to help diagnose the issue.</p><p>Also, if the answer provided solved your problem, please accept the solution so others can also learn.</p></div><div id="comment-49637-info" class="comment-info"><span class="comment-age">(29 Jan '16, 15:20)</span> Amato_C</div></div><span id="49638"></span><div id="comment-49638" class="comment"><div id="post-49638-score" class="comment-score"></div><div class="comment-text"><p>Thanks for helping to solve the EAPOL issue. I'm still playing around with the separate TCP issue but I will post a new thread if I can't get it working.</p></div><div id="comment-49638-info" class="comment-info"><span class="comment-age">(29 Jan '16, 15:35)</span> freyr</div></div></div><div id="comment-tools-49621" class="comment-tools"></div><div class="clear"></div><div id="comment-49621-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

