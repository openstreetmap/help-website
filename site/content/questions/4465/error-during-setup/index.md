+++
type = "question"
title = "error during setup"
description = '''while running &quot;nmake -f makefile.nmake verify_tools &quot; i am getting an error as end of file found before next directive, i replaced make file with other makefile but its still giving the same error. please reply if u hv any idea to solve this case.'''
date = "2011-06-08T22:22:00Z"
lastmod = "2011-06-09T20:00:00Z"
weight = 4465
keywords = [ "compile" ]
aliases = [ "/questions/4465" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [error during setup](/questions/4465/error-during-setup)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4465-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4465-score" class="post-score" title="current number of votes">0</div><span id="post-4465-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>while running <strong>"nmake -f makefile.nmake verify_tools "</strong> i am getting an error as end of file found before next directive, i replaced make file with other makefile but its still giving the same error. please reply if u hv any idea to solve this case.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-compile" rel="tag" title="see questions tagged &#39;compile&#39;">compile</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '11, 22:22</strong></p><img src="https://secure.gravatar.com/avatar/257c9f9e498193d7ddde57090efe094a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sagu072&#39;s gravatar image" /><p><span>sagu072</span><br />
<span class="score" title="35 reputation points">35</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sagu072 has no accepted answers">0%</span></p></div></div><div id="comments-container-4465" class="comments-container"></div><div id="comment-tools-4465" class="comment-tools"></div><div class="clear"></div><div id="comment-4465-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4486"></span>

<div id="answer-container-4486" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4486-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4486-score" class="post-score" title="current number of votes">0</div><span id="post-4486-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What do you mean by, <em>"i replaced make file with other makefile"</em>? Which makefile(s) are you referring to? It sounds like you might have made some modifications to one or more files, with one makefile in particular being one you tried to revert back to the original, but without luck.</p><p>Assuming that's the case, then I would suggest that you download Wireshark sources again and make sure you're able to run <strong>"nmake -f makefile.nmake verify_tools "</strong> with the stock Wireshark sources first before you try modifying anything. Once you confirm that you can do that, then make modifications as needed. Better still might be to have 2 complete source directories - one that is left untouched and one that you are working on. If you happen to break something in your working copy, you can run a diff against the pristine sources to help you determine what you might have done wrong.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jun '11, 20:00</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-4486" class="comments-container"></div><div id="comment-tools-4486" class="comment-tools"></div><div class="clear"></div><div id="comment-4486-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

