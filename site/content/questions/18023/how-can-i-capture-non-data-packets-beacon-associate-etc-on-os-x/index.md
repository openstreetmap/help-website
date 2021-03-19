+++
type = "question"
title = "How can I capture non-data packets (Beacon, Associate, etc.) on OS X?"
description = '''I installed the Wireshark on my MAC and tried to sniff the air for WLAN packets (802.11) I see packets that looks like a higher level than what I expected For ex. I do not see Beacons or do not see Association packets when I closed and opened my WiFi. On the other hand, I do see DNS packets and NBNC...'''
date = "2013-01-29T03:14:00Z"
lastmod = "2013-01-30T06:41:00Z"
weight = 18023
keywords = [ "wlan", "sniffer", "wifi", "802.11", "mac" ]
aliases = [ "/questions/18023" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How can I capture non-data packets (Beacon, Associate, etc.) on OS X?](/questions/18023/how-can-i-capture-non-data-packets-beacon-associate-etc-on-os-x)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18023-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I installed the Wireshark on my MAC and tried to sniff the air for WLAN packets (802.11) I see packets that looks like a higher level than what I expected For ex. I do not see Beacons or do not see Association packets when I closed and opened my WiFi. On the other hand, I do see DNS packets and NBNC packets.</p><p>Is there anything I need to configure to have this ability?</p></div><div id="question-tags" class="tags-container tags">wlan sniffer wifi 802.11 mac</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '13, 03:14</strong></p><img src="https://secure.gravatar.com/avatar/12fa7c789a8d12a8906726ee93f29a6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NimrodB&#39;s gravatar image" /><p>NimrodB<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NimrodB has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Jan '13, 17:00</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-18023" class="comments-container"><span id="18027"></span><div id="comment-18027" class="comment"><div id="post-18027-score" class="comment-score"></div><div class="comment-text"><p>I managed to find how to display all WLAN data only (Analyze -&gt; Enable Protocols -&gt; 802.11) Now I see only data with Protocol value of "Unknown" and in the Info value I have "WTAP_ENCAP". I can only assume this is my WiFi data but the Wireshark does not know how to decipher it (?)</p></div><div id="comment-18027-info" class="comment-info"><span class="comment-age">(29 Jan '13, 03:33)</span> NimrodB</div></div><span id="18066"></span><div id="comment-18066" class="comment"><div id="post-18066-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I managed to find how to display all WLAN data only (Analyze -&gt; Enable Protocols -&gt; 802.11)</p></blockquote><p>You probably <em>DIS</em>abled 802.11, which prevented Wireshark from dissecting 802.11 packets.</p></div><div id="comment-18066-info" class="comment-info"><span class="comment-age">(29 Jan '13, 16:59)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-18023" class="comment-tools"></div><div class="clear"></div><div id="comment-18023-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="18028"></span>

<div id="answer-container-18028" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18028-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Have you looked at the Wiki pages on <a href="http://wiki.wireshark.org/Wi-Fi">WiFi</a> and <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">WLAN Capturing</a>, particularly the section for <a href="http://wiki.wireshark.org/CaptureSetup/WLAN#Mac_OS_X">Mac OS X</a>?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '13, 03:34</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Jan '13, 03:36</p></div></div><div id="comments-container-18028" class="comments-container"><span id="18034"></span><div id="comment-18034" class="comment"><div id="post-18034-score" class="comment-score"></div><div class="comment-text"><p>I did but could not find the answer. But I must say - most of what was written there - I did not understand</p></div><div id="comment-18034-info" class="comment-info"><span class="comment-age">(29 Jan '13, 05:37)</span> NimrodB</div></div></div><div id="comment-tools-18028" class="comment-tools"></div><div class="clear"></div><div id="comment-18028-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18045"></span>

<div id="answer-container-18045" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18045-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think I found the way! :) When double clicking on the interface to use (in my case - e?1) - I chose Display in Monitor Mode (or something like that) Then I choose to use 802.11 on the item that used to be gray.</p><p>and that's it - I now see WLAN packets!</p><p>(Wireshark removes most of the packet which is a shame but... that is still something) :)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '13, 09:41</strong></p><img src="https://secure.gravatar.com/avatar/12fa7c789a8d12a8906726ee93f29a6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NimrodB&#39;s gravatar image" /><p>NimrodB<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NimrodB has no accepted answers">0%</span></p></div></div><div id="comments-container-18045" class="comments-container"><span id="18065"></span><div id="comment-18065" class="comment"><div id="post-18065-score" class="comment-score"></div><div class="comment-text"><p>Yes, on OS X you have to be in monitor mode in order to see non-data 802.11 packets; when not in monitor mode, only data packets are captured, and they have fake Ethernet headers.</p><p>Wireshark probably isn't removing most of the packet; in monitor mode, it captures packets other than packets to and from your machine, and doesn't supply decrypted packets. If you're on a WEP or WPA/WPA2 network, you'll need to supply the network key and capture the initial setup packets; see <a href="http://wiki.wireshark.org/HowToDecrypt802.11">How To Decrypt 802.11</a>.</p></div><div id="comment-18065-info" class="comment-info"><span class="comment-age">(29 Jan '13, 16:57)</span> Guy Harris ♦♦</div></div><span id="18076"></span><div id="comment-18076" class="comment"><div id="post-18076-score" class="comment-score"></div><div class="comment-text"><p>I looked at beacons from my AP and most of the data is not there. (Beacons are not encrypted) That is why I think it removes/do not display all the data.</p><p>If it's something in the Wireshark preferences - please let me know how to fix it.</p><p>thanks.</p></div><div id="comment-18076-info" class="comment-info"><span class="comment-age">(29 Jan '13, 23:36)</span> NimrodB</div></div><span id="18079"></span><div id="comment-18079" class="comment"><div id="post-18079-score" class="comment-score"></div><div class="comment-text"><p>Try capturing with tcpdump (to capture in monitor mode, use the -I (capital I) flag in OS X 10.6 and later, and do "tcpdump -L" and then choose one of the 802.11 flavors from that list and use it with the -y flag in 10.5), using "-i en1" (if the interface is en1) for all instances (including "tcpdump -L"), and, for the capture instance, using "-s 0" and "-w {pathname to file}".</p><p>Then try opening the file tcpdump wrote to with Wireshark.</p><p>If you see the same results, as I suspect you will, it is <em>NOT</em> a problem with Wireshark, it's probably a problem with your Wi-Fi adapter or the driver.</p></div><div id="comment-18079-info" class="comment-info"><span class="comment-age">(30 Jan '13, 00:10)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-18045" class="comment-tools"></div><div class="clear"></div><div id="comment-18045-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18103"></span>

<div id="answer-container-18103" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18103-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think I understand what I see - for ex. - the Beacon: The Wireshark does read all the data - but it does not understand some of it. All the InfoElements sections he sees as DATA. Is there a way for him (Wireshark) to learn/know from the AP type/name the order of the data and the IEs? For ex. Cisco AP - the IE order is xyz; and TP AP the order is yzx...?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '13, 06:41</strong></p><img src="https://secure.gravatar.com/avatar/12fa7c789a8d12a8906726ee93f29a6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NimrodB&#39;s gravatar image" /><p>NimrodB<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NimrodB has no accepted answers">0%</span></p></div></div><div id="comments-container-18103" class="comments-container"></div><div id="comment-tools-18103" class="comment-tools"></div><div class="clear"></div><div id="comment-18103-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

