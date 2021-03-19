+++
type = "question"
title = "How to get traffic graphs"
description = '''Hi Guys, Am looking for a way to simply monitor over a 2-3 weeks period, the incoming traffic, and I need it shown on a graph, so possible to see date/time of consumption. Which function do I need to use? Paul'''
date = "2015-09-29T07:26:00Z"
lastmod = "2015-09-30T04:30:00Z"
weight = 46255
keywords = [ "graphs", "traffic" ]
aliases = [ "/questions/46255" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get traffic graphs](/questions/46255/how-to-get-traffic-graphs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46255-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46255-score" class="post-score" title="current number of votes">0</div><span id="post-46255-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Guys, Am looking for a way to simply monitor over a 2-3 weeks period, the incoming traffic, and I need it shown on a graph, so possible to see date/time of consumption. Which function do I need to use? Paul</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-graphs" rel="tag" title="see questions tagged &#39;graphs&#39;">graphs</span> <span class="post-tag tag-link-traffic" rel="tag" title="see questions tagged &#39;traffic&#39;">traffic</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Sep '15, 07:26</strong></p><img src="https://secure.gravatar.com/avatar/27d7d8591b6f0b373eaa48a83b52a3f4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PAULWALKER&#39;s gravatar image" /><p><span>PAULWALKER</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PAULWALKER has no accepted answers">0%</span></p></div></div><div id="comments-container-46255" class="comments-container"><span id="46262"></span><div id="comment-46262" class="comment"><div id="post-46262-score" class="comment-score"></div><div class="comment-text"><p>Incoming traffic of what, a single PC, a small home network, or a larger business network?</p><p>Wireshark may not be the best tool for this, it's a Packet Analyzer that can produce some stats about traffic, not a network traffic grapher.</p></div><div id="comment-46262-info" class="comment-info"><span class="comment-age">(29 Sep '15, 09:40)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="46271"></span><div id="comment-46271" class="comment"><div id="post-46271-score" class="comment-score"></div><div class="comment-text"><p>I basically need to monitor how much the network is being used for A SINGLE LAPTOP. Just amounts of mb going up and down. Initially I have no interest in what kind of data it is. Which free software of max 10 $ would you advise for this purpose?</p></div><div id="comment-46271-info" class="comment-info"><span class="comment-age">(29 Sep '15, 17:13)</span> <span class="comment-user userinfo">PAULWALKER</span></div></div><span id="46275"></span><div id="comment-46275" class="comment"><div id="post-46275-score" class="comment-score"></div><div class="comment-text"><p>Please choose one yourself!</p><blockquote><p><a href="https://www.google.com/?q=windows+network+traffic+monitor">https://www.google.com/?q=windows+network+traffic+monitor</a></p></blockquote></div><div id="comment-46275-info" class="comment-info"><span class="comment-age">(29 Sep '15, 19:33)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="46279"></span><div id="comment-46279" class="comment"><div id="post-46279-score" class="comment-score"></div><div class="comment-text"><p>ok thanks guys. since I downloaded wireshark, i didnt know exactly what I am looking for. think maybe i know a bit better now. had hoped someone knew THE software. anyway thanks again.</p></div><div id="comment-46279-info" class="comment-info"><span class="comment-age">(30 Sep '15, 04:30)</span> <span class="comment-user userinfo">PAULWALKER</span></div></div></div><div id="comment-tools-46255" class="comment-tools"></div><div class="clear"></div><div id="comment-46255-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46277"></span>

<div id="answer-container-46277" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-46277-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-46277-score" class="post-score" title="current number of votes">0</div><span id="post-46277-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You'll need to find the right tool for the job and Wireshark isn't it I'm afraid. Wireshark is a power tool to drill into every little details of every packet it gets its hands on. Meanwhile what you need is an aggregator tool which collects and compiles statistics over long term use. That's a whole different ballgame, where other tools come into play. Depending on your platform and OS various options are available, see the comments.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Sep '15, 01:44</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-46277" class="comments-container"></div><div id="comment-tools-46277" class="comment-tools"></div><div class="clear"></div><div id="comment-46277-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

