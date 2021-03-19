+++
type = "question"
title = "Mergecap combine multiple named pipes"
description = '''I am looking for a way to combine multiple named pipes containing pcap data into one single pipe that can be used as input into Wireshark. As a fictitious and non-working example, I am trying to do something like this: mkfifo trace1 mkfifo trace2 mkfifo trace3 mergecap -w - trace1 trace2 trace3 | wi...'''
date = "2017-02-16T13:36:00Z"
lastmod = "2017-02-17T14:31:00Z"
weight = 59484
keywords = [ "combine", "tcpdump", "mergecap", "tshark", "wireshark" ]
aliases = [ "/questions/59484" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Mergecap combine multiple named pipes](/questions/59484/mergecap-combine-multiple-named-pipes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59484-score" class="post-score" title="current number of votes">0</div><span id="post-59484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am looking for a way to combine multiple named pipes containing pcap data into one single pipe that can be used as input into Wireshark. As a fictitious and non-working example, I am trying to do something like this:</p><pre><code>mkfifo trace1
mkfifo trace2
mkfifo trace3
mergecap -w - trace1 trace2 trace3 | wireshark -k -i - &amp;
tcpdump -i eth1 -s0 -w - &gt; trace1 &amp;
tcpdump -i eth2 -s0 -w - &gt; trace2 &amp;
tcpdump -i eth3 -s0 -w - &gt; trace3 &amp;</code></pre><p>(Of course, tshark would be much better suited to this specific example as I could specify multiple interfaces with it and obviate the need of named pipes altogether. In reality however, each of the tcpdumps will be executed on different remote hosts and their output will be piped to the local machine.)</p><p>I am trying to find a way to merge those separate streams into one so that I can view them all in wireshark simultaneously and in real-time. If mergecap cannot do it, are there any other tools you have used for this? Also, I have a tool that should merged arbitrary named pipes, but in order to make sure the packet data is not scrambled, I need to provide a separator. Does the pcap format have a standard separator between packets?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-combine" rel="tag" title="see questions tagged &#39;combine&#39;">combine</span> <span class="post-tag tag-link-tcpdump" rel="tag" title="see questions tagged &#39;tcpdump&#39;">tcpdump</span> <span class="post-tag tag-link-mergecap" rel="tag" title="see questions tagged &#39;mergecap&#39;">mergecap</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '17, 13:36</strong></p><img src="https://secure.gravatar.com/avatar/e96b0196e8e968b1a2d8f6ddfda87ab1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lemurshark&#39;s gravatar image" /><p><span>Lemurshark</span><br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lemurshark has no accepted answers">0%</span></p></div></div><div id="comments-container-59484" class="comments-container"></div><div id="comment-tools-59484" class="comment-tools"></div><div class="clear"></div><div id="comment-59484-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="59486"></span>

<div id="answer-container-59486" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59486-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59486-score" class="post-score" title="current number of votes">0</div><span id="post-59486-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Does the pcap format have a standard separator between packets?</p></blockquote><p>No. <a href="http://www.tcpdump.org/manpages/pcap-savefile.5.html">The pcap format</a> has a fixed-length header at the beginning of a file, followed by a sequence of records for packets; each packet record has a fixed-length header that includes a time stamp, an "on the wire" length for the packet, and a "number of bytes captured" length for the packet, followed by the packet data. The "number of bytes captured" length specifies the number of bytes of packet data.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '17, 15:18</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-59486" class="comments-container"></div><div id="comment-tools-59486" class="comment-tools"></div><div class="clear"></div><div id="comment-59486-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="59519"></span>

<div id="answer-container-59519" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59519-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59519-score" class="post-score" title="current number of votes">0</div><span id="post-59519-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In case you're unaware, Wireshark can read from multiple interfaces. I have experimented a bit with a possible solution for you using <code>tcpdump</code> and <code>libpcap</code> versions 4.9.0 and 1.8.1, respectively. Below is the contents of a script I ran to successfully test this. Perhaps it's useful to you?</p><p><code></code></p><code></code><pre><code>#!/bin/sh

# Remove pipes in case there are any unread data.
# (May not be completely necessary but doesn&#39;t hurt.)
rm -f sharkfin1 sharkfin2

# Create pipes, 1 per interface:
mkfifo sharkfin1 &amp;&gt; /dev/null
mkfifo sharkfin2 &amp;&gt; /dev/null

# Start wireshark, reading from sharkfin1 and sharkfin2 pipes
wireshark -k -i sharkfin1 -i sharkfin2 &amp;

# Begin capture on relevant interfaces and write packets to pipes
filter=icmp
tcpdump --immediate-mode -U -i eth0 -w sharkfin1 $filter &amp;
tcpdump --immediate-mode -U -i eth1 -w sharkfin2 $filter &amp;
wait</code></pre></code><p><code></code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '17, 14:31</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-59519" class="comments-container"></div><div id="comment-tools-59519" class="comment-tools"></div><div class="clear"></div><div id="comment-59519-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

