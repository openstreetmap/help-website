+++
type = "question"
title = "How to capture wireless traffic in specific channel?"
description = '''I am new to wireshark. I am trying to capture wireless traffic on one specific channel using wlan.channel filter. But it is not working.  I am using version 1.8.7 for wireshark. Can you please let me know exact filter to be used for the same? '''
date = "2013-05-24T00:28:00Z"
lastmod = "2013-05-24T14:00:00Z"
weight = 21433
keywords = [ "dynamic" ]
aliases = [ "/questions/21433" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture wireless traffic in specific channel?](/questions/21433/how-to-capture-wireless-traffic-in-specific-channel)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21433-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21433-score" class="post-score" title="current number of votes">0</div><span id="post-21433-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am new to wireshark. I am trying to capture wireless traffic on one specific channel using wlan.channel filter. But it is not working. I am using version 1.8.7 for wireshark.</p><p>Can you please let me know exact filter to be used for the same?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dynamic" rel="tag" title="see questions tagged &#39;dynamic&#39;">dynamic</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 May '13, 00:28</strong></p><img src="https://secure.gravatar.com/avatar/db51fd4d077e51eebc3e41d550e77352?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RajeAmit&#39;s gravatar image" /><p><span>RajeAmit</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RajeAmit has no accepted answers">0%</span></p></div></div><div id="comments-container-21433" class="comments-container"></div><div id="comment-tools-21433" class="comment-tools"></div><div class="clear"></div><div id="comment-21433-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21465"></span>

<div id="answer-container-21465" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21465-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21465-score" class="post-score" title="current number of votes">2</div><span id="post-21465-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>"wlan.channel" is a display filter, and cannot be used to control what channel you're capturing on. There's no way to specify, with a capture filter, a channel on which to capture.</p><p>(If you already have a capture that includes traffic on multiple channels, and want to display only the traffic on a particular channel, there are display filters that can, in some cases, be used for that, but the filter to use currently depends on the capture file format and the "radio header" format if the file format is pcap or pcap-ng.)</p><p>On Linux, in one of the 1.10 release candidates, you may be able to control the channel on which you're capturing using the wireless toolbar; the wireless toolbar isn't supported in 1.8.x or earlier releases. You might need to enable the wireless toolbar from the "View" menu.</p><p>On Windows, you'd need an AirPcap adapter, and it has its own toolbar to control the channel.</p><p>With earlier releases of Wireshark on Linux, or on OSes other than Linux and Windows, you will probably need to set the Wi-Fi adapter channel on the command line using a system command.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 May '13, 14:00</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-21465" class="comments-container"></div><div id="comment-tools-21465" class="comment-tools"></div><div class="clear"></div><div id="comment-21465-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

