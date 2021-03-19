+++
type = "question"
title = "monitoring vps"
description = '''hi I have a vps and I wanna to monitor it. I want to know witch IPs connect to it and how much traffic they use from it ( for any IP). thanks'''
date = "2014-04-23T03:32:00Z"
lastmod = "2014-04-26T11:52:00Z"
weight = 32094
keywords = [ "monitoring" ]
aliases = [ "/questions/32094" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [monitoring vps](/questions/32094/monitoring-vps)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32094-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32094-score" class="post-score" title="current number of votes">0</div><span id="post-32094-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi I have a vps and I wanna to monitor it. I want to know witch IPs connect to it and how much traffic they use from it ( for any IP).</p><p>thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-monitoring" rel="tag" title="see questions tagged &#39;monitoring&#39;">monitoring</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '14, 03:32</strong></p><img src="https://secure.gravatar.com/avatar/deec7afda5035771868d6acfbc90d994?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mosa&#39;s gravatar image" /><p><span>mosa</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mosa has no accepted answers">0%</span></p></div></div><div id="comments-container-32094" class="comments-container"><span id="32114"></span><div id="comment-32114" class="comment"><div id="post-32114-score" class="comment-score"></div><div class="comment-text"><p>can you please add <strong>your</strong> definition for <strong>vps</strong>, as there are several definitions for <strong>vps</strong>, like:</p><ul><li><a href="http://en.wikipedia.org/wiki/Virtual_private_server">VPS <strong>V</strong>irtual <strong>P</strong>rivate <strong>S</strong>erver</a></li><li><a href="http://www.vpspecialists.co.uk">VPS <strong>V</strong>acant <strong>P</strong>roperty <strong>S</strong>ecurity</a></li><li><a href="http://www.verkehrspilotenschule.com">VPS <strong>V</strong>erkehrs<strong>P</strong>ilotenschule <strong>B</strong>erlin</a></li><li><a href="http://www.vps-bahn.de">VPS <strong>V</strong>erkehrsbetriebe <strong>P</strong>eine-<strong>S</strong>alzgitter</a></li><li><a href="http://www.vps-zwickau.de">VPS <strong>V</strong>eranstaltungsservice und <strong>P</strong>arty<strong>S</strong>ervice Zwickau</a></li></ul><p>To be more specific: Please be more specific and add more details to your question by adding a comment to the question itself ;-))</p><p>So,</p><ul><li>what kind of VPS is it?</li><li>do you host it, or an ISP?</li><li>are you able to install software on it?</li><li>do you have a root shell?</li><li>etc.</li><li>etc.</li></ul></div><div id="comment-32114-info" class="comment-info"><span class="comment-age">(23 Apr '14, 11:48)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="32137"></span><div id="comment-32137" class="comment"><div id="post-32137-score" class="comment-score"></div><div class="comment-text"><p>Hi thanks for your attention vps means "Virtual Private Server" and I host it. I can able to install any software on it by root shell.</p><p>thanks</p></div><div id="comment-32137-info" class="comment-info"><span class="comment-age">(23 Apr '14, 22:23)</span> <span class="comment-user userinfo">mosa</span></div></div></div><div id="comment-tools-32094" class="comment-tools"></div><div class="clear"></div><div id="comment-32094-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="32138"></span>

<div id="answer-container-32138" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32138-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32138-score" class="post-score" title="current number of votes">1</div><span id="post-32138-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>vps means "Virtual Private Server" and I host it. I can able to install any software on it by root shell.</p></blockquote><p>for your requirement you should use <strong><a href="http://www.tcpdump.org/manpages/tcpdump.1.html">tcpdump</a></strong> on the VPS to capture traffic, as that's most certainly already installed if the VPS is a Lunix/Unix/*BSD system. Then copy the capture file to a different system to analyze it with Wireshark.</p><blockquote><p>tcpdump -ni eth0 -s0 -w /tmp/vps.pcap 'port xxxx'</p></blockquote><p>Please replace <strong>port xxxx</strong> with whatever <a href="http://wiki.wireshark.org/CaptureFilters">capture filter</a> you may need.</p><p>Then copy the file (with scp/ftp) to your Wireshark analysis system.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Apr '14, 01:18</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Apr '14, 01:18</strong> </span></p></div></div><div id="comments-container-32138" class="comments-container"><span id="32186"></span><div id="comment-32186" class="comment"><div id="post-32186-score" class="comment-score"></div><div class="comment-text"><p>thanks a lot but can you explain these parameters??? -ni ??? -s0 ???</p><p>note that I captured traffic from my vps by 'Tshark' but the performance for my VPS decreased because Tshark used cpu at high level. does Tcpdump use cpu like tshark ??? do you know tools that can capture traffic without use cpu like tshark??? do you know tools that capture traffic more than 2Gig/s ???</p><p>thanks</p></div><div id="comment-32186-info" class="comment-info"><span class="comment-age">(25 Apr '14, 22:38)</span> <span class="comment-user userinfo">mosa</span></div></div><span id="32194"></span><div id="comment-32194" class="comment"><div id="post-32194-score" class="comment-score"></div><div class="comment-text"><blockquote><p>o you know tools that capture traffic more than 2Gig/s ???</p></blockquote><p>2Gig/s for a VPS? I guess you should add much more details about your environment and what you are actually trying to do.</p><blockquote><p>I want to know witch IPs connect to it and how much traffic they use from it ( for any IP).</p></blockquote><p>This sounds more like you are trying to do some form of accounting. In that case both, tcpdump and tshark are the wrong tools for you and we need more information about what exactly you want to do accounting for.</p></div><div id="comment-32194-info" class="comment-info"><span class="comment-age">(26 Apr '14, 11:52)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-32138" class="comment-tools"></div><div class="clear"></div><div id="comment-32138-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="32188"></span>

<div id="answer-container-32188" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32188-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32188-score" class="post-score" title="current number of votes">0</div><span id="post-32188-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>A tool like <a href="http://www.ntop.org/products/ntop/">ntop</a> or <a href="http://unix4lyfe.org/darkstat/">darkstat</a> would be a better choice if you just want statistics (traffic, protocols, ports). The latter should be more resource friendly. Try and see what fits your needs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Apr '14, 06:52</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p><span>Roland</span><br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div></div><div id="comments-container-32188" class="comments-container"></div><div id="comment-tools-32188" class="comment-tools"></div><div class="clear"></div><div id="comment-32188-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

