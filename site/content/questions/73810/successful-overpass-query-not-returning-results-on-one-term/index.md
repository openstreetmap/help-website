+++
type = "question"
title = "Successful Overpass query not returning results on one term"
description = '''Folks, I&#x27;m trying to get some data out of OSM using Overpass for a beta corona community leaflet distribution process. My aim is to eventually have a spreadsheet with the streets in 2 areas, lat/long data - then push that data to a map so folks can visualise which streets have been done.  I managed ...'''
date = "2020-03-28T13:53:00Z"
lastmod = "2020-03-30T12:26:00Z"
weight = 73810
keywords = [ "overpass" ]
aliases = [ "/questions/73810" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Successful Overpass query not returning results on one term](/questions/73810/successful-overpass-query-not-returning-results-on-one-term)

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
<span id="post-73810-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73810-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73810-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Folks, I'm trying to get some data out of OSM using Overpass for a beta corona community leaflet distribution process. My aim is to eventually have a spreadsheet with the streets in 2 areas, lat/long data - then push that data to a map so folks can visualise which streets have been done.</p>
<p>I managed to get the query below to return results for <a href="https://www.openstreetmap.org/search?query=hollingdean#map=14/50.8443/-0.1281">Hollingdean</a>, but not <a href="https://www.openstreetmap.org/search?query=hollingbury#map=19/50.85628/-0.12390">Hollingbury</a>.</p>
<p>I'm a bit of a beginner to this (only come to Overpass API for this project), but I fiddled around a bit trying to get the ID of "Hollingbury" suburb to work and it didn't. Then I decided that it was due to the fact that maybe the Hollingbury search didn't show up any areas. I've now labelled an area (that was already drawn up) as Hollingbury, so the search pulls up an area, but still no search results returned.</p>
<ul>
<li>Am I correct in the assumption that this search is searching for a residential area?</li>
<li>If yes, are the lack of results due to the system not being updated with the new label? This was done about 18hrs ago.</li>
<li>If no, what am I doing wrong? Why am I not getting any results for the "Hollingbury" search?</li>
<li>Finally, any folks have a way of interfacing spreadsheets (online) with a map? Google used to have a <a href="https://www.google.com/earth/outreach/learn/mapping-from-a-google-spreadsheet/">Spreadsheet Mapper</a> but due to changes in the way that kml files work, I have to faff around importing into Google Earth then Maps, with a bunch of formatting lost in the process. An OSM solution would be great!</li>
</ul>
<p>Thanks very much in advance for your help!</p>
<pre><code>[out:csv(&quot;name&quot;, ::type, ::id, ::lat, ::lon)]
[timeout:25];
area[name=&quot;Hollingbury&quot;];
way(area)[highway][name];
foreach(           // for each way tagged as highway=* do...
  out center;             // output way id
);</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Mar '20, 13:53</strong></p>
<img src="https://secure.gravatar.com/avatar/6708dd35358365ab722eca934ab1ed21?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jt196&#39;s gravatar image" />
<p><span>jt196</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jt196 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73810" class="comments-container">
<span id="73812"></span>
<div id="comment-73812" class="comment">
<div id="post-73812-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Scratch that, either the DB was updated or I needed to refresh the page with another query, it's working now.</p>
<p>Any answers to my spreadsheet question, or do I have to figure out another API!? ;)</p>
</div>
<div id="comment-73812-info" class="comment-info">
<span class="comment-age">(28 Mar '20, 14:37)</span> <span class="comment-user userinfo">jt196</span>
</div>
</div>
<span id="73820"></span>
<div id="comment-73820" class="comment">
<div id="post-73820-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There are some leaflet plugins that will display a csv on a map. Haven't used one, so can't say if it works nice or not.</p>
<p>The repeated results come from the OSM data model. If something like the surface of the street varies, a new way is created for each different part. Depending on the scale of what you are doing, you may want to evaluate each one manually.</p>
<p>If you have many regions, there might be a way to get combined centers using aggregation functions: <a href="https://dev.overpass-api.de/blog/flat_world.html">https://dev.overpass-api.de/blog/flat_world.html</a></p>
</div>
<div id="comment-73820-info" class="comment-info">
<span class="comment-age">(28 Mar '20, 19:51)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="73822"></span>
<div id="comment-73822" class="comment">
<div id="post-73822-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/18100/jt196">@jt196</a>: Please use the "add new comment" function or edit your question if you have additional questions or information. "Your answer" is reserved for answers resolving your question.</p>
</div>
<div id="comment-73822-info" class="comment-info">
<span class="comment-age">(28 Mar '20, 20:43)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="73832"></span>
<div id="comment-73832" class="comment">
<div id="post-73832-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I see what I've done there - I know the format, but assumed it was just usual forum rules. Can I reformat the answers to make it clearer?</p>
</div>
<div id="comment-73832-info" class="comment-info">
<span class="comment-age">(29 Mar '20, 12:24)</span> <span class="comment-user userinfo">jt196</span>
</div>
</div>
</div>
<div id="comment-tools-73810" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73810-form-container" class="comment-form-container">
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

<span id="73813"></span>

<div id="answer-container-73813" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73813-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73813-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73813-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Strange. I'm still getting an error atm.</p>
<p>Note, the <code>foreach</code> &amp; [name] isn't required &amp; I've removed <code>::type</code> as only ways are being searched for.</p>
<pre><code>[out:csv(&quot;name&quot;, ::id, ::lat, ::lon)];
area[name=&quot;Hollingdean&quot;];
way(area)[highway];
out center;</code></pre>
<p>What output format is needed? The lat/lon is the approximate centre point of linear ways. Would this be more useful (Click on the Data tab):</p>
<pre><code>area[name=Hollingdean][landuse=residential]-&gt;.Suburb;
way[highway](area.Suburb);
out meta geom;
way(pivot.Suburb);
out geom;
&#10;//Hollingdean
//Hollingbury
&#10;{{style: 
way[highway] {color:green}
}}</code></pre>
<p>Also, check out the 'export' tools.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Mar '20, 15:42</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-73813" class="comments-container">
<span id="73815"></span>
<div id="comment-73815" class="comment">
<div id="post-73815-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for this Dave!</p>
<p>The idea was to import it into a google spreadsheet in the following format:</p>
<p>area road name Latitude Longitude Hollingbury Bavant Road 50.8447577 -0.1484516</p>
<p>ID isn't super essential.</p>
<p>I need every road in the area - including ones on the border of the area, so I don't know whether I'd need to add any other search criteria or not?</p>
<p>I added the foreach command as I was getting multiple outputs for each street, that seemed to limit it to one (aside from a limited number of cases).</p>
<pre><code>[out:csv(&quot;name&quot;, ::id, ::lat, ::lon)];
area[name=Hollingdean][landuse=residential]-&gt;.Suburb;
way[highway](area.Suburb);
out meta geom;
way(pivot.Suburb);
out geom;
&#10;//Hollingdean
//Hollingbury
&#10;{{style: 
way[highway] {color:green}
}}</code></pre>
<p>Excuse the cut and paste ninja work, I'm really new at this, and having a little difficulty getting my head around the code, despite having read the manual!</p>
<p>This seems to work but I get this kind of output:</p>
<pre><code>Lambourne Close 4748228 50.8447944  -0.1231223
    4748229 50.8461658  -0.1205447
    4748230 50.8439343  -0.1232559
    4748231 50.8438419  -0.1229539
    4748232 50.8441320  -0.1229460
    etc</code></pre>
