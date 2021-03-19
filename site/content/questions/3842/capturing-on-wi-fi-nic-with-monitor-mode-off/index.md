+++
type = "question"
title = "Capturing on Wi-Fi NIC with monitor mode off"
description = '''Hello, I&#x27;m trying to capture traffic passing through a Wi-Fi NIC, but with monitor mode off. When I set this up via capture options (pick my en1 interface, disable monitor mode) and click Start, I get a dialog that says this: &quot;Unable to set data link type (IEEE802_11 is not one of the DLTs supported...'''
date = "2011-04-30T08:51:00Z"
lastmod = "2011-05-23T00:15:00Z"
weight = 3842
keywords = [ "capture", "mac", "802.11", "osx" ]
aliases = [ "/questions/3842" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing on Wi-Fi NIC with monitor mode off](/questions/3842/capturing-on-wi-fi-nic-with-monitor-mode-off)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3842-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3842-score" class="post-score" title="current number of votes">1</div><span id="post-3842-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm trying to capture traffic passing through a Wi-Fi NIC, but with monitor mode off. When I set this up via capture options (pick my en1 interface, disable monitor mode) and click Start, I get a dialog that says this: "Unable to set data link type (IEEE802_11 is not one of the DLTs supported by this device). Please report this to the Wireshark developers. (This is not a crash; please do not report it as such.)" It has been a few months since I've tried to do this, but I am almost certain I used to be able to capture traffic over my 802.11 interface without having to put it into monitor mode.</p><p>I'm on Mac OS X 10.6.7, Wireshark 1.4.6 installed via MacPorts.</p><p>Any ideas?</p><p>Thanks for any help,</p><p>Smith</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span> <span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Apr '11, 08:51</strong></p><img src="https://secure.gravatar.com/avatar/60cd8879a73855d635baa0c72124cdfb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="klaushergesheimer&#39;s gravatar image" /><p><span>klaushergesh...</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="klaushergesheimer has no accepted answers">0%</span></p></div></div><div id="comments-container-3842" class="comments-container"></div><div id="comment-tools-3842" class="comment-tools"></div><div class="clear"></div><div id="comment-3842-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3846"></span>

<div id="answer-container-3846" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3846-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3846-score" class="post-score" title="current number of votes">0</div><span id="post-3846-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In Mac OS X, you can capture on an 802.11 interface without being in monitor mode.</p><p>However, you cannot, and never were able to, in any version of Mac OS X, capture with 802.11 headers, rather than fake Ethernet headers, if you're not in monitor mode. Wireshark <em>should</em> forcibly set the link-layer type to Ethernet if you disable monitor mode; if it doesn't, file a bug at <a href="http://bugs.wireshark.org">the Wireshark bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '11, 12:23</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-3846" class="comments-container"><span id="4177"></span><div id="comment-4177" class="comment"><div id="post-4177-score" class="comment-score"></div><div class="comment-text"><p>I'm sorry, perhaps I wasn't clear.</p><p>If I start Wireshark, do Capture Options, and select en1 (the typical interface for an on-board AirPort Extreme 802.11 NIC), I am presented with the option to enable / disable "Capture packets in monitor mode". If I have that checkbox checked (monitor mode enabled), I capture the raw 802.11 traffic, as expected.</p><p>However, if I <em>deselect</em> the "Capture packets in monitor mode" checkbox, to capture traffic in the pseudo-Ethernet format, and click "Start", I get a dialog with the message I described above:</p><p>"Unable to set data link type (IEEE802_11 is not one of the DLTs supported by this device). Please report this to the Wireshark developers. (This is not a crash; please do not report it as such.)"</p><p>Should I be seeing this, assuming I only have Wireshark installed?<br />
</p><p>I have a variety of other MacPorts ports installed, as well as some Wi-Fi programs not from MacPorts (like KisMAC, etc.), and I don't know if one of those is putting something into NKE / protocol stack that might be causing this problem, but before I begin that kind of time investment I wanted to know whether this was supported in the first place.</p></div><div id="comment-4177-info" class="comment-info"><span class="comment-age">(22 May '11, 20:41)</span> <span class="comment-user userinfo">klaushergesh...</span></div></div><span id="4179"></span><div id="comment-4179" class="comment"><div id="post-4179-score" class="comment-score"></div><div class="comment-text"><p>As another data point, I just tried running "sudo wireshark -i en1 -w foo.pcap", and tcpdump can capture at the Ethernet level:</p><pre><code>Hot-Needle-of-Inquiry:~ [502]$ sudo /usr/sbin/tcpdump -i en1 -w foo.pcap
tcpdump: listening on en1, link-type EN10MB (Ethernet), capture size 65535 bytes
^C4037 packets captured
4037 packets received by filter
0 packets dropped by kernel
Hot-Needle-of-Inquiry:~ [503]$</code></pre><p>I guess I have a workaround, but it is a disappointingly limited one, because I cannot take advantage of the live presentation functionality of Wireshark in that mode.</p><p>Is there some way to "dump" the driver stack that Wireshark is using? Obviously, the tcpdump is from Mac OS X core installation, whereas my Wireshark is from MacPorts. Perhaps it is the way that libpcap or one of the MacPorts libraries that Wireshark is using is built by MacPorts.</p></div><div id="comment-4179-info" class="comment-info"><span class="comment-age">(22 May '11, 21:06)</span> <span class="comment-user userinfo">klaushergesh...</span></div></div><span id="4181"></span><div id="comment-4181" class="comment"><div id="post-4181-score" class="comment-score"></div><div class="comment-text"><p>Ugh, more digging. Uninstalled all ports from MacPorts, then re-installed Wireshark. Still had this problem. Curiously, I dug into the wireshark man page, and found that this:</p><pre><code>sudo wireshark -i en1 -k -y EN10MB</code></pre><p>starts Wireshark immediately into a a capture on the 802.11 NIC (en1), but DOES use and present the Ethernet link layer header type, so I am getting the traffic on the Wi-Fi network to which I am connected. Sadly, if I stop and restart the capture, it again gives me the problem I first described. It seems like it is just that Wireshark somehow cannot connect the dots itself.</p></div><div id="comment-4181-info" class="comment-info"><span class="comment-age">(22 May '11, 22:41)</span> <span class="comment-user userinfo">klaushergesh...</span></div></div><span id="4182"></span><div id="comment-4182" class="comment"><div id="post-4182-score" class="comment-score"></div><div class="comment-text"><p>With the 1.4.6 version from wireshark.org, on 10.6.7, if I fire up Wireshark, set the interface to en1, and un-check the monitor mode checkbox, it forcibly sets the link-layer type to Ethernet (and does not allow it to be changed), and allows me to start a capture.</p><p>Try downloading and installing the wireshark.org version, and see whether it works the same way. If so, the macports people probably did something wrong.</p></div><div id="comment-4182-info" class="comment-info"><span class="comment-age">(23 May '11, 00:15)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-3846" class="comment-tools"></div><div class="clear"></div><div id="comment-3846-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

