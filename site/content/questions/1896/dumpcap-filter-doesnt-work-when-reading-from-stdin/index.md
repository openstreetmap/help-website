+++
type = "question"
title = "dumpcap Filter Doesn&#x27;t Work When Reading From stdin?"
description = '''I have a huge file in the pcap format from a dumpcap capture. I am wanting to create a second file that only contains packets going to or from a certain range of MAC address. So I tried doing something like this: dumpcap -f &#x27;eth.src[0:3] == 90:21:55 || eth.dst[0:3] == 90:21:55&#x27; -w htc.pcap -i - &amp;lt;...'''
date = "2011-01-23T11:26:00Z"
lastmod = "2011-01-23T14:32:00Z"
weight = 1896
keywords = [ "filter", "ethernet", "mac", "stdin", "dumpcap" ]
aliases = [ "/questions/1896" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [dumpcap Filter Doesn't Work When Reading From stdin?](/questions/1896/dumpcap-filter-doesnt-work-when-reading-from-stdin)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1896-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1896-score" class="post-score" title="current number of votes">0</div><span id="post-1896-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a huge file in the pcap format from a dumpcap capture. I am wanting to create a second file that only contains packets going to or from a certain range of MAC address. So I tried doing something like this:</p><pre><code>dumpcap -f &#39;eth.src[0:3] == 90:21:55 || eth.dst[0:3] == 90:21:55&#39; -w htc.pcap -i - &lt; wlan1.pcap</code></pre><p>But when I do, the resulting file is the same as the input. The filter syntax works fine in wireshark; is there a different filter syntax that I need to use for dumpcap? Does the dumpcap filter not work when reading from stdin?</p><p>I'm using Dumpcap 1.2.11 from Ubuntu 10.10</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-ethernet" rel="tag" title="see questions tagged &#39;ethernet&#39;">ethernet</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-stdin" rel="tag" title="see questions tagged &#39;stdin&#39;">stdin</span> <span class="post-tag tag-link-dumpcap" rel="tag" title="see questions tagged &#39;dumpcap&#39;">dumpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jan '11, 11:26</strong></p><img src="https://secure.gravatar.com/avatar/b6573e846830263ba2ed69503ecde4f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="unraveled&#39;s gravatar image" /><p><span>unraveled</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="unraveled has no accepted answers">0%</span></p></div></div><div id="comments-container-1896" class="comments-container"></div><div id="comment-tools-1896" class="comment-tools"></div><div class="clear"></div><div id="comment-1896-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1898"></span>

<div id="answer-container-1898" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1898-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1898-score" class="post-score" title="current number of votes">0</div><span id="post-1898-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think the problem is that -f is a capture filter syntax &amp; you are using a display filter. I think currently Dumpcap only works with capture filters. What about trying tshark with the filter starting -R instead of -f. This will allow you to read it in using the display filter syntax you have:-</p><p>tshark -r inputfile.pcap -R 'eth.src[0:3] == 90:21:55 || eth.dst[0:3] == 90:21:55' -w outputfile.pcap</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jan '11, 14:32</strong></p><img src="https://secure.gravatar.com/avatar/030196d67dc4e2b8f4ecff65eefdb63e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KeithFrench&#39;s gravatar image" /><p><span>KeithFrench</span><br />
<span class="score" title="121 reputation points">121</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KeithFrench has no accepted answers">0%</span></p></div></div><div id="comments-container-1898" class="comments-container"></div><div id="comment-tools-1898" class="comment-tools"></div><div class="clear"></div><div id="comment-1898-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

