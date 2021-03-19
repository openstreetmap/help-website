+++
type = "question"
title = "Capture streaming traffic from Roku"
description = '''I need to know if Wireshark can be used for gathering log files from a Roku playing TV shows, movies etc. using Sling TV?'''
date = "2016-02-03T16:48:00Z"
lastmod = "2016-02-04T08:22:00Z"
weight = 49798
keywords = [ "tv", "roku", "streaming" ]
aliases = [ "/questions/49798" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture streaming traffic from Roku](/questions/49798/capture-streaming-traffic-from-roku)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49798-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49798-score" class="post-score" title="current number of votes">0</div><span id="post-49798-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need to know if Wireshark can be used for gathering log files from a Roku playing TV shows, movies etc. using Sling TV?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tv" rel="tag" title="see questions tagged &#39;tv&#39;">tv</span> <span class="post-tag tag-link-roku" rel="tag" title="see questions tagged &#39;roku&#39;">roku</span> <span class="post-tag tag-link-streaming" rel="tag" title="see questions tagged &#39;streaming&#39;">streaming</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Feb '16, 16:48</strong></p><img src="https://secure.gravatar.com/avatar/02e2e010f5080aae9578a00eb03dec09?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lendab&#39;s gravatar image" /><p><span>lendab</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lendab has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Feb '16, 06:41</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-49798" class="comments-container"><span id="49808"></span><div id="comment-49808" class="comment"><div id="post-49808-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by log files?</p><p>Roku works by streaming media over the WiFi network. Wireshark is part of the solution to capture WiFi frames. You will also need a linux or MAC machine, a WiFi adapter and WiFi drivers that can capture all the WiFi traffic from your WLAN (promiscuous mode).</p><p>Now you have the WiFi capture, you have to analyze it. You will be able to see the Roku connect to your WiFi network and then connect to the Sling TV server. You will also be able to see any disconnects. But viewing the actual media over that connection would require you to decrypt the connection to Sling TV. That would require some encryption keys located on the Sling server (i.e., you will not be able to get those keys and thus will not be able to view the media sent over the connection).</p><p>So please provide further details on what you are trying to accomplish.</p></div><div id="comment-49808-info" class="comment-info"><span class="comment-age">(04 Feb '16, 01:50)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="49816"></span><div id="comment-49816" class="comment"><div id="post-49816-score" class="comment-score"></div><div class="comment-text"><p>I am needing to capture the log files from the streaming media. It doesn't sound as though this would work for us unless we have a linux or MAC machine, a WiFi adapter and WiFi drivers. I would welcome anymore insight you might have regarding this issue.</p><p>Thanks,</p><p>Lendab</p></div><div id="comment-49816-info" class="comment-info"><span class="comment-age">(04 Feb '16, 05:48)</span> <span class="comment-user userinfo">lendab</span></div></div><span id="49820"></span><div id="comment-49820" class="comment"><div id="post-49820-score" class="comment-score"></div><div class="comment-text"><p>I've amended the question title as it seems you wish to capture roku traffic, not examine any, possibly non-existent, log files from the roku.</p><p>Capture files and log files are different things here.</p></div><div id="comment-49820-info" class="comment-info"><span class="comment-age">(04 Feb '16, 06:41)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="49828"></span><div id="comment-49828" class="comment"><div id="post-49828-score" class="comment-score"></div><div class="comment-text"><p>It seems like a vocabulary problem. A "log" file is a file (usually but not necessarily a plaintext one) into which an application writes information about the progress of its execution, problems encountered during execution, and eventually also information gathered during execution. It is not normally transmitted over the network as part of normal operation.</p><p>A "capture" file is a file which contains a recording of some events or traffic - in case of Wireshark, the packets captured on a (network) interface.</p><p>To capture the packets on air - yes, you would need linux or MAC machine or an AirPcap adaptor for a Windows machine. But even if you would be able to capture the data transfers between the device running Roku and the video server, you wouldn't be able to decipher the multimedia stream.</p><p>You may be able to decipher the WPA2-encrypted communication between your Roku device and your WiFi Access Point, so that you would be able to see packet headers at IP layer (IP addresses, transport protocol type, ports etc). But the payload of these packets will be encrypted using SSL (or even some other encryption method), which is undecipherable for you unless you could get into the closed system of Roku and make it disclose the keys it uses for SSL on its side. This is possible with e.g. a Mozilla Firefox web browser, but hardly with a closed commercial product like Roku.</p></div><div id="comment-49828-info" class="comment-info"><span class="comment-age">(04 Feb '16, 08:22)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-49798" class="comment-tools"></div><div class="clear"></div><div id="comment-49798-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49818"></span>

<div id="answer-container-49818" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49818-score" class="post-score" title="current number of votes">0</div><span id="post-49818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>OK. Here are some good starting points:</p><ol><li>General knowledge about capturing WiFi traffic using Wireshark = <a href="https://wiki.wireshark.org/CaptureSetup/WLAN">https://wiki.wireshark.org/CaptureSetup/WLAN</a></li><li>How to decrypt WiFi traffic so you can view the upper layers in the protocol stack = <a href="https://wiki.wireshark.org/HowToDecrypt802.11">https://wiki.wireshark.org/HowToDecrypt802.11</a></li></ol><p>Saying all that, Wireshark is the cheapest solution. There are other solutions that provide the entire package (software, adapters, drivers and even training) but they cost money. So if your doing this for your own knowledge, then use Wireshark. But if you are trying to solve a problem and running on a tight development schedule, you might want to investigate other solutions. I can provide some recommendations for you if you like regarding the other solutions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Feb '16, 06:20</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-49818" class="comments-container"></div><div id="comment-tools-49818" class="comment-tools"></div><div class="clear"></div><div id="comment-49818-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

