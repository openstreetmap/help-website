+++
type = "question"
title = "Wireshark 2.2.0 freezes during first start after each reboot"
description = '''After upgrading wireshark 2.0.5 to the newest 2.2.0 Wireshark is stuck at the splash screen with 99% and the message &quot;Initializing tab listeners&quot;. I&#x27;m running windows 10 and WinPCAP 4.1.3 Anyone seen this before? Regards Jeppe'''
date = "2016-09-08T07:38:00Z"
lastmod = "2016-09-12T23:58:00Z"
weight = 55394
keywords = [ "wireshark", "stuck", "upgrade", "error", "2.2" ]
aliases = [ "/questions/55394" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 2.2.0 freezes during first start after each reboot](/questions/55394/wireshark-220-freezes-during-first-start-after-each-reboot)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55394-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55394-score" class="post-score" title="current number of votes">0</div><span id="post-55394-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>After upgrading wireshark 2.0.5 to the newest 2.2.0 Wireshark is stuck at the splash screen with 99% and the message "Initializing tab listeners". I'm running windows 10 and WinPCAP 4.1.3 Anyone seen this before? Regards Jeppe</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-stuck" rel="tag" title="see questions tagged &#39;stuck&#39;">stuck</span> <span class="post-tag tag-link-upgrade" rel="tag" title="see questions tagged &#39;upgrade&#39;">upgrade</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span> <span class="post-tag tag-link-2.2" rel="tag" title="see questions tagged &#39;2.2&#39;">2.2</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Sep '16, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/0042ccbcf6f07a360116c59a9b6970bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pixelweb&#39;s gravatar image" /><p><span>Pixelweb</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pixelweb has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Sep '16, 23:50</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-55394" class="comments-container"><span id="55395"></span><div id="comment-55395" class="comment"><div id="post-55395-score" class="comment-score"></div><div class="comment-text"><p>Downgraded back to 2.0.5 and Wireshark is running again.</p></div><div id="comment-55395-info" class="comment-info"><span class="comment-age">(08 Sep '16, 07:56)</span> <span class="comment-user userinfo">Pixelweb</span></div></div><span id="55400"></span><div id="comment-55400" class="comment"><div id="post-55400-score" class="comment-score"></div><div class="comment-text"><p>Do you have any custom plugin installed? If yes, does Wireshark start properly if you remove it?</p></div><div id="comment-55400-info" class="comment-info"><span class="comment-age">(08 Sep '16, 11:25)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div><span id="55403"></span><div id="comment-55403" class="comment"><div id="post-55403-score" class="comment-score"></div><div class="comment-text"><p>As I crashed into the same issue, I've given it some time and I've filed <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12845">Bug 12845</a>. The good news is that it seems that only the first start after reboot is affected, and that if you don't need live capturing from USB, removing <code>USBPcapCMD.exe</code> from the <code>extcap</code> directory probably hides the issue completely.</p></div><div id="comment-55403-info" class="comment-info"><span class="comment-age">(08 Sep '16, 15:47)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="55408"></span><div id="comment-55408" class="comment"><div id="post-55408-score" class="comment-score"></div><div class="comment-text"><p>I am having the same issue and a uninstall and re-install did not fix the issue. I updated from 2.05 64-bit.</p></div><div id="comment-55408-info" class="comment-info"><span class="comment-age">(08 Sep '16, 20:05)</span> <span class="comment-user userinfo">PLCMAN58</span></div></div><span id="55409"></span><div id="comment-55409" class="comment"><div id="post-55409-score" class="comment-score"></div><div class="comment-text"><p>Sindy, THANKS for the suggestion to remove the USBCAPCMD.EXE file from the extcap directory. I had to reboot the computer to remove the file and I can now launch Wireshark and Wireshark Legacy 64-bit without it hanging.</p><p>I currently do not do much capturing from USB and will wait for the next release for a possible long term fix.</p></div><div id="comment-55409-info" class="comment-info"><span class="comment-age">(08 Sep '16, 20:18)</span> <span class="comment-user userinfo">PLCMAN58</span></div></div><span id="55428"></span><div id="comment-55428" class="comment not_top_scorer"><div id="post-55428-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@Pixelweb</span>, <span>@PLCMAN58</span>, could you please help localize the issue?</p><p>Open the plain command shell (not Powershell!), go to the directory where USBPcap is installed (if default installation paths are used, it is <code>C:\Program Files\USBPcap</code>), and issue the following commands:</p><p><code>USBPcapCMD --extcap-interfaces</code></p><p>This should list something similar to the following:</p><p><code>interface {value=\\.\USBPcap1}{display=USBPcap1} interface {value=\\.\USBPcap2}{display=USBPcap2}</code></p><p>Then, for each <code>\\.\USBPcapX</code> you get as a <code>value</code> on your system, issue a command</p><p><code>c:\Program Files\USBPcap&gt;USBPcapCMD.exe --extcap-config --extcap-interface \\.\USBPcapX</code> (replacing the last X with 1 .. whatever the number of root hubs in your system), and paste the complete output of all of them to a Comment here?</p><p>An example output for</p><p><code>c:\Program Files\USBPcap&gt;USBPcapCMD.exe --extcap-config --extcap-interface \\.\USBPcap3</code></p><p>on my system is:</p><p><code>arg {number=0}{call=--snaplen}{display=Snapshot length}{tooltip=Snapshot length}{type=integer}{range=0,65535}{default=65535} arg {number=1}{call=--bufferlen}{display=Capture buffer length}{tooltip=USBPcap kernel-mode capture buffer length in bytes}{type=integer}{range=0,134217728}{default=1048576} arg {number=2}{call=--capture-from-all-devices}{display=Capture from all devices connected}{tooltip=Capture from all devices connected despite other options}{type=boolflag}{default=true} arg {number=3}{call=--capture-from-new-devices}{display=Capture from newly connected devices}{tooltip=Automatically start capture on all newly connected devices}{type=boolflag}{default=true} arg {number=99}{call=--devices}{display=Attached USB Devices}{tooltip=Select individual devices to capture from}{type=multicheck} value {arg=99}{value=1}{display=[1] Obecn├Ż rozbo─Źova─Ź USB}{enabled=true}</code></p><p>Yours may be much longer at least for one of the <code>\\.\USBPcapX</code>.</p><p><span></span><span>@Pixelweb</span>, you don't need to reinstall back to 2.2.0 if you haven't yet, the result of the USBPcap which came along the 2.0.5 will provide the necessary information as well.</p></div><div id="comment-55428-info" class="comment-info"><span class="comment-age">(09 Sep '16, 04:00)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="55429"></span><div id="comment-55429" class="comment not_top_scorer"><div id="post-55429-score" class="comment-score"></div><div class="comment-text"><p><span>@sindy</span> I get the error no matter if USBPcap is installed or not. Currnetly my C:\ProgramFiles\USBPcap-directory is present but completely empty Regards Jeppe</p></div><div id="comment-55429-info" class="comment-info"><span class="comment-age">(09 Sep '16, 05:26)</span> <span class="comment-user userinfo">Pixelweb</span></div></div><span id="55430"></span><div id="comment-55430" class="comment not_top_scorer"><div id="post-55430-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@Pixelweb</span>, please check the contents of your <code>C:\Program Files\Wireshark\extcap</code> directory. If there is something, let me know what it is, rename the whole <code>extcap</code> directory to something like <code>extcap_x</code> and create an empty <code>extcap</code> one next to it, and then try running Wireshark 2.2.0 again. I'm afraid the uninstall doesn't always tidy up completely. Hiding the original <code>extcap</code> directory from Wireshark by renaming it should eliminate any hangovers.</p></div><div id="comment-55430-info" class="comment-info"><span class="comment-age">(09 Sep '16, 05:50)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="55432"></span><div id="comment-55432" class="comment not_top_scorer"><div id="post-55432-score" class="comment-score"></div><div class="comment-text"><p><span>@sindy</span>, c:\program files\wireshark\extcab contains one file: USBPcapCMD.exe I have renamed extcap dir to extcap_x and created a new dir called extcab which is empty.</p><p>I uninstalled wireshark 2.0.5 and installen version 2.2.0 - without installing the USBPcap driver. During the installation I was asked if I wanted to uninstall 2.0.5 first which I accepted.</p><p>When the 2.2.0 install was complete the extcap_x dir was still present but the empty extcab dir was gone.</p><p>Now version 2.2.0 opens up fine both the new GUI and the Legacy version.</p><p>Thanks for your help :-) Best regards Jeppe</p></div><div id="comment-55432-info" class="comment-info"><span class="comment-age">(09 Sep '16, 06:17)</span> <span class="comment-user userinfo">Pixelweb</span></div></div><span id="55433"></span><div id="comment-55433" class="comment not_top_scorer"><div id="post-55433-score" class="comment-score"></div><div class="comment-text"><p><span>@Pixelweb</span>, I'm glad it has helped you, but now please help the development team by following the steps I've given above, using the <code>USBPcapCMD.exe</code> located in your extcap_x directory :-)</p></div><div id="comment-55433-info" class="comment-info"><span class="comment-age">(09 Sep '16, 06:20)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="55434"></span><div id="comment-55434" class="comment not_top_scorer"><div id="post-55434-score" class="comment-score"></div><div class="comment-text"><p><span></span><span>@sindy</span>, Sorry :-) Here it comes:</p><pre><code>c:\Program Files\Wireshark\extcap_x&gt;USBPcapCMD --extcap-interfaces

