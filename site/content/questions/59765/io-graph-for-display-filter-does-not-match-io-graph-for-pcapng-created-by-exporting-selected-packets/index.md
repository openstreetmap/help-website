+++
type = "question"
title = "IO graph for display filter does not match IO graph for .pcapng created by exporting selected packets"
description = '''Hello, I&#x27;m trying to Network profile for some embedded applications on 4 different devices. I&#x27;m using a managed switch to mirror the ports connected to each device to my capture pc. During a 2 hour capture, the traffic does not exceed 731 Kbits/sec.  I typically use a display filter to isolate the t...'''
date = "2017-03-01T08:52:00Z"
lastmod = "2017-03-01T10:08:00Z"
weight = 59765
keywords = [ "profile", "export", "iograph" ]
aliases = [ "/questions/59765" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [IO graph for display filter does not match IO graph for .pcapng created by exporting selected packets](/questions/59765/io-graph-for-display-filter-does-not-match-io-graph-for-pcapng-created-by-exporting-selected-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59765-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I'm trying to Network profile for some embedded applications on 4 different devices. I'm using a managed switch to mirror the ports connected to each device to my capture pc. During a 2 hour capture, the traffic does not exceed 731 Kbits/sec.</p><p>I typically use a display filter to isolate the traffic for one device and export the specified packets to a new .pcapng file that is smaller and easier to work with. While trying to find the peak data rates of short bursts of traffic I noticed a discrepancy between the IO graph from the original capture file and the exported capture file. For each capture I added a new graph and applied the same display filter used to export the packets.</p><p>Here is an example display filter, obviously the MAC has been changed:</p><p>(!(ip.addr==172.31.155.43 or ip.addr==172.16.5.122 or ip.addr==172.16.9.109 or ip.addr==172.31.155.95 or ip.addr==172.31.155.145 or arp)) &amp;&amp; (ip.addr==172.31.155.42 or eth.addr == 12:34:56:78:90:12) &amp;&amp; (frame.time &gt;= "Feb 28, 2017 09:10:00.000000" &amp;&amp; frame.time &lt;= "Feb 28, 2017 11:10:00.000000")</p><p>For one device the, difference in data rates for the same burst of traffic is 10031 Bits/s. For another device the difference was 72280 Bits/s. Even more confusing is the fact that in the capture file properties, the "Displayed" statistics from the original capture, when using the display filter used to export traffic for a particular device, match the "Captured" statistics in the exported capture file exactly. I should mention that this is all UDP traffic.<br />
</p><p>If I change the Y axis from bit/s to packets/s, these also do not match...</p><p>What is causing these discrepancies?</p></div><div id="question-tags" class="tags-container tags">profile export iograph</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Mar '17, 08:52</strong></p><img src="https://secure.gravatar.com/avatar/6f78056509e18a48c8793b8df3839693?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joeg4go&#39;s gravatar image" /><p>joeg4go<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joeg4go has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-59765" class="comments-container"></div><div id="comment-tools-59765" class="comment-tools"></div><div class="clear"></div><div id="comment-59765-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59770"></span>

<div id="answer-container-59770" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59770-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think this is the result of a change in start time, resulting in different sampling intervals. For example, in the original capture file, you might have packets split between two intervals whereas in the filtered file, they could fall within the same interval.</p><p>For example, suppose you had this distribution of packets in the original capture file (here <code>X</code> represents where those packets are within the interval):</p><pre><code>0         1         2         3
+----+----+----+----+----+----+----&gt; time (s)
|         |       X | X       |
|&lt;-- 0 --&gt;|&lt;-- 5 --&gt;|&lt;-- 5 --&gt;|</code></pre><p>In this case you would conclude an average of 5 packets per second over the 2 intervals where those packets occur. But once you filter <em>only</em> those packets, you end up with something like:</p><pre><code>0         1         2         3
+----+----+----+----+----+----+----&gt; time (s)
|X   X    |         |         |
|&lt;-- 10--&gt;|&lt;-- 0 --&gt;|&lt;-- 0 --&gt;|</code></pre><p>Now you would conclude an average of 10 packets per second within the interval in which these packets occur. Same data.</p><p>Try reducing your IO Graph time interval from 1 sec to 100ms or 10ms or even 1ms until the values match.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '17, 10:08</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-59770" class="comments-container"><span id="59774"></span><div id="comment-59774" class="comment"><div id="post-59774-score" class="comment-score"></div><div class="comment-text"><p>I have defined my sampling interval within the display filter. If what you're suggesting were true, wouldn't the "Displayed" statistics (from original pcap) and "Captured" statistics (from exported pcap) differ? In my case, they match exactly. The # of packets, timespan, everything matches...</p><p>Displayed 79781 (35.1%) 7199.501 11.1 186.5 14860775 (37.1%) 2064 16 k</p><p>Captured 79781 7199.501 11.1 186.5 14860775 2064 16 k</p></div><div id="comment-59774-info" class="comment-info"><span class="comment-age">(01 Mar '17, 11:30)</span> joeg4go</div></div><span id="59776"></span><div id="comment-59776" class="comment"><div id="post-59776-score" class="comment-score"></div><div class="comment-text"><p><em>I have defined my sampling interval within the display filter.</em></p><p>You have defined the time interval. I'm referring to the graphing interval, which used to be known as the X Axis Tick interval. Try changing it to 100ms (0.1 sec) or smaller as needed.</p></div><div id="comment-59776-info" class="comment-info"><span class="comment-age">(01 Mar '17, 11:55)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-59770" class="comment-tools"></div><div class="clear"></div><div id="comment-59770-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

