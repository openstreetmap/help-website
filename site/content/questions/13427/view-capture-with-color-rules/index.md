+++
type = "question"
title = "View Capture with Color Rules"
description = '''I saved a capture and sent it on the colleagues, they are able to view it with the color rules. When I view the same capture file it does not show with color rules. What setting am I missing?'''
date = "2012-08-07T08:12:00Z"
lastmod = "2012-08-07T08:43:00Z"
weight = 13427
keywords = [ "color-rules", "capture", "view" ]
aliases = [ "/questions/13427" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [View Capture with Color Rules](/questions/13427/view-capture-with-color-rules)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13427-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13427-score" class="post-score" title="current number of votes">0</div><span id="post-13427-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I saved a capture and sent it on the colleagues, they are able to view it with the color rules. When I view the same capture file it does not show with color rules. What setting am I missing?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-color-rules" rel="tag" title="see questions tagged &#39;color-rules&#39;">color-rules</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-view" rel="tag" title="see questions tagged &#39;view&#39;">view</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Aug '12, 08:12</strong></p><img src="https://secure.gravatar.com/avatar/676af8c3dff7ad09fc5324a294464b3e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mgwolf13&#39;s gravatar image" /><p><span>mgwolf13</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mgwolf13 has no accepted answers">0%</span></p></div></div><div id="comments-container-13427" class="comments-container"></div><div id="comment-tools-13427" class="comment-tools"></div><div class="clear"></div><div id="comment-13427-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13428"></span>

<div id="answer-container-13428" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-13428-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-13428-score" class="post-score" title="current number of votes">0</div><span id="post-13428-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Either you do not have color rules defined (you might have deleted them all) or your Wireshark is set to not colorize packets. You can toggle colorization in the toolbar with a button - if you hover over the buttons with a mouse you'll see a hint, and for the colorization button it says "colorize packet list" - it should be visibly pushed "down".</p><p>You can check your color rule set by using the button saying "edit color rules" or by choosing "View" -&gt; "Coloring Rules" in the menu. If your color rules are empty you can press the "Clear" button which does a funny thing... it doesn't clear anything (as the name would suggest) but restores the default rules (which I find pretty annoying, but that's just me...)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Aug '12, 08:24</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-13428" class="comments-container"><span id="13430"></span><div id="comment-13430" class="comment"><div id="post-13430-score" class="comment-score"></div><div class="comment-text"><p>Jasper thank you for the quick response. I applied both of these and not showing color in the view of the saved capture. If I view live the colorize packets appear.</p></div><div id="comment-13430-info" class="comment-info"><span class="comment-age">(07 Aug '12, 08:38)</span> <span class="comment-user userinfo">mgwolf13</span></div></div><span id="13431"></span><div id="comment-13431" class="comment"><div id="post-13431-score" class="comment-score"></div><div class="comment-text"><p>Then I guess your saved capture holds no packets that match any colorization rule. You can open the frame section in the decode pane to see if any rule was matched.</p><p>I would try to create a test color rule where I'm sure it matches a packet in the capture, and try loading the file again to see if it works. Or you could compare your color filter set to the one of your coworkers to see which ones they have and why they match.</p></div><div id="comment-13431-info" class="comment-info"><span class="comment-age">(07 Aug '12, 08:43)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-13428" class="comment-tools"></div><div class="clear"></div><div id="comment-13428-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

