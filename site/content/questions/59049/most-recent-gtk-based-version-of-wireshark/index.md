+++
type = "question"
title = "most recent GTK based version of Wireshark"
description = '''I am taking a Wireshark course from CBT Nuggets and the instructor is using version 1.8.7 which I believe is based on GTK. This appears to have a number of changes and some of them are really quite useful and appear to add a lot of functionality that does not appear to be available yet in the 2.2.1 ...'''
date = "2017-01-25T09:35:00Z"
lastmod = "2017-01-25T14:39:00Z"
weight = 59049
keywords = [ "pedro", "presidente" ]
aliases = [ "/questions/59049" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [most recent GTK based version of Wireshark](/questions/59049/most-recent-gtk-based-version-of-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59049-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59049-score" class="post-score" title="current number of votes">0</div><span id="post-59049-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am taking a Wireshark course from CBT Nuggets and the instructor is using version 1.8.7 which I believe is based on GTK. This appears to have a number of changes and some of them are really quite useful and appear to add a lot of functionality that does not appear to be available yet in the 2.2.1 version I am using. Are all the older version before 2.0 based on GTK and therefore likely to have the features like history for packet browsing and builtin ip address name resolution? These are just two things I have found so far that I could benefit from. I'm all for using the newer version but it seems like there are some features missing that I would rather wait on before moving up to version 2.x releases.</p><p>Opinions?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pedro" rel="tag" title="see questions tagged &#39;pedro&#39;">pedro</span> <span class="post-tag tag-link-presidente" rel="tag" title="see questions tagged &#39;presidente&#39;">presidente</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jan '17, 09:35</strong></p><img src="https://secure.gravatar.com/avatar/5aeb2216f3b1152c2e1e048efec95563?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="spkay31&#39;s gravatar image" /><p><span>spkay31</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="spkay31 has no accepted answers">0%</span></p></div></div><div id="comments-container-59049" class="comments-container"></div><div id="comment-tools-59049" class="comment-tools"></div><div class="clear"></div><div id="comment-59049-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59051"></span>

<div id="answer-container-59051" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59051-score" class="post-score" title="current number of votes">0</div><span id="post-59051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As mentioned elsewhere Wireshark is likely to be dropping the GTK builds for Windows and macOS for version 2.4.x.</p><p>You can see some info about the changes to the UI toolkits listed on the <a href="https://wiki.wireshark.org/Development/LifeCycle">LifeCycle</a> wiki page.</p><p>Name resolution is available in both versions, that's provided by the dissection library which is common between GTK and Qt.</p><p>For info about the Qt port (not entirely sure if it's up to date) see the wiki page <a href="https://wiki.wireshark.org/Development/QtShark">here</a>. If you follow the link for the Qt UI bugs note that a lot of them aren't actually Qt UI bugs, they need to be moved to a different category.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jan '17, 09:55</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-59051" class="comments-container"><span id="59068"></span><div id="comment-59068" class="comment"><div id="post-59068-score" class="comment-score"></div><div class="comment-text"><p>If you think there are missing features, please file bugs on them at <a href="http://bugs.wireshark.org">the Wireshark Bugzilla</a>.</p></div><div id="comment-59068-info" class="comment-info"><span class="comment-age">(25 Jan '17, 14:39)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-59051" class="comment-tools"></div><div class="clear"></div><div id="comment-59051-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

