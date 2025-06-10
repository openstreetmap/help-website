+++
type = "question"
title = "Overpass returns node&#x27;s data with area&#x27;s information that should not exist"
description = '''There is such village: http://www.openstreetmap.org/node/337512354 I want to get all relationships of this village. In order to get it, I do request: http://overpass-api.de/api/interpreter?data=node(337512354);is_in;out; In this file the top one area record shows:  &amp;lt;area id=&quot;2430719979&quot;&amp;gt;  &amp;lt;...'''
date = "2016-06-07T08:14:00Z"
lastmod = "2016-06-07T09:26:00Z"
weight = 50056
keywords = [ "overpass" ]
aliases = [ "/questions/50056" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass returns node's data with area's information that should not exist](/questions/50056/overpass-returns-nodes-data-with-areas-information-that-should-not-exist)

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
<span id="post-50056-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50056-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50056-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There is such village: <a href="http://www.openstreetmap.org/node/337512354">http://www.openstreetmap.org/node/337512354</a></p>
<p>I want to get all relationships of this village.<br />
In order to get it, I do request: <a href="http://overpass-api.de/api/interpreter?data=node(337512354);is_in;out;">http://overpass-api.de/api/interpreter?data=node(337512354);is_in;out;</a></p>
<p>In this file the top one area record shows:<br />
&lt;area id="2430719979"&gt;<br />
&lt;tag k="name" v="Пересіка"/&gt;<br />
&lt;tag k="place" v="village"/&gt;<br />
&lt;/area&gt;</p>
<p>The page of this area (way) is: <a href="http://www.openstreetmap.org/way/30719979">http://www.openstreetmap.org/way/30719979</a> As we can see, on this page there are no any tags at all.</p>
<p>My questions:<br />
1. Where\why does overpass take &lt;area id="2430719979"&gt; tag name\tag place &lt;/area&gt; from?<br />
2. How\where to fix this? (Remove this tags as this way should not have those tags)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jun '16, 08:14</strong></p>
<img src="https://secure.gravatar.com/avatar/1565cd50c70d1108a514e12877171c5f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bear_ukraine&#39;s gravatar image" />
<p><span>bear_ukraine</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bear_ukraine has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jun '16, 08:22</strong> </span></p>
</div>
</div>
<div id="comments-container-50056" class="comments-container">
&#10;</div>
<div id="comment-tools-50056" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50056-form-container" class="comment-form-container">
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

<span id="50060"></span>

<div id="answer-container-50060" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50060-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50060-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-50060-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="bear_ukraine has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Tags are not inherited from relation 6258680 to way 30719979.</p>
<p>This looks like a bug to me, as tags for areas and way are not consistent. That's even the case if I take the area creation timestamp as <code>[date:...]</code> value.</p>
<p>The issue is that way 30719979 used to be a valid way, but in the meantime, the way is just a line (rather than an area). The tags are retained from the last time, the way was still an area.</p>
<p><code>[date:"2016-05-06T05:51:02Z"];way(30719979);out geom meta;</code></p>
<p>Can you please file an issue on Github for it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '16, 09:26</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jun '16, 09:27</strong> </span></p>
</div>
</div>
<div id="comments-container-50060" class="comments-container">
&#10;</div>
<div id="comment-tools-50060" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50060-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="50058"></span>

<div id="answer-container-50058" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50058-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50058-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50058-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://www.openstreetmap.org/way/30719979">Way 30719979</a> is part of <a href="https://www.openstreetmap.org/relation/6258680">relation 6258680</a>. I guess that's where Overpass API is retrieving this information from.</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Areas">Areas</a> are an extension of Overpass API. They are constructed using the <a href="https://github.com/drolbr/Overpass-API/blob/master/rules/areas.osm3s">areas.osm3s</a> script. Since they don't exist in OSM there is no way for you to "fix" this. But if you think something is wrong with a generated area then you can create a <a href="https://github.com/drolbr/Overpass-API/issues">GitHub issue</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '16, 08:57</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span> </br></br></p>
</div>
</div>
<div id="comments-container-50058" class="comments-container">
&#10;</div>
<div id="comment-tools-50058" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50058-form-container" class="comment-form-container">
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

