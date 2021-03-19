+++
type = "question"
title = "Why can&#x27;t Kali Linux running on a virtual box detect the wireless adapter/card and instead uses an ethernet connection?"
description = ''' Host : Windows 8.1 Client Kali linux 3.12 Debian amd 64 WLAN card: Intel centrino Wirelss n-2230  The &quot;capture packet using monitor mode&quot; cannot be seen while running Wireshark in Kali Linux. Kindly help solving the issue'''
date = "2015-02-08T17:20:00Z"
lastmod = "2015-02-09T15:02:00Z"
weight = 39705
keywords = [ "wireshark" ]
aliases = [ "/questions/39705" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why can't Kali Linux running on a virtual box detect the wireless adapter/card and instead uses an ethernet connection?](/questions/39705/why-cant-kali-linux-running-on-a-virtual-box-detect-the-wireless-adaptercard-and-instead-uses-an-ethernet-connection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39705-score" class="post-score" title="current number of votes">0</div><span id="post-39705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><ul><li>Host : Windows 8.1</li><li>Client Kali linux 3.12 Debian amd 64</li><li>WLAN card: Intel centrino Wirelss n-2230</li></ul><p>The "capture packet using monitor mode" cannot be seen while running Wireshark in Kali Linux. Kindly help solving the issue</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Feb '15, 17:20</strong></p><img src="https://secure.gravatar.com/avatar/ee9ee4d7530bdb0b4c7d813a74df10ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="peterquinn&#39;s gravatar image" /><p><span>peterquinn</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="peterquinn has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> closed <strong>09 Feb '15, 05:43</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-39705" class="comments-container"><span id="39712"></span><div id="comment-39712" class="comment"><div id="post-39712-score" class="comment-score"></div><div class="comment-text"><p>This question would be better directed to the Kali Linux forum, or <a href="http://docs.kali.org/troubleshooting/troubleshooting-wireless-driver-issues">documentation</a>.</p></div><div id="comment-39712-info" class="comment-info"><span class="comment-age">(09 Feb '15, 05:43)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-39705" class="comment-tools"></div><div class="clear"></div><div id="comment-39705-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39721"></span>

<div id="answer-container-39721" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39721-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39721-score" class="post-score" title="current number of votes">0</div><span id="post-39721-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Why can't Kali Linux <strong>running on a virtual box</strong> detect the wireless adapter/card<br />
WLAN card: Intel centrino Wirelss n-2230</p></blockquote><p>because you <strong>cannot map real hardware</strong> into the virtual machine with <strong>Virtualbox</strong>. If you need a wifi adapter in your virtual machine, please buy a USB wifi adapter that is supported by Kali.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Feb '15, 15:02</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-39721" class="comments-container"></div><div id="comment-tools-39721" class="comment-tools"></div><div class="clear"></div><div id="comment-39721-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

