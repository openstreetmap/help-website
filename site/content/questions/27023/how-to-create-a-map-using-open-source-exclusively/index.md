+++
type = "question"
title = "How to create a map using open source exclusively."
description = '''Dear Sir or Madam,  I have geocoded postal codes, and have longitude and latitude for each postal code. I would like to create a map of all these data points without using any Google, Bing, or any other commercial sources so as to be able to use it in a publication without violating copyrights. This...'''
date = "2013-10-08T20:05:00Z"
lastmod = "2013-10-18T10:04:00Z"
weight = 27023
keywords = [ "postalcode", "license", "display", "free" ]
aliases = [ "/questions/27023" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to create a map using open source exclusively.](/questions/27023/how-to-create-a-map-using-open-source-exclusively)

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
<span id="post-27023-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27023-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-27023-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear Sir or Madam, I have geocoded postal codes, and have longitude and latitude for each postal code. I would like to create a map of all these data points without using any Google, Bing, or any other commercial sources so as to be able to use it in a publication without violating copyrights. This geographic area I am concerned with is North West Poland.</p>
<p>I thank you in advance for any help. Peter</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postalcode" rel="tag" title="see questions tagged &#39;postalcode&#39;">postalcode</span> <span class="post-tag tag-link-license" rel="tag" title="see questions tagged &#39;license&#39;">license</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span> <span class="post-tag tag-link-free" rel="tag" title="see questions tagged &#39;free&#39;">free</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Oct '13, 20:05</strong></p>
<img src="https://secure.gravatar.com/avatar/5c95ee73363d2706c8373867e09eb1eb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PeterPK&#39;s gravatar image" />
<p><span>PeterPK</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PeterPK has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Oct '13, 17:12</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span></p>
</div>
</div>
<div id="comments-container-27023" class="comments-container">
&#10;</div>
<div id="comment-tools-27023" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27023-form-container" class="comment-form-container">
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

<span id="27029"></span>

<div id="answer-container-27029" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27029-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27029-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-27029-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are many ways to do this, depending on your needs and tastes. One way is to use <a href="http://switch2osm.org/using-tiles/getting-started-with-leaflet/">leaflet</a> with an OSM basemap, and your POIs in <a href="http://leafletjs.com/examples/geojson.html">geojson</a> format. Please be more specific if you have problems.</p>
<p>Speaking of geocoded postal codes, where did you get yours from ? If your source is <a href="http://www.openstreetmap.org/copyright">compatible with osm</a>, it would be advantageous to get the data into OSM :</p>
<ul>
<li>Many ready-made tools will allow you to query and display the data</li>
<li>Data will be much more widely available</li>
<li>It will be merged with existing data, forming a more complete set</li>
<li>Other OSM contributors will help curate the data</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Oct '13, 10:13</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-27029" class="comments-container">
<span id="27030"></span>
<div id="comment-27030" class="comment">
<div id="post-27030-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>If your data can be added to OSM, please contact the <a href="https://lists.openstreetmap.org/listinfo/talk-pl">OSM Talk Poland</a> mailing list and see the <a href="http://wiki.openstreetmap.org/wiki/Import/Guidelines">import guidelines</a>.</p>
</div>
<div id="comment-27030-info" class="comment-info">
<span class="comment-age">(09 Oct '13, 10:16)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="27084"></span>
<div id="comment-27084" class="comment">
<div id="post-27084-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for the answer. I used GPSVisualizer when they offered batch geocoding through their website using Yahoo before that service was taken over my Microsoft/Bing. I was able to enter the latitude and longitude co-ordinates and get a map using various sources of map data, including openstreetmap, but the Google logo is present on all maps created using GPSVisualizer regardless of the source of the map data. I am not sure if that is copyrighted by Google, or not. An example of the data I have is: 52.380041,16.92445,"61-531". The postal code is present after each set of co-ordinates. I would like to have the data publicly available as soon as the work I am doing is completed. Thank you, Peter</p>
</div>
<div id="comment-27084-info" class="comment-info">
<span class="comment-age">(10 Oct '13, 18:58)</span> <span class="comment-user userinfo">PeterPK</span>
</div>
</div>
<span id="27296"></span>
<div id="comment-27296" class="comment">
<div id="post-27296-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You seem to indicate that your data was derived from Yahoo. This would make in unsuitable for inclusion into OSM.</p>
</div>
<div id="comment-27296-info" class="comment-info">
<span class="comment-age">(18 Oct '13, 08:31)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="27297"></span>
<div id="comment-27297" class="comment">
<div id="post-27297-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So the way to go would probably be using leaflet or openlayers and your postcode information as GeoJSON. Also, just out of curiosity: Are postcodes used for areas? How do your point features map to postcode areas (or are those the postcodes for specific buildings?).</p>
</div>
<div id="comment-27297-info" class="comment-info">
<span class="comment-age">(18 Oct '13, 10:04)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
</div>
<div id="comment-tools-27029" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27029-form-container" class="comment-form-container">
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

