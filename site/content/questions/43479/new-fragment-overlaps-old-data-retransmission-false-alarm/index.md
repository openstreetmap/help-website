+++
type = "question"
title = "New fragment overlaps old data (retransmission?) - false alarm?"
description = '''Hello all,  I have a packet capture with an expert analysis that doesn&#x27;t appear to be valid. The packet capture is located at https://www.cloudshark.org/captures/67d2b4aed1d4 Here is what my own window looks like:  What leads me to believe that this is a bug in Wireshark is that there have been no a...'''
date = "2015-06-23T08:59:00Z"
lastmod = "2015-06-23T18:18:00Z"
weight = 43479
keywords = [ "fragmentation", "overlap", "tcp", "error" ]
aliases = [ "/questions/43479" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [New fragment overlaps old data (retransmission?) - false alarm?](/questions/43479/new-fragment-overlaps-old-data-retransmission-false-alarm)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43479-score" class="post-score" title="current number of votes">0</div><span id="post-43479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all, I have a packet capture with an expert analysis that doesn't appear to be valid. The packet capture is located at <a href="https://www.cloudshark.org/captures/67d2b4aed1d4">https://www.cloudshark.org/captures/67d2b4aed1d4</a> Here is what my own window looks like:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Screenshot_2015-06-23_08.38.33.png" alt="alt text" /></p><p>What leads me to believe that this is a bug in Wireshark is that there have been no actual retransmissions. I've opened up the pcap on multiple platforms (win7, mac, ubuntu) and all are reporting the same thing, so it's not a platform-specific issue. Another curious thing is that Cloudshark's expert analysis doesn't show the fragment overlap error. To see it yourself you'll need to download the pcap and view it in a desktop client.</p><p>What I'm trying to do is verify that this is indeed not a network issue but instead anomalous behavior on the part of Wireshark.</p><p>Thanks in advance, -Geoff</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fragmentation" rel="tag" title="see questions tagged &#39;fragmentation&#39;">fragmentation</span> <span class="post-tag tag-link-overlap" rel="tag" title="see questions tagged &#39;overlap&#39;">overlap</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jun '15, 08:59</strong></p><img src="https://secure.gravatar.com/avatar/7d0b9a300c407e94be44caabc8e1fe9f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="glisk&#39;s gravatar image" /><p><span>glisk</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="glisk has no accepted answers">0%</span></p></img></div></div><div id="comments-container-43479" class="comments-container"><span id="43481"></span><div id="comment-43481" class="comment"><div id="post-43481-score" class="comment-score"></div><div class="comment-text"><p>I tried with 1.12.6 on Windows 7 64-bit and it seems like a bug to me. If you turn on TCP's "Validate the TCP checksum if possible" option, those <em>"New fragment overlaps old data (retransmission?)"</em> Expert Infos go away ... although you get 11 TCP <em>"Bad checksum"</em> Expert Infos instead.</p><p>By the way, I also tried with git-master and Wireshark crashed when I loaded the capture file. That might be a separate bug though, perhaps <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=10365">bug 10365</a>.</p></div><div id="comment-43481-info" class="comment-info"><span class="comment-age">(23 Jun '15, 11:10)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="43486"></span><div id="comment-43486" class="comment"><div id="post-43486-score" class="comment-score"></div><div class="comment-text"><p>I have played around withh the options and I found the following combination of Protocol Preferences which causes the strange output.</p><pre><code>TCP: Allow subdissectors to reassemle TCP Streams -&gt; activated
HTTP: Reassemble HTTP bodies spanning multiple TCP segments -&gt; activated</code></pre><p>If one of these two options or both are deactivated, the error does not occur.</p></div><div id="comment-43486-info" class="comment-info"><span class="comment-age">(23 Jun '15, 14:33)</span> <span class="comment-user userinfo">Christian_R</span></div></div></div><div id="comment-tools-43479" class="comment-tools"></div><div class="clear"></div><div id="comment-43479-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43490"></span>

<div id="answer-container-43490" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43490-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43490-score" class="post-score" title="current number of votes">0</div><span id="post-43490-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The problem with this capture is that the HTTP header indicates a Content-Length of 391048208 bytes, which is more than half of the TCP sequence number overlap value, thus defeating Wireshark logic when comparing sequence numbers. So at some point it considers that segment with sequence number 394 is greater than sequence number 391048208.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jun '15, 18:18</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p><span>Pascal Quantin</span><br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-43490" class="comments-container"></div><div id="comment-tools-43490" class="comment-tools"></div><div class="clear"></div><div id="comment-43490-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

