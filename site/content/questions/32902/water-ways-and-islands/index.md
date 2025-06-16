+++
type = "question"
title = "water ways and islands"
description = '''im trying to add waterways and islands in an area.I dnt have much idea about it,still i made waterways after a long try.But there is an island in the river.I marked the island area as landuse.But still its shown as apart of river.can anybody help with this? Pls tell me the correct n easiest way to d...'''
date = "2014-05-06T13:12:00Z"
lastmod = "2014-05-08T11:26:00Z"
weight = 32902
keywords = [ "island", "waterway" ]
aliases = [ "/questions/32902" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [water ways and islands](/questions/32902/water-ways-and-islands)

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
<span id="post-32902-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32902-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-32902-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>im trying to add waterways and islands in an area.I dnt have much idea about it,still i made waterways after a long try.But there is an island in the river.I marked the island area as landuse.But still its shown as apart of river.can anybody help with this? Pls tell me the correct n easiest way to draw waterways and islands etc.</p>
<p>the part now editing</p>
<p><a href="https://www.openstreetmap.org/edit?editor=id#map=17/10.18260/76.21570">https://www.openstreetmap.org/edit?editor=id#map=17/10.18260/76.21570</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-island" rel="tag" title="see questions tagged &#39;island&#39;">island</span> <span class="post-tag tag-link-waterway" rel="tag" title="see questions tagged &#39;waterway&#39;">waterway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 May '14, 13:12</strong></p>
<img src="https://secure.gravatar.com/avatar/3f41fc43cde9e1fe7707bcc692eb0b99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="muzirian&#39;s gravatar image" />
<p><span>muzirian</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="muzirian has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-32902" class="comments-container">
&#10;</div>
<div id="comment-tools-32902" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32902-form-container" class="comment-form-container">
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

<span id="32915"></span>

<div id="answer-container-32915" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32915-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32915-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-32915-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello, your question is answered in this thread with specific reference to the iD editor :- <a href="/questions/8129/how-to-make-a-hole-in-an-area-eg-woodland">https://help.openstreetmap.org/questions/8129/how-to-make-a-hole-in-an-area-eg-woodland</a> Specificaly your outer ways should be all joined together, either as individual ways or (which should be easiest), one continuous way, and all tagged as waterway=riverbank. The island drawn as a continuous way and tagged as landuse=residential. A multipolygon can then be created by selecting all ways at the same time, with the river banks as outer roles and island as an inner role. Check the roles after creating the multipolygon. As is explained here :- <a href="https://wiki.openstreetmap.org/wiki/Tag:waterway%3Driverbank">https://wiki.openstreetmap.org/wiki/Tag:waterway%3Driverbank</a> This is a fairly simple procedure in JOSM but iD might not be so.</p>
<p>Also with regard to this particular water way, the new waterway should be joined to the existing waterway Periyar to make the various sections of water one complete body. The middle new arm joins correctly but both the north west and the eastern arms do not. Lastly don't forget to add the two bridges to the road under which your new water flows.</p>
<p>Regards</p>
<p>PS If you still have trouble I can fix it for you, you'll then see how it could be achieved.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 May '14, 19:25</strong></p>
<img src="https://secure.gravatar.com/avatar/e3283a6b5f83e16214ec39a1478f64f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BCNorwich&#39;s gravatar image" />
<p><span>BCNorwich</span><br />
<span class="score" title="6299 reputation points"><span>6.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="44 badges"><span class="silver">●</span><span class="badgecount">44</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BCNorwich has 44 accepted answers">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 May '14, 19:28</strong> </span></p>
</div>
</div>
<div id="comments-container-32915" class="comments-container">
<span id="32919"></span>
<div id="comment-32919" class="comment">
<div id="post-32919-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>thanks a lot.this is what i want .: josm feels a bit complicated. And still i cant coorect the map.</p>
</div>
<div id="comment-32919-info" class="comment-info">
<span class="comment-age">(06 May '14, 21:18)</span> <span class="comment-user userinfo">muzirian</span>
</div>
</div>
<span id="32929"></span>
<div id="comment-32929" class="comment">
<div id="post-32929-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>All done now, please have a look. Had quite a few problems resolving conflicts, found more problems as well. Possibly due to folk having a look to see what's wrong and moving things around. In the end had to correct just one thing at a time and upload it.</p>
</div>
<div id="comment-32929-info" class="comment-info">
<span class="comment-age">(07 May '14, 07:21)</span> <span class="comment-user userinfo">BCNorwich</span>
</div>
</div>
</div>
<div id="comment-tools-32915" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32915-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="32905"></span>

<div id="answer-container-32905" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32905-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32905-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-32905-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Muzirian, be shure to connect both riverbanks together by cutting the river, stream or lake into, <a href="https://www.openstreetmap.org/#map=17/52.48985/4.78471">https://www.openstreetmap.org/#map=17/52.48985/4.78471</a> and please read these pages too, <a href="https://wiki.openstreetmap.org/wiki/River">https://wiki.openstreetmap.org/wiki/River</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 May '14, 14:53</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 May '14, 15:00</strong> </span></p>
</div>
</div>
<div id="comments-container-32905" class="comments-container">
<span id="32908"></span>
<div id="comment-32908" class="comment">
<div id="post-32908-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was looking for some info on the correct way to do this.</p>
<p>Thnks for the example,its a great reference.</p>
</div>
<div id="comment-32908-info" class="comment-info">
<span class="comment-age">(06 May '14, 17:19)</span> <span class="comment-user userinfo">muzirian</span>
</div>
</div>
<span id="32910"></span>
<div id="comment-32910" class="comment">
<div id="post-32910-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>But in that example the islands are small and are tagged as farm meadow etc.But for the part which im editing has bigger islands with buildings roads etc it cant be tagged in whole as farmland mradow etc. How can u tell me how to split a water body into two streams so that it can flow around an island. Or can u take a look at this <a href="https://www.openstreetmap.org/edit?editor=id#map=16/10.1833/76.2152">https://www.openstreetmap.org/edit?editor=id#map=16/10.1833/76.2152</a></p>
<p>this area has many parts like that.</p>
</div>
<div id="comment-32910-info" class="comment-info">
<span class="comment-age">(06 May '14, 17:38)</span> <span class="comment-user userinfo">muzirian</span>
</div>
</div>
<span id="32911"></span>
<div id="comment-32911" class="comment">
<div id="post-32911-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Made in P2, just for the creation of the multipolygonen with inner and outer. The 'outer' tag, has to be added last while the inners can be added on the job.</p>
</div>
<div id="comment-32911-info" class="comment-info">
<span class="comment-age">(06 May '14, 17:41)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="32912"></span>
<div id="comment-32912" class="comment">
<div id="post-32912-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>i think we have problems in comunication</p>
</div>
<div id="comment-32912-info" class="comment-info">
<span class="comment-age">(06 May '14, 18:02)</span> <span class="comment-user userinfo">muzirian</span>
</div>
</div>
</div>
<div id="comment-tools-32905" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32905-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="32903"></span>

<div id="answer-container-32903" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32903-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32903-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32903-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I haven't used id for polygons I use Potlatch2. but the riverbank polygon needs to form a complete polygon, you can split the river in sections to do that, otherwise the polygon would be too big.It can't be tagged as a riverbank polygon until its end join up. The islands first and last node(s) must also join to become one. When both polygons are done they both have to be selected so cntl click both then select multipolygon. If you search these questions for islands you will get lots of similar Q and As. If you search the map for an island in a river you could carefully open your editor and use that as an example. I just tried to sort a bit of the riverbank with iD but i/you would need the plot an area not a line. So I have edited the section with potlatch2. This is the section I've re-done for you to study. for details see my editing note. <a href="https://www.openstreetmap.org/search?query=%2056%20-.2#map=16/10.1835/76.2141">https://www.openstreetmap.org/search?query=%2056%20-.2#map=16/10.1835/76.2141</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 May '14, 14:30</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 May '14, 19:50</strong> </span></p>
</div>
</div>
<div id="comments-container-32903" class="comments-container">
<span id="32904"></span>
<div id="comment-32904" class="comment">
<div id="post-32904-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>here is a similar question <a href="/questions/22483/islands-in-lakes-not-showing">https://help.openstreetmap.org/questions/22483/islands-in-lakes-not-showing</a></p>
</div>
<div id="comment-32904-info" class="comment-info">
<span class="comment-age">(06 May '14, 14:45)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="32909"></span>
<div id="comment-32909" class="comment">
<div id="post-32909-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>there is some problem with potlatch for tagging areas with water.But it works fine with id and josm for me.</p>
</div>
<div id="comment-32909-info" class="comment-info">
<span class="comment-age">(06 May '14, 17:20)</span> <span class="comment-user userinfo">muzirian</span>
</div>
</div>
<span id="32921"></span>
<div id="comment-32921" class="comment">
<div id="post-32921-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Muzirian, some remarks, read the River pages in the Wiki. Please look at the ways carefully. I have added some. Theres a node in the river but different from the riverbanks name ? Connect the triangle ways and the riverbanks by selecting them and connect them. Read the Wiki <a href="https://wiki.openstreetmap.org/wiki/Wood">https://wiki.openstreetmap.org/wiki/Wood</a> as well. You have drawn single ways; a way has always to tags at each side, riverbank and forest. You’ll have to draw each line 2 times and connect them, look at the island. Please look at the work of other mappers in your area and communicate with them. Keep mapping and welcome</p>
</div>
<div id="comment-32921-info" class="comment-info">
<span class="comment-age">(07 May '14, 00:55)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="32969"></span>
<div id="comment-32969" class="comment">
<div id="post-32969-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have asked a related Q <a href="/questions/32968/id-editor-lines-and-areas">https://help.openstreetmap.org/questions/32968/id-editor-lines-and-areas</a></p>
</div>
<div id="comment-32969-info" class="comment-info">
<span class="comment-age">(08 May '14, 11:26)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-32903" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32903-form-container" class="comment-form-container">
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

