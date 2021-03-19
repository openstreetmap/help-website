+++
type = "question"
title = "Images In WireShark"
description = '''guys i captured an image in wireshark. But it is encrypted in the form like that. this is a piece of it how can i decrypt it ?&amp;gt;  .PNG . ... IHDR.............#.......gAMA......a.....sRGB.........PLTE..............F.7&quot;....../r...................................................G....../r...........6#...'''
date = "2014-05-19T10:17:00Z"
lastmod = "2014-05-19T11:32:00Z"
weight = 32908
keywords = [ "capture", "image" ]
aliases = [ "/questions/32908" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Images In WireShark](/questions/32908/images-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32908-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32908-score" class="post-score" title="current number of votes">0</div><span id="post-32908-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>guys i captured an image in wireshark. But it is encrypted in the form like that. this is a piece of it how can i decrypt it ?&gt; .PNG</p><p>. ... IHDR.............#.......gAMA......a.....sRGB.........PLTE..............F.7"....../r...................................................G....../r...........6#..H..F............/r....</p><p>111......%%%.6"..................<span class="__cf_email__" data-cfemail="d9f2f2f2f7f7f7f7f7f7aaaaadf7f7f7f7f79ee9a8f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f7f78a8a8a8e8e8ef7f7f7f7f7f7f7f7f7898989aeaeaef7f7f799">[email protected]</span>@@...........GJJJ...EEE...:::...............777.........]]]......ppp===...hhh.........MMM...mmm.7"...""" ccc(((............```...444.........0p...</p><p>..zyz..............D...BBB}}}'''eee....1..7#..F....0.jjjZZZ..B...{{{.6".. GGG.$..:.-f..{:..80o..t9.A ......../..&gt;.).....J"#.......%.d0...-h..,..[<em>..A....4!. J.m4.k./m.. .)a....:..#V..B.E......R'']..2!</em>..)]Q. .K..+..D._. .#U"P..?..G..7t....!..%...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-image" rel="tag" title="see questions tagged &#39;image&#39;">image</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 May '14, 10:17</strong></p><img src="https://secure.gravatar.com/avatar/2e7b21dd264180599cbe94b4c507c44f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vancer&#39;s gravatar image" /><p><span>vancer</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vancer has no accepted answers">0%</span></p></div></div><div id="comments-container-32908" class="comments-container"></div><div id="comment-tools-32908" class="comment-tools"></div><div class="clear"></div><div id="comment-32908-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32910"></span>

<div id="answer-container-32910" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32910-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32910-score" class="post-score" title="current number of votes">0</div><span id="post-32910-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What you have posted is the PNG file structure (at least parts of it). There is no need to <strong>decrypt</strong> that.</p><p>If you want to see the image itself, you should save/export it and then open it in any image viewer.</p><p>This works well for images in HTTP connections</p><blockquote><p>File -&gt; Export Objects -&gt; HTTP</p></blockquote><p>If the connection is encrypted (HTTPS), this will <strong>not work</strong>, unless you are able to decrypt it.</p><p>If the protocol is <strong>not HTTP</strong>, there is no <strong>easy</strong> way to export the image. If that is the case, please comment my answer and I'll let you know what to do.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '14, 11:32</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-32910" class="comments-container"></div><div id="comment-tools-32910" class="comment-tools"></div><div class="clear"></div><div id="comment-32910-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

