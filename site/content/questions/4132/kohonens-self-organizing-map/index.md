+++
type = "question"
title = "Kohonen&#x27;s Self-Organizing Map"
description = '''How can I add visualization capabilities to wireshark ? Like to add SOM capabilities ?'''
date = "2011-05-19T00:48:00Z"
lastmod = "2011-05-19T13:57:00Z"
weight = 4132
keywords = [ "som" ]
aliases = [ "/questions/4132" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Kohonen's Self-Organizing Map](/questions/4132/kohonens-self-organizing-map)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4132-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4132-score" class="post-score" title="current number of votes">0</div><span id="post-4132-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I add visualization capabilities to wireshark ? Like to add SOM capabilities ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-som" rel="tag" title="see questions tagged &#39;som&#39;">som</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '11, 00:48</strong></p><img src="https://secure.gravatar.com/avatar/8689ba501f7e1c3a5fa28a1eb3b7e981?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alia%20ElRoubi&#39;s gravatar image" /><p><span>Alia ElRoubi</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alia ElRoubi has no accepted answers">0%</span></p></div></div><div id="comments-container-4132" class="comments-container"></div><div id="comment-tools-4132" class="comment-tools"></div><div class="clear"></div><div id="comment-4132-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4148"></span>

<div id="answer-container-4148" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4148-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4148-score" class="post-score" title="current number of votes">2</div><span id="post-4148-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>By writing code. :-)</p><p>I assume the idea is to generate a <a href="http://www.willamette.edu/~gorr/classes/cs449/Unsupervised/SOM.html">self-organizing map</a> of network hosts, with the input layer being the sending hosts and the output layer being the receiving hosts. You'd probably make a tap listener, similar to, say, the conversation tap listeners, so you get to look at all the packets to see which hosts are sending to which hosts, choose some form of weight for each such link (choosing a weight is left as an exercise for the reader), and generate and draw the map. Writing the code to implement Kohonen's algorithm (I'm not sure whether a network map would be fully connected, but maybe the idea is that you set the distance between unconnected nodes to infinity) and to draw the result is also left as an exercise for the reader.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '11, 13:12</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-4148" class="comments-container"><span id="4149"></span><div id="comment-4149" class="comment"><div id="post-4149-score" class="comment-score"></div><div class="comment-text"><p>I mean do I program it using Visual C++ as a Plugin to wireshark. Thanks in advance.</p></div><div id="comment-4149-info" class="comment-info"><span class="comment-age">(19 May '11, 13:52)</span> <span class="comment-user userinfo">Alia ElRoubi</span></div></div><span id="4151"></span><div id="comment-4151" class="comment"><div id="post-4151-score" class="comment-score"></div><div class="comment-text"><p>(If you're asking additional questions, they should be comments, not answers.)</p><p>You could program it as a plugin - Wireshark does support plugin tap listeners. The GUI code might have to be written for GTK+, not any Windows GUI APIs, however. C will work; C++ plugins should, in theory, be implementable as well (see, for example, the <a href="http://wsgd.free.fr/">Wireshark Generic Dissector</a>, although that's a dissector plugin rather than a tap listener plugin).</p></div><div id="comment-4151-info" class="comment-info"><span class="comment-age">(19 May '11, 13:57)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-4148" class="comment-tools"></div><div class="clear"></div><div id="comment-4148-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

