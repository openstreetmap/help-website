+++
type = "question"
title = "multipolygon not working as expected [solved]"
description = '''Hi there, I have added some water elements in an area of meadows (grass-type vegetation). The larger area is marked with way 346287712. This way has a relation: multipolygon 5640835. The selected role is &#x27;outer&#x27;. The relation has the following two keys/values: landuse/meadow and type/multipolygon. T...'''
date = "2015-11-05T16:19:00Z"
lastmod = "2016-10-10T17:18:00Z"
weight = 46414
keywords = [ "water", "multipolygon" ]
aliases = [ "/questions/46414" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [multipolygon not working as expected \[solved\]](/questions/46414/multipolygon-not-working-as-expected-solved)

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
<span id="post-46414-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46414-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46414-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there, I have added some water elements in an area of meadows (grass-type vegetation).</p>
<p>The larger area is marked with way <a href="http://www.openstreetmap.org/way/346287712">346287712</a>. This way has a relation: multipolygon <a href="http://www.openstreetmap.org/relation/5640835">5640835</a>. The selected role is 'outer'. The relation has the following two keys/values: landuse/meadow and type/multipolygon. This part seems to work, as can be seen here:</p>
<p><a href="http://www.openstreetmap.org/#map=16/52.2843/5.5249">link to the map</a></p>
<p>Inside of the multipolygon I created a number of lakes. The lake that is most south ('Zuiderzee') has an island in it, so I had to create <a href="http://www.openstreetmap.org/relation/5640834">another relation</a> (multopolygon) for the lake. The island is rendered correctly. The water is also rendered, but it has the small tree icons through it, just like the surrounding land.</p>
<p>So my question is: how do I make the water completely blue, without the small tree icons in it?</p>
<p>I have already tried making the water without any relations, this can be seen in the third lake from the south called 't Aelmare. This brings up the same problem.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-water" rel="tag" title="see questions tagged &#39;water&#39;">water</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Nov '15, 16:19</strong></p>
<img src="https://secure.gravatar.com/avatar/f02efb083fed246097e8c87f5b92be99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_Ari&#39;s gravatar image" />
<p><span>_Ari</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_Ari has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Oct '16, 17:11</strong> </span></p>
</div>
</div>
<div id="comments-container-46414" class="comments-container">
<span id="46416"></span>
<div id="comment-46416" class="comment">
<div id="post-46416-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Your edit is recent, it will take time for it to render, if time does not fix it maybe this is the answer--- <a href="http://wiki.openstreetmap.org/wiki/Multipolygon_Examples#Forest_with_two_lakes_and_an_island_.28Nested_multipolygons.29">http://wiki.openstreetmap.org/wiki/Multipolygon_Examples#Forest_with_two_lakes_and_an_island_.28Nested_multipolygons.29</a></p>
</div>
<div id="comment-46416-info" class="comment-info">
<span class="comment-age">(05 Nov '15, 19:58)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="46435"></span>
<div id="comment-46435" class="comment">
<div id="post-46435-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Relation 5640835 has no landuse value, I only see its type. That said, there are lots of trees everywhere, and I don't quite get where they're coming from. Probably, as andy said, time will fix it.</p>
</div>
<div id="comment-46435-info" class="comment-info">
<span class="comment-age">(06 Nov '15, 12:56)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
<span id="46450"></span>
<div id="comment-46450" class="comment">
<div id="post-46450-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Time didn't fix it, there must still be something wrong with the multipolygon relations. The lakes still contain trees.</p>
</div>
<div id="comment-46450-info" class="comment-info">
<span class="comment-age">(07 Nov '15, 19:14)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="52423"></span>
<div id="comment-52423" class="comment">
<div id="post-52423-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This place is a mystery. Something is seriously wrong there with the mapnik-carto tiles, almost as if they were write-protected!? Since about a YEAR, despite changes in the meantime. Anyone can figure this out?</p>
<p><a href="http://mc.bbbike.org/mc/?lat=52.2871906&amp;lon=5.52683644&amp;zoom=15&amp;num=3&amp;mt0=mapnik&amp;mt1=osmfr&amp;mt2=osm-no-labels">http://mc.bbbike.org/mc/?lat=52.2871906&amp;lon=5.52683644&amp;zoom=15&amp;num=3&amp;mt0=mapnik&amp;mt1=osmfr&amp;mt2=osm-no-labels</a></p>
<p>About a year ago the old forest area was completely restructured to install a new campsite, Scoutinglandgoed Zeewolde. Big parts of the forest cut down, new lakes created, tracks and paths are partly different, and OSM was updated accordingly. But mapnik won't show any of it, no matter what.</p>
<p>Cannot find anything wrong with the areas there, and doubt there is. It's not only the areas, but even the tracks and paths are still cached old, for example a way going through the middle of a new lake. And other renderers do show the updates correctly, no prob.</p>
</div>
<div id="comment-52423-info" class="comment-info">
<span class="comment-age">(09 Oct '16, 15:18)</span> <span class="comment-user userinfo">wycbtma</span>
</div>
</div>
<span id="52424"></span>
<div id="comment-52424" class="comment not_top_scorer">
<div id="post-52424-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The weirdest thing is: I did already get mapnik to update the tiles correctly, some weeks ago. After a major struggle, and when nothing helped ending up trying brute force (new fake stream all over the area, updated tiles, some minutes later deleted the fake stream again, updated tiles - all looked fine then). But today came across the area again and was shocked: it had actually RESTORED the OLD tiles again! Just for testing tried the fake-stream method again, but this time didn't help a thing anymore. The stream was shown, but the area behind it NOT updated any more. Have deleted all traces of my fixing attemps again.</p>
<p>No idea if it would help to delete and then rebuild the new AREAs there again. But do not want to get involved any deeper there myself, having no local knowledge. Especially not as long as Bing still shows the old forest too.<br />
But cannot imagine it has anything to do with the data anyway, must be some server prob.</p>
</div>
<div id="comment-52424-info" class="comment-info">
<span class="comment-age">(09 Oct '16, 15:18)</span> <span class="comment-user userinfo">wycbtma</span>
</div>
</div>
<span id="52425"></span>
<div id="comment-52425" class="comment not_top_scorer">
<div id="post-52425-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is this the "way going through the middle of a new lake"? <a href="http://www.openstreetmap.org/?mlat=52.28860&amp;mlon=5.52322#map=17/52.28860/5.52322">http://www.openstreetmap.org/?mlat=52.28860&amp;mlon=5.52322#map=17/52.28860/5.52322</a></p>
<p>I think that's a typical database bug. Something went wrong during the update or the diffs were broken. Now the way remains in the database until someone touches it again or until a complete re-import occurs. Here, touching the way means doing an undelete and then deleting it again. A re-import probably won't happen any time soon since it is very ressource-intensive.</p>
</div>
<div id="comment-52425-info" class="comment-info">
<span class="comment-age">(09 Oct '16, 15:34)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="52427"></span>
<div id="comment-52427" class="comment not_top_scorer">
<div id="post-52427-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So... How long will it probably take for the bug to crawl out of the database if things keep going as usual?</p>
<p>Or what options do we have to chase the bug ourselves? I don't mind doing something to get this sorted, if I need what to do.</p>
</div>
<div id="comment-52427-info" class="comment-info">
<span class="comment-age">(09 Oct '16, 20:29)</span> <span class="comment-user userinfo">_Ari</span>
</div>
</div>
<span id="52429"></span>
<div id="comment-52429" class="comment not_top_scorer">
<div id="post-52429-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>As explained in my previous comment it will stay in the database until the way gets modified again or a re-import occurs.</p>
<p>The way in question seems to be this one: <a href="https://www.openstreetmap.org/way/314866940">https://www.openstreetmap.org/way/314866940</a> Maybe someone can revert and delete it again. I tried to do it a few times but I'm always getting timeouts.</p>
</div>
<div id="comment-52429-info" class="comment-info">
<span class="comment-age">(09 Oct '16, 21:33)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="52444"></span>
<div id="comment-52444" class="comment">
<div id="post-52444-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I've undeleted and re-deleted way 314866940. Rendering seems to be fine now for this way, i.e. it disappeared. You may have to clear your browser cache first. Afterwards I did the same for the forest (way 188676289). Let's see if this is enough.</p>
</div>
<div id="comment-52444-info" class="comment-info">
<span class="comment-age">(10 Oct '16, 16:20)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-46414" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-46414-form-container" class="comment-form-container">
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

<span id="52446"></span>

<div id="answer-container-52446" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52446-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52446-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52446-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The trees are gone, thank you scai! Nice to see that this problem is resolved.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Oct '16, 17:10</strong></p>
<img src="https://secure.gravatar.com/avatar/f02efb083fed246097e8c87f5b92be99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_Ari&#39;s gravatar image" />
<p><span>_Ari</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_Ari has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Oct '16, 17:10</strong> </span></p>
</div>
</div>
<div id="comments-container-52446" class="comments-container">
<span id="52448"></span>
<div id="comment-52448" class="comment">
<div id="post-52448-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, but the new forest still doesn't get rendered compared to the other layers. Seems like the whole changeset needs to be reverted and re-applied.</p>
<p>By the way, please use the "add new comment" button if you just want to add a comment instead of an answer (= a solution) to your question.</p>
</div>
<div id="comment-52448-info" class="comment-info">
<span class="comment-age">(10 Oct '16, 17:18)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-52446" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52446-form-container" class="comment-form-container">
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

