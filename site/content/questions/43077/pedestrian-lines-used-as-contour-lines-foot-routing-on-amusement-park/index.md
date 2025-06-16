+++
type = "question"
title = "Pedestrian lines used as contour lines. Foot routing on amusement park."
description = '''In SeaWorld Orlando, I see that a huge multipolygon was made out of &quot;highway=pedestrian&quot; lines. When asking in the normal map to go from one place to another within the park like this, it plots a route along the contour of the path or of buildings, etc. If the places aren&#x27;t connected by the same lin...'''
date = "2015-05-14T13:42:00Z"
lastmod = "2015-05-14T15:05:00Z"
weight = 43077
keywords = [ "pedestrian", "park", "routing" ]
aliases = [ "/questions/43077" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Pedestrian lines used as contour lines. Foot routing on amusement park.](/questions/43077/pedestrian-lines-used-as-contour-lines-foot-routing-on-amusement-park)

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
<span id="post-43077-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43077-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-43077-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In <a href="https://www.openstreetmap.org/edit#map=17/28.41040/-81.46210">SeaWorld Orlando</a>, I see that a huge multipolygon was made out of "highway=pedestrian" lines. When asking in the normal map to go from one place to another within the park <a href="https://www.openstreetmap.org/directions?engine=mapquest_foot&amp;route=28.41052%2C-81.45967%3B28.40882%2C-81.46119#map=17/28.40866/-81.46165">like this</a>, it plots a route along the contour of the path or of buildings, etc. If the places aren't connected by the same line, or close enough, it tells me that a path couldn't be found between these points.</p>
<p>Is it OK to change all these contour lines to just a normal line, and then make linear pathways along the surface where people walk? That would help in routing.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pedestrian" rel="tag" title="see questions tagged &#39;pedestrian&#39;">pedestrian</span> <span class="post-tag tag-link-park" rel="tag" title="see questions tagged &#39;park&#39;">park</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 May '15, 13:42</strong></p>
<img src="https://secure.gravatar.com/avatar/141108f8bb9ba4c092e002143d5a2edc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Laserion&#39;s gravatar image" />
<p><span>Laserion</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Laserion has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43077" class="comments-container">
&#10;</div>
<div id="comment-tools-43077" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43077-form-container" class="comment-form-container">
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

<span id="43079"></span>

<div id="answer-container-43079" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43079-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43079-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-43079-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For clarification, the user has made a multipolygon relation with those highway=pedestrian ways: <a href="https://www.openstreetmap.org/relation/4667908">https://www.openstreetmap.org/relation/4667908</a></p>
<p>I think the goal was to make the walkways pedestrian areas, as mentioned on the <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dpedestrian">highway=pedestrian</a> wiki page. This is a valid method to do detailed mapping rather than linear footways.</p>
<p>However, I'm not sure this was done in quite the right way--I'd think it'd be better to leave tagging off the actual ways, and tag highway=pedestrian, area=yes on the multipolygon relation. Have you contacted the user about this?</p>
<p>All that said, I've heard that most routers don't deal with routing through areas very well, so I'm not sure if changing the tagging as I mention above will improve routing.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 May '15, 14:47</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-43079" class="comments-container">
<span id="43081"></span>
<div id="comment-43081" class="comment">
<div id="post-43081-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You're right, highway=pedestrian should be tagged on th MP, not the ways. I've edited my answer to note that the data is partially/also at fault.</p>
</div>
<div id="comment-43081-info" class="comment-info">
<span class="comment-age">(14 May '15, 15:05)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-43079" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43079-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43080"></span>

<div id="answer-container-43080" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43080-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-43080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The data should be improved, but this is mainly an issue with the router software. See also the answers to <a href="/questions/42460/what-to-do-in-these-situations-pedestrian-areas">this question</a>.</p>
<p>Routing over areas is seemingly not a trivial feature. Some routers implement the workaround that the route along the edge of areas. There are a lot of discussions on the development mailing lists of various routers, so hopefully this'll soon be a solved problem.</p>
<p>Some mappers have taken the pragmatic step of helping the routers by adding linear footpaths in addition to the area. But in a case like SeaWorld, it could become ugly quite quickly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 May '15, 14:58</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 May '15, 15:02</strong> </span></p>
</div>
</div>
<div id="comments-container-43080" class="comments-container">
&#10;</div>
<div id="comment-tools-43080" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43080-form-container" class="comment-form-container">
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

