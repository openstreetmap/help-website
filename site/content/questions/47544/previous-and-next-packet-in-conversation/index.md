+++
type = "question"
title = "Previous and Next Packet in conversation"
description = '''In WireShark 2.0 the previous and next packet buttons are missing under the Go Button.'''
date = "2015-11-12T08:14:00Z"
lastmod = "2015-11-13T12:59:00Z"
weight = 47544
keywords = [ "button" ]
aliases = [ "/questions/47544" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Previous and Next Packet in conversation](/questions/47544/previous-and-next-packet-in-conversation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47544-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47544-score" class="post-score" title="current number of votes">0</div><span id="post-47544-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In WireShark 2.0 the previous and next packet buttons are missing under the Go Button.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-button" rel="tag" title="see questions tagged &#39;button&#39;">button</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Nov '15, 08:14</strong></p><img src="https://secure.gravatar.com/avatar/328e4e3c363565d7a50d22167dd1a5b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="philvilla&#39;s gravatar image" /><p><span>philvilla</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="philvilla has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Nov '15, 08:37</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-47544" class="comments-container"></div><div id="comment-tools-47544" class="comment-tools"></div><div class="clear"></div><div id="comment-47544-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="47545"></span>

<div id="answer-container-47545" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47545-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47545-score" class="post-score" title="current number of votes">0</div><span id="post-47545-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What is your exact version (from the Help -&gt; About Wireshark dialog)? Are you using the Qt or GTK version (Legacy)? What is your OS?</p><p>I have Previous and Next buttons on the toolbar next to the "Go to specified packet" button on Windows on a locally built copy from master.</p><p><strong>Update</strong></p><p>I now think I see what you mean, you're missing the "Previous Packet In Conversation" and "Next Packet In Conversation" options under the "Go" menu.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '15, 08:41</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Nov '15, 08:46</strong> </span></p></div></div><div id="comments-container-47545" class="comments-container"><span id="47547"></span><div id="comment-47547" class="comment"><div id="post-47547-score" class="comment-score"></div><div class="comment-text"><p>There's now a <a href="https://code.wireshark.org/review/#/c/11771/">change</a> pending for this.</p></div><div id="comment-47547-info" class="comment-info"><span class="comment-age">(12 Nov '15, 09:57)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="47556"></span><div id="comment-47556" class="comment"><div id="post-47556-score" class="comment-score"></div><div class="comment-text"><p>The buttons don't exist in the new beta version 2.0.</p></div><div id="comment-47556-info" class="comment-info"><span class="comment-age">(12 Nov '15, 17:46)</span> <span class="comment-user userinfo">philvilla</span></div></div><span id="47569"></span><div id="comment-47569" class="comment"><div id="post-47569-score" class="comment-score"></div><div class="comment-text"><p>You keep referring to them as buttons, do you mean menu items? If the latter then they'll be in the next build as the change mentioned above has now been merged to master and another <a href="https://code.wireshark.org/review/#/c/11800/">change</a> is pending to backport to 2.0 for the next build.</p><p>If you do mean buttons, to which buttons are you referring?</p></div><div id="comment-47569-info" class="comment-info"><span class="comment-age">(13 Nov '15, 03:36)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="47582"></span><div id="comment-47582" class="comment"><div id="post-47582-score" class="comment-score"></div><div class="comment-text"><p>Yes that is what I mean Thanks</p></div><div id="comment-47582-info" class="comment-info"><span class="comment-age">(13 Nov '15, 12:59)</span> <span class="comment-user userinfo">philvilla</span></div></div></div><div id="comment-tools-47545" class="comment-tools"></div><div class="clear"></div><div id="comment-47545-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

