+++
type = "question"
title = "using follow udp stream&#x27; in script to dealing thousands pcap files"
description = '''I have thousands of pcap file 100M each which contains the data i need transferred from my device by UDP protocol. I can use &#x27;follow udp stream command&#x27; in the wireshark desktop manually and save it into a raw file one by one, and later further coding with python, but that would be very time consumi...'''
date = "2017-07-10T19:32:00Z"
lastmod = "2017-07-10T22:26:00Z"
weight = 62653
keywords = [ "udp" ]
aliases = [ "/questions/62653" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [using follow udp stream' in script to dealing thousands pcap files](/questions/62653/using-follow-udp-stream-in-script-to-dealing-thousands-pcap-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62653-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62653-score" class="post-score" title="current number of votes">0</div><span id="post-62653-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have thousands of pcap file 100M each which contains the data i need transferred from my device by UDP protocol. I can use 'follow udp stream command' in the wireshark desktop manually and save it into a raw file one by one, and later further coding with python, but that would be very time consuming.</p><p>Is there any way i can using batching/script to save all the pcap files into raw data files automatically?</p><p>Much appreciated!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '17, 19:32</strong></p><img src="https://secure.gravatar.com/avatar/5c7f90f23654a6f637a2c1955a6fbd66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tree0520&#39;s gravatar image" /><p><span>tree0520</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tree0520 has no accepted answers">0%</span></p></div></div><div id="comments-container-62653" class="comments-container"></div><div id="comment-tools-62653" class="comment-tools"></div><div class="clear"></div><div id="comment-62653-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62654"></span>

<div id="answer-container-62654" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62654-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62654-score" class="post-score" title="current number of votes">2</div><span id="post-62654-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, create a script that feeds the capture files to <code>tshark</code> and pass it the command line option -z "follow,udp,...". See <a href="https://www.wireshark.org/docs/man-pages/tshark.html">the manual</a> for more details.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '17, 22:26</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-62654" class="comments-container"></div><div id="comment-tools-62654" class="comment-tools"></div><div class="clear"></div><div id="comment-62654-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

