+++
type = "question"
title = "Unable to capture wireless traffic on monitor mode on Ubuntu 10.04 version"
description = '''I have been trying to capture the wireless traffic using old wireless cards (Trendnet, TP-Link) etc.  But am unable to capture the traffic other than my own. Can someone please guide as to how to set up the wireshark to capture on monitor mode (including how to set up the wireless card). I have trie...'''
date = "2013-10-23T23:53:00Z"
lastmod = "2013-10-28T08:29:00Z"
weight = 26347
keywords = [ "wireless", "capture", "wireshark", "ubuntu" ]
aliases = [ "/questions/26347" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Unable to capture wireless traffic on monitor mode on Ubuntu 10.04 version](/questions/26347/unable-to-capture-wireless-traffic-on-monitor-mode-on-ubuntu-1004-version)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26347-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have been trying to capture the wireless traffic using old wireless cards (Trendnet, TP-Link) etc. But am unable to capture the traffic other than my own. Can someone please guide as to how to set up the wireshark to capture on monitor mode (including how to set up the wireless card). I have tried implementing suggestion from various bogs and forums and am yet to get the required results. I am using a Belkin wireless router and enabled the WPA-WPA2 personal. and have set it on a channel.</p></div><div id="question-tags" class="tags-container tags">wireless capture wireshark ubuntu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Oct '13, 23:53</strong></p><img src="https://secure.gravatar.com/avatar/c930bfdb6dd68a43136fc6bf6abc408b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kartzoft&#39;s gravatar image" /><p>Kartzoft<br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kartzoft has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 15 Sep '14, 22:35</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-26347" class="comments-container"></div><div id="comment-tools-26347" class="comment-tools"></div><div class="clear"></div><div id="comment-26347-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26468"></span>

