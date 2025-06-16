+++
type = "question"
title = "Help! I&#x27;ve lost a road"
description = '''I have updated an unclassified road to add the name of a trail which follows the road. In the process the road no longer shows up on OSM. I don&#x27;t know why - what have I done wrong? Road = https://www.openstreetmap.org/changeset/29805078'''
date = "2015-03-28T13:29:00Z"
lastmod = "2015-03-28T15:36:00Z"
weight = 41960
keywords = [ "road", "missing" ]
aliases = [ "/questions/41960" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Help! I've lost a road](/questions/41960/help-ive-lost-a-road)

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
<span id="post-41960-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41960-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41960-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have updated an unclassified road to add the name of a trail which follows the road. In the process the road no longer shows up on OSM. I don't know why - what have I done wrong? Road = <a href="https://www.openstreetmap.org/changeset/29805078">https://www.openstreetmap.org/changeset/29805078</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Mar '15, 13:29</strong></p>
<img src="https://secure.gravatar.com/avatar/45d62517b772d1ae37975c05be147cf9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FollowMeChaps&#39;s gravatar image" />
<p><span>FollowMeChaps</span><br />
<span class="score" title="325 reputation points">325</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FollowMeChaps has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-41960" class="comments-container">
&#10;</div>
<div id="comment-tools-41960" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41960-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="41961"></span>

<div id="answer-container-41961" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41961-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41961-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-41961-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's there on at least some zoom levels now - <a href="https://www.openstreetmap.org/way/30698459/history">https://www.openstreetmap.org/way/30698459/history</a></p>
<p>What happened was that it got inadvertantly set to "unclassified;service" in <a href="https://www.openstreetmap.org/changeset/29738345">this changeset</a> - probably by merging a <a href="https://www.openstreetmap.org/way/153227862/history">road previously tagged as "service"</a> with a road previously tagged as "unclassified".</p>
<p>Actually, I wouldn't add the name "Mendip Trail" to the road unless the name of the road really is "Mendip Trail". If that's a waymarked route that runs along several footpaths and roads, I'd add it as a <a href="https://wiki.openstreetmap.org/wiki/Relation:route">route relation</a> and add the relevant footpaths and roads to that relation. That way it'll show up on sites such as <a href="http://waymarkedtrails.org/en/?zoom=13&amp;lat=51.31671&amp;lon=-2.7357&amp;hill=0#">this one</a> like the West Mendip Way does.</p>
<p>I'd also check for other ways in recent changesets that have got inadvertently merged too - <a href="https://www.openstreetmap.org/way/35647833/history">this one</a> seems to have been created from a separate bridleway and footway and all the tags from either piece are now applied to the whole. What you'll need to do (or ask someone else to do) is to figure out where the previously merged sections started and ended, split the way again, and apply the correct tags to the correct piece.</p>
<p>If you want to ask real-time questions about fixing something like this, normally the place that I'd suggest would be #osm-gb on <a href="https://wiki.openstreetmap.org/wiki/Irc">IRC</a> (or an appropriate other country channel or #osm) for elsewhere in the world, but on Saturday afternoon in the UK I it might not be very busy.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Mar '15, 14:10</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Mar '15, 14:19</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span></p>
</div>
</div>
<div id="comments-container-41961" class="comments-container">
<span id="41963"></span>
<div id="comment-41963" class="comment">
<div id="post-41963-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The answers I got here may help. <a href="/questions/34347/i-want-to-add-a-new-long-distance-hiking-route-to-the-map">https://help.openstreetmap.org/questions/34347/i-want-to-add-a-new-long-distance-hiking-route-to-the-map</a></p>
</div>
<div id="comment-41963-info" class="comment-info">
<span class="comment-age">(28 Mar '15, 14:33)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="41964"></span>
<div id="comment-41964" class="comment">
<div id="post-41964-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Many thanks for your speedy and helpful response. I have now done as suggested an removed name and added a relation.</p>
</div>
<div id="comment-41964-info" class="comment-info">
<span class="comment-age">(28 Mar '15, 15:36)</span> <span class="comment-user userinfo">FollowMeChaps</span>
</div>
</div>
</div>
<div id="comment-tools-41961" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41961-form-container" class="comment-form-container">
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

