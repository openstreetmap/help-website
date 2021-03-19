+++
type = "question"
title = "Decimal point vs. decimal comma"
description = '''I am currently copying conversation statistics provided by Wireshark to an Excel spreadsheet for further analysis. It seems that the column &quot;Relative Start&quot; is using a decimal point while the column &quot;Duration&quot; uses a comma.  What format is Wireshark using? Is there a way to change Wireshark&#x27;s behavi...'''
date = "2011-09-08T00:44:00Z"
lastmod = "2011-09-10T08:42:00Z"
weight = 6207
keywords = [ "conversation", "statistics" ]
aliases = [ "/questions/6207" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Decimal point vs. decimal comma](/questions/6207/decimal-point-vs-decimal-comma)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6207-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6207-score" class="post-score" title="current number of votes">0</div><span id="post-6207-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am currently copying conversation statistics provided by Wireshark to an Excel spreadsheet for further analysis.</p><p>It seems that the column "Relative Start" is using a decimal point while the column "Duration" uses a comma.</p><p>What format is Wireshark using? Is there a way to change Wireshark's behavior? BTW, my system locale is set to German (decimal comma, digit separator is a point)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-conversation" rel="tag" title="see questions tagged &#39;conversation&#39;">conversation</span> <span class="post-tag tag-link-statistics" rel="tag" title="see questions tagged &#39;statistics&#39;">statistics</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Sep '11, 00:44</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-6207" class="comments-container"></div><div id="comment-tools-6207" class="comment-tools"></div><div class="clear"></div><div id="comment-6207-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6224"></span>

<div id="answer-container-6224" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6224-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6224-score" class="post-score" title="current number of votes">3</div><span id="post-6224-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="packethunter has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like this was a Wireshark bug where the start time was being formatted as a string prior to being displayed/exported. I checked in a fix in <a href="http://anonsvn.wireshark.org/viewvc?revision=38948&amp;view=revision">r38948</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Sep '11, 19:16</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-6224" class="comments-container"><span id="6243"></span><div id="comment-6243" class="comment"><div id="post-6243-score" class="comment-score"></div><div class="comment-text"><p>excellent. Thanks a lot!</p></div><div id="comment-6243-info" class="comment-info"><span class="comment-age">(10 Sep '11, 01:00)</span> <span class="comment-user userinfo">packethunter</span></div></div><span id="6255"></span><div id="comment-6255" class="comment"><div id="post-6255-score" class="comment-score"></div><div class="comment-text"><p>Try the checkmark to accept the answer ;-)</p></div><div id="comment-6255-info" class="comment-info"><span class="comment-age">(10 Sep '11, 08:42)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-6224" class="comment-tools"></div><div class="clear"></div><div id="comment-6224-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

