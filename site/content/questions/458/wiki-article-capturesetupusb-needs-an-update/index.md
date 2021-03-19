+++
type = "question"
title = "Wiki Article &quot;CaptureSetup/USB&quot; needs an update"
description = '''Some information is wrong:  &quot;The latest libpcap from the main Git branch is required...&quot; -&amp;gt; libpcap 1.1.1 or newer would be correct. Setup for Linux &amp;gt;= 2.6.21 : Not only &quot;mount -t usbfs /dev/bus/usb /proc/bus/usb&quot;, I also needed a &quot;modprobe usbmon&quot; &quot;8. On Linux, startup a USB-enabled version o...'''
date = "2010-10-08T04:50:00Z"
lastmod = "2010-10-09T11:36:00Z"
weight = 458
keywords = [ "wiki" ]
aliases = [ "/questions/458" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Wiki Article "CaptureSetup/USB" needs an update](/questions/458/wiki-article-capturesetupusb-needs-an-update)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-458-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-458-score" class="post-score" title="current number of votes">0</div><span id="post-458-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Some information is wrong:</p><ul><li>"The latest libpcap from the main Git branch is required..." -&gt; libpcap 1.1.1 or newer would be correct.</li><li>Setup for Linux &gt;= 2.6.21 : Not only "mount -t usbfs /dev/bus/usb /proc/bus/usb", I also needed a "modprobe usbmon"</li><li>"8. On Linux, startup a USB-enabled version of Wireshark" -&gt; "8. On Linux, startup Wireshark..."</li></ul><p>Is this the right place for my tip ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wiki" rel="tag" title="see questions tagged &#39;wiki&#39;">wiki</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Oct '10, 04:50</strong></p><img src="https://secure.gravatar.com/avatar/dbeba090e42c20071befe0719def822f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerd&#39;s gravatar image" /><p><span>Gerd</span><br />
<span class="score" title="36 reputation points">36</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerd has one accepted answer">100%</span></p></div></div><div id="comments-container-458" class="comments-container"><span id="466"></span><div id="comment-466" class="comment"><div id="post-466-score" class="comment-score">1</div><div class="comment-text"><p>The setup is probably more complicated than that.</p><p>For example, libpcap 1.1.1 will first try scanning /sys/bus/usb/devices for devices, and will only scan /proc/bus/usb if it can't open /sys/bus/usb/devices.</p><p>In addition, as Gerald noted in answer to your earlier question, he was able to capture from usbmon1 on Ubuntu 10.04 (Linux kernel 2.6.32-24) without having to do anything special.</p><p>What needs to be done may differ from kernel version to kernel version <em>and</em> might differ from <em>distribution</em> and <em>distribution version</em> to distribution/distribution version.</p></div><div id="comment-466-info" class="comment-info"><span class="comment-age">(08 Oct '10, 19:31)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-458" class="comment-tools"></div><div class="clear"></div><div id="comment-458-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="459"></span>

<div id="answer-container-459" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-459-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-459-score" class="post-score" title="current number of votes">2</div><span id="post-459-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Gerd has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, it's a Wiki, by definition a resource to be edited by the community. So go ahead and hack it yourself; but "Please don't pee in the pool".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Oct '10, 05:28</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-459" class="comments-container"><span id="468"></span><div id="comment-468" class="comment"><div id="post-468-score" class="comment-score"></div><div class="comment-text"><p>Now it's done.</p></div><div id="comment-468-info" class="comment-info"><span class="comment-age">(09 Oct '10, 11:36)</span> <span class="comment-user userinfo">Gerd</span></div></div></div><div id="comment-tools-459" class="comment-tools"></div><div class="clear"></div><div id="comment-459-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

