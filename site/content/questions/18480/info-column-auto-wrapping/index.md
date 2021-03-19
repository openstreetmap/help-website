+++
type = "question"
title = "Info column auto-wrapping"
description = '''When I set the info column with either  col_set_str(); or col_append_fstr(); it doesn&#x27;t auto wrap the sentence onto the next line when the info column is full. Is there a function I can use to fix this or will I have to determine the length of the string and insert new line feeds where necessary??'''
date = "2013-02-10T15:23:00Z"
lastmod = "2014-05-15T19:53:00Z"
weight = 18480
keywords = [ "info", "column" ]
aliases = [ "/questions/18480" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Info column auto-wrapping](/questions/18480/info-column-auto-wrapping)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18480-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18480-score" class="post-score" title="current number of votes">1</div><span id="post-18480-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I set the info column with either col_set_str(); or col_append_fstr(); it doesn't auto wrap the sentence onto the next line when the info column is full. Is there a function I can use to fix this or will I have to determine the length of the string and insert new line feeds where necessary??</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-info" rel="tag" title="see questions tagged &#39;info&#39;">info</span> <span class="post-tag tag-link-column" rel="tag" title="see questions tagged &#39;column&#39;">column</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '13, 15:23</strong></p><img src="https://secure.gravatar.com/avatar/024c038a84faf77c618cfe43ee97ed64?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="StealthUE&#39;s gravatar image" /><p><span>StealthUE</span><br />
<span class="score" title="66 reputation points">66</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="StealthUE has one accepted answer">100%</span></p></div></div><div id="comments-container-18480" class="comments-container"></div><div id="comment-tools-18480" class="comment-tools"></div><div class="clear"></div><div id="comment-18480-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18482"></span>

<div id="answer-container-18482" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18482-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18482-score" class="post-score" title="current number of votes">2</div><span id="post-18482-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Currently, Wireshark does not set up the widget used to render columns in the packet list, the <a href="http://developer.gnome.org/gtk2/stable/GtkCellRendererText.html">GtkCellRendererText</a> widget, to do word-wrapping, so you would have to determine the length of the string and insert new lines where necessary.</p><p>Note that "where necessary" can't mean "where necessary to keep the string from filling up the info column", because that width is adjustable.</p><p>The GtkCellRendererText widget <em>can</em> do word-wrapping, <em>but</em> only does so if the <code>"wrap-width"</code> property is set, which sounds as if, in order to make wrapping happen, Wireshark would have to wire in a wrap width, and that wrap width that would take effect regardless of how wide the column actually is. It might be possible to have the code adjust the wrap width when the column is resized. That's not likely to happen in the near future, however.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '13, 18:28</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-18482" class="comments-container"><span id="32843"></span><div id="comment-32843" class="comment"><div id="post-32843-score" class="comment-score"></div><div class="comment-text"><p>Is the same true for the lines in the Packet Details pane?</p></div><div id="comment-32843-info" class="comment-info"><span class="comment-age">(15 May '14, 19:53)</span> <span class="comment-user userinfo">lid</span></div></div></div><div id="comment-tools-18482" class="comment-tools"></div><div class="clear"></div><div id="comment-18482-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

