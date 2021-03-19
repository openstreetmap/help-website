+++
type = "question"
title = "Filtering out ICMP Destination unreachable"
description = '''Hi ! I managed to create this filter : icmp &amp;gt;= &quot;Destination unreachable&quot; but of course it does only show these items ! I want them filtered out ! How do I do this ? I tried : Not icmp &amp;gt;= &quot;Destination unreachable&quot; icmp not &amp;gt;= &quot;Destination unreachable&quot; icmp != &quot;Destination unreachable&quot; to no ...'''
date = "2015-06-17T10:55:00Z"
lastmod = "2015-06-17T14:04:00Z"
weight = 43275
keywords = [ "exclude", "icmp", "unreachable" ]
aliases = [ "/questions/43275" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Filtering out ICMP Destination unreachable](/questions/43275/filtering-out-icmp-destination-unreachable)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43275-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43275-score" class="post-score" title="current number of votes">0</div><span id="post-43275-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hi !</p><p>I managed to create this filter : <strong>icmp &gt;= "Destination unreachable"</strong> but of course it does only show these items ! I want them filtered out ! How do I do this ?</p><p>I tried :</p><p><strong>Not</strong> icmp &gt;= "Destination unreachable"</p><p>icmp <strong>not</strong> &gt;= "Destination unreachable"</p><p>icmp <strong>!=</strong> "Destination unreachable"</p><p>to no avail ! What shoul I do ?</p><p>Thanks for the answer...</p><p><strong>iBenny</strong></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-exclude" rel="tag" title="see questions tagged &#39;exclude&#39;">exclude</span> <span class="post-tag tag-link-icmp" rel="tag" title="see questions tagged &#39;icmp&#39;">icmp</span> <span class="post-tag tag-link-unreachable" rel="tag" title="see questions tagged &#39;unreachable&#39;">unreachable</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jun '15, 10:55</strong></p><img src="https://secure.gravatar.com/avatar/62b3d6bffa7a1ce038f6f372b7e3cd96?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iBenny&#39;s gravatar image" /><p><span>iBenny</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iBenny has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Jun '15, 02:22</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-43275" class="comments-container"></div><div id="comment-tools-43275" class="comment-tools"></div><div class="clear"></div><div id="comment-43275-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43277"></span>

<div id="answer-container-43277" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43277-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43277-score" class="post-score" title="current number of votes">2</div><span id="post-43277-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="cmaynard has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>!(icmp &gt;= "Destination unreachable")</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '15, 11:15</strong></p><img src="https://secure.gravatar.com/avatar/d9cf592a79eafbc3b2a8b3f38cf38362?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Amato_C&#39;s gravatar image" /><p><span>Amato_C</span><br />
<span class="score" title="1098 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="32 badges"><span class="bronze">●</span><span class="badgecount">32</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Amato_C has 15 accepted answers">14%</span></p></div></div><div id="comments-container-43277" class="comments-container"><span id="43278"></span><div id="comment-43278" class="comment"><div id="post-43278-score" class="comment-score"></div><div class="comment-text"><p>Hi Amato !</p><p>It works perfectly !</p><p>Meny thanks,</p><p><strong>iBenny</strong></p></div><div id="comment-43278-info" class="comment-info"><span class="comment-age">(17 Jun '15, 12:31)</span> <span class="comment-user userinfo">iBenny</span></div></div><span id="43284"></span><div id="comment-43284" class="comment"><div id="post-43284-score" class="comment-score"></div><div class="comment-text"><p>Hi Benny. Could you mark the answer as solved so it can help others?</p></div><div id="comment-43284-info" class="comment-info"><span class="comment-age">(17 Jun '15, 14:04)</span> <span class="comment-user userinfo">Amato_C</span></div></div></div><div id="comment-tools-43277" class="comment-tools"></div><div class="clear"></div><div id="comment-43277-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

