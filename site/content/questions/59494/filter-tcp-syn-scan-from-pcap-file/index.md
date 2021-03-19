+++
type = "question"
title = "Filter TCP SYN scan from pcap file?"
description = '''Hello, I want to filter only the SYN packets from TCP SYN scan (both for open ports(SYN-&amp;gt;SYN/ACK-&amp;gt;RST) and closed ports(SYN-&amp;gt;RST/ACK)) from a pcap file. I have written a following script to do the same and it seems working for me. for stream in `tshark -nr capture.pcap -Y &quot;(ip.dst==192.68.1...'''
date = "2017-02-17T04:35:00Z"
lastmod = "2017-02-17T08:17:00Z"
weight = 59494
keywords = [ "port-scanning", "pcap", "syn", "snort", "tshark" ]
aliases = [ "/questions/59494" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Filter TCP SYN scan from pcap file?](/questions/59494/filter-tcp-syn-scan-from-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59494-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59494-score" class="post-score" title="current number of votes">0</div><span id="post-59494-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I want to filter only the SYN packets from TCP SYN scan (both for open ports(SYN-&gt;SYN/ACK-&gt;RST) and closed ports(SYN-&gt;RST/ACK)) from a pcap file.</p><p>I have written a following script to do the same and it seems working for me.</p><pre><code>for stream in `tshark -nr  capture.pcap -Y &quot;(ip.dst==192.68.167.00/24 &amp;&amp; tcp.seq==1 &amp;&amp; tcp.flags.reset==1 &amp;&amp; tcp.flags.ack==0)||(tcp.flags.reset==1 &amp;&amp; tcp.flags.ack==1 &amp;&amp; tcp.ack==1)&quot; -T fields -e tcp.stream | sort -n | uniq`

do
  tshark -r capture.pcap -w ./portscans/stream_$stream.pcap -Y &quot;ip.dst==192.68.167.00/24 &amp;&amp; tcp.seq==0 &amp;&amp; tcp.flags.syn==1 &amp;&amp; tcp.flags.ack==0 &amp;&amp; tcp.stream eq $stream&quot;
done</code></pre><p>But the above script is taking hell out of time to run it.. It is taking more than a day to filter out packets from a 150MB pcap file.</p><p>Can someone suggest me any other method to do the same(with tshark or snort)?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-port-scanning" rel="tag" title="see questions tagged &#39;port-scanning&#39;">port-scanning</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-syn" rel="tag" title="see questions tagged &#39;syn&#39;">syn</span> <span class="post-tag tag-link-snort" rel="tag" title="see questions tagged &#39;snort&#39;">snort</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Feb '17, 04:35</strong></p><img src="https://secure.gravatar.com/avatar/95e9674b7a67d58ada813e0c6bc38d84?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="subinjp&#39;s gravatar image" /><p><span>subinjp</span><br />
<span class="score" title="41 reputation points">41</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="subinjp has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Feb '17, 04:42</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-59494" class="comments-container"></div><div id="comment-tools-59494" class="comment-tools"></div><div class="clear"></div><div id="comment-59494-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59501"></span>

<div id="answer-container-59501" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59501-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59501-score" class="post-score" title="current number of votes">0</div><span id="post-59501-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>For starters you could see if you can apply the '<code>in</code>' operator to <code>tcp.stream</code>, to get an expression like '<code>tcp.stream in { n m ...}</code>', where <code>n</code> and <code>m</code> are stream numbers collected before. Although that would give you one single output file, so you may have to split that up afterwards.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '17, 08:08</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-59501" class="comments-container"><span id="59503"></span><div id="comment-59503" class="comment"><div id="post-59503-score" class="comment-score"></div><div class="comment-text"><p><span>@jaap</span> Thanks for your reply. In fact I dont want to split packets in to different files. But I did not get what do you mean by it? Could you write the script below or describe it little more?</p></div><div id="comment-59503-info" class="comment-info"><span class="comment-age">(17 Feb '17, 08:17)</span> <span class="comment-user userinfo">subinjp</span></div></div></div><div id="comment-tools-59501" class="comment-tools"></div><div class="clear"></div><div id="comment-59501-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

