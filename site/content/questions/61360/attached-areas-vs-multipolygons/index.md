+++
type = "question"
title = "Attached areas vs. multipolygons"
description = '''Hi, So as I started right with editing complex multipolygons I was sure when you have for e.g. a highway with two areas attached to it, you have to split the way at the proper nodes, draw the external lines of the areas and define them with outer roles.   Now &quot;accidentally&quot; I&#x27;ve found that you can j...'''
date = "2017-12-26T10:25:00Z"
lastmod = "2017-12-27T01:41:00Z"
weight = 61360
keywords = [ "multipolygon", "attached", "areas" ]
aliases = [ "/questions/61360" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Attached areas vs. multipolygons](/questions/61360/attached-areas-vs-multipolygons)

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
<span id="post-61360-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61360-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61360-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>So as I started right with editing complex <em>multipolygon</em>s I was sure when you have for e.g. a highway with two areas attached to it, you have to split the way at the proper nodes, draw the external lines of the areas and define them with <em>outer roles</em>.</p>
<p><img src="https://i.imgur.com/QJlov4O.png" title="multipolygons" alt="image" /></p>
<p>Now "accidentally" I've found that you can just draw the two areas in ID or JOSM taking care that the nodes snap to the existing nodes so you have two selectable closed areas (on the screenshot both are selected, the "shared segment" shows two directions), no multipolygon stuff at all, and no validation errors in JOSM or geofabrik's OSM Inspector.</p>
<p><img src="https://i.imgur.com/u9Dj3IX.png" title="attached areas" alt="image" /></p>
<p>So can it be said that the ONE and ONLY case when you need multipolygons is when you have to punch a hole into an area with <em>inner role</em> otherwise unnecessary?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span> <span class="post-tag tag-link-attached" rel="tag" title="see questions tagged &#39;attached&#39;">attached</span> <span class="post-tag tag-link-areas" rel="tag" title="see questions tagged &#39;areas&#39;">areas</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Dec '17, 10:25</strong></p>
<img src="https://secure.gravatar.com/avatar/7fa29659531211471ebd66569f20cd79?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="I_G&#39;s gravatar image" />
<p><span>I_G</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="I_G has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-61360" class="comments-container">
&#10;</div>
<div id="comment-tools-61360" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61360-form-container" class="comment-form-container">
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

<span id="61361"></span>

<div id="answer-container-61361" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61361-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61361-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-61361-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="I_G has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As always it is a matter of taste, and judgement. If you are looking at larger areas, and especially if the line between the two areas has a character of its own (e.g. a river, a fence, or a highway as in your example), then it might be advisable to use multipolygons for clarity. Personally I wouldn't use multipolygons if we're only talking 4 or 5 shared nodes but I would start thinking about it if it was 40 or 50!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Dec '17, 11:01</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</img>
</div>
</div>
<div id="comments-container-61361" class="comments-container">
<span id="61370"></span>
<div id="comment-61370" class="comment">
<div id="post-61370-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah, as it seems that both are valid constructions so it can be a judgement call. I'd think that the advantage of the second example would be that you don't have to split that line in the middle. I am personally responsible for a lot of nice long tracks/paths turning into even more not so nice short tracks/paths because of splitting them to use their segments in multipolygons. And then if you want to change a tag you have to change on 10 short paths instead of 1 long one, the original history is also remains only on one path... so yeah, as always you get some, you lose some. Anyways thanks for the reply.</p>
</div>
<div id="comment-61370-info" class="comment-info">
<span class="comment-age">(26 Dec '17, 15:01)</span> <span class="comment-user userinfo">I_G</span>
</div>
</div>
<span id="61371"></span>
<div id="comment-61371" class="comment">
<div id="post-61371-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>An observation: while there is not unanimous agreement on the topic, most mappers will agree that "gluing" areas (I suspect in your case they are actually landuse areas) to highways is not a particularly good idea, so maybe you should simply change your editing style and avoid the multi-polygon issue that way.</p>
</div>
<div id="comment-61371-info" class="comment-info">
<span class="comment-age">(26 Dec '17, 15:30)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="61375"></span>
<div id="comment-61375" class="comment">
<div id="post-61375-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I do this "gluing" only when that track/path/etc. is really one of the borders of an area, when it's not I don't glue them just to be more "tidier". Or you mean when it really is the border still draw the entire area separately just very close to that highway?</p>
</div>
<div id="comment-61375-info" class="comment-info">
<span class="comment-age">(26 Dec '17, 17:32)</span> <span class="comment-user userinfo">I_G</span>
</div>
</div>
<span id="61376"></span>
<div id="comment-61376" class="comment">
<div id="post-61376-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>As a experienced mapper who has edited quite a substantial number of roads, I have personally come to really dislike highways (paths, tracks, roads) glued to areas, so I recommend that the two are always kept separate. Anecdotal, I once saw someone mapping bus routes in Copenhagen, where at the time a number of landuse=residential polygons were glued to roads. This guy apparently didn't notice the polygons and ended up splitting them, rather than split the roads and... put parts of the bus route relations on some of the split landuse ways. So, while it can be quite annoying to work with roads glued to areas, there's also absolutely no guarantee that subsequent (inexperienced) mappers will even notice that an area is glued to the road they are editing or that a road is glued to the area they are editing.</p>
</div>
<div id="comment-61376-info" class="comment-info">
<span class="comment-age">(26 Dec '17, 19:47)</span> <span class="comment-user userinfo">Hjart</span>
</div>
</div>
<span id="61378"></span>
<div id="comment-61378" class="comment">
<div id="post-61378-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Another situation where multipolygons are useful is when two riverbank polygons meet. To join them I create two multipolygons and then make it so they share one common way, the way that spans their intersection.</p>
<p>Also, each way in OSM is limited to 2000 nodes. When you create an object with more then that number of nodes, you must split it and then make those two ways into a multipolygon.</p>
</div>
<div id="comment-61378-info" class="comment-info">
<span class="comment-age">(27 Dec '17, 01:41)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-61361" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61361-form-container" class="comment-form-container">
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

