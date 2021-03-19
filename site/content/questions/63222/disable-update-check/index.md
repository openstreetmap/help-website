+++
type = "question"
title = "Disable update check"
description = '''Hello. I am trying to disable the Wireshark update check. I notice that whenever Wireshark (running on Windows 7) starts, it updates the registry setting &#x27;HKEY_Users/Wireshark/WinSparkle Settings/CheckForUpdates&#x27; to 1. What setting should I use to disable the update check?  I am running Version 2.2....'''
date = "2017-07-28T11:48:00Z"
lastmod = "2017-07-28T11:54:00Z"
weight = 63222
keywords = [ "windows", "update" ]
aliases = [ "/questions/63222" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Disable update check](/questions/63222/disable-update-check)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63222-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63222-score" class="post-score" title="current number of votes">0</div><span id="post-63222-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello.</p><p>I am trying to disable the Wireshark update check. I notice that whenever Wireshark (running on Windows 7) starts, it updates the registry setting 'HKEY_Users/Wireshark/WinSparkle Settings/CheckForUpdates' to 1.</p><p>What setting should I use to disable the update check?</p><p>I am running Version 2.2.2 (v2.2.2-0-g775fb08) on Windows 7</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jul '17, 11:48</strong></p><img src="https://secure.gravatar.com/avatar/b40cb1894651b955f81fdc10570fc065?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jbreukelman&#39;s gravatar image" /><p><span>jbreukelman</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jbreukelman has no accepted answers">0%</span></p></div></div><div id="comments-container-63222" class="comments-container"></div><div id="comment-tools-63222" class="comment-tools"></div><div class="clear"></div><div id="comment-63222-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63223"></span>

<div id="answer-container-63223" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63223-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63223-score" class="post-score" title="current number of votes">2</div><span id="post-63223-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cmaynard has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>In Wireshark, go <code>Edit -&gt; Preferences -&gt; Advanced</code>. Write "update" into the <code>Search</code> field, and at the <code>gui.update.enabled</code> line below, double-click the <code>TRUE</code> to change it to <code>FALSE</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jul '17, 11:54</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-63223" class="comments-container"></div><div id="comment-tools-63223" class="comment-tools"></div><div class="clear"></div><div id="comment-63223-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

