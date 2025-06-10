+++
type = "question"
title = "River &quot;area&quot; rendering problem"
description = '''The Schuylkill River near and surrounding 40°13&#x27;27.0&quot;N 75°36&#x27;24.2&quot;W has a &quot;fix me&quot; associated with a messy rendering of one [or more] &quot;river area&quot; polygons trying to show a nominal coastline. Depending on how one pans/zooms, the shading that accompanies the polygon can be on the proper side of that ...'''
date = "2022-03-11T15:06:00Z"
lastmod = "2022-03-13T00:07:00Z"
weight = 83805
keywords = [ "river" ]
aliases = [ "/questions/83805" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [River "area" rendering problem](/questions/83805/river-area-rendering-problem)

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
<span id="post-83805-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83805-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83805-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The Schuylkill River near and surrounding 40°13'27.0"N 75°36'24.2"W has a "fix me" associated with a messy rendering of one [or more] "river area" polygons trying to show a nominal coastline. Depending on how one pans/zooms, the shading that accompanies the polygon can be on the proper side of that line, the opposite side of the same line, or even on both sides of the line. Worse, with different pan/zooms, you can see that the rendering algorithm gets confused by which vertices to consider, including connecting radically distant vertices for the purposes of shading. I'm no expert, but I seem to remember from decades ago something about an even-odd winding rule that has something to do with the graphics algorithm and these phenomena. Is there an accepted way to craft such "river area" polygons to avoid this rendering problem? It appears the creator might have tried to do a fairly large distance of the river along its flow in a single polygon, which would be easy to believe makes the problem worse.</p>
<p>For the specific URI: <a href="https://www.openstreetmap.org/edit?editor=id#map=16/40.2201/-75.6082">https://www.openstreetmap.org/edit?editor=id#map=16/40.2201/-75.6082</a> the attached screen grab shows two shadings angling down from upper left toward lower right - these are representative of the fill problem described and likely representative of the original "fix me". Clearing my browser (Edge) cache had no discernable effect. I tried Chrome, which had never visited any part of OSM site before now, and observe the same exact result. Also note that the upper (northern) shore of the river does not appear to be shaded while the southern shore has its shading on the "land side".</p>
<p><img src="https://help.openstreetmap.org/upfiles/Screenshot_2022-03-11_122511.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-river" rel="tag" title="see questions tagged &#39;river&#39;">river</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Mar '22, 15:06</strong></p>
<img src="https://secure.gravatar.com/avatar/768202083e5ae734af73d32add71cc0a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="R%20J%20H&#39;s gravatar image" />
<p><span>R J H</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="R J H has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Mar '22, 17:32</strong> </span></p>
</div>
</div>
<div id="comments-container-83805" class="comments-container">
&#10;</div>
<div id="comment-tools-83805" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83805-form-container" class="comment-form-container">
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

<span id="83815"></span>

<div id="answer-container-83815" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83815-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83815-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83815-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="R J H has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've seen this same effect in JOSM as well when only some of the relation members are loaded into JOSM. Loading all relation members, (and sometimes neighboring relations, (all members)) usually rectifies the problem. I don't know if all members can be loaded into the iD editor to rectify the problem there.</p>
<p>As mentioned there's nothing wrong with the relation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Mar '22, 08:20</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-83815" class="comments-container">
&#10;</div>
<div id="comment-tools-83815" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83815-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83806"></span>

<div id="answer-container-83806" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83806-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83806-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-83806-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I checked both visually and with automated tools (JOSM Validator and Relation Analyzer), and I can't find any errors in the data. The OSM Standard rendering looks just like I would expect, with no spilling outside of the riverbanks. If you're seeing something different, you may want to clear your browser cache to make sure you aren't still seeing tiles from before someone made a fix about 3 weeks ago.</p>
<p>For those interested, the relation in question is <a href="https://www.openstreetmap.org/relation/285856">here</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Mar '22, 16:56</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Mar '22, 16:57</strong> </span></p>
</div>
</div>
<div id="comments-container-83806" class="comments-container">
<span id="83808"></span>
<div id="comment-83808" class="comment">
<div id="post-83808-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I updated my original inquiry with an example, but responded to your <a href="https://help.openstreetmap.org/users/8189/alester"></a><a href="https://help.openstreetmap.org/users/8189/alester">@alester</a>'s browser recommendation at the same time. Again, I'm not certain the data is necessarily in error - I think the probability lies in the rendering algorithm's determination of which vertices are visible within the pan/zoom viewport.</p>
</div>
<div id="comment-83808-info" class="comment-info">
<span class="comment-age">(11 Mar '22, 17:42)</span> <span class="comment-user userinfo">R J H</span>
</div>
</div>
<span id="83809"></span>
<div id="comment-83809" class="comment">
<div id="post-83809-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I initially thought you were talking about the final OSM Standard rendering, not the rendering inside the editor.</p>
<p>This appears to just be a visual artifact in the iD editor because not all of the necessary data has been loaded in order to properly shade the water area. I see similar effects in other editors like JOSM when working with incomplete relations. Since only some of the relation is downloaded, the in-editor renderer has to make some guesses and sometimes guesses wrong. This isn't really an error, since the editor is doing the best it can with the partial information. If you browse around enough such that iD downloads the rest of the data for that relation, the rendering should display correctly.</p>
</div>
<div id="comment-83809-info" class="comment-info">
<span class="comment-age">(11 Mar '22, 18:33)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="83811"></span>
<div id="comment-83811" class="comment">
<div id="post-83811-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/8189/alester">@alester</a> - add your observation about this being a phenomena of the ID editor as an 'answer', and I'll up vote it as the correct answer. I do, however, continue to wonder if there isn't a recommendation to be had about how many tiles should be spanned by huge polygons to minimize this happening. Rivers will be popular instigators, but things like large military bases should theoretically tickle the same vulnerability.</p>
</div>
<div id="comment-83811-info" class="comment-info">
<span class="comment-age">(11 Mar '22, 21:17)</span> <span class="comment-user userinfo">R J H</span>
</div>
</div>
</div>
<div id="comment-tools-83806" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83806-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83827"></span>

<div id="answer-container-83827" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83827-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83827-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-83827-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This isn't a rendering, but an editor problem. fixme tags shouldn't be used in this situation, a ticket raised on github instead (good luck with that).</p>
<p>Similar happens in Potlatch.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Mar '22, 00:07</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-83827" class="comments-container">
&#10;</div>
<div id="comment-tools-83827" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83827-form-container" class="comment-form-container">
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

