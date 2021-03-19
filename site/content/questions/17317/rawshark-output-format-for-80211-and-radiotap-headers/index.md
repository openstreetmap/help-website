+++
type = "question"
title = "rawshark output format for 802.11 and radiotap headers"
description = '''Hi, I want to use rawshark to read packets from pipe and print some useful information for me. Here&#x27;s the scenario.  1. Remote machine with wireless interface in monitor mode capturing with tcpdump and pipe to netcat  2. Another remote machine read from machine 1 netcat stream and pipes data to raws...'''
date = "2012-12-30T02:25:00Z"
lastmod = "2012-12-30T14:48:00Z"
weight = 17317
keywords = [ "rawshark", "802.11" ]
aliases = [ "/questions/17317" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [rawshark output format for 802.11 and radiotap headers](/questions/17317/rawshark-output-format-for-80211-and-radiotap-headers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17317-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17317-score" class="post-score" title="current number of votes">0</div><span id="post-17317-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I want to use rawshark to read packets from pipe and print some useful information for me.</p><p>Here's the scenario. 1. Remote machine with wireless interface in monitor mode capturing with tcpdump and pipe to netcat 2. Another remote machine read from machine 1 netcat stream and pipes data to rawshark 3. rawshark have to output parsed information in useful for me format.</p><p>So far I try to pipe previous captured data (local file) to rawshark and it's fine (cat test.pcap | rawshark -s -r - -d encap:105). But I can't find the right value for the '-F' flag to make it display package source mac address and radiotap header information like signal strength. I was trying with -F <a href="http://wlan.sa">wlan.sa</a> -F radiotap.dbm_antsignal</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rawshark" rel="tag" title="see questions tagged &#39;rawshark&#39;">rawshark</span> <span class="post-tag tag-link-802.11" rel="tag" title="see questions tagged &#39;802.11&#39;">802.11</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Dec '12, 02:25</strong></p><img src="https://secure.gravatar.com/avatar/c97c06010507974eb0931fad93ae9600?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nerform&#39;s gravatar image" /><p><span>nerform</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nerform has no accepted answers">0%</span></p></div></div><div id="comments-container-17317" class="comments-container"></div><div id="comment-tools-17317" class="comment-tools"></div><div class="clear"></div><div id="comment-17317-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17320"></span>

<div id="answer-container-17320" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17320-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17320-score" class="post-score" title="current number of votes">1</div><span id="post-17320-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="nerform has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please try this:</p><blockquote><p><code>rawshark -nr input.pcap -s -d proto:radiotap -F wlan.sa -F radiotap.dbm_antsignal</code></p></blockquote><p>It works with this sample file.</p><blockquote><p><code>http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=view&amp;target=mesh.pcap</code><br />
</p></blockquote><p>If it <strong>does not work</strong> with your capture, then your version of tcpdump does not provide a radiotap header.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Dec '12, 14:44</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-17320" class="comments-container"><span id="17323"></span><div id="comment-17323" class="comment"><div id="post-17323-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much Kurt. It works!</p></div><div id="comment-17323-info" class="comment-info"><span class="comment-age">(30 Dec '12, 14:48)</span> <span class="comment-user userinfo">nerform</span></div></div></div><div id="comment-tools-17320" class="comment-tools"></div><div class="clear"></div><div id="comment-17320-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

