+++
type = "question"
title = "How best to customize wireshark?"
description = '''At work, I currently have an application which uses the libpcap API to do packet sniffing of our internal TCP messages (and to do various things with the data that&#x27;s sniffed). I am considering converting this application into an application that uses wireshark instead (since the visualization of the...'''
date = "2011-08-11T16:06:00Z"
lastmod = "2011-08-17T22:09:00Z"
weight = 5659
keywords = [ "development", "lua", "dissector" ]
aliases = [ "/questions/5659" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How best to customize wireshark?](/questions/5659/how-best-to-customize-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5659-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5659-score" class="post-score" title="current number of votes">0</div><span id="post-5659-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>At work, I currently have an application which uses the libpcap API to do packet sniffing of our internal TCP messages (and to do various things with the data that's sniffed). I am considering converting this application into an application that uses wireshark instead (since the visualization of the data that wireshark provides is great, and since I'd like to take advantage of all of the other capabilities that wireshark provides).</p><p>My question is: what is the best method to go about this? I see that I can either modify the C code itself or use the lua API. (I know C, and I don't know anything about lua.)</p><p>I guess I would want to add dissectors, but I would also want to add the capability to trigger an event that would receive packet data and do specific things with that data. (Listener?)</p><p>I guess the main question is whether to modify the C or use lua...and if you have any other specific advice that would be great. Let me know if you have any other questions about what I'm trying to accomplish. Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Aug '11, 16:06</strong></p><img src="https://secure.gravatar.com/avatar/851676df3c7a09999c0522099f40d6e1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JVo&#39;s gravatar image" /><p><span>JVo</span><br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JVo has no accepted answers">0%</span></p></div></div><div id="comments-container-5659" class="comments-container"><span id="5733"></span><div id="comment-5733" class="comment"><div id="post-5733-score" class="comment-score"></div><div class="comment-text"><p>possible <a href="http://ask.wireshark.org/questions/5724/adding-a-listener">duplicate</a></p></div><div id="comment-5733-info" class="comment-info"><span class="comment-age">(17 Aug '11, 22:09)</span> <span class="comment-user userinfo">helloworld</span></div></div></div><div id="comment-tools-5659" class="comment-tools"></div><div class="clear"></div><div id="comment-5659-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5672"></span>

<div id="answer-container-5672" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5672-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5672-score" class="post-score" title="current number of votes">0</div><span id="post-5672-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds like a dissector and tap listener, although 'trigger an event that would receive packet data' is not all to clear to me.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Aug '11, 01:42</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-5672" class="comments-container"><span id="5687"></span><div id="comment-5687" class="comment"><div id="post-5687-score" class="comment-score"></div><div class="comment-text"><p>Thanks. Any thoughts on whether to use lua or modify the C++ for dissectors and listeners?</p></div><div id="comment-5687-info" class="comment-info"><span class="comment-age">(12 Aug '11, 10:31)</span> <span class="comment-user userinfo">JVo</span></div></div><span id="5688"></span><div id="comment-5688" class="comment"><div id="post-5688-score" class="comment-score"></div><div class="comment-text"><p>Lua or C (no C++ (!)), or even python are possible. Think about the most appropriate language for your work, organization and maintainability. I've little experience with Lua of Python in this context; using C, Wiresharks native programming language gives most power.</p></div><div id="comment-5688-info" class="comment-info"><span class="comment-age">(12 Aug '11, 11:26)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-5672" class="comment-tools"></div><div class="clear"></div><div id="comment-5672-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

