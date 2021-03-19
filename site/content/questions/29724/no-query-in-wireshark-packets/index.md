+++
type = "question"
title = "No Query in wireshark packets"
description = '''Hi Team, I am not able to find the query packets in my wireshark trace, I always get the first packet as response not matter what i do. I flushed the dns, clear the browser cache tried from browser as well as from the cli nslookup option, Still doesnot work. Thanks  Irfan '''
date = "2014-02-11T19:55:00Z"
lastmod = "2014-02-12T00:45:00Z"
weight = 29724
keywords = [ "dns", "dnsquery" ]
aliases = [ "/questions/29724" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [No Query in wireshark packets](/questions/29724/no-query-in-wireshark-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29724-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Team,</p><p>I am not able to find the query packets in my wireshark trace, I always get the first packet as response not matter what i do. I flushed the dns, clear the browser cache tried from browser as well as from the cli nslookup option, Still doesnot work.</p><p>Thanks Irfan</p></div><div id="question-tags" class="tags-container tags">dns dnsquery</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '14, 19:55</strong></p><img src="https://secure.gravatar.com/avatar/959e162efb513fc227dc3b3fd7a18770?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arshmohd&#39;s gravatar image" /><p>arshmohd<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arshmohd has no accepted answers">0%</span></p></div></div><div id="comments-container-29724" class="comments-container"><span id="29735"></span><div id="comment-29735" class="comment"><div id="post-29735-score" class="comment-score"></div><div class="comment-text"><p>Where are you capturing? I guess you're connected via wireless and capturing on your own system?</p></div><div id="comment-29735-info" class="comment-info"><span class="comment-age">(12 Feb '14, 00:41)</span> Jasper ♦♦</div></div><span id="29818"></span><div id="comment-29818" class="comment"><div id="post-29818-score" class="comment-score"></div><div class="comment-text"><p>Yes i am connected from Wireless...</p></div><div id="comment-29818-info" class="comment-info"><span class="comment-age">(12 Feb '14, 23:30)</span> arshmohd</div></div></div><div id="comment-tools-29724" class="comment-tools"></div><div class="clear"></div><div id="comment-29724-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29736"></span>

<div id="answer-container-29736" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29736-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds like you don't see outgoing packets, especially DNS requests. If so, please see the other questions (and answers) tagged with outgoing.</p><blockquote><p><a href="http://ask.wireshark.org/tags/outgoing/">http://ask.wireshark.org/tags/outgoing/</a></p></blockquote><p>In most of the cases there is an interfering software installed on the client, that prevents Wireshark from capturing outbound/outgoing frames, like: AV, Firewall, IDS, VPN client, Endpoint Security. If that is that case on your system, please disable and/or uninstall that software.</p><p>See also here:</p><blockquote><p><a href="http://ask.wireshark.org/questions/28909/no-outgoing-packets">http://ask.wireshark.org/questions/28909/no-outgoing-packets</a></p></blockquote><p>where Symantec Endpoint Security has been the problem (again).</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '14, 00:45</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Feb '14, 01:40</p></div></div><div id="comments-container-29736" class="comments-container"><span id="29817"></span><div id="comment-29817" class="comment"><div id="post-29817-score" class="comment-score"></div><div class="comment-text"><p>I have symantec Endpoint but i will try this again today on my homepc if that helps.. Could it be possible that specific websites dont let the query packets to be captured,.... we have anycast DNS infra.. If that could be an issue..... ?</p><p>Regards Irfna</p></div><div id="comment-29817-info" class="comment-info"><span class="comment-age">(12 Feb '14, 23:30)</span> arshmohd</div></div><span id="29819"></span><div id="comment-29819" class="comment"><div id="post-29819-score" class="comment-score"></div><div class="comment-text"><p>Websites have no influence on your local DNS query. Symantec Endpoint has been reported as a problem in similar cases, several times.</p></div><div id="comment-29819-info" class="comment-info"><span class="comment-age">(13 Feb '14, 00:07)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-29736" class="comment-tools"></div><div class="clear"></div><div id="comment-29736-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

