+++
type = "question"
title = "Translating a dissector from Lua to C"
description = '''Are there any examples of dissectors written in Lua that have been translated to C? I&#x27;m a beginner and have written a dissector in Lua - now that it does what I want it to, I&#x27;d like to write it in C. I know about the development guide and the README, but was looking for a more tangible example to pu...'''
date = "2016-05-31T15:27:00Z"
lastmod = "2016-07-19T02:29:00Z"
weight = 53086
keywords = [ "lua", "c", "dissector", "wireshark" ]
aliases = [ "/questions/53086" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Translating a dissector from Lua to C](/questions/53086/translating-a-dissector-from-lua-to-c)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53086-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53086-score" class="post-score" title="current number of votes">0</div><span id="post-53086-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Are there any examples of dissectors written in Lua that have been translated to C? I'm a beginner and have written a dissector in Lua - now that it does what I want it to, I'd like to write it in C. I know about the development guide and the README, but was looking for a more tangible example to put it in context.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-c" rel="tag" title="see questions tagged &#39;c&#39;">c</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 May '16, 15:27</strong></p><img src="https://secure.gravatar.com/avatar/69337c614f643f05439087eb2c42ac6d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="osarkar&#39;s gravatar image" /><p><span>osarkar</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="osarkar has no accepted answers">0%</span></p></div></div><div id="comments-container-53086" class="comments-container"></div><div id="comment-tools-53086" class="comment-tools"></div><div class="clear"></div><div id="comment-53086-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54135"></span>

<div id="answer-container-54135" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54135-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54135-score" class="post-score" title="current number of votes">1</div><span id="post-54135-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You could try visiting the <a href="https://sharkfest.wireshark.org/sf16.html">Sharkfest 2016 Retrospective</a> page and looking at <a href="https://ask.wireshark.org/users/1225/grahamb">Graham Bloice</a>'s presentation (and related materials) titled, "<a href="https://sharkfest.wireshark.org/assets/presentations16/03.7z">Writing a Dissector: 3 Way to Eat Bytes</a>". When you unzip the .7z archive (using <a href="http://7-zip.org/">7-zip</a>), you'll not only have the presentation but a sample dissector written in C and Lua as well as in <a href="http://wsgd.free.fr/">wsgd</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jul '16, 11:00</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-54135" class="comments-container"><span id="54154"></span><div id="comment-54154" class="comment"><div id="post-54154-score" class="comment-score"></div><div class="comment-text"><p>The example dissector is very basic, but is meant to show the difference in the "boilerplate" parts needed for a dissector.</p></div><div id="comment-54154-info" class="comment-info"><span class="comment-age">(19 Jul '16, 02:29)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-54135" class="comment-tools"></div><div class="clear"></div><div id="comment-54135-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

