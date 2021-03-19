+++
type = "question"
title = "Different .so dependencies between normal build and RPM"
description = '''With 1.10.x, I&#x27;m able to build the two RPMs, but when installing, there&#x27;s a dependency for libwiretap.so.2 and libwsutil.so.2, even though the build directory contains only the .so.3 varieties. The RPM won&#x27;t install without these. If I force the install and do an &quot;ldd wireshark&quot; on the executable, i...'''
date = "2014-01-22T12:05:00Z"
lastmod = "2014-01-22T12:17:00Z"
weight = 29106
keywords = [ "rpm", "redhat" ]
aliases = [ "/questions/29106" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Different .so dependencies between normal build and RPM](/questions/29106/different-so-dependencies-between-normal-build-and-rpm)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29106-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29106-score" class="post-score" title="current number of votes">0</div><span id="post-29106-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>With 1.10.x, I'm able to build the two RPMs, but when installing, there's a dependency for libwiretap.so.2 and libwsutil.so.2, even though the build directory contains only the .so.3 varieties. The RPM won't install without these. If I force the install and do an "ldd wireshark" on the executable, it claims to need <strong>both the .so.3 and the .so.2 varieties</strong></p><p>When I do a "make install" and run an ldd on the /usr/local/bin/wireshark executable, it only has a requirement for the .so.3 varieties.</p><p>I do not know enough about the build process to know what is informing the RPM build that wireshark needs the .so.2's. Perhaps there's the Makefiles in the packaging/rpm directory are not sync'd with the toplevel Makefile's more recent changes?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rpm" rel="tag" title="see questions tagged &#39;rpm&#39;">rpm</span> <span class="post-tag tag-link-redhat" rel="tag" title="see questions tagged &#39;redhat&#39;">redhat</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '14, 12:05</strong></p><img src="https://secure.gravatar.com/avatar/34ab7b09251ce1194b33bb66c2b32d17?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jorwex&#39;s gravatar image" /><p><span>jorwex</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jorwex has no accepted answers">0%</span></p></div></div><div id="comments-container-29106" class="comments-container"></div><div id="comment-tools-29106" class="comment-tools"></div><div class="clear"></div><div id="comment-29106-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29110"></span>

<div id="answer-container-29110" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29110-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29110-score" class="post-score" title="current number of votes">0</div><span id="post-29110-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Answered in <a href="http://ask.wireshark.org/questions/29102/single-rpm-instead-of-wireshark-wireshark-gnome">http://ask.wireshark.org/questions/29102/single-rpm-instead-of-wireshark-wireshark-gnome</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '14, 12:17</strong></p><img src="https://secure.gravatar.com/avatar/34ab7b09251ce1194b33bb66c2b32d17?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jorwex&#39;s gravatar image" /><p><span>jorwex</span><br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jorwex has no accepted answers">0%</span></p></div></div><div id="comments-container-29110" class="comments-container"></div><div id="comment-tools-29110" class="comment-tools"></div><div class="clear"></div><div id="comment-29110-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

