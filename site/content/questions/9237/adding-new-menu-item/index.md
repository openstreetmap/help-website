+++
type = "question"
title = "adding new menu item"
description = '''i&#x27;m trying to edit the GUI of wireshark to add new menu items to existing menu bar...but the code is huge and i dont know what files it is dependent on ..please kndly help me with which files to be edited sangmeshcp@gmail.com'''
date = "2012-02-27T02:22:00Z"
lastmod = "2012-02-27T08:43:00Z"
weight = 9237
keywords = [ "menu" ]
aliases = [ "/questions/9237" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [adding new menu item](/questions/9237/adding-new-menu-item)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9237-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9237-score" class="post-score" title="current number of votes">0</div><span id="post-9237-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i'm trying to edit the GUI of wireshark to add new menu items to existing menu bar...but the code is huge and i dont know what files it is dependent on ..please kndly help me with which files to be edited</p><p><span class="__cf_email__" data-cfemail="aeddcfc0c9c3cbddc6cddeee">[email protected]</span><a href="http://gmail.com">gmail.com</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-menu" rel="tag" title="see questions tagged &#39;menu&#39;">menu</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Feb '12, 02:22</strong></p><img src="https://secure.gravatar.com/avatar/6cb6685f12bd537f0f2e1e86a591e940?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sangmeshp&#39;s gravatar image" /><p><span>sangmeshp</span><br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sangmeshp has no accepted answers">0%</span></p></div></div><div id="comments-container-9237" class="comments-container"></div><div id="comment-tools-9237" class="comment-tools"></div><div class="clear"></div><div id="comment-9237-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9242"></span>

<div id="answer-container-9242" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9242-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9242-score" class="post-score" title="current number of votes">1</div><span id="post-9242-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It very much depends on which branch you're working with.</p><ul><li>for 1.4, look in gtk/menu.c</li><li>for 1.6, look in gtk/menu.c, note there's a lot of UI_MANAGER stuff in there.</li><li>for trunk, look ui/gtk/ui/main-menubar-ui.xml (assuming you want your changes in the GTK+ interface)</li></ul><p>There are other ways to add menus, like registering a statistics menu item.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Feb '12, 04:16</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-9242" class="comments-container"><span id="9251"></span><div id="comment-9251" class="comment"><div id="post-9251-score" class="comment-score">1</div><div class="comment-text"><p>ui/gtk/ui/main-menubar-ui.xml isn't used you have to edit main_menubar.c or use the tap interface to add a custom menu.</p></div><div id="comment-9251-info" class="comment-info"><span class="comment-age">(27 Feb '12, 08:43)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-9242" class="comment-tools"></div><div class="clear"></div><div id="comment-9242-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

