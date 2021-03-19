+++
type = "question"
title = "High throughput captures, USB better than onboard NIC?"
description = '''I am attempting to use Wireshark on a laptop using the built-in NIC. The throughput of the traffic being captured is very high and sustained, and it appears I may be dropping traffic (observing &quot;acknowledgement for unseen packet&quot; errors).  I feel the laptop NIC may be inadequate. Purchasing a probe ...'''
date = "2011-06-08T14:17:00Z"
lastmod = "2011-06-08T16:23:00Z"
weight = 4458
keywords = [ "nic", "bandwidth", "throughput", "usb" ]
aliases = [ "/questions/4458" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [High throughput captures, USB better than onboard NIC?](/questions/4458/high-throughput-captures-usb-better-than-onboard-nic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4458-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4458-score" class="post-score" title="current number of votes">0</div><span id="post-4458-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am attempting to use Wireshark on a laptop using the built-in NIC. The throughput of the traffic being captured is very high and sustained, and it appears I may be dropping traffic (observing "acknowledgement for unseen packet" errors).<br />
</p><p>I feel the laptop NIC may be inadequate. Purchasing a probe or server with industrial NIC's is a bit overkill, as I only need this for a few days.<br />
</p><p>Would a separate USB NIC provide the ability to capture higher throughput using the same laptop?<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nic" rel="tag" title="see questions tagged &#39;nic&#39;">nic</span> <span class="post-tag tag-link-bandwidth" rel="tag" title="see questions tagged &#39;bandwidth&#39;">bandwidth</span> <span class="post-tag tag-link-throughput" rel="tag" title="see questions tagged &#39;throughput&#39;">throughput</span> <span class="post-tag tag-link-usb" rel="tag" title="see questions tagged &#39;usb&#39;">usb</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '11, 14:17</strong></p><img src="https://secure.gravatar.com/avatar/1d2b3e323d00727b8ea190cd0587ac5b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Husker97&#39;s gravatar image" /><p><span>Husker97</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Husker97 has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> retagged <strong>08 Jun '11, 19:41</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></br></p></div></div><div id="comments-container-4458" class="comments-container"></div><div id="comment-tools-4458" class="comment-tools"></div><div class="clear"></div><div id="comment-4458-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4462"></span>

<div id="answer-container-4462" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4462-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4462-score" class="post-score" title="current number of votes">1</div><span id="post-4462-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't see how a separate USB NIC would help you.</p><p>For performance problems like dropped packets, you might try reading the <a href="http://wiki.wireshark.org/Performance">Performance</a> page on the Wireshark wiki. But I would highly recommend using <a href="http://www.wireshark.org/docs/man-pages/dumpcap.html">dumpcap</a> instead of Wireshark for capturing if you're dropping too many packets. Besides helping with performance, another benefit of using dumpcap instead of Wireshark is that it will avoid/eliminate any potential "<a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">out of memory</a>" problems you could otherwise encounter by using Wireshark, especially if you intend to capture for lengthy periods of time.</p><p>You could also try using <a href="http://www.winpcap.org/windump/default.htm">Windump</a> or <a href="http://www.tcpdump.org/">tcpdump</a> depending on what OS your laptop is running.<br />
</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jun '11, 16:23</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span> </br></p></div></div><div id="comments-container-4462" class="comments-container"></div><div id="comment-tools-4462" class="comment-tools"></div><div class="clear"></div><div id="comment-4462-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

