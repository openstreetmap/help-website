+++
type = "question"
title = "Tshark not resolving names and not showing protocol as text when exporting to CSV file"
description = '''Hello,  I have captured a Wireshark file and would like to extract some information using Tshark. The below command is what I have been using: tshark -r c:&#92;temp&#92;test.pcap &amp;gt;c:&#92;temp&#92;test1.csv -T fields -e ip.src_host -e ip.dst_host -e ip.proto Issue 1 = Not resolving IP addresses to network names. ...'''
date = "2012-09-07T12:37:00Z"
lastmod = "2012-09-11T06:36:00Z"
weight = 14126
keywords = [ "ip.proto", "resolution", "tshark", "name" ]
aliases = [ "/questions/14126" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark not resolving names and not showing protocol as text when exporting to CSV file](/questions/14126/tshark-not-resolving-names-and-not-showing-protocol-as-text-when-exporting-to-csv-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14126-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14126-score" class="post-score" title="current number of votes">1</div><span id="post-14126-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have captured a Wireshark file and would like to extract some information using Tshark. The below command is what I have been using:</p><p>tshark -r c:\temp\test.pcap &gt;c:\temp\test1.csv -T fields -e ip.src_host -e ip.dst_host -e ip.proto</p><p>Issue 1 = Not resolving IP addresses to network names. When I captured the PCAP file, I had "Enable Name Resolution". But after exporting to CSV, the IP addresses are not resolved. If I do not export to a CSV file, then the names are resolved to the stdout (screen).</p><p>Issue 2 = The "ip.proto" filed does print the protocol, but as a number. Is there a way to print the protocol as a text. For example, ip.proto = 6 should be printed as TCP.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip.proto" rel="tag" title="see questions tagged &#39;ip.proto&#39;">ip.proto</span> <span class="post-tag tag-link-resolution" rel="tag" title="see questions tagged &#39;resolution&#39;">resolution</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Sep '12, 12:37</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-14126" class="comments-container"></div><div id="comment-tools-14126" class="comment-tools"></div><div class="clear"></div><div id="comment-14126-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="14130"></span>

<div id="answer-container-14130" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14130-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14130-score" class="post-score" title="current number of votes">0</div><span id="post-14130-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Technically, "127.0.0.1", or whatever the IP address is, and 6 are the values of the field, so that's what it's printing.</p><p>The problem is that there really should be a way to, in the <code>-e</code> flag, specify whether the "resolved" value of the field or the "raw" value of the field should be reported (there are probably cases where the raw value is desired); please file a bug for this on the <a href="http://bugs.wireshark.org/">Wireshark Bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '12, 14:32</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-14130" class="comments-container"><span id="14166"></span><div id="comment-14166" class="comment"><div id="post-14166-score" class="comment-score"></div><div class="comment-text"><p>I submitted bug 7712</p></div><div id="comment-14166-info" class="comment-info"><span class="comment-age">(10 Sep '12, 08:50)</span> <span class="comment-user userinfo">Amato_C</span></div></div></div><div id="comment-tools-14130" class="comment-tools"></div><div class="clear"></div><div id="comment-14130-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14167"></span>

<div id="answer-container-14167" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14167-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14167-score" class="post-score" title="current number of votes">0</div><span id="post-14167-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Issue 1 = Not resolving IP addresses to network names. <strong>When I captured</strong> the PCAP file, <strong>I had "Enable Name Resolution"</strong>. But after exporting to CSV, the IP addresses are not resolved. If I do not export to a CSV file, then the names are resolved to the stdout (screen)</p></blockquote><p>This works well on my system (Win7_64, WS 1.8.x). <strong>ip.src_host</strong> and <strong>ip.dst_host</strong> DO print the resolved names, but only if name resolution is enabled while tshark runs.</p><p>From your bug report.</p><blockquote><p>It appears that only known IP addresses are being resolved. Tshark should try to resolve all IP addresses.</p></blockquote><p>What do you mean bye "only known IP addresses" are beeing resolved? Tshark asks the resolver of the OS and if the resolver is unable to resolve an IP address to a name (no PTR record, timeout, whatever problem else), it cannot show the resolved names.</p><p>Maybe I don't fully understand your problem, but it works as expected on my system.</p><p>However, it does not help to enable <strong>name resolution during capturing</strong>. If you want Wireshark to store the resolved names during the capture phase, wireshark needs to be extended to write those names (plus the raw IP addresses) to a pcapng file and tshark/wireshark needs to be extended as mentioned by Guy Harris.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '12, 09:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-14167" class="comments-container"><span id="14173"></span><div id="comment-14173" class="comment"><div id="post-14173-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the reply Kurt. Let me better explain what I mean by "only known addresses" are being resolved. The PCAP file I included in the bug report contains both public and private IP addresses. After executing the Tshark command, the prublic IP addresses are being resolved. For example: 74.125.137.94 resolves to <a href="http://www.google.ca">www.google.ca</a> (packet #5). However, the private IP addresses are not being resolved in the Tshark analysis. Referring to PCAP file in the bug report, please look at packet #6. In the Tshark analysis, the private IP address is not being resolved. Wireshark resolves these IPs</p></div><div id="comment-14173-info" class="comment-info"><span class="comment-age">(10 Sep '12, 11:49)</span> <span class="comment-user userinfo">Amato_C</span></div></div><span id="14181"></span><div id="comment-14181" class="comment"><div id="post-14181-score" class="comment-score"></div><div class="comment-text"><blockquote><p>In the Tshark analysis, the private IP address is not being resolved. Wireshark resolves these IPs</p></blockquote><p>O.K. if that's the case, I would think it's a bug. Are you sure that name resolving for those private addresses do work in your environment? Do you have PTR records for them in your local DNS server?</p></div><div id="comment-14181-info" class="comment-info"><span class="comment-age">(10 Sep '12, 18:55)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="14187"></span><div id="comment-14187" class="comment"><div id="post-14187-score" class="comment-score"></div><div class="comment-text"><p>I am certain that the names are being resolved in Wireshark and not in Tshark. Yes, the PTR records exist. I created bug 7712.</p></div><div id="comment-14187-info" class="comment-info"><span class="comment-age">(11 Sep '12, 06:36)</span> <span class="comment-user userinfo">Amato_C</span></div></div></div><div id="comment-tools-14167" class="comment-tools"></div><div class="clear"></div><div id="comment-14167-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

