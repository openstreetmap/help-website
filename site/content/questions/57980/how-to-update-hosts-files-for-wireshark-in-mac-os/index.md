+++
type = "question"
title = "How to update Hosts Files for Wireshark in Mac os"
description = '''I want to update hosts files for Wireshark in Mac OS , I mean I want to see the Nodes Name instead of IP address, I know how to do that in Microsoft Windows, I need to do the same for Mac OS. Appreciate if anyone reply and answer my question. Thanks'''
date = "2016-12-09T14:21:00Z"
lastmod = "2016-12-10T16:17:00Z"
weight = 57980
keywords = [ "macosx", "hosts" ]
aliases = [ "/questions/57980" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to update Hosts Files for Wireshark in Mac os](/questions/57980/how-to-update-hosts-files-for-wireshark-in-mac-os)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57980-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57980-score" class="post-score" title="current number of votes">0</div><span id="post-57980-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to update hosts files for Wireshark in Mac OS , I mean I want to see the Nodes Name instead of IP address, I know how to do that in Microsoft Windows, I need to do the same for Mac OS. Appreciate if anyone reply and answer my question. Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-macosx" rel="tag" title="see questions tagged &#39;macosx&#39;">macosx</span> <span class="post-tag tag-link-hosts" rel="tag" title="see questions tagged &#39;hosts&#39;">hosts</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Dec '16, 14:21</strong></p><img src="https://secure.gravatar.com/avatar/72c00bab5c18aee635f4af540c533b97?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ramin&#39;s gravatar image" /><p><span>Ramin</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ramin has no accepted answers">0%</span></p></div></div><div id="comments-container-57980" class="comments-container"></div><div id="comment-tools-57980" class="comment-tools"></div><div class="clear"></div><div id="comment-57980-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57996"></span>

<div id="answer-container-57996" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57996-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57996-score" class="post-score" title="current number of votes">1</div><span id="post-57996-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ramin has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark reads two hosts files - the one that's part of Wireshark's global data and your personal one.</p><p>In macOS, the Wireshark global hosts file is in the <code>Contents/Resources/share/wireshark</code> subdirectory of the app bundle, which is probably in <code>/Applications/Wireshark.app</code>, in which case the global hosts file would be <code>/Applications/Wireshark.app/Contents/Resources/share/wireshark/hosts</code>.</p><p>In UN*Xes such as macOS, your personal hosts file would, in newer versions of Wireshark, be in <code>~/.config/wireshark/hosts</code>. In older versions, and in newer versions if that directory doesn't exist but <code>~/.wireshark</code> exists, it would be in <code>~/.wireshark/hosts</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Dec '16, 16:17</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-57996" class="comments-container"></div><div id="comment-tools-57996" class="comment-tools"></div><div class="clear"></div><div id="comment-57996-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

