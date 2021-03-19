+++
type = "question"
title = "wireshark capture only my pc packets"
description = '''Hi, I have broadcom 4313 wirless adapter, I used wireshark but I can only see my packets how I can see pacekts of other pc&#x27;s on my lan, I have windows 7 64bit.'''
date = "2012-08-21T12:51:00Z"
lastmod = "2012-08-24T12:36:00Z"
weight = 13799
keywords = [ "wireshark" ]
aliases = [ "/questions/13799" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [wireshark capture only my pc packets](/questions/13799/wireshark-capture-only-my-pc-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13799-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have broadcom 4313 wirless adapter, I used wireshark but I can only see my packets how I can see pacekts of other pc's on my lan, I have windows 7 64bit.</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Aug '12, 12:51</strong></p><img src="https://secure.gravatar.com/avatar/993ceee7e25758f6fd2d07f42777c66b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mkarmi&#39;s gravatar image" /><p>mkarmi<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mkarmi has no accepted answers">0%</span></p></div></div><div id="comments-container-13799" class="comments-container"></div><div id="comment-tools-13799" class="comment-tools"></div><div class="clear"></div><div id="comment-13799-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="13811"></span>

<div id="answer-container-13811" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13811-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>By either running something other than Windows, by running something other than Wireshark, or by buying an <a href="http://www.riverbed.com/us/products/cascade/wireshark_enhancements/airpcap.php">AirPcap USB adapter</a>.</p><p>On a Wi-Fi network, you'd have to run in monitor mode to see traffic to or from other machines on the network.</p><p>On Windows, Wireshark uses WinPcap, which doesn't support the Windows feature (Native Wi-Fi) required to run in monitor mode. <a href="http://support.microsoft.com/kb/933741">Microsoft Network Monitor</a> <em>does</em> support Native Wi-Fi and thus can support monitor mode <em>if</em> the driver for your network adapter supports it - which, unfortunately, many don't, and others do but not correctly, so that's not a guarantee. (I don't know whether the Windows driver for the Broadcom 4313 supports monitor mode correctly.) There are also programs that cost money that can capture in monitor mode on at least some types of network adapters (at least some of them supply their own drivers for the network adapters, so they only work with some network adapters). Some of those programs include:</p><ul><li><a href="http://www.tamos.com/products/commwifi/">CommView for WiFi</a>, which supports <a href="http://www.tamos.com/products/commwifi/adapterlist.php">these adapters</a>;</li><li><a href="http://www.wildpackets.com/products/omnipeek_network_analyzer">OmniPeek</a>, which supports <a href="http://www.wildpackets.com/support/omni/omnipeek_basic/wireless">these adapters</a>;</li><li><a href="http://www.netscout.com/products/enterprise/Sniffer_Portable_Analyzer/Sniffer_Portable_Professional_Analyzer/Pages/default.aspx">Sniffer Portable</a>, which appears to support <a href="http://www.netscout.com/library/Data%20sheets/NetScout_ds_Sniffer_Portable.pdf">only some Atheros adapters</a>.</li></ul><p>The AirPcap adapters don't go through the normal Wi-Fi networking stack on Windows (they <em>only</em> act as capture devices; they don't work as regular Wi-Fi adapters), and WinPcap includes support for them, so they can be used to capture other machines' traffic on Windows using Wireshark.</p><p>On, for example, Linux, Wireshark uses libpcap, which uses mechanisms that support monitor mode.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Aug '12, 01:10</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Aug '12, 14:51</p></div></div><div id="comments-container-13811" class="comments-container"><span id="13827"></span><div id="comment-13827" class="comment"><div id="post-13827-score" class="comment-score"></div><div class="comment-text"><p>Thank you, but I want to ask if I downloaded wireshark in linux can I capture in monitor mode? and how can I download libcap on it?</p></div><div id="comment-13827-info" class="comment-info"><span class="comment-age">(22 Aug '12, 13:38)</span> mkarmi</div></div><span id="13828"></span><div id="comment-13828" class="comment"><div id="post-13828-score" class="comment-score"></div><div class="comment-text"><blockquote><p>if I downloaded wireshark in linux can I capture in monitor mode</p></blockquote><p>Yes. See <a href="http://wiki.wireshark.org/CaptureSetup/WLAN#Linux">this part of the Wireshark Wiki</a> for information on how to turn monitor mode on.</p><blockquote><p>and how can I download libcap on it</p></blockquote><p>Most Linux distributions have both command-line and GUI tools for installing packaged software for the distribution. If you were to install Wireshark through one of those tools, the tool would also install libpcap, as Wireshark on UN*X depends on libpcap.</p></div><div id="comment-13828-info" class="comment-info"><span class="comment-age">(22 Aug '12, 14:32)</span> Guy Harris ♦♦</div></div><span id="13848"></span><div id="comment-13848" class="comment"><div id="post-13848-score" class="comment-score"></div><div class="comment-text"><p>I downloaded wireshark in linux, first I got no intreface I solved that by typping in the terminal "sudo wireshark" but I got this message Lua: Error during loading: [string "/usr/share/wireshark/init.lua"]:45: dofile has been disabled" and capture monitor mode is grey in eth0, so that means my wirlesscard not supported?</p></div><div id="comment-13848-info" class="comment-info"><span class="comment-age">(23 Aug '12, 09:33)</span> mkarmi</div></div><span id="13883"></span><div id="comment-13883" class="comment"><div id="post-13883-score" class="comment-score"></div><div class="comment-text"><p>The Lua message may mean "I'm running as root, so I'm afraid of running random bits of possibly-untrustworthy Lua code, so I'm not going to do it'. You should probably be afraid of <a href="http://anonsvn.wireshark.org/viewvc/trunk/doc/README.packaging?revision=34311&amp;view=markup">running over 2 million lines of C code as root</a>, too. See the sections on Debian/Ubuntu/etc., and on other Linux distributions, in <a href="http://wiki.wireshark.org/CaptureSetup/CapturePrivileges">the Capture Privileges page in the Wireshark Wiki</a>.</p></div><div id="comment-13883-info" class="comment-info"><span class="comment-age">(24 Aug '12, 13:51)</span> Guy Harris ♦♦</div></div><span id="13884"></span><div id="comment-13884" class="comment"><div id="post-13884-score" class="comment-score"></div><div class="comment-text"><p>On many Linux distributions, libpcap isn't built with libnl, causing its APIs for turning monitor mode on not to work. Those APIs are what Wireshark uses, so, on those distributions, Wireshark will (correctly) think it can't turn monitor mode on.</p><p>See <a href="http://wiki.wireshark.org/CaptureSetup/WLAN#Linux">the Linux section of the CaptureSetup/WLAN page of the Wireshark Wiki</a> for information on an alternative way to capture in monitor mode, using the <code>airmon-ng</code> script.</p></div><div id="comment-13884-info" class="comment-info"><span class="comment-age">(24 Aug '12, 13:54)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-13811" class="comment-tools"></div><div class="clear"></div><div id="comment-13811-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13879"></span>

<div id="answer-container-13879" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13879-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Check this <a href="http://nagaraj-embedded.blogspot.in/2012/03/capturing-usb-data-through-wireshark.html">link</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '12, 12:36</strong></p><img src="https://secure.gravatar.com/avatar/0cf7e05b14ad6662ecde4c327bb2c39f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harsha&#39;s gravatar image" /><p>Harsha<br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harsha has no accepted answers">0%</span></p></div></div><div id="comments-container-13879" class="comments-container"><span id="13885"></span><div id="comment-13885" class="comment"><div id="post-13885-score" class="comment-score"></div><div class="comment-text"><p>That helps if you want to capture USB traffic, but that won't help for Wi-Fi traffic between other machines on your network.</p></div><div id="comment-13885-info" class="comment-info"><span class="comment-age">(24 Aug '12, 13:55)</span> Guy Harris ♦♦</div></div><span id="13886"></span><div id="comment-13886" class="comment"><div id="post-13886-score" class="comment-score"></div><div class="comment-text"><p>additionally, you assume Linux, whereas the OP mentioned 'windows 7 64bit' !?!</p></div><div id="comment-13886-info" class="comment-info"><span class="comment-age">(24 Aug '12, 14:10)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-13879" class="comment-tools"></div><div class="clear"></div><div id="comment-13879-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

