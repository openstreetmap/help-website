+++
type = "question"
title = "How to display an OSM map in a piece of software ?"
description = '''Hello, I would like to create a piece of software (with VB preferably) which displays maps offline. So, it seems that the best solution is OpenStreetMap. But the question is : how to use a OSM bin file in a program, like Navit software does ? Do you know some tools (API, SDK, ...) which allow to inc...'''
date = "2011-11-07T17:54:00Z"
lastmod = "2011-11-10T13:01:00Z"
weight = 8869
keywords = [ "development", "sdk", "display", "software" ]
aliases = [ "/questions/8869" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to display an OSM map in a piece of software ?](/questions/8869/how-to-display-an-osm-map-in-a-piece-of-software)

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
<span id="post-8869-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8869-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8869-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I would like to create a piece of software (with VB preferably) which displays maps offline. So, it seems that the best solution is OpenStreetMap. But the question is : how to use a OSM bin file in a program, like Navit software does ? Do you know some tools (API, SDK, ...) which allow to include an OSM map in a piece of software ?</p>
<p>Is there a documeentation about the file structure of OSM files ?</p>
<p>Louis</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-sdk" rel="tag" title="see questions tagged &#39;sdk&#39;">sdk</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span> <span class="post-tag tag-link-software" rel="tag" title="see questions tagged &#39;software&#39;">software</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Nov '11, 17:54</strong></p>
<img src="https://secure.gravatar.com/avatar/d00ddaf5f11a01486629fc761df861a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="louis10&#39;s gravatar image" />
<p><span>louis10</span><br />
<span class="score" title="30 reputation points">30</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="louis10 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Nov '11, 09:51</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-8869" class="comments-container">
<span id="8890"></span>
<div id="comment-8890" class="comment">
<div id="post-8890-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As I am totally new in maps, I don't fully understand all the comments. Here is that I understand.</p>
<p>I just would like to draw maps (without interest points, pubs, ...), only maps (with streets, roads, highways, rivers, maybe railways). Just in order to know where I am in a car. I don't want to deploy any software.</p>
<p>I understand that I can download OSM data files, so which file extension(s) ? There are a lot : 7z, bz2, ... If we download tile files without knowning it, are we aware of the licence problem when downloading ?</p>
<p>With your explanations, I still don't know if downloading Navit files is good or not. Same for .7z files.</p>
<p>NaviPOWM seems interesting but it doesn't work on Windows (missing file QtCore4.dll) and, moreover, the source code is not downloaded. I understand that this point is external to your site but how to get the code ?</p>
<p>Last question : why did somebody change "software" to "piece of software", and maybe other words ? What is the meaning ?</p>
</div>
<div id="comment-8890-info" class="comment-info">
<span class="comment-age">(08 Nov '11, 19:12)</span> <span class="comment-user userinfo">louis10</span>
</div>
</div>
<span id="8891"></span>
<div id="comment-8891" class="comment">
<div id="post-8891-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When you say "know where I am in a car" do you mean "so that I can see my current position superimposed on a picture of where I am" or "so that my software can work out how to get from where I am to somewhere else"?<br />
</p>
<p>That's the key question, but I'm guessing from what you've said above that you just want a picture of where you are, and so may be able to make do with tiles - with the caveat as mentioned previously that bulk downloading from the OSM site isn't an option.</p>
</div>
<div id="comment-8891-info" class="comment-info">
<span class="comment-age">(08 Nov '11, 20:23)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="8892"></span>
<div id="comment-8892" class="comment">
<div id="post-8892-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not knowing exactly what you want to do and not being familar with Navit's binfile format (beyond Vclaw's link) I can't say whether that's ideal for your purposes or not - it may (if you just need what we refer to as "tiles") overcomplicate things.</p>
</div>
<div id="comment-8892-info" class="comment-info">
<span class="comment-age">(08 Nov '11, 20:35)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="8893"></span>
<div id="comment-8893" class="comment">
<div id="post-8893-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Finally - I plead guilty to changing "a software" to "a piece of software" in the question. That's because there's no such thing as "a software" in English (it's a funny language) - in the sentence "I work for a company that sells software" the word "software" is a singular noun that refers to multiple items, hence commonly used constructions such as "a piece of ..." to indicate just one.</p>
</div>
<div id="comment-8893-info" class="comment-info">
<span class="comment-age">(08 Nov '11, 20:36)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="8894"></span>
<div id="comment-8894" class="comment">
<div id="post-8894-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When I say "to know where I am in my car", I mean "just to see my current position on a map". Help for navigation to go somewhere else is not interesting for me, I prefer to ... improvise and search my way by myself ! But from a position ... And the main feature I'll forecast is the recording (in any simple text file) of a position (longitude+latitude) which I found interesting. I don't need other functions.</p>
<p>To do that, are tiles necessary ?</p>
<p>I forgot to mention that I also need street and city names in addition to roads and rivers.</p>
</div>
<div id="comment-8894-info" class="comment-info">
<span class="comment-age">(09 Nov '11, 18:20)</span> <span class="comment-user userinfo">louis10</span>
</div>
</div>
<span id="8895"></span>
<div id="comment-8895" class="comment not_top_scorer">
<div id="post-8895-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I mentioned Navit because that's the 1st free "software" (or program !) that I found, with free maps proposed on the site <a href="http://maps7.navit-project.org">http://maps7.navit-project.org</a> (so, I did not wonder anything about policy), which works offline, and works on Windows and Windows Mobile. But it is not suitable for me because of the user interface.</p>
<p>As I found many free softwares, I supposed that creating a software is not too difficult ! Otherwise, they would be not free of charge.</p>
</div>
<div id="comment-8895-info" class="comment-info">
<span class="comment-age">(09 Nov '11, 18:31)</span> <span class="comment-user userinfo">louis10</span>
</div>
</div>
<span id="8896"></span>
<div id="comment-8896" class="comment not_top_scorer">
<div id="post-8896-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As you suppose, English is not my usual language. But I did not think that "software" was not correct, or funny, or a familiar word. In information technology, we can see everywhere "software engineer", "software development", "software package", ... ! Do English and American people think or speak in the same way ? So "program" seems more suitable... In French, we say "logiciel" but it seems that "software" is now a french word ! Dictionaries include this word. But we are making a digression ... Generally not accepted in forums.</p>
</div>
<div id="comment-8896-info" class="comment-info">
<span class="comment-age">(09 Nov '11, 18:50)</span> <span class="comment-user userinfo">louis10</span>
</div>
</div>
<span id="8898"></span>
<div id="comment-8898" class="comment not_top_scorer">
<div id="post-8898-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you just want to see your location superimposed on a picture of where you are, then tiles may be the way to go. To get familiar with how these can be created from OSM data, and how different style rules can be used to create different-looking maps, I'd have a play with something such as Maperitive (<a href="http://maperitive.net/).">http://maperitive.net/).</a> You can also use that to generate tiles at whatever zoom level you like for your new offline map application, when you need them.</p>
</div>
<div id="comment-8898-info" class="comment-info">
<span class="comment-age">(09 Nov '11, 21:46)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="8903"></span>
<div id="comment-8903" class="comment not_top_scorer">
<div id="post-8903-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So, if I'll use tiles files as you advise, I'll be "exposed" to the policy, isn't it ? Even if my application is installed only on my computer and my phone.</p>
</div>
<div id="comment-8903-info" class="comment-info">
<span class="comment-age">(10 Nov '11, 11:08)</span> <span class="comment-user userinfo">louis10</span>
</div>
</div>
<span id="8904"></span>
<div id="comment-8904" class="comment not_top_scorer">
<div id="post-8904-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Generate your own tiles and you're not bound by OSM's tile usage policy because you're not using OSM tiles. You're bound by the terms described on <a href="https://www.openstreetmap.org/copyright">https://www.openstreetmap.org/copyright</a> , but that's pretty easy to do.</p>
</div>
<div id="comment-8904-info" class="comment-info">
<span class="comment-age">(10 Nov '11, 13:01)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-8869" class="comment-tools">
<span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-8869-form-container" class="comment-form-container">
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

<span id="8872"></span>

<div id="answer-container-8872" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8872-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8872-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-8872-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You'll find plenty of information in the wiki. The osm format is explained <a href="https://wiki.openstreetmap.org/wiki/.osm">here</a>. Follow the category links at the bottom of that page to get info on other formats, tools, libraries, etc.</p>
<p>Programming your own rendering from osm data can be a dauting task (altough very interesting), especially if you're rather new to programming (sorry for my bias, that's what the mention of VB triggers). Note that there are tons of existing software for all kinds of usages (again, see wiki). Maybe if you have an itch to scratch which isn't served by existing software, you'd be better off improving said software instead of starting from nothing ?</p>
<p>If on the other hand you're mainly interested by the fun of learning, then go ahead and dive in, start from scratch :) But be prepared to spend a lot of time in the wiki at first.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Nov '11, 18:36</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span> </br></p>
</div>
</div>
<div id="comments-container-8872" class="comments-container">
<span id="8875"></span>
<div id="comment-8875" class="comment">
<div id="post-8875-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the information.</p>
<p>The osm format is explained in the above link but what about the OSM bin file we can download from <a href="http://maps7.navit-project.org">http://maps7.navit-project.org</a> ?</p>
<p>And ... don't worry, even if I like to use VB, I'm not new in programming ! :) . That's my job. But I'm new in maps and GPS. Anyway, I have no much time, so I'll try to catch open sources.</p>
</div>
<div id="comment-8875-info" class="comment-info">
<span class="comment-age">(07 Nov '11, 18:58)</span> <span class="comment-user userinfo">louis10</span>
</div>
</div>
</div>
<div id="comment-tools-8872" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8872-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8887"></span>

<div id="answer-container-8887" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8887-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8887-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-8887-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think that it's worth taking a step back and trying to expand on ChrisH's excellent comments about data and tiles.</p>
<p>What is behind OpenStreetMap (essentially what IS OpenStreetMap) is just lots and lots of data. Here's an example:</p>
<p><a href="https://www.openstreetmap.org/browse/node/254949910">https://www.openstreetmap.org/browse/node/254949910</a></p>
<p>It's a pub (a very nice pub, actually). Click on the "download XML" link on that web page and you'll see the XML associated with it - what it is (a "node"), where it is, who last edited it and tags associated with it that in this case say "it's a pub".</p>
<p>Together with lots of other pieces of data that makes up OpenStreetMap. If you only want to work with part of it, it's often convenient to obtain extracts of it. For example, if I'm creating maps for my Garmin GPS I'll download data from here:</p>
<p><a href="http://download.geofabrik.de/osm/europe/great_britain/">http://download.geofabrik.de/osm/europe/great_britain/</a></p>
<p>I'll then process the data using a <a href="https://wiki.openstreetmap.org/wiki/Mkgmap/help/How_to_create_a_map">program</a> to create something that my Garmin GPS understands and load it onto my GPS. On there the pub appears both as an icon on a map (actually a vector map rather than just a simple picture) and as a searchable point of interest.</p>
<p>A slightly different process happens to create main Mapnik map on the OSM site here:</p>
<p><a href="https://www.openstreetmap.org/?lat=53.27722&amp;lon=-1.72995&amp;zoom=18&amp;layers=M">https://www.openstreetmap.org/?lat=53.27722&amp;lon=-1.72995&amp;zoom=18&amp;layers=M</a></p>
<p>In this case some other software runs behind the scenes and creates a picture from the data (a "tile"):</p>
<p><a href="http://a.tile.openstreetmap.org/18/129812/85057.png">http://a.tile.openstreetmap.org/18/129812/85057.png</a></p>
<p>That is just an image - the only thing that communicates "pub" is the picture of the beer glass on it. It's no use for routing, and would be no use to an application that wanted to find the nearest pub. Also, this is just one of many different renderings of the data - on the main OSM site there are 4 (click the + at the top-right of the map); on other sites there are many more.</p>
<p>Depending on what you want to be able to do in your application, it might be appropriate to handle data internally as just data, or (if you only want to display pictures) as tiles.<br />
</p>
<p>If you do only want to display tiles, you won't be able to download them in bulk from OSM - see the <a href="https://wiki.openstreetmap.org/wiki/Tile_usage_policy">tile usage policy</a> for details as to why and what your alternatives are.</p>
<p>However, if you want to be able to something with the map other than just look at the picture, you'll probably want to download data, store it in a manner that's appropriate for your application, and render it in a manner that's also appropriate.<br />
</p>
<p>It's possible that other people may have already solved some of the problems that you'll need to solve to get your application working (and <a href="https://wiki.openstreetmap.org/wiki/Navit">Navit</a> might be one example of that) but first you'll need to define what you want to be able to do with your application, and that will define what data you need to store on whatever is going to run your application, and so on.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Nov '11, 11:56</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></br></p>
</div>
</div>
<div id="comments-container-8887" class="comments-container">
&#10;</div>
<div id="comment-tools-8887" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8887-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8870"></span>

<div id="answer-container-8870" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8870-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8870-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8870-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Displaying maps offline sounds like you intend to download tiles into a cache for later use. Please be aware that we have a policy that restricts that on OSM tiles. <a href="https://wiki.openstreetmap.org/wiki/Tile_usage_policy">https://wiki.openstreetmap.org/wiki/Tile_usage_policy</a> There are other sources of tiles, including commercial ones. You can also create your own tiles by downloading the OSM data (not the tiles) and rendering your own tiles.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Nov '11, 18:06</strong></p>
<img src="https://secure.gravatar.com/avatar/b906204accce0fd58bc408b22bae01f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChrisH&#39;s gravatar image" />
<p><span>ChrisH</span><br />
<span class="score" title="4075 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="42 badges"><span class="silver">●</span><span class="badgecount">42</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChrisH has 11 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-8870" class="comments-container">
<span id="8871"></span>
<div id="comment-8871" class="comment">
<div id="post-8871-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Rather sounds to me like he wants to do his own rendering from an *.osm file, not download tiles.</p>
</div>
<div id="comment-8871-info" class="comment-info">
<span class="comment-age">(07 Nov '11, 18:24)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="8873"></span>
<div id="comment-8873" class="comment">
<div id="post-8873-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I downloaded 2 files from <a href="http://maps7.navit-project.org">http://maps7.navit-project.org</a> (respectively 1 Mb and 208 Mb) in order to know if Navit software works (the first free software that I found). So, if I'll be able to render maps in my software (that seems diffcult at present because of the documentation), I'll download probably one map for France, and 1 or 2 close countries, just once and maybe one update per year. I suppose that it is authorized ! Please confirm.</p>
<p>For example, the small file is named osm_bbox_11.3,47.9,11.7,48.2.bin. Is it a tile file or a data file ?</p>
<p>Louis</p>
</div>
<div id="comment-8873-info" class="comment-info">
<span class="comment-age">(07 Nov '11, 18:42)</span> <span class="comment-user userinfo">louis10</span>
</div>
</div>
<span id="8876"></span>
<div id="comment-8876" class="comment">
<div id="post-8876-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Vincent, I wanted Louis to understand the issue from the beginning. It's good you pointed him to the data, but many developers see a map and the tiles as what OSM is about, when OSMers know that the data is the real prize. There are too many apps (esp. mobile apps) that cache OSM tiles and cause OSM a lot of problems, so it is good Louis asked first and that he understands to use the data not the tiles. His question sounded like a newbie so tile usage is a good thing to understand, not least to save him wasting his time.</p>
</div>
<div id="comment-8876-info" class="comment-info">
<span class="comment-age">(07 Nov '11, 19:01)</span> <span class="comment-user userinfo">ChrisH</span>
</div>
</div>
<span id="8877"></span>
<div id="comment-8877" class="comment">
<div id="post-8877-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could you explain your reply ? Downloading the bin files from <a href="http://maps7.navit-project.org">http://maps7.navit-project.org</a> is bad or good ? I don't know the difference between tiles and data...</p>
</div>
<div id="comment-8877-info" class="comment-info">
<span class="comment-age">(07 Nov '11, 19:07)</span> <span class="comment-user userinfo">louis10</span>
</div>
</div>
<span id="8878"></span>
<div id="comment-8878" class="comment">
<div id="post-8878-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I don't know about Navit - that is an app that uses the OSM data in its own format and not native OSM data. It seems their .BIN file is specialised to their app. You would have to ask them about their format. Native OSM data is available as XML. The moving map images you see on the <a href="http://osm.org">osm.org</a> website are made of tiles. Using OSM tiles have a usage limit, as above, but you can use the OSM data (XML) with with no usage limit. You can get downloads that cover a country from geofabrik [1] or cloudmade [2] websites.</p>
<p>[1] <a href="http://download.geofabrik.de/osm/">http://download.geofabrik.de/osm/</a> [2] <a href="http://downloads.cloudmade.com/">http://downloads.cloudmade.com/</a></p>
</div>
<div id="comment-8878-info" class="comment-info">
<span class="comment-age">(07 Nov '11, 19:34)</span> <span class="comment-user userinfo">ChrisH</span>
</div>
</div>
<span id="8880"></span>
<div id="comment-8880" class="comment not_top_scorer">
<div id="post-8880-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There is some documentation about the Navit binfile format here: <a href="http://wiki.navit-project.org/index.php/Navit%27s_binary_map_driver">http://wiki.navit-project.org/index.php/Navit%27s_binary_map_driver</a></p>
</div>
<div id="comment-8880-info" class="comment-info">
<span class="comment-age">(07 Nov '11, 20:24)</span> <span class="comment-user userinfo">Vclaw</span>
</div>
</div>
<span id="8889"></span>
<div id="comment-8889" class="comment not_top_scorer">
<div id="post-8889-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... you can also have a look at NaviPOWM (search in the wiki!) ... this opensource program also uses an own vector map format to display OSM data on PC or WinMobile.</p>
</div>
<div id="comment-8889-info" class="comment-info">
<span class="comment-age">(08 Nov '11, 17:01)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-8870" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-8870-form-container" class="comment-form-container">
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

