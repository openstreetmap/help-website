+++
type = "question"
title = "Lua: Link in Tap output that can apply display filter to main window"
description = '''Hi folks, I have written a tap in Lua that opens a TextWindow and displays a breakdown of all TCP conversations, along with some performance metrics for each. I would like to include in the output a link for each conversation, that would apply a filter in the main window to display packets from that...'''
date = "2016-11-03T13:03:00Z"
lastmod = "2017-03-08T06:39:00Z"
weight = 56951
keywords = [ "link", "lua", "tap", "filter", "display_filter" ]
aliases = [ "/questions/56951" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lua: Link in Tap output that can apply display filter to main window](/questions/56951/lua-link-in-tap-output-that-can-apply-display-filter-to-main-window)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56951-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56951-score" class="post-score" title="current number of votes">0</div><span id="post-56951-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi folks,</p><p>I have written a tap in Lua that opens a TextWindow and displays a breakdown of all TCP conversations, along with some performance metrics for each. I would like to include in the output a link for each conversation, that would apply a filter in the main window to display packets from that conversation only. This way a user can click on a link for a conversation they want to drill down into.</p><p>I have been able to generate the filter without a problem, but right now the user has to copy and paste it. I can find no way to create a link in the Tap's TextWindow that can dynamically apply the filter.</p><p>Is there some way to do this I am not aware of? If it is not possible from within a TextWindow, is there another way I can display output from a tap where I can include such a link to apply a display filter?</p><p>Thanks in advance, Ryan</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-link" rel="tag" title="see questions tagged &#39;link&#39;">link</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-tap" rel="tag" title="see questions tagged &#39;tap&#39;">tap</span> <span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-display_filter" rel="tag" title="see questions tagged &#39;display_filter&#39;">display_filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Nov '16, 13:03</strong></p><img src="https://secure.gravatar.com/avatar/ba1199f4d360c53a6cc8aa6aa5da37c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ryber&#39;s gravatar image" /><p><span>ryber</span><br />
<span class="score" title="146 reputation points">146</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ryber has one accepted answer">16%</span></p></div></div><div id="comments-container-56951" class="comments-container"><span id="59325"></span><div id="comment-59325" class="comment"><div id="post-59325-score" class="comment-score"></div><div class="comment-text"><p>I've got the same question. Have you found something ?</p></div><div id="comment-59325-info" class="comment-info"><span class="comment-age">(10 Feb '17, 06:28)</span> <span class="comment-user userinfo">Schafer</span></div></div><span id="59925"></span><div id="comment-59925" class="comment"><div id="post-59925-score" class="comment-score"></div><div class="comment-text"><p>Hi <span>@Schafer</span>, sorry for the delayed response. I never did find a way to do this, and am assuming there is not one. I settled for just displaying the filter expression in the window and requiring the user to copy and paste it. It's easy, but makes the output a lot busier and harder to read.</p><p>If you find a better solution, please let me know.</p></div><div id="comment-59925-info" class="comment-info"><span class="comment-age">(08 Mar '17, 06:39)</span> <span class="comment-user userinfo">ryber</span></div></div></div><div id="comment-tools-56951" class="comment-tools"></div><div class="clear"></div><div id="comment-56951-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

