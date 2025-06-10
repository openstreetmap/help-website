+++
type = "question"
title = "Wrong placements at Tonga"
description = '''Hi, Could someone make a revert here at Tonga Island, its seems that some gates and ways are at the right place, but a lot of fences and houses are out of place. Compared with DigitalGlobe Premium Imagery.  https://www.openstreetmap.org/#map=18/-21.09995/-175.33821&amp;amp;layers=N I am not used to star...'''
date = "2019-03-30T21:34:00Z"
lastmod = "2019-04-01T13:59:00Z"
weight = 68557
keywords = [ "image", "revert" ]
aliases = [ "/questions/68557" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Wrong placements at Tonga](/questions/68557/wrong-placements-at-tonga)

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
<span id="post-68557-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68557-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68557-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Could someone make a revert here at Tonga Island, its seems that some gates and ways are at the right place, but a lot of fences and houses are out of place. Compared with DigitalGlobe Premium Imagery. <a href="https://www.openstreetmap.org/#map=18/-21.09995/-175.33821&amp;layers=N">https://www.openstreetmap.org/#map=18/-21.09995/-175.33821&amp;layers=N</a> I am not used to start a revert.</p>
<p>Greetz</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-image" rel="tag" title="see questions tagged &#39;image&#39;">image</span> <span class="post-tag tag-link-revert" rel="tag" title="see questions tagged &#39;revert&#39;">revert</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Mar '19, 21:34</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-68557" class="comments-container">
<span id="68566"></span>
<div id="comment-68566" class="comment">
<div id="post-68566-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Are there any GPS traces for the roads?</p>
</div>
<div id="comment-68566-info" class="comment-info">
<span class="comment-age">(01 Apr '19, 00:39)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-68557" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68557-form-container" class="comment-form-container">
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

<span id="68575"></span>

<div id="answer-container-68575" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68575-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68575-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68575-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Hendrikklaas has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>An example node that is offset is <a href="https://www.openstreetmap.org/node/3233951970">https://www.openstreetmap.org/node/3233951970</a> . That was added in 2014, apparently using Bing imagery, and has not been moved. It is offset according to current Bing imagery. All current imagery agrees about the offset, so presumably the older Bing imagery was wrong.</p>
<p>This unfortunately is the danger of using only imagery to add lots of detail - there's lots of work to do to fix the wrongly-added detail afterwards. Also, it's not simply case of selecting everything and moving; the offsets of different features seem to vary.</p>
<p>What I'd do before doing anything else is try to get a number of north-south and east-west GPS tracks in place (if you're not local talk to someone who is). It'll be a lot of work to realign data and you don't want to do that twice! In the meantime until you can get some GPS traces uploaded I'd just live with the offset and add features logically with respect to other features. Then, when you have enough local GPS traces to be sure about how much the data is offset you can begin the task of lining the data up.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Apr '19, 13:54</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 May '19, 15:40</strong> </span></p>
</div>
</div>
<div id="comments-container-68575" class="comments-container">
&#10;</div>
<div id="comment-tools-68575" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68575-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="68559"></span>

<div id="answer-container-68559" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68559-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68559-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68559-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think you need to find the changeset that messed everything up. If you know a changeset you could start a discussion on it. That will help move things forward. I am not an expert either, I tried to look back through history, could this one be to blame:</p>
<p>Changeset: 65964144 Smoothed and aligned roads and driveways. #Kaart 2019 Closed 3 months ago by TigerTamer</p>
<p>i dont know how to see diffs of before and after.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Mar '19, 03:17</strong></p>
<img src="https://secure.gravatar.com/avatar/f18844202962b4d8003d464e71f4ae6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OpenMapsRH&#39;s gravatar image" />
<p><span>OpenMapsRH</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OpenMapsRH has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68559" class="comments-container">
<span id="68565"></span>
<div id="comment-68565" class="comment">
<div id="post-68565-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You can see diffs <a href="https://overpass-api.de/achavi/?changeset=65964144">on achavi</a>, if the changeset is small enough. OSMCha <a href="https://osmcha.mapbox.com/changesets/65964144/">also does this</a> (although it seems to be struggling right now).</p>
</div>
<div id="comment-68565-info" class="comment-info">
<span class="comment-age">(01 Apr '19, 00:38)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="68577"></span>
<div id="comment-68577" class="comment">
<div id="post-68577-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>An example node from that changeset is <a href="https://www.openstreetmap.org/node/5287342639/history">https://www.openstreetmap.org/node/5287342639/history</a> . That moved a node that's part of a road, but not any of the underlying buildings. Arguably this makes the eventual fixing job harder rather than easier as it means the the data offset isn't consistent (though it'd be unfair to say "messed everything up" the the data was wrong to start with). At the very least I'd suggest commenting on that changeset to make that user aware of this help discussion.</p>
</div>
<div id="comment-68577-info" class="comment-info">
<span class="comment-age">(01 Apr '19, 13:59)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-68559" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68559-form-container" class="comment-form-container">
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

