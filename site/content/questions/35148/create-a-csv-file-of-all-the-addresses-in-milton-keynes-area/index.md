+++
type = "question"
title = "Create a CSV file of all the addresses in Milton Keynes area"
description = '''I am interested in creating a CSV file of addresses from the the Milton Keynes area (in the format street name, town, postcode, city, latitude, longitude).  This is what I&#x27;ve done so far: 1) Download osm files for the UK at http://nick.dev.openstreetmap.org/downloads/planet/ 2) Run osmfilter: osmfil...'''
date = "2014-07-24T20:02:00Z"
lastmod = "2014-07-25T15:33:00Z"
weight = 35148
keywords = [ "osmconvert", "osmfilter" ]
aliases = [ "/questions/35148" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Create a CSV file of all the addresses in Milton Keynes area](/questions/35148/create-a-csv-file-of-all-the-addresses-in-milton-keynes-area)

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
<span id="post-35148-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35148-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35148-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am interested in creating a CSV file of addresses from the the Milton Keynes area (in the format <strong>street name, town, postcode, city, latitude, longitude</strong>).</p>
<p><img src="/upfiles/Capture_8.PNG" alt="alt text" /></p>
<p><strong>This is what I've done so far:</strong></p>
<p>1) Download osm files for the UK at <a href="http://nick.dev.openstreetmap.org/downloads/planet/">http://nick.dev.openstreetmap.org/downloads/planet/</a></p>
<p>2) Run osmfilter:</p>
<pre><code>osmfilter uk.osm --keep=&quot;highway=residential =primary =secondary =tertiaty =unclassified&quot; &gt;uk_streets.osm</code></pre>
<p>3) Run osmconvert:</p>
<pre><code>osmconvert uk_streets.osm --csv=&quot;@lon @lat addr:city addr:street&quot; --csv-headline --csv-separator=, -o=uk_streets.csv</code></pre>
<p><strong>My problems</strong></p>
<ul>
<li>I can't figure out how to only pull addresses from the Milton Keynes area, the above script seems to pull from the whole of UK (i.e. in the bounds shown in the image above)</li>
<li>There were lots of gaps in the data after running the script, I could not find some of the addresses that appeared on the OSM website in the database</li>
</ul>
<p>How would I refactor my osmfilter and osmconvert commands to pull the necessary information for the Milton Keynes area?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jul '14, 20:02</strong></p>
<img src="https://secure.gravatar.com/avatar/7c5b80d364f476ff4c9d5ac815bd2f50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="methuselah90&#39;s gravatar image" />
<p><span>methuselah90</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="methuselah90 has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-35148" class="comments-container">
&#10;</div>
<div id="comment-tools-35148" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35148-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="35166"></span>

<div id="answer-container-35166" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35166-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35166-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-35166-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>nominatim (the engine behind the search on the map on osm.org) builds hierarchies out of the OSM data and does not return results based on the unprocessed OSM data. For example if there is a house with just a number it will match that with the nearest road and so on, without doing such processing you will not get the same results.</p>
<p>Back to your question: osmconvert supports clipping on a bounding box or a polygon, see the OSM wiki section on <a href="https://wiki.openstreetmap.org/wiki/Osmconvert#Applying_Geographical_Borders">"Applying Geographical Borders"</a>. Using a bounding box is likely to be simplest for starters (you already have one displayed in the picture you supplied).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jul '14, 07:56</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Jul '14, 12:04</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-35166" class="comments-container">
&#10;</div>
<div id="comment-tools-35166" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35166-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="35185"></span>

<div id="answer-container-35185" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35185-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35185-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35185-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>According to the data model used at least in Germany, the information about a city or postalcode area to where a street belons is NOT stored on each street.</p>
<p>For that purpose we have boundary relations, a group of boundary ways in a closed circle that describe an area.</p>
<p>So you should have a look whether these relations are present in the OSM data for your purposes.</p>
<p>About administrative borders, see <a href="http://openmapsurfer.uni-hd.de">openmapsurfer</a> (choose grayscale layer with borders overlay) or <a href="https://osm.wno-edv-service.de/boundaries/">wambacher's boundary display</a></p>
<p>Then you have to adjust your osmfilter commands, and find a solution how to determine in which area you have each street.</p>
<p>OR alternatively:</p>
<p>when your area has almost complete <a href="https://wiki.openstreetmap.org/wiki/Key:addr">addr: data</a>, try keeping it with osmfilter</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jul '14, 15:33</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-35185" class="comments-container">
&#10;</div>
<div id="comment-tools-35185" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35185-form-container" class="comment-form-container">
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

