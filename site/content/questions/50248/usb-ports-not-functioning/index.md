+++
type = "question"
title = "USB ports not functioning"
description = '''Hello Been using WireShark for years, love it. Went to do some packet capturing today and it was only sniffing the incoming packets, not the outgoing. No big deal, let me uninstall and reinstall. Removed the program completely, including WinPcap and USBPcap. Downloaded a new version, went through th...'''
date = "2016-02-16T16:56:00Z"
lastmod = "2016-02-17T01:07:00Z"
weight = 50248
keywords = [ "usb", "usbpcap" ]
aliases = [ "/questions/50248" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [USB ports not functioning](/questions/50248/usb-ports-not-functioning)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50248-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>Been using WireShark for years, love it. Went to do some packet capturing today and it was only sniffing the incoming packets, not the outgoing. No big deal, let me uninstall and reinstall.</p><p>Removed the program completely, including WinPcap and USBPcap. Downloaded a new version, went through the install, an error popped up that I ignored during the USBPcap install, hit OK, needed to reboot, closed things up, rebooted... All USB devices dead.</p><p>Tried 2 keyboards, 2 mice. No luck. All 4 devices work when plugged into the laptop. The keyboard also works when booting up, but then dies after POST and Win10 takes over. No LED's when using CAPS lock or NUM lock.<br />
</p><p>Since this is an HP Windows 10, I cannot get into safe mode. My only option is to hit ESC for a Startup Menu. There's a System Recovery option in there, but it only brings me back to the logon screen with a dead keyboard and mouse.</p><p>I have no PS2 ports on my system. Does anyone have any ideas or suggestions on how I can recover from this?</p><p>thank you</p></div><div id="question-tags" class="tags-container tags">usb usbpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '16, 16:56</strong></p><img src="https://secure.gravatar.com/avatar/e294b31cf974b24aa87dd2ecfcc2a648?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ean_bw&#39;s gravatar image" /><p>ean_bw<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ean_bw has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-50248" class="comments-container"><span id="50254"></span><div id="comment-50254" class="comment"><div id="post-50254-score" class="comment-score"></div><div class="comment-text"><p>The explanation what has most probably happened is in <a href="https://ask.wireshark.org/questions/50196/wireshark201usb">this Question</a>; the advice what to do on a Win10 system with no other HID but USB is a different matter. Are there any "recovery points" in Win10, as there used to be in older Windows, which could be used to return back to state before you have installed the last Wireshark package? If not, you'll have to boot from a CD or USB flash disk and modify the files/registry on your HDD to get back on track.</p></div><div id="comment-50254-info" class="comment-info"><span class="comment-age">(17 Feb '16, 00:35)</span> sindy</div></div></div><div id="comment-tools-50248" class="comment-tools"></div><div class="clear"></div><div id="comment-50248-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50257"></span>

<div id="answer-container-50257" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50257-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If by chance Remote Desktop has been enabled on that machine, you can login to it remotely.</p><p>If it hasn't, you'll have to boot Windows 10 from a CD/DVD, and it should find out that there is a Win10 installation on the harddisk and allow you to modify it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '16, 01:07</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-50257" class="comments-container"><span id="50264"></span><div id="comment-50264" class="comment"><div id="post-50264-score" class="comment-score"></div><div class="comment-text"><p>Sindy I could kiss you! I love when I get so deep into troubleshooting that I can't see the forest for the trees.</p><p>Connected via RDP, uninstalled USBPcap, rebooted, all good!<br />
</p><p>Yes, you're right, this is more of a Win10 question, but maybe if it happens to someone else and they come looking for help they'll be pleasantly surprised.</p><p>Thank you!</p></div><div id="comment-50264-info" class="comment-info"><span class="comment-age">(17 Feb '16, 05:23)</span> ean_bw</div></div><span id="50265"></span><div id="comment-50265" class="comment"><div id="post-50265-score" class="comment-score"></div><div class="comment-text"><p>Your kiss has been honestly forwarded to the real author of the idea.</p><p>To make the usefulness of the answer visible at first glance, please use the checkmark icon next to it instead of the "thumbs up". The thumbs up raise my karma but do not make the number of answers in the list look green. Nobody else but you can do it.</p></div><div id="comment-50265-info" class="comment-info"><span class="comment-age">(17 Feb '16, 05:43)</span> sindy</div></div></div><div id="comment-tools-50257" class="comment-tools"></div><div class="clear"></div><div id="comment-50257-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

