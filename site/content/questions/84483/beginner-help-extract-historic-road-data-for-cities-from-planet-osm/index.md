+++
type = "question"
title = "Beginner help - extract historic road data for cities from planet osm."
description = '''Hi there, I would like some help in extracting the OSM road line data for the cities of Kigali (Rwanda), Dar es Salaam (Tanzania) and Mombasa (Kenya) for 2012,2017 and 2022. I have the latest 2022 data for each city from Geofabrik, and I know that the 2012 and 2017 data is available from https://pla...'''
date = "2022-05-15T18:30:00Z"
lastmod = "2022-05-16T10:28:00Z"
weight = 84483
keywords = [ "osmium", "beginner", "extract", "osmosis", "planet_osm" ]
aliases = [ "/questions/84483" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Beginner help - extract historic road data for cities from planet osm.](/questions/84483/beginner-help-extract-historic-road-data-for-cities-from-planet-osm)

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
<span id="post-84483-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84483-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84483-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there, I would like some help in extracting the OSM road line data for the cities of Kigali (Rwanda), Dar es Salaam (Tanzania) and Mombasa (Kenya) for 2012,2017 and 2022. I have the latest 2022 data for each city from Geofabrik, and I know that the 2012 and 2017 data is available from <a href="https://planet.openstreetmap.org">https://planet.openstreetmap.org</a>. However, I have been struggling to understand and correctly execute the necessary steps to download, decompress and extract the data from these very large planet osm files. I have a good knowledge of QGIS and working with .shp files. My knowledge of coding, various programming languages and various file types is very limited. I am using a Mac.</p>
<p>It would be amazing if you could help me to get the 2012 and 2017 road line maps for the cities of Kigali, Dar es Salaam and Mombasa so that I can use them in QGIS for my research purposes. Thank you!</p>
<p>I am currently not sure of the process required and how to go about it. Questions include:</p>
<ul>
<li>Which exact file should I be downloading from <a href="https://planet.openstreetmap.org">https://planet.openstreetmap.org</a> ?</li>
<li>How can I de-compress these large files? is the right thing to do? Is it possible to extract the 2012 and 2017 data for the 3 cities without de-compressing the file?</li>
<li>How do I extract the 2012 and 2017 data for these 3 cities? I have come across Osmosis, Osmium, JOSM and History Splitter in my search, but I am not sure which is most appropriate to my problem and how to use it (the technicality of the GitHub pages are tricky for me to decipher).</li>
</ul>
<p>Thank you so much for taking the time to consider my problem - I welcome any help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmium" rel="tag" title="see questions tagged &#39;osmium&#39;">osmium</span> <span class="post-tag tag-link-beginner" rel="tag" title="see questions tagged &#39;beginner&#39;">beginner</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-planet_osm" rel="tag" title="see questions tagged &#39;planet_osm&#39;">planet_osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 May '22, 18:30</strong></p>
<img src="https://secure.gravatar.com/avatar/da9b24811b6148ed0b3d29ad63a26947?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cosh99&#39;s gravatar image" />
<p><span>Cosh99</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cosh99 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84483" class="comments-container">
&#10;</div>
<div id="comment-tools-84483" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84483-form-container" class="comment-form-container">
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

<span id="84484"></span>

<div id="answer-container-84484" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84484-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-84484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First, the usual caveat regarding historic data in OSM: You will be looking at "what OSM knew about the place at the time", not "what the place was like at the time". To give an extreme example, for 2008 there will probably be almost zero streets in your cities of interest. Does that mean that all streets that are there now have been built in the last 14 years? No, it just means that they had not been added to OSM at the time.</p>
<p>While the process of "downloading old planet file and extracting an area of interest from that" is possible (you would try to grab an .osm.pbf file and then use the "osmium" command line utility to extract an area of interest from the huge file), a better process might be to download the "history" file for the country in question (from osm-internal.download.geofabrik.de), then use the "osmosis" command line utility to extract from this file a country snapshot for any point in time (repeat the process for multiple times if desired), then again use osmium to extract the city of interest from the time snapshot.</p>
<p>And a second caveat about the 2012 data: In April 2012, OSM changed its data license from "CC-BY-SA" to "ODbL". At that time, all old data was purged from OSM unless the contributors had agreed to re-license their data. This purge affects even the history data. So if you want to go back further than April 2012 and see a complete picture (and not just the data from people who have said yes to the relicensing), you will need to use a different history file that is licensed under the CC-BY-SA license. That, however, is not available in a per-country version from Geofabrik, and also mixing CC-BY-SA licensed data with ODbL data in your project is a sure recipe for headache.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 May '22, 18:44</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 May '22, 18:45</strong> </span></p>
</div>
</div>
<div id="comments-container-84484" class="comments-container">
&#10;</div>
<div id="comment-tools-84484" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84484-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="84490"></span>

<div id="answer-container-84490" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84490-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84490-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-84490-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Read all the caveats mentioned by Frederik. The easiest way to collect data of this type from September 2012 onwards is via Overpass queries using <a href="https://wiki.openstreetmap.org/wiki/Attic_Data">"Attic" data</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 May '22, 10:28</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-84490" class="comments-container">
&#10;</div>
<div id="comment-tools-84490" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84490-form-container" class="comment-form-container">
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

