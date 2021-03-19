+++
type = "question"
title = "diameter response time"
description = '''I need the response time for each CCA paquet, so i&#x27;m trying with: tshark -r TraficoDiameter.pcap -d tcp.port==6553,diameter -R &quot;diameter.cmd.code == 272 &amp;amp;&amp;amp; diameter.resp_time&quot; -e diameter.resp_time -e frame.time_epoch -E separator=&quot;;&quot; -T fields this result is giving me: resp_time;epoch:time,...'''
date = "2013-04-23T10:48:00Z"
lastmod = "2013-07-17T15:38:00Z"
weight = 20740
keywords = [ "diameter" ]
aliases = [ "/questions/20740" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [diameter response time](/questions/20740/diameter-response-time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20740-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20740-score" class="post-score" title="current number of votes">0</div><span id="post-20740-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I need the response time for each CCA paquet, so i'm trying with: tshark -r TraficoDiameter.pcap -d tcp.port==6553,diameter -R "diameter.cmd.code == 272 &amp;&amp; diameter.resp_time" -e diameter.resp_time -e frame.time_epoch -E separator=";" -T fields</p><p>this result is giving me: resp_time;epoch:time, but some packets have several CCR so the result is: <strong>resp_time,resp_time,resp_time,...</strong>;epoch:time</p><p>there is a way to separate all resp_time with his own epoch time?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-diameter" rel="tag" title="see questions tagged &#39;diameter&#39;">diameter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '13, 10:48</strong></p><img src="https://secure.gravatar.com/avatar/ca20bac738bbb8b012045602a77d7115?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fachav2&#39;s gravatar image" /><p><span>fachav2</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fachav2 has no accepted answers">0%</span></p></div></div><div id="comments-container-20740" class="comments-container"><span id="23074"></span><div id="comment-23074" class="comment"><div id="post-23074-score" class="comment-score"></div><div class="comment-text"><p>Did you manage to work this out?</p><p>I'm also interested in this case.</p></div><div id="comment-23074-info" class="comment-info"><span class="comment-age">(17 Jul '13, 10:48)</span> <span class="comment-user userinfo">Edmond</span></div></div><span id="23077"></span><div id="comment-23077" class="comment"><div id="post-23077-score" class="comment-score"></div><div class="comment-text"><p>not yet, I`m thinking there is no solution for this, maybe with a post-result script. If you get something please tell to all here</p></div><div id="comment-23077-info" class="comment-info"><span class="comment-age">(17 Jul '13, 11:56)</span> <span class="comment-user userinfo">fachav2</span></div></div></div><div id="comment-tools-20740" class="comment-tools"></div><div class="clear"></div><div id="comment-20740-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23084"></span>

<div id="answer-container-23084" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23084-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23084-score" class="post-score" title="current number of votes">1</div><span id="post-23084-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please have a look at my answer to the following question.</p><blockquote><p><a href="http://ask.wireshark.org/questions/11265/tshark-e-occurrencea">http://ask.wireshark.org/questions/11265/tshark-e-occurrencea</a></p></blockquote><p>It contains a perl script to solve a similar problem. Maybe you can adapt it for your scenario. If that does not work, please check the Lua code in the answer of <span>@helloworld</span>.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jul '13, 15:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Jul '13, 16:10</strong> </span></p></div></div><div id="comments-container-23084" class="comments-container"></div><div id="comment-tools-23084" class="comment-tools"></div><div class="clear"></div><div id="comment-23084-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

