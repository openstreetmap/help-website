+++
type = "question"
title = "Can Wireshark be installed on a Raspberry Pi running Windows 10 IoT Core?"
description = '''This is what I have, and this is what I have tried: Hardware: Raspberry Pi 2 Model B OS: Windows 10 IoT Core Build 10.0.10240 Driver: WinPcap Version 4.1.3 (installed and verified via DevCon.exe command) Environment:  Remote PowerShell session Install files attempted: Wireshark-win32-1.12.7.exe, Wir...'''
date = "2015-10-08T09:58:00Z"
lastmod = "2015-10-08T14:25:00Z"
weight = 46422
keywords = [ "windows", "raspberry", "arm" ]
aliases = [ "/questions/46422" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can Wireshark be installed on a Raspberry Pi running Windows 10 IoT Core?](/questions/46422/can-wireshark-be-installed-on-a-raspberry-pi-running-windows-10-iot-core)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46422-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This is what I have, and this is what I have tried:</p><p>Hardware: Raspberry Pi 2 Model B</p><p>OS: Windows 10 IoT Core Build 10.0.10240</p><p>Driver: WinPcap Version 4.1.3 (installed and verified via DevCon.exe command)</p><p>Environment: Remote PowerShell session</p><p>Install files attempted: Wireshark-win32-1.12.7.exe, Wireshark-win64-1.12.7.exe, WiresharkPortable-1.12.7.paf.exe</p><p>Command used: start [setupFilePath\setupFileName] /S</p><p>Results: This command cannot be run due to the error: This version of %1 is not compatible with the version of Windows you're running. Check your computer's system information and then contact the software publisher. + CategoryInfo : InvalidOperation: (:) [Start-Process], InvalidOperationException + FullyQualifiedErrorId : InvalidOperationException,Microsoft.PowerShell.Commands.StartProcessCommand</p><p>If anyone knows how to install Wireshark on Windows 10 IoT Core (loaded on RPi2), please help me accomplish this.</p><p>Is there a way to install just TShark through command line?</p></div><div id="question-tags" class="tags-container tags">windows raspberry arm</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Oct '15, 09:58</strong></p><img src="https://secure.gravatar.com/avatar/b7af5749249abc686438721de5bf81d1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="areue&#39;s gravatar image" /><p>areue<br />
<span class="score" title="5 reputation points">5</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="areue has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Oct '15, 14:27</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-46422" class="comments-container"><span id="50167"></span><div id="comment-50167" class="comment"><div id="post-50167-score" class="comment-score"></div><div class="comment-text"><p>I'm curios to know where you found the following?</p><p>Driver: WinPcap Version 4.1.3 (installed and verified via DevCon.exe command)</p><p>I've got the need for WinPcap for Win10 IoT, but I've not found this available anywhere yet. I'm tempted to hack the build scripts to build my own copy, but if this has already been done by somebody I'd prefer to use what works.</p></div><div id="comment-50167-info" class="comment-info"><span class="comment-age">(12 Feb '16, 14:43)</span> decanio</div></div></div><div id="comment-tools-46422" class="comment-tools"></div><div class="clear"></div><div id="comment-46422-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46424"></span>

<div id="answer-container-46424" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46424-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><a href="https://www.raspberrypi.org/help/faqs/#generalSoCUsed">Question 22 in the Raspberry Pi FAQ</a> is answered:</p><blockquote><p>All versions and revisions of the Raspberry Pi other than the Raspberry Pi 2B use the Broadcom BCM2835. This contains an ARM1176JZFS with floating point, running at 700Mhz, and a Videocore 4 GPU. The GPU is capable of Blu-Ray-quality playback, using H.264 at 40MBits/s. It has a fast 3D core accessed using the supplied OpenGL ES2.0 and OpenVG libraries. The Model 2B uses the Broadcom BCM2836. This contains a quad-core ARM Cortex-a7 processor with floating point &amp; NEON, running at 900MHz, and the same Videocore 4 GPU that is in the other models of Raspberry Pi.</p></blockquote><p>Note the repeated appearance of the string "ARM" and the complete lack of the strings "x86", "x64", "AMD64", or "x86-64".</p><p><a href="https://buildbot.wireshark.org/wireshark-1.12/waterfall">The Wireshark 1.12 buildbot</a> has builders for:</p><ul><li><a href="https://buildbot.wireshark.org/wireshark-1.12/builders/Windows%207%20x64">x64, with the builder running on Windows 7</a>;</li><li><a href="https://buildbot.wireshark.org/wireshark-1.12/builders/Windows%208.1%20x86">x86, with the builder running on Windows 8.1</a></li></ul><p>Note the complete lack of the string "ARM" on the main buildbot page.</p><p>So <em>NO</em> version of Wireshark, as built by the Wireshark buildbots, is capable of running on a Raspberry Pi, or any other ARM-based machine, <em>if</em> it's running Windows. (There are probably ARM Linuxes for which there are Wireshark builds, but we don't do those builds.) "This version of %1 is not compatible with the version of Windows you're running." means that the ".exe" files are x86 or x64 binaries and the version of Windows you're running is, by virtue of running on an ARM processor, incapable of running that binary. (And, no, this isn't a Wireshark vs. TShark issue - both the Wireshark and TShark binaries are x86/x64 binaries in the Wireshark builds, so <em>neither</em> of them will work on your RPi.)</p><p>We would have to add a buildbot to build a version of Wireshark for ARM Windows in order for there to be a version of Wireshark that could be installed on a Raspberry Pi running Windows. But, first, there would have to be a WinPcap build for ARM as well, unless you're willing to run Wireshark or TShark without it being able to capture any network traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '15, 14:25</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Oct '15, 14:27</p></div></div><div id="comments-container-46424" class="comments-container"></div><div id="comment-tools-46424" class="comment-tools"></div><div class="clear"></div><div id="comment-46424-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

