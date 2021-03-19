+++
type = "question"
title = "Total length of packets"
description = '''I am capturing packets using libpcap. I am calculating the payload size as given here size_payload = ntohs(ip-&amp;gt;ip_len) - (size_ip + size_tcp); Now when I print ntohs(ip-&amp;gt;ip_len), I see that the value is 1280. For the same packets, wireshark shows a value of 1500 for the total length field in t...'''
date = "2012-09-28T01:59:00Z"
lastmod = "2012-09-28T01:59:00Z"
weight = 14587
keywords = [ "ethernet", "libpcap", "wireshark" ]
aliases = [ "/questions/14587" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Total length of packets](/questions/14587/total-length-of-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14587-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I am capturing packets using <code>libpcap</code>. I am calculating the payload size as given <a href="http://www.google.com/url?sa=t&amp;rct=j&amp;q=&amp;esrc=s&amp;source=web&amp;cd=1&amp;cad=rja&amp;ved=0CCIQFjAA&amp;url=http://www.tcpdump.org/sniffex.c&amp;ei=iGRlUP6WLIrW9QTXyIHQCw&amp;usg=AFQjCNG06vPZLcb_gnMas5sM1m7uu5K53A&amp;sig2=VKvPBo3Qicjw1cNg1Dn3QA">here</a><br />
<code>size_payload = ntohs(ip-&gt;ip_len) - (size_ip + size_tcp);</code><br />
Now when I print <code>ntohs(ip-&gt;ip_len)</code>, I see that the value is <code>1280</code>. For the same packets, wireshark shows a value of <code>1500</code> for the <code>total length</code> field in the IP header. Why do they differ?</p></div><div id="question-tags" class="tags-container tags">ethernet libpcap wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Sep '12, 01:59</strong></p><img src="https://secure.gravatar.com/avatar/f3f4fc6a0a5a04ac28b2415eddc34d54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rony358&#39;s gravatar image" /><p>rony358<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rony358 has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Sep '12, 01:59</p></div></div><div id="comments-container-14587" class="comments-container"></div><div id="comment-tools-14587" class="comment-tools"></div><div class="clear"></div><div id="comment-14587-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

