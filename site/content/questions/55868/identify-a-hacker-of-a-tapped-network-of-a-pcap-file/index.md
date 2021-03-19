+++
type = "question"
title = "Identify a hacker of a tapped network of a pcap file?"
description = '''Hey guys, I want to know how to identify a hacker from a tapped network traffic. I want to determine the identity of a hacker from a pcap file. How can I do that? I got the file here, if someone help me how to do it with instructions, I will be happy'''
date = "2016-09-26T11:11:00Z"
lastmod = "2016-09-26T11:33:00Z"
weight = 55868
keywords = [ "tapped", "homework", "hackers" ]
aliases = [ "/questions/55868" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Identify a hacker of a tapped network of a pcap file?](/questions/55868/identify-a-hacker-of-a-tapped-network-of-a-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55868-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey guys,</p><p>I want to know how to identify a hacker from a tapped network traffic. I want to determine the identity of a hacker from a pcap file. How can I do that? I got the file here, if someone help me how to do it with instructions, I will be happy</p></div><div id="question-tags" class="tags-container tags">tapped homework hackers</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '16, 11:11</strong></p><img src="https://secure.gravatar.com/avatar/83aa16a967e8a733521d50d9f3d569eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Farsa42&#39;s gravatar image" /><p>Farsa42<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Farsa42 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Oct '16, 04:40</p><img src="https://secure.gravatar.com/avatar/3b24b339fc62fb46dced6a443d3202ea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Christian_R&#39;s gravatar image" /><p>Christian_R<br />
<span class="score" title="1830 reputation points"><span>1.8k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span></p></div></div><div id="comments-container-55868" class="comments-container"></div><div id="comment-tools-55868" class="comment-tools"></div><div class="clear"></div><div id="comment-55868-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="55870"></span>

<div id="answer-container-55870" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-55870-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Identification of a hacker is rarely possible. All you may get is an IP address that is contacted for command &amp; control traffic, but those are usually compromised systems themselves. So don't get your hopes up.</p><p>So what you need to do is to identify the malicious traffic. For that you need to know what the "normal" traffic of the network looks like, and find what doesn't fit the pattern. You can do that by looking at the protocols involved (e.g. via the Statistics menu, using the Protocol Distribution stats), or IPs contacted that seem odd. It will take a while if you're not trained in spotting malicious activity, but often filtering for http requests can be a good starting point. This can by done by filtering on "http.request.method" and looking at the host and URL called in the packets you get.</p><p>Another point is filtering on "dns" and check if there's any host names that are odd - again, this is something that will take a lot of work checking things out to see if they're legit or not.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '16, 11:33</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-55870" class="comments-container"><span id="55872"></span><div id="comment-55872" class="comment"><div id="post-55872-score" class="comment-score"></div><div class="comment-text"><p>There's nothing at that Protocol Hierarchy Statistics? Am I doing it wrong? I only see TCP/HTTP, but nothing else. Percent packets are 100.0.</p></div><div id="comment-55872-info" class="comment-info"><span class="comment-age">(26 Sep '16, 12:59)</span> Farsa42</div></div><span id="55873"></span><div id="comment-55873" class="comment"><div id="post-55873-score" class="comment-score"></div><div class="comment-text"><p>So the question still is as @Jasper has asked you, too: What do you exactly mean with identify the attacker? Do you want his full name, IP address, home address, telephone number or birthday?</p></div><div id="comment-55873-info" class="comment-info"><span class="comment-age">(26 Sep '16, 13:09)</span> Christian_R</div></div><span id="55874"></span><div id="comment-55874" class="comment"><div id="post-55874-score" class="comment-score"></div><div class="comment-text"><p>A teacher gave me a pcap file to find out ID of a 'hacker' and telling what his/her ID is. I don't know what it meant to be, but only identify a 'hacker' from this pcap file that is been tapped.</p></div><div id="comment-55874-info" class="comment-info"><span class="comment-age">(26 Sep '16, 13:22)</span> Farsa42</div></div><span id="55877"></span><div id="comment-55877" class="comment"><div id="post-55877-score" class="comment-score"></div><div class="comment-text"><p>without any prior training as what to look for? That's not a good assignment...</p></div><div id="comment-55877-info" class="comment-info"><span class="comment-age">(26 Sep '16, 13:50)</span> Jasper ♦♦</div></div><span id="55881"></span><div id="comment-55881" class="comment"><div id="post-55881-score" class="comment-score"></div><div class="comment-text"><p>No no, it's a bonus, but I want it do it, because I like it. But there was no explanation</p></div><div id="comment-55881-info" class="comment-info"><span class="comment-age">(26 Sep '16, 14:17)</span> Farsa42</div></div><span id="55885"></span><div id="comment-55885" class="comment not_top_scorer"><div id="post-55885-score" class="comment-score"></div><div class="comment-text"><p>Well, then you can only look through the packets and statistics to find something that looks odd...</p></div><div id="comment-55885-info" class="comment-info"><span class="comment-age">(26 Sep '16, 16:21)</span> Jasper ♦♦</div></div></div><div id="comment-tools-55870" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-55870-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

