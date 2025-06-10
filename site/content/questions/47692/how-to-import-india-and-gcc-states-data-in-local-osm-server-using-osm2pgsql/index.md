+++
type = "question"
title = "How to import India and GCC States data in local OSM server using osm2pgsql?"
description = '''Hi, How to import India and GCC States data in local OSM server using osm2pgsql?'''
date = "2016-01-28T08:52:00Z"
lastmod = "2016-02-02T19:57:00Z"
weight = 47692
keywords = [ "import", "data", "two", "for", "countries" ]
aliases = [ "/questions/47692" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to import India and GCC States data in local OSM server using osm2pgsql?](/questions/47692/how-to-import-india-and-gcc-states-data-in-local-osm-server-using-osm2pgsql)

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
<span id="post-47692-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47692-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47692-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>How to import India and GCC States data in local OSM server using osm2pgsql?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span> <span class="post-tag tag-link-two" rel="tag" title="see questions tagged &#39;two&#39;">two</span> <span class="post-tag tag-link-for" rel="tag" title="see questions tagged &#39;for&#39;">for</span> <span class="post-tag tag-link-countries" rel="tag" title="see questions tagged &#39;countries&#39;">countries</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jan '16, 08:52</strong></p>
<img src="https://secure.gravatar.com/avatar/1a9eea008bc0c9a26985aa042d9b8ac2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Reshma%20Maner&#39;s gravatar image" />
<p><span>Reshma Maner</span><br />
<span class="score" title="235 reputation points">235</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Reshma Maner has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47692" class="comments-container">
<span id="47693"></span>
<div id="comment-47693" class="comment">
<div id="post-47693-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could you explain what GCC States is? Is it Gulf Cooperation Council States?</p>
</div>
<div id="comment-47693-info" class="comment-info">
<span class="comment-age">(28 Jan '16, 08:53)</span> <span class="comment-user userinfo">rorym</span>
</div>
</div>
<span id="47696"></span>
<div id="comment-47696" class="comment">
<div id="post-47696-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes. It is Gulf Cooperation Council States</p>
</div>
<div id="comment-47696-info" class="comment-info">
<span class="comment-age">(28 Jan '16, 08:57)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
</div>
<div id="comment-tools-47692" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47692-form-container" class="comment-form-container">
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

<span id="47737"></span>

<div id="answer-container-47737" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47737-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47737-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-47737-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Download both country files &amp; merge them with <a href="http://wiki.openstreetmap.org/wiki/Osmconvert#Merging_two_or_more_Geographical_Areas">osmconvert</a> (easier to use, as has fewer dependencies, but less functional, than Osmosis). Then import using osm2pgsql.</p>
<p>Note that if you want to add additional countries with shared borders you will most likely have to reimport all the data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jan '16, 14:20</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-47737" class="comments-container">
<span id="47752"></span>
<div id="comment-47752" class="comment">
<div id="post-47752-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can I not use osm2pgsql --append option to import the second pbf file?</p>
</div>
<div id="comment-47752-info" class="comment-info">
<span class="comment-age">(30 Jan '16, 10:25)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
<span id="47753"></span>
<div id="comment-47753" class="comment">
<div id="post-47753-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You can try it. Don't expect it to work at a reasonable speed, though - much faster to merge first and then load.</p>
<p>(or at least it was when I last tried it, and looked at the "append" code in osm2pgsql, around 3 years ago).</p>
</div>
<div id="comment-47753-info" class="comment-info">
<span class="comment-age">(30 Jan '16, 10:33)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="47778"></span>
<div id="comment-47778" class="comment">
<div id="post-47778-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How to merge .osm.pbf files. If I merge two files with these extensions and pass the merged file to osm2pgsql command, it gives error</p>
</div>
<div id="comment-47778-info" class="comment-info">
<span class="comment-age">(01 Feb '16, 07:38)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
<span id="47780"></span>
<div id="comment-47780" class="comment not_top_scorer">
<div id="post-47780-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Which error? And how did you merge them?</p>
</div>
<div id="comment-47780-info" class="comment-info">
<span class="comment-age">(01 Feb '16, 08:05)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="47784"></span>
<div id="comment-47784" class="comment">
<div id="post-47784-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>osmconvert india-latest.osm.pbf gcc-states-latest.osm.pbf -o=newmap.osm.pbf osmconvert Error: more than one .pbf input file is not allowed.</p>
</div>
<div id="comment-47784-info" class="comment-info">
<span class="comment-age">(01 Feb '16, 09:24)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
<span id="47810"></span>
<div id="comment-47810" class="comment not_top_scorer">
<div id="post-47810-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi,</p>
<p>Can somebody help?</p>
</div>
<div id="comment-47810-info" class="comment-info">
<span class="comment-age">(02 Feb '16, 09:54)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
<span id="47811"></span>
<div id="comment-47811" class="comment not_top_scorer">
<div id="post-47811-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe osmconvert can't merge PBF files directly and you have to convert them to another format before. Just a guess.</p>
</div>
<div id="comment-47811-info" class="comment-info">
<span class="comment-age">(02 Feb '16, 10:07)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="47812"></span>
<div id="comment-47812" class="comment not_top_scorer">
<div id="post-47812-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I did that too. I first converted both the pbf files to .osm files. Then merged the two .osm files into single one. Then converted back .osm to .osm.pbf.</p>
<p>But osm2pgsql command does not work with such created file.</p>
</div>
<div id="comment-47812-info" class="comment-info">
<span class="comment-age">(02 Feb '16, 10:19)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
<span id="47823"></span>
<div id="comment-47823" class="comment">
<div id="post-47823-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Following steps work for me:</p>
<p>osmconvert gcc-state-latest.osm.pbf --out-o5m &gt;gcc.o5m osmconvert india-latest.osm.pbf --out-o5m &gt;india.o5m osmconvert india.o5m gcc.o5m --out-o5m &gt; merged.o5m osmconvert merged.o5m --out-pbf &gt;merged.pbf osm2pgsql -U postgres -d osm --host localhost -S default.style -s -C 500 -k merged.pbf</p>
<p>The discrete conversion of the merged file from o5m to pbf might be doable in one step.</p>
</div>
<div id="comment-47823-info" class="comment-info">
<span class="comment-age">(02 Feb '16, 19:57)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-47737" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-47737-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47694"></span>

<div id="answer-container-47694" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47694-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47694-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47694-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can download the full OSM planet file from planet.openstreetmap.org, and then use <a href="http://wiki.openstreetmap.org/wiki/Osmosis">osmosis</a> to <a href="http://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.44#--bounding-polygon_.28--bp.29">clip out the polygon(s) you want</a>. You'll be left with a pbf file which you can import with osm2psql.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jan '16, 08:54</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jan '16, 08:55</strong> </span></p>
</div>
</div>
<div id="comments-container-47694" class="comments-container">
<span id="47695"></span>
<div id="comment-47695" class="comment">
<div id="post-47695-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can I not download two pbf files from geofabrik one for India and one for Gcc states and import both of them?</p>
<p>Do I need to install osmosis? How to do that?</p>
</div>
<div id="comment-47695-info" class="comment-info">
<span class="comment-age">(28 Jan '16, 08:56)</span> <span class="comment-user userinfo">Reshma Maner</span>
</div>
</div>
<span id="47697"></span>
<div id="comment-47697" class="comment">
<div id="post-47697-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The pbf files on Geofabrik don't follow exactly the borders of the respective countries, they simplify and go into the next country by maybe a few hundred metres, or so. Everything in the country is in the pbf file, but so is stuff from the neighbouring country. Hence importing 2 pbfs from countries that border each other will probably display OK for generating tiles, but not be very useful for say OSRM routing. India and GCC states appear to share no border, so that would be less of a problem</p>
</div>
<div id="comment-47697-info" class="comment-info">
<span class="comment-age">(28 Jan '16, 09:58)</span> <span class="comment-user userinfo">rorym</span>
</div>
</div>
<span id="47698"></span>
<div id="comment-47698" class="comment">
<div id="post-47698-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can download osmosis here <a href="http://wiki.openstreetmap.org/wiki/Osmosis#Downloading">http://wiki.openstreetmap.org/wiki/Osmosis#Downloading</a></p>
</div>
<div id="comment-47698-info" class="comment-info">
<span class="comment-age">(28 Jan '16, 09:58)</span> <span class="comment-user userinfo">rorym</span>
</div>
</div>
<span id="47755"></span>
<div id="comment-47755" class="comment">
<div id="post-47755-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://extract.bbbike.org">http://extract.bbbike.org</a> offers extracts of self defined areas in one file but there is a size limit</p>
</div>
<div id="comment-47755-info" class="comment-info">
<span class="comment-age">(30 Jan '16, 11:42)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
</div>
<div id="comment-tools-47694" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47694-form-container" class="comment-form-container">
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

