+++
type = "question"
title = "Wireshark Capture Interfaces not showing up properly"
description = '''I installed Wireshark 1.6.5 to do packet captures on my home network for my LAN Security class and under the capture interface window my adapters are not listed properly. I see my Ethernet adapter show up but not the wireless. It shows up as &quot;Microsoft&quot; instead of &quot;Atheros AR9285&quot;. I need to be able...'''
date = "2012-03-03T10:13:00Z"
lastmod = "2012-03-03T10:13:00Z"
weight = 9331
keywords = [ "wireshark" ]
aliases = [ "/questions/9331" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Capture Interfaces not showing up properly](/questions/9331/wireshark-capture-interfaces-not-showing-up-properly)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9331-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I installed Wireshark 1.6.5 to do packet captures on my home network for my LAN Security class and under the capture interface window my adapters are not listed properly. I see my Ethernet adapter show up but not the wireless. It shows up as "Microsoft" instead of "Atheros AR9285". I need to be able to see the wireless packets flowing through the network to do my assignment.</p><p>I have tried uninstalling and re-installing the wireless drivers and no luck same thing shows up. Im at a loss at what the problem can be. So I'm asking on the kindness of strangers to help me figure this out.</p><p>I have included a screenshot of both my Device Manager and Wireshark Interfaces capture below. My PC is a windows 7 Ultimate x64 Asus K53TA-BBR6 model laptop.</p><p>Wireshark Capture Interfaces: <img src="http://i1165.photobucket.com/albums/q600/emiljan-haxhi/WiresharkCaptureInterface.jpg" alt="alt text" /></p><p>Device Manager: <img src="http://i1165.photobucket.com/albums/q600/emiljan-haxhi/DeviceManager.jpg" alt="alt text" /></p><p>Thank You,</p><p>Emiljan</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Mar '12, 10:13</strong></p><img src="https://secure.gravatar.com/avatar/9f1efd71c3a22648cc5523880c93fe3d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emiljan&#39;s gravatar image" /><p>emiljan<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emiljan has no accepted answers">0%</span></p></img></div></div><div id="comments-container-9331" class="comments-container"><span id="9334"></span><div id="comment-9334" class="comment"><div id="post-9334-score" class="comment-score"></div><div class="comment-text"><p>Given that you say</p><blockquote><p>I see my Ethernet adapter show up but not the wireless. It shows up as "Microsoft" instead of "Atheros AR9285".</p></blockquote><p>you apparently <em>do</em> see your wireless show up; it just doesn't show up with a useful name. (For some reason, WinPcap gets "Microsoft" as the name for some network adapters, and that's what it reports to Wireshark, so that's what Wireshark displays; that's a known problem, but I'm not sure what the solution is.)</p><p>What happens if you try to capture on that interface? Does it work?</p></div><div id="comment-9334-info" class="comment-info"><span class="comment-age">(03 Mar '12, 12:57)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-9331" class="comment-tools"></div><div class="clear"></div><div id="comment-9331-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

