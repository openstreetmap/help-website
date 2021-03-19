+++
type = "question"
title = "TCP&#92;HTTP reassemble"
description = '''Hi, I would like to write code in c++ that reassemble http request response packets and save then in some container.. so I downloaded the wireshark source code and found the packet-http.c and packet-http.h code. I tried to look for the actual parts that using this code to reassemble the TCP packets ...'''
date = "2017-07-15T05:31:00Z"
lastmod = "2017-07-15T09:51:00Z"
weight = 62798
keywords = [ "reassembly", "http", "tcp" ]
aliases = [ "/questions/62798" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP\\HTTP reassemble](/questions/62798/tcphttp-reassemble)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62798-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62798-score" class="post-score" title="current number of votes">0</div><span id="post-62798-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I would like to write code in c++ that reassemble http request response packets and save then in some container..</p><p>so I downloaded the wireshark source code and found the <code>packet-http.c</code> and <code>packet-http.h</code> code.</p><p>I tried to look for the actual parts that using this code to reassemble the TCP packets and get the HTTP request\response- but with no success.</p><p>It will be very helpful if someone could direct me to this HTTP request\response dissector, or to some code example for that matter.</p><p>What are the set of commands to "filetr" HTTP and where is the "pointer"\data structure that holds that request\response?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-reassembly" rel="tag" title="see questions tagged &#39;reassembly&#39;">reassembly</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '17, 05:31</strong></p><img src="https://secure.gravatar.com/avatar/19382512e78f5e497f0dfbd170a09837?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dr%20seuss&#39;s gravatar image" /><p><span>dr seuss</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dr seuss has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Jul '17, 06:07</strong> </span></p></div></div><div id="comments-container-62798" class="comments-container"></div><div id="comment-tools-62798" class="comment-tools"></div><div class="clear"></div><div id="comment-62798-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62802"></span>

<div id="answer-container-62802" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62802-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62802-score" class="post-score" title="current number of votes">0</div><span id="post-62802-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>TCP reassembly is carried out via several routines in packet-tcp.c and epan/reassemble.c. Note that the code is C, not C++ and is very complicated and unlikely to be easily extractable.</p><p>The code is licensed under GPL2, so please observe the license conditions.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '17, 07:40</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-62802" class="comments-container"><span id="62803"></span><div id="comment-62803" class="comment"><div id="post-62803-score" class="comment-score"></div><div class="comment-text"><p>Hi thank you for your answer, my goal is to extract the HTTP fields I dont want to reassemble the TCP packets on my own. I guess the HTTP dissector already does which is great. I just want to integrate this and pull out the HTTP header fields to my container. and C its also ok</p></div><div id="comment-62803-info" class="comment-info"><span class="comment-age">(15 Jul '17, 08:39)</span> <span class="comment-user userinfo">dr seuss</span></div></div><span id="62806"></span><div id="comment-62806" class="comment"><div id="post-62806-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately (for you) the Wireshark code is not structured that way, it works as a whole ensemble.</p><p>Maybe you could spawn tshark and apply filters and field selectors (<code>-T fields</code> &amp; <code>-e fieldname</code> ...) to achieve your needs.</p></div><div id="comment-62806-info" class="comment-info"><span class="comment-age">(15 Jul '17, 09:51)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-62802" class="comment-tools"></div><div class="clear"></div><div id="comment-62802-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

