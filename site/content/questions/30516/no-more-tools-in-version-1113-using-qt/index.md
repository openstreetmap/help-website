+++
type = "question"
title = "No more &quot;tools&quot; in version 1.11.3 using QT"
description = '''The &quot;tools&quot; item is gone in the 1.11.3 nightly build of Wireshark (using QT). So I don&#x27;t have the Lua options under it anymore. Can we get it back?'''
date = "2014-03-06T20:05:00Z"
lastmod = "2014-03-07T07:49:00Z"
weight = 30516
keywords = [ "menu", "qt", "lua" ]
aliases = [ "/questions/30516" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [No more "tools" in version 1.11.3 using QT](/questions/30516/no-more-tools-in-version-1113-using-qt)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30516-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30516-score" class="post-score" title="current number of votes">0</div><span id="post-30516-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The "tools" item is gone in the 1.11.3 nightly build of Wireshark (using QT). So I don't have the Lua options under it anymore. Can we get it back?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-menu" rel="tag" title="see questions tagged &#39;menu&#39;">menu</span> <span class="post-tag tag-link-qt" rel="tag" title="see questions tagged &#39;qt&#39;">qt</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '14, 20:05</strong></p><img src="https://secure.gravatar.com/avatar/b18cada3e3589f311e24f5ffbd1737bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YXI&#39;s gravatar image" /><p><span>YXI</span><br />
<span class="score" title="21 reputation points">21</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YXI has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> retagged <strong>06 Mar '14, 21:34</strong> </span></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span></p></div></div><div id="comments-container-30516" class="comments-container"><span id="30520"></span><div id="comment-30520" class="comment"><div id="post-30520-score" class="comment-score"></div><div class="comment-text"><p>Hmmm... sorry about that - I wasn't even able to compile the Qt version until a couple days ago, due to changes in Qt 5.2 and my using a Mac with Mavericks. I'll add a bug to go add that menu in, but it'll be a while before that gets done.</p></div><div id="comment-30520-info" class="comment-info"><span class="comment-age">(06 Mar '14, 21:55)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="30548"></span><div id="comment-30548" class="comment"><div id="post-30548-score" class="comment-score"></div><div class="comment-text"><p>No rush. I can do what I need with tshark, or launching the whole Wireshark again. I can also use the GTK version of 1.11, which does have tools.</p></div><div id="comment-30548-info" class="comment-info"><span class="comment-age">(07 Mar '14, 07:49)</span> <span class="comment-user userinfo">YXI</span></div></div></div><div id="comment-tools-30516" class="comment-tools"></div><div class="clear"></div><div id="comment-30516-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30519"></span>

<div id="answer-container-30519" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30519-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30519-score" class="post-score" title="current number of votes">1</div><span id="post-30519-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>using QT</p></blockquote><p>To quote <a href="http://wiki.wireshark.org/Development/QtShark">the QtShark page on the Wireshark Wiki</a>, "An initial port to Qt (aka QtShark) has begun but there is lots of work to do." The 1.11 builds do not have full functionality, so there is a tradeoff between new stuff in 1.11 and stuff that hasn't yet been ported to Qt. Stuff will be ported as people find the time and energy to do so.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '14, 20:40</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-30519" class="comments-container"></div><div id="comment-tools-30519" class="comment-tools"></div><div class="clear"></div><div id="comment-30519-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

