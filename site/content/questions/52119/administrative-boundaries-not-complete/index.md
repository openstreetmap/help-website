+++
type = "question"
title = "Administrative boundaries not complete"
description = '''Hi, I&#x27;m looking for a way to get lines of an administrative level (f.e. 4) with no duplicate parts. When I select all lines from planet_osm_line where admin_level=4 (within a specific country, in this case Papua new guinea) then I get the following: 5 records with osm_id=-311772, that I don&#x27;t want b...'''
date = "2016-09-19T21:53:00Z"
lastmod = "2016-09-27T08:24:00Z"
weight = 52119
keywords = [ "boundaries", "administrative" ]
aliases = [ "/questions/52119" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Administrative boundaries not complete](/questions/52119/administrative-boundaries-not-complete)

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
<span id="post-52119-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52119-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52119-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm looking for a way to get lines of an administrative level (f.e. 4) with no duplicate parts.</p>
<p>When I select all lines from planet_osm_line where admin_level=4 (within a specific country, in this case Papua new guinea) then I get the following: 5 records with osm_id=-311772, that I don't want because they duplicate the geometry of the adjacent level-4 polygon 1 record with osm_id=284884115, which is good no record with osm_id=352439111, which is not good, it's part of the boundary of that polygon.</p>
<p>Some links: full polygon: <a href="http://www.openstreetmap.org/relation/311772#map=12/-6.1016/144.1605">http://www.openstreetmap.org/relation/311772#map=12/-6.1016/144.1605</a> part in the result-set: <a href="http://www.openstreetmap.org/way/284884115#map=12/-6.1015/144.1605">http://www.openstreetmap.org/way/284884115#map=12/-6.1015/144.1605</a> missing part: <a href="http://www.openstreetmap.org/way/352439111#map=12/-6.1015/144.1605">http://www.openstreetmap.org/way/352439111#map=12/-6.1015/144.1605</a> The missing part is a river which also is the boundary of that polygon.</p>
<p>Is this something that has to be fixed in the osm2pgsql config (style-file)? relevant part: node,way admin_level text linear</p>
<p>or is there some query where I can include the missing parts easily?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-administrative" rel="tag" title="see questions tagged &#39;administrative&#39;">administrative</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Sep '16, 21:53</strong></p>
<img src="https://secure.gravatar.com/avatar/31d950f81ca152c66d5ed83bb7c53950?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paulosm2016&#39;s gravatar image" />
<p><span>Paulosm2016</span><br />
<span class="score" title="25 reputation points">25</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paulosm2016 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Sep '16, 21:54</strong> </span></p>
</div>
</div>
<div id="comments-container-52119" class="comments-container">
<span id="52121"></span>
<div id="comment-52121" class="comment">
<div id="post-52121-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Whenever I need boundaries, I use <a href="https://wambachers-osm.website/boundaries/">https://wambachers-osm.website/boundaries/</a></p>
</div>
<div id="comment-52121-info" class="comment-info">
<span class="comment-age">(20 Sep '16, 04:17)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="52124"></span>
<div id="comment-52124" class="comment">
<div id="post-52124-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>After searching a bit more, this could ofcourse also be a data-error...</p>
</div>
<div id="comment-52124-info" class="comment-info">
<span class="comment-age">(20 Sep '16, 07:37)</span> <span class="comment-user userinfo">Paulosm2016</span>
</div>
</div>
<span id="52143"></span>
<div id="comment-52143" class="comment">
<div id="post-52143-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I really don't understand the question. What exactly is going wrong?</p>
<p>You get 5 records of relation (polygon) 311772, but that's no problem? You seem to call way 284884115 a polygon, but that's just a line. Or is the problem that way 352439111 is missing from the polygon 311772?</p>
<p>(Boundaries are relations which are built upon ways. So it is perfectly normal that a way is called by several relations.)</p>
</div>
<div id="comment-52143-info" class="comment-info">
<span class="comment-age">(21 Sep '16, 14:03)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
<span id="52158"></span>
<div id="comment-52158" class="comment">
<div id="post-52158-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The more I think about it, the more convinced I am that it's a data issue, but I don't know enough of the rules to be sure.</p>
<p>Should there be a way with the same geometry as way 352439111, and that way having admin_level and boundary tags?</p>
</div>
<div id="comment-52158-info" class="comment-info">
<span class="comment-age">(22 Sep '16, 08:59)</span> <span class="comment-user userinfo">Paulosm2016</span>
</div>
</div>
<span id="52170"></span>
<div id="comment-52170" class="comment">
<div id="post-52170-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>After more investigation I'm getting to the conclusion that I don't understand how to render administrative boundaries where f.e. a river is used to define part of the boundary (there doesn't seem to be an admin_level tag in that case), so if anyone can answer me that, I think it would answer my main question</p>
</div>
<div id="comment-52170-info" class="comment-info">
<span class="comment-age">(22 Sep '16, 15:21)</span> <span class="comment-user userinfo">Paulosm2016</span>
</div>
</div>
</div>
<div id="comment-tools-52119" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52119-form-container" class="comment-form-container">
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

<span id="52240"></span>

<div id="answer-container-52240" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52240-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52240-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52240-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I finally figured it out. I join the planet_osm_line l table with the planet_osm_rels r on r.parts@&gt;array_append(NULL,l.osm_id) and hstore(tags)-&gt;'boundary' ='administrative' From there I can make my selection without duplicate lines</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Sep '16, 08:24</strong></p>
<img src="https://secure.gravatar.com/avatar/31d950f81ca152c66d5ed83bb7c53950?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paulosm2016&#39;s gravatar image" />
<p><span>Paulosm2016</span><br />
<span class="score" title="25 reputation points">25</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paulosm2016 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52240" class="comments-container">
&#10;</div>
<div id="comment-tools-52240" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52240-form-container" class="comment-form-container">
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

