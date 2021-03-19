+++
type = "question"
title = "How do I find cause of packet overruns?"
description = '''I&#x27;ve just been stuck with solving an issue on a clients backup server. &quot;Backup performance is awful&quot; was my only description before being dumped into this situation on this beautiful (albeit cold) Saturday. Anyways, we were seeing output packet drops at the switch (cisco 4509). Disabled QoS on all s...'''
date = "2012-12-01T12:12:00Z"
lastmod = "2012-12-02T23:18:00Z"
weight = 16480
keywords = [ "windows", "backup", "overrun", "packet", "wireshark" ]
aliases = [ "/questions/16480" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I find cause of packet overruns?](/questions/16480/how-do-i-find-cause-of-packet-overruns)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16480-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16480-score" class="post-score" title="current number of votes">0</div><span id="post-16480-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've just been stuck with solving an issue on a clients backup server. "Backup performance is awful" was my only description before being dumped into this situation on this beautiful (albeit cold) Saturday.</p><p>Anyways, we were seeing output packet drops at the switch (cisco 4509). Disabled QoS on all server ports and that immediately stopped.</p><p>However, the "interface details" tab in Wireshark shows an ever increasing value under statistics "Packets not received due to overrun". Dozens of these a second.</p><p>I setup PRTG to monitor bandwidth, I'm seeing a steady 50,000 kbits/sec. The port isn't being throttled near as I can tell.</p><p>Any tips how I can track down the cause of this "overrun"?<br />
</p><p>Any help is appreciated. Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-backup" rel="tag" title="see questions tagged &#39;backup&#39;">backup</span> <span class="post-tag tag-link-overrun" rel="tag" title="see questions tagged &#39;overrun&#39;">overrun</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '12, 12:12</strong></p><img src="https://secure.gravatar.com/avatar/0a919c9cbb95f41257071e595274e212?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JonnyTheG&#39;s gravatar image" /><p><span>JonnyTheG</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JonnyTheG has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-16480" class="comments-container"></div><div id="comment-tools-16480" class="comment-tools"></div><div class="clear"></div><div id="comment-16480-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16488"></span>

<div id="answer-container-16488" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16488-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16488-score" class="post-score" title="current number of votes">0</div><span id="post-16488-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"Packets not received due to overrun" is the number reported by a <a href="http://msdn.microsoft.com/en-us/library/windows/hardware/ff569076(v=vs.85).aspx">OID_802_3_RCV_OVERRUN</a> request to the driver; the page for it says it's "The number of frames not received due to overrun errors on the NIC."</p><p>When the "Interfaces" dialog is open, the interfaces are all open and capturing packets (that's where the statistics in that dialog come from); the overruns may just mean that the machine running Wireshark isn't processing packets fast enough - and that's probably processing in Windows before the packets reach Wireshark/dumpcap, as "overrun errors on the NIC" means, I think, "packets are coming in faster than the host driver can remove them from the driver's ring buffer" or possibly even "faster than the NIC can handle them". If Wireshark is running on one of the machines involved with the backup, the problem may just be that there's too much traffic for the machine to handle.</p><p>If there were a program that reported adapter statistics such as the overrun count <em>without</em> doing any capturing, I'd suggest running that and seeing whether it reports overruns - if so, that means that the overruns can't be blamed on running Wireshark, in which case you're probably just overloading the machine. I don't know of one, though, and some Googling didn't turn anything up.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '12, 16:31</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-16488" class="comments-container"><span id="16490"></span><div id="comment-16490" class="comment"><div id="post-16490-score" class="comment-score"></div><div class="comment-text"><p>I think the server is overloaded, too. The value increments regardless of Wireshark being open, open and capture or closed.</p></div><div id="comment-16490-info" class="comment-info"><span class="comment-age">(02 Dec '12, 19:47)</span> <span class="comment-user userinfo">JonnyTheG</span></div></div><span id="16491"></span><div id="comment-16491" class="comment"><div id="post-16491-score" class="comment-score"></div><div class="comment-text"><p>a few things to check/consider.</p><ul><li>if there is adapter teaming in place, disable it (if you can) and test again.</li><li>overruns can occur due to an overload (how many packets/s do you see in Wireshark) or due to problems with the NIC hardware <strong>or</strong> the interrupt handling in the OS (in conjunction with the driver). If the packet rate you see in Wireshark is not 'that high' (a few hundred packets per second or less), you might have a problem with the hardware (replace the NIC, update NIC firmware ) or with the driver (update it).</li></ul></div><div id="comment-16491-info" class="comment-info"><span class="comment-age">(02 Dec '12, 23:18)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-16488" class="comment-tools"></div><div class="clear"></div><div id="comment-16488-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

