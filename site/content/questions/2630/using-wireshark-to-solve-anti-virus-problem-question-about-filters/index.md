+++
type = "question"
title = "Using wireshark to solve anti virus problem, question about filters?"
description = '''Hi, I am having problems with my anti virus on one of my servers. the tech support of the company have asked me to take a capture using wireshark while the anti virus is trying to update. I am however finding a problem with this. For obvious reasons I do not want to send them a full scan of my netwo...'''
date = "2011-03-02T06:26:00Z"
lastmod = "2011-03-02T13:35:00Z"
weight = 2630
keywords = [ "virus", "anti", "filters", "wireshark" ]
aliases = [ "/questions/2630" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Using wireshark to solve anti virus problem, question about filters?](/questions/2630/using-wireshark-to-solve-anti-virus-problem-question-about-filters)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2630-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2630-score" class="post-score" title="current number of votes">0</div><span id="post-2630-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am having problems with my anti virus on one of my servers. the tech support of the company have asked me to take a capture using wireshark while the anti virus is trying to update. I am however finding a problem with this. For obvious reasons I do not want to send them a full scan of my network...so I was hoping that if I run wireshark off my windows 7 workstation and apply a filter to wireshark so it only gathers packets from the servers IP address, then on the server set the antivurs to update will this collect the information?</p><p>If I do this when im RDC'd into the server it only records packets between me and the server not the server and sophos. I am sure this is a problem with the filter I am applying in Wireshark which is "host XX.X.X.X".</p><p>I dont supose anyone is experienced with wireshark that would be able to shed any light on where I am going wrong.</p><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-virus" rel="tag" title="see questions tagged &#39;virus&#39;">virus</span> <span class="post-tag tag-link-anti" rel="tag" title="see questions tagged &#39;anti&#39;">anti</span> <span class="post-tag tag-link-filters" rel="tag" title="see questions tagged &#39;filters&#39;">filters</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Mar '11, 06:26</strong></p><img src="https://secure.gravatar.com/avatar/e8336e62452087521f427d029ed3e967?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ben%20Marks&#39;s gravatar image" /><p><span>Ben Marks</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ben Marks has no accepted answers">0%</span></p></div></div><div id="comments-container-2630" class="comments-container"></div><div id="comment-tools-2630" class="comment-tools"></div><div class="clear"></div><div id="comment-2630-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2641"></span>

<div id="answer-container-2641" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2641-score" class="post-score" title="current number of votes">2</div><span id="post-2641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I understand from your question that the anti-virus software is not downloading updates. For obvious reasons you don't want to send them a full trace of every juice packet going through your server.</p><p>The filter <strong>host x.x.x.x</strong> would be a capture fiter and limit recorded traffic to the specified ip address.</p><p>My personal approach to these situations is capture everything, then apply display filters until only the relevant packets are on the screen. In most cases when sending a trace file to tech support 30 frames or less easily do the job. The proper display filter would be <strong>ip.addr == x.x.x.x</strong> where x.x.x.x is the IP address for the update server.</p><p>As far as your update is concerned a few points to look out for:</p><ul><li>Is your server sending out DNS requests to obtain an IP address for the download server? The DNS request will <em>not</em> go to the anti-virus company.</li><li>Are your server and the remote system completing the TCP handshake?</li><li>If the download uses plaintext protocols: Do you see error messages? A good candidate can be "HTTP Proxy authentication required"</li><li>Do you have a firewall in your network that blocks "ICMP fragmentation needed" messages? (aka a "Blackhole router") This would allow your system to complete the handshake, but would interrupt the bulk data transfer.</li></ul><p>Hint: run <strong>ipconfig /flushdns</strong> on the command line before starting your test run. If you don't see a DNS request check your hosts file for bogus entries.</p><p>Good luck!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Mar '11, 13:35</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Mar '11, 13:39</strong> </span></p></div></div><div id="comments-container-2641" class="comments-container"></div><div id="comment-tools-2641" class="comment-tools"></div><div class="clear"></div><div id="comment-2641-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

