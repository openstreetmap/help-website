+++
type = "question"
title = "[Lua] Custom Text Window Sizes?"
description = '''Is there support for the customization of TextWindow sizes so that when the window is opened, it opens to a specific size? This is really just out of curiosity. Any and all comments are appreciated! Wireshark Version 1.10.8 Windows 7 Thanks, Jeffrey'''
date = "2014-06-27T14:11:00Z"
lastmod = "2014-06-29T11:24:00Z"
weight = 34251
keywords = [ "lua", "window", "api", "gui", "wireshark" ]
aliases = [ "/questions/34251" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [\[Lua\] Custom Text Window Sizes?](/questions/34251/lua-custom-text-window-sizes)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34251-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34251-score" class="post-score" title="current number of votes">0</div><span id="post-34251-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there support for the customization of TextWindow sizes so that when the window is opened, it opens to a specific size? This is really just out of curiosity. Any and all comments are appreciated!</p><p>Wireshark Version 1.10.8 Windows 7</p><p>Thanks, Jeffrey</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-window" rel="tag" title="see questions tagged &#39;window&#39;">window</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-gui" rel="tag" title="see questions tagged &#39;gui&#39;">gui</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jun '14, 14:11</strong></p><img src="https://secure.gravatar.com/avatar/e66163b53ebae2cb35d621d806073ea2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jphmiller&#39;s gravatar image" /><p><span>jphmiller</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jphmiller has no accepted answers">0%</span></p></div></div><div id="comments-container-34251" class="comments-container"></div><div id="comment-tools-34251" class="comment-tools"></div><div class="clear"></div><div id="comment-34251-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34265"></span>

<div id="answer-container-34265" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34265-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34265-score" class="post-score" title="current number of votes">0</div><span id="post-34265-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jphmiller has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Nope, only what's in the <a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Gui.html#lua_class_TextWindow">API docs for TextWindow</a>, and it's currently fixed to creating a new window of 400 x 300 pixels. An additional pair of arguments for <code>TextWindow.new()</code> could be easily added to control it, but the current GTK-based GUI is being phased out with a Qt one replacing it, and that might not end up having the same API exactly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jun '14, 22:39</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-34265" class="comments-container"><span id="34270"></span><div id="comment-34270" class="comment"><div id="post-34270-score" class="comment-score"></div><div class="comment-text"><p>Thanks! I'm interested to see what the Qt GUI will be capable of when it is implemented.</p></div><div id="comment-34270-info" class="comment-info"><span class="comment-age">(29 Jun '14, 10:48)</span> <span class="comment-user userinfo">jphmiller</span></div></div><span id="34271"></span><div id="comment-34271" class="comment"><div id="post-34271-score" class="comment-score"></div><div class="comment-text"><p>The Windows 1.12 versions include the Qt version, currently this is in rc, but the release should be out soon.</p></div><div id="comment-34271-info" class="comment-info"><span class="comment-age">(29 Jun '14, 11:24)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-34265" class="comment-tools"></div><div class="clear"></div><div id="comment-34265-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

