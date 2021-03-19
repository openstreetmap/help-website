+++
type = "question"
title = "How to specify start and stop conditions?"
description = '''How to specify start and stop conditions to wireshark?'''
date = "2011-10-01T02:15:00Z"
lastmod = "2011-10-03T20:34:00Z"
weight = 6664
keywords = [ "trigger" ]
aliases = [ "/questions/6664" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to specify start and stop conditions?](/questions/6664/how-to-specify-start-and-stop-conditions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6664-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6664-score" class="post-score" title="current number of votes">0</div><span id="post-6664-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to specify start and stop conditions to wireshark?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-trigger" rel="tag" title="see questions tagged &#39;trigger&#39;">trigger</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Oct '11, 02:15</strong></p><img src="https://secure.gravatar.com/avatar/968cc7ddfc48322ffbd1d7f5e3d37b85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Terrestrial%20shark&#39;s gravatar image" /><p><span>Terrestrial ...</span><br />
<span class="score" title="96 reputation points">96</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Terrestrial shark has 3 accepted answers">42%</span></p></div></div><div id="comments-container-6664" class="comments-container"><span id="6669"></span><div id="comment-6669" class="comment"><div id="post-6669-score" class="comment-score"></div><div class="comment-text"><p>Do we have any updates with the triggers for wireshark? Is there any research being done? I need them badly. May i know the details like: what all the files that can be changed to bring triggers into effect? when triggers are possible using dumpcap or trigcap, why not with wireshark? Please help.</p></div><div id="comment-6669-info" class="comment-info"><span class="comment-age">(01 Oct '11, 03:24)</span> <span class="comment-user userinfo">Terrestrial ...</span></div></div></div><div id="comment-tools-6664" class="comment-tools"></div><div class="clear"></div><div id="comment-6664-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6688"></span>

<div id="answer-container-6688" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6688-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6688-score" class="post-score" title="current number of votes">2</div><span id="post-6688-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Terrestrial shark has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As I think you noticed in another question, capture triggers are not something which have been finished; there's a proof-of-concept in <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=2039">bug 2039</a>. So for now the answer to your questions is basically: there are no triggers until someone has time to [finish] implement[ing] them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Oct '11, 11:44</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-6688" class="comments-container"><span id="6690"></span><div id="comment-6690" class="comment"><div id="post-6690-score" class="comment-score"></div><div class="comment-text"><p>See also <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3967">bug 3967</a>.</p></div><div id="comment-6690-info" class="comment-info"><span class="comment-age">(03 Oct '11, 20:34)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-6688" class="comment-tools"></div><div class="clear"></div><div id="comment-6688-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

