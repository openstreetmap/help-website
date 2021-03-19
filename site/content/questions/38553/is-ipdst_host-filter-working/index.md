+++
type = "question"
title = "Is ip.dst_host filter working?"
description = '''I&#x27;m trying to apply filter ip.dst_host. The Wshark Wiki says it should work, and Wshark accepts it. However when I apply it I get no results whatsoever. Is the filter broken, or am I using it wrong?'''
date = "2014-12-14T06:31:00Z"
lastmod = "2014-12-14T06:55:00Z"
weight = 38553
keywords = [ "capture-filters", "filters", "display-filter" ]
aliases = [ "/questions/38553" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is ip.dst\_host filter working?](/questions/38553/is-ipdst_host-filter-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38553-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to apply filter ip.dst_host. The Wshark Wiki says it should work, and Wshark accepts it. However when I apply it I get no results whatsoever. Is the filter broken, or am I using it wrong?</p></div><div id="question-tags" class="tags-container tags">capture-filters filters display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Dec '14, 06:31</strong></p><img src="https://secure.gravatar.com/avatar/7f37b0855db956ae09e58a7e90481f34?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Peregrino69&#39;s gravatar image" /><p>Peregrino69<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Peregrino69 has no accepted answers">0%</span></p></div></div><div id="comments-container-38553" class="comments-container"></div><div id="comment-tools-38553" class="comment-tools"></div><div class="clear"></div><div id="comment-38553-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38555"></span>

<div id="answer-container-38555" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38555-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Works for me. However, once you resolved an ip address to a hostname you need to filter on the hostname. The filter will not match if you use the ip address.</p><p>Here's an example where a hostname resolves to 3 different ip addresses, not uncommon in the internet. So using <code>ip.host == gmail-imap.l.google.com</code> will filter traffic to/from all three ip addresses. Another use case is filtering on any 'amazon' or "imap" addresses using the "contains" operator. Works if you can resolve the ip addresses - ideally by having the DNS answers in the tracefile.</p><p>Regards Matthias <img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-178.png" alt="alt text" /> <img src="https://osqa-ask.wireshark.org/upfiles/Screenshot-179.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Dec '14, 06:55</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 14 Dec '14, 22:17</p></div></div><div id="comments-container-38555" class="comments-container"><span id="38558"></span><div id="comment-38558" class="comment"><div id="post-38558-score" class="comment-score"></div><div class="comment-text"><p>Sorry but I'm not following you now. When using ip.dst_host you use the dns name, not IP address. And that's not working for me - or I'm expecting a different result.</p><p>I tested now with Ubuntu 14.04 and Debian Wheezy 7.7, with wsark 1.12.2. When I apply filter ip.dst_host hostname.com, no packets are displayed. If I apply filter http and check the packets, I can find the hostname in the payload of the first http packet.</p></div><div id="comment-38558-info" class="comment-info"><span class="comment-age">(14 Dec '14, 09:21)</span> Peregrino69</div></div><span id="38560"></span><div id="comment-38560" class="comment"><div id="post-38560-score" class="comment-score"></div><div class="comment-text"><p>ip.dest_hostname filters on a host name or an ipadress, whatever is available. So if you traced the DNS traffic and allow wireshark to resolve the ip addresses, it will use the resolved hostnames for those addresses that could be resolved, an IP addresses for those that couldn't be resolved. You could also manually resolve the ip addresses to host names which then would enable you to apply this filtr. If I understaand your comment correctly, you're expecting that wireshark filters on the hostnames in the http payload?</p></div><div id="comment-38560-info" class="comment-info"><span class="comment-age">(14 Dec '14, 13:19)</span> mrEEde</div></div><span id="38562"></span><div id="comment-38562" class="comment"><div id="post-38562-score" class="comment-score"></div><div class="comment-text"><p>I assumed ip.dest_host could be used for example to monitor traffic to a given DNS host. I was specifically testing with http and icmp traffic (ping hostname). There's a DNS request which resolves the host successfully, but even that doesn't come up with this filter. I'm fine with that - but now I'm interested in a practical situation when / how I could use this filter :) Maybe you can give me an example?</p></div><div id="comment-38562-info" class="comment-info"><span class="comment-age">(14 Dec '14, 15:29)</span> Peregrino69</div></div></div><div id="comment-tools-38555" class="comment-tools"></div><div class="clear"></div><div id="comment-38555-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

