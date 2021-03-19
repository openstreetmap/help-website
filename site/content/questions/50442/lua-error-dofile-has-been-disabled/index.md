+++
type = "question"
title = "Lua Error - dofile has been disabled"
description = '''Hi i run wireshark at root and see this error, and change disable_lua = false to true but after this wireshark crashed ... please help me... thanks Lua: Error during loading. [string &quot;/usr/share/wireshark/init.lua&quot;]:44 dofile has been disabled due to running Wireshark as superuser. See https:// wiki...'''
date = "2016-02-23T08:41:00Z"
lastmod = "2016-02-28T14:32:00Z"
weight = 50442
keywords = [ "lua", "dofile" ]
aliases = [ "/questions/50442" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Lua Error - dofile has been disabled](/questions/50442/lua-error-dofile-has-been-disabled)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50442-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50442-score" class="post-score" title="current number of votes">0</div><span id="post-50442-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi i run wireshark at root and see this error, and change disable_lua = false to true but after this wireshark crashed ... please help me... thanks</p><p>Lua: Error during loading. [string "/usr/share/wireshark/init.lua"]:44 dofile has been disabled due to running Wireshark as superuser. See https:// wiki.wireshark.org/CaptureSetup/CapturePrivileges for help in running Wireshark as an unprivileged user.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dofile" rel="tag" title="see questions tagged &#39;dofile&#39;">dofile</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Feb '16, 08:41</strong></p><img src="https://secure.gravatar.com/avatar/f28cf12a8aeea7ce3f65f537af81fcea?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TeVeN&#39;s gravatar image" /><p><span>TeVeN</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TeVeN has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Feb '16, 10:16</strong> </span></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-50442" class="comments-container"></div><div id="comment-tools-50442" class="comment-tools"></div><div class="clear"></div><div id="comment-50442-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="50446"></span>

<div id="answer-container-50446" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50446-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50446-score" class="post-score" title="current number of votes">0</div><span id="post-50446-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The error message from Lua is not a crash (or is not the cause of a crash). It's just telling you that certain parts of Lua aren't going to work correctly because you're running Wireshark as root.</p><p>Really, don't do that (that is, don't run Wireshark as root). Wireshark has over 2 million lines of source code which are analyzing (potentially malicious) network traffic. See the URL quoted by the error message for instructions on setting up Wireshark so it will be able to run Wireshark as a non-root user while still being able to capture. It will also make Lua plugins work correctly.</p><p>If Wireshark really is crashing then that's almost certainly a separate issue. Does it crash if you run Wireshark as a normal user? Does it crash if you leave Lua fully disabled?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Feb '16, 11:41</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-50446" class="comments-container"><span id="50566"></span><div id="comment-50566" class="comment"><div id="post-50566-score" class="comment-score"></div><div class="comment-text"><p>Actually I was wrong: Wireshark does (did) crash when disable_lua was true. This was <a href="https://code.wireshark.org/review/14228">recently fixed</a> and will be fixed in 2.0.3.</p></div><div id="comment-50566-info" class="comment-info"><span class="comment-age">(28 Feb '16, 14:32)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-50446" class="comment-tools"></div><div class="clear"></div><div id="comment-50446-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="50443"></span>

<div id="answer-container-50443" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50443-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50443-score" class="post-score" title="current number of votes">-1</div><span id="post-50443-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>to fix this you want to remove your sudo privileges from the account you are working on. Make sure you don't need sudo to access any of the files that your script will be running on.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Feb '16, 10:01</strong></p><img src="https://secure.gravatar.com/avatar/2a64be647ac8ec21b76a6c042bebb6e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="testname0110&#39;s gravatar image" /><p><span>testname0110</span><br />
<span class="score" title="15 reputation points">15</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="testname0110 has 3 accepted answers">75%</span></p></div></div><div id="comments-container-50443" class="comments-container"></div><div id="comment-tools-50443" class="comment-tools"></div><div class="clear"></div><div id="comment-50443-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

