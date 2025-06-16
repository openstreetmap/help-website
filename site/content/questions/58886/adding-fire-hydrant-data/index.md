+++
type = "question"
title = "Adding fire hydrant data"
description = '''I recently acquired data describing the location of several hundred fire hydrants in my hometown of Homer, Alaska. When I requested the data, I was under the impression it would be on the order of a few dozen, maybe even 100, hydrants and that I would add them manually. However, it turns out the ful...'''
date = "2017-08-31T09:19:00Z"
lastmod = "2017-09-07T23:31:00Z"
weight = 58886
keywords = [ "adding", "coordinates", "poi" ]
aliases = [ "/questions/58886" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Adding fire hydrant data](/questions/58886/adding-fire-hydrant-data)

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
<span id="post-58886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58886-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-58886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I recently acquired data describing the location of several hundred fire hydrants in my hometown of Homer, Alaska. When I requested the data, I was under the impression it would be on the order of a few dozen, maybe even 100, hydrants and that I would add them manually.</p>
<p>However, it turns out the full list contains about 450 fire_hydrants which is way too many to add manually. The data is in three columns of an Excel spreadsheet, namely Ref#, latitude, longitude.</p>
<p>What is the best way to add this data?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-adding" rel="tag" title="see questions tagged &#39;adding&#39;">adding</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Aug '17, 09:19</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-58886" class="comments-container">
&#10;</div>
<div id="comment-tools-58886" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-58886-form-container" class="comment-form-container">
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

<span id="58973"></span>

