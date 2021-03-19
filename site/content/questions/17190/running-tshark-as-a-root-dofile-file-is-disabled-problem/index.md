+++
type = "question"
title = "Running tshark as a root, dofile file is disabled problem"
description = '''Whenever i try to analyze packets using tshark on Ubuntu with root permission i got the following error, however when i switch to user profile (su berkey), there is no problem. Why this occurs? is there a solution?  tshark: Lua: Error during loading:  [string &quot;/usr/share/wireshark/init.lua&quot;]:45: dof...'''
date = "2012-12-23T03:53:00Z"
lastmod = "2014-12-07T11:48:00Z"
weight = 17190
keywords = [ "lua", "tshark" ]
aliases = [ "/questions/17190" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [Running tshark as a root, dofile file is disabled problem](/questions/17190/running-tshark-as-a-root-dofile-file-is-disabled-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17190-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17190-score" class="post-score" title="current number of votes">1</div><span id="post-17190-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Whenever i try to analyze packets using tshark on Ubuntu with root permission i got the following error, however when i switch to user profile (su berkey), there is no problem. Why this occurs? is there a solution?</p><blockquote><p>tshark: Lua: Error during loading: [string "/usr/share/wireshark/init.lua"]:45: dofile has been disabled Running as user "root" and group "root". This could be dangerous.</p></blockquote></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Dec '12, 03:53</strong></p><img src="https://secure.gravatar.com/avatar/bde1409a68745702a5dd0f41c6a544e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="berkey&#39;s gravatar image" /><p><span>berkey</span><br />
<span class="score" title="31 reputation points">31</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="berkey has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 Dec '12, 03:53</strong> </span></p></div></div><div id="comments-container-17190" class="comments-container"></div><div id="comment-tools-17190" class="comment-tools"></div><div class="clear"></div><div id="comment-17190-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="17191"></span>

<div id="answer-container-17191" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17191-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17191-score" class="post-score" title="current number of votes">2</div><span id="post-17191-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jaap has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you're not using any lua scripting with Tshark, then all is fine. Tshark just protects you from running a script (with endless possibilities to mess up your system if programmed badly) with root privileges. You can ignore the warning in that case.</p><p>If you do run lua scripts, it is strongly advised to change your system to be able to do capturing and analysis without root <a href="http://wiki.wireshark.org/CaptureSetup/CapturePrivileges">privileges</a>.</p><p>If you do need to run Tshark with root privileges and lua scripts, then you need to patch the Tshark source code to remove the root-check...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Dec '12, 04:17</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-17191" class="comments-container"><span id="17199"></span><div id="comment-17199" class="comment"><div id="post-17199-score" class="comment-score"></div><div class="comment-text"><p>thanks i don't use any Lua commands. Your answer solved my question.</p></div><div id="comment-17199-info" class="comment-info"><span class="comment-age">(23 Dec '12, 08:52)</span> <span class="comment-user userinfo">berkey</span></div></div></div><div id="comment-tools-17191" class="comment-tools"></div><div class="clear"></div><div id="comment-17191-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="17229"></span>

<div id="answer-container-17229" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17229-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17229-score" class="post-score" title="current number of votes">2</div><span id="post-17229-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Whenever i try to analyze packets using tshark on Ubuntu with root permission</p></blockquote><p>Don't do that. Instead, <a href="http://anonscm.debian.org/viewvc/collab-maint/ext-maint/wireshark/trunk/debian/README.Debian?view=markup">give dumpcap the privileges it needs to capture traffic without requiring root privileges</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Dec '12, 02:37</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-17229" class="comments-container"></div><div id="comment-tools-17229" class="comment-tools"></div><div class="clear"></div><div id="comment-17229-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="26460"></span>

<div id="answer-container-26460" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26460-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26460-score" class="post-score" title="current number of votes">0</div><span id="post-26460-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>fix lua error:</p><p><strong>cd /usr/share/wireshark</strong></p><p><strong>nano init.lua</strong></p><p>line #29 change to:</p><p><strong>disable_lua = true</strong></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '13, 05:15</strong></p><img src="https://secure.gravatar.com/avatar/6bc95064f4a319225837db6a811a8509?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="oops13&#39;s gravatar image" /><p><span>oops13</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="oops13 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Oct '13, 05:16</strong> </span></p></div></div><div id="comments-container-26460" class="comments-container"></div><div id="comment-tools-26460" class="comment-tools"></div><div class="clear"></div><div id="comment-26460-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38417"></span>

<div id="answer-container-38417" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38417-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38417-score" class="post-score" title="current number of votes">0</div><span id="post-38417-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I just commented out the dialog line.</p><p>From:</p><p><strong>dofile = function() error("dofile has been disabled") end</strong></p><p>To:</p><p><strong>-- dofile = function() error("dofile has been disabled") end</strong></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '14, 11:48</strong></p><img src="https://secure.gravatar.com/avatar/1391fe339a48dabf8b1060889cec3d76?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kennybobs&#39;s gravatar image" /><p><span>Kennybobs</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kennybobs has no accepted answers">0%</span></p></div></div><div id="comments-container-38417" class="comments-container"></div><div id="comment-tools-38417" class="comment-tools"></div><div class="clear"></div><div id="comment-38417-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

