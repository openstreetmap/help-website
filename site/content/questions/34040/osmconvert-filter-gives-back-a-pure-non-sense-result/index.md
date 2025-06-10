+++
type = "question"
title = "osmconvert -filter gives back a pure non-sense result"
description = '''did a request with the following  in order to filter &amp;amp; gather the schools - but believe me: the results in the cal-sheets were looking like pure none - sense... update: thanks to someoneElse i have corrected the code for the request regarding danish shools:  ./osmconvert denmark-latest.osm.pbf -...'''
date = "2014-06-17T18:30:00Z"
lastmod = "2014-06-17T20:54:00Z"
weight = 34040
keywords = [ "overpass", "linux", "osm", "mysql" ]
aliases = [ "/questions/34040" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [osmconvert -filter gives back a pure non-sense result](/questions/34040/osmconvert-filter-gives-back-a-pure-non-sense-result)

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
<span id="post-34040-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-34040-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-34040-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>did a request with the following</p>
<p>in order to filter &amp; gather the schools - but believe me: the results in the cal-sheets were looking like pure none - sense...</p>
<p>update: thanks to someoneElse i have corrected the code for the request regarding danish shools:</p>
<pre><code>./osmconvert denmark-latest.osm.pbf -o=denmark.o5m
./osmfilter denmark.o5m --keep=&quot;amenity=school&quot; -o=denmarkschools.o5m
./osmconvert denmarkschools.o5m --csv=&quot;@id @lon @lat name addr:street addr:housenumber addr:city website email&quot; --csv-headline -o=denmarkschools_3.csv</code></pre>
<p>now the results are a bit better!!!</p>
<p>end of the update: see the code:</p>
<p>denmark</p>
<pre><code>./osmconvert denmark-latest.osm.pbf -o=denmark.o5m
./osmfilter denmark.o5m --keep=&quot;amenity=school&quot; -o=denmarkschools.o5m
./osmconvert denmarkschools.o5m --csv=&quot;@id @lon @lat restaurant:name addr:street addr:housenumber addr:city website email&quot; --csv-headline -o=denmarkschools_2.csv
--csv-headline -o=denmarkschools_2.csv</code></pre>
<p>luxembourg</p>
<pre><code>./osmconvert luxembourg-latest.osm.pbf -o=luxembourg-schools.o5m
./osmfilter luxembourg-schools.o5m --keep=&quot;amenity=school&quot; -o=luxschools.o5m
./osmconvert luxschools.o5m --csv=&quot;@id @lon @lat schools:name addr:street addr:housenumber addr:city website email&quot; --csv-headline -o=luxschools_2.csv</code></pre>
<p>hamburg: ./osmconvert hamburg-latest.osm.pbf -o=hh-schools.o5m ./osmfilter hh-schools.o5m --keep="amenity=school" -o=all_hh_schools.o5m ./osmconvert all_hh_schools.o5m --csv="<span><span><span><span>@id</span></span></span></span> <span><span><span><span>@lon</span></span></span></span> <span><span><span><span>@lat</span></span></span></span> schools:name addr:street addr:housenumber addr:city website email" --csv-headline -o=all_hh_schools_2.csv</p>
<p>i have no glue why !?</p>
<p>any help will be greatly appreciated</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-mysql" rel="tag" title="see questions tagged &#39;mysql&#39;">mysql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jun '14, 18:30</strong></p>
<img src="https://secure.gravatar.com/avatar/bf4d2d8660e82c4a7387b7d2a8a8cfcd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="say_hello_to_the_world&#39;s gravatar image" />
<p><span>say_hello_to...</span><br />
<span class="score" title="19 reputation points">19</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="say_hello_to_the_world has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jun '14, 20:53</strong> </span></p>
</div>
</div>
<div id="comments-container-34040" class="comments-container">
<span id="34041"></span>
<div id="comment-34041" class="comment">
<div id="post-34041-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>So you're extracting "restaurant:name" for Danish Schools? This seems a somewhat odd thing to do - taginfo only finds one:</p>
<p><a href="http://taginfo.openstreetmap.org/keys/restaurant:name">http://taginfo.openstreetmap.org/keys/restaurant:name</a></p>
<p>Can you define "crap"?</p>
</div>
<div id="comment-34041-info" class="comment-info">
<span class="comment-age">(17 Jun '14, 18:50)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="34047"></span>
<div id="comment-34047" class="comment">
<div id="post-34047-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>hello many thanks - you mean that i have a consistency-error; I will have a closer look at the lines....</p>
</div>
<div id="comment-34047-info" class="comment-info">
<span class="comment-age">(17 Jun '14, 20:28)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
<span id="34050"></span>
<div id="comment-34050" class="comment">
<div id="post-34050-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>updated the danish code - now the results look like a bit better... many thanks . conclusion,. it looks that i have made a systematic error - that i have written bad bad requests...</p>
</div>
<div id="comment-34050-info" class="comment-info">
<span class="comment-age">(17 Jun '14, 20:54)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
</div>
<div id="comment-tools-34040" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-34040-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

