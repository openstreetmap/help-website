+++
type = "question"
title = "Help requested: Basic capture and statistics"
description = '''Greetings! I&#x27;m trying to answer a simple question: what&#x27;s eating up my bandwidth on one machine? I would like to see a list of URLs or IP addrs and throughput for each one in a 24-hour period. I&#x27;ve been told that WireShark can do this, but I don&#x27;t have the expertise to set this up properly (I&#x27;m an o...'''
date = "2015-02-13T09:37:00Z"
lastmod = "2015-02-24T22:52:00Z"
weight = 39856
keywords = [ "capture", "statistics" ]
aliases = [ "/questions/39856" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Help requested: Basic capture and statistics](/questions/39856/help-requested-basic-capture-and-statistics)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39856-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39856-score" class="post-score" title="current number of votes">0</div><span id="post-39856-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Greetings!</p><p>I'm trying to answer a simple question: what's eating up my bandwidth on one machine? I would like to see a list of URLs or IP addrs and throughput for each one in a 24-hour period. I've been told that WireShark can do this, but I don't have the expertise to set this up properly (I'm an old techie but don't know much about comms).</p><p>Could I trouble someone to guide me on the settings required to do this, please? For example, I set "limit each packet" to 100 bytes, since I'll be capturing for 24 hrs, but I have no idea if this is enough -- or more than needed.</p><p>Thank you very much for any help, info, guidance, etc.!</p><p>Ariel</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '15, 09:37</strong></p><img src="https://secure.gravatar.com/avatar/2241f06e691be1d99183fe194096cffc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arielsfr&#39;s gravatar image" /><p><span>arielsfr</span><br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arielsfr has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Feb '15, 09:47</strong> </span></p></div></div><div id="comments-container-39856" class="comments-container"></div><div id="comment-tools-39856" class="comment-tools"></div><div class="clear"></div><div id="comment-39856-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39862"></span>

<div id="answer-container-39862" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39862-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39862-score" class="post-score" title="current number of votes">1</div><span id="post-39862-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="arielsfr has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There are probably a few tutorials out there, so this should get you on the right track if you need to search for more info. I also assume you can find your way around a manual page and a command line.</p><p>We'll start at <a href="https://en.wikipedia.org/wiki/OSI_model">layer 1</a>; I've got no idea about your network setup, but <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">here</a> you should be able to find info on how to define your capture point.</p><p>Now that we know where to capture we'll setup a capture session. Wireshark is perfectly capable of managing a capture, but doesn't do it itself. It spawns <a href="https://www.wireshark.org/docs/man-pages/dumpcap.html">dumpcap</a> to do the heavy lifting. All that Wireshark does is read the packets and analyses them. Now there's one thing to know about that, and that's that Wireshark keeps metadata on the <em>all</em> packets in memory. Now you understand why it can <a href="http://wiki.wireshark.org/KnownBugs/OutOfMemory">blow out of the water the beefiest machine</a>: just capture more packets.</p><p>You already figured out that you can limit the amount of data by limiting the capture size. That's a good thing, but tricky, because you have to figure out how much to keep (trial and err come to mind). Also we don't want Wireshark to blow up in a long term capture/dissection session. Therefore we can launch the capture engine directly, keeping 'the shark at bay' for now.</p><p>Referring to the <a href="https://www.wireshark.org/docs/man-pages/dumpcap.html">manual page</a> you can work out the parameters to use to get 24h worth of capture data in reasonably sized capture files (plural), with reasonable amount of packets. There are other command line tools available to manipulate the capture files should there be any resizing done afterwards.</p><p>Now, assuming that you have reasonable sized capture files, you can load them in Wireshark and use the menu options found in the Analyse menu to get views of the data captured, eg. type of network traffic, IP addresses and HTTP analysis. When confronted with HTTPS, you can look at the DNS traffic to see what resolving is going on, presumably for HTTP.</p><p>So, these are some tips to do this using Wireshark. But is this the right tool for the job? Have you looked into something like <a href="http://www.ntop.org/products/ntop/">ntop-ng</a> for instance? It's using the same capture infrastructure down at layer 1 and 2, but does the analysis a whole lot better.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '15, 03:04</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-39862" class="comments-container"><span id="40036"></span><div id="comment-40036" class="comment"><div id="post-40036-score" class="comment-score"></div><div class="comment-text"><p>Hello, Jaap,</p><p>Thank you very much for taking the time and trouble to explain this! It has helped a lot; it gave me a starting point from which to learn more.</p><p>Originally, I had tried nettop and iftop -- both excellent programs, but they only handle real-time transactions. That's when I asked a fellow OSX-user for help, and he suggested WireShark, which is what brought me here.</p><p>ntop-ng looks like it's exactly what I need, but unfortunately, I can't get it to work on my system. After doing some homework, I tried many different things, both *nix and Mac-specific, but haven't found anything satisfactory yet. As it stands now, I want to experiment with tcpdump for the capture, and see if I can find some statistics package to look at the results -- or, if absolutely necessary, write a few perl scripts (my time is very limited). I don't think I can get the stats I need with WireShark, but when the time comes, I can study the manual and find out for myself, now that it's no longer incomprehensible!</p><p>Again, thank you very much for your help! All the best-- Ariel</p></div><div id="comment-40036-info" class="comment-info"><span class="comment-age">(23 Feb '15, 13:28)</span> <span class="comment-user userinfo">arielsfr</span></div></div><span id="40061"></span><div id="comment-40061" class="comment"><div id="post-40061-score" class="comment-score"></div><div class="comment-text"><p>Good luck. If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-40061-info" class="comment-info"><span class="comment-age">(24 Feb '15, 22:52)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-39862" class="comment-tools"></div><div class="clear"></div><div id="comment-39862-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

