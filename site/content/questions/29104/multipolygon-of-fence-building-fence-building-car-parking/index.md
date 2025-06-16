+++
type = "question"
title = "Multipolygon of fence, building, fence, building, car parking"
description = '''Hi, I want to map a Lumber shop business. Its outer boundaries are defined by:   a fence in the west and north west side a building in the north side a car parking in the north east, east and south east side a building in the south side a fence in the south side and another building in the south sid...'''
date = "2013-12-16T02:48:00Z"
lastmod = "2013-12-18T12:50:00Z"
weight = 29104
keywords = [ "building", "outer", "fence", "multipolygon" ]
aliases = [ "/questions/29104" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [Multipolygon of fence, building, fence, building, car parking](/questions/29104/multipolygon-of-fence-building-fence-building-car-parking)

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
<span id="post-29104-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29104-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-29104-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I want to map a Lumber shop business. Its outer boundaries are defined by:<br />
</p>
<ul>
<li>a fence in the west and north west side</li>
<li>a building in the north side</li>
<li>a car parking in the north east, east and south east side</li>
<li>a building in the south side</li>
<li>a fence in the south side</li>
<li>and another building in the south side</li>
</ul>
<p>I can't find the best way to represent such configuration. I tried creating a multipolygon relation but it fails to "link" those members together. Any suggestion ? Should I use a "site" relation?</p>
<p>For the curious ones, here is the case: <a href="https://www.openstreetmap.org/edit?editor=id#map=19/35.91258/-79.07332">https://www.openstreetmap.org/edit?editor=id#map=19/35.91258/-79.07332</a></p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-building" rel="tag" title="see questions tagged &#39;building&#39;">building</span> <span class="post-tag tag-link-outer" rel="tag" title="see questions tagged &#39;outer&#39;">outer</span> <span class="post-tag tag-link-fence" rel="tag" title="see questions tagged &#39;fence&#39;">fence</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Dec '13, 02:48</strong></p>
<img src="https://secure.gravatar.com/avatar/de5e2187d1e002fc2aa5d8aa59729e1e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="exxos&#39;s gravatar image" />
<p><span>exxos</span><br />
<span class="score" title="81 reputation points">81</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="exxos has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Dec '13, 07:23</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span></p>
</div>
</div>
<div id="comments-container-29104" class="comments-container">
<span id="29112"></span>
<div id="comment-29112" class="comment">
<div id="post-29112-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answers. It seems to me that I should do as Pieren and Hendrikklaas suggest: * Create a new "way" that covers the entire area and tag it as a "shop"</p>
<p>To make things more complicated, it appears that there is a warehouse located 1 block north of the area that belongs to the store (and customers can go there). <a href="https://www.openstreetmap.org/edit?editor=id#map=19/35.91461/-79.07082">https://www.openstreetmap.org/edit?editor=id#map=19/35.91461/-79.07082</a></p>
<p>So should I use "multipolygon" or "site" to "link" both areas ?</p>
<p>bonus question: do we have a wiki page that lists all the techniques ?</p>
</div>
<div id="comment-29112-info" class="comment-info">
<span class="comment-age">(16 Dec '13, 12:37)</span> <span class="comment-user userinfo">exxos</span>
</div>
</div>
<span id="29115"></span>
<div id="comment-29115" class="comment">
<div id="post-29115-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>If you cannot surroung the whole facility within a single polygon (as you suggest with the warehouse), then create as many polygons as required and put all of them in the "site" relation. The "shop" tag then belongs to the relation (following the principle that "one feature is tagged only once").</p>
</div>
<div id="comment-29115-info" class="comment-info">
<span class="comment-age">(16 Dec '13, 14:10)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="29117"></span>
<div id="comment-29117" class="comment">
<div id="post-29117-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Bonus comment: not really in the wiki. But you can also download the data from well mapped areas and check how it is done by others. It's true that the wiki is lacking in such stuff. We just need motivated writers ;-)</p>
</div>
<div id="comment-29117-info" class="comment-info">
<span class="comment-age">(16 Dec '13, 14:11)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="29132"></span>
<div id="comment-29132" class="comment">
<div id="post-29132-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Pieren for your answers. I am surprised there is only 6 site=shop relations in the entire world. I feel that my case should be somewhat a popular case. <a href="http://taginfo.openstreetmap.org/tags/site=shop">http://taginfo.openstreetmap.org/tags/site=shop</a> Moreover, the new relation icon/name does not render correctly. Are you sure it is best way to do it? Thanks.</p>
</div>
<div id="comment-29132-info" class="comment-info">
<span class="comment-age">(17 Dec '13, 05:21)</span> <span class="comment-user userinfo">exxos</span>
</div>
</div>
<span id="29142"></span>
<div id="comment-29142" class="comment">
<div id="post-29142-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The tag "site=shop" is purely optional (and more cosmetic than anything else). After the mandatory "type=site", add the sames tags as for normal polygons. Here, add "shop=<em>" + "name=</em>"</p>
</div>
<div id="comment-29142-info" class="comment-info">
<span class="comment-age">(17 Dec '13, 15:09)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="29143"></span>
<div id="comment-29143" class="comment not_top_scorer">
<div id="post-29143-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Fair enough, thanks.</p>
<p>I already added all those tags, but no luck; nothing shows up in the renderer. Any suggestion ?</p>
</div>
<div id="comment-29143-info" class="comment-info">
<span class="comment-age">(17 Dec '13, 15:20)</span> <span class="comment-user userinfo">exxos</span>
</div>
</div>
</div>
<div id="comment-tools-29104" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-29104-form-container" class="comment-form-container">
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

<span id="29108"></span>

<div id="answer-container-29108" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29108-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29108-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-29108-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="exxos has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What you need is to draw a simple polygon (closed way) surrounding the facility and add the tags qualifying the shop onto this polygon with e.g. "shop=lumber" + "name=name_of_the_shop". When you draw this polygon, you might have to reuse existing nodes created for the fences and buildings. Hence the fence will partially overlap with the surrounding polygon but this is not a problem if this is physically the case. (see this <a href="https://wiki.openstreetmap.org/wiki/File:Amenity_school_usage_example.svg">school example</a> from the wiki)<br />
Later, you can improve the map by specifying which building is doing what (warehouse, office, etc) on each building polygon.<br />
The "multipolygon" relation is only required for complex geometries (with inners/outers) or very big polygons (a way is limited to 2000 nodes in OSM).<br />
A <a href="https://wiki.openstreetmap.org/wiki/Relation:site">"site" relation</a> is only required when a single area is not possible. For instance, a university is often spread on multiple locations in a town/city.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Dec '13, 10:00</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Dec '13, 14:05</strong> </span></p>
</div>
</div>
<div id="comments-container-29108" class="comments-container">
<span id="29159"></span>
<div id="comment-29159" class="comment">
<div id="post-29159-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Agree, besides that a site relation would be required for a feature consisting of several areas: this can also be expressed with a multipolygon relation. IMHO the only compelling reason for a site relation is the possibility to add additional roles like "label", "ticket_office", "parking", "main_entrance" etc. which is not defined for multipolygons.</p>
</div>
<div id="comment-29159-info" class="comment-info">
<span class="comment-age">(18 Dec '13, 12:43)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
</div>
<div id="comment-tools-29108" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29108-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29106"></span>

<div id="answer-container-29106" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29106-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29106-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29106-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Like always in OSM, there is not one single 'best' way that fits for every scenario ;) , so I just will try to present a few that IMHO might make sense:</p>
<ol>
<li><strong>No Multipolygon</strong><br />
In your case, I don't see an advantage to make use of a relation to group all things together (beside that it would be semantical correct). So what I usually do is to map the biggest area (here the fence) with the POI properties and keep all the others as they are. If you like, you can tag the buildings <a href="https://wiki.openstreetmap.org/wiki/Key:building">more detailed</a>.</li>
<li><strong>Site-relation</strong><br />
As you already wrote, a <a href="https://wiki.openstreetmap.org/wiki/Site">site relation</a> is a common way to group things together, but AFAIK it's more used for keeping distributed sites together (as a university campus that is spread over the city etc.). AFAIK there is currently no tool/service that makes use of this relation.</li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Dec '13, 07:31</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span> </br></br></p>
</div>
</div>
<div id="comments-container-29106" class="comments-container">
<span id="29110"></span>
<div id="comment-29110" class="comment">
<div id="post-29110-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer. That is helpful. However I've some questions:</p>
<ol>
<li>No Multipolygon</li>
</ol>
<p>Do you mean I should extend the fence to cover the entire area ? the problem is that there is no fence over the entire area so it would not be correct. If I don't extend the fence, then how would we know that the parking belongs to the store ?</p>
<ol>
<li>Site-relation</li>
</ol>
<p>If no tool/service that makes use of this relation, how come is it a "common" way to group things together ?</p>
</div>
<div id="comment-29110-info" class="comment-info">
<span class="comment-age">(16 Dec '13, 12:14)</span> <span class="comment-user userinfo">exxos</span>
</div>
</div>
<span id="29160"></span>
<div id="comment-29160" class="comment">
<div id="post-29160-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<ol>
<li>This is a case for a multipolygon, because there is not a fence all around it, so you have to use several outer ways to form together one outline. Also if the fence was all around it, it would be better to use a multipolygon, as a fence is a linear (and distinct feature) and should not be tagged on the same object as the area inside it.</li>
</ol>
</div>
<div id="comment-29160-info" class="comment-info">
<span class="comment-age">(18 Dec '13, 12:47)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
<span id="29161"></span>
<div id="comment-29161" class="comment">
<div id="post-29161-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you wanted to do the latter (tag the fence on the area) the way to do it would be to keep the fence untagged (as it is a linear way) and add the attribute "fenced=yes" to the area, but this is not possible here because you don't have a continuous fence (and 2 different mapping styles for the same thing are not desirable anyway). KISS.</p>
</div>
<div id="comment-29161-info" class="comment-info">
<span class="comment-age">(18 Dec '13, 12:48)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
</div>
<div id="comment-tools-29106" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29106-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29107"></span>

<div id="answer-container-29107" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29107-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29107-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29107-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi take a look at a university or school area, <a href="/questions/5148/mapping-a-university-campus.">https://help.openstreetmap.org/questions/5148/mapping-a-university-campus.</a> Or just draw a complete way around the area and ad a name tag, without building a multipolygone like iii stated.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Dec '13, 07:36</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span> </br></p>
</div>
</div>
<div id="comments-container-29107" class="comments-container">
&#10;</div>
<div id="comment-tools-29107" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29107-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="29113"></span>

<div id="answer-container-29113" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29113-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29113-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-29113-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you want to avoid overlapping ways, which happens in <a href="#29108">Pieren's case</a>, then you can draw single ways which you chain up as needed with a multipolygon (like you described in your question). Likely you just did something wrong (e.g. no closed multipolygon outer way). However, this does not help for pieces of fence which are no closed circles as multipolygons always need to be "closed".</p>
<p>See the <span>usage example(s)</span>. I <a href="http://overpass-turbo.eu/s/1MO">have searched</a> for realworld examples. Look at <a href="https://www.openstreetmap.org/relation/2182994">this one</a>.</p>
<p>I am trying to make an example (numbers represent nodes, x-y is a way consisting of node x and y):</p>
<pre><code>1-----2
|     |
6-----3
|     |
5-----4</code></pre>
<ul>
<li>fence and other tags which apply to the complete area: tag them onto a multipolygon which consists of those outer ways:
<ul>
<li>1-2,2-3,3-4,4-5,5-6,6-1</li>
</ul></li>
<li>if I assume there is a car parking in the south: tag the car parking tags to a multipolygon which consists of those outer ways:</li>
<li>6-3,3-4,4-5,5-6</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Dec '13, 13:06</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Dec '13, 13:38</strong> </span></p>
</div>
</div>
<div id="comments-container-29113" class="comments-container">
<span id="29116"></span>
<div id="comment-29116" class="comment">
<div id="post-29116-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Okayokay, seems here are some relation haters. ;-) Note that I do not recommend this method. I just mention that it is possible. Also note that this help site is no policy vote. Please instead just comment what the downsides of this are in your opinion.</p>
</div>
<div id="comment-29116-info" class="comment-info">
<span class="comment-age">(16 Dec '13, 14:11)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="29120"></span>
<div id="comment-29120" class="comment">
<div id="post-29120-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>yeah, you can move everything to multipolygon relations, even a simple square. Problem is readability and maintainability. Once the same way (or segment) belongs to more than one relation, interpreting the data becomes harder for humans. You move to a more abstractive world where only few people feel confortable.</p>
</div>
<div id="comment-29120-info" class="comment-info">
<span class="comment-age">(16 Dec '13, 14:53)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="29122"></span>
<div id="comment-29122" class="comment">
<div id="post-29122-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Pieren</span>: Thank you. Yes, it has many downsides. But using overlapping ways also has downsides. I still think that my answer is helpful to the original question, which <em>is</em> about multipolys.</p>
</div>
<div id="comment-29122-info" class="comment-info">
<span class="comment-age">(16 Dec '13, 15:11)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="29162"></span>
<div id="comment-29162" class="comment">
<div id="post-29162-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>you can create a multipolygon and won't have any problems or overlapping ways. You simply add the fence-tag to the fence-pieces and leave the non-fence parts of the perimeter untagged (but you add them as outer parts to the multipolygon relation).</p>
</div>
<div id="comment-29162-info" class="comment-info">
<span class="comment-age">(18 Dec '13, 12:50)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
</div>
<div id="comment-tools-29113" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29113-form-container" class="comment-form-container">
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

