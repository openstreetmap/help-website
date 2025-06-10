+++
type = "question"
title = "[closed] smaller planet file after recent update?"
description = '''Hello - Yesterday I updated my planet.osm file using osmosis (for the first time!) and the updated planet_new.osm file is smaller than the original planet.osm. This is not the result I expected, I expect the updated file to always be larger, unless there has been an (extensive) clean up.  By the num...'''
date = "2014-11-06T18:38:00Z"
lastmod = "2014-11-13T18:02:00Z"
weight = 38360
keywords = [ "planet" ]
aliases = [ "/questions/38360" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] smaller planet file after recent update?](/questions/38360/smaller-planet-file-after-recent-update)

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
<span id="post-38360-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38360-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38360-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello -</p>
<p>Yesterday I updated my planet.osm file using osmosis (for the first time!) and the updated planet_new.osm file is smaller than the original planet.osm. This is not the result I expected, I expect the updated file to always be larger, unless there has been an (extensive) clean up. By the numbers:</p>
<p>25.9gb planet.osm.pbf from 25 September</p>
<p>1.9gb "update.osc.gz from 5 November</p>
<p>21.3gb planet_new.osm.pbf from 5 November</p>
<p>Before I post my "update" code I am wondering if these results are correct.</p>
<p>Thanks, pitney</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Nov '14, 18:38</strong></p>
<img src="https://secure.gravatar.com/avatar/92443a39a30b5e613ce00de446845b9e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pitney&#39;s gravatar image" />
<p><span>pitney</span><br />
<span class="score" title="44 reputation points">44</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pitney has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>13 Nov '14, 18:05</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-38360" class="comments-container">
<span id="38379"></span>
<div id="comment-38379" class="comment">
<div id="post-38379-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There's quite some detail missing in your question. Can you post the exact steps you performed as well, e.g. exact command line arguments, how you created update.osc.gz, etc.</p>
<p>Do you know osmupdate? This tool might come in handy to update your pbf file, as it runs all required download and merge steps automatically without much need for user intervention.</p>
</div>
<div id="comment-38379-info" class="comment-info">
<span class="comment-age">(08 Nov '14, 14:05)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="38541"></span>
<div id="comment-38541" class="comment">
<div id="post-38541-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>mmd -</p>
<p>Thank you for the suggestion on osmupdate, it worked better for me. First I installed osmtools (for osmconvert (zlib)) from here:</p>
<p><a href="http://trajectorycomputing.com/category/tools/">http://trajectorycomputing.com/category/tools/</a></p>
<p>then osmupdate. I may still have an issue because I am using a planet file from osm2garmin (trying to avoid that 26gb download) but I am good to go for now. How do I mark this as closed? pitney</p>
</div>
<div id="comment-38541-info" class="comment-info">
<span class="comment-age">(13 Nov '14, 17:52)</span> <span class="comment-user userinfo">pitney</span>
</div>
</div>
<span id="38542"></span>
<div id="comment-38542" class="comment">
<div id="post-38542-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/9955/pitney">@pitney</a>: and now your file is not smaller any more?</p>
</div>
<div id="comment-38542-info" class="comment-info">
<span class="comment-age">(13 Nov '14, 18:02)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="38543"></span>
<div id="comment-38543" class="comment">
<div id="post-38543-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/9955/pitney"></a><a href="http://help.openstreetmap.org/users/9955/pitney">@pitney</a>: If mmd's comment would be an "answer", you could <a href="/questions/34318/how-to-mark-an-answer-as-accepted-and-mark-my-question-as-answered">accept</a> it. Converting would also work, but not currently (software bug). I have closed this question in the alternative.</p>
</div>
<div id="comment-38543-info" class="comment-info">
<span class="comment-age">(13 Nov '14, 18:02)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-38360" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38360-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Solved. See comments below (osmupdate worked better)." by aseerel4c26 13 Nov '14, 18:05

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38371"></span>

<div id="answer-container-38371" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38371-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38371-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38371-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hmm, the <a href="http://planet.openstreetmap.org/pbf/"><em>full</em> planet pbf files</a> did not get smaller recently (and I am not aware of a recent big cleanup). So, yes, this seems to be strange.</p>
<p>Note: I really may not be the best person to answer this (because I got really no experience with planet files or OSM DBs).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Nov '14, 02:52</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Nov '14, 02:53</strong> </span></p>
</div>
</div>
<div id="comments-container-38371" class="comments-container">
&#10;</div>
<div id="comment-tools-38371" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38371-form-container" class="comment-form-container">
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

