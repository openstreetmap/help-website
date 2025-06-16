+++
type = "question"
title = "Count street length of a city"
description = '''Dear community, i am aware that the topic is discussed on several places - nevertheless i didn&#x27;t find an answer up to now (sorry when i missed it).  My goal is simply to count the total street length of all streets within a certain city (the exact district) for a running project. Two things i can&#x27;t ...'''
date = "2019-04-22T20:16:00Z"
lastmod = "2020-04-30T22:29:00Z"
weight = 68878
keywords = [ "city", "length", "street" ]
aliases = [ "/questions/68878" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Count street length of a city](/questions/68878/count-street-length-of-a-city)

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
<span id="post-68878-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68878-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68878-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear community, i am aware that the topic is discussed on several places - nevertheless i didn't find an answer up to now (sorry when i missed it). My goal is simply to count the total street length of all streets within a certain city (the exact district) for a running project. Two things i can't solve:</p>
<ol>
<li><p>I am not able to export ONLY a certain city district within its exact borders - like: <a href="https://www.openstreetmap.org/relation/959809#map=12/48.8367/13.0167">https://www.openstreetmap.org/relation/959809#map=12/48.8367/13.0167</a> The information is there ... in theory it would be enough to export only the data with a certain regional or community key. I tried it with <a href="https://export.hotosm.org">https://export.hotosm.org</a> - but even with a certain export shape formed i do not get the correct data. So i do not look for a rectangle data - only the data within the city border.</p></li>
<li><p>I can't find a solution to calculate the street length. In QGIS there is under vector/analytic-tools/summary line length - but this didn't get me any results and i am not sure if it counts only street length or every line. Than i found <strong>osm-length-2.pl</strong> but i could't get it to work - (besides the fact i do not have the right data). Sorry for this dummy question: I installed Perl - i have a OSM-file - i run osm-length-2.pl and how tell i the script to use my OSM-file? Within the script there is the info to use stdin - but i could't figure out HOW to use it and i am not a Perl-Programmer - sorry.</p></li>
</ol>
<p>Appreciate any help - didn't thought it is so difficult :-O Christoph</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-length" rel="tag" title="see questions tagged &#39;length&#39;">length</span> <span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Apr '19, 20:16</strong></p>
<img src="https://secure.gravatar.com/avatar/4a915fd75da0e50efe7bdaa2173cb998?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KCBCOM&#39;s gravatar image" />
<p><span>KCBCOM</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KCBCOM has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68878" class="comments-container">
&#10;</div>
<div id="comment-tools-68878" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68878-form-container" class="comment-form-container">
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

<span id="68883"></span>

<div id="answer-container-68883" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68883-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68883-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-68883-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For a precise result, you cannot hope to cut out "all streets within a city" from OSM before you compute the length, because streets can cross the city boundary and if I understand you correctly, in this case you'd only want the length of the bit inside.</p>
<p>One way of getting this done is:</p>
<ol>
<li>Import OSM data for a rectangle around your city into a PostGIS database with osm2pgsql. This will not only give you the roads but also the city boundary if mapped in OSM.</li>
<li>Use PostGIS to sum up the length of geometries inside your area of interest ("clipping polygon") as discussed in <a href="/questions/49200/actual-road-length-of-exported-map">"Actual road length of exported map"</a></li>
</ol>
<p>QGIS will also allow you to filter out all roads and clip them at the polygon boundary but it is a more cumbersome and manual process.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Apr '19, 09:27</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-68883" class="comments-container">
&#10;</div>
<div id="comment-tools-68883" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68883-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="68971"></span>

<div id="answer-container-68971" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68971-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68971-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-68971-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yet another possiblity: you can run a query on Overpass API. <a href="https://overpass-turbo.eu/s/Ii6">This one</a> produces a sample statistic for my home town, by value of highway. Length is in meters.</p>
<p>This should also point you to the real issues: You should decide for yourself whether you want to count footways and tracks or not. Another source of incertainty are dual carriageways; they would be counted twice because they are two ways in OpenStreetMap. Frontage roads, turn lanes and more may also affect the results. Finally, the request keeps ways on the boundary intact, thus slightly overestimating length values for that part of the problem.</p>
<p>Nontheless, for best effort guess data is for sure good enough.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Apr '19, 18:48</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-68971" class="comments-container">
&#10;</div>
<div id="comment-tools-68971" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68971-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="68930"></span>

<div id="answer-container-68930" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68930-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68930-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-68930-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thanks for your answer Frederik! After trying your solution it still turned out a little bit complicated for me. So now i came up with following workaround (QGIS 3.6.2):</p>
<ol>
<li>Install QuickOSM-Plugin. Make a search with key=highway and In=NameOfYourCity. Under additionale settings (Dropdown) i checked only Node, Way, Relation and Line. Run the query.</li>
<li>The result will be a list of streets within your city - added in the layers panel. Now i made a right click on the new layer and opened the attribute table. Problem is: There are to many not valid streets (like private or motorway etc.) included. My solution was: A) Make the layer edible (Pen button). Sort by street name. Delete all streets without name. Rename the layer for this result. Problem now is: Some linking overland streets are missing B) Run the same query. Now delete all streets with name. Afterwards sort by highway and delete anything except primary, residential, secondary and tertiary.</li>
<li>Finally for calculating the length i added a new field with the field calculator button in the attribute table. Fieldname=length_km, Fieldtype=decimal(real), Fieldlength=10, precision=2. In the query window add: $length / 1000. Than press ok - sort the new field from the end to the beginning if you want and close the attribute table.</li>
<li>Open Vector/Analytic-Tools/Basic-Statistic-For-Fields. Choose your preferred layer for input and choose your new field lenght_km for calculation. Start the process. Under sum you can see the Km.</li>
</ol>
<p>Step 3+4 are fully described here: <a href="http://www.qgistutorials.com/en/docs/calculating_line_lengths.html">http://www.qgistutorials.com/en/docs/calculating_line_lengths.html</a></p>
<p>Greetings - Christoph</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Apr '19, 20:30</strong></p>
<img src="https://secure.gravatar.com/avatar/4a915fd75da0e50efe7bdaa2173cb998?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KCBCOM&#39;s gravatar image" />
<p><span>KCBCOM</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KCBCOM has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Apr '19, 20:34</strong> </span></p>
</div>
</div>
<div id="comments-container-68930" class="comments-container">
&#10;</div>
<div id="comment-tools-68930" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68930-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74519"></span>

<div id="answer-container-74519" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74519-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74519-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74519-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have you tried this package?</p>
<p><a href="https://github.com/JoaoCarabetta/osm-road-length">https://github.com/JoaoCarabetta/osm-road-length</a></p>
<p>It is super easy,</p>
<p>Install it: pip install osm-road-length</p>
<p>And run:</p>
<p>import osm_road_length from shapely import wkt</p>
<p>geometry = wkt.loads('POLYGON((-43.2958811591311 -22.853167273541693,-43.30961406928735 -23.035275736044728,-43.115980036084224 -23.02010939749927,-43.157178766552974 -22.832917893834313,-43.2958811591311 -22.853167273541693))')</p>
<p>length = osm_road_length.get(geometry)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Apr '20, 22:29</strong></p>
<img src="https://secure.gravatar.com/avatar/233392fffdef27e8db3a844cf613d74d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JOAO%20LUIZ&#39;s gravatar image" />
<p><span>JOAO LUIZ</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JOAO LUIZ has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74519" class="comments-container">
&#10;</div>
<div id="comment-tools-74519" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74519-form-container" class="comment-form-container">
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

