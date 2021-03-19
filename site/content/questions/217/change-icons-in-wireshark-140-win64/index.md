+++
type = "question"
title = "Change icons in Wireshark 1.4.0 Win64?"
description = '''I have Wireshark 1.4.0 running on Vista Home Premium x64. On my screen, the Wireshark toolbar icons are rather hard to read. I tried going through all of the DLLs and EXEs with a (64-bit) resource editor and found no picture data to speak of. Is there a way to modify the toolbar icon set in Wireshar...'''
date = "2010-09-19T12:58:00Z"
lastmod = "2010-09-19T14:07:00Z"
weight = 217
keywords = [ "icons", "modify", "64-bit", "resources", "icon" ]
aliases = [ "/questions/217" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Change icons in Wireshark 1.4.0 Win64?](/questions/217/change-icons-in-wireshark-140-win64)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-217-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-217-score" class="post-score" title="current number of votes">0</div><span id="post-217-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have Wireshark 1.4.0 running on Vista Home Premium x64. On my screen, the Wireshark toolbar icons are rather hard to read. I tried going through all of the DLLs and EXEs with a (64-bit) resource editor and found no picture data to speak of. Is there a way to modify the toolbar icon set in Wireshark?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-icons" rel="tag" title="see questions tagged &#39;icons&#39;">icons</span> <span class="post-tag tag-link-modify" rel="tag" title="see questions tagged &#39;modify&#39;">modify</span> <span class="post-tag tag-link-64-bit" rel="tag" title="see questions tagged &#39;64-bit&#39;">64-bit</span> <span class="post-tag tag-link-resources" rel="tag" title="see questions tagged &#39;resources&#39;">resources</span> <span class="post-tag tag-link-icon" rel="tag" title="see questions tagged &#39;icon&#39;">icon</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Sep '10, 12:58</strong></p><img src="https://secure.gravatar.com/avatar/c04f2b4fb0d88dc25e89378b9b0542b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hmmwhatsthisdo&#39;s gravatar image" /><p><span>hmmwhatsthisdo</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hmmwhatsthisdo has no accepted answers">0%</span></p></div></div><div id="comments-container-217" class="comments-container"></div><div id="comment-tools-217" class="comment-tools"></div><div class="clear"></div><div id="comment-217-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="218"></span>

<div id="answer-container-218" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-218-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-218-score" class="post-score" title="current number of votes">0</div><span id="post-218-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Go to this file: C:\Program Files\Wireshark\share\themes\Default\gtk-2.0\gtkrc</p><p>and change</p><p>gtk-toolbar-icon-size = small-toolbar</p><p>into</p><p>gtk-toolbar-icon-size = large-toolbar</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Sep '10, 14:02</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Sep '10, 14:06</strong> </span></p></div></div><div id="comments-container-218" class="comments-container"><span id="220"></span><div id="comment-220" class="comment"><div id="post-220-score" class="comment-score"></div><div class="comment-text"><p>Yes, but that only changes the icon's SIZES, not the actual icons themselves. Besides, I don't really care for the way they look. They cramp mah style, ya'know.</p></div><div id="comment-220-info" class="comment-info"><span class="comment-age">(19 Sep '10, 14:07)</span> <span class="comment-user userinfo">hmmwhatsthisdo</span></div></div></div><div id="comment-tools-218" class="comment-tools"></div><div class="clear"></div><div id="comment-218-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

