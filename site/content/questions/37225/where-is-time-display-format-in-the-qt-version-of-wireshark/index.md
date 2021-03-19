+++
type = "question"
title = "Where is time display format in the Qt version of Wireshark?"
description = '''On Windows and Linux, the view menu is extensive and you can choose from different time display formats. (as described in the manual, https://www.wireshark.org/docs/wsug_html/#ChWorkTimeFormatsSection) How do I do this on Wireshark for OS X? I have version 1.99.1-248-ga2508bd and my view menu looks ...'''
date = "2014-10-21T03:58:00Z"
lastmod = "2014-10-21T05:25:00Z"
weight = 37225
keywords = [ "qt", "time" ]
aliases = [ "/questions/37225" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Where is time display format in the Qt version of Wireshark?](/questions/37225/where-is-time-display-format-in-the-qt-version-of-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37225-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37225-score" class="post-score" title="current number of votes">0</div><span id="post-37225-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>On Windows and Linux, the view menu is extensive and you can choose from different time display formats.</p><p>(as described in the manual, <a href="https://www.wireshark.org/docs/wsug_html/#ChWorkTimeFormatsSection)">https://www.wireshark.org/docs/wsug_html/#ChWorkTimeFormatsSection)</a></p><p>How do I do this on Wireshark for OS X? I have version 1.99.1-248-ga2508bd and my view menu looks like this:</p><p><a href="https://www.dropbox.com/s/259p0ajk1mnhztc/Screenshot%202014-10-21%2012.57.10.png">https://www.dropbox.com/s/259p0ajk1mnhztc/Screenshot%202014-10-21%2012.57.10.png</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-qt" rel="tag" title="see questions tagged &#39;qt&#39;">qt</span> <span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '14, 03:58</strong></p><img src="https://secure.gravatar.com/avatar/60a6e028c2b288b38e133662af95eb88?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Konstigt&#39;s gravatar image" /><p><span>Konstigt</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Konstigt has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Oct '14, 11:04</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-37225" class="comments-container"></div><div id="comment-tools-37225" class="comment-tools"></div><div class="clear"></div><div id="comment-37225-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37228"></span>

<div id="answer-container-37228" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37228-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37228-score" class="post-score" title="current number of votes">2</div><span id="post-37228-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The QT version is still a work in progress and so may not have all the functionality of the older versions yet.</p><p>Edit: Any of the <a href="https://www.wireshark.org/download/automated/osx/">automated builds</a> 1.99.1-271 or later should now have a the View | Time Display Format options enabled thanks to <span>@Gerald Combs</span>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '14, 04:15</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Oct '14, 02:24</strong> </span></p></div></div><div id="comments-container-37228" class="comments-container"><span id="37232"></span><div id="comment-37232" class="comment"><div id="post-37232-score" class="comment-score"></div><div class="comment-text"><p>See also <a href="https://ask.wireshark.org/questions/35664/wireshark-qt-unable-to-change-timestamp-presentation-format">this question</a>. If you don't mind running X you could simply switch back to the Gtk-based GUI.</p></div><div id="comment-37232-info" class="comment-info"><span class="comment-age">(21 Oct '14, 05:25)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-37228" class="comment-tools"></div><div class="clear"></div><div id="comment-37228-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

