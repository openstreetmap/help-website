+++
type = "question"
title = "Wireshark not detecting wireless card"
description = '''Hi, I have been trying to get my wireless card working with wireshark. I&#x27;m using ubuntu, I&#x27;ve used my card in monitor mode lots. Its a USB Ralink rt2870. Any ideas on why it won&#x27;t let me into the wireless options? I&#x27;ve tired putting it in monitor mode before starting wireshark and that doesnt help. ...'''
date = "2010-10-13T02:00:00Z"
lastmod = "2010-10-19T06:29:00Z"
weight = 501
keywords = [ "wireless", "ubuntu" ]
aliases = [ "/questions/501" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark not detecting wireless card](/questions/501/wireshark-not-detecting-wireless-card)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-501-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-501-score" class="post-score" title="current number of votes">0</div><span id="post-501-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have been trying to get my wireless card working with wireshark. I'm using ubuntu, I've used my card in monitor mode lots. Its a USB Ralink rt2870.</p><p>Any ideas on why it won't let me into the wireless options?</p><p>I've tired putting it in monitor mode before starting wireshark and that doesnt help.</p><p>thanks, Chris</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireless" rel="tag" title="see questions tagged &#39;wireless&#39;">wireless</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Oct '10, 02:00</strong></p><img src="https://secure.gravatar.com/avatar/399412ecb7323ec2fb5e18ae99016b87?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chris99&#39;s gravatar image" /><p><span>chris99</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chris99 has no accepted answers">0%</span></p></div></div><div id="comments-container-501" class="comments-container"></div><div id="comment-tools-501" class="comment-tools"></div><div class="clear"></div><div id="comment-501-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="532"></span>

<div id="answer-container-532" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-532-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-532-score" class="post-score" title="current number of votes">0</div><span id="post-532-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Check to make sure your wireless card is in the up state:</p><pre><code>ifconfig wlan0 up</code></pre><p>There is a lot of variation in how to place an interface in monitor mode on Linux systems, depending your Linux kernel version and selected drivers. The Aircrack-ng tool airmon-ng does a great job at figuring out the "right thing to do" automatically:</p><pre><code>airmon-ng start wlan0</code></pre><p>Also double-check your ability to capture on the interface at the command-line with tshark:</p><pre><code>tshark -ni wlan0</code></pre><p>-Josh</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Oct '10, 06:29</strong></p><img src="https://secure.gravatar.com/avatar/8f0c7ef69be39a820dca2c32ca3df1c5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joswr1ght&#39;s gravatar image" /><p><span>joswr1ght</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joswr1ght has no accepted answers">0%</span></p></div></div><div id="comments-container-532" class="comments-container"></div><div id="comment-tools-532" class="comment-tools"></div><div class="clear"></div><div id="comment-532-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

