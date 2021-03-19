+++
type = "question"
title = "dissector accessed an invalid memory address"
description = '''Hi all, I&#x27;m trying to modify a code of packet-data.c in order to change some piece of code. Then, i run a command: tshark -r vnp2.pcapng  After some minutes, I got a problem of memory: ** (tshark.exe:6552): WARNING **: Dissector bug, protocol Data, in packet 82644:  STATUS_ACCESS_VIOLATION: dissecto...'''
date = "2014-09-16T19:32:00Z"
lastmod = "2014-09-18T02:25:00Z"
weight = 36387
keywords = [ "dissector", "tshark" ]
aliases = [ "/questions/36387" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [dissector accessed an invalid memory address](/questions/36387/dissector-accessed-an-invalid-memory-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36387-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36387-score" class="post-score" title="current number of votes">0</div><span id="post-36387-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I'm trying to modify a code of packet-data.c in order to change some piece of code. Then, i run a command:</p><pre><code>tshark -r vnp2.pcapng</code></pre><p>After some minutes, I got a problem of memory:</p><pre><code>** (tshark.exe:6552): WARNING **: Dissector bug, protocol Data, in packet 82644:
 STATUS_ACCESS_VIOLATION: dissector accessed an invalid memory address</code></pre><p>and the program crashed. I check the code and see that it could be caused by this code:</p><pre><code>sccp_sonnh = (guint8 *)malloc(sizeof(guint8)*nSccp_length);</code></pre><p>even I tried to free after using sccp:</p><pre><code>free(sccp_sonnh);</code></pre><p>At first, I think I should ask this question on StackOverFlow but finally, I think it is better to post on this forum because it is quite related to the source code of Wireshark. So, I have some questions:</p><ol><li>Is this code the root cause of this problem ?</li><li>Is there any way to solve this problem?</li><li>Is it possible to use malloc and free like this?</li><li>If NO, please provide me the way to declare an array with variable length (I can not do this, so I used malloc)</li></ol><p>Please help if you have any experience on this. Thank you so much!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Sep '14, 19:32</strong></p><img src="https://secure.gravatar.com/avatar/824a7342f59ff90e6040505b38626416?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hoangsonk49&#39;s gravatar image" /><p><span>hoangsonk49</span><br />
<span class="score" title="81 reputation points">81</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hoangsonk49 has 2 accepted answers">28%</span></p></div></div><div id="comments-container-36387" class="comments-container"></div><div id="comment-tools-36387" class="comment-tools"></div><div class="clear"></div><div id="comment-36387-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36395"></span>

<div id="answer-container-36395" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36395-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36395-score" class="post-score" title="current number of votes">1</div><span id="post-36395-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hoangsonk49 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Depending on which version of the source you're working with, Wireshark has had a number of memory allocators, the current one is wmem. See README.wmem in the doc directory of the source tree.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Sep '14, 01:45</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-36395" class="comments-container"><span id="36429"></span><div id="comment-36429" class="comment"><div id="post-36429-score" class="comment-score"></div><div class="comment-text"><p>Problem solved. I use wmem_alloc instead of malloc. Malloc and free should not be used for code modification. Thanks for your suggestion :)</p></div><div id="comment-36429-info" class="comment-info"><span class="comment-age">(17 Sep '14, 23:38)</span> <span class="comment-user userinfo">hoangsonk49</span></div></div><span id="36431"></span><div id="comment-36431" class="comment"><div id="post-36431-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-36431-info" class="comment-info"><span class="comment-age">(18 Sep '14, 02:25)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-36395" class="comment-tools"></div><div class="clear"></div><div id="comment-36395-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

