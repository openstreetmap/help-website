+++
type = "question"
title = "GUI shows no text on OS X 10.8"
description = '''Hi, Last night I downloaded the latest Wireshark dmg for OSX and installed it. After launching wireshark, I found that all text in the GUI are not shown, the menu bars, menu items, dialogs, everything. Only icons are shown in the UI. I deleted all directions like .config, .gtk, .wireshark, rerun fc-...'''
date = "2013-10-18T09:44:00Z"
lastmod = "2013-10-18T10:40:00Z"
weight = 26176
keywords = [ "text", "gui" ]
aliases = [ "/questions/26176" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [GUI shows no text on OS X 10.8](/questions/26176/gui-shows-no-text-on-os-x-108)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26176-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26176-score" class="post-score" title="current number of votes">0</div><span id="post-26176-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Last night I downloaded the latest Wireshark dmg for OSX and installed it. After launching wireshark, I found that all text in the GUI are not shown, the menu bars, menu items, dialogs, everything. Only icons are shown in the UI. I deleted all directions like .config, .gtk<em>, .wireshark</em>, rerun fc-cache, and the problem still persist. Can anyone give me some hint on what might go wrong here? Thanks!</p><p>Jimmy</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-text" rel="tag" title="see questions tagged &#39;text&#39;">text</span> <span class="post-tag tag-link-gui" rel="tag" title="see questions tagged &#39;gui&#39;">gui</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '13, 09:44</strong></p><img src="https://secure.gravatar.com/avatar/5d6c08ff6fb17a635ecd0d2a59e08b24?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmzhou13&#39;s gravatar image" /><p><span>jmzhou13</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmzhou13 has no accepted answers">0%</span></p></div></div><div id="comments-container-26176" class="comments-container"></div><div id="comment-tools-26176" class="comment-tools"></div><div class="clear"></div><div id="comment-26176-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26178"></span>

<div id="answer-container-26178" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26178-score" class="post-score" title="current number of votes">0</div><span id="post-26178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Which version did you install? If you installed 1.10 or 1.8 can you try the 64-bit 1.11.0 installer instead?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Oct '13, 09:50</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-26178" class="comments-container"><span id="26188"></span><div id="comment-26188" class="comment"><div id="post-26188-score" class="comment-score"></div><div class="comment-text"><p>I had the 1.10 installed. I believe this problem is related to gtk because I ran gconf-editor and it had the same problem. But I have no clue what went wrong with gtk.</p><p>Just re-installed 1.11.0. The GUI has changed to native OS X, and all text are shown in the new GUI.</p><p>Thanks!</p></div><div id="comment-26188-info" class="comment-info"><span class="comment-age">(18 Oct '13, 10:29)</span> <span class="comment-user userinfo">jmzhou13</span></div></div><span id="26190"></span><div id="comment-26190" class="comment"><div id="post-26190-score" class="comment-score"></div><div class="comment-text"><p>Keep in mind that the new Qt-based UI in 1.11 is very much under development. Right now OS X users get to choose between a rock (an incomplete Qt UI) and a hard place (dealing with GTK+ issues). This should improve over time.</p></div><div id="comment-26190-info" class="comment-info"><span class="comment-age">(18 Oct '13, 10:40)</span> <span class="comment-user userinfo">Gerald Combs ♦♦</span></div></div></div><div id="comment-tools-26178" class="comment-tools"></div><div class="clear"></div><div id="comment-26178-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

