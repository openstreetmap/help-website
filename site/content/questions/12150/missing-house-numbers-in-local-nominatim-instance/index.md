+++
type = "question"
title = "Missing House Numbers in local Nominatim instance?"
description = '''I downloaded a US State extract from CloudMade, imported into Nominatim, and found that house numbers are not recognized.  I don&#x27;t understand why I am getting completely different results than nominatim.openstreetmap.org. Would I get better results from a full planet OSM file? I kind of have cold fe...'''
date = "2012-04-19T00:11:00Z"
lastmod = "2014-05-14T23:38:00Z"
weight = 12150
keywords = [ "house", "nominatim", "cloudmade", "number" ]
aliases = [ "/questions/12150" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Missing House Numbers in local Nominatim instance?](/questions/12150/missing-house-numbers-in-local-nominatim-instance)

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
<span id="post-12150-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12150-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12150-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I downloaded a US State extract from CloudMade, imported into Nominatim, and found that house numbers are not recognized.</p>
<p>I don't understand why I am getting completely different results than nominatim.openstreetmap.org.</p>
<p>Would I get better results from a full planet OSM file? I kind of have cold feet with the experience so far from this small extract.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-house" rel="tag" title="see questions tagged &#39;house&#39;">house</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-cloudmade" rel="tag" title="see questions tagged &#39;cloudmade&#39;">cloudmade</span> <span class="post-tag tag-link-number" rel="tag" title="see questions tagged &#39;number&#39;">number</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Apr '12, 00:11</strong></p>
<img src="https://secure.gravatar.com/avatar/e17c2bfaed82349f7a355866ff24e4cf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Norm1&#39;s gravatar image" />
<p><span>Norm1</span><br />
<span class="score" title="126 reputation points">126</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Norm1 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Apr '12, 11:12</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-12150" class="comments-container">
<span id="12185"></span>
<div id="comment-12185" class="comment">
<div id="post-12185-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My table <code>location_property_tiger</code> is empty, could that have anything to do with not finding house numbers? Where would that source data come from?</p>
</div>
<div id="comment-12185-info" class="comment-info">
<span class="comment-age">(19 Apr '12, 20:52)</span> <span class="comment-user userinfo">Norm1</span>
</div>
</div>
<span id="12197"></span>
<div id="comment-12197" class="comment">
<div id="post-12197-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe we need some testcases to see where the problem is.</p>
<p>And perhabs you can ask <a href="https://www.openstreetmap.org/user/lonvia">https://www.openstreetmap.org/user/lonvia</a> ... she seems to be involved in some way to Nominatim.</p>
</div>
<div id="comment-12197-info" class="comment-info">
<span class="comment-age">(20 Apr '12, 13:16)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="12276"></span>
<div id="comment-12276" class="comment">
<div id="post-12276-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, I will reach out to lonvia.</p>
<p>On a side note, is anyone here running a copy of Nominatim? Is your table location_property_tiger empty?</p>
<p>I scoured through the source code of OSM and Nominatim and I don't see anything that is responsible for populating data for that table.</p>
</div>
<div id="comment-12276-info" class="comment-info">
<span class="comment-age">(23 Apr '12, 13:59)</span> <span class="comment-user userinfo">Norm1</span>
</div>
</div>
<span id="12296"></span>
<div id="comment-12296" class="comment">
<div id="post-12296-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Here is a perfect example with missing house numbers:</p>
<p><a href="http://ec2-23-22-23-186.compute-1.amazonaws.com/search.php?q=19+gloria+lane%2C+fairfield+nj&amp;viewbox=-74.3%2C40.88%2C-74.29%2C40.87">http://ec2-23-22-23-186.compute-1.amazonaws.com/search.php?q=19+gloria+lane%2C+fairfield+nj&amp;viewbox=-74.3%2C40.88%2C-74.29%2C40.87</a></p>
<p><a href="http://nominatim.openstreetmap.org/search.php?q=19+gloria+lane%2C+fairfield+nj&amp;viewbox=-74.3%2C40.88%2C-74.29%2C40.87">http://nominatim.openstreetmap.org/search.php?q=19+gloria+lane%2C+fairfield+nj&amp;viewbox=-74.3%2C40.88%2C-74.29%2C40.87</a></p>
</div>
<div id="comment-12296-info" class="comment-info">
<span class="comment-age">(23 Apr '12, 17:37)</span> <span class="comment-user userinfo">Norm1</span>
</div>
</div>
</div>
<div id="comment-tools-12150" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12150-form-container" class="comment-form-container">
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

<span id="12303"></span>

<div id="answer-container-12303" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12303-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12303-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-12303-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Norm1 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the US, the OSM instance of Nominatim uses TIGER address data to complement the still sparse OSM house number data. You can add TIGER data to your own Nominatim instance by following these steps:</p>
<ol>
<li>Get the <a href="ftp://ftp2.census.gov/geo/tiger/TIGER2012">TIGER 2012</a> data. You will need the EDGES files.</li>
<li>Extract the relevant data: <code>./utils/imports.php --parse-tiger-2011 &lt;tiger directory&gt;</code></li>
<li>Import the data into your Nominatim database: <code>./utils/setup.php --import-tiger-data</code></li>
</ol>
<p>Be warned that the import can take a very long time, especially if you are importing all of the US.</p>
<p>Note: answer updated for TIGER 2012 data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Apr '12, 19:36</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jul '13, 10:52</strong> </span></p>
</div>
</div>
<div id="comments-container-12303" class="comments-container">
<span id="12333"></span>
<div id="comment-12333" class="comment">
<div id="post-12333-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Cheers, lonvia. Your instructions were spot on!</p>
</div>
<div id="comment-12333-info" class="comment-info">
<span class="comment-age">(24 Apr '12, 14:35)</span> <span class="comment-user userinfo">Norm1</span>
</div>
</div>
<span id="15466"></span>
<div id="comment-15466" class="comment">
<div id="post-15466-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello, I'm having this problem when I try to import tiger data by following the steps you mention. I've downloaded the edges from here <a href="ftp://ftp2.census.gov/geo/tiger/TIGER2011/EDGES/">ftp://ftp2.census.gov/geo/tiger/TIGER2011/EDGES/</a> The command I use is ./utils/imports.php --parse-tiger-2011 EDGES/ I get the output of this sort: File "/Nominatim/utils/tigerAddressImport.py", line 50, in &lt;module&gt; import ogr ImportError: No module named ogr Failed parse (/root/tiger/ftp2.census.gov/geo/tiger/TIGER2011/EDGES/tl_2011_01001_edges.zip) Any help you could give will be extremely appreciated!</p>
</div>
<div id="comment-15466-info" class="comment-info">
<span class="comment-age">(24 Aug '12, 09:04)</span> <span class="comment-user userinfo">silviu_</span>
</div>
</div>
<span id="15508"></span>
<div id="comment-15508" class="comment">
<div id="post-15508-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You need the <a href="http://pypi.python.org/pypi/GDAL">GDAL package for python</a>. In Ubuntu install it with <code>sudo apt-get install python-gdal</code>.</p>
</div>
<div id="comment-15508-info" class="comment-info">
<span class="comment-age">(25 Aug '12, 13:09)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="25845"></span>
<div id="comment-25845" class="comment">
<div id="post-25845-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I am running this command ./utils/imports.php --parse-tiger-2011 /osm/tiger_data/ but the process does not start and no output even.</p>
</div>
<div id="comment-25845-info" class="comment-info">
<span class="comment-age">(27 Aug '13, 10:37)</span> <span class="comment-user userinfo">mezbaur</span>
</div>
</div>
<span id="25867"></span>
<div id="comment-25867" class="comment">
<div id="post-25867-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Looks like the changes for the 2012 and 2013 editions haven't made it into the release yet. You need the import script from the latest git version. It is safe to simply clone the latest version temporarily and run the TIGER import from there.</p>
</div>
<div id="comment-25867-info" class="comment-info">
<span class="comment-age">(27 Aug '13, 19:12)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="33188"></span>
<div id="comment-33188" class="comment not_top_scorer">
<div id="post-33188-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span>@mezbaur</span> I needed to put the edge zip file(s) in their own directory and pass that directory in as the argument. Hope that helps. Also you can get a specific county's EDGEs by going here <a href="http://www.census.gov/cgi-bin/geo/shapefiles2013/main.">http://www.census.gov/cgi-bin/geo/shapefiles2013/main.</a> Select "All Lines" from the drop down. Then choose the state/county.</p>
<p>Also note that this process took up a bunch of ram.</p>
<p>I imported it and it still seems to not be working</p>
</div>
<div id="comment-33188-info" class="comment-info">
<span class="comment-age">(14 May '14, 23:38)</span> <span class="comment-user userinfo">drewlesueur</span>
</div>
</div>
</div>
<div id="comment-tools-12303" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-12303-form-container" class="comment-form-container">
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

