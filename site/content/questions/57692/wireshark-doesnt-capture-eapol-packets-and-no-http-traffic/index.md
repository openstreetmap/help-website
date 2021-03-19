+++
type = "question"
title = "Wireshark doesn&#x27;t capture EAPOL Packets and no HTTP Traffic"
description = '''Hello All: I am having a bit of a problem here with wireshark, no matter what I do or what I try to do Wireshark doesnt capture EAPOL traffic that means no handshake capture which means no decryption of HTTP/TCP traffic. Here are few details that will list out what I exactly did.   Platform: KALI Li...'''
date = "2016-11-29T01:34:00Z"
lastmod = "2016-11-29T03:18:00Z"
weight = 57692
keywords = [ "http", "eapol", "traffic", "tcp" ]
aliases = [ "/questions/57692" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark doesn't capture EAPOL Packets and no HTTP Traffic](/questions/57692/wireshark-doesnt-capture-eapol-packets-and-no-http-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57692-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57692-score" class="post-score" title="current number of votes">0</div><span id="post-57692-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All:</p><p>I am having a bit of a problem here with wireshark, no matter what I do or what I try to do Wireshark doesnt capture EAPOL traffic that means no handshake capture which means no decryption of HTTP/TCP traffic. Here are few details that will list out what I exactly did.</p><ol><li>Platform: KALI Linux running on Virtual Box over Macbook Air</li><li>Wireless Card: TP-Link TL-WN722N</li><li>Wifi is PSK2 - So I have already got the psk key from Wireshark psk calculator, the name of the ssid is Cisco01096 and password is arnold06.</li><li>Added decryption keys in the wireless protocol IEEE 802.11 enabled/disabled Assume FCS etc.</li><li>Started wireshark without airmon running in the background</li><li>Started wireshark with airmon running in the background</li><li>started wireshark with Sudo command (I know its not supposed to be done yet I gave a go)</li><li>started wireshark without Sudo command.</li><li>Reconnected my devices to the wifi so it captures the handshake nothing at all, done every time I start wireshark.</li></ol><p>after doing everything as aforesaid, all I still see is just encrypted packets no EAPOL or HTTP traffic.</p><p>Can someone please guide where am I going wrong?</p><p>Regards, BM</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-eapol" rel="tag" title="see questions tagged &#39;eapol&#39;">eapol</span> <span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Nov '16, 01:34</strong></p><img src="https://secure.gravatar.com/avatar/2b8282719dd40d81fe394a4a94fa1656?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BMC&#39;s gravatar image" /><p><span>BMC</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BMC has no accepted answers">0%</span></p></div></div><div id="comments-container-57692" class="comments-container"></div><div id="comment-tools-57692" class="comment-tools"></div><div class="clear"></div><div id="comment-57692-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57693"></span>

<div id="answer-container-57693" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57693-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57693-score" class="post-score" title="current number of votes">0</div><span id="post-57693-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A couple of points:</p><ol><li>I assume you have seen this, but just to be sure: <a href="https://wiki.wireshark.org/HowToDecrypt802.11">https://wiki.wireshark.org/HowToDecrypt802.11</a></li><li>Share a trace - this will go faster if you post a short trace of what you do get - the people on this site are very good at looking at traces and troubleshooting - without the trace, the community is left to guess. Good place to put a trace for review by the community: <a href="https://www.cloudshark.org/">https://www.cloudshark.org/</a></li><li>I use those adapters all the time to capture traffic and they work fine, so I will hypothesize there is something specific about your setup causing issues</li><li>To get EAPOL frames, you need to have the device re-authenticate. There are a couple of ways to do this: go to the AP or wireless controller and kick the client off. Not all have this feature readily available, but some do. Another way, likely more popular, is to just reboot the device - like a smart phone, laptop, whatever, or disconnect the wifi and reconnect. You need to force the reassociation while capturing to get all four EAPOL packets.</li></ol><p>So the technique I suggest:</p><ol><li>Be sure your capture setup picks up all traffic, both uni- and multi-/broadcast. This should be good with that adapter - I am not aware of any issues. Also check for data frames (or QoS data frames) to be sure there is data to decrypt.</li><li>Start the capture on the correct channel - may need to hunt around to find it. Keep changing channels until you find encrypted frames from the client under test.</li><li>Once you find the client, reboot it. Wait to look for the probes/authentication/association/eapol sequence. If you don't get all four eapol frames, do the whole thing again until you do.</li></ol><p>Also, since you are on a MAC, you can try capturing with the built in adapter on the MAC with Wireshark (supports monitor+promisc mode by default) and see if you pick up the eapol frames if the USB adapter piped into the VM does not. I run Kali on my MAC, but I don't capture traffic this way so can't be 100% sure there is not a VM issue. I know on some of my newer Dell laptops I cannot attach a USB wifi adapter to a VM in VirtualBox for whatever reason. However, in these cases where firmware fails to load, the adapter does not work at all so no frames can be captured. Since you claim to be getting at least something, then this likely is not your issue.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Nov '16, 03:18</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p><span>Bob Jones</span><br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div></div><div id="comments-container-57693" class="comments-container"></div><div id="comment-tools-57693" class="comment-tools"></div><div class="clear"></div><div id="comment-57693-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

