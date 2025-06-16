+++
type = "question"
title = "Can the web interface show POIs?"
description = '''I know that Points Of Interest are in the database. Is it possible to see them in a browser? For example, I can search for &quot;campground&quot; in google maps and it will show them as little red dots. If this isn&#x27;t implemented, I would like to know is anyone working on this and what is the way this is plann...'''
date = "2012-10-08T23:13:00Z"
lastmod = "2017-08-01T11:07:00Z"
weight = 16741
keywords = [ "poi" ]
aliases = [ "/questions/16741" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Can the web interface show POIs?](/questions/16741/can-the-web-interface-show-pois)

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
<span id="post-16741-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16741-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-16741-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I know that Points Of Interest are in the database. Is it possible to see them in a browser? For example, I can search for "campground" in google maps and it will show them as little red dots.</p>
<p>If this isn't implemented, I would like to know is anyone working on this and what is the way this is planned to be implemented?</p>
<p>I know there is some derivation of openstreetmap at <a href="http://www.openstreetbrowser.org">http://www.openstreetbrowser.org</a>, but it has totally different tile rendering and many POIs don't show (like camping). Also many tiles are missing. Also I found a missing lake in California!</p>
<p>So any idea how to get similar functionality to openstreetmap?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Oct '12, 23:13</strong></p>
<img src="https://secure.gravatar.com/avatar/0b2f25d587c9ef215558ed14884ea603?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zubr&#39;s gravatar image" />
<p><span>zubr</span><br />
<span class="score" title="76 reputation points">76</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zubr has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Oct '12, 11:56</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-16741" class="comments-container">
&#10;</div>
<div id="comment-tools-16741" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16741-form-container" class="comment-form-container">
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

<span id="16748"></span>

<div id="answer-container-16748" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16748-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16748-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-16748-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The main page does show some POIs including camp sites (<a href="https://www.openstreetmap.org/?lat=37.93838&amp;lon=-119.24599&amp;zoom=17&amp;layers=M">example</a>), but not every possible <a href="https://wiki.openstreetmap.org/wiki/Map_Features">map feature</a> as this would make the map too cluttered.</p>
<p>The tile rendering style of <a href="https://wiki.openstreetmap.org/wiki/OpenStreetBrowser">OpenStreetBrowser</a> is just a configuration issue and many other maps also use slightly different styles for their tiles. There are also lots of other <a href="https://wiki.openstreetmap.org/wiki/List_of_OSM_based_Services">OSM based services</a>. Some are interactive like OpenStreetBrowser allowing to select specific POIs to show, like <a href="http://www.lenz-online.de/cgi-bin/osmpoi/osmpoi.pl">OSM POI Viewer</a> (standard rendering style) and <a href="http://www.flosm.de/en/POI-map.html">FLOSM</a> (custom rendering style). Others just have different POI rendering priorities like the <a href="http://hikebikemap.de/?lat=37.93838&amp;lon=-119.24599&amp;zoom=13&amp;layers=B0000TFFFF">Hike &amp; Bike map</a> where camp sites already show up at lower zoom levels.</p>
<p>There is also a list of current <a href="https://wiki.openstreetmap.org/wiki/Top_Ten_Tasks">Top Ten Tasks</a> including <a href="https://wiki.openstreetmap.org/wiki/Top_Ten_Tasks#Clickable_POIs_on_the_frontpage">clickable POIs on the frontpage</a>. This might also lead to different POI layers in the end, let's see.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Oct '12, 07:44</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-16748" class="comments-container">
&#10;</div>
<div id="comment-tools-16748" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16748-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16754"></span>

