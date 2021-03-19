+++
type = "question"
title = "fragment_table_init (unknown symbol)"
description = '''Hi, I inherited some dissector code from a former colleague, which runs well under windows (V1.7.2). Now I wanted to port it to linux, using the latest wireshark code base (svn; but problem also occurs with latest stable). My dissector plugin compiles without problems, but when starting wireshark, I...'''
date = "2013-07-11T23:38:00Z"
lastmod = "2013-07-12T08:31:00Z"
weight = 22884
keywords = [ "dissector", "fragmented_ip", "linux" ]
aliases = [ "/questions/22884" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [fragment\_table\_init (unknown symbol)](/questions/22884/fragment_table_init-unknown-symbol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22884-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22884-score" class="post-score" title="current number of votes">0</div><span id="post-22884-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I inherited some dissector code from a former colleague, which runs well under windows (V1.7.2). Now I wanted to port it to linux, using the latest wireshark code base (svn; but problem also occurs with latest stable).</p><p>My dissector plugin compiles without problems, but when starting wireshark, I get the error message <code>undefined symbol: fragment_table_init</code>.</p><p>Do I have to link my plugin against any library? Why is this not handled by make-dissector-reg or makefile.am or what else automatically?</p><p>Thanks for any help!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-fragmented_ip" rel="tag" title="see questions tagged &#39;fragmented_ip&#39;">fragmented_ip</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jul '13, 23:38</strong></p><img src="https://secure.gravatar.com/avatar/93cc10f2a772e3751b6434924d077b39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Atlantis&#39;s gravatar image" /><p><span>Atlantis</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Atlantis has no accepted answers">0%</span></p></div></div><div id="comments-container-22884" class="comments-container"><span id="22885"></span><div id="comment-22885" class="comment"><div id="post-22885-score" class="comment-score"></div><div class="comment-text"><p>Oh - I forgot - I am running an Ubuntu 13.04 64bit Linux ...</p></div><div id="comment-22885-info" class="comment-info"><span class="comment-age">(11 Jul '13, 23:39)</span> <span class="comment-user userinfo">Atlantis</span></div></div></div><div id="comment-tools-22884" class="comment-tools"></div><div class="clear"></div><div id="comment-22884-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22889"></span>

<div id="answer-container-22889" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22889-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22889-score" class="post-score" title="current number of votes">3</div><span id="post-22889-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JeffMorriss has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The dissector does reassembly, and the reassembly APIs changed in 1.10. That's why it won't build; you're probably building against a recent version of Wireshark, either 1.10.0 or the trunk. ("Without problems" probably <em>really</em> means "without fatal errors"; it probably compiles with warnings that represent real problems.)</p><p>See, for example, the difference between revisions 48490 and 48491 of <code>epan/dissectors/packet-ip.c</code> for an example of the changes you will need to make in order to make the dissector work with Wireshark 1.10.0 or later.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jul '13, 00:54</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-22889" class="comments-container"><span id="22893"></span><div id="comment-22893" class="comment"><div id="post-22893-score" class="comment-score"></div><div class="comment-text"><p>Great - you saved my day ...</p><p>With the information from the mentioned patch I was able to modify my dissector. I still get lots of warnings from the code so maybe you are right that I got a <em>severe</em> warning previously but could not identify it due to all the other warnings ...</p><p>Thanks!</p></div><div id="comment-22893-info" class="comment-info"><span class="comment-age">(12 Jul '13, 02:00)</span> <span class="comment-user userinfo">Atlantis</span></div></div><span id="22920"></span><div id="comment-22920" class="comment"><div id="post-22920-score" class="comment-score"></div><div class="comment-text"><p>The Wireshark buildbots build most source files modules with the "warnings are errors" flag turned on in the compiler, so that various problems are caught. (The exceptions are mostly source files generated by Flex/yacc/Lemon/other code generators, where the warnings are difficult or impossible to eliminate.)</p></div><div id="comment-22920-info" class="comment-info"><span class="comment-age">(12 Jul '13, 08:31)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-22889" class="comment-tools"></div><div class="clear"></div><div id="comment-22889-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

