+++
type = "question"
title = "Osmium and overpass results do not match"
description = '''I have been trying to find the difference in the number of features of an area over a specific time period.  My workflow:  Download the full history file of the area of interest. Extracted two separate data files as of the starting and ending time period using osmium time-filter. Using osmium tags-c...'''
date = "2021-01-08T18:46:00Z"
lastmod = "2021-01-09T18:37:00Z"
weight = 78284
keywords = [ "osmium", "overpass" ]
aliases = [ "/questions/78284" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Osmium and overpass results do not match](/questions/78284/osmium-and-overpass-results-do-not-match)

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
<span id="post-78284-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78284-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78284-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been trying to find the difference in the number of features of an area over a specific time period.</p>
<p><strong>My workflow:</strong></p>
<ol>
<li>Download the full history file of the area of interest.</li>
<li>Extracted two separate data files as of the starting and ending time period using <em>osmium time-filter</em>.</li>
<li>Using <em>osmium tags-count</em>, counted the same feature (say amenity=hospital) from both files and subtracted them.</li>
</ol>
<p>The result is equivalent to the number of hospitals mapped in that region within that particular period. I cross-checked the number by applying the overpass query in the same area over the same period and clipped the data with my area of interest using QGIS.</p>
<hr />
<p><em>nwr["amenity"="hospital"] (if:timestamp()&gt;="2020-01-01T00:00:00Z" &amp;&amp; timestamp() &lt;="2020-02-01T00:00:00Z")({{bbox}});</em></p>
<hr />
<p>To my surprise, the numbers (difference) obtained from <em>osmium</em> and <em>overpass-turbo</em> were very different. My understanding is that these numbers should match.</p>
<p>Am I doing something wrong?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jan '21, 18:46</strong></p>
<img src="https://secure.gravatar.com/avatar/8eb4b1d144482efa17ccbfc0373c0606?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rabenojha&#39;s gravatar image" />
<p><span>rabenojha</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rabenojha has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78284" class="comments-container">
<span id="78287"></span>
<div id="comment-78287" class="comment">
<div id="post-78287-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'd cross check first by doing two date queries on overpass [date:"2020-01-01T00:00:00Z"] &amp; [date:"2020-01-01T00:00:00Z"] with your regular nwr<a href="%7B%7Bbbox%7D%7D">"amenity"="hospital"</a> query &amp; comparing those to your two osmium extracts. Not sure why you're clipping in QGIS rather than with Osmium.</p>
</div>
<div id="comment-78287-info" class="comment-info">
<span class="comment-age">(08 Jan '21, 19:48)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="78298"></span>
<div id="comment-78298" class="comment">
<div id="post-78298-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am talking about clipping the resulted file (exported as GeoJSON) obtained by the overpass query in the bounding box by my area of interest. But, if you are mentioning osmium-extract about clipping with Osmium, I am yet to explore that.</p>
</div>
<div id="comment-78298-info" class="comment-info">
<span class="comment-age">(09 Jan '21, 18:37)</span> <span class="comment-user userinfo">rabenojha</span>
</div>
</div>
</div>
<div id="comment-tools-78284" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78284-form-container" class="comment-form-container">
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

<span id="78295"></span>

<div id="answer-container-78295" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78295-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78295-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78295-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The two queries ask for different numbers. The Osmium query gives the number you want to know - how much did the number of hospitals change in the given time range.</p>
<p>The Overpass query asks how many hospitals have been last edited in the time range. I.e. if the object was edited later again, it is not counted. Likewise, if an old hospital object got updated in the period it is counted.</p>
<p>If you want to use Overpass (on a server that has the full history), you can use the 'date' modifier to access historic data, see <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Difference_between_two_dates_.28diff.29">Overpass Language Documentation</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jan '21, 13:46</strong></p>
<img src="https://secure.gravatar.com/avatar/9fbbc400eb10c1432ab84779b6f7e539?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mueschel&#39;s gravatar image" />
<p><span>mueschel</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mueschel has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jan '21, 13:49</strong> </span></p>
</div>
</div>
<div id="comments-container-78295" class="comments-container">
&#10;</div>
<div id="comment-tools-78295" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78295-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

