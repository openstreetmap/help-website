+++
type = "question"
title = "J5Create JU130 (with AX88179 chipset) compatibility"
description = '''I just bought J5Create&#x27;s JU130 USB to ethernet adapter, specifically to inspect packets as a &quot;man-in-the-middle&quot; in order to debug a problem we&#x27;re having with an embedded device we&#x27;re developing. This device has an AX88179 inside (according to Windows 7&#x27;s device manager). Is this compatibile with Wi...'''
date = "2014-11-14T12:01:00Z"
lastmod = "2014-11-17T16:57:00Z"
weight = 37871
keywords = [ "compatibility" ]
aliases = [ "/questions/37871" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [J5Create JU130 (with AX88179 chipset) compatibility](/questions/37871/j5create-ju130-with-ax88179-chipset-compatibility)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37871-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37871-score" class="post-score" title="current number of votes">0</div><span id="post-37871-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just bought J5Create's <code>JU130 USB to ethernet adapte</code>r, specifically to inspect packets as a "man-in-the-middle" in order to debug a problem we're having with an embedded device we're developing. This device has an <code>AX88179</code> inside (according to Windows 7's device manager).</p><p>Is this compatibile with Wireshark? It is not appearing in the interface list. According to <a href="http://www.asix.com.tw/faq.php?op=faqdetail&amp;PItemID=131&amp;FaqNoID=#689">this FAQ on ASIX's website</a>, it seems like it should work.</p><p>Any ideas?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-compatibility" rel="tag" title="see questions tagged &#39;compatibility&#39;">compatibility</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '14, 12:01</strong></p><img src="https://secure.gravatar.com/avatar/31fa336e42452eede1353d1040abda02?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zman97211&#39;s gravatar image" /><p><span>zman97211</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zman97211 has no accepted answers">0%</span></p></div></div><div id="comments-container-37871" class="comments-container"></div><div id="comment-tools-37871" class="comment-tools"></div><div class="clear"></div><div id="comment-37871-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37874"></span>

<div id="answer-container-37874" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37874-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37874-score" class="post-score" title="current number of votes">0</div><span id="post-37874-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is this compatibile with Wireshark?</p></blockquote><p>Wireshark isn't directly compatible, or incompatible, with <em>any</em> networking hardware; for example, it has no device drivers. It relies on the hardware's drivers, the OS's native packet capture mechanism on UN*X and the OS's NDIS and the WinPcap driver (which isn't a hardware device driver) on Windows, and the libpcap/WinPcap library.</p><p>The code above the driver shouldn't be treating any particular Ethernet adapter differently on Windows; does your adapter show up in the "Network and Sharing Center" pane in Control Panel?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Nov '14, 16:08</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-37874" class="comments-container"><span id="37900"></span><div id="comment-37900" class="comment"><div id="post-37900-score" class="comment-score"></div><div class="comment-text"><p>It does show up in the control panel. The solution I ended up using was passing the USB-Ethernet adapter through to Ubuntu 12.04 running inside VirtualBox. Wireshark was able to use the adapter there without a problem.</p></div><div id="comment-37900-info" class="comment-info"><span class="comment-age">(17 Nov '14, 05:46)</span> <span class="comment-user userinfo">zman97211</span></div></div><span id="37926"></span><div id="comment-37926" class="comment"><div id="post-37926-score" class="comment-score"></div><div class="comment-text"><p>Did you plug the JU130 in after you started Wireshark? If so, what happens if you quit Wireshark and restart it? Does it show up again?</p><p>If it doesn't show up in that case, or if you plugged it in <em>before</em> you started Wireshark, what happens if you plug the JU130, reboot the machine, and start Wireshark? Does Wireshark see it then?</p><p>This might be a case of WinPcap not handling interfaces plugged in after the program starts, or not handling adapters added after the system booted. Those tests could help determine whether that's the case.</p></div><div id="comment-37926-info" class="comment-info"><span class="comment-age">(17 Nov '14, 16:57)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-37874" class="comment-tools"></div><div class="clear"></div><div id="comment-37874-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