<div id="answer-container-26468" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26468-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please try the following steps:</p><p>Run the following commands</p><blockquote><p>ifconfig -a</p></blockquote><p>Do you see a wlan0 or wlan1 interface?</p><p><strong>If no</strong>, your wireless card is <strong>not recognized by your kernel</strong> and there is nothing Wireshark can do about it. <strong>Stop here</strong> and ask the the people in the user forum of your Linux distribution (Ubuntu, Fedora, etc.) how to add a working driver for your wireless card.</p><p>If you <strong>do see wlan0/1, proceed</strong> with</p><blockquote><p>sudo airmon-ng start wlan0<br />
</p></blockquote><p>or</p><blockquote><p>sudo airmon-ng start wlan1<br />
</p></blockquote><p>depending on which wireless interface you want to capture. That command should report the following message:</p><blockquote><p>monitor mode enabled on <strong>mon0</strong></p></blockquote><p>Now, capture on mon0 with tcpdump and/or dumpcap.</p><blockquote><p>sudo tcpdump -ni mon0 -w /var/tmp/wlan.pcap</p></blockquote><p>or</p><blockquote><p>sudo dumpcap -ni mon0 -w /var/tmp/wlan.pcap</p></blockquote><p>Then open that file with Wireshark</p><blockquote><p>wireshark -nr /var/tmp/wlan.pcap</p></blockquote><p>If any of the above does not work, please post the <strong>exact</strong> error message as a <strong>comment</strong> to my answer.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '13, 08:29</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-26468" class="comments-container"><span id="26509"></span><div id="comment-26509" class="comment"><div id="post-26509-score" class="comment-score"></div><div class="comment-text"><p>Hey Kurt,</p><p>Thanks a lot. Am able to capture now. :)</p></div><div id="comment-26509-info" class="comment-info"><span class="comment-age">(29 Oct '13, 06:10)</span> Kartzoft</div></div><span id="26527"></span><div id="comment-26527" class="comment"><div id="post-26527-score" class="comment-score"></div><div class="comment-text"><p>Hey Kurt,</p><p>After capturing the traffic, how do I do a wireless decryption by entering the keys?</p></div><div id="comment-26527-info" class="comment-info"><span class="comment-age">(29 Oct '13, 21:16)</span> Kartzoft</div></div><span id="26528"></span><div id="comment-26528" class="comment"><div id="post-26528-score" class="comment-score"></div><div class="comment-text"><p>as described in the Wiki</p><blockquote><p><a href="https://www.google.com/?q=wireshark+wireless+decryption">https://www.google.com/?q=wireshark+wireless+decryption</a></p></blockquote></div><div id="comment-26528-info" class="comment-info"><span class="comment-age">(30 Oct '13, 00:08)</span> Kurt Knochner ♦</div></div><span id="27194"></span><div id="comment-27194" class="comment"><div id="post-27194-score" class="comment-score"></div><div class="comment-text"><p>Hey Kurt,</p><p>After the decryption am still unable to view the IP address. I followed the steps in the wiki. Is there any other alternatives? However when I switch off the security mode of my WLAN (Belkin) and capture am able to see the proper trace along with the IPs.</p></div><div id="comment-27194-info" class="comment-info"><span class="comment-age">(20 Nov '13, 22:13)</span> Kartzoft</div></div><span id="27200"></span><div id="comment-27200" class="comment"><div id="post-27200-score" class="comment-score">1</div><div class="comment-text"><p>One part of <a href="http://wiki.wireshark.org/HowToDecrypt802.11">the page to which Kurt was referring</a> that's a bit obscure is</p><blockquote><p>WPA and WPA2 use keys derived from an EAPOL handshake to encrypt traffic. Unless all four handshake packets are present for the session you're trying to decrypt, Wireshark won't be able to decrypt the traffic.</p></blockquote><p>In order to capture that handshake, you might have to disconnect all the hosts you care about from the network and re-connect them; for devices that can sleep and wake up, putting them to sleep and waking them up (closing and reopening the lid on a laptop, "turning off" a smartphone or tablet and turning it back on again), and, for other devices, turning off the Wi-Fi and turning it back on again, might do the job.</p><p>Yes, this is a pain, but, remember, the <em>whole point of WEP and WPA/WPA2</em> is to make it <em>hard</em> to sniff a wireless network (i.e., to make it hard for others to snoop your traffic, but that also makes it hard for you to snoop your own traffic). A side-effect of making your network more secure against other people is that it's also more secure against you....</p></div><div id="comment-27200-info" class="comment-info"><span class="comment-age">(21 Nov '13, 00:42)</span> Guy Harris ♦♦</div></div><span id="27547"></span><div id="comment-27547" class="comment not_top_scorer"><div id="post-27547-score" class="comment-score"></div><div class="comment-text"><p>I have no error, but is captured only my traffic (where stands the program) how do whatever and other notebooks seen traffic?</p><p>step</p><p>sudo airmon-ng start wlan 1</p><p>sudo dumpcap -ni mon0 -w /var/tmp/wlan.pcap</p><p>wireshark -nr /var/tmp/wlan.pcap</p><p>after opening only seen my traffic</p></div><div id="comment-27547-info" class="comment-info"><span class="comment-age">(28 Nov '13, 21:05)</span> Sokolov Andrey</div></div><span id="61631"></span><div id="comment-61631" class="comment not_top_scorer"><div id="post-61631-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt Knochner and Guy Harris,</p><p>My problem is I cannot decrypt the captured data using WireShark, even though I captured full 4 EAPOL handshakes.</p><p>I posted my problem here, and I need your helps</p><p><a href="https://ask.wireshark.org/questions/61469/unable-to-decrypt-wifi-data">https://ask.wireshark.org/questions/61469/unable-to-decrypt-wifi-data</a></p><p>Can you look for a while and give me some direction to solve the problem</p><p>Look forward to hearing you,</p><p>Thanks, --Will</p></div><div id="comment-61631-info" class="comment-info"><span class="comment-age">(25 May '17, 21:26)</span> dknovo</div></div><span id="61634"></span><div id="comment-61634" class="comment not_top_scorer"><div id="post-61634-score" class="comment-score"></div><div class="comment-text"><p><a href="https://ask.wireshark.org/users/31939/dknovo">@dknovo</a></p><p>Please don't cross post on another very old question, it won't help get answers to your issue.</p></div><div id="comment-61634-info" class="comment-info"><span class="comment-age">(26 May '17, 02:04)</span> grahamb ♦</div></div></div><div id="comment-tools-26468" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-26468-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

