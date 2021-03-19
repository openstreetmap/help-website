+++
type = "question"
title = "Wireshark support for USB Alfa Network wireless adapter AWUS036NH"
description = '''I have an Alfa Network USB wireless adapter AWUS036NH. Can it be used to capture wireless management traffic in Wireshark? It does not show up in the list of interfaces in Wireshark. I was told it provided support within Windows 7.'''
date = "2013-09-25T10:53:00Z"
lastmod = "2013-09-25T12:25:00Z"
weight = 25229
keywords = [ "capture" ]
aliases = [ "/questions/25229" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark support for USB Alfa Network wireless adapter AWUS036NH](/questions/25229/wireshark-support-for-usb-alfa-network-wireless-adapter-awus036nh)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25229-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25229-score" class="post-score" title="current number of votes">0</div><span id="post-25229-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an Alfa Network USB wireless adapter AWUS036NH. Can it be used to capture wireless management traffic in Wireshark? It does not show up in the list of interfaces in Wireshark. I was told it provided support within Windows 7.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Sep '13, 10:53</strong></p><img src="https://secure.gravatar.com/avatar/996cfc675ec424afea22c5da0d8c9722?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mfuszner&#39;s gravatar image" /><p><span>mfuszner</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mfuszner has no accepted answers">0%</span></p></div></div><div id="comments-container-25229" class="comments-container"></div><div id="comment-tools-25229" class="comment-tools"></div><div class="clear"></div><div id="comment-25229-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25235"></span>

<div id="answer-container-25235" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-25235-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-25235-score" class="post-score" title="current number of votes">0</div><span id="post-25235-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to capture wlan/wifi traffic on Windows, you need something different than <a href="http://www.winpcap.org/">WinPcap</a> (the library used by Wireshark), because WinPcap does not support <a href="http://wiki.wireshark.org/CaptureSetup/WLAN#Monitor_mode">monitor mode</a>, regardless of the device used.</p><p>So, in short: You can't use Wireshark on Windows to capture wlan/wifi traffic with the AWUS036NH.</p><p>Your options are:</p><ul><li>Buy an <a href="http://www.riverbed.com/de/products/cascade/wireshark_enhancements/airpcap.php">AirPcap</a> adapter (rather expensive compared to the AWUS036NH, for private use)</li><li>Capture on Linux. Several distributions provide a driver for the AWUS036NH (e.g. <a href="http://www.kali.org/">Kali Linux</a>)</li><li>On Windows: Try to capture with <a href="http://www.microsoft.com/en-us/download/details.aspx?id=4865">Microsoft Network Monitor</a>. Maybe it detects the USB adapter and is able to enable/handle monitor mode for it.</li></ul><p>See also here: <a href="https://www.google.com/?q=site%3Aask.wireshark.org+AWUS036">https://www.google.com/?q=site%3Aask.wireshark.org+AWUS036</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Sep '13, 12:25</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Sep '13, 12:31</strong> </span></p></div></div><div id="comments-container-25235" class="comments-container"></div><div id="comment-tools-25235" class="comment-tools"></div><div class="clear"></div><div id="comment-25235-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

