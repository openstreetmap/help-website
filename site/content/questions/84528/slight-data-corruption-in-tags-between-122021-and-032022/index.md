+++
type = "question"
title = "Slight data corruption in tags between 12/2021 and 03/2022?"
description = '''I found some odd data in the tags on some sampled ways, including ways with the same id, tstamp, version with slightly different tag data (like space insertion or char(127) insertion) between the 2021 and 2022 data. One example is way 129970575 with a tstamp &quot;2021-07-28 18:10:02&quot; version 9. You noti...'''
date = "2022-05-19T14:32:00Z"
lastmod = "2022-05-19T17:10:00Z"
weight = 84528
keywords = [ "corrupt", "data", "tags" ]
aliases = [ "/questions/84528" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Slight data corruption in tags between 12/2021 and 03/2022?](/questions/84528/slight-data-corruption-in-tags-between-122021-and-032022)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84528-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84528-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84528-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I found some odd data in the tags on some sampled ways, including ways with the same id, tstamp, version with slightly different tag data (like space insertion or char(127) insertion) between the 2021 and 2022 data.</p>
<p>One example is way 129970575 with a tstamp "2021-07-28 18:10:02" version 9.<br />
You notice the insertion of two chr(127) in the tag value for tiger:cfcc,A21 in the most recent data.</p>
<p>My older data from 12/2021 includes tags: "{HFCS,""Minor Arterial"",name,""Walton Way"",lanes,3,oneway,yes,highway,primary,tiger:cfcc,A21,tiger:county,""Richmond, GA"",tiger:reviewed,no,tiger:zip_left,30901,tiger:name_base,Walton,tiger:name_type,Way,tiger:zip_right,30901}"</p>
<p>But the newer data from 3/2022: "{HFCS,""Minor Arterial"",name,""Walton Way"",lanes,3,oneway,yes,highway,primary,tiger:cfcc,A21,tiger:county,""Richmond, GA"",tiger:reviewed,no,tiger:zip_left,30901,tiger:name_base,Walton,tiger:name_type,Way,tiger:zip_right,30901}"</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-corrupt" rel="tag" title="see questions tagged &#39;corrupt&#39;">corrupt</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 May '22, 14:32</strong></p>
<img src="https://secure.gravatar.com/avatar/a8f374f9e963631edb07189841ca233e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gcapilot&#39;s gravatar image" />
<p><span>gcapilot</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gcapilot has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-84528" class="comments-container">
&#10;</div>
<div id="comment-tools-84528" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84528-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="84531"></span>

<div id="answer-container-84531" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84531-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84531-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84531-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I might be wrong, but there are definitely a couple of extra characters in front of A21 that don't copy/paste as spaces if you view the way history <a href="https://www.openstreetmap.org/way/129970575/history">https://www.openstreetmap.org/way/129970575/history</a> and as you post above the most recent edit was July 2021, so however you got the data in December must have removed them, and no longer does.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 May '22, 16:40</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-84531" class="comments-container">
<span id="84533"></span>
<div id="comment-84533" class="comment">
<div id="post-84533-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Looking back in the history, the non-printing characters were added in version 8 in 2015. Like you said, if these weren't present in gcapilot's December 2021 data, that must have been a result of the tool-chain used to retrieve the data. The "correct" state of the data should include these characters (though they obviously shouldn't be in the database at all).</p>
</div>
<div id="comment-84533-info" class="comment-info">
<span class="comment-age">(19 May '22, 17:09)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-84531" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84531-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="84534"></span>

<div id="answer-container-84534" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84534-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84534-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84534-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks very much! I need to learn how to view history in that way.</p>
<p>I used osmosis in both cases and it is entirely possible that those [DEL] characters got scrubbed somewhere along the line!</p>
<p>It looks like there were several instances of the chr(127) being inserted in various places in the current OSM ways that I'm using -</p>
<p>the following list of way-id and versions all have this chr(127) character embeded :</p>
<p>382363986 4 15025131 14 20143848 6 129970575 9 14664038 11 52109740 6 356378230 7 374035295 11 420904921 5 611000788 3 562474719 2 699814543 2 883155980 2 858385263 2 776387551 2 883155981 1 894524157 2 12289973 4 11466281 7 11466289 7 5584156 9</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 May '22, 17:10</strong></p>
<img src="https://secure.gravatar.com/avatar/a8f374f9e963631edb07189841ca233e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gcapilot&#39;s gravatar image" />
<p><span>gcapilot</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gcapilot has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 May '22, 18:49</strong> </span></p>
</div>
</div>
<div id="comments-container-84534" class="comments-container">
&#10;</div>
<div id="comment-tools-84534" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84534-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

