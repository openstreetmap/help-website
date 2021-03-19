+++
type = "question"
title = "What equipment can I use to capture bluetooth packets?"
description = '''http://wiki.wireshark.org/CaptureSetup/Bluetooth This page mentioned that I can use wireshark capture Bluetooth package,can I use a Bluetooth adapter to capture?'''
date = "2012-11-12T17:22:00Z"
lastmod = "2012-11-12T20:16:00Z"
weight = 15837
keywords = [ "wireless", "equipment", "bluetooth" ]
aliases = [ "/questions/15837" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What equipment can I use to capture bluetooth packets?](/questions/15837/what-equipment-can-i-use-to-capture-bluetooth-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15837-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15837-score" class="post-score" title="current number of votes">0</div><span id="post-15837-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p><a href="http://wiki.wireshark.org/CaptureSetup/Bluetooth">http://wiki.wireshark.org/CaptureSetup/Bluetooth</a> This page mentioned that I can use wireshark capture Bluetooth package,can I use a Bluetooth adapter to capture?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireless" rel="tag" title="see questions tagged &#39;wireless&#39;">wireless</span> <span class="post-tag tag-link-equipment" rel="tag" title="see questions tagged &#39;equipment&#39;">equipment</span> <span class="post-tag tag-link-bluetooth" rel="tag" title="see questions tagged &#39;bluetooth&#39;">bluetooth</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Nov '12, 17:22</strong></p><img src="https://secure.gravatar.com/avatar/985fc283889fe7c82e9befb923ea92ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kanon2000&#39;s gravatar image" /><p><span>kanon2000</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kanon2000 has no accepted answers">0%</span></p></div></div><div id="comments-container-15837" class="comments-container"></div><div id="comment-tools-15837" class="comment-tools"></div><div class="clear"></div><div id="comment-15837-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15838"></span>

<div id="answer-container-15838" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15838-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15838-score" class="post-score" title="current number of votes">1</div><span id="post-15838-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As that page says, "Bluetooth capture support is supported on Linux in Wireshark with libpcap 0.9.6 and later, if the kernel includes the BlueZ Bluetooth stack; starting with the 2.4.6 kernel, the BlueZ stack was incorporated into the mainline kernel."</p><p>So, if you have a Linux machine running either an older kernel with the BlueZ stack added to it or a 2.4.6 kernel or later, and with libpcap 0.9.6 or later, and it has a Bluetooth adapter, you should be able to capture on it.</p><p>Note, however, that this captures traffic between the CPU and the Bluetooth controller, so it only captures traffic your machine sends or receives. If you want to do passive "promiscuous" Bluetooth capture, to see traffic between two machines neither of which is your machine, you may need your own special hardware and software; <a href="http://static.usenix.org/event/woot07/tech/full_papers/spill/spill_html/">BlueSniff: Eve meets Alice and Bluetooth</a> from a 2007 conference, or look at <a href="http://greatscottgadgets.com/ubertoothone/">Ubertooth</a>/<a href="http://ubertooth.sourceforge.net">Project Ubertooth</a> and the <a href="http://ubertooth.blogspot.com">Project Ubertooth blog</a>. There is currently no libpcap support for Ubertooth, so Wireshark can't capture on it. However, there's apparently <a href="http://ubertooth.sourceforge.net/usage/start/">a plugin</a> for <a href="http://www.kismetwireless.net">Kismet</a> that lets you capture and <a href="https://sourceforge.net/p/libbtbb/code/ci/623ee465f3a4fd15c13cafb237f01ebf7f20fc33/tree/wireshark/">a Wireshark plugin</a> to handle those capture files - try Googling for</p><pre><code>ubertooth wireshark</code></pre><p>to find pages on how to build and install it - for example, there are several pages of using Ubertooth on OS X, and there are probably similar pages to help on Linux (I don't know about Windows or about other UN*Xes).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '12, 18:34</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Nov '12, 20:15</strong> </span></p></div></div><div id="comments-container-15838" class="comments-container"><span id="15839"></span><div id="comment-15839" class="comment"><div id="post-15839-score" class="comment-score"></div><div class="comment-text"><p>Thank you!I give it a try.</p></div><div id="comment-15839-info" class="comment-info"><span class="comment-age">(12 Nov '12, 19:11)</span> <span class="comment-user userinfo">kanon2000</span></div></div><span id="15840"></span><div id="comment-15840" class="comment"><div id="post-15840-score" class="comment-score"></div><div class="comment-text"><p>I've updated the answer to note that what you can capture is traffic to or from the machine on which you're running Wireshark; if you want to do passive promiscuous Bluetooth capture, that'd be harder.</p></div><div id="comment-15840-info" class="comment-info"><span class="comment-age">(12 Nov '12, 20:10)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="15841"></span><div id="comment-15841" class="comment"><div id="post-15841-score" class="comment-score"></div><div class="comment-text"><p>I've also added some links to pages discussing promiscuous Bluetooth sniffing and using Wireshark with the captures. I haven't tried any of that software (or hardware!), so I can't give advice or answer questions.</p></div><div id="comment-15841-info" class="comment-info"><span class="comment-age">(12 Nov '12, 20:16)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-15838" class="comment-tools"></div><div class="clear"></div><div id="comment-15838-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

