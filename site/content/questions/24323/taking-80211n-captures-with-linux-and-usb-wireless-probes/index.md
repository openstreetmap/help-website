+++
type = "question"
title = "Taking 802.11n captures with Linux and USB wireless probes"
description = '''This is my first question so please be nice. I want to set up my first package capture kit. I need to capture packages on a 802.11n network.  This is what I&#x27;m thinking on getting:  Dell D630 Linux Distro (any flavor but possibly Fedora) USB N wireless Probes HUB  Here are my questions:  If the lapto...'''
date = "2013-09-03T21:27:00Z"
lastmod = "2013-09-05T04:40:00Z"
weight = 24323
keywords = [ "capture-setup", "802.11", "802.11n" ]
aliases = [ "/questions/24323" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Taking 802.11n captures with Linux and USB wireless probes](/questions/24323/taking-80211n-captures-with-linux-and-usb-wireless-probes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24323-score" class="post-score" title="current number of votes">0</div><span id="post-24323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This is my first question so please be nice.</p><p>I want to set up my first package capture kit. I need to capture packages on a 802.11n network.</p><p>This is what I'm thinking on getting:</p><ul><li>Dell D630</li><li>Linux Distro (any flavor but possibly Fedora)</li><li>USB N wireless Probes</li><li>HUB</li></ul><p>Here are my questions:</p><ul><li>If the laptop I get does not have a 802.11n card, can I still buy a hub and USB N wireless probes and still be able to capture packages?</li></ul><p>Thanks, Ricco</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-setup" rel="tag" title="see questions tagged &#39;capture-setup&#39;">capture-setup</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span> <span class="post-tag tag-link-802.11n" rel="tag" title="see questions tagged &#39;802.11n&#39;">802.11n</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Sep '13, 21:27</strong></p><img src="https://secure.gravatar.com/avatar/aab02649c6c5ad77836869be2b1a9d4a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ricco1982&#39;s gravatar image" /><p><span>ricco1982</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ricco1982 has no accepted answers">0%</span></p></div></div><div id="comments-container-24323" class="comments-container"></div><div id="comment-tools-24323" class="comment-tools"></div><div class="clear"></div><div id="comment-24323-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24332"></span>

<div id="answer-container-24332" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24332-score" class="post-score" title="current number of votes">1</div><span id="post-24332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ricco1982 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>If the laptop I get does not have a 802.11n card, can I still buy a hub and USB N wireless probes and still be able to capture packages?</p></blockquote><p>Yes, especially if you run Linux on your Laptop. There are quite some USB adapters that support monitor mode (required to capture wifi traffic of other machines).</p><p>See here:</p><blockquote><p><a href="http://wiki.wireshark.org/CaptureSetup/WLAN#Linux">http://wiki.wireshark.org/CaptureSetup/WLAN#Linux</a><br />
<a href="http://needsec.com/kali-linux-how-to-hack-wifi-tutorial-sniffing-wifi-networks-capturing-packets-backtrack-6/">http://needsec.com/kali-linux-how-to-hack-wifi-tutorial-sniffing-wifi-networks-capturing-packets-backtrack-6/</a><br />
<a href="http://ask.wireshark.org/questions/14148/cannot-scan-with-my-alfa-awus036h">http://ask.wireshark.org/questions/14148/cannot-scan-with-my-alfa-awus036h</a></p></blockquote><p>Regarding the <strong>Hub</strong>. You won't need that for WLAN capturing, unless it is a USB hub to extend the number of USB ports (more wlan adapters to capture from).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Sep '13, 23:54</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Sep '13, 23:59</strong> </span></p></div></div><div id="comments-container-24332" class="comments-container"><span id="24360"></span><div id="comment-24360" class="comment"><div id="post-24360-score" class="comment-score"></div><div class="comment-text"><p>Regarding to the Hub: I was thinking that I would a hub if I need to take a multichannel capture? Thoughts?? so at least 3 wireless N USB adapters + HUB + Linux + wireshark = 802.11n package capture??</p><p>Aprreciate the clear answer.</p></div><div id="comment-24360-info" class="comment-info"><span class="comment-age">(04 Sep '13, 15:37)</span> <span class="comment-user userinfo">ricco1982</span></div></div><span id="24361"></span><div id="comment-24361" class="comment"><div id="post-24361-score" class="comment-score"></div><div class="comment-text"><blockquote><p>if I need to take a multichannel capture? Thoughts??</p></blockquote><p>O.K. if you talk about a USB hub (not a network hub), then I agree. You would need several USB adapters to capture on different channels in parallel.</p></div><div id="comment-24361-info" class="comment-info"><span class="comment-age">(04 Sep '13, 15:40)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="24368"></span><div id="comment-24368" class="comment"><div id="post-24368-score" class="comment-score"></div><div class="comment-text"><p>Kurt,</p><p>you have been very helpful. I really appreciate all the help here. One last question and I promise I'll leave you alone.</p><p>Should I go safe and buy a "dual-band" Wireless-N USB Adapter or only a 2.4 or a 5 GHZ? Any recommendations or preference?</p><p>Thanks,</p></div><div id="comment-24368-info" class="comment-info"><span class="comment-age">(04 Sep '13, 20:06)</span> <span class="comment-user userinfo">ricco1982</span></div></div><span id="24376"></span><div id="comment-24376" class="comment"><div id="post-24376-score" class="comment-score"></div><div class="comment-text"><blockquote><p>One last question and I promise I'll leave you alone.</p></blockquote><p>I hope you will not leave us alone. This site lives from contributions of people interested in Wireshark and network troubleshooting. So, please stay around ;-)</p><blockquote><p>Should I go safe and buy a "dual-band" Wireless-N USB Adapter or only a 2.4 or a 5 GHZ? Any recommendations or preference?</p></blockquote><p>Well, that's hard to say and in general it is not that easy to find a USB adapter with really good Linux support. I'm not going to give an advice regarding a certain adapter. Instead I suggest to look into the forums of Aircrack-NG and Kali/BackTrack Linux. There are several threads discussing the pros and cons of several USB adapters for wireless sniffing.</p></div><div id="comment-24376-info" class="comment-info"><span class="comment-age">(05 Sep '13, 04:40)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-24332" class="comment-tools"></div><div class="clear"></div><div id="comment-24332-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

