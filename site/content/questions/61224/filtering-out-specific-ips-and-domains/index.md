+++
type = "question"
title = "filtering out specific IP&#x27;s and domains"
description = '''I want to make a system to analyze pcap files. So far I&#x27;m using Bro (for JSON output) and the Elastic-stack for visualizing the data. This works great, but there is a lot of traffic in the pcaps from ad-servers, that I want to filter out. I&#x27;ve been looking at modifying bro to do the job when &#x27;proces...'''
date = "2017-05-04T02:45:00Z"
lastmod = "2017-05-04T02:45:00Z"
weight = 61224
keywords = [ "ad-servers", "sanitize" ]
aliases = [ "/questions/61224" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [filtering out specific IP's and domains](/questions/61224/filtering-out-specific-ips-and-domains)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-61224-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to make a system to analyze pcap files. So far I'm using Bro (for JSON output) and the Elastic-stack for visualizing the data. This works great, but there is a lot of traffic in the pcaps from ad-servers, that I want to filter out. I've been looking at modifying bro to do the job when 'processing' pcap's. But I think it would be easier/better to remove the unwanted traffic before processing with bro, for example with tshark.</p><p>I found some lists of ad-server IP's and domains at the following urls:</p><pre><code>https://pgl.yoyo.org/as/serverlist.php?hostformat=nohtml
https://pgl.yoyo.org/adservers/iplist.php?ipformat=plain&amp;showintro=0&amp;mimetype=plaintext</code></pre><p>These list's are not complete, but they do cover many ad-servers that I want to exclude from the pcap's I want to analyze.</p><pre><code>1) What would be a good tshark filter to remove ad-server traffic (ip and domain) and creating a new &#39;clean&#39; pcap?
2) Is there a limitation to a tshark command/filter with let&#39;s say IP&#39;s and domains? Because the aforementioned lists are pretty long.
3) Can this solution of sanitizing pcap&#39;s also work on larger 30GB+ pcaps (after merging for example)</code></pre></div><div id="question-tags" class="tags-container tags">ad-servers sanitize</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 May '17, 02:45</strong></p><img src="https://secure.gravatar.com/avatar/1bd7aa9ec4636e9d234ddfb63bb15f85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="r00t070&#39;s gravatar image" /><p>r00t070<br />
<span class="score" title="6 reputation points">6</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="r00t070 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 May '17, 02:46</p></div></div><div id="comments-container-61224" class="comments-container"></div><div id="comment-tools-61224" class="comment-tools"></div><div class="clear"></div><div id="comment-61224-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

