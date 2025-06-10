+++
type = "question"
title = "Riverbank to relation?"
description = '''In an area I am mapping there is a large river. It has been mapped as a series of multi-polygon riverbanks - each for part of the river&#x27;s course. The river is untagged apart form that. Ideally should I:  Add a &#x27;river&#x27; way(s) that marks the centre line Create a relation for the river  Should the rela...'''
date = "2013-05-13T11:11:00Z"
lastmod = "2013-05-20T08:57:00Z"
weight = 22364
keywords = [ "river", "riverbank", "relations" ]
aliases = [ "/questions/22364" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Riverbank to relation?](/questions/22364/riverbank-to-relation)

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
<span id="post-22364-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22364-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22364-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In an area I am mapping there is a large river. It has been mapped as a series of multi-polygon riverbanks - each for part of the river's course. The river is untagged apart form that. Ideally should I:</p>
<ol>
<li>Add a 'river' way(s) that marks the centre line</li>
<li>Create a relation for the river</li>
</ol>
<p>Should the relation contain all the ways (riverbank and river)? Should just the relation be given a name tag or all the ways (river and riverbank)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-river" rel="tag" title="see questions tagged &#39;river&#39;">river</span> <span class="post-tag tag-link-riverbank" rel="tag" title="see questions tagged &#39;riverbank&#39;">riverbank</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 May '13, 11:11</strong></p>
<img src="https://secure.gravatar.com/avatar/f975d12117093ce5b3b4748dc4927400?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RobChafer&#39;s gravatar image" />
<p><span>RobChafer</span><br />
<span class="score" title="220 reputation points">220</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RobChafer has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-22364" class="comments-container">
&#10;</div>
<div id="comment-tools-22364" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22364-form-container" class="comment-form-container">
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

<span id="22372"></span>

