+++
type = "question"
title = "BAD TCP Question"
description = '''Hello, Looking at multiple capture files and is there a rule of thumb or best practice that says If X percentage of packets in a TCP stream are deemed bad those should be investigated before trying to resolve the main issue? For example If I&#x27;m reading this correctly I created a BAD TCP button and wh...'''
date = "2017-02-14T12:16:00Z"
lastmod = "2017-02-15T14:13:00Z"
weight = 59420
keywords = [ "bad", "question", "tcp" ]
aliases = [ "/questions/59420" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [BAD TCP Question](/questions/59420/bad-tcp-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59420-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>Looking at multiple capture files and is there a rule of thumb or best practice that says If X percentage of packets in a TCP stream are deemed bad those should be investigated before trying to resolve the main issue? For example If I'm reading this correctly I created a BAD TCP button and when I clicked on it for this entire capture it says 70,637 packets, displayed 4,785 or 6.8% so I assume this means 6.8% of all the packets are considered bad. Is this a problem I should address before moving on?</p><p>Thanks,</p></div><div id="question-tags" class="tags-container tags">bad question tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Feb '17, 12:16</strong></p><img src="https://secure.gravatar.com/avatar/a6414c2ff8204ee9c4a3bc2a646c4644?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rock90&#39;s gravatar image" /><p>rock90<br />
<span class="score" title="21 reputation points">21</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rock90 has no accepted answers">0%</span></p></div></div><div id="comments-container-59420" class="comments-container"></div><div id="comment-tools-59420" class="comment-tools"></div><div class="clear"></div><div id="comment-59420-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="59443"></span>

<div id="answer-container-59443" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59443-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hello Rock90,</p><p>It also is important to understand exactly what BAD TCP is filtering for. If you created the button to display tcp.analysis.flags - that will show you TCP events like retransmissions, duplicate acks, and window updates - among other things.</p><p>Some of these are not inherently bad on their own, and may not be directly related to the problem you are troubleshooting. For example, I have a trace I use in training that has several TCP Window Updates that are caught by that filter, but are not the root cause of the delay in the trace.</p><p>So some context is important. You could have the filter capture full of TCP events, but have nothing to do with what you are trying to analyze. So it is hard to put a rule of thumb that works for all situations, networks, and applications.</p><p>For me, if I capture performance issue between a client and server, filter on that conversation, and then apply the analysis filter, that is when I pay close attention to the errors reported by the tcp.analysis.flags filter. If I see a bunch of retransmissions accompanied by delays, then I will start digging to find the cause of the packet loss.</p><p>I hope this is helpful toward answering your question. It is just hard to put a fixed number on such a dynamic thing.</p><p>-Chris</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '17, 14:13</strong></p><img src="https://secure.gravatar.com/avatar/e4b59638a8d10a76524620f016f04e5f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cgreer&#39;s gravatar image" /><p>cgreer<br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cgreer has one accepted answer">100%</span></p></div></div><div id="comments-container-59443" class="comments-container"><span id="59469"></span><div id="comment-59469" class="comment"><div id="post-59469-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the response Chris. I am new to WS and have been watching your videos online. Thanks for all the great videos.</p></div><div id="comment-59469-info" class="comment-info"><span class="comment-age">(16 Feb '17, 06:42)</span> rock90</div></div></div><div id="comment-tools-59443" class="comment-tools"></div><div class="clear"></div><div id="comment-59443-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="59439"></span>

<div id="answer-container-59439" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59439-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>This depends on your capture setup. The excellent network capture playbook on <a href="https://blog.packet-foo.com">blog.packet-foo.com</a> describes the most likely scenario in <a href="https://blog.packet-foo.com/2016/11/the-network-capture-playbook-part-3-network-cards/">part 3</a>.</p><p>If you observe the packets in transit, going from system A to system B and recorded by system C, then you are in trouble.</p><p>It would help, if you can upload a trace file and give a few hints on the scenario.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Feb '17, 11:34</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-59439" class="comments-container"></div><div id="comment-tools-59439" class="comment-tools"></div><div class="clear"></div><div id="comment-59439-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

