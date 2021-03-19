+++
type = "question"
title = "Wireless Phones? Android devices, iPhones can wireshark help?"
description = '''Hello, I am looking for a software that I can install on my PC, connect an Android device or iPhone to the PC, and the software will tell me what data is being transfered between the wireless device and the wireless carrier. For instance an iPhone is connected and it will show the applications and p...'''
date = "2011-03-17T08:59:00Z"
lastmod = "2011-03-17T10:21:00Z"
weight = 2904
keywords = [ "wireless", "phones", "android", "iphone", "mobile" ]
aliases = [ "/questions/2904" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireless Phones? Android devices, iPhones can wireshark help?](/questions/2904/wireless-phones-android-devices-iphones-can-wireshark-help)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2904-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am looking for a software that I can install on my PC, connect an Android device or iPhone to the PC, and the software will tell me what data is being transfered between the wireless device and the wireless carrier.</p><p>For instance an iPhone is connected and it will show the applications and packet trasfers between AT&amp;T network and the device.</p><p>Or an Android connected to Verizon will show the applications and packet...</p><p>Will WireShark do this? Any help would be greatly appreciated!</p></div><div id="question-tags" class="tags-container tags">wireless phones android iphone mobile</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Mar '11, 08:59</strong></p><img src="https://secure.gravatar.com/avatar/c5211f297decacd9b68cc41b3e620189?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ppercy&#39;s gravatar image" /><p>ppercy<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ppercy has no accepted answers">0%</span></p></div></div><div id="comments-container-2904" class="comments-container"></div><div id="comment-tools-2904" class="comment-tools"></div><div class="clear"></div><div id="comment-2904-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2905"></span>

<div id="answer-container-2905" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2905-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you jailbreak your iphone or root the Android you'll be able to ssh into your phone and capture traffic. Interface towards the carrier network it's usually some sort of PPP connection from the OS to baseband processor. You can run tcpdump or tshark on such interface and either save it as pcap file on the phone or pump the data out via ssh session to be fed into wireshark directly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Mar '11, 10:21</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p>izopizo<br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div></div><div id="comments-container-2905" class="comments-container"><span id="2910"></span><div id="comment-2910" class="comment"><div id="post-2910-score" class="comment-score"></div><div class="comment-text"><p>Thank you! I appreciate the help!</p></div><div id="comment-2910-info" class="comment-info"><span class="comment-age">(17 Mar '11, 13:56)</span> ppercy</div></div><span id="2915"></span><div id="comment-2915" class="comment"><div id="post-2915-score" class="comment-score"></div><div class="comment-text"><p>If you run tcpdump on the phone, use "-w" so that it writes out a pcap file <em>and</em> use "-s 0" so that it has a large snapshot length and doesn't cut off packets at 68 or 96 bytes. (I think one of the packages available for jailbroken iPhones includes tcpdump; I don't know of any package with *shark. I don't know whether there's a tcpdump-for-Android out there, but I wouldn't be surprised if there were; I doubt there's a *shark for Android.)</p></div><div id="comment-2915-info" class="comment-info"><span class="comment-age">(17 Mar '11, 17:54)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-2905" class="comment-tools"></div><div class="clear"></div><div id="comment-2905-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

