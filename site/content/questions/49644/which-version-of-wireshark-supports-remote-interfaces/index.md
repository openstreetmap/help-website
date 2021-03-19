+++
type = "question"
title = "Which version of Wireshark supports Remote Interfaces."
description = '''Hi... My version of Wireshark does not support analysis of Remote Interfaces. (Ver 2.0.1 running on Apple iMac OSX Yosemite 10.10.5).  Does anyone know which version of WireShark does...and how I get hold of it? Many thanks,  Dave.'''
date = "2016-01-30T04:48:00Z"
lastmod = "2016-01-31T01:18:00Z"
weight = 49644
keywords = [ "capture", "remote" ]
aliases = [ "/questions/49644" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Which version of Wireshark supports Remote Interfaces.](/questions/49644/which-version-of-wireshark-supports-remote-interfaces)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49644-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49644-score" class="post-score" title="current number of votes">0</div><span id="post-49644-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi...</p><p>My version of Wireshark does not support analysis of Remote Interfaces. (Ver 2.0.1 running on Apple iMac OSX Yosemite 10.10.5).</p><p>Does anyone know which version of WireShark does...and how I get hold of it?</p><p>Many thanks,</p><p>Dave.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-remote" rel="tag" title="see questions tagged &#39;remote&#39;">remote</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jan '16, 04:48</strong></p><img src="https://secure.gravatar.com/avatar/f5086cdaa59a07733697c8e2e8ef7e4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CDD_Dave&#39;s gravatar image" /><p><span>CDD_Dave</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CDD_Dave has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Jan '16, 05:43</strong> </span></p></div></div><div id="comments-container-49644" class="comments-container"></div><div id="comment-tools-49644" class="comment-tools"></div><div class="clear"></div><div id="comment-49644-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49645"></span>

<div id="answer-container-49645" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49645-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49645-score" class="post-score" title="current number of votes">1</div><span id="post-49645-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>which version of WireShark does</p></blockquote><p>The version that's built with a version of libpcap/WinPcap that supports remote interfaces and that's running with a version of libpcap/WinPcap that supports remote interfaces.</p><blockquote><p>and how I get hold of it?</p></blockquote><p>Either 1) run Windows (BootCamp or a virtual machine monitor such as VMware Fusion, Parallels Workstations, or VirtualBox) and run the Windows version or 2) add the support to libpcap yourself, compile libpcap, and then compile Wireshark with that version of libpcap.</p><p>(No, there's no easy way. At some point in the future there may be a standard libpcap release with remote capture support, and at some point after that Apple may pick up that release, and at some point the OS X version of Wireshark may be modified to use those capabilities if present.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '16, 14:26</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-49645" class="comments-container"><span id="49656"></span><div id="comment-49656" class="comment"><div id="post-49656-score" class="comment-score"></div><div class="comment-text"><p>Guy...</p><p>Many thanks.</p><p>Excellent guidance!</p><p>Dave.</p></div><div id="comment-49656-info" class="comment-info"><span class="comment-age">(31 Jan '16, 01:18)</span> <span class="comment-user userinfo">CDD_Dave</span></div></div></div><div id="comment-tools-49645" class="comment-tools"></div><div class="clear"></div><div id="comment-49645-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