<div id="answer-container-58973" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-58973-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-58973-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-58973-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>One technical way to approach this is to write a script that generates an OSM file with 450 nodes, or if you cannot do that, perhaps save as .csv then use ogr2ogr (from the GDAL utilities suite) to convert into a shape file and then open that in JOSM.</p>
<p>What you're talking about here straddles the boundary between manual mapping and a data import. If you get a file with hydrants from your local fire dept. and you use that to aid your mapping, perhaps even adding them to OSM one by one and visually verifying they're in the right place then, at a couple 100 nodes, we could still say it's not a wholesale import, it's just a mapper exploring all available sources to map his home town. If however you plan to upload the lot to OSM in one go then you're clearly importing a data set and you should be clearing that with the imports mailing list and following the <a href="https://wiki.openstreetmap.org/wiki/Import/Guidelines">import guidelines</a>.</p>
<p>Whichever way you do it, be sure to attribute your source correctly, and check that the license is actually suitable for using the data in OSM. Just because you got something under some FOI request doesn't necessarily mean you have permission to distribute it further. They need to explicitly say it's public domain or it's ok for use in OSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Sep '17, 21:57</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-58973" class="comments-container">
<span id="59434"></span>
<div id="comment-59434" class="comment">
<div id="post-59434-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But what prevents from saying, that someone just walked through the city and put all data manually using GPS?</p>
</div>
<div id="comment-59434-info" class="comment-info">
<span class="comment-age">(06 Sep '17, 11:38)</span> <span class="comment-user userinfo">Sergey Karavay</span>
</div>
</div>
<span id="59435"></span>
<div id="comment-59435" class="comment">
<div id="post-59435-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The data in OSM MUST be based on freely available data (e.g. surveys, open source data), otherwise all of the users of OSM data would be in violation of the copyright of the original owner of the data (e.g. the Homer city council, for example). If the city council could prove that we copied their data in violation of their copyright they can sue OSM. One way to determine this is if they put intentional errors (e.g. a fictional fire hydrant) into their data (that's what mapping companies do) - if the same error then shows up on our map, it's fairly likely that we copied their data.</p>
</div>
<div id="comment-59435-info" class="comment-info">
<span class="comment-age">(06 Sep '17, 13:14)</span> <span class="comment-user userinfo">Lightsider</span>
</div>
</div>
<span id="59436"></span>
<div id="comment-59436" class="comment">
<div id="post-59436-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There has been a case where exactly this happened: Person takes location of hydrants from copyrighted provider's map, provider complains, we say "but the mapper has simply recorded what he saw" and provider says "well, hydrants A, K, and M are under ground and don't have signage so how exactly did you 'see' them"? - Busted! Don't do it. Don't talk about how data "could have been" recorded when it hasn't been.</p>
</div>
<div id="comment-59436-info" class="comment-info">
<span class="comment-age">(06 Sep '17, 13:38)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="59439"></span>
<div id="comment-59439" class="comment">
<div id="post-59439-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thaks for the replies - I will check with the city administration again. I did explain it fully to my contact person but I will get a document that will more firmly outline their permission.</p>
<p>Frederick mentioned "straddling the boundary" re: imports and I knew that when I asked for help. But I can tell you right now that if I have to write a full proposal to do this work, I'm going to forget about it. I have too much other stuff to do in Alaska. I'll add the hydrants that I can visually check as time allows.</p>
</div>
<div id="comment-59439-info" class="comment-info">
<span class="comment-age">(06 Sep '17, 14:10)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="59456"></span>
<div id="comment-59456" class="comment">
<div id="post-59456-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is it allowed to use the third-party list as the basis of a survey? I.e., to use that list as a checklist of places to physically visit? Or would that just be an expensive way of creating a dataset that's still a copyright violation? (E.g., because hydrants missing in the original data would also be missing in the OSM data)</p>
</div>
<div id="comment-59456-info" class="comment-info">
<span class="comment-age">(07 Sep '17, 07:40)</span> <span class="comment-user userinfo">dsh4</span>
</div>
</div>
<span id="59461"></span>
<div id="comment-59461" class="comment not_top_scorer">
<div id="post-59461-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/8996/dshimer">@dsh</a>: That should be fine. Missing data is not a problem for copyright - after all, our map is permanently incomplete. :)</p>
</div>
<div id="comment-59461-info" class="comment-info">
<span class="comment-age">(07 Sep '17, 09:09)</span> <span class="comment-user userinfo">Lightsider</span>
</div>
</div>
</div>
<div id="comment-tools-58973" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-58973-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="59445"></span>

<div id="answer-container-59445" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59445-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59445-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-59445-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Skipping over the nearly obligatory comments about compatible copyrights. . .</p>
<p>Excel data is easy to export as csv (comma separated value) files. From there, with a bit of munging with a reasonably capable text editor you can convert it to a GPX file (a flavor of XML).</p>
<p>Or if you have the tool set I have on my Mac (may be an equivalent one on Windows or Linux): I have a program called MacGPS Pro that I've used for decades for setting up my GPS for hiking, plotting my hikes on topo maps, etc. It's native format for storing waypoints happens to be tab separated values with a specific set of headers. It only takes me a couple of minute to covert a CSV file exported from Excel into the format needed by that program. Then it is an easy one, two, three process: 1) Load the waypoints into Mac GPS Pro. 2) Export waypoints as GPX file. 3) Load GPX file into JOSM.</p>
<p>I happen to be debugging an Android app that collects some geospatial data while I am out and about. I like to get the raw data into a map presentation of some sort to give me a quick visual check to see if it makes sense. Getting the data into a mapping program like MacGPS Pro or JOSM uses the above with only a couple of additional preliminary steps: Pull Sqlite database file from phone, using Sqlite3 on my laptop query the data to convert I want to text, then follow the same as above with a text editor. From the time I plug my phone in to my laptop to the point I am looking at thousands of lat/lon points overlay on top of an older USGS topo map is maybe two or three minutes. If I want to see what they look like with current building outlines, etc., then a quick export as GPX from GpsPro and import to JOSM allows that.</p>
<p>If you don't have the tool set needed to covert the file or the confidence to edit a CSV file into a GPX file, contact me off line and I can probably do the conversion in a couple of minutes and email you back the results.</p>
<p>EDIT: I think current US government data is NAD83. You may want to verify the datum used by the provider, I think states, counties and cities are likely to follow the national standard. NAD83 and WGS84 are not too different (continental plate movement in the last 30 years hasn't been that much) but you may still need to do a conversion on the data.</p>
<p>Also, an OSM file is also just a XML flavor and can be created with a text editor too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Sep '17, 16:41</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Sep '17, 16:48</strong> </span></p>
</div>
</div>
<div id="comments-container-59445" class="comments-container">
<span id="59448"></span>
<div id="comment-59448" class="comment">
<div id="post-59448-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks so much, stf, I will contact you separately about the data conversion. I had hoped perhaps GPSBabel could perform the conversion but a quick check suggests it cannot.</p>
<p>I know I could create a GPX file in a text editor but that's a lot of work when other mapping chores in Alaska are more pressing.</p>
<p>I checked several hydrant positions in person and believe the city's data to be more accurate than I can attain using my usual positioning methods which involve a GPS and camera.</p>
<p>Dave</p>
</div>
<div id="comment-59448-info" class="comment-info">
<span class="comment-age">(07 Sep '17, 03:09)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="59449"></span>
<div id="comment-59449" class="comment not_top_scorer">
<div id="post-59449-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>FWIW, if I want to position something fairly accurately I use the waypoint averaging feature of my low end Garmin eTrex. If you average the waypoint at different times so the satellite constellation is different you can get a fairly decent position recorded. Takes about 30 seconds for my unit to do an averaged waypoint (or to update one). I use this when hiking to collect the position of signs and trail junctions. If it is a "out and back" type of hike my return is usually at least a couple hours after my hike in so the GPS satellite positions will be different. Trail signs are not usually visible in satellite imagery and often trail junctions are hidden in the trees. If junctions are clearly visible in the imagery then I can use the junction waypoints to verify image alignment.</p>
<p>Anyway, a fire hydrant is a bit like a trail sign: Not usually visible on the satellite imagery but something you can set a GPS unit on top of before telling the unit to create or update an averaged waypoint.</p>
<p>All that said, I think I can convert your Excel data. I assume you are the same AlaskaDave that I see on the mail lists. . . If so, I'll send you an email so you can send me the data.</p>
</div>
<div id="comment-59449-info" class="comment-info">
<span class="comment-age">(07 Sep '17, 04:00)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="59450"></span>
<div id="comment-59450" class="comment">
<div id="post-59450-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>The <a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/OpenData">OpenData</a> plugin for JOSM can work with csv files</p>
</div>
<div id="comment-59450-info" class="comment-info">
<span class="comment-age">(07 Sep '17, 04:12)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="59451"></span>
<div id="comment-59451" class="comment not_top_scorer">
<div id="post-59451-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks escada! I did not know that. Just tried it and my last data from my app testing just came in perfectly. A far better workflow for me to use.</p>
<p>Seems like that will be the easiest way for AlaskaDave to import his fire hydrants.</p>
</div>
<div id="comment-59451-info" class="comment-info">
<span class="comment-age">(07 Sep '17, 04:34)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="59452"></span>
<div id="comment-59452" class="comment">
<div id="post-59452-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Another handy free conversion tool for csv to gpx is GPSVisualizer<br />
<a href="http://www.gpsvisualizer.com/convert_input">http://www.gpsvisualizer.com/convert_input</a></p>
</div>
<div id="comment-59452-info" class="comment-info">
<span class="comment-age">(07 Sep '17, 04:36)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="59453"></span>
<div id="comment-59453" class="comment">
<div id="post-59453-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I tried the Opendata plugin but it failed complaining that it was "unable to find any valid coordinates" My CSV file is simple, three comma-separated columns, a ref column, latitude column and longitude column containing coordinates in decimal degrees. (???)</p>
<p>But the GPS visualizer convert page worked like a charm. So that part of the job is now behind me.</p>
<p><a href="https://help.openstreetmap.org/users/5918/stf"></a><a href="https://help.openstreetmap.org/users/5918/stf">@stf</a>, I have used the averaging feature of my Garmin before. Time consuming so I don't use it often. And thanks for your offer of conversion but gpsvisualizer did the trick.</p>
<p>Many thanks to all contributors.</p>
<p>Dave</p>
</div>
<div id="comment-59453-info" class="comment-info">
<span class="comment-age">(07 Sep '17, 06:08)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="59468"></span>
<div id="comment-59468" class="comment not_top_scorer">
<div id="post-59468-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Interesting, the header on my cvs file that loaded perfectly was: "id","type","guard","lat","lon","radius"</p>
<p>Maybe the lat/lon have to be abbreviated. Or maybe the quotes need to be there even if there is no particular csv reason for them in this case.</p>
</div>
<div id="comment-59468-info" class="comment-info">
<span class="comment-age">(07 Sep '17, 15:36)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="59478"></span>
<div id="comment-59478" class="comment">
<div id="post-59478-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I considered adding quotes around the values too but gpsvisualizer saved me the trouble.</p>
<p>Thanks again stf</p>
</div>
<div id="comment-59478-info" class="comment-info">
<span class="comment-age">(07 Sep '17, 23:31)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
</div>
<div id="comment-tools-59445" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-59445-form-container" class="comment-form-container">
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

