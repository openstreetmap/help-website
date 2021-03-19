+++
type = "question"
title = "tcp options dissection"
description = '''I was wondering if there is some way to do this.   1. to decode the options part of tcp protocol or say dissect the options part of the tcp header.  2.once i decode the options part, get wireshark to do the rest of decoding as usual. There are certain options that wireshark shows as unknown. These c...'''
date = "2011-03-27T06:30:00Z"
lastmod = "2013-09-26T23:29:00Z"
weight = 3153
keywords = [ "dissector", "options", "tcp" ]
aliases = [ "/questions/3153" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tcp options dissection](/questions/3153/tcp-options-dissection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3153-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3153-score" class="post-score" title="current number of votes">0</div><span id="post-3153-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was wondering if there is some way to do this. 1. to decode the options part of tcp protocol or say dissect the options part of the tcp header. 2.once i decode the options part, get wireshark to do the rest of decoding as usual.</p><p>There are certain options that wireshark shows as unknown. These contain some important info which my company has requested me to dissect. Kindly let me know where I should make the change since the packet-tcp.c is very complicated</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-options" rel="tag" title="see questions tagged &#39;options&#39;">options</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Mar '11, 06:30</strong></p><img src="https://secure.gravatar.com/avatar/46023e482c60329a251a137848f8f5f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="niks3089&#39;s gravatar image" /><p><span>niks3089</span><br />
<span class="score" title="21 reputation points">21</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="niks3089 has no accepted answers">0%</span></p></div></div><div id="comments-container-3153" class="comments-container"></div><div id="comment-tools-3153" class="comment-tools"></div><div class="clear"></div><div id="comment-3153-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3162"></span>

<div id="answer-container-3162" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3162-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3162-score" class="post-score" title="current number of votes">1</div><span id="post-3162-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You should modify the tcpopts array to add the TCP options in question. See epan/ip_opts.h for the definition of the ip_tcp_opt structure.</p><p>If you have any more questions, you should ask them on the wireshark-dev mailing list; see <a href="http://www.wireshark.org/lists/">the Wireshark mailing list page</a> for more information.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '11, 14:35</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-3162" class="comments-container"><span id="25298"></span><div id="comment-25298" class="comment"><div id="post-25298-score" class="comment-score"></div><div class="comment-text"><p>Hi Is there anyway we can do this using the Lua dissector? I know I need to use the chained dissector but will I need to parse the Options from the beginning in order to reach the unknown part in the options or can I jump to the unknown part in the options?</p></div><div id="comment-25298-info" class="comment-info"><span class="comment-age">(26 Sep '13, 23:29)</span> <span class="comment-user userinfo">Vinay</span></div></div></div><div id="comment-tools-3162" class="comment-tools"></div><div class="clear"></div><div id="comment-3162-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

