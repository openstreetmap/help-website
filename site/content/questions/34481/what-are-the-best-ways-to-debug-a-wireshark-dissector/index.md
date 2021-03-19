+++
type = "question"
title = "What are the best ways to debug a Wireshark Dissector?"
description = '''I&#x27;m testing someone&#x27;s else dissector which seems not working as expected in the decryption part that is related to Wireshark(more specifically, the file called packet-ssl-utils.c). I want to find out what is going wrong so I decided to debug the relevant code.  I built Wireshark under linux in the c...'''
date = "2014-07-08T15:41:00Z"
lastmod = "2014-07-15T10:57:00Z"
weight = 34481
keywords = [ "debug", "dissector", "wireshark", "linux" ]
aliases = [ "/questions/34481" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What are the best ways to debug a Wireshark Dissector?](/questions/34481/what-are-the-best-ways-to-debug-a-wireshark-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34481-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34481-score" class="post-score" title="current number of votes">0</div><span id="post-34481-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm testing someone's else dissector which seems not working as expected in the decryption part that is related to Wireshark(more specifically, the file called <strong>packet-ssl-utils.c</strong>). I want to find out what is going wrong so I decided to debug the relevant code.</p><p>I built Wireshark under linux in the command line and I used <strong>Mousepad</strong> text editor to add several <code>ssl_debug_print</code>f statements here and there but I found them not that practical to use. I feel this way is naive and I believe there should be more professional ways to accomplish this specific task but I'm really not sure what they are.</p><p>One solution I'm thinking in is rebuilding Wireshark in <strong>eclipse</strong> and use the debugger there. However, this solution seems to involve some complicated steps and I wasn't able to tell if it works or not based on the quick Google's search I did. So I thought that I can ask here about suggestions to methods or tools to use to debug a WireShark dissector.</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-debug" rel="tag" title="see questions tagged &#39;debug&#39;">debug</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jul '14, 15:41</strong></p><img src="https://secure.gravatar.com/avatar/5642d9fe33d29ee47043f7e5796e67aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flora&#39;s gravatar image" /><p><span>flora</span><br />
<span class="score" title="156 reputation points">156</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flora has 2 accepted answers">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Jul '14, 15:42</strong> </span></p></div></div><div id="comments-container-34481" class="comments-container"></div><div id="comment-tools-34481" class="comment-tools"></div><div class="clear"></div><div id="comment-34481-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34482"></span>

<div id="answer-container-34482" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34482-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34482-score" class="post-score" title="current number of votes">1</div><span id="post-34482-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="flora has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Well, I don't think there is a 'best' way, so I recommend to start with the Wiki</p><blockquote><p><a href="http://wiki.wireshark.org/Development/Tips">http://wiki.wireshark.org/Development/Tips</a></p></blockquote><p>Furthermore you could use your preferred debugger add some breakpoints with the G_BREAKPOINT() macro. See my comment in the following question:</p><blockquote><p><a href="http://ask.wireshark.org/questions/15602/how-to-debug-my-plugin-on-ubuntu-linux">http://ask.wireshark.org/questions/15602/how-to-debug-my-plugin-on-ubuntu-linux</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '14, 17:27</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-34482" class="comments-container"><span id="34671"></span><div id="comment-34671" class="comment"><div id="post-34671-score" class="comment-score"></div><div class="comment-text"><p>Thank you. The first link was really useful.</p></div><div id="comment-34671-info" class="comment-info"><span class="comment-age">(15 Jul '14, 10:41)</span> <span class="comment-user userinfo">flora</span></div></div><span id="34673"></span><div id="comment-34673" class="comment"><div id="post-34673-score" class="comment-score"></div><div class="comment-text"><p>You're welcome.</p></div><div id="comment-34673-info" class="comment-info"><span class="comment-age">(15 Jul '14, 10:57)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-34482" class="comment-tools"></div><div class="clear"></div><div id="comment-34482-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