<div id="answer-container-22372" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22372-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22372-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-22372-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="RobChafer has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A river usually consists of a way with the <em>waterway</em> key (or multiple ways for longer rivers) and optionally an area with the <em>waterway=riverbank</em> tag (or multiple areas for longer rivers). The way usually runs through the center or, if known, along the deepest points of the river and is always required. The riverbanks are only optional.</p>
<p>For longer rivers the ways are often grouped in a relation (example: <a href="http://www.openstreetmap.org/browse/relation/123822">http://www.openstreetmap.org/browse/relation/123822</a>). Likewise the riverbanks can be grouped in a relation, too, but this is usually not the case.</p>
<p>tl;dr: Yes, add the center way and create a relation consisting of all your center river ways if you feel familiar enough with relations.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 May '13, 13:07</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 May '13, 13:40</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-22372" class="comments-container">
<span id="22374"></span>
<div id="comment-22374" class="comment">
<div id="post-22374-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>A couple more examples - <a href="http://www.openstreetmap.org/browse/relation/89652">here</a> is the relation for the Danube, and <a href="http://www.openstreetmap.org/browse/relation/2566210">here</a> is one for the Douro / Duero (though that, for some reason, has two relations for it). None of these example relations have riverbank polygons as part of the "river" relation.</p>
</div>
<div id="comment-22374-info" class="comment-info">
<span class="comment-age">(13 May '13, 13:43)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="22376"></span>
<div id="comment-22376" class="comment">
<div id="post-22376-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I found a <a href="http://www.openstreetmap.org/browse/relation/6692">relation of riverbanks</a> but this seems to be rather uncommon.</p>
</div>
<div id="comment-22376-info" class="comment-info">
<span class="comment-age">(13 May '13, 13:54)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="22377"></span>
<div id="comment-22377" class="comment">
<div id="post-22377-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks <span>@scai</span> - would the riverbank normally be named?</p>
</div>
<div id="comment-22377-info" class="comment-info">
<span class="comment-age">(13 May '13, 14:19)</span> <span class="comment-user userinfo">RobChafer</span>
</div>
</div>
<span id="22382"></span>
<div id="comment-22382" class="comment">
<div id="post-22382-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span></span><span>@RobChafer</span> Thats a good question. Some have a name and some don't have one. <a href="http://taginfo.openstreetmap.org/tags/?key=waterway&amp;value=riverbank#combinations">taginfo</a> shows that around 12% of the riverbanks have a name tag which is not very much compared to 71% of the <a href="http://taginfo.openstreetmap.org/tags/?key=waterway&amp;value=river#combinations">rivers</a>.</p>
</div>
<div id="comment-22382-info" class="comment-info">
<span class="comment-age">(13 May '13, 15:01)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="22413"></span>
<div id="comment-22413" class="comment">
<div id="post-22413-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If I may add a suggestion: this should be illustrated in a diagram and posted to the wiki.</p>
</div>
<div id="comment-22413-info" class="comment-info">
<span class="comment-age">(14 May '13, 09:43)</span> <span class="comment-user userinfo">Russkel</span>
</div>
</div>
<span id="22414"></span>
<div id="comment-22414" class="comment not_top_scorer">
<div id="post-22414-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@Russkel</span> What exactly? The wiki already has pages about <a href="http://wiki.openstreetmap.org/wiki/Tag:waterway%3Driver">rivers</a> and <a href="http://wiki.openstreetmap.org/wiki/Tag:waterway%3Driverbank">riverbanks</a>. And of course everybody is welcome to improve them, including you :).</p>
</div>
<div id="comment-22414-info" class="comment-info">
<span class="comment-age">(14 May '13, 09:51)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="22415"></span>
<div id="comment-22415" class="comment not_top_scorer">
<div id="post-22415-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@scai</span> sorry, nevermind, I reread your answer and it's not nearly as complicated as I thought it was (I imagined some multi-way river system with relations, for some reason). It's been a long day.</p>
</div>
<div id="comment-22415-info" class="comment-info">
<span class="comment-age">(14 May '13, 09:56)</span> <span class="comment-user userinfo">Russkel</span>
</div>
</div>
</div>
<div id="comment-tools-22372" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-22372-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="22391"></span>

<div id="answer-container-22391" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22391-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22391-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-22391-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Normally, bigger rivers are tagged with a waterway=river for the main stream(s) where the water flows and waterway=riverbank for the whole extension of the waters the rivers contain.<br />
(For such questions it is mostly a good idea to search for several big, already mapped objects of the same kind and use their mapping as example)</p>
<p>For my part, I do map rivers and riverbanks with name=*, national names and source= all the same except the waterway tag.</p>
<p>As the (now) top voted answer sais: rivers are often mapped with relations.</p>
<p>IMO this has "historic" reasons since in earlier times this was the only way to handle bigger rivers in one go.</p>
<p>But now the times and the tools have changed.<br />
There is the <a href="http://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a> to query for anything you can describe, there is WIWOSM, there is a <a href="http://www.kompf.de/gps/rivermap.html?lat=50.53150&amp;lon=12.38978&amp;zoom=6">watershed map</a> which just uses connections and directions of waterways so IMO there is no need to use relations on complete rivers anymore - I don't use them. Of course you still need multipolygon relations for riverbanks encircling islands.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 May '13, 21:01</strong></p>
<img src="https://secure.gravatar.com/avatar/a18e2b8eb41515c09bb66159941584bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="malenki&#39;s gravatar image" />
<p><span>malenki</span><br />
<span class="score" title="4713 reputation points"><span>4.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="46 badges"><span class="silver">●</span><span class="badgecount">46</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="malenki has 10 accepted answers">6%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 May '13, 21:06</strong> </span></p>
</div>
</div>
<div id="comments-container-22391" class="comments-container">
<span id="22407"></span>
<div id="comment-22407" class="comment">
<div id="post-22407-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>That's correct, the grouping aspect of the relation is no longer necessary. But it seems easier to put all the additional tags like <em>name:&lt;lang&gt;</em>, <em>wikipedia</em> etc. to a single relation instead of keeping all individual ways up to date and consistent with each other. Also tags like <em>length</em> seem to belong to the relation and not to a single element because that might be misleading.</p>
</div>
<div id="comment-22407-info" class="comment-info">
<span class="comment-age">(14 May '13, 06:28)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="22540"></span>
<div id="comment-22540" class="comment">
<div id="post-22540-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I consider length= as superfluous since this can be derived from the object(s) themselves.<br />
What do you do if length= doesn't match the objects length? Though a relation maybe can be updated more easily - but it also breaks more easily.</p>
</div>
<div id="comment-22540-info" class="comment-info">
<span class="comment-age">(18 May '13, 14:10)</span> <span class="comment-user userinfo">malenki</span>
</div>
</div>
<span id="22546"></span>
<div id="comment-22546" class="comment">
<div id="post-22546-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The length can only be derived from the object if it has been completely mapped.</p>
</div>
<div id="comment-22546-info" class="comment-info">
<span class="comment-age">(19 May '13, 17:09)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="22552"></span>
<div id="comment-22552" class="comment">
<div id="post-22552-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Where else would you get the length from?<br />
Recently I mapped a river which Wikipedia told is 233km long. I traced it to about 257km before I had to stop due to the poor imagery...</p>
</div>
<div id="comment-22552-info" class="comment-info">
<span class="comment-age">(20 May '13, 00:23)</span> <span class="comment-user userinfo">malenki</span>
</div>
</div>
<span id="22560"></span>
<div id="comment-22560" class="comment">
<div id="post-22560-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I guess there is always something you could call an "official length" and a "real length". And the length in the OSM database, of course.</p>
</div>
<div id="comment-22560-info" class="comment-info">
<span class="comment-age">(20 May '13, 08:57)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-22391" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22391-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="22366"></span>

<div id="answer-container-22366" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22366-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22366-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-22366-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi RobChafer did you read this page of the wiki ? <a href="http://wiki.openstreetmap.org/wiki/River">http://wiki.openstreetmap.org/wiki/River</a> If you’re working in Potlach (2), there’s a limit of 2000 nodes, so dont make ways bigger than that. Or your work cannot be saved.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 May '13, 11:48</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span> </br></br></p>
</div>
</div>
<div id="comments-container-22366" class="comments-container">
<span id="22368"></span>
<div id="comment-22368" class="comment">
<div id="post-22368-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, so that means I should to add a river way. What about the relation bit?</p>
</div>
<div id="comment-22368-info" class="comment-info">
<span class="comment-age">(13 May '13, 12:11)</span> <span class="comment-user userinfo">RobChafer</span>
</div>
</div>
<span id="22370"></span>
<div id="comment-22370" class="comment">
<div id="post-22370-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>To be clear:</p>
<p>1) The 2000-node limit is an API restriction, not an editor restriction.</p>
<p>2) It's spelt "Potlatch".</p>
</div>
<div id="comment-22370-info" class="comment-info">
<span class="comment-age">(13 May '13, 12:37)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="22371"></span>
<div id="comment-22371" class="comment">
<div id="post-22371-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What do you mean with the relation bit? The mainstream is the centre. The riverbanks are a separate part or relation of the system. And can be added to the system later but not necessary. IMHO it looks better if a water system becomes visible on display, although it almost as if it’s tagging for the renderer.</p>
</div>
<div id="comment-22371-info" class="comment-info">
<span class="comment-age">(13 May '13, 12:57)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="22387"></span>
<div id="comment-22387" class="comment">
<div id="post-22387-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I meant should the riverbanks be added to the relation for the river as a whole.</p>
</div>
<div id="comment-22387-info" class="comment-info">
<span class="comment-age">(13 May '13, 17:04)</span> <span class="comment-user userinfo">RobChafer</span>
</div>
</div>
</div>
<div id="comment-tools-22366" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22366-form-container" class="comment-form-container">
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

