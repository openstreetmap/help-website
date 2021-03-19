+++
type = "question"
title = "problem with dissector_add function.."
description = '''I have to design a dissector for core to core messages. In the code, inside the proto_ reg_ handoff_ccm() function, dissector_ handle_ t ccm_ handle; ccm_ handle=new_ create_ dissector_ handle(dissect_ ccm, proto_ ccm); dissector_ add(...............................................); I have a proble...'''
date = "2011-02-16T22:22:00Z"
lastmod = "2012-11-27T14:46:00Z"
weight = 2392
keywords = [ "dissector", "wireshark" ]
aliases = [ "/questions/2392" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [problem with dissector\_add function..](/questions/2392/problem-with-dissector_add-function)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2392-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2392-score" class="post-score" title="current number of votes">0</div><span id="post-2392-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have to design a dissector for core to core messages. In the code, inside the proto_ reg_ handoff_ccm() function,</p><p>dissector_ handle_ t ccm_ handle;</p><p>ccm_ handle=new_ create_ dissector_ handle(dissect_ ccm, proto_ ccm);</p><p>dissector_ add(...............................................);</p><p>I have a problem in writing this third line. There are three options;</p><ol><li>dissector_ add("wtap_ encap", WTAP_ ENCAP_ CCM, ccm_ handle);</li><li>dissector_ add(" ", NULL, ccm_ handle);</li></ol><p>What should I use?? Or if I am completely mistaken and I have to rather write something completely different..</p><p>please reply,</p><p>Thanks and Regards, Sid</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '11, 22:22</strong></p><img src="https://secure.gravatar.com/avatar/5a41ae1c710064aebdb9a4e0a1788d12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sid&#39;s gravatar image" /><p><span>sid</span><br />
<span class="score" title="45 reputation points">45</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sid has no accepted answers">0%</span></p></div></div><div id="comments-container-2392" class="comments-container"></div><div id="comment-tools-2392" class="comment-tools"></div><div class="clear"></div><div id="comment-2392-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16355"></span>

<div id="answer-container-16355" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16355-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16355-score" class="post-score" title="current number of votes">0</div><span id="post-16355-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See the discussion on <a href="http://ask.wireshark.org/questions/2341/dissector-for-core-to-core-messages-ie-shared-memory-messages">another one of your questions</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '12, 14:46</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-16355" class="comments-container"></div><div id="comment-tools-16355" class="comment-tools"></div><div class="clear"></div><div id="comment-16355-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

