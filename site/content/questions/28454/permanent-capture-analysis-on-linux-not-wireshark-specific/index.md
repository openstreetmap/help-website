+++
type = "question"
title = "permanent capture &amp; analysis on linux  [not Wireshark-specific]"
description = '''This is not exactly a Wireshark question, but I wasn&#x27;t sure where to ask. If you have an idea for a community where to turn to, let me know. In the mean time... I&#x27;m setting up a server/gateway machine (a linux desktop) that is supposed to capture all traffic coming through it via LAN or VPN. And by ...'''
date = "2013-12-27T16:05:00Z"
lastmod = "2013-12-30T12:52:00Z"
weight = 28454
keywords = [ "traffic-analysis" ]
aliases = [ "/questions/28454" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [permanent capture & analysis on linux \[not Wireshark-specific\]](/questions/28454/permanent-capture-analysis-on-linux-not-wireshark-specific)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28454-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>This is not exactly a Wireshark question, but I wasn't sure where to ask. If you have an idea for a community where to turn to, let me know. In the mean time...</p><p>I'm setting up a server/gateway machine (a linux desktop) that is supposed to capture all traffic coming through it via LAN or VPN. And by that I mean write to disk every single bit of network traffic content. The purpose is security and debugging review and analysis.</p><p>However, I don't want to just create a gigantic dump file of packets. For it to be useful, it has to:</p><p>1) Filter out some white-listed content. So not write to disk stuff like YouTube videos or BitTorrent downloads. (Ergo: white-listing rules by protocol, IPs/domains, header/content keywords, DPI. Also, some rules could alert me in real-time when strange things happen.)</p><p>2) Let me analyze that traffic in a useful manner. That is, I'd like to be able to easily query for things like:</p><ul><li>all the files (html, js, png) that my Android Firefox loaded this morning when it crashed; (Assuming I know the time more or less, and the URL I tried to open.)</li><li>all the communications that an Android music app sent home this week, so that I can figure out how it knows my location;</li><li>the update my Ubuntu laptop downloaded yesterday, since from that moment it behaves weirdly.</li></ul><p>etc, etc.</p><p>How do I go about this? Are there open-source tools that do this?</p></div><div id="question-tags" class="tags-container tags">traffic-analysis</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Dec '13, 16:05</strong></p><img src="https://secure.gravatar.com/avatar/ed3651b409c59df349c465cc62cb9c1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ricky%20Moore&#39;s gravatar image" /><p>Ricky Moore<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ricky Moore has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 27 Dec '13, 16:07</p></div></div><div id="comments-container-28454" class="comments-container"></div><div id="comment-tools-28454" class="comment-tools"></div><div class="clear"></div><div id="comment-28454-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28481"></span>

<div id="answer-container-28481" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28481-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think there is any open source tool that is able to fulfill all your requirements. However, there are interesting projects, that might be inspiring to you.</p><blockquote><p><a href="http://www.xplico.org/">http://www.xplico.org/</a><br />
<a href="https://github.com/aol/moloch">https://github.com/aol/moloch</a> (<a href="http://blog.alejandronolla.com/2013/04/06/moloch-capturing-and-indexing-network-traffic-in-realtime/">Article about Moloch</a>)<br />
<a href="https://labs.ripe.net/Members/wnagele/large-scale-pcap-data-analysis-using-apache-hadoop">https://labs.ripe.net/Members/wnagele/large-scale-pcap-data-analysis-using-apache-hadoop</a><br />
</p></blockquote><p>So, it's up to you to grab one of those and 'tweak' it to meet your requirements.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Dec '13, 12:52</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-28481" class="comments-container"></div><div id="comment-tools-28481" class="comment-tools"></div><div class="clear"></div><div id="comment-28481-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

