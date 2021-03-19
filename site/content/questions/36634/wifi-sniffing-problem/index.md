+++
type = "question"
title = "Wifi sniffing problem"
description = '''I am connected to wifi router with Wpa2-personal security. I use Linux Mint platform,than put my NIC in monitor mode with aircrack-ng and decrypt wifi connection in wireshark. Everything fine. The problem is, that I can see just my traffic via wifi when I capture on mon0 interface.  While I was capt...'''
date = "2014-09-26T06:01:00Z"
lastmod = "2014-09-26T06:01:00Z"
weight = 36634
keywords = [ "sniffing", "problem", "wifi", "wpa2", "monitor" ]
aliases = [ "/questions/36634" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wifi sniffing problem](/questions/36634/wifi-sniffing-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36634-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am connected to wifi router with Wpa2-personal security. I use Linux Mint platform,than put my NIC in monitor mode with aircrack-ng and decrypt wifi connection in wireshark. Everything fine.</p><p>The problem is, that I can see just my traffic via wifi when I capture on mon0 interface. While I was capturing I reconnect my phone connection. The only thing I could see were DHCP broadcast packets.</p><p>So why I cannot see traffic between router and other PCs or phones ?</p><p>regards, m.</p></div><div id="question-tags" class="tags-container tags">sniffing problem wifi wpa2 monitor</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '14, 06:01</strong></p><img src="https://secure.gravatar.com/avatar/e8673e166d1ab5d73f51e6badda1a9d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mojito&#39;s gravatar image" /><p>mojito<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mojito has no accepted answers">0%</span></p></div></div><div id="comments-container-36634" class="comments-container"><span id="36677"></span><div id="comment-36677" class="comment"><div id="post-36677-score" class="comment-score">1</div><div class="comment-text"><p>Are you also connected to a wireless network with the client you're running the sniffer? Because that won't work together with monitor mode of course.</p><p>Other check: Are you listening on the correct channel and are you NOT using 802.11n connections for testing if the problem also appears when your AP is in a/b/g mode</p></div><div id="comment-36677-info" class="comment-info"><span class="comment-age">(28 Sep '14, 23:58)</span> Landi</div></div><span id="36679"></span><div id="comment-36679" class="comment"><div id="post-36679-score" class="comment-score"></div><div class="comment-text"><p>Thanks for answering me. Yes, I was connected to network. But now I tried without connection and captured on mon0 interface . There were just 802.11 broadcast frames and some LLC packets ...</p><p>Sorry if this is silly, but how do you check for 802.11n connection and correct channel ?</p></div><div id="comment-36679-info" class="comment-info"><span class="comment-age">(29 Sep '14, 00:52)</span> mojito</div></div><span id="36682"></span><div id="comment-36682" class="comment"><div id="post-36682-score" class="comment-score">1</div><div class="comment-text"><p>You should always capture with a third device which is not associated to any wireless network.</p><p>Check your AP to see if you can force the wifi to e.g. 802.11b/g testwise - 802.11n uses multiple antennas/channels, so if you're having issues it's always good to check against a single channel network (a/b/g) first to see if that might be an issue.</p></div><div id="comment-36682-info" class="comment-info"><span class="comment-age">(29 Sep '14, 02:02)</span> Landi</div></div></div><div id="comment-tools-36634" class="comment-tools"></div><div class="clear"></div><div id="comment-36634-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

