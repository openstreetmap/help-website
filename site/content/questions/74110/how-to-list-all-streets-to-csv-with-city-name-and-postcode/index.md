+++
type = "question"
title = "How to list all streets to CSV with city name and postcode?"
description = '''Hi, I try to create a CSV file with street names, postcodes and city names: wget https://download.geofabrik.de/europe/hungary-latest.osm.pbf osmconvert hungary-latest.osm.pbf -o=hun.o5m osmfilter hun.o5m --keep=&quot;addr:postcode=* addr:country= addr:city= addr:street= highway=cycleway highway=path high...'''
date = "2020-04-12T14:48:00Z"
lastmod = "2020-04-14T09:10:00Z"
weight = 74110
keywords = [ "osmfilter", "street", "streetnames", "residential", "address" ]
aliases = [ "/questions/74110" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to list all streets to CSV with city name and postcode?](/questions/74110/how-to-list-all-streets-to-csv-with-city-name-and-postcode)

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
<span id="post-74110-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74110-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74110-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I try to create a CSV file with street names, postcodes and city names:</p>
<pre><code>wget https://download.geofabrik.de/europe/hungary-latest.osm.pbf
osmconvert hungary-latest.osm.pbf -o=hun.o5m
osmfilter hun.o5m --keep=&quot;addr:postcode=* addr:country= addr:city= addr:street= highway=cycleway highway=path highway=primary highway=residential highway=tertiary&quot; | osmconvert - --csv=&quot;name addr:postcode addr:city addr:street&quot; --csv-separator=&quot;,&quot; &gt; hun_streets.csv</code></pre>
<p>A useful output would be like this (postcode, city, street) that is present in the CSV:</p>
<pre><code>2941,Ács,Posta köz</code></pre>
<p><strong>However, "Posta köz" is listed in an incomplete way:</strong></p>
<pre><code>Posta köz,,,</code></pre>
<p>Instead of showing up like this:</p>
<pre><code>2011,Budakalász,Posta köz</code></pre>
<p>"Posta köz" can be seen here: <a href="https://nominatim.openstreetmap.org/details.php?osmtype=W&amp;osmid=361968551&amp;class=highway">https://nominatim.openstreetmap.org/details.php?osmtype=W&amp;osmid=361968551&amp;class=highway</a></p>
<p>Using the command below, this entry is not visible in the output:</p>
<pre><code>osmfilter hun.o5m --keep=&quot;highway=residential&quot; | osmconvert - --csv=&quot;addr:street&quot; --csv-separator=&quot;,&quot; &gt; hun_residential.csv
grep -i &quot;posta köz&quot; hun_residential.csv</code></pre>
<p>And this returns with only 66 street names which is a very low number.</p>
<pre><code>cat hun_residential.csv | wc -l</code></pre>
<p>Any ideas how to get city,postcode and street names next to each other?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span> <span class="post-tag tag-link-residential" rel="tag" title="see questions tagged &#39;residential&#39;">residential</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Apr '20, 14:48</strong></p>
<img src="https://secure.gravatar.com/avatar/5d3669c082ad6c7e175f2491a838d15b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jovokep&#39;s gravatar image" />
<p><span>jovokep</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jovokep has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Apr '20, 09:05</strong> </span></p>
</div>
</div>
<div id="comments-container-74110" class="comments-container">
<span id="74111"></span>
<div id="comment-74111" class="comment">
<div id="post-74111-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What happens if you include 'name' in the osmconvert output?</p>
<p>I expect the issue is that you aren't causing highways to be included in that step, but I'm not terribly familiar with the tools.</p>
</div>
<div id="comment-74111-info" class="comment-info">
<span class="comment-age">(12 Apr '20, 15:12)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="74116"></span>
<div id="comment-74116" class="comment">
<div id="post-74116-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>After adding "name" I see 141820 lines which is promising. The issue is that I don't see the postcode or any other data related to this street.</p>
<p>Output is: "Posta köz,,,"</p>
<p>A useful output would be like this (postcode, city, street) 2941,Ács,Posta köz</p>
<p>For reference, this is how I try to create a CSV with street names, postcodes and city names:</p>
<pre><code>osmfilter hun.o5m --keep=&quot;addr:postcode=* addr:country= addr:city= addr:street= highway=cycleway highway=path highway=primary highway=residential highway=tertiary&quot; | osmconvert - --csv=&quot;name addr:postcode addr:city addr:street&quot; --csv-separator=&quot;,&quot; &gt; hun_streets.csv</code></pre>
</div>
<div id="comment-74116-info" class="comment-info">
<span class="comment-age">(12 Apr '20, 21:51)</span> <span class="comment-user userinfo">jovokep</span>
</div>
</div>
<span id="74117"></span>
<div id="comment-74117" class="comment">
<div id="post-74117-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've edited the whole question for greater clarity.</p>
</div>
<div id="comment-74117-info" class="comment-info">
<span class="comment-age">(12 Apr '20, 22:06)</span> <span class="comment-user userinfo">jovokep</span>
</div>
</div>
<span id="74121"></span>
<div id="comment-74121" class="comment">
<div id="post-74121-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>So nominatim processes the raw data that is included in hungary-latest.osm.pbf to match up streets and cities/postcodes/etc. In the .pbf file, the street is stored as a line, and then separately, a city or postcode is stored as an area(this is over-simplified, but it's close enough). Nominatim goes through and makes the associations.</p>
<p>It will take a long time to query so many streets from the public servers (and such high volume is heavily discouraged). It's possible to run a local copy that is limited to a smaller area.</p>
</div>
<div id="comment-74121-info" class="comment-info">
<span class="comment-age">(13 Apr '20, 02:39)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="74160"></span>
<div id="comment-74160" class="comment">
<div id="post-74160-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd like to make these associations too, offline. The question is what is an easy way to do it?</p>
<p>If I could count on the fact that all streets belonging to the same city are listed together (and not randomly in the CSV output) then I would be able to fill in the gaps.</p>
</div>
<div id="comment-74160-info" class="comment-info">
<span class="comment-age">(14 Apr '20, 09:10)</span> <span class="comment-user userinfo">jovokep</span>
</div>
</div>
</div>
<div id="comment-tools-74110" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74110-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

