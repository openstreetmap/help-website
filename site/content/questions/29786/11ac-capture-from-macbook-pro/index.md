+++
type = "question"
title = "11ac capture from macbook pro"
description = '''I am noticing that phy rates are not always being decoded properly and wondered if there was a fix in the works. iPhone 5S supports and is connected to 40MHz channel but only reports PHY RATE of 72.2, which is not correct. There are also other times when it doesnt report any rates at all. Thoughts? ...'''
date = "2014-02-12T09:43:00Z"
lastmod = "2014-02-12T19:30:00Z"
weight = 29786
keywords = [ "802.11ac" ]
aliases = [ "/questions/29786" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [11ac capture from macbook pro](/questions/29786/11ac-capture-from-macbook-pro)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29786-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29786-score" class="post-score" title="current number of votes">0</div><span id="post-29786-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am noticing that phy rates are not always being decoded properly and wondered if there was a fix in the works. iPhone 5S supports and is connected to 40MHz channel but only reports PHY RATE of 72.2, which is not correct. There are also other times when it doesnt report any rates at all.</p><p>Thoughts? I have tried PPI and RadioTap.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-802.11ac" rel="tag" title="see questions tagged &#39;802.11ac&#39;">802.11ac</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Feb '14, 09:43</strong></p><img src="https://secure.gravatar.com/avatar/7e0fa53c46a4e72be341936407078f86?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ericsr&#39;s gravatar image" /><p><span>ericsr</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ericsr has no accepted answers">0%</span></p></div></div><div id="comments-container-29786" class="comments-container"><span id="29801"></span><div id="comment-29801" class="comment"><div id="post-29801-score" class="comment-score"></div><div class="comment-text"><p><a href="http://www.radiotap.org/defined-fields/Rate">The rate field in radiotap</a> and the rate field in <a href="http://www.cacetech.com/documents/PPI%20Header%20format%201.0.7.pdf">the PPI specification</a> are both numbers in units of .5 Mb/s, and thus can't represent a PHY rate of 72.2 Mb/s (72.2 Mb/s is not a multiple of .5 Mb/s). Are you referring to a PHY rate reported somewhere <em>other</em> than the radiotap or PPI header?</p></div><div id="comment-29801-info" class="comment-info"><span class="comment-age">(12 Feb '14, 16:26)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="29803"></span><div id="comment-29803" class="comment"><div id="post-29803-score" class="comment-score"></div><div class="comment-text"><p>See attachment</p></div><div id="comment-29803-info" class="comment-info"><span class="comment-age">(12 Feb '14, 16:43)</span> <span class="comment-user userinfo">ericsr</span></div></div><span id="29804"></span><div id="comment-29804" class="comment"><div id="post-29804-score" class="comment-score"></div><div class="comment-text"><p><img src="https://osqa-ask.wireshark.org/upfiles/_Wi-Fi__en0____Wireshark_1_10_5___SVN_Rev_54262_from__trunk-1_10__-2.jpg" alt="alt text" /></p></div><div id="comment-29804-info" class="comment-info"><span class="comment-age">(12 Feb '14, 16:43)</span> <span class="comment-user userinfo">ericsr</span></div></div></div><div id="comment-tools-29786" class="comment-tools"></div><div class="clear"></div><div id="comment-29786-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29811"></span>

<div id="answer-container-29811" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29811-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29811-score" class="post-score" title="current number of votes">0</div><span id="post-29811-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>UPDATE: having looked at the capture attached to the bug, the VHT field is not present, so either:</p><p>1) the traffic is <em>NOT</em> 11ac traffic - if it's coming from the iPhone 5s, either it's not 11ac traffic, or Apple isn't telling the entire truth when they say, on <a href="http://www.apple.com/iphone-5s/specs/">their iPhone 5s tech specs page</a>, that the 5s supports "802.11a/b/g/n Wi-Fi (802.11n 2.4GHz and 5GHz" and don't mention 11ac</p><p>or</p><p>2) it's 11ac traffic but the driver in the OS is reporting it as 11n traffic (the MCS field is present).</p><p>OK, that's not coming from the radiotap Rate field, it's looked up in a table using the MCS rate index, bandwidth, and guard interval length, from the <a href="http://www.radiotap.org/defined-fields/MCS">radiotap MCS field</a>, as indices. The table comes from information in section 20.6 "Parameters for HT MCSs" in the 802.11 spec.</p><p>I think the <a href="http://www.radiotap.org/defined-fields/VHT">VHT field</a> in the radiotap header is for 11ac.</p><p><em>If</em> the driver for the adapter in the version you're using of the OS you're using (Mountain Lion or Mavericks, probably, in your case, but similar stuff would need to be done for Linux and *BSD, for example) supplies the VHT field, then there is code in Wireshark 1.10.x to handle that field. If it's not calculating the correct data rate, either the driver isn't supplying the right VHT field values or isn't supplying them at all, in which case you'd have to ask Apple whether there's a fix in the works, or the rate isn't being calculated correctly from that field value, in which case Wireshark would need to be changed.</p><p>If the driver is <em>not</em> supplying the VHT field, but is supplying the MCS field, then Wireshark is doing the best that it can, and you'd have to ask Apple whether there's a fix in the works.</p><p>If you're not running the latest wireshark 1.10.x release (currently 1.10.5), upgrade to it, and see if that fixes the problem.</p><p>If that doesn't fix it, you should file a bug on <a href="http://bugs.wireshark.org">the Wireshark Bugzilla</a> on this, and attach a raw capture file (not a screenshot of Wireshark's display of the capture file) containing a packet showing the problem. (If it was captured on a protected network - WEP or WPA/WPA2-encrypted - you do <strong><em>NOT</em></strong> need to supply the password for the network; we don't need any information other than the radiotap header information.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '14, 18:13</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Feb '14, 10:35</strong> </span></p></div></div><div id="comments-container-29811" class="comments-container"><span id="29812"></span><div id="comment-29812" class="comment"><div id="post-29812-score" class="comment-score"></div><div class="comment-text"><p>Appears to only happen on 80MHz channelization. I am now on 40 and it displays properly. I have entered a bug.</p></div><div id="comment-29812-info" class="comment-info"><span class="comment-age">(12 Feb '14, 18:23)</span> <span class="comment-user userinfo">ericsr</span></div></div><span id="29813"></span><div id="comment-29813" class="comment"><div id="post-29813-score" class="comment-score"></div><div class="comment-text"><p>You're not going to get 80 MHz channelization, or anything else 11ac, with your iPhone - the iPhone 5s only supports 802.11a/b/c/n, <em>not</em> 802.11ac, according to <a href="http://www.apple.com/iphone-5s/specs/">Apple's tech specs page for the 5s</a>. You can get data rates higher than 72.2 with 11n; are the data rates for 802.11n packets correct, or are there problems with them as well?</p></div><div id="comment-29813-info" class="comment-info"><span class="comment-age">(12 Feb '14, 18:42)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="29814"></span><div id="comment-29814" class="comment"><div id="post-29814-score" class="comment-score"></div><div class="comment-text"><p>We'll need some captures, containing problematic packets, attached to the bug. (You can just make small captures containing only the problematic packets and, if the packets are from a protected network, using WEP or WPA/WPA2, you do <em>not</em> need to supply the password for the network - we only need to look at the radiotap header, not the packet data.)</p></div><div id="comment-29814-info" class="comment-info"><span class="comment-age">(12 Feb '14, 19:30)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-29811" class="comment-tools"></div><div class="clear"></div><div id="comment-29811-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

