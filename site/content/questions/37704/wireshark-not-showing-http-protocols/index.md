+++
type = "question"
title = "Wireshark not showing HTTP protocols"
description = '''I&#x27;ve been struggling with this problem for some time now and can&#x27;t seem to find a solution. Please help! I&#x27;m using wireshark to collect the packets on my WLAN, but I&#x27;m not getting any HTTP packets.  The capture device is wlan0 and/or mon0 (depending on whether im using monitor mode) and it doesn&#x27;t m...'''
date = "2014-11-08T12:35:00Z"
lastmod = "2014-11-09T14:08:00Z"
weight = 37704
keywords = [ "http", "wlan0", "protocols", "wireshark" ]
aliases = [ "/questions/37704" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark not showing HTTP protocols](/questions/37704/wireshark-not-showing-http-protocols)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37704-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37704-score" class="post-score" title="current number of votes">0</div><span id="post-37704-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I've been struggling with this problem for some time now and can't seem to find a solution. Please help!</p><p>I'm using wireshark to collect the packets on my WLAN, but I'm not getting any HTTP packets.</p><p>The capture device is wlan0 and/or mon0 (depending on whether im using monitor mode) and it doesn't matter if it's set to promiscuous mode, because all I'm getting is DHCPv6, SSDP, LLMNR (and 802.11 when monitor mode is on while using mon0).</p><p>Why can't my computer find HTTP protocols with data packets? Please help me :\ I'll be happy to post additional info if needed.</p><p>edit: I'm using Kali linux</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-wlan0" rel="tag" title="see questions tagged &#39;wlan0&#39;">wlan0</span> <span class="post-tag tag-link-protocols" rel="tag" title="see questions tagged &#39;protocols&#39;">protocols</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '14, 12:35</strong></p><img src="https://secure.gravatar.com/avatar/9d9c6e7bc447f5f6a5395f6ce8c21d0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="whiteiswhite&#39;s gravatar image" /><p><span>whiteiswhite</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="whiteiswhite has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Nov '14, 12:42</strong> </span></p></div></div><div id="comments-container-37704" class="comments-container"><span id="37708"></span><div id="comment-37708" class="comment"><div id="post-37708-score" class="comment-score"></div><div class="comment-text"><p>When you're not in monitor mode, is <em>the machine running Wireshark</em> sending or receiving any HTTP traffic? What happens if you start a Web browser on that machine or use curl to fetch a page from some site?</p></div><div id="comment-37708-info" class="comment-info"><span class="comment-age">(08 Nov '14, 20:46)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="37714"></span><div id="comment-37714" class="comment"><div id="post-37714-score" class="comment-score"></div><div class="comment-text"><p>First of all thank you very much for your reply!</p><p>When I'm not in monitor mode the machine running Wireshark doesn't receive or send any HTTP traffic. Now that you've mentioned starting a Web browser on that machine I see some HTTP packets being received, where source is the address of the requested website (in this case google.com[173.194.113.67]) and destination IP is the internal IP address of the computer running Wireshark (192.168.x.xx). I'm sorry but I don't understand the "curl to fetch a page from some site" :. I can send you some screenshots if you are willing to help further. Once again thank you very much for the reply!</p></div><div id="comment-37714-info" class="comment-info"><span class="comment-age">(09 Nov '14, 13:36)</span> <span class="comment-user userinfo">whiteiswhite</span></div></div></div><div id="comment-tools-37704" class="comment-tools"></div><div class="clear"></div><div id="comment-37704-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37715"></span>

<div id="answer-container-37715" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37715-score" class="post-score" title="current number of votes">1</div><span id="post-37715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="whiteiswhite has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As I suspected.</p><p>If you're not in monitor mode, the Wi-Fi adapter will see only traffic sent to and from your machine. However, that traffic will, if it has been encrypted at the 802.11 layer, have been decrypted by the Wi-Fi adapter. The packets you were seeing were probably mostly broadcast or multicast traffic, which your machine would see even if it weren't sending <em>any</em> requests out on the network.</p><p>If you <em>are</em> in monitor mode, the Wi-Fi adapter will see whatever traffic its radio receives; however, unless that traffic is to or from your machine, it will, if has been encrypted at the 802.11 layer, <em>not</em> be decrypted by the adapter (and I'm not sure whether traffic to and from the host will be decrypted).</p><p>A "protected" Wi-Fi network is a network that's using WEP or WPA/WPA2; on that network, traffic is encrypted, in a deliberate attempt to make traffic sniffing difficult. You're probably capturing on a protected network; the 802.11 header isn't encrypted, so Wireshark is able to dissect the encrypted traffic as 802.11 traffic, but the payload is encrypted, so Wireshark can't even dissect it as IP traffic, much less TCP or HTTP, so it shows up as "802.11".</p><p>Wireshark <em>can</em> decrypt 802.11 traffic, <em>if</em> you give it the password for the network and, for WPA/WPA2, <em>if</em>, for each host whose traffic it wants to decrypt, it sees the initial "EAPOL handshake" between the host and the access point. See <a href="http://wiki.wireshark.org/HowToDecrypt802.11">the Wireshark page on decrypting 802.11</a> for details.</p><p>("use curl to fetch a page from some site" means to use the <a href="http://curl.haxx.se">curl</a> command-line utility to fetch a page from an HTTP site; that might be more convenient than installing a Web browser - given that Kali Linux is a distribution intended for use on machines used for testing network security, it might have a limited set of tools such as Web browsers. However, as installed on your machine, it apparently <em>does</em> have a Web browser, so you could do the tests I wanted done without installing a browser, and, when you did so, it supported my guess as to what was happening. You don't need to worry about curl.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '14, 14:08</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Nov '14, 14:09</strong> </span></p></div></div><div id="comments-container-37715" class="comments-container"></div><div id="comment-tools-37715" class="comment-tools"></div><div class="clear"></div><div id="comment-37715-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

