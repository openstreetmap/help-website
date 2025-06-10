+++
type = "question"
title = "The best way to extract street list"
description = '''Hi,  I am in a need to extract a street list of a given city in a csv format, with some lon/lat data, to focus on the map on the street, when a person is searching it in the app. What is the easyest way/tool to make it?'''
date = "2012-01-05T11:10:00Z"
lastmod = "2020-03-17T10:27:00Z"
weight = 9816
keywords = [ "extract", "street", "osm" ]
aliases = [ "/questions/9816" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [The best way to extract street list](/questions/9816/the-best-way-to-extract-street-list)

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
<span id="post-9816-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9816-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-9816-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
3
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am in a need to extract a street list of a given city in a csv format, with some lon/lat data, to focus on the map on the street, when a person is searching it in the app. What is the easyest way/tool to make it?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jan '12, 11:10</strong></p>
<img src="https://secure.gravatar.com/avatar/d5392fe7a68088f8c8e3bdc43a16f156?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gevork&#39;s gravatar image" />
<p><span>Gevork</span><br />
<span class="score" title="234 reputation points">234</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gevork has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-9816" class="comments-container">
&#10;</div>
<div id="comment-tools-9816" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9816-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="16248"></span>

<div id="answer-container-16248" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16248-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16248-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-16248-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="https://wiki.openstreetmap.org/wiki/Osmconvert#Writing_CSV_Files">CSV option of osmconvert</a> will help you generating the required list.</p>
<p>First, use osmfilter with <code>--keep="highway=residential =primary =secondary =tertiaty =unclassified"</code>, etc., to get all streets, then use osmconvert with <code>--all-to-nodes</code> and <code>--csv="</code><span><code>@lon</code></span><code> @lat name etc."</code> to get the CSV list.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Sep '12, 00:20</strong></p>
<img src="https://secure.gravatar.com/avatar/3b5b4abfedd46928c7cd0d5cbf907ed3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marqqs&#39;s gravatar image" />
<p><span>Marqqs</span><br />
<span class="score" title="448 reputation points">448</span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marqqs has 2 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Sep '12, 00:24</strong> </span></p>
</div>
</div>
<div id="comments-container-16248" class="comments-container">
<span id="73574"></span>
<div id="comment-73574" class="comment">
<div id="post-73574-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>it should be <code>=tertiary</code> not <code>=tertiaty</code></p>
</div>
<div id="comment-73574-info" class="comment-info">
<span class="comment-age">(17 Mar '20, 10:27)</span> <span class="comment-user userinfo">dsaket</span>
</div>
</div>
</div>
<div id="comment-tools-16248" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16248-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33653"></span>

<div id="answer-container-33653" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33653-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33653-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-33653-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>osmfilter city.osm --keep="addr:country= and addr:city= and addr:street=" --ignore-depemdencies --drop-relations --drop-ways |osmconvert - --csv="@oname <span>@id</span> <span>@lon</span> <span>@lat</span> addr:country addr:city addr:street"</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jun '14, 00:17</strong></p>
<img src="https://secure.gravatar.com/avatar/d5392fe7a68088f8c8e3bdc43a16f156?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gevork&#39;s gravatar image" />
<p><span>Gevork</span><br />
<span class="score" title="234 reputation points">234</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gevork has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33653" class="comments-container">
<span id="52309"></span>
<div id="comment-52309" class="comment">
<div id="post-52309-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. I used your command line and it worked but it doesn't show all the streets.</p>
<p>I am working on Spain map data.[1] I did this:</p>
<ul>
<li>osmconvert spain-latest.osm.pbf -o=spain-latest.osm.o5m</li>
<li>osmfilter spain-latest.osm.o5m --keep="addr:country= and addr:city= and addr:street=" --ignore-depemdencies --drop-relations --drop-ways | osmconvert - --csv="@oname <a href="http://help.openstreetmap.org/users/260/idoneus"></a><a href="http://help.openstreetmap.org/users/260/idoneus">@id</a> <a href="http://help.openstreetmap.org/users/1350/longestaugust"></a><a href="http://help.openstreetmap.org/users/1350/longestaugust">@lon</a> <a href="http://help.openstreetmap.org/users/5110/latroc"></a><a href="http://help.openstreetmap.org/users/5110/latroc">@lat</a> addr:country addr:city addr:street"</li>
</ul>
<p>And it shows 135444 results, including duplicates. Then I grep a municipality like "Jerez de la Frontera":</p>
<ul>
<li>osmfilter spain-latest.osm.o5m --keep="addr:country= and addr:city= and addr:street=" --ignore-depemdencies --drop-relations --drop-ways | osmconvert - --csv="@oname <a href="http://help.openstreetmap.org/users/260/idoneus"></a><a href="http://help.openstreetmap.org/users/260/idoneus">@id</a> <a href="http://help.openstreetmap.org/users/1350/longestaugust"></a><a href="http://help.openstreetmap.org/users/1350/longestaugust">@lon</a> <a href="http://help.openstreetmap.org/users/5110/latroc"></a><a href="http://help.openstreetmap.org/users/5110/latroc">@lat</a> addr:country addr:city addr:street" | cut -f6-7 | grep "Jerez de la Frontera" | sort | uniq</li>
</ul>
<p>And it shows only 2 streets, which is obvious wrong:</p>
<p>Jerez de la Frontera Calle Perú Jerez de la Frontera Matadero</p>
<p>That municipality has names for many streets in OpenStreetMap.</p>
<p><a href="https://www.openstreetmap.org/relation/342097#map=14/36.6805/-6.1285">https://www.openstreetmap.org/relation/342097#map=14/36.6805/-6.1285</a></p>
<p>What is the problem? Thank you.</p>
<p>[1] <a href="http://download.geofabrik.de/europe/spain.html">http://download.geofabrik.de/europe/spain.html</a></p>
</div>
<div id="comment-52309-info" class="comment-info">
<span class="comment-age">(30 Sep '16, 12:46)</span> <span class="comment-user userinfo">emijrp</span>
</div>
</div>
<span id="73573"></span>
<div id="comment-73573" class="comment">
<div id="post-73573-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>it's <code>--ignore-dependencies</code> guys.</p>
</div>
<div id="comment-73573-info" class="comment-info">
<span class="comment-age">(17 Mar '20, 10:19)</span> <span class="comment-user userinfo">dsaket</span>
</div>
</div>
</div>
<div id="comment-tools-33653" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33653-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="52310"></span>

<div id="answer-container-52310" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52310-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52310-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52310-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I reply to myself. It shows few streets because not all the streets have a defined "addr:city" parameter.</p>
<p>So I used this solution:</p>
<ul>
<li>Download the .pbf for your country <a href="http://download.geofabrik.de">http://download.geofabrik.de</a></li>
<li>Download the polygon file for the desired municipality from <a href="https://github.com/JamesChevalier/cities">https://github.com/JamesChevalier/cities</a></li>
<li>Do this: osmosis --read-pbf-fast spain-latest.osm.pbf file="spain-latest.osm.pbf" --bounding-polygon file="cadiz.poly" --write-xml file="cadiz.osm"</li>
</ul>
<p>Now you have a .osm file for the municipality. Inside it is all the information (streets, buildings, monuments, etc) for that city.</p>
<p>You can use osmfilter or grep to extract the info your want.</p>
<p>Regards</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Sep '16, 14:42</strong></p>
<img src="https://secure.gravatar.com/avatar/eb5dfc0e7013baf4643a8d81e1b7d214?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emijrp&#39;s gravatar image" />
<p><span>emijrp</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emijrp has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Oct '16, 00:36</strong> </span></p>
</div>
</div>
<div id="comments-container-52310" class="comments-container">
&#10;</div>
<div id="comment-tools-52310" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52310-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="9826"></span>

<div id="answer-container-9826" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-9826-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-9826-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-9826-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://maposmatic.org/">Maposmatic</a> will give you a csv of the streets, but it shows a local grid reference instead of an exact lat-long. Maybe you can reverse that reference to get the approximate lat/lon, since you know the bounding box and the size of the grid ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jan '12, 12:08</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-9826" class="comments-container">
<span id="9895"></span>
<div id="comment-9895" class="comment">
<div id="post-9895-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Vincent</span>-de-phily Thank you, but it's not an easy way...</p>
</div>
<div id="comment-9895-info" class="comment-info">
<span class="comment-age">(11 Jan '12, 11:17)</span> <span class="comment-user userinfo">Gevork</span>
</div>
</div>
</div>
<div id="comment-tools-9826" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-9826-form-container" class="comment-form-container">
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

