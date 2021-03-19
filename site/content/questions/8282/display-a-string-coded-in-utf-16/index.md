+++
type = "question"
title = "Display a string coded in UTF-16"
description = '''Hi. I am trying to patch a home made plugin. To summarize, a xml file describes message format and the plugin manages to decode the messages. I have some messages containing some string coded in UTF-8. It works fine. I just have to write in my xml that I have to decode a FT_STRING . Now, I have some...'''
date = "2012-01-09T01:34:00Z"
lastmod = "2012-01-09T22:39:00Z"
weight = 8282
keywords = [ "utf-16", "ft_string" ]
aliases = [ "/questions/8282" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Display a string coded in UTF-16](/questions/8282/display-a-string-coded-in-utf-16)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8282-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8282-score" class="post-score" title="current number of votes">0</div><span id="post-8282-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi.</p><p>I am trying to patch a home made plugin. To summarize, a xml file describes message format and the plugin manages to decode the messages.</p><p>I have some messages containing some string coded in UTF-8. It works fine. I just have to write in my xml that I have to decode a FT_STRING .</p><p>Now, I have some new messages that are coded in UTF-16 If I use a FT_STRING, it just prints the first character (stop at the first 000 encountered)</p><p>The plugin calls proto_tree_add_item. I dont't find any other type that FT_STRING that could support UTF-16 I am using 1.6.0rc2 I can use a more recent version if needed.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-utf-16" rel="tag" title="see questions tagged &#39;utf-16&#39;">utf-16</span> <span class="post-tag tag-link-ft_string" rel="tag" title="see questions tagged &#39;ft_string&#39;">ft_string</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jan '12, 01:34</strong></p><img src="https://secure.gravatar.com/avatar/bd299b3680beb7713576358a70120457?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="blinde&#39;s gravatar image" /><p><span>blinde</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="blinde has no accepted answers">0%</span></p></div></div><div id="comments-container-8282" class="comments-container"></div><div id="comment-tools-8282" class="comment-tools"></div><div class="clear"></div><div id="comment-8282-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8295"></span>

<div id="answer-container-8295" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8295-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8295-score" class="post-score" title="current number of votes">0</div><span id="post-8295-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As glib internaly uses UTF-8 encoding you will have to convert the string yourself tvb_get_unicode_string() or tvb_get_ephemeral_unicode_string() may be of help or use somting from http://developer.gnome.org/glib/stable/glib-Character-Set-Conversion.html Regards Anders</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jan '12, 22:39</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-8295" class="comments-container"></div><div id="comment-tools-8295" class="comment-tools"></div><div class="clear"></div><div id="comment-8295-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

