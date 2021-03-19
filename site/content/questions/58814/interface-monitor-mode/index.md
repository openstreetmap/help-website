+++
type = "question"
title = "interface monitor mode"
description = '''under &#x27;mon-mode&#x27; WS had both of my interfaces (AR9271 @ wlan0 | BCM4322 @ wlan1) labeled &#x27;disabled&#x27; although only one (wlan0) had the capability. after closing WS i put down and changed wlan0 to monitor mode using &#x27;ifconfig&#x27; and &#x27;iwconfig&#x27; from the terminal. expecting wlan0 to have different status,...'''
date = "2017-01-16T08:45:00Z"
lastmod = "2017-01-16T08:45:00Z"
weight = 58814
keywords = [ "mon-mode" ]
aliases = [ "/questions/58814" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [interface monitor mode](/questions/58814/interface-monitor-mode)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58814-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>under 'mon-mode' WS had both of my interfaces (AR9271 @ wlan0 | BCM4322 @ wlan1) labeled 'disabled' although only one (wlan0) had the capability. after closing WS i put down and changed wlan0 to monitor mode using 'ifconfig' and 'iwconfig' from the terminal. expecting wlan0 to have different status, now it is not in the interface list. even after a reboot (and rechange wlan0 to monitor mode) WS still do not have it on the list. after closing the program again, i ran the following lines onto the terminal:</p><pre><code>$ sudo airmon-ng start wlan0</code></pre><p>when running WS again, wlan0 were still absent from the list but now the interface 'mon0' is in it eventhough it had the same 'disabled' as the 'mon-mode' status. when setting up WS i used the following command lines to remedy appropriate capture priviledge for all user:</p><pre><code>$  sudo groupadd wireshark
$  sudo usermod -a -G wireshark $USER
$  sudo chgrp wireshark /usr/bin/dumpcap
$  sudo chmod 755 /usr/bin/dumpcap
$  sudo setcap cap_net_raw,cap_net_admin=eip /usr/bin/dumpcap</code></pre><p>if this is not a normal outcome, i suspect that i either had missed something in the privilege setup or need to configure some new link layer header that i yet to understand. can someone please advice, thank you.</p></div><div id="question-tags" class="tags-container tags">mon-mode</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jan '17, 08:45</strong></p><img src="https://secure.gravatar.com/avatar/60026646367fa10a74b8a95a1728a0dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="harayz&#39;s gravatar image" /><p>harayz<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="harayz has no accepted answers">0%</span></p></div></div><div id="comments-container-58814" class="comments-container"><span id="58820"></span><div id="comment-58820" class="comment"><div id="post-58820-score" class="comment-score"></div><div class="comment-text"><p>Is the interface up? The description seems to indicate you took it down with ifconfig, did you bring it back up? Also turn off the network manager if you have not already done so.</p><p>$ sudo ifconfig wlan0 up</p><p>You can do all of this manually, which you may have to do. The iw command provides all the configuration capability.</p><p>Just as a test, run wireshark as root. See if you get a behavior change.</p></div><div id="comment-58820-info" class="comment-info"><span class="comment-age">(16 Jan '17, 09:52)</span> Bob Jones</div></div><span id="58821"></span><div id="comment-58821" class="comment"><div id="post-58821-score" class="comment-score"></div><div class="comment-text"><p>@Bob Jones: I would rather not have you recommend running Wireshark as root. People will take it as a solution, while it is a problem. Use the right tool and build from the ground up. As in this case, run dumpcap from the command line and see what it says, then step up to tshark, then Wireshark.</p></div><div id="comment-58821-info" class="comment-info"><span class="comment-age">(16 Jan '17, 13:30)</span> Jaap ♦</div></div></div><div id="comment-tools-58814" class="comment-tools"></div><div class="clear"></div><div id="comment-58814-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

