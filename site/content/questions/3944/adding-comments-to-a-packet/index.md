+++
type = "question"
title = "Adding Comments to a Packet"
description = '''Does Wireshark have a way to enter a comment on a specific packet for future reference? (e.g. Here is the start of the issue.)'''
date = "2011-05-05T08:17:00Z"
lastmod = "2012-01-06T02:13:00Z"
weight = 3944
keywords = [ "annotate", "pcapng", "comments" ]
aliases = [ "/questions/3944" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Adding Comments to a Packet](/questions/3944/adding-comments-to-a-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3944-score" class="post-score" title="current number of votes">0</div><span id="post-3944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Does Wireshark have a way to enter a comment on a specific packet for future reference? (e.g. Here is the start of the issue.)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-annotate" rel="tag" title="see questions tagged &#39;annotate&#39;">annotate</span> <span class="post-tag tag-link-pcapng" rel="tag" title="see questions tagged &#39;pcapng&#39;">pcapng</span> <span class="post-tag tag-link-comments" rel="tag" title="see questions tagged &#39;comments&#39;">comments</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 May '11, 08:17</strong></p><img src="https://secure.gravatar.com/avatar/9b63b6c21518055db59ce7f1f839985a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CarlT&#39;s gravatar image" /><p><span>CarlT</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CarlT has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 May '11, 08:39</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-3944" class="comments-container"></div><div id="comment-tools-3944" class="comment-tools"></div><div class="clear"></div><div id="comment-3944-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3947"></span>

<div id="answer-container-3947" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3947-score" class="post-score" title="current number of votes">1</div><span id="post-3947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The <a href="http://wiki.wireshark.org/Development/PcapNg">pcapng</a> file format supports this, but Wireshark itself does not yet have good support for it. A bug has been filed for it though, namely <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3096">bug 3096</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 May '11, 08:43</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-3947" class="comments-container"><span id="3948"></span><div id="comment-3948" class="comment"><div id="post-3948-score" class="comment-score"></div><div class="comment-text"><p>Awesome, glad it's already in the bug list. Thanks for the update and reference.</p></div><div id="comment-3948-info" class="comment-info"><span class="comment-age">(05 May '11, 08:47)</span> <span class="comment-user userinfo">CarlT</span></div></div><span id="8247"></span><div id="comment-8247" class="comment"><div id="post-8247-score" class="comment-score"></div><div class="comment-text"><p>A similar <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6229">bug 6229</a> has been fixed on wireshark 1.6.2 release related to reading and displaying comment option in wire shark.</p><p>I tried but not able to view the comment field from pcapng file using wireshark 1.6.3 release. Any idea ??</p></div><div id="comment-8247-info" class="comment-info"><span class="comment-age">(06 Jan '12, 01:35)</span> <span class="comment-user userinfo">ambika</span></div></div><span id="8249"></span><div id="comment-8249" class="comment"><div id="post-8249-score" class="comment-score"></div><div class="comment-text"><p>Bug 6229 is <em>NOT</em> a similar bug; that bug is <em>not</em> that the comment can't be read, it's that Wireshark mishandled the comment in a way that meant that it didn't properly return the <em>packet data</em> for a frame with comments, meaning Wireshark wouldn't even properly show the packet data.</p><p>The only way you're going to be able to view the comment field is to wait for bug 3096 to be fixed and then use a version of Wireshark with that fix.</p></div><div id="comment-8249-info" class="comment-info"><span class="comment-age">(06 Jan '12, 02:13)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-3947" class="comment-tools"></div><div class="clear"></div><div id="comment-3947-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