<div id="answer-container-16754" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16754-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16754-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-16754-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The front page of osm.org isn't supposed to be a "Google Maps replacement" - the standard map is just an example showing what you can do with the data.</p>
<p>There are a few other examples out there: <a href="http://open.mapquest.co.uk/">Mapquest Open</a> is one, and <a href="http://osm.dumoulin63.net/xapiviewer/?zoom=12&amp;lat=53.18599&amp;lon=-1.59566&amp;layers=B0T&amp;icon=icons%2Faccommodation_camping.n.32.png&amp;request=tourism%3Dcamp_site">this one</a> by <a href="https://help.openstreetmap.org/users/868/nicolasdumoulin">Nicolas Dumoulin</a> is another.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Oct '12, 12:07</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-16754" class="comments-container">
<span id="16758"></span>
<div id="comment-16758" class="comment">
<div id="post-16758-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Having many different sites each having various extra features implemented is horrible from the standpoint of promotion of the idea of openmaps to simple users. openstreetmap.org has nice maps but no POIs, openstretbrowser.org has one coloful map and some POIs and missing data, dimoulin63.net has yet one other rendering and 5 POI types display.</p>
<p>Which one should simple users (non-geeks) use that would like to use openmaps? Even for geeks, this isn't right.</p>
</div>
<div id="comment-16758-info" class="comment-info">
<span class="comment-age">(09 Oct '12, 16:58)</span> <span class="comment-user userinfo">zubr</span>
</div>
</div>
<span id="16761"></span>
<div id="comment-16761" class="comment">
<div id="post-16761-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I understand your frustration. I'm a centre-thinking person &amp; this whole project is quite frustrating to define. Right or wrong, OSM promoted itself as "Wikipedia of maps" - but it's only a database of geo-objects - a subset of this appears on the main map. The data is free for others to create their own maps, but the manner in which they render it is out of OSMs control. OSM has tried to be ordinary-person friendly, but firmly remains a geeky backwater. It doesn't want to be "mainstream". This identity confuses people, and I believe causes them to lose interest. Refer to OSMF for reasons why.</p>
</div>
<div id="comment-16761-info" class="comment-info">
<span class="comment-age">(09 Oct '12, 17:49)</span> <span class="comment-user userinfo">wolftracker</span>
</div>
</div>
<span id="16764"></span>
<div id="comment-16764" class="comment">
<div id="post-16764-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Both these comments are well-founded, but the hard fact is that it takes people to build all this good stuff. Clickable POIs have been a high-priority item on the <a href="https://wiki.openstreetmap.org/wiki/Top_Ten_Tasks">Top Ten Tasks</a> for a year now, and still no-one has stepped up to build it. Saying "it isn't right" is fine, but doesn't help to get the job done; we can't just magic features out of nowhere. Perhaps you could help?</p>
</div>
<div id="comment-16764-info" class="comment-info">
<span class="comment-age">(09 Oct '12, 18:46)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="16765"></span>
<div id="comment-16765" class="comment">
<div id="post-16765-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>@<a href="https://help.openstreetmap.org/users/4694/zubr">zubr</a>: The "but which one should I use" question <a href="http://en.wikipedia.org/wiki/The_Cathedral_and_the_Bazaar">isn't a new one</a>. The fundamental difference between e.g. Google Maps and OSM is that people here are volunteers. As <a href="https://help.openstreetmap.org/users/158/scai">scai</a> says, <a href="https://wiki.openstreetmap.org/wiki/Top_Ten_Tasks#Clickable_POIs_on_the_frontpage">clickable POIs on the frontpage</a> is on a list of "<a href="https://wiki.openstreetmap.org/wiki/Top_Ten_Tasks">top ten tasks</a>" - it "just" needs people to volunteer to help with it.</p>
<p>Incidentally, to correct a couple of points about <a href="http://osm.dumoulin63.net/xapiviewer/?zoom=12&amp;lat=53.18599&amp;lon=-1.59566&amp;layers=B0T&amp;icon=icons%2Faccommodation_camping.n.32.png&amp;request=tourism%3Dcamp_site">Nick Dumoulin's map</a> that I linked to - you can select from more than just the 5 canned queries - just select the "custom request" link, and it's not "yet another rendering" - it uses Mapquest tiles by default as a background or (if you select it) OSM's "standard" map.</p>
</div>
<div id="comment-16765-info" class="comment-info">
<span class="comment-age">(09 Oct '12, 19:02)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-16754" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16754-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16746"></span>

<div id="answer-container-16746" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16746-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16746-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16746-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi there! I've been experimenting a little bit with doing something like that, showing POIs on the map. I just have the problem that my laptop is a quite bit slow, and have overheating problems. But I might be able to continue my experiments on a friends computer. I guess that if it's good enough, they'll put it on the main OSM page.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Oct '12, 05:54</strong></p>
<img src="https://secure.gravatar.com/avatar/7daf187eb7d7f78223d8f7fc3743fe00?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="knarF&#39;s gravatar image" />
<p><span>knarF</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="knarF has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16746" class="comments-container">
&#10;</div>
<div id="comment-tools-16746" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16746-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="57406"></span>

<div id="answer-container-57406" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57406-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is a new website called <a href="http://www.mapcat.com">MAPCAT</a> that uses vector maps based on OSM and allows to show POI search results directly on the map in real time - just go to the website, zoom your map to your desired location and enter "restaurant" or "campsite" into search box in the top left corner of the page and the results will appear on the map immediately. Nice, isn't it?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Aug '17, 11:07</strong></p>
<img src="https://secure.gravatar.com/avatar/7d327873d48d28e563c9ad7259853c35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kozuch&#39;s gravatar image" />
<p><span>Kozuch</span><br />
<span class="score" title="1720 reputation points"><span>1.7k</span></span><span title="58 badges"><span class="badge1">●</span><span class="badgecount">58</span></span><span title="72 badges"><span class="silver">●</span><span class="badgecount">72</span></span><span title="85 badges"><span class="bronze">●</span><span class="badgecount">85</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kozuch has one accepted answer">8%</span></p>
</div>
</div>
<div id="comments-container-57406" class="comments-container">
&#10;</div>
<div id="comment-tools-57406" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57406-form-container" class="comment-form-container">
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

