+++
type = "question"
title = "Debug console - nothing displayed"
description = '''I want to do some printf debugging and have used g_print() as described in http://wiki.wireshark.org/Development/Tips . I am setting the &quot;Open a console window&quot; dropdown to show &quot;Always (debugging)&quot;. I am building from SVN source using MSVC Express 2010. When I run Wireshark by double-clicking on th...'''
date = "2012-06-13T09:01:00Z"
lastmod = "2012-06-13T10:35:00Z"
weight = 11874
keywords = [ "debug", "console" ]
aliases = [ "/questions/11874" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Debug console - nothing displayed](/questions/11874/debug-console-nothing-displayed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11874-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11874-score" class="post-score" title="current number of votes">1</div><span id="post-11874-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to do some printf debugging and have used g_print() as described in <a href="http://wiki.wireshark.org/Development/Tips">http://wiki.wireshark.org/Development/Tips</a> .</p><p>I am setting the "Open a console window" dropdown to show "Always (debugging)".</p><p>I am building from SVN source using MSVC Express 2010. When I run Wireshark by double-clicking on the "Wireshark" icon in "wireshark-gtk2" directory, the console appears but there is no output at all apart from when I close Wireshark and it says "Press and key to exit".</p><p>I have read something about stdout redirects but I thought this only applied to dumppcap, not Wireshark itself.</p><p>Anyone any idea why g_print() isn't working? I can use fprintf() to a file OK but it is not as convenient</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-debug" rel="tag" title="see questions tagged &#39;debug&#39;">debug</span> <span class="post-tag tag-link-console" rel="tag" title="see questions tagged &#39;console&#39;">console</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jun '12, 09:01</strong></p><img src="https://secure.gravatar.com/avatar/06a5afffe289c6e8db91113fcae8ecb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="806cat&#39;s gravatar image" /><p><span>806cat</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="806cat has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Jun '12, 09:31</strong> </span></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span></p></div></div><div id="comments-container-11874" class="comments-container"><span id="11875"></span><div id="comment-11875" class="comment"><div id="post-11875-score" class="comment-score"></div><div class="comment-text"><p>Sorry, that should be "Press any key to exit" above</p></div><div id="comment-11875-info" class="comment-info"><span class="comment-age">(13 Jun '12, 09:02)</span> <span class="comment-user userinfo">806cat</span></div></div></div><div id="comment-tools-11874" class="comment-tools"></div><div class="clear"></div><div id="comment-11874-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11876"></span>

<div id="answer-container-11876" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11876-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11876-score" class="post-score" title="current number of votes">2</div><span id="post-11876-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>OK, I found the solution myself. Using g_print() doesn't work. If you use just printf(), then it does work. The Wiki page is misleading in this respect.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '12, 10:35</strong></p><img src="https://secure.gravatar.com/avatar/06a5afffe289c6e8db91113fcae8ecb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="806cat&#39;s gravatar image" /><p><span>806cat</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="806cat has no accepted answers">0%</span></p></div></div><div id="comments-container-11876" class="comments-container"></div><div id="comment-tools-11876" class="comment-tools"></div><div class="clear"></div><div id="comment-11876-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

