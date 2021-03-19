+++
type = "question"
title = "Comparison of packet captures"
description = '''Ideally I want to be able to use something like the compare feature but with the ability to be more specific. A good example would be to take two responses to an identical request and get the differences in the responses highlighted with the ability to filter out differences I don&#x27;t care about.'''
date = "2011-07-28T11:59:00Z"
lastmod = "2012-07-15T06:51:00Z"
weight = 5352
keywords = [ "comparison", "different" ]
aliases = [ "/questions/5352" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Comparison of packet captures](/questions/5352/comparison-of-packet-captures)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5352-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Ideally I want to be able to use something like the compare feature but with the ability to be more specific.</p><p>A good example would be to take two responses to an identical request and get the differences in the responses highlighted with the ability to filter out differences I don't care about.</p></div><div id="question-tags" class="tags-container tags">comparison different</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jul '11, 11:59</strong></p><img src="https://secure.gravatar.com/avatar/861605a7cb8eca9cb6d38d376b78156f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Brandon&#39;s gravatar image" /><p>Brandon<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Brandon has no accepted answers">0%</span></p></div></div><div id="comments-container-5352" class="comments-container"><span id="5364"></span><div id="comment-5364" class="comment"><div id="post-5364-score" class="comment-score"></div><div class="comment-text"><p>So what exactly is your question? This is after all a question and answer site.</p></div><div id="comment-5364-info" class="comment-info"><span class="comment-age">(29 Jul '11, 17:55)</span> cmaynard ♦♦</div></div><span id="12725"></span><div id="comment-12725" class="comment"><div id="post-12725-score" class="comment-score"></div><div class="comment-text"><p>I would like to do a simmilar thing to work out the issues that we are experiencing accessing a web aplication through a VPN and IPS's network. Looking for a quick way of running a capture at source (from a monitor port on a local switch) and comparing to a capture from the host.</p><p>Looking to identify any mutation of the header, packet loss or truncation. At the same time filter packets from other sessions. The clients are not behind a particular gw, full s2s so I'm hoping the compare filtering wouldnt be too dissimilar to wireshark.</p><p>Will have a look and see what tools there are</p></div><div id="comment-12725-info" class="comment-info"><span class="comment-age">(15 Jul '12, 04:32)</span> xeode</div></div></div><div id="comment-tools-5352" class="comment-tools"></div><div class="clear"></div><div id="comment-5352-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12726"></span>

<div id="answer-container-12726" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12726-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I would like to do a simmilar thing to work out the issues that we are experiencing accessing a web aplication through a VPN and IPS's network</p></blockquote><p>I would use <a href="http://www.circlemud.org/jelson/software/tcpflow/">tcpflow</a> (part of major linux distros) for this. Feed it a capture file and it will output all tcp streams, each in a file, named like this:</p><blockquote><p><code>x.x.x.x.sport-y.y.y.y.dport</code><br />
</p></blockquote><p>These files will contain the payload data. In the case of a web request, it will be the requests and responses. Then just compare those files (diff) at the client side with those at the server side to find any differences.</p><p>If there is NAT in place, it might be a bit extra work to identify identical/related sessions. Start with the source port. If your lucky, the NAT device does not change that. Otherwise the order of the TCP "streams" is a good criteria as well (file creation time). If that does not work either (it should), you need a script that reads all files, and creates a hash over all request URLs in each file. Files with the same request hash "might" be related, if the stream index (only visible by the file creation time).</p><p>Together with the other criteria I mentioned, you should be able to automate the comparison process.</p><p>HINT: If you use HTTPS, things will get a bit tricky, as tcpflow is not able to decrypt traffic. Please report back, if you need a solution for that.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '12, 06:51</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-12726" class="comments-container"></div><div id="comment-tools-12726" class="comment-tools"></div><div class="clear"></div><div id="comment-12726-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

