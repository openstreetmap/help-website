+++
type = "question"
title = "&quot;Duplicate protocol name&quot; errors on Wireshark on OS X"
description = '''i am also not able to run wireshark, after i installed the x11 update. I gor error messages on the command line: (wireshark-bin:8895): Gtk-WARNING **: Unable to locate theme engine in module_path: &quot;clearlooks&quot;, 23:33:23 Err Duplicate protocol name &quot;Coseventcomm Dissector Using GIOP API&quot;! This might ...'''
date = "2012-12-22T14:52:00Z"
lastmod = "2012-12-22T16:25:00Z"
weight = 17179
keywords = [ "duplicate", "protocol", "name" ]
aliases = [ "/questions/17179" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# ["Duplicate protocol name" errors on Wireshark on OS X](/questions/17179/duplicate-protocol-name-errors-on-wireshark-on-os-x)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17179-score" class="post-score" title="current number of votes">0</div><span id="post-17179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i am also not able to run wireshark, after i installed the x11 update. I gor error messages on the command line:</p><pre><code>(wireshark-bin:8895): Gtk-WARNING **: Unable to locate theme engine in module_path: &quot;clearlooks&quot;,
23:33:23          Err  Duplicate protocol name &quot;Coseventcomm Dissector Using GIOP API&quot;! This might be caused by an inappropriate plugin or a development error.
Peers-iMac-4:asl peer$ pwd</code></pre><p>Maybe a development error?????</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-duplicate" rel="tag" title="see questions tagged &#39;duplicate&#39;">duplicate</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Dec '12, 14:52</strong></p><img src="https://secure.gravatar.com/avatar/6006be721841c4734d547d001583f1f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="peer60&#39;s gravatar image" /><p><span>peer60</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="peer60 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>22 Dec '12, 16:17</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-17179" class="comments-container"></div><div id="comment-tools-17179" class="comment-tools"></div><div class="clear"></div><div id="comment-17179-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="17184"></span>

<div id="answer-container-17184" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17184-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17184-score" class="post-score" title="current number of votes">1</div><span id="post-17184-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=7401">bug 7401</a>. The built-in coseventcomm dissector, and a plugin left over from an old installation (from an older version of Wireshark, where that dissector was a plugin), are both trying to register dissectors for the same protocol. Try entirely removing Wireshark and re-installing it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Dec '12, 16:25</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Dec '12, 16:28</strong> </span></p></div></div><div id="comments-container-17184" class="comments-container"></div><div id="comment-tools-17184" class="comment-tools"></div><div class="clear"></div><div id="comment-17184-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

