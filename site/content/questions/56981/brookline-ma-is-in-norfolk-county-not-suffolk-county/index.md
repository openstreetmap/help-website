+++
type = "question"
title = "Brookline, MA is in Norfolk County, not Suffolk County"
description = '''I just signed up because I noticed that OpenStreetMap thinks that Brookline, MA is in Suffolk County, but it&#x27;s actually in Norfolk County. It&#x27;s not clear to me - do I have the ability to personally edit this information, like Wikipedia? Or do I have to file a ticket?'''
date = "2017-07-10T07:00:00Z"
lastmod = "2017-07-12T20:20:00Z"
weight = 56981
keywords = [ "brookline", "norfolk", "suffolk" ]
aliases = [ "/questions/56981" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Brookline, MA is in Norfolk County, not Suffolk County](/questions/56981/brookline-ma-is-in-norfolk-county-not-suffolk-county)

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
<span id="post-56981-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56981-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56981-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I just signed up because I noticed that OpenStreetMap thinks that Brookline, MA is in Suffolk County, but it's actually in Norfolk County. It's not clear to me - do I have the ability to personally edit this information, like Wikipedia? Or do I have to file a ticket?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-brookline" rel="tag" title="see questions tagged &#39;brookline&#39;">brookline</span> <span class="post-tag tag-link-norfolk" rel="tag" title="see questions tagged &#39;norfolk&#39;">norfolk</span> <span class="post-tag tag-link-suffolk" rel="tag" title="see questions tagged &#39;suffolk&#39;">suffolk</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jul '17, 07:00</strong></p>
<img src="https://secure.gravatar.com/avatar/b615ed111c47f5ccae72f35c30a60996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="robatino&#39;s gravatar image" />
<p><span>robatino</span><br />
<span class="score" title="25 reputation points">25</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="robatino has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jul '17, 07:04</strong> </span></p>
</div>
</div>
<div id="comments-container-56981" class="comments-container">
&#10;</div>
<div id="comment-tools-56981" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56981-form-container" class="comment-form-container">
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

<span id="56982"></span>

