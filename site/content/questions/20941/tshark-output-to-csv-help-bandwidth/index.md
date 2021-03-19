+++
type = "question"
title = "tshark output to csv help (bandwidth)"
description = '''I am trying to figure how to output what was the bandwidth useage at the time the packets were logged. This is what my command line looks like.  tshark -nr 3.pcap -T fields -E separator=, -E header=y -e frame.number -e frame.time -e frame.len -e eth.type -e eth.src -e eth.dst -e ip.len -e ip.id -e i...'''
date = "2013-05-03T13:11:00Z"
lastmod = "2013-05-03T14:31:00Z"
weight = 20941
keywords = [ "bandwidth", "csv", "tshark", "command-line" ]
aliases = [ "/questions/20941" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark output to csv help (bandwidth)](/questions/20941/tshark-output-to-csv-help-bandwidth)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20941-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20941-score" class="post-score" title="current number of votes">0</div><span id="post-20941-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to figure how to output what was the bandwidth useage at the time the packets were logged. This is what my command line looks like.</p><p>tshark -nr 3.pcap -T fields -E separator=, -E header=y -e frame.number -e frame.time -e frame.len -e eth.type -e eth.src -e eth.dst -e ip.len -e ip.id -e ip.flags -e ip.dst -e ip.src -e ip.proto -e ip.ttl &gt;3.csv</p><p>What do I need to enter to get bandwidth or do I have make something in excel do it?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-bandwidth" rel="tag" title="see questions tagged &#39;bandwidth&#39;">bandwidth</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-command-line" rel="tag" title="see questions tagged &#39;command-line&#39;">command-line</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 May '13, 13:11</strong></p><img src="https://secure.gravatar.com/avatar/b60c5d6f09d2af166e99c1db849dd7e5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spanky55amg&#39;s gravatar image" /><p><span>spanky55amg</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spanky55amg has no accepted answers">0%</span></p></div></div><div id="comments-container-20941" class="comments-container"><span id="20944"></span><div id="comment-20944" class="comment"><div id="post-20944-score" class="comment-score"></div><div class="comment-text"><p>More specifically... How do I get bytes? If I can go into Statisitcs &gt; Endpoints&gt; IPv4 and see the bytes, how do I get that from the command line? Total perfered but maybe with Tx and Rx bytes too.</p></div><div id="comment-20944-info" class="comment-info"><span class="comment-age">(03 May '13, 13:39)</span> <span class="comment-user userinfo">spanky55amg</span></div></div></div><div id="comment-tools-20941" class="comment-tools"></div><div class="clear"></div><div id="comment-20941-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20945"></span>

<div id="answer-container-20945" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20945-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20945-score" class="post-score" title="current number of votes">1</div><span id="post-20945-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is a similar tool in tshark.</p><blockquote><p><code>tshark -nr data.pcap -z conv,ip -q</code><br />
</p></blockquote><p>That will print a similar overview as the Endpoint statistics (see <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark man page</a> for more statistics options). <strong>However</strong> it does <strong>not</strong> print the throughput. As it <strong>does</strong> print the duration and the amount of bytes it is easy to calculate the throughput. If you need a time series of the throughput, exel or gnuplot are your friends. Plot the fields frame.number and ip.len for a certain stream.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 May '13, 14:16</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 May '13, 14:16</strong> </span></p></div></div><div id="comments-container-20945" class="comments-container"><span id="20947"></span><div id="comment-20947" class="comment"><div id="post-20947-score" class="comment-score"></div><div class="comment-text"><p>I was looking at that too. Thats why I wondered if I could get something like that out on a csv.</p></div><div id="comment-20947-info" class="comment-info"><span class="comment-age">(03 May '13, 14:26)</span> <span class="comment-user userinfo">spanky55amg</span></div></div><span id="20948"></span><div id="comment-20948" class="comment"><div id="post-20948-score" class="comment-score">1</div><div class="comment-text"><p>perl/python/lua and/or Excel will extract whatever you need/want from that csv ;-)</p></div><div id="comment-20948-info" class="comment-info"><span class="comment-age">(03 May '13, 14:31)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-20945" class="comment-tools"></div><div class="clear"></div><div id="comment-20945-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

