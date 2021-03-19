+++
type = "question"
title = "Monitor Mode problem"
description = '''I&#x27;m trying to view the RTS/CTS process that occurs when you lower the RTS threshold on a wireless router. I have to be in monitor mode to be able to view this traffic but I can&#x27;t seem to be able to get there. I&#x27;m looking under &quot;Capture&quot; for an option under promiscuous mode but from the Wireshark Use...'''
date = "2011-03-07T17:23:00Z"
lastmod = "2014-08-07T10:41:00Z"
weight = 2702
keywords = [ "cts", "monitor", "rts", "mode" ]
aliases = [ "/questions/2702" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Monitor Mode problem](/questions/2702/monitor-mode-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2702-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2702-score" class="post-score" title="current number of votes">0</div><span id="post-2702-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to view the RTS/CTS process that occurs when you lower the RTS threshold on a wireless router. I have to be in monitor mode to be able to view this traffic but I can't seem to be able to get there. I'm looking under "Capture" for an option under promiscuous mode but from the Wireshark User's Guide I see that this option may be available only if you are running Linux or Unix. I've read some other things online that suggest that even if you are running Linux your adapter must still be capable of being configured to accept monitor mode. I've read other posts that suggest that it is possible to get into monitor mode even if you are running Vista, as I am.<br />
I'd really appreciate a clear explanation of what, if anything, I can do to be able to view my captures in monitor mode. Is there a NIC that will allow me to get into monitor mode using Vista? If I add Linux to my PC am I assured of being able to get into monitor mode or will I still have to wait and see if my NIC supports it? Appreciate any help with this from the community.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-cts" rel="tag" title="see questions tagged &#39;cts&#39;">cts</span> <span class="post-tag tag-link-monitor" rel="tag" title="see questions tagged &#39;monitor&#39;">monitor</span> <span class="post-tag tag-link-rts" rel="tag" title="see questions tagged &#39;rts&#39;">rts</span> <span class="post-tag tag-link-mode" rel="tag" title="see questions tagged &#39;mode&#39;">mode</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Mar '11, 17:23</strong></p><img src="https://secure.gravatar.com/avatar/b111a3c8683f50aca9fba6e11fa05fb7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tedsini&#39;s gravatar image" /><p><span>tedsini</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tedsini has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-2702" class="comments-container"></div><div id="comment-tools-2702" class="comment-tools"></div><div class="clear"></div><div id="comment-2702-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="2703"></span>

<div id="answer-container-2703" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2703-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2703-score" class="post-score" title="current number of votes">2</div><span id="post-2703-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"Unix" is a generic term; it either means "any OS that looks like a Unix", which includes Linux and Solaris and <em>BSD and Mac OS X and AIX and HP-UX and..., or "any OS that's passed that validation suite so the 'Unix' trademark can be used with it", which includes Solaris and AIX and HP-UX and Mac OS X but not Linux or</em> BSD. In either case, there are some Unixes that support monitor mode and that don't.</p><p>The actual answer is that the OSes on which you can capture in monitor mode with tcpdump or Wireshark are Linux, *BSD, and Mac OS X, and that's it; you cannot do so on Windows (or on Unixes such as Solaris). All you can do on Windows is buy an <a href="http://www.cacetech.com/products/airpcap.html">AirPcap adapter</a> and use that.</p><p>You <em>can</em> capture in monitor mode on Vista and Windows 7 with, for example, <a href="http://www.microsoft.com/downloads/en/details.aspx?displaylang=en&amp;FamilyID=983b941d-06cb-4658-b7f6-3088333d062f">Microsoft Network Monitor</a>, as well as with some other network analyzers that cost money. That should work with any wireless network adapter that has a driver that supports "Native WiFi" - you might have to ask the vendor of the adapter (or, if it's built into your machine, the vendor of your machine) whether the driver supports Native WiFi or not.</p><p>If you "add" Linux to it, you'll either have to replace Windows with Linux so that you can't run Windows at all, dual-boot Windows and Linux so that you can only run one of them at a time, or use something like VMware or Parallels to run Linux on a virtual machine, but the virtual machine would require that you get something such as a USB Wi-Fi adapter and have Linux use that adapter. All of those would be somewhat inconvenient. If you <em>are</em> running a reasonably recent version of some Linux distribution, most adapters and their drivers will support monitor mode.</p><p>For more information, including some links in the Linux section to pages that should indicate which adapters and drivers support monitor mode, see <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">the CaptureSetup/WLAN page of the Wireshark Wiki</a>.</p><p>(<a href="http://en.wikipedia.org/wiki/Promiscuous_mode">Promiscuous mode</a> and <a href="http://en.wikipedia.org/wiki/Monitor_mode">monitor mode</a> are not the same. Promiscuous mode is supported on networks other than Wi-Fi networks, and it's supported on all OSes on which Wireshark works, including Windows. It may, or may not, work with Wi-Fi adapters; on Windows, it usually <em>doesn't</em> work with Wi-Fi adapters. Monitor mode is specific to Wi-Fi adapters, and is what you'd need if you want to see low-level Wi-Fi details such as RTS and CTS packets.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Mar '11, 17:57</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Mar '11, 18:01</strong> </span></p></div></div><div id="comments-container-2703" class="comments-container"><span id="5598"></span><div id="comment-5598" class="comment"><div id="post-5598-score" class="comment-score"></div><div class="comment-text"><p>As it turns out, this was why I was able to see multicast packets being received on a dual-boot Linux/Windows machine in Linux, but not in Windows, when going over wireless. Thank you for posting!</p></div><div id="comment-5598-info" class="comment-info"><span class="comment-age">(09 Aug '11, 12:52)</span> <span class="comment-user userinfo">bch36</span></div></div></div><div id="comment-tools-2703" class="comment-tools"></div><div class="clear"></div><div id="comment-2703-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="35311"></span>

<div id="answer-container-35311" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35311-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35311-score" class="post-score" title="current number of votes">0</div><span id="post-35311-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Install <a href="https://www.acrylicwifi.com/en/wlan-software/wlan-scanner-acrylic-wifi-free/">Acrylic WiFi</a> under windows, and then execute Wireshark as an Administrator. Wireshark will be able to capture WiFi packets under windows because Acrylic emulates monitor mode capable cards.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Aug '14, 10:41</strong></p><img src="https://secure.gravatar.com/avatar/c601fc1140b59596c899c2386bd29460?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AcrylicWiFi&#39;s gravatar image" /><p><span>AcrylicWiFi</span><br />
<span class="score" title="9 reputation points">9</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AcrylicWiFi has no accepted answers">0%</span></p></div></div><div id="comments-container-35311" class="comments-container"></div><div id="comment-tools-35311" class="comment-tools"></div><div class="clear"></div><div id="comment-35311-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

