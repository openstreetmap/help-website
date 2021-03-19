+++
type = "question"
title = "Remote Capture OSX"
description = '''Will there be support for remote capture for OSX? I tried doing this and there is a note in the window that says this feature is not supported in this version? We were able to use remote capture on a Windows box. '''
date = "2016-01-07T05:30:00Z"
lastmod = "2016-01-07T17:35:00Z"
weight = 48942
keywords = [ "osx", "remote-capture" ]
aliases = [ "/questions/48942" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Remote Capture OSX](/questions/48942/remote-capture-osx)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48942-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48942-score" class="post-score" title="current number of votes">0</div><span id="post-48942-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Will there be support for remote capture for OSX? I tried doing this and there is a note in the window that says this feature is not supported in this version? We were able to use remote capture on a Windows box.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span> <span class="post-tag tag-link-remote-capture" rel="tag" title="see questions tagged &#39;remote-capture&#39;">remote-capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jan '16, 05:30</strong></p><img src="https://secure.gravatar.com/avatar/ec23e36c7f18755e9b48372a15b5c382?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JDaniel&#39;s gravatar image" /><p><span>JDaniel</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JDaniel has no accepted answers">0%</span></p></div></div><div id="comments-container-48942" class="comments-container"></div><div id="comment-tools-48942" class="comment-tools"></div><div class="clear"></div><div id="comment-48942-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48961"></span>

<div id="answer-container-48961" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48961-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48961-score" class="post-score" title="current number of votes">0</div><span id="post-48961-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Will there be support for remote capture for OS X?</p></blockquote><p>If libpcap adds support for it in a future release (it's in progress, but I can't say when it'll be ready) and if either</p><ol><li><p>Apple picks up that version of libpcap (getting them to do so probably also means adding a bunch of other capabilities to libpcap, which are also on my to-do list - along with a ton of other things);</p></li><li><p>the official Wireshark release switches to using a version of libpcap built from that future release;</p></li></ol><p>then there will be support for remote capture.</p><p>(The libpcap programming interface will probably be different from the one WinPcap currently has, so it'll also involve Wireshark changes; the good news is that it might also add support for other forms of remote capture.)</p><p>That version of libpcap, if adopted by a particular OS (some Linux distribution, some version of *BSD, Solaris, etc.) would allow Wireshark, if built to use that version's capabilities, to do remote capture on that OS.</p><p>Of course, that would require that the remote machine be running the remote capture daemon, just as the Windows version requires that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jan '16, 17:35</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Jan '16, 17:36</strong> </span></p></div></div><div id="comments-container-48961" class="comments-container"></div><div id="comment-tools-48961" class="comment-tools"></div><div class="clear"></div><div id="comment-48961-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

