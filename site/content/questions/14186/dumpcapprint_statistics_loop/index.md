+++
type = "question"
title = "dumpcap:print_statistics_loop"
description = '''I was referred to dumpcap:print_statistics_loop by some of the experts here(forgive me if I don&#x27;t remember his name). Trying to import the function into my code I see no linkage to the function get_interface_list (my be some others also). So far I use WinPcap library. What should I do more? Regards ...'''
date = "2012-09-11T05:43:00Z"
lastmod = "2012-09-13T06:33:00Z"
weight = 14186
keywords = [ "winpcap" ]
aliases = [ "/questions/14186" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [dumpcap:print\_statistics\_loop](/questions/14186/dumpcapprint_statistics_loop)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14186-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14186-score" class="post-score" title="current number of votes">0</div><span id="post-14186-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was referred to dumpcap:print_statistics_loop by some of the experts here(forgive me if I don't remember his name). Trying to import the function into my code I see no linkage to the function get_interface_list (my be some others also). So far I use WinPcap library. What should I do more? Regards I. Lesher</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-winpcap" rel="tag" title="see questions tagged &#39;winpcap&#39;">winpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Sep '12, 05:43</strong></p><img src="https://secure.gravatar.com/avatar/c46b9d0cf13adb17325f5d9519406546?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="triplebit&#39;s gravatar image" /><p><span>triplebit</span><br />
<span class="score" title="1 reputation points">1</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="triplebit has no accepted answers">0%</span></p></div></div><div id="comments-container-14186" class="comments-container"></div><div id="comment-tools-14186" class="comment-tools"></div><div class="clear"></div><div id="comment-14186-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14232"></span>

<div id="answer-container-14232" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14232-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14232-score" class="post-score" title="current number of votes">0</div><span id="post-14232-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That was me, and it was just a hint to look at the code used there. You can't just import that function into your code, as that's all very specific to Wireshark.</p><p>What you need is the pcap_stats() function from WinPcap (<a href="http://www.winpcap.org">www.winpcap.org</a>), used in the mentioned dumpcap function.</p><p>I also mentioned the WinPcap developer guide, which I believe is the best way for you to get it working.</p><blockquote><p><code>http://ask.wireshark.org/questions/14077/display-packet-transitions-before-capturing</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Sep '12, 06:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-14232" class="comments-container"></div><div id="comment-tools-14232" class="comment-tools"></div><div class="clear"></div><div id="comment-14232-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