<div id="answer-container-56982" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56982-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56982-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-56982-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is not something you can edit by just changing a simple text from "is in this county" to "is in other county". OpenStreetMap (or more precisely, the OpenStreetMap geocoder, Nominatim) <em>deduces</em> the information from the county boundaries. Here are what OpenStreetMap believes to be the county boundaries for Suffolk</p>
<p><a href="http://www.openstreetmap.org/relation/2298154">http://www.openstreetmap.org/relation/2298154</a></p>
<p>and Norfolk</p>
<p><a href="http://www.openstreetmap.org/relation/1840539">http://www.openstreetmap.org/relation/1840539</a></p>
<p>As you can see (at least at the time of writing this), the city of Brookline is clearly in Suffolk County according to these boundaries. If Brookline is in Norfolk, as you say, then both these boundaries are wrong and need to be changed. This is something that everyone can do (from a "having the permission to do it" point of view), but for a new signup editing boundaries can be a daunting task since they are often not drawn as stand-alone geometries, but re-use roads or rivers to form the boundary, and if you are not careful you can break other parts of the map by changing a geometry.</p>
<p>Perhaps you could point us to a source from which we could derive the correct boundaries and then an experienced mapper could look at the problem?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '17, 07:38</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jul '17, 07:39</strong> </span></p>
</div>
</div>
<div id="comments-container-56982" class="comments-container">
<span id="56984"></span>
<div id="comment-56984" class="comment">
<div id="post-56984-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for the detailed information. I live in Brookline, so I know for a fact that it's located in Norfolk County. I don't know if it's possible for parts of a city or town to be in different counties, but I'm pretty sure that Brookline is entirely contained in Norfolk County. When you refer to "correct boundaries", are you referring to Brookline, to Norfolk County, or both? (Unfortunately I probably can't provide the information for either of those, but someone who knows how to use the information should also know where to find it.) The following link indicates that Brookline, MA is noncontiguous with the rest of Norfolk County (which I didn't realize) which is probably why it's broken.</p>
<p><a href="https://en.wikipedia.org/wiki/Brookline,_Massachusetts#Geography">https://en.wikipedia.org/wiki/Brookline,_Massachusetts#Geography</a></p>
<p>And this map illustrates it:</p>
<p><a href="https://en.wikipedia.org/wiki/File:Brookline_ma_lg.png">https://en.wikipedia.org/wiki/File:Brookline_ma_lg.png</a></p>
</div>
<div id="comment-56984-info" class="comment-info">
<span class="comment-age">(10 Jul '17, 07:56)</span> <span class="comment-user userinfo">robatino</span>
</div>
</div>
<span id="56985"></span>
<div id="comment-56985" class="comment">
<div id="post-56985-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Yes it seems as if the ex-clave covering Brookline is missing. I would suggest taking this up on the talk-us list, there is a current interest in US sub-state boundaries and you will be sure to find somebody there willing to help. See <a href="https://lists.openstreetmap.org/listinfo/talk-us">https://lists.openstreetmap.org/listinfo/talk-us</a></p>
</div>
<div id="comment-56985-info" class="comment-info">
<span class="comment-age">(10 Jul '17, 08:01)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="56986"></span>
<div id="comment-56986" class="comment">
<div id="post-56986-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It was ok in late 2014: <a href="http://overpass-turbo.eu/s/qib">http://overpass-turbo.eu/s/qib</a> - it got broken in this edit <a href="http://www.openstreetmap.org/changeset/25407313">http://www.openstreetmap.org/changeset/25407313</a> and then wrongly "repaired" in this <a href="http://www.openstreetmap.org/changeset/25426805">http://www.openstreetmap.org/changeset/25426805</a></p>
</div>
<div id="comment-56986-info" class="comment-info">
<span class="comment-age">(10 Jul '17, 08:05)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="56989"></span>
<div id="comment-56989" class="comment">
<div id="post-56989-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I posted <a href="https://lists.openstreetmap.org/pipermail/talk-us/2017-July/017529.html">https://lists.openstreetmap.org/pipermail/talk-us/2017-July/017529.html</a> , and got a reply saying it's fixed in <a href="https://www.openstreetmap.org/changeset/50175342">https://www.openstreetmap.org/changeset/50175342</a> . The above links <a href="http://www.openstreetmap.org/relation/2298154">http://www.openstreetmap.org/relation/2298154</a> and <a href="http://www.openstreetmap.org/relation/1840539">http://www.openstreetmap.org/relation/1840539</a> appear to be correct now, though a search for "Brookline, MA" on OpenStreetMap.org still says "Suffolk County". How long does the fix take to propagate?</p>
</div>
<div id="comment-56989-info" class="comment-info">
<span class="comment-age">(10 Jul '17, 13:37)</span> <span class="comment-user userinfo">robatino</span>
</div>
</div>
<span id="56991"></span>
<div id="comment-56991" class="comment">
<div id="post-56991-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Depends on the data consumer. Any time from a few minutes to a few weeks.</p>
<p>Basically what happens is that each consumer (map renderer, geocoder, router, etc.) project refreshes their copy of the database of the main one at intervals they have picked and it won't show up on their product until they have updated their internal database with the changes from OSM.</p>
<p>Nominatim, the software/project giving you the county Brookline is in, despite being linked to by OpenStreetMap reference map page is actually a separate project. I believe their update is fairly quick so you should see the fix there in a day or so.</p>
</div>
<div id="comment-56991-info" class="comment-info">
<span class="comment-age">(10 Jul '17, 14:23)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="56992"></span>
<div id="comment-56992" class="comment not_top_scorer">
<div id="post-56992-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>To answer my own question above about whether it's possible for a city or town to be in different counties, the answer is yes - a list is at <a href="https://en.wikipedia.org/wiki/List_of_U.S._municipalities_in_multiple_counties">https://en.wikipedia.org/wiki/List_of_U.S._municipalities_in_multiple_counties</a> . If I search for one of them at Nominatum, it only returns one county, though, so it doesn't appear to be possible to associate more than one.</p>
</div>
<div id="comment-56992-info" class="comment-info">
<span class="comment-age">(10 Jul '17, 14:42)</span> <span class="comment-user userinfo">robatino</span>
</div>
</div>
<span id="57041"></span>
<div id="comment-57041" class="comment not_top_scorer">
<div id="post-57041-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/13918/robatino">@robatino</a> I believe this is because no single point belongs to more than one county (that is, county borders do not overlap). I don't know what Nominatim does to associate an area to a given county, it depends on the Centre Point I believe (I choose Joliet, Illinois, from that wiki list: <a href="https://www.openstreetmap.org/relation/124820">https://www.openstreetmap.org/relation/124820</a> linked to Will County <a href="http://nominatim.openstreetmap.org/details.php?place_id=172756881)">http://nominatim.openstreetmap.org/details.php?place_id=172756881)</a> but a simple reverse geocoding works fine. If you click on "where I am" at this point: <a href="http://bit.ly/2sRfutv">http://bit.ly/2sRfutv</a> you get "Joliet, Kendall County" while crossing the border here: <a href="http://bit.ly/2uS77z4">http://bit.ly/2uS77z4</a> it becomes "Joliet, Will County". Same city, but different county, as we expect.</p>
</div>
<div id="comment-57041-info" class="comment-info">
<span class="comment-age">(12 Jul '17, 20:20)</span> <span class="comment-user userinfo">Alecs01</span>
</div>
</div>
</div>
<div id="comment-tools-56982" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-56982-form-container" class="comment-form-container">
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

