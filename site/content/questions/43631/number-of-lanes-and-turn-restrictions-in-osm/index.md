+++
type = "question"
title = "Number of lanes and turn restrictions in OSM"
description = '''I&#x27;m having some trouble with extracting the number of lanes and appropriate turn restrictions in OSM. Take for example Penn Avenue, at the intersection with Center Avenue in Pittsburgh. On the map you clearly see a purple road with a dotted center line which indicates multiple lanes. Yet in the data...'''
date = "2015-06-19T06:29:00Z"
lastmod = "2015-06-20T16:34:00Z"
weight = 43631
keywords = [ "lanes", "turn_restrictions" ]
aliases = [ "/questions/43631" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Number of lanes and turn restrictions in OSM](/questions/43631/number-of-lanes-and-turn-restrictions-in-osm)

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
<span id="post-43631-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43631-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43631-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm having some trouble with extracting the number of lanes and appropriate turn restrictions in OSM. Take for example <a href="https://www.openstreetmap.org/way/54460235#map=19/40.46047/-79.92243">Penn Avenue</a>, at the intersection with Center Avenue in Pittsburgh. On the map you clearly see a purple road with a dotted center line which indicates multiple lanes. Yet in the data, there is no "lanes" tag. How can I get the number of lanes for this particular street? If it's not in OSM, is there some external source where I might be able to get this kind of data?</p>
<p><strong>Update</strong>: Here is a screenshot of that particular intersection from Google maps satelite: <img src="/upfiles/pennAve_CenterAve.png" width="800" height="400" /> When coming from the street at the bottom left (Center ave), there are 2 lanes: one to go straight and one to go right. It is prohibited to turn left onto Penn Ave. The street from the top left to bottom right is Penn ave. As you can see, there are multiple lanes as well. When I export the OSM data for this intersection, there seems to be no information about the number of lanes, nor is there any information on the turn restrictions?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-lanes" rel="tag" title="see questions tagged &#39;lanes&#39;">lanes</span> <span class="post-tag tag-link-turn_restrictions" rel="tag" title="see questions tagged &#39;turn_restrictions&#39;">turn_restrictions</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jun '15, 06:29</strong></p>
<img src="https://secure.gravatar.com/avatar/6feb1ed05cdbdc6c0d788f514fd07e1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JorisK&#39;s gravatar image" />
<p><span>JorisK</span><br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JorisK has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jun '15, 16:32</strong> </span></p>
</div>
</div>
<div id="comments-container-43631" class="comments-container">
&#10;</div>
<div id="comment-tools-43631" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43631-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="43634"></span>

<div id="answer-container-43634" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43634-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43634-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-43634-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>On the map you clearly see a purple road with a dotted center line which indicates multiple lanes</p>
</blockquote>
<p>Are you sure about that? I'm pretty sure that dotted purple lines represent administrative boundaries (countries/states/counites/etc.), and it looks like that road is in an administrative relation: <a href="https://www.openstreetmap.org/relation/3893364">https://www.openstreetmap.org/relation/3893364</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jun '15, 08:36</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-43634" class="comments-container">
<span id="43648"></span>
<div id="comment-43648" class="comment">
<div id="post-43648-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've updated my question with an image of that particular intersection. Hope this clarifies. Perhaps my interpretation of the 'dotted' line was wrong, but there are certainly multiple lanes and turn restrictions for this particular intersection. Yet I can't find information about this in the data.</p>
</div>
<div id="comment-43648-info" class="comment-info">
<span class="comment-age">(19 Jun '15, 16:34)</span> <span class="comment-user userinfo">JorisK</span>
</div>
</div>
<span id="43664"></span>
<div id="comment-43664" class="comment">
<div id="post-43664-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>It looks like no-one has added the lanes value to the OSM database. This is not unusual, ~97% of roads in OSM have no lane information. Perhaps you could map it yourself?</p>
</div>
<div id="comment-43664-info" class="comment-info">
<span class="comment-age">(20 Jun '15, 16:34)</span> <span class="comment-user userinfo">rorym</span>
</div>
</div>
</div>
<div id="comment-tools-43634" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43634-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43652"></span>

<div id="answer-container-43652" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43652-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43652-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-43652-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Like rorym said, the purple dotted line you see is <a href="https://www.openstreetmap.org/relation/3893364">this administrative boundary</a> for the Shadyside neighbourhood. While there may exist multiple lanes and turn restrictions in real life, those have not yet been represented in the OpenStreetMap data. Further, neither the number of lanes nor turn restrictions are currently rendered by the style used on that map, so they wouldn't be visible even if they were in the data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jun '15, 17:25</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-43652" class="comments-container">
&#10;</div>
<div id="comment-tools-43652" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43652-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="43649"></span>

<div id="answer-container-43649" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43649-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43649-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-43649-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>After being a bit familiar with OSM tagging schema for <a href="https://wiki.openstreetmap.org/wiki/Lanes">turn lanes</a> and <a href="https://wiki.openstreetmap.org/wiki/Relation:restriction">turn restrictions</a>, you can load that area for example in the offline editor <a href="https://wiki.openstreetmap.org/wiki/JOSM">JOSM</a>.</p>
<p>There you can see that right to this moment (maybe someone is adding tags in the next hours or days) thereis NO tagging about lanes, turn lanes and turn restrictions.</p>
<p>In JOSM there are symbols for turn restrictions, and there is a mappaint style for lanes, and turn lanes!</p>
<p>And I never came accross any legal data source with real data about lanes count and turn restriction for any area in the world.</p>
<p>So it is hard work to derive that real world information by own knowledge, or any webservice where we have the explicit permission to use for OSM purposes, like mapillary.com, <a href="https://wiki.openstreetmap.org/wiki/Aerial_imagery">Bing aerial photos or Mapbox aerial photos</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jun '15, 16:47</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-43649" class="comments-container">
&#10;</div>
<div id="comment-tools-43649" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43649-form-container" class="comment-form-container">
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

