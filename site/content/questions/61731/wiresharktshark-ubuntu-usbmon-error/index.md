+++
type = "question"
title = "Wireshark/Tshark Ubuntu usbmon error"
description = '''I ran tshark on Ubuntu/Windows 10 as follows $ tshark -i 6 Capturing on &#x27;usbmon1&#x27; tshark: The capture session could not be initiated on interface &#x27;usbmon1&#x27; (Can&#x27;t open USB bus file /sys/kernel/debug/usb/usbmon/1t: Permission denied). Please check to make sure you have sufficient permissions, and tha...'''
date = "2017-06-01T13:25:00Z"
lastmod = "2017-06-04T08:55:00Z"
weight = 61731
keywords = [ "windows", "permissions", "usbmon", "ubuntu" ]
aliases = [ "/questions/61731" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark/Tshark Ubuntu usbmon error](/questions/61731/wiresharktshark-ubuntu-usbmon-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61731-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I ran tshark on Ubuntu/Windows 10 as follows</p><p>$ tshark -i 6</p><p>Capturing on 'usbmon1'</p><p>tshark: The capture session could not be initiated on interface 'usbmon1' (Can't open USB bus file /sys/kernel/debug/usb/usbmon/1t: Permission denied). Please check to make sure you have sufficient permissions, and that you have the proper interface or pipe specified. 0 packets captured</p><p>(I get the same message when I run Wireshark)</p><p>I followed instructions on this web site including "sudo dpkg-reconfigure wireshark-common"; responding "yes", signing off and on. Again I got the same error message.</p><p>WiresharAny idea how to fix this problem?</p><p><strong>Update:</strong> Thank you for the advice that I got from the community</p><p>I was able to handle usbmon as suggested and I got to capture data for it. he way for me to run tshark without errors was by executing it through gksudo.</p><p>gksudo -- tshark -i 1 -l -a duration:30</p><p>The -- between gksudo and tshark are necessary for tshark to interpret the parameters. The only problem is that ^C does not stop the running program</p></div><div id="question-tags" class="tags-container tags">windows permissions usbmon ubuntu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '17, 13:25</strong></p><img src="https://secure.gravatar.com/avatar/3def1eb46dec3558cdfc1067b04f67bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jh2222&#39;s gravatar image" /><p>jh2222<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jh2222 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Jun '17, 06:30</p></div></div><div id="comments-container-61731" class="comments-container"><span id="61732"></span><div id="comment-61732" class="comment"><div id="post-61732-score" class="comment-score"></div><div class="comment-text"><p>What does <code>ls -l /usr/bin/dumpcap</code> print?</p></div><div id="comment-61732-info" class="comment-info"><span class="comment-age">(01 Jun '17, 13:56)</span> Guy Harris ♦♦</div></div><span id="61801"></span><div id="comment-61801" class="comment"><div id="post-61801-score" class="comment-score"></div><div class="comment-text"><p>ls -l /usr/bin/dumpcap -rwxr-xr-- 1 root wireshark 88272 Apr 8 2016 /usr/bin/dumpcap</p></div><div id="comment-61801-info" class="comment-info"><span class="comment-age">(06 Jun '17, 03:20)</span> jh2222</div></div><span id="61803"></span><div id="comment-61803" class="comment"><div id="post-61803-score" class="comment-score"></div><div class="comment-text"><p>You really should not be running tshark (or Wireshark) as root. If you think you have to do that, it simply means you haven't given sufficient capture privileges to your user on the required interfaces.</p></div><div id="comment-61803-info" class="comment-info"><span class="comment-age">(06 Jun '17, 06:52)</span> grahamb ♦</div></div></div><div id="comment-tools-61731" class="comment-tools"></div><div class="clear"></div><div id="comment-61731-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="61769"></span>

<div id="answer-container-61769" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61769-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>On Linux, you need to load the <code>usbmon</code> module (<code>sudo modprobe usbmon</code>) and make the <code>/dev/usbmonX</code> files readable for your user (<code>sudo setfacl -m u:$USER:r /dev/usbmon*</code>). After doing so you can capture USB traffic as a regular user.</p><p>Alternatively you can allow any user that executes the capture process to bypass file permissions (this is done by Arch Linux for example), but might be more risky.</p><pre><code>sudo setcap CAP_DAC_OVERRIDE+eip /usr/bin/dumpcap</code></pre><p>See <a href="https://wiki.wireshark.org/CaptureSetup/USB">https://wiki.wireshark.org/CaptureSetup/USB</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jun '17, 08:55</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Jun '17, 08:56</p></div></div><div id="comments-container-61769" class="comments-container"><span id="61777"></span><div id="comment-61777" class="comment"><div id="post-61777-score" class="comment-score"></div><div class="comment-text"><p>Thank you. It works. So both usbmon1 and usbmon2 capture packets!</p></div><div id="comment-61777-info" class="comment-info"><span class="comment-age">(04 Jun '17, 18:09)</span> jh2222</div></div><span id="61802"></span><div id="comment-61802" class="comment"><div id="post-61802-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-61802-info" class="comment-info"><span class="comment-age">(06 Jun '17, 04:34)</span> grahamb ♦</div></div></div><div id="comment-tools-61769" class="comment-tools"></div><div class="clear"></div><div id="comment-61769-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

