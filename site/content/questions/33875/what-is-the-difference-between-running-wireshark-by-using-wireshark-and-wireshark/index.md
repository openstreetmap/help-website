+++
type = "question"
title = "what is the difference between running Wireshark by using ./wireshark and wireshark?"
description = '''I&#x27;m asking because when I use ./wireshark I get an error message that is different from when I run it by using wireshark only. Thanks in advance!'''
date = "2014-06-16T16:44:00Z"
lastmod = "2014-06-17T08:14:00Z"
weight = 33875
keywords = [ "difference", "startup", "wireshark" ]
aliases = [ "/questions/33875" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [what is the difference between running Wireshark by using ./wireshark and wireshark?](/questions/33875/what-is-the-difference-between-running-wireshark-by-using-wireshark-and-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33875-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33875-score" class="post-score" title="current number of votes">0</div><span id="post-33875-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm asking because when I use ./wireshark I get an error message that is different from when I run it by using wireshark only.</p><p>Thanks in advance!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-difference" rel="tag" title="see questions tagged &#39;difference&#39;">difference</span> <span class="post-tag tag-link-startup" rel="tag" title="see questions tagged &#39;startup&#39;">startup</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jun '14, 16:44</strong></p><img src="https://secure.gravatar.com/avatar/5642d9fe33d29ee47043f7e5796e67aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flora&#39;s gravatar image" /><p><span>flora</span><br />
<span class="score" title="156 reputation points">156</span><span title="31 badges"><span class="badge1">●</span><span class="badgecount">31</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flora has 2 accepted answers">100%</span></p></div></div><div id="comments-container-33875" class="comments-container"></div><div id="comment-tools-33875" class="comment-tools"></div><div class="clear"></div><div id="comment-33875-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33876"></span>

<div id="answer-container-33876" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-33876-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-33876-score" class="post-score" title="current number of votes">1</div><span id="post-33876-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="flora has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In UNIX, a command on its own like "wireshark" will execute the "wireshark" program that is found in a directory in your "PATH" environmental variable. Using "./wireshark" would call the program "wireshark" in your current directory.</p><p>The distinction is useful if you have multiple versions of wireshark installed. To see which wireshark will be run when you just type "wireshark" try typing the command "which wireshark" and it will tell you what one is found in directories in your "PATH".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Jun '14, 18:20</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p><span>Quadratic</span><br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Jun '14, 18:21</strong> </span></p></div></div><div id="comments-container-33876" class="comments-container"><span id="33877"></span><div id="comment-33877" class="comment"><div id="post-33877-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your reply! So is it like "wireshark" runs what is in the install location but "./wireshark" runs what is in the build directory?</p><p>In deed, I've got confused when I found the following in a wireshark README.plugins file "The bad news is that Wireshark will not use the plugins unless the plugins are installed in one of the places it expects them to find. One way of dealing with this problem is to set an environment variable when running Wireshark: WIRESHARK_RUN_FROM_BUILD_DIRECTORY=1. " why we should use that environmental variable if we are at the build directory already?!</p></div><div id="comment-33877-info" class="comment-info"><span class="comment-age">(16 Jun '14, 19:34)</span> <span class="comment-user userinfo">flora</span></div></div><span id="33878"></span><div id="comment-33878" class="comment"><div id="post-33878-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>So is it like "wireshark" runs what is in the install location but "./wireshark" runs what is in the build directory?</p></blockquote><p>"wireshark" runs whatever it first finds in your PATH; it might be in the current directory, if that's the first directory in PATH that contains a Wireshark binary (an empty entry in PATH means "the current directory"), or it might be in the install location, if that's the first directory in PATH that contains a Wireshark binary.</p><p>"./wireshark" runs whatever is in the <em>current</em> directory, which isn't guaranteed to be the build directory; if, for example, Wireshark is installed in "/usr/local/bin/wireshark", then, if you do "cd /usr/local/bin", and then do "./wireshark", it'll run what is in the current directory, i.e. it'll run "/usr/local/bin/wireshark".</p><blockquote><p>why we should use that environmental variable if we are at the build directory already?!</p></blockquote><p>Because Wireshark can't figure that out for itself, as it doesn't know what the build directory is.</p></div><div id="comment-33878-info" class="comment-info"><span class="comment-age">(16 Jun '14, 19:54)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="33895"></span><div id="comment-33895" class="comment"><div id="post-33895-score" class="comment-score"></div><div class="comment-text"><p>Thanks for correcting me. It is clear now.</p></div><div id="comment-33895-info" class="comment-info"><span class="comment-age">(17 Jun '14, 08:14)</span> <span class="comment-user userinfo">flora</span></div></div></div><div id="comment-tools-33876" class="comment-tools"></div><div class="clear"></div><div id="comment-33876-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

