+++
type = "question"
title = "1.10.x with Lua"
description = '''Is there a built version of 1.10.x with lua enabled? I have downloaded 1.10.2pre1-51630 on osx and it shows without Lua in the about dialog. If I need to compile myself where can I find some documentstion'''
date = "2013-09-06T07:41:00Z"
lastmod = "2013-09-06T11:57:00Z"
weight = 24426
keywords = [ "compile", "lua", "1.10.0" ]
aliases = [ "/questions/24426" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [1.10.x with Lua](/questions/24426/110x-with-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24426-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24426-score" class="post-score" title="current number of votes">0</div><span id="post-24426-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a built version of 1.10.x with lua enabled? I have downloaded 1.10.2pre1-51630 on osx and it shows without Lua in the about dialog.</p><p>If I need to compile myself where can I find some documentstion</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-compile" rel="tag" title="see questions tagged &#39;compile&#39;">compile</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-1.10.0" rel="tag" title="see questions tagged &#39;1.10.0&#39;">1.10.0</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Sep '13, 07:41</strong></p><img src="https://secure.gravatar.com/avatar/2c43a46da2e699c6ea7e39ba5fc2b6ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hoss&#39;s gravatar image" /><p><span>Hoss</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hoss has no accepted answers">0%</span></p></div></div><div id="comments-container-24426" class="comments-container"><span id="24427"></span><div id="comment-24427" class="comment"><div id="post-24427-score" class="comment-score"></div><div class="comment-text"><p>I ended up installing <code>1.11.0-SVN-51797</code> and that at least works with my script.</p></div><div id="comment-24427-info" class="comment-info"><span class="comment-age">(06 Sep '13, 08:04)</span> <span class="comment-user userinfo">Hoss</span></div></div></div><div id="comment-tools-24426" class="comment-tools"></div><div class="clear"></div><div id="comment-24426-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="24438"></span>

<div id="answer-container-24438" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24438-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24438-score" class="post-score" title="current number of votes">2</div><span id="post-24438-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Hoss has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I have downloaded 1.10.2pre1-51630 on osx and it shows without Lua in the about dialog.</p></blockquote><p>From a quick look at the most recent 1.10 buildbot logs on the 32-bit and 64-bit buildbots, the 64-bit buildbot is building with Lua (so it should say it's built with Lua), but the 32-bit buildbot is finding Lua 5.2 with the configure script but failing to find <code>luaL_openlibs</code> in the library (so it will be built without Lua). This could be a bug in the build process, so please file this as a bug on <a href="http://bugs.wireshark.org">the Wireshark Bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Sep '13, 11:57</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-24438" class="comments-container"></div><div id="comment-tools-24438" class="comment-tools"></div><div class="clear"></div><div id="comment-24438-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24430"></span>

<div id="answer-container-24430" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24430-score" class="post-score" title="current number of votes">0</div><span id="post-24430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you need to compile Wireshark yourself, you can refer to the <a href="http://www.wireshark.org/docs/wsdg_html_chunked/">developer's guide</a>, or probably even more useful to you is the information in the <a href="http://anonsvn.wireshark.org/viewvc/trunk/README.macos?revision=46953&amp;view=markup">README.macos</a> file, which you will find after <a href="http://www.wireshark.org/download.html">downloading</a> the Wireshark sources.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Sep '13, 08:29</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-24430" class="comments-container"></div><div id="comment-tools-24430" class="comment-tools"></div><div class="clear"></div><div id="comment-24430-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

