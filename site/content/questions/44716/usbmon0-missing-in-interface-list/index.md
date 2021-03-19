+++
type = "question"
title = "usbmon0 missing in interface list"
description = '''I have usbmon installed and /sys/kernel/debug/usb/usbmon has entries for 0 to 4. If I cat 0u, I see transactions when I run an application I want to debug. Therefore, I think usbmon is working. Note that permissions on all are rw for root. All things I have tried run with sudo including enabled usbm...'''
date = "2015-07-31T17:42:00Z"
lastmod = "2015-08-03T02:41:00Z"
weight = 44716
keywords = [ "usbmon" ]
aliases = [ "/questions/44716" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [usbmon0 missing in interface list](/questions/44716/usbmon0-missing-in-interface-list)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44716-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44716-score" class="post-score" title="current number of votes">0</div><span id="post-44716-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have usbmon installed and /sys/kernel/debug/usb/usbmon has entries for 0 to 4. If I cat 0u, I see transactions when I run an application I want to debug. Therefore, I think usbmon is working.</p><p>Note that permissions on all are rw for root. All things I have tried run with sudo including enabled usbmon and wireshark.</p><p>Wireshark 1.10.6 lists usbmon1-4, none of which see traffic.</p><p>I assume there should be a usbmon0 in the interface list, but it is not listed.</p><p>Can someone confirm that there should be a usbmon0, and are there any ideas on how to make wireshark list it?</p><p>Or if the numbers aren't supposed to align, like 0s/u is really usbmon1 in wireshark, how do I debug the problem?</p><p>Ubuntu 14.X LTS</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-usbmon" rel="tag" title="see questions tagged &#39;usbmon&#39;">usbmon</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Jul '15, 17:42</strong></p><img src="https://secure.gravatar.com/avatar/3364122e826440010748627f007d6b96?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Proclivis&#39;s gravatar image" /><p><span>Proclivis</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Proclivis has no accepted answers">0%</span></p></div></div><div id="comments-container-44716" class="comments-container"><span id="44717"></span><div id="comment-44717" class="comment"><div id="post-44717-score" class="comment-score"></div><div class="comment-text"><p>Libpcap provides a usbmon<em>N</em> device for each entry in /sys/bus/usb/devices with a name of the form usb<em>N</em>. What does <code>ls /sys/bus/usb/devices</code> print?</p></div><div id="comment-44717-info" class="comment-info"><span class="comment-age">(31 Jul '15, 23:49)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-44716" class="comment-tools"></div><div class="clear"></div><div id="comment-44716-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44759"></span>

<div id="answer-container-44759" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44759-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44759-score" class="post-score" title="current number of votes">0</div><span id="post-44759-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Modern kernels (with the <code>usbmon</code> module loaded) also create a <code>/dev/usbmonX</code> device which is first probed for by Wireshark (actually, libpcap). When you run Wireshark as non-root user, it will not be able to capture from those devices. In that case, make sure that your user is allowed to read from it (write access is unnecessary):</p><pre><code>sudo setfacl -m u:$USER:r /dev/usbmon1
# Alternatively, if you do not have setfacl installed:
sudo chgrp $USER /dev/ubsmon1 &amp;&amp; sudo chmog g+t /dev/usbmon1</code></pre><p>See also <a href="https://wiki.wireshark.org/CaptureSetup/USB">https://wiki.wireshark.org/CaptureSetup/USB</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '15, 02:41</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p><span>Lekensteyn</span><br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-44759" class="comments-container"></div><div id="comment-tools-44759" class="comment-tools"></div><div class="clear"></div><div id="comment-44759-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

