+++
type = "question"
title = "tshark batch file"
description = '''hey all, I am trying to make a windows batch script for tshark. here is the tshark command I use tshark -V -r file.pcap -T fields -E header=y -E separator=% -e wlan.sa -e ip.src -e wlan.da -e ip.dst &amp;gt; file.csv I want to create a batch to ask where the folder is for the pcap, what the name of the ...'''
date = "2011-12-10T13:17:00Z"
lastmod = "2011-12-11T13:12:00Z"
weight = 7894
keywords = [ "tshark", "batch" ]
aliases = [ "/questions/7894" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark batch file](/questions/7894/tshark-batch-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7894-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7894-score" class="post-score" title="current number of votes">0</div><span id="post-7894-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hey all, I am trying to make a windows batch script for tshark.</p><p>here is the tshark command I use</p><p>tshark -V -r file.pcap -T fields -E header=y -E separator=% -e wlan.sa -e ip.src -e wlan.da -e ip.dst &gt; file.csv</p><p>I want to create a batch to ask where the folder is for the pcap, what the name of the pcap is and where to write the csv file.</p><p>Can anyone help me? Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-batch" rel="tag" title="see questions tagged &#39;batch&#39;">batch</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Dec '11, 13:17</strong></p><img src="https://secure.gravatar.com/avatar/a132ed8bc0ebce606397080f40341738?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NetSamSpade&#39;s gravatar image" /><p><span>NetSamSpade</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NetSamSpade has no accepted answers">0%</span></p></div></div><div id="comments-container-7894" class="comments-container"><span id="7895"></span><div id="comment-7895" class="comment"><div id="post-7895-score" class="comment-score">1</div><div class="comment-text"><p>This isn't really a Wireshark (or tshark) question, rather it's about windows batch files. You will be better off asking on a Q&amp;A site that covers those sort of things such as <a href="http://superuser.com/">SuperUser</a> or <a href="http://serverfault.com/">ServerFault</a></p></div><div id="comment-7895-info" class="comment-info"><span class="comment-age">(10 Dec '11, 14:11)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-7894" class="comment-tools"></div><div class="clear"></div><div id="comment-7894-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7897"></span>

<div id="answer-container-7897" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7897-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7897-score" class="post-score" title="current number of votes">1</div><span id="post-7897-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's kinda a Wireshark question as the batch file variable is conflicting with the Wireshark separator value used I think. Try changing that to a comma. Here are a couple ideas -</p><p><strong>test.bat contents:</strong></p><pre><code>tshark -V -r %1 -T fields -E header=y -e wlan.sa -e ip.src -e wlan.da -e ip.dst -E separator=, &gt; %2</code></pre><p><strong>Run sample</strong></p><pre><code>test c:\traces\wlan1.pcap c:\reports\wlan1.csv</code></pre><p>If you want to simplify further, place the CSV into the same directory as the trace file and use the same file name (except for the extension) and include the extensions in the batch file.</p><p><strong>test2.bat contents:</strong></p><pre><code>tshark -V -r %1.pcap -T fields -E header=y -e wlan.sa -e ip.src -e wlan.da -e ip.dst -E separator=, &gt; %1.csv</code></pre><p><strong>Run sample</strong> (against a file called wlan-radiotap.pcap - just sample name)...</p><pre><code>test2 c:\traces\wlan-radiotap</code></pre><p>You'll end up with your new CSV file in the same directory as the trace file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Dec '11, 13:12</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p><span>lchappell ♦</span><br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-7897" class="comments-container"></div><div id="comment-tools-7897" class="comment-tools"></div><div class="clear"></div><div id="comment-7897-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

