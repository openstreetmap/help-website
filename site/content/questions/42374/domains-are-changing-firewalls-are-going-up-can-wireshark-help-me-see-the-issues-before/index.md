+++
type = "question"
title = "domains are changing, firewalls are going up. can wireshark help me see the issues before?"
description = '''company A is splitting. there are 10 thousand plus servers. i need a valid way to see the communication between them that exists currently and the current ports they use. is that possible?'''
date = "2015-05-13T11:28:00Z"
lastmod = "2015-05-15T03:25:00Z"
weight = 42374
keywords = [ "network" ]
aliases = [ "/questions/42374" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [domains are changing, firewalls are going up. can wireshark help me see the issues before?](/questions/42374/domains-are-changing-firewalls-are-going-up-can-wireshark-help-me-see-the-issues-before)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42374-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42374-score" class="post-score" title="current number of votes">0</div><span id="post-42374-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>company A is splitting. there are 10 thousand plus servers. i need a valid way to see the communication between them that exists currently and the current ports they use. is that possible?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 May '15, 11:28</strong></p><img src="https://secure.gravatar.com/avatar/ac509fb54040bc70655c3cfd2ee96438?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="youngandpoor&#39;s gravatar image" /><p><span>youngandpoor</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="youngandpoor has no accepted answers">0%</span></p></div></div><div id="comments-container-42374" class="comments-container"></div><div id="comment-tools-42374" class="comment-tools"></div><div class="clear"></div><div id="comment-42374-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="42412"></span>

<div id="answer-container-42412" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42412-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42412-score" class="post-score" title="current number of votes">2</div><span id="post-42412-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p><strong>there are 10 thousand plus servers</strong>. i need a valid way to <strong>see the communication between them</strong></p></blockquote><p>Wow, nice little project.</p><p>Now, <strong>I'm going to tell you something you certainly don't want to hear</strong>. <strong>Really NO offense</strong>, just an attempt to "adjust" your expectations regarding the way you are going to handle this <strong>massive</strong> project ;-))</p><p>So, here we go ....</p><p>Based on your questions/comments about Packet capturing, Wireshark and Netflow, it looks like you don't have much experience with networking stuff, or at least not with the things mentioned. As I said: <strong>No offense</strong>, just a diagnosis! Please correct me if I'm wrong.</p><p>Now, you are trying to figure out the communication matrix of &gt; 10.000 servers. I <strong>strongly recommend</strong> to get a team of professionals on board, with decent experience in networking, firewalling and similar migration projects. If you try to do this yourself with Wireshark, you're going to get into real deep trouble!</p><p>Things to consider:</p><ul><li>Conversation matrix between clients and servers</li><li>Conversation matrix servers and servers</li><li>Conversation matrix servers and external systems</li><li>Conversation matrix servers and other internal systems (not servers - like printers, etc.)</li><li>How do clients/systems access other systems. Primarily via direct IP access (configured on the system) or via DNS?</li><li>Will you have to assign new IP addresses to some of the servers after the split</li></ul><p>It's by no means easy to figure out all that stuff for &gt; 10.000 server, plus a considerable amount of clients.</p><p><strong>What you can do,</strong> and what has been mentioned already:</p><ul><li>Capture traffic at certain points in your network, where all communication has to pass by, like core switches/routers</li><li>Capture the traffic in front of the servers</li><li>etc.</li></ul><p>These methods will require TAPs or a Switches with port mirroring, which are both challenges for themselves in a scenario like yours, let alone the massive amount of data you will get with that approach.</p><p>So, honestly: <strong>FORGET about the approach</strong> "Let's capture the whole traffic and generate a communication matrix based on that information". That's simply not going to work at a scale like this, unless you are willing to invest a <strong>huge</strong> amount of money and man power to install several hundred (or even several thousand) capture devices plus a system that is able to handle the huge amount of data.</p><p><strong>What else can you do?</strong></p><ul><li>enable Netflow, Sflow, Jflow, WhateverFlow your switches and router do support</li></ul><p>Depending on the Flow collection method (Sampling yes/no), you will get a better or worse idea about the communication matrix of your systems.</p><p>Caveats are:</p><ul><li>you will have routers/switches that don't support any form of Flow collection</li><li>you will have routers/switches that only support Flow sampling, which does not give you exact data, just a (more or less) rough distribution of the traffic</li><li>you will need a <strong>massive</strong> system that is able to handle the amount of flows per second coming in from the whole network. Such systems do exist but they cost a fortune.</li><li>you will still have to create the firewall rules based on that data set manually, because only few systems will do this for you autmatically, if they exist at all.</li></ul><p><strong>What else can you do?</strong></p><p>You could install a firewall in bridge mode, allow everything and log everything for a couple of weeks and then build a rough ruleset based on the logs. That's possible with scripting and I have done it that way, but not with an environment consisting of &gt; 10.000 servers and possibly even many more clients.</p><p><strong>Summary:</strong> So again, you should hire a team of professionals with a lot of experience to get this job done. It's <strong>impossible to do this with "a bit of sniffing" with Wireshark</strong>! ;-)</p><p>Hope this helps.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 May '15, 03:25</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 May '15, 04:56</strong> </span></p></div></div><div id="comments-container-42412" class="comments-container"></div><div id="comment-tools-42412" class="comment-tools"></div><div class="clear"></div><div id="comment-42412-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42375"></span>

<div id="answer-container-42375" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42375-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42375-score" class="post-score" title="current number of votes">0</div><span id="post-42375-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, it could if you have capture spots in each and every location (which you probably don't). I'd try to get NetFlow data from routers/switches instead, which is much more helpful, because it is just metadata for all the communication flows.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 May '15, 11:55</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-42375" class="comments-container"><span id="42376"></span><div id="comment-42376" class="comment"><div id="post-42376-score" class="comment-score"></div><div class="comment-text"><p>is netflow only available for cisco routers? will netflow produce port info? i want to see the traffic in the current state. what do you mean by capture spots? i may or may not know source and destination.</p><p>thank you!</p></div><div id="comment-42376-info" class="comment-info"><span class="comment-age">(13 May '15, 12:10)</span> <span class="comment-user userinfo">youngandpoor</span></div></div><span id="42394"></span><div id="comment-42394" class="comment"><div id="post-42394-score" class="comment-score"></div><div class="comment-text"><p>any ideas fellows?</p></div><div id="comment-42394-info" class="comment-info"><span class="comment-age">(14 May '15, 07:29)</span> <span class="comment-user userinfo">youngandpoor</span></div></div><span id="42395"></span><div id="comment-42395" class="comment"><div id="post-42395-score" class="comment-score"></div><div class="comment-text"><p>As Jasper said, to capture traffic between servers, you will need capture points, e.g. mirrored or span ports at each switch that passes traffic. Likely a big task.</p><p>Using <a href="http://en.wikipedia.org/wiki/NetFlow">Netflow</a>, or non-Cisco similar, the routers\switches send your flow collectors the metadata, e.g. source, dest ip and ports which you can then analyze. Much easier if your routers\switches can produce the flow data.</p></div><div id="comment-42395-info" class="comment-info"><span class="comment-age">(14 May '15, 07:45)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-42375" class="comment-tools"></div><div class="clear"></div><div id="comment-42375-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

