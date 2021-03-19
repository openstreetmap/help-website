+++
type = "question"
title = "Display mac addresses from wifi clients"
description = '''Hi there, Is there a way to capture and display the mac addresses of devices with wifi enabled. I saw that the probe statement can be use full for this but i cannot find information to filter on that. Thanks for your Help. //p'''
date = "2014-05-23T05:30:00Z"
lastmod = "2014-05-26T16:58:00Z"
weight = 33019
keywords = [ "filter", "probe", "mac-address" ]
aliases = [ "/questions/33019" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Display mac addresses from wifi clients](/questions/33019/display-mac-addresses-from-wifi-clients)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33019-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33019-score" class="post-score" title="current number of votes">0</div><span id="post-33019-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>Is there a way to capture and display the mac addresses of devices with wifi enabled. I saw that the probe statement can be use full for this but i cannot find information to filter on that.</p><p>Thanks for your Help.</p><p>//p</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-probe" rel="tag" title="see questions tagged &#39;probe&#39;">probe</span> <span class="post-tag tag-link-mac-address" rel="tag" title="see questions tagged &#39;mac-address&#39;">mac-address</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 May '14, 05:30</strong></p><img src="https://secure.gravatar.com/avatar/37ec99960fe6fd0729f26d077b34b0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal1969&#39;s gravatar image" /><p><span>Pascal1969</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal1969 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 May '14, 02:01</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-33019" class="comments-container"><span id="33023"></span><div id="comment-33023" class="comment"><div id="post-33023-score" class="comment-score"></div><div class="comment-text"><p>Okay, a relative of me found this out....</p><p>wlan.fc.subtype == 0x04 as display filter.</p><p>It displays only de wlan devices that are probing.</p><p>Anybody nows how to change this in a capture filter?</p></div><div id="comment-33023-info" class="comment-info"><span class="comment-age">(23 May '14, 08:48)</span> <span class="comment-user userinfo">Pascal1969</span></div></div></div><div id="comment-tools-33019" class="comment-tools"></div><div class="clear"></div><div id="comment-33019-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33097"></span>

<div id="answer-container-33097" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33097-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33097-score" class="post-score" title="current number of votes">0</div><span id="post-33097-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Is there a way to <strong>capture and display the mac addresses</strong> of devices with <strong>wifi enabled</strong></p></blockquote><p>sure, just use a capture device that is able to operate in <a href="http://wiki.wireshark.org/CaptureSetup/WLAN#Monitor_mode">wifi monitor mode</a> to capture the wlan/wifi traffic in its vicinity.</p><blockquote><p><a href="http://wiki.wireshark.org/CaptureSetup/WLAN">http://wiki.wireshark.org/CaptureSetup/WLAN</a></p></blockquote><p>On Windows, you'll need</p><ul><li>either a sniffer that does <strong>not</strong> rely on WinPcap (as WinPcap does not support monitor mode)</li><li>or a special capture device like <a href="http://www.riverbed.com/products/performance-management-control/network-performance-management/wireless-packet-capture.html">AirPcap</a>.</li></ul><p>On Linux/Unix/*BSD you can use whatever wlan/wifi device is supported by your kernel.</p><p>After you've finished capturing, you'll find an overview of the MAC addresses within several statistics functions (GUI: Statistics).</p><p>You can also use <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark</a> to print the MAC addresses.</p><blockquote><p>tshark -nr input.pcap -T fields -e wlan.addr</p></blockquote><p>Additionally to wlan.addr you can use any of the fields described here: <a href="http://www.wireshark.org/docs/dfref/w/wlan.html">http://www.wireshark.org/docs/dfref/w/wlan.html</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 May '14, 16:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-33097" class="comments-container"></div><div id="comment-tools-33097" class="comment-tools"></div><div class="clear"></div><div id="comment-33097-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

