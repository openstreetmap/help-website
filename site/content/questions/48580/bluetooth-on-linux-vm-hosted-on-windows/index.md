+++
type = "question"
title = "Bluetooth on Linux VM hosted on Windows?"
description = '''I think I just answered my own question, but if I cannot capture Bluetooth traffic using Wireshark on a Windows laptop, I&#x27;m probably not going to be terribly successful capturing Bluetooth traffic using Wireshark on a Linux VM hosted on that same Windows laptop, am I? Thanks, John'''
date = "2015-12-16T11:44:00Z"
lastmod = "2015-12-20T09:45:00Z"
weight = 48580
keywords = [ "bluetooth", "vmware", "linux" ]
aliases = [ "/questions/48580" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Bluetooth on Linux VM hosted on Windows?](/questions/48580/bluetooth-on-linux-vm-hosted-on-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48580-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48580-score" class="post-score" title="current number of votes">0</div><span id="post-48580-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I think I just answered my own question, but if I cannot capture Bluetooth traffic using Wireshark on a Windows laptop, I'm probably not going to be terribly successful capturing Bluetooth traffic using Wireshark on a Linux VM hosted on that same Windows laptop, am I?</p><p>Thanks, John</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bluetooth" rel="tag" title="see questions tagged &#39;bluetooth&#39;">bluetooth</span> <span class="post-tag tag-link-vmware" rel="tag" title="see questions tagged &#39;vmware&#39;">vmware</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Dec '15, 11:44</strong></p><img src="https://secure.gravatar.com/avatar/674a1eaa580f91629e6178ba8e75a8fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JohnG&#39;s gravatar image" /><p><span>JohnG</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JohnG has no accepted answers">0%</span></p></div></div><div id="comments-container-48580" class="comments-container"></div><div id="comment-tools-48580" class="comment-tools"></div><div class="clear"></div><div id="comment-48580-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48590"></span>

<div id="answer-container-48590" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48590-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48590-score" class="post-score" title="current number of votes">1</div><span id="post-48590-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>but if I cannot capture Bluetooth traffic using Wireshark on a Windows laptop, I'm probably not going to be terribly successful capturing Bluetooth traffic using Wireshark on a Linux VM hosted on that same Windows laptop, am I?</p></blockquote><p>You <em>might</em> be.</p><p><em>If</em> the virtual machine software provides a Bluetooth interface on the VM guest machine, using the host machine's Bluetooth adapter, and <em>if</em> the Linux recognizes that Bluetooth interface, you should be able to capture Bluetooth traffic between the <em>Linux guest</em> and other machines. However, you won't be able to capture Bluetooth traffic between the <em>Windows host</em> and other machines, and you won't be able to capture <em>other</em> Bluetooth traffic - traffic between two other machines - on the Linux guest.</p><p>If you want to passively capture <em>third-party</em> Bluetooth traffic, between two other machines, you'll need something such as <a href="https://github.com/greatscottgadgets/ubertooth/wiki">Ubertooth</a> software and a device that supports it, such as an Ubertooth One. Ubertooth <em>might</em> work on OS X, but doesn't appear to work on Windows, so you'll have to run it on your Linux guest, which will require that the virtual machine support connecting to the guest USB devices plugged into the host.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Dec '15, 17:16</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-48590" class="comments-container"><span id="48612"></span><div id="comment-48612" class="comment"><div id="post-48612-score" class="comment-score"></div><div class="comment-text"><p>Thanks - I am attempting to debug the BT link between a device and a printer. Not being able to see if there is any traffic is rather hobbling. Thanks for the Ubertooth hint.</p></div><div id="comment-48612-info" class="comment-info"><span class="comment-age">(17 Dec '15, 06:21)</span> <span class="comment-user userinfo">JohnG</span></div></div><span id="48650"></span><div id="comment-48650" class="comment"><div id="post-48650-score" class="comment-score"></div><div class="comment-text"><p>If you have Standard USB Bluetooth dongle (or your laptop has Bluetooth pluged by internal/virtual USB) then you can try do that on Windows by USBPcap (Wireshark 2.0 or later.. or standalone USBPcap: <a href="http://desowin.org/usbpcap/).">http://desowin.org/usbpcap/).</a></p></div><div id="comment-48650-info" class="comment-info"><span class="comment-age">(20 Dec '15, 09:45)</span> <span class="comment-user userinfo">Michał Łabędzki</span></div></div></div><div id="comment-tools-48590" class="comment-tools"></div><div class="clear"></div><div id="comment-48590-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

