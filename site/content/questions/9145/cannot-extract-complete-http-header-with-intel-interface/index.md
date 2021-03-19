+++
type = "question"
title = "Cannot extract complete Http Header with Intel Interface"
description = '''I am using jNetPcap library to extract packet information from an offline Pcap file.When I capture packets on Wi-fi network with Microsoft Interface I am able to extract the Http header with all fields. However with Intel Interface(i.e when I am on Proxy Connection), I am unable to get the complete ...'''
date = "2012-02-20T12:03:00Z"
lastmod = "2012-02-20T12:03:00Z"
weight = 9145
keywords = [ "interface", "jnetpcap", "http" ]
aliases = [ "/questions/9145" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot extract complete Http Header with Intel Interface](/questions/9145/cannot-extract-complete-http-header-with-intel-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9145-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using jNetPcap library to extract packet information from an offline Pcap file.When I capture packets on Wi-fi network with Microsoft Interface I am able to extract the Http header with all fields. However with Intel Interface(i.e when I am on Proxy Connection), I am unable to get the complete http header, certain fields such as RequestURl,Request Version,RequestMethod are missing, Although they are visible in my Pcap file. Kindly let me know why this happens.</p><p>And the output is :</p><pre><code>Http:  ******* Http offset=54 (0x36) length=463 protocol suite=TCP/IP

Http: 
Http:             HOST = google.com
Http: PROXY-CONNECTION = keep-alive
Http:       USER-AGENT = Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7
Http:           ACCEPT = text/html,application/xhtml+xml,applic(etc..)
Http:          REFERER = http://googleads.g.doubleclick.net/pagead/drt/s
Http:  ACCEPT-ENCODING = gzip,deflate,sdch
Http:  ACCEPT-LANGUAGE = en-US,en;q=0.8
Http:   ACCEPT-CHARSET = ISO-8859-1,utf-8;q=0.7,*;q=0.3</code></pre></div><div id="question-tags" class="tags-container tags">interface jnetpcap http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Feb '12, 12:03</strong></p><img src="https://secure.gravatar.com/avatar/84da5ede7d868490afe7e099e42aeed2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rhiya&#39;s gravatar image" /><p>Rhiya<br />
<span class="score" title="0 reputation points">0</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rhiya has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Feb '12, 12:14</p></div></div><div id="comments-container-9145" class="comments-container"><span id="9147"></span><div id="comment-9147" class="comment"><div id="post-9147-score" class="comment-score"></div><div class="comment-text"><p>And exactly how does this relate to Wireshark?</p></div><div id="comment-9147-info" class="comment-info"><span class="comment-age">(20 Feb '12, 13:12)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-9145" class="comment-tools"></div><div class="clear"></div><div id="comment-9145-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

