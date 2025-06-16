+++
type = "question"
title = "[closed] Check if the a person has entered a train station"
description = '''Thanks, had a good look and found the following query helped me to get the result for the train station EAST CROYDON. node[&quot;name&quot;=&quot;East Croydon&quot;]&quot;train&quot;=&quot;yes&quot;; &quot;type&quot;: &quot;node&quot;, &quot;id&quot;: 302042289, &quot;lat&quot;: 51.3758448, &quot;lon&quot;: -0.0927317, &quot;tags&quot;: { &quot;electrified&quot;: &quot;rail&quot;, &quot;name&quot;: &quot;East Croydon&quot;, &quot;naptan:Atco...'''
date = "2016-10-12T22:45:00Z"
lastmod = "2016-10-12T22:48:00Z"
weight = 52504
keywords = [ "overpass", "railway" ]
aliases = [ "/questions/52504" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Check if the a person has entered a train station](/questions/52504/check-if-the-a-person-has-entered-a-train-station)

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
<span id="post-52504-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52504-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-52504-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Thanks, had a good look and found the following query helped me to get the result for the train station EAST CROYDON.</p>
<p>node["name"="East Croydon"]"train"="yes"; "type": "node", "id": 302042289, "lat": 51.3758448, "lon": -0.0927317, "tags": { "electrified": "rail", "name": "East Croydon", "naptan:AtcoCode": "9100ECROYDN", "network": "National Rail", "platforms": "6", "postal_code": "CR0 1LF", "public_transport": "station", "railway": "station", "ref": "ECR", "source_ref": "http://en.wikipedia.org/wiki/List_of_London_railway_stations", "toilets:wheelchair": "yes", "train": "yes", "website": "http://www.nationalrail.co.uk/stations/ecr/details.html", "wheelchair": "yes", "wikipedia": "en:East Croydon station" } }, { "type": "node", "id": 676877753, "lat": 51.3760143, "lon": -0.0923223, "tags": { "name": "East Croydon", "public_transport": "stop_position", "train": "yes" } }, + 4 more stop_position sections this had 6 records which includes different platform points (log and lat) with in the station</p>
<p>But for me to identify the user within the railway station I need to cover the area of the whole east croydon station (land and building) the person can be anywhere here, how can i find the bounding box of the whole station so that i can then check if the person with X and Y is within the station?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-railway" rel="tag" title="see questions tagged &#39;railway&#39;">railway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Oct '16, 22:45</strong></p>
<img src="https://secure.gravatar.com/avatar/24f9ddfbc116657dafd9c60b67801a4a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="brightnlight&#39;s gravatar image" />
<p><span>brightnlight</span><br />
<span class="score" title="10 reputation points">10</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="brightnlight has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>12 Oct '16, 23:08</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-52504" class="comments-container">
<span id="52505"></span>
<div id="comment-52505" class="comment">
<div id="post-52505-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Is this not exactly the same as <a href="/questions/52402/how-to-find-out-if-a-person-has-entered-a-train-station">https://help.openstreetmap.org/questions/52402/how-to-find-out-if-a-person-has-entered-a-train-station</a> ?</p>
</div>
<div id="comment-52505-info" class="comment-info">
<span class="comment-age">(12 Oct '16, 22:48)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-52504" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52504-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question" by aseerel4c26 12 Oct '16, 23:08

</div>

</div>

</div>

