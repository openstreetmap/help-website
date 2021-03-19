+++
type = "question"
title = "Parse incoming DNS but do not query DNS server"
description = '''Hello, I have a packet capture from my LAN that contains a DNS query (wireless) and response (192.168.0.7). When I copy it to another network and turn on name resolution it attempts to ask the DNS server for the host name of the IP (192.168.0.7) of the traffic... then gives up because the DNS server...'''
date = "2011-11-09T15:06:00Z"
lastmod = "2011-11-09T22:39:00Z"
weight = 7339
keywords = [ "query", "resolution", "name", "dns" ]
aliases = [ "/questions/7339" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Parse incoming DNS but do not query DNS server](/questions/7339/parse-incoming-dns-but-do-not-query-dns-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7339-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7339-score" class="post-score" title="current number of votes">0</div><span id="post-7339-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have a packet capture from my LAN that contains a DNS query (wireless) and response (192.168.0.7).</p><p>When I copy it to another network and turn on name resolution it attempts to ask the DNS server for the host name of the IP (192.168.0.7) of the traffic... then gives up because the DNS server doesn't have it, <em>but</em> then notices that there is a DNS packet in the file already and uses the results of that. The HTTP session is then showing a destination of "wireless".</p><p>Turning off host name resolution shows only connections to 192.168.0.7</p><p>How can I make Wireshark (or tshark) look at the DNS in the file and see if it resolves the IP addresses to hostnames but <strong>not</strong> have it issue queries to the DNS server of my machine which take a while to time out and slow the loading of files down?</p><p>Basically I want to do a filter on "ip.host == wireless" which the trace contains the DNS request and response to (and it works if I leave name resolution enabled even on a different network) but I want to cut out querying my DNS servers (which turning on name resolution does).</p><p>Thanks for your time, Matthew</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-resolution" rel="tag" title="see questions tagged &#39;resolution&#39;">resolution</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Nov '11, 15:06</strong></p><img src="https://secure.gravatar.com/avatar/d97559d5a31cc1f74bd63a10430f210b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="matthew1471&#39;s gravatar image" /><p><span>matthew1471</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="matthew1471 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Nov '11, 15:07</strong> </span></p></div></div><div id="comments-container-7339" class="comments-container"></div><div id="comment-tools-7339" class="comment-tools"></div><div class="clear"></div><div id="comment-7339-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="7345"></span>

<div id="answer-container-7345" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7345-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7345-score" class="post-score" title="current number of votes">0</div><span id="post-7345-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><a href="http://www.wireshark.org/docs/wsug_html_chunked/ChAppFilesConfigurationSection.html">Docs</a> shed some light upon it: there's configuration file 'hosts' at Wireshark folder where you can put all your names to. And the <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChAdvNameResolutionSection.html">wireshark name resolution</a> section states that while DNS responses are cached, I don't see any means to populate that cache from the capture file itself, that's weird.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '11, 16:40</strong></p><img src="https://secure.gravatar.com/avatar/35d96b8e73e6deb4e332d076fd3269b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ShomeaX&#39;s gravatar image" /><p><span>ShomeaX</span><br />
<span class="score" title="73 reputation points">73</span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ShomeaX has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Nov '11, 16:44</strong> </span></p></div></div><div id="comments-container-7345" class="comments-container"></div><div id="comment-tools-7345" class="comment-tools"></div><div class="clear"></div><div id="comment-7345-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7354"></span>

<div id="answer-container-7354" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7354-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7354-score" class="post-score" title="current number of votes">0</div><span id="post-7354-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Network name resolution is now either switched on or off. There are no controls over where it gets its information from (DNS server, Hosts, seen names).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Nov '11, 22:39</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-7354" class="comments-container"></div><div id="comment-tools-7354" class="comment-tools"></div><div class="clear"></div><div id="comment-7354-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

