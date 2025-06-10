+++
type = "question"
title = "[closed] Netatmo weather station elevation error"
description = '''I have a Netatmo Weather Station that references OSM for its location and hence elevation. The elevation ex OSM is reflecting as 867m when in fact it is 1240m. How do I correct this?'''
date = "2020-01-07T07:22:00Z"
lastmod = "2020-01-07T10:02:00Z"
weight = 72390
keywords = [ "netatmo", "elevation" ]
aliases = [ "/questions/72390" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Netatmo weather station elevation error](/questions/72390/netatmo-weather-station-elevation-error)

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
<span id="post-72390-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72390-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72390-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a Netatmo Weather Station that references OSM for its location and hence elevation.</p>
<p>The elevation ex OSM is reflecting as 867m when in fact it is 1240m.</p>
<p>How do I correct this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-netatmo" rel="tag" title="see questions tagged &#39;netatmo&#39;">netatmo</span> <span class="post-tag tag-link-elevation" rel="tag" title="see questions tagged &#39;elevation&#39;">elevation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jan '20, 07:22</strong></p>
<img src="https://secure.gravatar.com/avatar/55f3d34f90f432c047effdb5e31a137a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Steve%20Lovemore&#39;s gravatar image" />
<p><span>Steve Lovemore</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Steve Lovemore has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>07 Jan '20, 10:30</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span></p>
</div>
</div>
<div id="comments-container-72390" class="comments-container">
<span id="72392"></span>
<div id="comment-72392" class="comment">
<div id="post-72392-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OSM itself does not store elevation information except for a few landmarks (summits etc.). There are service providers that overlay OSM data with elevation data. I assume there is such service provider (or Netatmo themselves) providing the elevation data for your weather station and you should contact them for any questions.</p>
<p>But to double check there is indeed no elevation data in our database: Could you please pinpoint the exact location where you get the wrong reading?</p>
</div>
<div id="comment-72392-info" class="comment-info">
<span class="comment-age">(07 Jan '20, 08:40)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="72393"></span>
<div id="comment-72393" class="comment">
<div id="post-72393-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The location is 31°58'04.0"S 22°48'02.8"E.</p>
<p>If you look at the layer OpenTopoMap you can see that elevation at this point is approx 1240m</p>
</div>
<div id="comment-72393-info" class="comment-info">
<span class="comment-age">(07 Jan '20, 09:20)</span> <span class="comment-user userinfo">Steve Lovemore</span>
</div>
</div>
<span id="72394"></span>
<div id="comment-72394" class="comment">
<div id="post-72394-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't see anything in the OSM data in that vicinity that could create the false elevation reading. Please contact Netatmo where the elevation information is coming from.</p>
<p>Are you sure the location is correct in the device? Does it have GPS?</p>
</div>
<div id="comment-72394-info" class="comment-info">
<span class="comment-age">(07 Jan '20, 09:56)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="72395"></span>
<div id="comment-72395" class="comment">
<div id="post-72395-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The location is definitely accurate to within 50m - I can see its location on the map.</p>
<p>I will contact Netatmo thanks</p>
</div>
<div id="comment-72395-info" class="comment-info">
<span class="comment-age">(07 Jan '20, 10:02)</span> <span class="comment-user userinfo">Steve Lovemore</span>
</div>
</div>
</div>
<div id="comment-tools-72390" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72390-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Not an OpenStreetMap issue" by Richard 07 Jan '20, 10:30

</div>

</div>

</div>

