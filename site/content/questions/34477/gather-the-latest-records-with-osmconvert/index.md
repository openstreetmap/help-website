+++
type = "question"
title = "gather the latest records with osmconvert"
description = '''hello  update; - i want to gather the latest 100 records that have the amenity=school - school from  a. south-america -(yes - the whole continent)  b. Africa  c. the planet - (guess that my notebook do not will do this job - the file is toooo big.  So as a first step i am willing to start with South...'''
date = "2014-06-30T23:44:00Z"
lastmod = "2014-07-01T20:00:00Z"
weight = 34477
keywords = [ "xml", "apache", "perl", "osm", "linux" ]
aliases = [ "/questions/34477" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [gather the latest records with osmconvert](/questions/34477/gather-the-latest-records-with-osmconvert)

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
<span id="post-34477-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34477-score" class="post-score" title="current number of votes">
-3
</div>
<span id="post-34477-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hello</p>
<p><strong>update;</strong> - i want to gather the latest 100 records that <strong>have the amenity=school</strong> - school from</p>
<pre><code>a. south-america -(yes - the whole continent) 
b. Africa 
c. the planet - (guess that my notebook do not will do this job - the file is toooo big.</code></pre>
<p>So as a first step i am willing to start with South-America.</p>
<p>According the manual here <a href="http://m.m.i24.cc/osmconvert.c">http://m.m.i24.cc/osmconvert.c</a> I THINK THAT i can use some of the following terms to get the right data out of the bunch of data.</p>
<pre><code>&quot;--timestamp=&lt;date_time&gt;   add a timestamp to the data\n&quot;
&quot;--timestamp=NOW-&lt;seconds&gt; add a timestamp in seconds before now\n&quot;
&quot;--out-timestamp           **output the file\&#39;s timestamp, nothing else\n&quot;**</code></pre>
<p>and if i want to gather all the results that contain a webseite then</p>
<pre><code>a.  i reduce the new entries and records to a minimum - 
note we have approx 1000 new records..
b.  the question is : how to name this condition - &quot; have a website&quot; ?</code></pre>
<p>i want to do this with osmconvert.... any and all help will be greatly appreciated. Question: i wonder where i can use the drop-statement. If it will be used very early then i can limit the amount of data that has to be parsed. What do you think !? Does this make sense..!?</p>
<p>See below - my first trials which are very very general... and not very sophisticatde --- lo-level-processing;-)</p>
<p><strong>end of update:</strong></p>
<p>i am pretty new to Geographic-information Systems so do not bear with me if i ask newby questions: i am interested in gatherin information on schools Some days before i have heard that it is interesting to have a closer look at the taginfo-site (see below): i have question: what does this mean <a href="https://taginfo.openstreetmap.org/tags/amenity=school">https://taginfo.openstreetmap.org/tags/amenity=school</a></p>
<p>here we have two requests on the above site:</p>
<p>see the details:</p>
<pre><code>593 454 - at 30 th of june 
593 319
593 194
592 853
592 443 - at 24 th of june</code></pre>
<p>1000 records</p>
<p>you see: the results differs: approx 1000 x (entries, records or some what)</p>
<p>questions:</p>
<p>a. is it true that we can see the diff - that means how the entries of schools grow? b. is there a total growth of records (!!!) of schools or does the this mean - some records have been changed!? c. can i grab the neewst ones -- that are the newest entires with osmonvert?</p>
<p>look forward to hear from you</p>
<p>btw i have this code up and running...</p>
<pre><code> wget http://download.geofabrik.de/south-america/colombia-latest.osm.pbf
./osmconvert colombia-latest.osm.pbf -o=columbia.o5m
./osmfilter columbia.o5m --keep=&quot;amenity=school&quot; -o=columbia-schools.o5m
./osmconvert columbia-schools.o5m --all-to-nodes -o=columbia-schools_nodes.o5m
./osmfilter columbia-schools_nodes.o5m --keep=&quot;amenity=school&quot; -o=columbia-schools-results.o5m
./osmconvert columbia-schools-results.o5m --csv=&quot;@id @lon @lat name addr:street addr:housenumber addr:city website email&quot; --csv-headline -o=columbia-schools-results.csv</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-apache" rel="tag" title="see questions tagged &#39;apache&#39;">apache</span> <span class="post-tag tag-link-perl" rel="tag" title="see questions tagged &#39;perl&#39;">perl</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>30 Jun '14, 23:44</strong></p>
<img src="https://secure.gravatar.com/avatar/bf4d2d8660e82c4a7387b7d2a8a8cfcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="say_hello_to_the_world&#39;s gravatar image" />
<p><span>say_hello_to...</span><br />
<span class="score" title="19 reputation points">19</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="say_hello_to_the_world has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Jul '14, 19:37</strong> </span></p>
</div>
</div>
<div id="comments-container-34477" class="comments-container">
<span id="34494"></span>
<div id="comment-34494" class="comment">
<div id="post-34494-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Your two questions <em>a</em> and <em>b</em> have already been answered a week ago here: <a href="https://gis.stackexchange.com/questions/103052/scaling-of-results-the-comparing-of-osm-files-for-a-few-days-a-statistical-ap">https://gis.stackexchange.com/questions/103052/scaling-of-results-the-comparing-of-osm-files-for-a-few-days-a-statistical-ap</a></p>
</div>
<div id="comment-34494-info" class="comment-info">
<span class="comment-age">(01 Jul '14, 14:36)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="34502"></span>
<div id="comment-34502" class="comment">
<div id="post-34502-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hello dear scai - right said! well at the moment i try to find a way to get with osmconvert the latest records - from a osm-files. i try to figure out how to do that... hopefully osmconvert will provide some ways - other wise i have to use another technique or what do you suggest. note. i am not familiar with much of the others - with java or java-script</p>
</div>
<div id="comment-34502-info" class="comment-info">
<span class="comment-age">(01 Jul '14, 18:07)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
<span id="34504"></span>
<div id="comment-34504" class="comment">
<div id="post-34504-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you struggle with osmconvert then try asking a question about osmconvert including what you have tried, what result you are expecting and what actual result or error message you got. Your current question is not very clear.</p>
</div>
<div id="comment-34504-info" class="comment-info">
<span class="comment-age">(01 Jul '14, 18:23)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="34507"></span>
<div id="comment-34507" class="comment">
<div id="post-34507-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hello dear scai - many many thanks for the response. i ve added a update. You see i have made some efforts - and figured out which conditions i need to have in the osmconvert-request. i ve digged into the man-pages. and i have found out that we can use the timestamp to do the magic. Additionally - i want to exclude all the new records (that are within ) the new time-zone of let me say one or two weeks - which have no website... so this will limit the results to a minimum - note we ve got (sometimes )a rate of 1 -to-10 percent of records that contain a website. so we need to take 1000 records</p>
</div>
<div id="comment-34507-info" class="comment-info">
<span class="comment-age">(01 Jul '14, 19:26)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
<span id="34508"></span>
<div id="comment-34508" class="comment not_top_scorer">
<div id="post-34508-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>if we take the timestamp that lies in the past let me say the last one or two weeks - then we usually gather more than 1000 records (in the global file) - and if wie drop all those records that do not contain a website - then we get - approx 100 in the results... what do you say? Now i try to make the posting above a bit more concrete. And i would be more than happy if you can show me how i got stuck - so that i can finally go there and write down the full osmconvert request. - Scai i look forward to any and all help - greetings say helloi</p>
</div>
<div id="comment-34508-info" class="comment-info">
<span class="comment-age">(01 Jul '14, 19:29)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
<span id="34509"></span>
<div id="comment-34509" class="comment">
<div id="post-34509-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I'm not a friend of editing the question over and over again. This doesn't make things clearer.</p>
</div>
<div id="comment-34509-info" class="comment-info">
<span class="comment-age">(01 Jul '14, 19:49)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="34510"></span>
<div id="comment-34510" class="comment not_top_scorer">
<div id="post-34510-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hmm - i understand. what should i do now... i think that i have some dificulties in expressing the necesary conditions in a osmconvert-request. the tooolchain is a bit tricky - what do you say. in short; i need to gather the latest 100 records from south america - best would be a relatively full dataset (therefore in want to exclude all non-website-records) .... Guess that i need to add a timestamp into the search-request. BTW - did not take into account if this would be gained with overpasss-api - too</p>
</div>
<div id="comment-34510-info" class="comment-info">
<span class="comment-age">(01 Jul '14, 20:00)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
</div>
<div id="comment-tools-34477" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-34477-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

