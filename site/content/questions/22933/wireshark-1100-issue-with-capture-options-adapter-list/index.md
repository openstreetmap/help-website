+++
type = "question"
title = "Wireshark 1.10.0 issue with Capture Options Adapter List"
description = '''I have an issue on a few PC&#x27;s (Windows 7 Home Premium and Professional both 64 bit)not showing the adapters next to their check boxes when in the &quot;Capture Options&quot; menu. See graphic below. I have uninstalled and reinstalled with no change in results. Its not the end of the world, but am wondering if...'''
date = "2013-07-13T13:15:00Z"
lastmod = "2013-07-14T17:07:00Z"
weight = 22933
keywords = [ "capture-options", "capture", "1.10.0", "64-bit", "wireshark" ]
aliases = [ "/questions/22933" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 1.10.0 issue with Capture Options Adapter List](/questions/22933/wireshark-1100-issue-with-capture-options-adapter-list)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22933-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22933-score" class="post-score" title="current number of votes">0</div><span id="post-22933-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an issue on a few PC's (Windows 7 Home Premium and Professional both 64 bit)not showing the adapters next to their check boxes when in the "Capture Options" menu. See graphic below.</p><p>I have uninstalled and reinstalled with no change in results. Its not the end of the world, but am wondering if its something with the application or my PC's.</p><p>Thanks for any input!</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Wireshark_Issue_1.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-options" rel="tag" title="see questions tagged &#39;capture-options&#39;">capture-options</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-1.10.0" rel="tag" title="see questions tagged &#39;1.10.0&#39;">1.10.0</span> <span class="post-tag tag-link-64-bit" rel="tag" title="see questions tagged &#39;64-bit&#39;">64-bit</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jul '13, 13:15</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p><span>Rooster_50</span><br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Jul '13, 14:20</strong> </span></p></div></div><div id="comments-container-22933" class="comments-container"><span id="22938"></span><div id="comment-22938" class="comment"><div id="post-22938-score" class="comment-score">1</div><div class="comment-text"><p>What displays if you select Edit -&gt; Preferences, click Capture, and then click the "Edit..." button for "Columns"?</p></div><div id="comment-22938-info" class="comment-info"><span class="comment-age">(13 Jul '13, 20:11)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="22939"></span><div id="comment-22939" class="comment"><div id="post-22939-score" class="comment-score"></div><div class="comment-text"><p><img src="https://osqa-ask.wireshark.org/upfiles/Picture1.png" alt="alt text" /></p></div><div id="comment-22939-info" class="comment-info"><span class="comment-age">(13 Jul '13, 20:40)</span> <span class="comment-user userinfo">Rooster_50</span></div></div></div><div id="comment-tools-22933" class="comment-tools"></div><div class="clear"></div><div id="comment-22933-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22940"></span>

<div id="answer-container-22940" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22940-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22940-score" class="post-score" title="current number of votes">0</div><span id="post-22940-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Rooster_50 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, that was the cause. I dont understand why that would have all been unselected.<br />
</p><p>Thank you Guy Harris.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jul '13, 20:41</strong></p><img src="https://secure.gravatar.com/avatar/bb79e0c62df46ecf47cc004a0a2d3cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rooster_50&#39;s gravatar image" /><p><span>Rooster_50</span><br />
<span class="score" title="238 reputation points">238</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rooster_50 has 5 accepted answers">15%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>13 Jul '13, 20:45</strong> </span></p></div></div><div id="comments-container-22940" class="comments-container"><span id="22941"></span><div id="comment-22941" class="comment"><div id="post-22941-score" class="comment-score"></div><div class="comment-text"><p>Please file a bug (and attach both screenshots), because:</p><ul><li>it shouldn't be possible to make the column with the interface name and details disappear;</li><li>if it should be possible to make a checkbox column disappear, it should <em>disappear</em>, complete with the checkbox.</li></ul></div><div id="comment-22941-info" class="comment-info"><span class="comment-age">(13 Jul '13, 23:25)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="22962"></span><div id="comment-22962" class="comment"><div id="post-22962-score" class="comment-score"></div><div class="comment-text"><p>Will do....Thanks for your feedback.</p></div><div id="comment-22962-info" class="comment-info"><span class="comment-age">(14 Jul '13, 15:21)</span> <span class="comment-user userinfo">Rooster_50</span></div></div><span id="22963"></span><div id="comment-22963" class="comment"><div id="post-22963-score" class="comment-score"></div><div class="comment-text"><p>Bug number <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8932">8932</a>.</p></div><div id="comment-22963-info" class="comment-info"><span class="comment-age">(14 Jul '13, 17:07)</span> <span class="comment-user userinfo">Rooster_50</span></div></div></div><div id="comment-tools-22940" class="comment-tools"></div><div class="clear"></div><div id="comment-22940-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