c:\Program Files\Wireshark\extcap_x&gt;interface {value=\\.\USBPcap1}{display=USBPcap1}
interface {value=\\.\USBPcap2}{display=USBPcap2}

c:\Program Files\Wireshark\extcap_x&gt;USBPcapCMD.exe --extcap-config --extcap-interface \\.\USBPcap1

c:\Program Files\Wireshark\extcap_x&gt;arg {number=0}{call=--snaplen}{display=Snapshot length}{tooltip=Snapshot length}{type=integer}{range=0,65535}{default=65535}
arg {number=1}{call=--bufferlen}{display=Capture buffer length}{tooltip=USBPcap kernel-mode capture buffer length in bytes}{type=integer}{range=0,134217728}{default=1048576}
arg {number=2}{call=--capture-from-all-devices}{display=Capture from all devices connected}{tooltip=Capture from all devices connected despite other options}{type=boolflag}{default=true}
arg {number=3}{call=--capture-from-new-devices}{display=Capture from newly connected devices}{tooltip=Automatically start capture on all newly connected devices}{type=boolflag}{default=true}
arg {number=99}{call=--devices}{display=Attached USB Devices}{tooltip=Select individual devices to capture from}{type=multicheck}
value {arg=99}{value=5}{display=[5] Generic USB Hub}{enabled=true}
value {arg=99}{value=1}{display=[1] Intel(R) Wireless Bluetooth(R)}{enabled=true}{parent=5}
value {arg=99}{value=1_1}{display=Microsoft Bluetooth LE Enumerator}{enabled=false}{parent=1}
value {arg=99}{value=1_2}{display=Bluetooth Device (RFCOMM Protocol TDI)}{enabled=false}{parent=1}
value {arg=99}{value=1_3}{display=Microsoft Bluetooth Enumerator}{enabled=false}{parent=1}
value {arg=99}{value=1_4}{display=Bluetooth HID Device}{enabled=false}{parent=1_3}
value {arg=99}{value=1_5}{display=HID-compliant mouse}{enabled=false}{parent=1_4}
value {arg=99}{value=1_6}{display=Device Identification Service}{enabled=false}{parent=1_3}
value {arg=99}{value=1_7}{display=Jeppe SchoubyeÔÇÖs Mouse #1}{enabled=false}{parent=1_3}
value {arg=99}{value=1_8}{display=Bluetooth Device (Personal Area Network)}{enabled=false}{parent=1}
value {arg=99}{value=2}{display=[2] USB Composite Device}{enabled=true}{parent=5}
value {arg=99}{value=2_1}{display=Integrated Webcam}{enabled=false}{parent=2}
value {arg=99}{value=3}{display=[3] USB Composite Device}{enabled=true}{parent=5}
value {arg=99}{value=3_1}{display=Dell ControlVault w/ Fingerprint Swipe Sensor}{enabled=false}{parent=3}
value {arg=99}{value=3_2}{display=Control Vault w/ Fingerprint Swipe Sensor}{enabled=false}{parent=3_1}
value {arg=99}{value=3_3}{display=Broadcom Usbccid Smartcard Reader (WUDF)}{enabled=false}{parent=3}
value {arg=99}{value=3_4}{display=Smart card filter driver}{enabled=false}{parent=3_3}
value {arg=99}{value=3_5}{display=Broadcom Usbccid Smartcard Reader (WUDF)}{enabled=false}{parent=3}
value {arg=99}{value=3_6}{display=Smart card filter driver}{enabled=false}{parent=3_5}
value {arg=99}{value=3_7}{display=NFC USB Bus Driver}{enabled=false}{parent=3}
value {arg=99}{value=3_8}{display=NFC Proximity Provider}{enabled=false}{parent=3_7}

c:\Program Files\Wireshark\extcap_x&gt;USBPcapCMD.exe --extcap-config --extcap-interface \\.\USBPcap2

c:\Program Files\Wireshark\extcap_x&gt;arg {number=0}{call=--snaplen}{display=Snapshot length}{tooltip=Snapshot length}{type=integer}{range=0,65535}{default=65535}
arg {number=1}{call=--bufferlen}{display=Capture buffer length}{tooltip=USBPcap kernel-mode capture buffer length in bytes}{type=integer}{range=0,134217728}{default=1048576}
arg {number=2}{call=--capture-from-all-devices}{display=Capture from all devices connected}{tooltip=Capture from all devices connected despite other options}{type=boolflag}{default=true}
arg {number=3}{call=--capture-from-new-devices}{display=Capture from newly connected devices}{tooltip=Automatically start capture on all newly connected devices}{type=boolflag}{default=true}
arg {number=99}{call=--devices}{display=Attached USB Devices}{tooltip=Select individual devices to capture from}{type=multicheck}
value {arg=99}{value=21}{display=[21] Generic USB Hub}{enabled=true}
value {arg=99}{value=24}{display=[24] USB Composite Device}{enabled=true}{parent=21}
value {arg=99}{value=24_1}{display=USB Input Device}{enabled=false}{parent=24}
value {arg=99}{value=24_2}{display=HID Keyboard Device}{enabled=false}{parent=24_1}
value {arg=99}{value=24_3}{display=USB Input Device}{enabled=false}{parent=24}
value {arg=99}{value=24_4}{display=HID-compliant consumer control device}{enabled=false}{parent=24_3}
value {arg=99}{value=24_5}{display=HID-compliant vendor-defined device}{enabled=false}{parent=24_3}
value {arg=99}{value=19}{display=[19] Generic USB Hub}{enabled=true}
value {arg=99}{value=22}{display=[22] Logitech USB Camera (Pro 9000)}{enabled=true}{parent=19}
value {arg=99}{value=22_1}{display=Logitech QuickCam Pro 9000}{enabled=false}{parent=22}
value {arg=99}{value=22_2}{display=Pro 9000}{enabled=false}{parent=22}
value {arg=99}{value=22_3}{display=Microphone (Pro 9000)}{enabled=false}{parent=22_2}
value {arg=99}{value=25}{display=[25] USB Composite Device}{enabled=true}{parent=19}
value {arg=99}{value=25_1}{display=Jabra PRO 9470}{enabled=false}{parent=25}
value {arg=99}{value=25_2}{display=Headset Microphone (Jabra PRO 9470)}{enabled=false}{parent=25_1}
value {arg=99}{value=25_3}{display=Headset Earphone (Jabra PRO 9470)}{enabled=false}{parent=25_1}
value {arg=99}{value=25_4}{display=USB Input Device}{enabled=false}{parent=25}
value {arg=99}{value=25_5}{display=HID-compliant headset}{enabled=false}{parent=25_4}
value {arg=99}{value=25_6}{display=HID-compliant vendor-defined device}{enabled=false}{parent=25_4}
value {arg=99}{value=25_7}{display=HID-compliant consumer control device}{enabled=false}{parent=25_4}
value {arg=99}{value=23}{display=[23] USB Composite Device}{enabled=true}{parent=19}
value {arg=99}{value=23_1}{display=USB Input Device (Logitech Download Assistant)}{enabled=false}{parent=23}
value {arg=99}{value=23_2}{display=HID Keyboard Device}{enabled=false}{parent=23_1}
value {arg=99}{value=23_3}{display=USB Input Device}{enabled=false}{parent=23}
value {arg=99}{value=23_4}{display=HID-compliant mouse}{enabled=false}{parent=23_3}
value {arg=99}{value=23_5}{display=HID-compliant consumer control device}{enabled=false}{parent=23_3}
value {arg=99}{value=23_6}{display=HID-compliant system controller}{enabled=false}{parent=23_3}
value {arg=99}{value=23_7}{display=HID-compliant vendor-defined device}{enabled=false}{parent=23_3}
value {arg=99}{value=23_8}{display=USB Input Device}{enabled=false}{parent=23}
value {arg=99}{value=23_9}{display=HID-compliant vendor-defined device}{enabled=false}{parent=23_8}
value {arg=99}{value=23_10}{display=HID-compliant vendor-defined device}{enabled=false}{parent=23_8}
value {arg=99}{value=23_11}{display=HID-compliant vendor-defined device}{enabled=false}{parent=23_8}
value {arg=99}{value=9}{display=[9] Sierra Wireless USB Composite Device}{enabled=true}
value {arg=99}{value=9_1}{display=Dell Wireless 5809e GobiÔäó 4G LTE Mobile Broadband Card}{enabled=false}{parent=9}
value {arg=99}{value=9_2}{display=SMS_DEVICE2_{E8153BDB-9380-4359-A948-4B1D4C45D67C}}{enabled=false}{parent=9_1}
value {arg=99}{value=9_3}{display=Mobile Broadband Firmware Device}{enabled=false}{parent=9_1}
value {arg=99}{value=20}{display=[20] Generic SuperSpeed USB Hub}{enabled=true}</code></pre><p>Regards Jeppe</p></div><div id="comment-55434-info" class="comment-info"><span class="comment-age">(09 Sep '16, 06:28)</span> <span class="comment-user userinfo">Pixelweb</span></div></div></div><div id="comment-tools-55394" class="comment-tools"><span class="comments-showing"> showing 5 of 11 </span> <a href="#" class="show-all-comments-link">show 6 more comments</a></div><div class="clear"></div><div id="comment-55394-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55512"></span>

<div id="answer-container-55512" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55512-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55512-score" class="post-score" title="current number of votes">0</div><span id="post-55512-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The issue affects only users who have installed USBPcap (or, possibly, also those who run their own extcap applications) and who have a lot of USB and/or bluetooth devices connected. The behaviour is explained in detail in <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12845">Bug 12845</a>. If you are affected, you are welcome to help resolve the bug by following the instructions given in the comments to the Question and contribute the information directly to the bugzilla or as another Comment here.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Sep '16, 23:58</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-55512" class="comments-container"></div><div id="comment-tools-55512" class="comment-tools"></div><div class="clear"></div><div id="comment-55512-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

