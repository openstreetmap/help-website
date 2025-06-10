+++
type = "question"
title = "How to get the element id for a given GPS coordinate?"
description = '''I have a lot of GPS coordinates. How can I find the respective element id according the GPS data? (I can not use the webpage and per the mouse click on the query button, since I have too many points...)  For example: Given this GPS coordinate: [51.645401, 12.052744] Return the element id: farmland #...'''
date = "2017-02-09T16:12:00Z"
lastmod = "2017-02-10T13:32:00Z"
weight = 54570
keywords = [ "elements" ]
aliases = [ "/questions/54570" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to get the element id for a given GPS coordinate?](/questions/54570/how-to-get-the-element-id-for-a-given-gps-coordinate)

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
<span id="post-54570-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54570-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54570-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a lot of GPS coordinates. How can I find the respective element id according the GPS data? (I can not use the webpage and per the mouse click on the query button, since I have too many points...)</p>
<p>For example:</p>
<p>Given this GPS coordinate: [51.645401, 12.052744]</p>
<p>Return the element id: farmland #6249468</p>
<p>How can I do that?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-elements" rel="tag" title="see questions tagged &#39;elements&#39;">elements</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Feb '17, 16:12</strong></p>
<img src="https://secure.gravatar.com/avatar/ad034953750232b32ac9fdbe894c33db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xirururu&#39;s gravatar image" />
<p><span>xirururu</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xirururu has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Feb '17, 18:12</strong> </span></p>
</div>
</div>
<div id="comments-container-54570" class="comments-container">
&#10;</div>
<div id="comment-tools-54570" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54570-form-container" class="comment-form-container">
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

<span id="54579"></span>

<div id="answer-container-54579" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54579-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54579-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-54579-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="xirururu has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The query button on the website is implemented using a publicly available service, Overpass-API:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Overpass_API">http://wiki.openstreetmap.org/wiki/Overpass_API</a></p>
<p>There is some discussion of it in the website code:</p>
<p><a href="https://github.com/openstreetmap/openstreetmap-website/blob/e3357b27e61c3ee4f4cf51c87fdc94deeaaa7c6f/app/assets/javascripts/index/query.js#L262">https://github.com/openstreetmap/openstreetmap-website/blob/e3357b27e61c3ee4f4cf51c87fdc94deeaaa7c6f/app/assets/javascripts/index/query.js#L262</a></p>
<p>(the query language used there is documented at <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL">http://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL</a> )</p>
<p>You can experiment with Overpass-API using a convenient gui at Overpass Turbo:</p>
<p><a href="http://overpass-turbo.eu/s/mC9">http://overpass-turbo.eu/s/mC9</a></p>
<p>I've only added a piece of the query there, the is_in operator returns a subset of nearby objects, you'd need to add the around operators and experiment a bit to see if the output is useful for what you need.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Feb '17, 23:52</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-54579" class="comments-container">
<span id="54582"></span>
<div id="comment-54582" class="comment">
<div id="post-54582-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/10973/maxerickson"></a><a href="http://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a> Thanks so much for the answer! Run your is_in() function works perfectly. But how can I write the nearby function? According your query.js file, I made the nearby function. But it doesn't work.</p>
<p>(node(around:100, 51.645401, 12.052744); way(around:100, 51.645401, 12.052744));</p>
<p>out tags;</p>
<p>relation(around:10, 51.645401, 12.052744); out;</p>
<p>Here is my code in overpass-turbo</p>
<p><a href="http://overpass-turbo.eu/s/mCa">http://overpass-turbo.eu/s/mCa</a></p>
</div>
<div id="comment-54582-info" class="comment-info">
<span class="comment-age">(10 Feb '17, 01:34)</span> <span class="comment-user userinfo">xirururu</span>
</div>
</div>
<span id="54583"></span>
<div id="comment-54583" class="comment">
<div id="post-54583-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There are no features within the 100 meter radius. Increasing it returns some features (200 works for nodes).</p>
<p>Also get rid of the <code>tags</code> from the output statement. That removes the geographic information from the results. <code>out geom</code> will add geographic information for ways and relations.</p>
<p><a href="http://overpass-turbo.eu/s/mCd">http://overpass-turbo.eu/s/mCd</a></p>
</div>
<div id="comment-54583-info" class="comment-info">
<span class="comment-age">(10 Feb '17, 03:12)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="54586"></span>
<div id="comment-54586" class="comment">
<div id="post-54586-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a> Thanks! I still have a little doubt, The gps point [51.645401, 12.052744] is actually in the "Farmland #6249468", but why it returned as a nearby feature?</p>
</div>
<div id="comment-54586-info" class="comment-info">
<span class="comment-age">(10 Feb '17, 10:56)</span> <span class="comment-user userinfo">xirururu</span>
</div>
</div>
<span id="54590"></span>
<div id="comment-54590" class="comment">
<div id="post-54590-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The areas that the is_in operator returns are generated by Overpass API using a set of rules. For landuse types (and most other features), they are only included as areas if they have a name.</p>
<p>The rules are here: <a href="https://github.com/drolbr/Overpass-API/blob/master/src/rules/areas.osm3s">https://github.com/drolbr/Overpass-API/blob/master/src/rules/areas.osm3s</a></p>
</div>
<div id="comment-54590-info" class="comment-info">
<span class="comment-age">(10 Feb '17, 13:32)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-54579" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54579-form-container" class="comment-form-container">
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

