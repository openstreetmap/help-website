+++
type = "question"
title = "Cannot see Interface in preferences"
description = '''I just installed wireshark on my Linux Mint 10 workstation and when I select interfaces I do not see anything there. There are no options.'''
date = "2011-07-27T16:55:00Z"
lastmod = "2011-07-27T18:05:00Z"
weight = 5331
keywords = [ "interface" ]
aliases = [ "/questions/5331" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot see Interface in preferences](/questions/5331/cannot-see-interface-in-preferences)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5331-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5331-score" class="post-score" title="current number of votes">0</div><span id="post-5331-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just installed wireshark on my Linux Mint 10 workstation and when I select interfaces I do not see anything there. There are no options.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-interface" rel="tag" title="see questions tagged &#39;interface&#39;">interface</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '11, 16:55</strong></p><img src="https://secure.gravatar.com/avatar/2ab4b6b00f26ecca3f03c5850e6df29d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="socratease&#39;s gravatar image" /><p><span>socratease</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="socratease has no accepted answers">0%</span></p></div></div><div id="comments-container-5331" class="comments-container"></div><div id="comment-tools-5331" class="comment-tools"></div><div class="clear"></div><div id="comment-5331-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5333"></span>

<div id="answer-container-5333" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5333-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5333-score" class="post-score" title="current number of votes">2</div><span id="post-5333-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>See the Wireshark Wiki:</p><p><a href="http://wiki.wireshark.org/CaptureSetup">Capture Setup</a> and</p><p><a href="http://wiki.wireshark.org/CaptureSetup/CapturePrivileges">Capture Setup/Capture Privileges</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '11, 18:05</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Jul '11, 18:12</strong> </span></p></div></div><div id="comments-container-5333" class="comments-container"></div><div id="comment-tools-5333" class="comment-tools"></div><div class="clear"></div><div id="comment-5333-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5332"></span>

<div id="answer-container-5332" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5332-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5332-score" class="post-score" title="current number of votes">0</div><span id="post-5332-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Use sudo wireshark to start wireshark from your terminal box. If you can then see your interfaces then it's a security related issue within linux and you'll need to read up on what to change to run it normally. It's not advisable to run wireshark all the time with the sudo command because it gives it superuser privileges.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '11, 17:58</strong></p><img src="https://secure.gravatar.com/avatar/1f3966b6e9de3a63326e2d3fd51c8c04?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John_Modlin&#39;s gravatar image" /><p><span>John_Modlin</span><br />
<span class="score" title="120 reputation points">120</span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John_Modlin has no accepted answers">0%</span></p></div></div><div id="comments-container-5332" class="comments-container"></div><div id="comment-tools-5332" class="comment-tools"></div><div class="clear"></div><div id="comment-5332-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

