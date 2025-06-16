+++
type = "question"
title = "place=* - node vs. area"
description = '''Forgive me, if this question is already answered, but on a quick search, I could not find an answer that fits my issue 100%: It is possible to use the place=town/village/suburb etc. on an area or a node.  In most cases in my area, both an area and a node are used at the same time. And when tagging, ...'''
date = "2012-02-28T09:57:00Z"
lastmod = "2014-05-14T09:07:00Z"
weight = 10851
keywords = [ "node", "place", "area" ]
aliases = [ "/questions/10851" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [place=\* - node vs. area](/questions/10851/place-node-vs-area)

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
<span id="post-10851-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10851-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-10851-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Forgive me, if this question is already answered, but on a quick search, I could not find an answer that fits my issue 100%:</p>
<p>It is possible to use the place=town/village/suburb etc. on an area or a node. In most cases in my area, both an area and a node are used at the same time. And when tagging, I also do it like this to keep the database uniform.</p>
<p>Although it has the result, that a named place appears now twice in the search results, which is not good in my opinion.</p>
<p>But it would make sense to use both as in my opinion:</p>
<ul>
<li>the area with place=* shows clearly, that a certain feature (e.g. street, restaurant) is located in this village or town.</li>
<li>the node with place=* is useful for routing purposes, e.g. I want to go to village XXX, please send me to the village <em>centre</em> (e.g. main square or something similar).</li>
</ul>
<p>What is the optimal way of having both benefits without disadvantages? Or is it just like eating the cake and keeping it at the same time?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-place" rel="tag" title="see questions tagged &#39;place&#39;">place</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Feb '12, 09:57</strong></p>
<img src="https://secure.gravatar.com/avatar/139902838ec4406143a7d9f286419a52?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="moszkva%20ter&#39;s gravatar image" />
<p><span>moszkva ter</span><br />
<span class="score" title="2125 reputation points"><span>2.1k</span></span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="moszkva ter has 8 accepted answers">17%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Feb '12, 09:58</strong> </span></p>
</div>
</div>
<div id="comments-container-10851" class="comments-container">
<span id="10870"></span>
<div id="comment-10870" class="comment">
<div id="post-10870-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would like to expand this question: What about multipolygon consisting of all the residential/commercial/farming/... boundaries?<br />
That should give precise borders of the city without creating duplicate geometries.</p>
</div>
<div id="comment-10870-info" class="comment-info">
<span class="comment-age">(28 Feb '12, 20:30)</span> <span class="comment-user userinfo">LM_1</span>
</div>
</div>
</div>
<div id="comment-tools-10851" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10851-form-container" class="comment-form-container">
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

<span id="10859"></span>

<div id="answer-container-10859" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10859-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10859-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-10859-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="moszkva ter has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Follow the <span>tagging good practices</span> and in your case, the "<span>One feature, one OSM element</span>". Therefore, put the tag place either on a node or on the area, but not on both.</p>
<p>For a village or town, the "area" might be:</p>
<ul>
<li>the settlement itself where most of the buildings are, the urbanized area. This can be tagged with "landuse=residential" on a single polygon as a starting point. Later, it can be more detailed and split in smaller pieces (apart the residentials, you might have farms, shops, industries, offices, crafts, etc areas). But if you have a single polygon, you can put the tag "place=<em>" there. Or keep the place node and tag the polygon with the tag "place_name=</em>" (see <span>this wiki</span> or <span>that one</span>).</li>
<li>the administrative boundary which may include the countryside around the settlement. You can also put the tag "place*" on this polygon (or more commonly, on the <span>boundary/multipolygon relation</span>). But this is less usual as we can see in the statistics that <span>currently only 6% of the boundaries are combined with the "place" tag</span>. An alternative is to keep the place node indicating where the place "centre" is (more or less, the definition of the place centre being sometimes subjective) and attach it to the <span>boundary relation with the role "admin_centre"</span>.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Feb '12, 12:37</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 May '14, 11:26</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-10859" class="comments-container">
<span id="10894"></span>
<div id="comment-10894" class="comment">
<div id="post-10894-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks for the hint with the place_name. That should work out. Unfortunately, in Georgia we do not have any admin levels for villages and small suburbs / neighbourhoods. They either don't exist, or a source is not accessible. So for now, this workaround must do it.</p>
<p>Also, in Tbilisi, historic neighbourhoods are sometimes split up between two raion boundaries, which is also a little annoying to tag. But with a polygon and place_name, I think it is fine.</p>
</div>
<div id="comment-10894-info" class="comment-info">
<span class="comment-age">(01 Mar '12, 06:49)</span> <span class="comment-user userinfo">moszkva ter</span>
</div>
</div>
</div>
<div id="comment-tools-10859" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10859-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="10854"></span>

<div id="answer-container-10854" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10854-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10854-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-10854-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In my point of view, the place=* tag should be used on a node. The spatial relation between a feature and the village/town can be deduced with the administrative boundary. See also <a href="/questions/3942/how-to-map-inhabited-places-settlements">this similar question (with my answer)</a>.</p>
<p>The area is used for giving the administrative boundary, while the node give a more accurate information on the "place" center's position.</p>
<p>In some case, there isn't a suitable boundary, but it is mainly for the hamlets, that are commonly attached to a village/town with a administrative boundary (at least in France). In this case, I don't think it is so annoying to not have a geometric inclusion of a feature of this hamlet in an area.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Feb '12, 10:41</strong></p>
<img src="https://secure.gravatar.com/avatar/a2839f25c5f2da24f6ffd25de1641684?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NicolasDumoulin&#39;s gravatar image" />
<p><span>NicolasDumoulin</span><br />
<span class="score" title="3327 reputation points"><span>3.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NicolasDumoulin has 15 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Feb '12, 10:44</strong> </span></p>
</div>
</div>
<div id="comments-container-10854" class="comments-container">
<span id="10892"></span>
<div id="comment-10892" class="comment">
<div id="post-10892-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I will now follow your advice partly. I will use the place= <em>on the node and place_name=</em> on the areas.</p>
<p>The problem here in Georgia is, that towns or suburbs don't have an official boundary - or at least there is no access to a source for an official boundary. So the boundaries are added by common sense. Still it would be good to have at least rough outlines for the bigger areas.</p>
</div>
<div id="comment-10892-info" class="comment-info">
<span class="comment-age">(01 Mar '12, 06:44)</span> <span class="comment-user userinfo">moszkva ter</span>
</div>
</div>
</div>
<div id="comment-tools-10854" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10854-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="10856"></span>

<div id="answer-container-10856" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10856-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10856-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-10856-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Seems like there are differing views, because I tend to think that the area provides a superset of what the node provides, so the node can be deleted once the area is created (the node will often have been added by an earlyer mapper, as an approximation.</p>
<p>Some arguments why a node isn't worth it when an area is available:</p>
<ul>
<li>The center of the area will usually be just as good an approximation of the town center as could be achieved with a node.</li>
<li>For smaller places it really doesn't matter to have the map point you to the "center". For bigger cities, you'd typically be interested in a specific neighbouhood anyway, so puting the city center as a lone feature in the map is not very usefull.</li>
<li>If you <em>do</em> want your satnav to navigate to a specific neighbourhood, there are other osm tags better suited for that (landuse=residential/comercial, individual place=locality within the larger place=* area, etc).</li>
<li>As mentioned by OP, tools get confused when there is duplicate data in the database.</li>
</ul>
<p>So again I'd say do not keep the node after you draw the area. If you really want to map the city center explicitly (say because the town has a very excentric shape), do so using a place=locality node or a landuse=* area and use "name=city center" instead of "name=Foobartown".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Feb '12, 11:17</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-10856" class="comments-container">
<span id="10893"></span>
<div id="comment-10893" class="comment">
<div id="post-10893-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Your advice somehow violates the "on-ground-rule". If a neighbourhood is not called "City Centre" officially, why add it as a name then?</p>
</div>
<div id="comment-10893-info" class="comment-info">
<span class="comment-age">(01 Mar '12, 06:46)</span> <span class="comment-user userinfo">moszkva ter</span>
</div>
</div>
<span id="33169"></span>
<div id="comment-33169" class="comment">
<div id="post-33169-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Do not invent names like 'city center' if they are not used locally. Also, for marking the "center" of a place, there's ""admin_centre", as explained in Pieren's answer.</p>
</div>
<div id="comment-33169-info" class="comment-info">
<span class="comment-age">(14 May '14, 09:07)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
</div>
<div id="comment-tools-10856" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10856-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33104"></span>

<div id="answer-container-33104" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33104-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33104-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33104-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The older question <a href="/questions/4068/">when-does-it-make-sense-to-use-place-on-an-area</a> (with currently <em>three answers</em>) is quite about the same topic.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 May '14, 11:19</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-33104" class="comments-container">
&#10;</div>
<div id="comment-tools-33104" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33104-form-container" class="comment-form-container">
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

