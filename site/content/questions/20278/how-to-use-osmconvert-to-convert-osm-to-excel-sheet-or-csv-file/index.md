+++
type = "question"
title = "how to use osmconvert to convert osm to excel sheet or csv file"
description = '''I have tried osmconvert to convert osm to .o5m and .pbf file it works fine but am having problem converting osm to .csv or excel file I used  ./osmconvert addis.osm --all-to-nodes --csv=&quot;@id @lon @lat amenity cafe restaurant name&quot; or ./osmconvert addis.osm --all-to-nodes --csv=&quot;@id @lon @lat amenity...'''
date = "2013-02-25T18:01:00Z"
lastmod = "2015-12-17T20:38:00Z"
weight = 20278
keywords = [ "osmconvert", "csv", "excel", "convert", "spreadsheet" ]
aliases = [ "/questions/20278" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [how to use osmconvert to convert osm to excel sheet or csv file](/questions/20278/how-to-use-osmconvert-to-convert-osm-to-excel-sheet-or-csv-file)

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
<span id="post-20278-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20278-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20278-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have tried osmconvert to convert osm to .o5m and .pbf file it works fine but am having problem converting osm to .csv or excel file I used</p>
<p>./osmconvert addis.osm --all-to-nodes --csv="<span><span>@id</span></span> <span><span>@lon</span></span> <span><span>@lat</span></span> amenity cafe restaurant name" or ./osmconvert addis.osm --all-to-nodes --csv="<span><span>@id</span></span> <span><span>@lon</span></span> <span><span>@lat</span></span> amenity cafe name"</p>
<p>but nothing comes up is there any other way to convert osm to excel sheet or csv file?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-excel" rel="tag" title="see questions tagged &#39;excel&#39;">excel</span> <span class="post-tag tag-link-convert" rel="tag" title="see questions tagged &#39;convert&#39;">convert</span> <span class="post-tag tag-link-spreadsheet" rel="tag" title="see questions tagged &#39;spreadsheet&#39;">spreadsheet</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Feb '13, 18:01</strong></p>
<img src="https://secure.gravatar.com/avatar/123ba309f933f61ed3f4bad9b26ee8ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AddisMap%20Meti&#39;s gravatar image" />
<p><span>AddisMap Meti</span><br />
<span class="score" title="71 reputation points">71</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AddisMap Meti has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-20278" class="comments-container">
<span id="20280"></span>
<div id="comment-20280" class="comment">
<div id="post-20280-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>you forgot --out-csv and --o=...</p>
<p>also, see my answer</p>
</div>
<div id="comment-20280-info" class="comment-info">
<span class="comment-age">(25 Feb '13, 19:38)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
</div>
<div id="comment-tools-20278" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20278-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="20279"></span>

<div id="answer-container-20279" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20279-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20279-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-20279-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSMconvert is not a filter. This means that all features will be converted.</p>
<p>To achieve your goal of having only certain features in your csv file, you will have to filter the csv file generated by osmconvert afterwards.</p>
<p>Also, the arguments to the --csv option of osmconvert are the tag keys you want to have in your csv file. If you want "amenity" and "name" columns in addition to id, lat and lon, you specify "<span><span>@id</span></span> <span><span>@lon</span></span> <span><span>@lat</span></span> amenity name", and then filter the CSV output.</p>
<p>For example:</p>
<pre><code>./osmconvert addis.osm --all-to-nodes --csv=&quot;@id @lon @lat amenity name&quot; --out-csv -o=outfile.csv
&#10;grep cafe outfile.csv &gt; cafes.csv
grep restaurant outfile.csv &gt; restaurants.csv
cat cafes.csv restaurants.csv &gt; cafes_and_restaurants.csv</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Feb '13, 19:37</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Feb '13, 19:39</strong> </span></p>
</div>
</div>
<div id="comments-container-20279" class="comments-container">
<span id="33319"></span>
<div id="comment-33319" class="comment">
<div id="post-33319-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>how to store that in mysql</p>
</div>
<div id="comment-33319-info" class="comment-info">
<span class="comment-age">(20 May '14, 12:16)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
<span id="33320"></span>
<div id="comment-33320" class="comment">
<div id="post-33320-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>What do you mean with "that"?</p>
</div>
<div id="comment-33320-info" class="comment-info">
<span class="comment-age">(20 May '14, 12:30)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="33359"></span>
<div id="comment-33359" class="comment">
<div id="post-33359-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Have you ever tried any internet search engines like duckduckgo, google, yahoo or similar, and do a search there for "import csv in mysql" or similar?????</p>
</div>
<div id="comment-33359-info" class="comment-info">
<span class="comment-age">(21 May '14, 18:18)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="33362"></span>
<div id="comment-33362" class="comment">
<div id="post-33362-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@stephan75</span> : apparently he has not bothered. So he might find some hints for the problem he faces at <a href="http://stackoverflow.com/questions/3635166/how-to-import-csv-file-to-mysql-table">http://stackoverflow.com/questions/3635166/how-to-import-csv-file-to-mysql-table</a> . At least be helpful, too.</p>
</div>
<div id="comment-33362-info" class="comment-info">
<span class="comment-age">(21 May '14, 20:01)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
</div>
<div id="comment-tools-20279" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20279-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33539"></span>

<div id="answer-container-33539" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33539-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33539-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33539-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have tried do a similar thing: convert a way in baikal.osm to baikal.csv . The problem is the order of nodes I get in .csv file. I used</p>
<p>osmconvert baikal.osm --all-to-nodes --csv="<span>@lon</span> <span>@lat</span>" &gt; baikal.csv</p>
<p>I get nodes in wrong order. osmconvert do not read the second part of .osm file with &lt;nd ref= ...</p>
<p>How to solve this?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 May '14, 20:29</strong></p>
<img src="https://secure.gravatar.com/avatar/9b18be372f895390b2f63a41066498a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="miko679&#39;s gravatar image" />
<p><span>miko679</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="miko679 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33539" class="comments-container">
&#10;</div>
<div id="comment-tools-33539" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33539-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47201"></span>

<div id="answer-container-47201" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47201-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47201-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47201-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can also have closer look at the Java based tool <a href="https://github.com/MorbZ/OsmPoisPbf">OsmPoisPbf</a>, which scans an OpenStreetMap file for nodes and areas (and relations) whose tags indicate them as POIs (points of interest) and extracts those into a comma separated file (CSV).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Dec '15, 20:38</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-47201" class="comments-container">
&#10;</div>
<div id="comment-tools-47201" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47201-form-container" class="comment-form-container">
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

