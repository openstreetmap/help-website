+++
type = "question"
title = "Nominatim - returning road type to figure out max road speed"
description = '''I&#x27;m using nominatim to get max road speed If the data is not present (only around 10% is), I can guess the roadspeed based on road type i.e. in the UK, if its a residential road, it will be 30mph, and if its a motorway it will be 70mph However the data returned does not indicate the road type,  I ge...'''
date = "2018-10-08T08:22:00Z"
lastmod = "2018-10-08T15:22:00Z"
weight = 66203
keywords = [ "roadtype", "maxspeed", "osm_type", "nominatim" ]
aliases = [ "/questions/66203" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim - returning road type to figure out max road speed](/questions/66203/nominatim-returning-road-type-to-figure-out-max-road-speed)

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
<span id="post-66203-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66203-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66203-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm using nominatim to get max road speed</p>
<p>If the data is not present (only around 10% is), I can guess the roadspeed based on road type</p>
<p>i.e. in the UK, if its a residential road, it will be 30mph, and if its a motorway it will be 70mph</p>
<p>However the data returned does not indicate the road type, I get a OSM_TYPE of WAY, but that's it.</p>
<p>Is the above possible? if so how can i alter my call to return this info?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-roadtype" rel="tag" title="see questions tagged &#39;roadtype&#39;">roadtype</span> <span class="post-tag tag-link-maxspeed" rel="tag" title="see questions tagged &#39;maxspeed&#39;">maxspeed</span> <span class="post-tag tag-link-osm_type" rel="tag" title="see questions tagged &#39;osm_type&#39;">osm_type</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Oct '18, 08:22</strong></p>
<img src="https://secure.gravatar.com/avatar/629c67b24fafaf747f4410cfbc7f1fc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mark%20Davies1664&#39;s gravatar image" />
<p><span>Mark Davies1664</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mark Davies1664 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Oct '18, 08:23</strong> </span></p>
</div>
</div>
<div id="comments-container-66203" class="comments-container">
<span id="66204"></span>
<div id="comment-66204" class="comment">
<div id="post-66204-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Nominatim seems like an odd choice to get max road speed?</p>
</div>
<div id="comment-66204-info" class="comment-info">
<span class="comment-age">(08 Oct '18, 08:58)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="66205"></span>
<div id="comment-66205" class="comment">
<div id="post-66205-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Can you give an example query that does not tell you the road type when you expected it to do so?</p>
</div>
<div id="comment-66205-info" class="comment-info">
<span class="comment-age">(08 Oct '18, 08:59)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="66206"></span>
<div id="comment-66206" class="comment">
<div id="post-66206-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm using it to get the road name and roadspeed as one call Here is an example of one</p>
<p>{"place_id":"70381573","licence":"Data © OpenStreetMap contributors, ODbL 1.0. https:\/\/osm.org\/copyright", "osm_type":"way", "osm_id":"4968823", "lat":"51.51465608749", "lon":"-3.1915241864833", "display_name":"Heathwood Road, Heath, Cardiff, Wales, CF, UK","address": {"road":"Heathwood Road", "suburb":"Heath", "city":"Cardiff", "county":"Cardiff", "state":"Wales", "postcode":"CF", "country":"UK", "country_code":"gb"}, "extratags":{"foot":"yes", "lanes":"2", "oneway":"no", "surface":"asphalt", "maxspeed":"30 mph"}, "boundingbox":["51.5115152","51.516782","-3.1997308","-3.1860733"]}</p>
</div>
<div id="comment-66206-info" class="comment-info">
<span class="comment-age">(08 Oct '18, 09:25)</span> <span class="comment-user userinfo">Mark Davies1664</span>
</div>
</div>
<span id="66207"></span>
<div id="comment-66207" class="comment">
<div id="post-66207-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Which query led to this result - did you do a "search.php?q=Heathwood Road, Cardiff" or rather a "reverse.php?lat=51.514656&amp;lon=-3.191524" or...? Please specify exact URL as it might be relevant for finding the problem.</p>
</div>
<div id="comment-66207-info" class="comment-info">
<span class="comment-age">(08 Oct '18, 09:37)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="66212"></span>
<div id="comment-66212" class="comment">
<div id="post-66212-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Its Reverse and JSON Here is an example <a href="http://myurl.com/nominatim/reverse?format=json&amp;lat=51.51465608749&amp;lon=-3.1915241864833&amp;zoom=18&amp;addressdetails=1&amp;extratags=1">http://myurl.com/nominatim/reverse?format=json&amp;lat=51.51465608749&amp;lon=-3.1915241864833&amp;zoom=18&amp;addressdetails=1&amp;extratags=1</a></p>
</div>
<div id="comment-66212-info" class="comment-info">
<span class="comment-age">(08 Oct '18, 12:34)</span> <span class="comment-user userinfo">Mark Davies1664</span>
</div>
</div>
</div>
<div id="comment-tools-66203" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66203-form-container" class="comment-form-container">
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

<span id="66213"></span>

<div id="answer-container-66213" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66213-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66213-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66213-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Mark Davies1664 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Building up on what Frederik said. Use format=jsonv2, then you'll see a field 'category' and 'type'. Example <a href="https://nominatim.openstreetmap.org/reverse?format=jsonv2&amp;lat=51.51465608749&amp;lon=-3.1915241864833&amp;zoom=18&amp;addressdetails=1&amp;extratags=1">https://nominatim.openstreetmap.org/reverse?format=jsonv2&amp;lat=51.51465608749&amp;lon=-3.1915241864833&amp;zoom=18&amp;addressdetails=1&amp;extratags=1</a> shows 'category=highway', 'type=tertiary' which is equivalent to 'highway=tertiary' in <a href="https://www.openstreetmap.org/way/4968823">https://www.openstreetmap.org/way/4968823</a></p>
<p>Same for forward search <a href="https://nominatim.openstreetmap.org/search?format=jsonv2&amp;q=Heathwood%20Road,%20Cardiff&amp;addressdetails=1&amp;extratags=1">https://nominatim.openstreetmap.org/search?format=jsonv2&amp;q=Heathwood%20Road,%20Cardiff&amp;addressdetails=1&amp;extratags=1</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Oct '18, 12:44</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-66213" class="comments-container">
<span id="66215"></span>
<div id="comment-66215" class="comment">
<div id="post-66215-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>great thanks So in the UK i can assume tertiary and residential are both 30mph, and highway is 70mph</p>
<p>I guess primary, secondary etc are a bit harder to classify so i can leave these as unknown ?</p>
</div>
<div id="comment-66215-info" class="comment-info">
<span class="comment-age">(08 Oct '18, 13:57)</span> <span class="comment-user userinfo">Mark Davies1664</span>
</div>
</div>
<span id="66218"></span>
<div id="comment-66218" class="comment">
<div id="post-66218-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Probably. And there might be limits if it's inside or outside a city boundary. maxspeed is complex <a href="https://wiki.openstreetmap.org/wiki/Talk:Key:maxspeed">https://wiki.openstreetmap.org/wiki/Talk:Key:maxspeed</a> and I'd check if there was previous discussion on <a href="https://lists.openstreetmap.org/listinfo/talk-gb">https://lists.openstreetmap.org/listinfo/talk-gb</a> (or start a new one)</p>
</div>
<div id="comment-66218-info" class="comment-info">
<span class="comment-age">(08 Oct '18, 15:22)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-66213" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66213-form-container" class="comment-form-container">
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

