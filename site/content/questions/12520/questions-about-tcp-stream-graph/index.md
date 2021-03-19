+++
type = "question"
title = "Questions about &quot;TCP Stream Graph&quot;"
description = '''Hi all!! Please, see attached graphs.  1. How to zoom on the graphs? I haven&#x27;t got middle mouse button, then I used the &#x27;+&#x27; and &#x27;-&#x27; keys to zoom in and out, but I get nothing.  2. How to change the values of X and Y axes on the graphs to values more appropriate for me? Please, see Time/Sequence Grap...'''
date = "2012-07-09T02:08:00Z"
lastmod = "2012-07-20T02:10:00Z"
weight = 12520
keywords = [ "graph" ]
aliases = [ "/questions/12520" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Questions about "TCP Stream Graph"](/questions/12520/questions-about-tcp-stream-graph)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12520-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12520-score" class="post-score" title="current number of votes">0</div><span id="post-12520-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all!!</p><p>Please, see attached graphs. 1. How to zoom on the graphs? I haven't got middle mouse button, then I used the '+' and '-' keys to zoom in and out, but I get nothing. 2. How to change the values of X and Y axes on the graphs to values more appropriate for me? Please, see Time/Sequence Graph. 3. Why do I get horizontal lines on the RTT graph? Please, see Round Trip Time Graph.</p><p>Thanks!!</p><p>Regards,</p><p>Rocío.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/RTT.png" alt="alt text" /></p><p><img src="https://osqa-ask.wireshark.org/upfiles/Sequence.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-graph" rel="tag" title="see questions tagged &#39;graph&#39;">graph</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '12, 02:08</strong></p><img src="https://secure.gravatar.com/avatar/8d28a5820c4e6d8f2e49289dcd08d719?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rocio&#39;s gravatar image" /><p><span>Rocio</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rocio has no accepted answers">0%</span></p></img></div></div><div id="comments-container-12520" class="comments-container"></div><div id="comment-tools-12520" class="comment-tools"></div><div class="clear"></div><div id="comment-12520-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12784"></span>

<div id="answer-container-12784" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12784-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12784-score" class="post-score" title="current number of votes">1</div><span id="post-12784-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p><code>1. How to zoom on the graphs? I haven't got middle mouse button, then I used the '+' and '-' keys to zoom in and out, but I get nothing.</code><br />
</p></blockquote><p>'+' and '-' do work with Wireshark 1.8.0 (Win7 64 Bit). You can also try 'i' (zoom in) and 'o' (zoom out). Then scroll with cursor: left/right/up/down. (Click Help button of the TCP graph control window).</p><p>What is your Wireshark version?</p><p>HOWEVER, the mouse commands <strong>do not work</strong> with Wireshark 1.8.0 (Win7 64 Bit) on my system!?!</p><blockquote><p><code>2. How to change the values of X and Y axes on the graphs to values more appropriate for me?</code><br />
</p></blockquote><p>You can't without changing the code.</p><blockquote><p><code>3. Why do I get horizontal lines on the RTT graph? Please, see Round Trip Time Graph.</code><br />
</p></blockquote><p>that's interesting. The RTT graph is calculated based on the timestamps in the capture file. The only 'plausible' explanation I can imagine (at the moment) is a problem with the way the timestamps are created. If the OS on which you captured the data is 'busy' that might create timestamp pattern. However I would expect a more diffuse pattern and not 8 straight lines. But then: If you <strong>could zoom in</strong>, you might discover, that the lines are not THAT straight.</p><p>Just a wild guess: Did you capture within a virtual machine? If no: any other special 'configuration' on that machine?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jul '12, 13:29</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></img></div></div><div id="comments-container-12784" class="comments-container"><span id="12878"></span><div id="comment-12878" class="comment"><div id="post-12878-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much for your response Kurt!</p><p>My Wireshark version is 1.2.7. It is a very old version and I guess that in it I cannot zoom in/out. I will install a newer version. I am working with a pcap file, but I use Wireshark only for getting graphs and statistics, I don't capture traffics with Wireshark.</p><p>Thanks!</p><p>Regards, Rocío.</p></div><div id="comment-12878-info" class="comment-info"><span class="comment-age">(20 Jul '12, 02:10)</span> <span class="comment-user userinfo">Rocio</span></div></div></div><div id="comment-tools-12784" class="comment-tools"></div><div class="clear"></div><div id="comment-12784-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

