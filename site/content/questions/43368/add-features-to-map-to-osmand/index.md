+++
type = "question"
title = "Add features to map to OSMand"
description = '''I would like to add a list of features (points) to OSMand that I need to survey on the ground. Steps I have managed so far:  I have got an extract (by clicking the GPX file link at http://robert.mathmos.net/osm/postboxes/2/map.html?lat=52.39322&amp;amp;lon=-1.62701&amp;amp;zoom=13&amp;amp;layers=TB0T )  Have co...'''
date = "2015-06-02T23:03:00Z"
lastmod = "2015-06-07T23:06:00Z"
weight = 43368
keywords = [ "gpx", "android", "osmand", "waypoints", "ios" ]
aliases = [ "/questions/43368" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Add features to map to OSMand](/questions/43368/add-features-to-map-to-osmand)

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
<span id="post-43368-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43368-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-43368-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to add a list of features (points) to OSMand that I need to survey on the ground. Steps I have managed so far:</p>
<ol>
<li>I have got an extract (by clicking the GPX file link at <a href="http://robert.mathmos.net/osm/postboxes/2/map.html?lat=52.39322&amp;lon=-1.62701&amp;zoom=13&amp;layers=TB0T">http://robert.mathmos.net/osm/postboxes/2/map.html?lat=52.39322&amp;lon=-1.62701&amp;zoom=13&amp;layers=TB0T</a> )</li>
<li>Have copied this to /osmand/tracks on the phone</li>
<li>Have got the GPS "track" to show.</li>
</ol>
<p>My issue is that all features appear the same in OSMand and clicking on each one only brings up the waypoint name (some useless ID).</p>
<p>What I would ideally like is to be able to view each waypoint in a different colour depending on its status (see link above). Is this possible? If not then is there some other way to achieve a similar effect.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-osmand" rel="tag" title="see questions tagged &#39;osmand&#39;">osmand</span> <span class="post-tag tag-link-waypoints" rel="tag" title="see questions tagged &#39;waypoints&#39;">waypoints</span> <span class="post-tag tag-link-ios" rel="tag" title="see questions tagged &#39;ios&#39;">ios</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Jun '15, 23:03</strong></p>
<img src="https://secure.gravatar.com/avatar/132b767a2673eaf42f00ceaa141a619c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RobJN&#39;s gravatar image" />
<p><span>RobJN</span><br />
<span class="score" title="160 reputation points">160</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RobJN has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-43368" class="comments-container">
<span id="43369"></span>
<div id="comment-43369" class="comment">
<div id="post-43369-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I used text wrangler to replace the &lt;/name&gt; &lt;cmt&gt; with a space and then the &lt;/cmt&gt; with &lt;/name&gt; from your boxes.gpx</p>
<p>From this...<br />
&lt;wpt lat="52.411469959414" lon="-1.67507208439022"&gt; &lt;name&gt;PB-014&lt;/name&gt; &lt;cmt&gt;Missing OSM Box&lt;/cmt&gt; &lt;sym&gt;Post Office&lt;/sym&gt; &lt;/wpt&gt;</p>
<p>to give this at each waypoint ...<br />
&lt;wpt lat="52.411469959414" lon="-1.67507208439022"&gt; &lt;name&gt;PB-014 Missing OSM Box &lt;/name&gt; &lt;sym&gt;Post Office&lt;/sym&gt; &lt;/wpt&gt;</p>
<p>and you can copy it from <a href="https://www.dropbox.com/s/0y3higaej9eztlr/boxes2.gpx?dl=0">https://www.dropbox.com/s/0y3higaej9eztlr/boxes2.gpx?dl=0</a></p>
<p>This may work for you.</p>
</div>
<div id="comment-43369-info" class="comment-info">
<span class="comment-age">(03 Jun '15, 01:44)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="43457"></span>
<div id="comment-43457" class="comment">
<div id="post-43457-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Editing the text file seems like the best approach for now. I don't want to add a load of Notes as this could get very cluttered very quickly.</p>
</div>
<div id="comment-43457-info" class="comment-info">
<span class="comment-age">(07 Jun '15, 23:06)</span> <span class="comment-user userinfo">RobJN</span>
</div>
</div>
</div>
<div id="comment-tools-43368" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43368-form-container" class="comment-form-container">
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

<span id="43383"></span>

<div id="answer-container-43383" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-43383-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-43383-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-43383-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Use the notes feature. As far as I can recall, OSMand pulls in open notes</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Jun '15, 18:26</strong></p>
<img src="https://secure.gravatar.com/avatar/9f0faef4659de616c82f448ff3f4e8e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaCor&#39;s gravatar image" />
<p><span>DaCor</span><br />
<span class="score" title="1339 reputation points"><span>1.3k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaCor has one accepted answer">2%</span> </br></br></p>
</div>
</div>
<div id="comments-container-43383" class="comments-container">
<span id="43385"></span>
<div id="comment-43385" class="comment">
<div id="post-43385-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It does after activating the corresponding notes plugin.</p>
</div>
<div id="comment-43385-info" class="comment-info">
<span class="comment-age">(03 Jun '15, 19:37)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-43383" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-43383-form-container" class="comment-form-container">
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

