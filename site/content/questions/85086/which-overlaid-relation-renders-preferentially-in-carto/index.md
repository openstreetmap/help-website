+++
type = "question"
title = "Which overlaid relation renders preferentially in carto?"
description = '''Different tack for wooded open space / park land. If a park / protected area has an administrative boundary, as either a way or a relation, and I create a new relation that includes it and possibly additional area outside it and is tagged as woodland, should the new relation take precedence and rend...'''
date = "2022-07-16T06:22:00Z"
lastmod = "2022-07-19T00:00:00Z"
weight = 85086
keywords = [ "wood", "tags" ]
aliases = [ "/questions/85086" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Which overlaid relation renders preferentially in carto?](/questions/85086/which-overlaid-relation-renders-preferentially-in-carto)

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
<span id="post-85086-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85086-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85086-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Different tack for wooded open space / park land. If a park / protected area has an administrative boundary, as either a way or a relation, and I create a <em>new</em> relation that includes it and possibly additional area outside it and is tagged as woodland, should the new relation take precedence and render the entire area as woods? I don't think the original objects have tags that affect the renderer other than their original protected_area border. Major non-wooded objects such as ponds, parking lots, etc should be able to then get carved out as "inners" in the meta-relationship.</p>
<p>How deep can relationships nest?? Can "outer" and "inner" components be relationships <em>and</em> ways as needed?</p>
<p>This is in the interest of tagging a la <a href="https://help.openstreetmap.org/questions/84812/">my prior question</a> to avoid messing with the underlying objects. Part of the intent is for expansion, bringing more woodlands outside the boundary into the larger relation where appropriate. So far, though, the approach doesn't seem to work, failing to render the woods at all in default Carto on the OSM site. How do I accomplish what I need here?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wood" rel="tag" title="see questions tagged &#39;wood&#39;">wood</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jul '22, 06:22</strong></p>
<img src="https://secure.gravatar.com/avatar/3031665c506b04f416a1af103cf8cf6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_Hobbit&#39;s gravatar image" />
<p><span>_Hobbit</span><br />
<span class="score" title="51 reputation points">51</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_Hobbit has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-85086" class="comments-container">
<span id="85087"></span>
<div id="comment-85087" class="comment">
<div id="post-85087-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, Please be aware that the Lynn Woods area you referred to in the prior question as a park, the outline of which is used in two different relations, being Relation: Lynn Woods Reservation (1153480) and Relation: Lynn woods (14356649). Both of these multipolygon relations have an outer border that is not part of the overall border. One multipolygon includes the large area of Walden Pond the other does not. So it is no surprise that the area does not render as expected. I think your first move should be to correct the multipolygon relations and remove one of them.</p>
</div>
<div id="comment-85087-info" class="comment-info">
<span class="comment-age">(16 Jul '22, 08:07)</span> <span class="comment-user userinfo">BCNorwich</span>
</div>
</div>
<span id="85091"></span>
<div id="comment-85091" class="comment">
<div id="post-85091-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm never sure whether to "answer" or "comment" in these things, that's confusing AF...</p>
<p>There are two relations because one of them is the overlay one I'm trying to build. I want to tag it as woods, in one or both of the hotly-debated methods landuse=forest and/or natural=wood, and then carve the ponds and other non-wooded features out of it as inners.</p>
<p>Original "Lynn Woods" that I directly modified and then un-did because people objected: <a href="https://www.openstreetmap.org/relation/1153480">https://www.openstreetmap.org/relation/1153480</a> <em>as I found it</em></p>
<p>New overlay where I'm trying to do the "right thing" and allow for further expansion of rendered woodland <em>that exists</em> outside the boundary: <a href="https://www.openstreetmap.org/relation/14356649">https://www.openstreetmap.org/relation/14356649</a> Note that "woods" is not capitalized in the name of this one for now.</p>
<p>Mostly, since others built the original Lynn Woods as the protected_area with its funny border and never had a protected_class, I cannot take responsibility for that.</p>
</div>
<div id="comment-85091-info" class="comment-info">
<span class="comment-age">(16 Jul '22, 12:19)</span> <span class="comment-user userinfo">_Hobbit</span>
</div>
</div>
<span id="85093"></span>
<div id="comment-85093" class="comment">
<div id="post-85093-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I guess a related question is, can a <em>relation</em> be an "inner" of another relation and work correctly? I cannot find <em>any</em> information about that specific thing in the Relation wiki documentation. iD didn't object to it, so I assume it's fine.</p>
<p>When I look directly at relation 143556649 right now, highlighted in orange, it doesn't even <em>show</em> the inners of the ponds and golf course. Why? They're completely contained, wtf.</p>
</div>
<div id="comment-85093-info" class="comment-info">
<span class="comment-age">(16 Jul '22, 12:37)</span> <span class="comment-user userinfo">_Hobbit</span>
</div>
</div>
<span id="85100"></span>
<div id="comment-85100" class="comment">
<div id="post-85100-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's not a good practice to upload test data to the live database as this just further confuses any original problems. It would be good to remove the test data, saving it offline for further testing.</p>
</div>
<div id="comment-85100-info" class="comment-info">
<span class="comment-age">(17 Jul '22, 08:03)</span> <span class="comment-user userinfo">BCNorwich</span>
</div>
</div>
<span id="85108"></span>
<div id="comment-85108" class="comment">
<div id="post-85108-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>"test data"? What?</p>
</div>
<div id="comment-85108-info" class="comment-info">
<span class="comment-age">(17 Jul '22, 13:43)</span> <span class="comment-user userinfo">_Hobbit</span>
</div>
</div>
</div>
<div id="comment-tools-85086" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85086-form-container" class="comment-form-container">
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

<span id="85088"></span>

<div id="answer-container-85088" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85088-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85088-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85088-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If I'm understanding your question correctly, putting aside any other technical mistakes, this is caused by <code>landuse=forest</code> on the <code>=nature_reserve</code>. It has been considered as synonymous with <code>natural=wood</code> for tree areas due to disorganized use. Therefore it is usually rendered the same as <code>natural=wood</code> as tree areas. This tag should be removed.</p>
<p>Secondarily, <code>boundary=protected_area</code> needs to be used on a <code>type=boundary</code>, meaning there is a conflict with <code>=nature_reserve</code> as a <code>type=multipolygon</code>. Since <code>=protected_area</code> itself has some problems, and you are not determining its <code>protected_class=</code> or <code>iucn_level=</code> yet, I suggest you remove it as well, keeping it as a <code>type=multipolygon</code> + <code>=nature_reserve</code>. (it is technically not correct to use <code>type=boundary</code> + <code>leisure=nature_reserve</code> although this is the most common representation, like how <code>place=city</code> is often redundantly added on the <code>boundary=administrative</code>)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '22, 09:02</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jul '22, 09:05</strong> </span></p>
</div>
</div>
<div id="comments-container-85088" class="comments-container">
<span id="85092"></span>
<div id="comment-85092" class="comment">
<div id="post-85092-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's part of the point, simply adding natural=wood <em>OR</em> landuse=forest to the original relation is what people were objecting to, "woodland doesn't follow cadastral boundaries" and all that. So I'm trying to lay down real, genuine woodlands in new relationships to avoid messing with the underlying objects. Again, see previous comment, I did not put in the original Lynn Woods. And in fact I'm trying to avoid stepping on the toes of its other editors.</p>
<p>I realize you're trying to help, but I'm just confused by comments on other tags that I wouldn't expect to have any effect on <em>MY</em> new overlay. Thus, the original question. Why would the original Lynn Woods [relation ...3480] be affecting tile display of my Lynn <em>w</em>oods woodland [rel. ...6649] ??</p>
<p>What's happening right now, and this may be because of tile caching, is that different renderings show up randomly at different zoom levels. I've waited, I've tried to dirty some tiles, and it's still just behaving stupidly on the website. I know a lot of this stuff is contentious and has been for years, and I'm trying to do minimal but reasonably "correct" things within that framework rather than stir up those old arguments.</p>
</div>
<div id="comment-85092-info" class="comment-info">
<span class="comment-age">(16 Jul '22, 12:28)</span> <span class="comment-user userinfo">_Hobbit</span>
</div>
</div>
</div>
<div id="comment-tools-85088" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85088-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="85149"></span>

<div id="answer-container-85149" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85149-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85149-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85149-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>"I guess a related question is, can a relation be an "inner" of another relation and work correctly?"</p>
<p>I think this is the root of the issue. In the context of OSM-Carto (the Standard rendering), the answer to your question is no. The relations for the ponds and golf course that you've added as "inner" on the <code>natural=wood</code> relation will not be considered when rendering the trees. That's why you see trees rendered across the entire area.</p>
<p>In order for this to work, you'll need to explicitly add the member ways of those ponds and golf course to the <code>natural=wood</code> relation, specified as inner or outer depending on whether they need to be cut out of the wood relation (the water, inner) or included (the islands, outer).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jul '22, 19:44</strong></p>
<img src="https://secure.gravatar.com/avatar/087bb38ba920baadf1df9dfc473208ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alester&#39;s gravatar image" />
<p><span>alester</span><br />
<span class="score" title="6631 reputation points"><span>6.6k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alester has 37 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-85149" class="comments-container">
<span id="85151"></span>
<div id="comment-85151" class="comment">
<div id="post-85151-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, while thrashing around further I was becoming more afraid that was the truth of it. It's odd that a well-enclosed relation can't serve the purpose, implicitly pointing at all the segments as a group. Wouldn't that amount to less stored data overall?</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Multipolygon_Examples">https://wiki.openstreetmap.org/wiki/Multipolygon_Examples</a> strongly implies that an "inner relation" is kosher, and iD doesn't object to arranging things that way, so it's easy to be confused.</p>
<p>What happens if an "inner" object penetrates the path of the outer one, such as a pond that's half surrounded by woods and half by something else? And what happens if an inner way component or two is missed, thus not correctly closing the inner loop? Is the entire thing invalid?</p>
</div>
<div id="comment-85151-info" class="comment-info">
<span class="comment-age">(18 Jul '22, 23:01)</span> <span class="comment-user userinfo">_Hobbit</span>
</div>
</div>
<span id="85152"></span>
<div id="comment-85152" class="comment">
<div id="post-85152-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A well-enclosed relation can be a member of another relation. That's completely kosher and some renderers may fully support that. OSM-Carto unfortunately doesn't (at least at this time).</p>
<p>If an inner crosses an outer, or an inner or outer ring are unclosed, that would generally be considered a broken multipolygon. If the woods only encompass half of a pond, you'd need to split ways at that point and "wrap" the woods around the one half of the pond's shore.</p>
</div>
<div id="comment-85152-info" class="comment-info">
<span class="comment-age">(19 Jul '22, 00:00)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-85149" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85149-form-container" class="comment-form-container">
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

