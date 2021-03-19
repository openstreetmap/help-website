+++
type = "question"
title = "How to capture Bluetooth on Debian Wheezy?"
description = '''Hi everyone. I&#x27;m trying to capture Bluetooth as per a college assignment. I started following the instructions here: http://wiki.wireshark.org/CaptureSetup/Bluetooth The highest libpcap version in the Debian repos is 0.8, which doesn&#x27;t support Bluetooth, so I downloaded the latest 1.6.2 version. Dur...'''
date = "2014-10-27T05:00:00Z"
lastmod = "2014-10-27T14:46:00Z"
weight = 37372
keywords = [ "setup", "configuration", "bluetooth", "hci_h4", "capture-setup" ]
aliases = [ "/questions/37372" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture Bluetooth on Debian Wheezy?](/questions/37372/how-to-capture-bluetooth-on-debian-wheezy)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37372-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone.</p><p>I'm trying to capture Bluetooth as per a college assignment. I started following the instructions here:</p><p><a href="http://wiki.wireshark.org/CaptureSetup/Bluetooth">http://wiki.wireshark.org/CaptureSetup/Bluetooth</a></p><p>The highest <code>libpcap</code> version in the Debian repos is 0.8, which doesn't support Bluetooth, so I downloaded the latest 1.6.2 version. During the <code>configure</code> step, I installed <code>libbluetooth-dev</code>, <code>libusb-dev</code>, and <code>libusb-1.0-0-dev</code>. After that, I based myself on the instructions here:</p><p><a href="https://www.myricom.com/software/sniffer10g/487-how-do-i-set-up-a-linux-libpcap-application-to-use-sniffer10g-receive-bypass.html">https://www.myricom.com/software/sniffer10g/487-how-do-i-set-up-a-linux-libpcap-application-to-use-sniffer10g-receive-bypass.html</a></p><p>to get Wireshark to use the newest <code>libpcap</code> (by linking from the old <code>libpcap</code>). It worked, in the sense that <code>bluetooth0</code> was added to the interfaces list. But, when I tried to capture from it, I got an error message:</p><p>The specified data link type "BLUETOOTH_HCI_H4_WITH_P" isn't valid</p><p>Since I couldn't find a thing on Google, I looked around the repos and installed <code>bluez-hcidump</code>, which changed nothing.</p><p>I have <code>Linux 3.2.0-4-686-pae</code> and Debian Wheezy 7.6 in an HP Mini 110-3100. I think that the adapter responsible for Bluetooth is <code>Broadcom Corporation BCM4313 802.11b/g/n Wireless LAN Controller</code>. It was the closest in <code>lspci</code>, and HP no longer supports it, so I can't get the info from them.</p><p>Is it possible to capture Bluetooth in Debian Wheezy? What do I need to do to do that?</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags">setup configuration bluetooth hci_h4 capture-setup</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Oct '14, 05:00</strong></p><img src="https://secure.gravatar.com/avatar/482f373cebb74faf059d33fcdf0f15de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GuiRitter&#39;s gravatar image" /><p>GuiRitter<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GuiRitter has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Oct '14, 06:20</p></div></div><div id="comments-container-37372" class="comments-container"></div><div id="comment-tools-37372" class="comment-tools"></div><div class="clear"></div><div id="comment-37372-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37380"></span>

<div id="answer-container-37380" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37380-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>The highest libpcap version in the Debian repos is 0.8</p></blockquote><p>The version number in the Debian libpcap package name is a bit mysterious. There was an "0.7" before the "0.8", so <em>maybe</em> there was a time when the version number in the package tracked the actual libpcap version number; however, perhaps they realized, when libpcap 0.9 came out, that I was ensuring binary compatibility between libpcap releases and that they didn't need to come out with a new "libpcap-x.y" package for every new version.</p><p>So they stopped updating the version number in the package name to match the libpcap version number. In Wheezy, <a href="https://packages.debian.org/wheezy/libpcap0.8">the libpcap-0.8 package is based on libpcap 1.3.0</a>.</p><p>libpcap 1.3.0 <em>does</em> include Bluetooth capture support for Linux; however, it's only built if the system on which libpcap is compiled has the <code>bluetooth/bluetooth.h</code> header file, so, <em>if</em> Bluetooth capture doesn't work on Wheezy with the <em>standard</em> libpcap package, perhaps it wasn't, for whatever reason, built with Bluetooth capture included (either they explicitly turned it off or the build wasn't done on a system with the bluez <em>developer</em> package installed.</p><p>I.e., do <em>not</em> assume, just because Debian chooses to call their libpcap package "libpcap-0.8", that the libpcap on Wheezy doesn't support Bluetooth. Try using the standard libpcap first (uninstall the libpcap you built, and, if you built Wireshark from source with that library, do a <code>make distclean</code> on your Wireshark source tree, make sure "libpcap-dev" is installed, and reconfigure and rebuild Wireshark) .</p><p><em>If</em> that still doesn't work, what version of Wireshark are you using? The data link type "BLUETOOTH_HCI_H4_WITH_P" <em>isn't</em>, in fact, valid, because the correct type is "BLUETOOTH_HCI_H4_WITH_PHDR", so that seems to be a problem between Wireshark and dumpcap.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Oct '14, 14:46</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-37380" class="comments-container"><span id="37420"></span><div id="comment-37420" class="comment"><div id="post-37420-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your answer and sorry for my late answer, I've been busy. Too bad the name is misleading and I did't paid attention to that. I didn't built Wireshark manually, I just installed it from the repo. It's expected it would not work then, because the Debian repo programs are always outdated. I'll try to build Wireshark manually following your instructions soon and post the results here.</p><p>As I said, I'm using the latest stable version from the Wheezy repo (1.8.2-5wheezy12): <a href="https://packages.debian.org/wheezy/wireshark">https://packages.debian.org/wheezy/wireshark</a></p></div><div id="comment-37420-info" class="comment-info"><span class="comment-age">(28 Oct '14, 18:21)</span> GuiRitter</div></div><span id="37503"></span><div id="comment-37503" class="comment"><div id="post-37503-score" class="comment-score"></div><div class="comment-text"><p>The <a href="http://sources.debian.net/src/libpcap/1.6.2-2/debian/changelog/">changelog</a> of the Debian package says:</p><pre><code>libpcap (1.5.3-2) unstable; urgency=low
  * Enable Bluetooth capture on Linux (closes: #737357).
 -- Romain Francoise [email protected]  Mon, 03 Feb 2014 22:03:51 +0100</code></pre></div><div id="comment-37503-info" class="comment-info"><span class="comment-age">(31 Oct '14, 05:16)</span> Jaap ♦</div></div><span id="37516"></span><div id="comment-37516" class="comment"><div id="post-37516-score" class="comment-score"></div><div class="comment-text"><p>I uninstalled Wireshark from the repo and tried to install the latest Wireshark from the website. In the installation instructions, <code>gtk-config --version</code> failed. So I downloaded the latest GTK+ from it's website. To install it, I'll have to install the latest version of 4 more packages I already have. Is this the only way?</p></div><div id="comment-37516-info" class="comment-info"><span class="comment-age">(31 Oct '14, 15:11)</span> GuiRitter</div></div></div><div id="comment-tools-37380" class="comment-tools"></div><div class="clear"></div><div id="comment-37380-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