</div>
<div id="comment-73815-info" class="comment-info">
<span class="comment-age">(28 Mar '20, 16:17)</span> <span class="comment-user userinfo">jt196</span>
</div>
</div>
<span id="73816"></span>
<div id="comment-73816" class="comment">
<div id="post-73816-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Exporting data is great but I really need a way of casual folk being able to interact with the information, hence me extracting the data, then adding it to an online spreadsheet in order for folk to be able to edit. Importing that info into Gmaps is pretty straightforward after, even though I'd prefer not to use it.</p>
</div>
<div id="comment-73816-info" class="comment-info">
<span class="comment-age">(28 Mar '20, 16:20)</span> <span class="comment-user userinfo">jt196</span>
</div>
</div>
<span id="73819"></span>
<div id="comment-73819" class="comment">
<div id="post-73819-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah, I made a slight mistake, where I said you didn't need 'name'. way(area)[highway][name]; &lt; this line returns all ways with a 'highway' tag that have a 'name' tag. This may be what you want, but it could include footways, tracks etc. Alternatively use way(area)[highway=residential]; which will restrict it to just residential roads. There is one without a name. if you know it please add it: <a href="https://www.openstreetmap.org/way/4747413">https://www.openstreetmap.org/way/4747413</a></p>
</div>
<div id="comment-73819-info" class="comment-info">
<span class="comment-age">(28 Mar '20, 19:41)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="73821"></span>
<div id="comment-73821" class="comment">
<div id="post-73821-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In your latest output what your seeing is one named way &amp; a few unnamed ways (probably footways). '4748229' are the IDs. Try this: <a href="https://overpass-turbo.eu/s/S1C.">https://overpass-turbo.eu/s/S1C.</a> I've removed the first line header (with 'false') &amp; added ";" so it returns comma separated data.</p>
</div>
<div id="comment-73821-info" class="comment-info">
<span class="comment-age">(28 Mar '20, 19:56)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="73833"></span>
<div id="comment-73833" class="comment">
<div id="post-73833-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Dave I've added the street name (pulled from another source).</p>
<p>Your link had a "." at the end so confused me for a bit. Looks like it's working fine and dandy now thanks very much!</p>
<p>As I found before, when you change the search term (Hollingdean to Hollingbury), the Overpass API outputs nothing, then if you run one of the sample queries, then paste back in an updated query, it works again.</p>
</div>
<div id="comment-73833-info" class="comment-info">
<span class="comment-age">(29 Mar '20, 12:31)</span> <span class="comment-user userinfo">jt196</span>
</div>
</div>
<span id="73857"></span>
<div id="comment-73857" class="comment not_top_scorer">
<div id="post-73857-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So, this was the working answer from Dave:</p>
<pre><code>[out:csv(&quot;name&quot;, ::lat, ::lon; false; &quot;,&quot;)];
area[name=Hollingdean][landuse=residential];
way[highway=residential](area);
out geom;</code></pre>
</div>
<div id="comment-73857-info" class="comment-info">
<span class="comment-age">(30 Mar '20, 12:26)</span> <span class="comment-user userinfo">jt196</span>
</div>
</div>
</div>
<div id="comment-tools-73813" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-73813-form-container" class="comment-form-container">
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

