+++
type = "question"
title = "Overpass Turbo: Park not highlighted?"
description = '''This is clearly a park. It was marked as such over 4 years ago (in 2013). However, the following query, when done with said park in view, does not highlight it: [bbox:{{bbox}}]; (  way[leisure=park]; ); out body; &amp;gt;; out skel qt;  {{style:  way[leisure=park], { color:blue; fill-color:blue; } }}  I...'''
date = "2018-04-25T09:54:00Z"
lastmod = "2018-04-25T12:15:00Z"
weight = 63123
keywords = [ "park", "highlighting", "overpass-turbo" ]
aliases = [ "/questions/63123" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass Turbo: Park not highlighted?](/questions/63123/overpass-turbo-park-not-highlighted)

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
<span id="post-63123-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63123-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63123-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This is clearly <a href="https://www.openstreetmap.org/relation/3118071">a park</a>. It was marked as such over 4 years ago (in 2013).</p>
<p>However, the following query, when done with said park in view, does not highlight it:</p>
<pre><code>[bbox:{{bbox}}];
(
    way[leisure=park];
);
out body;
&gt;;
out skel qt;
&#10;{{style:
    way[leisure=park],
{ color:blue; fill-color:blue; }
}}</code></pre>
<p>Is there any reason for that? It seems that <code>rel[leisure=park]</code> does highlight it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-park" rel="tag" title="see questions tagged &#39;park&#39;">park</span> <span class="post-tag tag-link-highlighting" rel="tag" title="see questions tagged &#39;highlighting&#39;">highlighting</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Apr '18, 09:54</strong></p>
<img src="https://secure.gravatar.com/avatar/931d7ae976d4b6bc0463ebc6f04a6a9c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="moriakaice&#39;s gravatar image" />
<p><span>moriakaice</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="moriakaice has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-63123" class="comments-container">
&#10;</div>
<div id="comment-tools-63123" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63123-form-container" class="comment-form-container">
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

<span id="63124"></span>

<div id="answer-container-63124" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63124-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63124-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-63124-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="moriakaice has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello,</p>
<p>In your Overpass query you are searching for way with leisure=park tag, but the park you have linked is not a way it's a relation, a multipolygon type relation used to describe a complex area.</p>
<p>You should add relation to your Overpass query by adding <code>relation[leisure=park];</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Apr '18, 10:05</strong></p>
<img src="https://secure.gravatar.com/avatar/487887a5692e82a08bb50e587292033a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kazing&#39;s gravatar image" />
<p><span>Kazing</span><br />
<span class="score" title="66 reputation points">66</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kazing has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-63124" class="comments-container">
<span id="63126"></span>
<div id="comment-63126" class="comment">
<div id="post-63126-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for the answer.</p>
<p>What does make an area a <code>relation</code> and not a <code>way</code>? We've got other parks (like Hyde Park) that are <code>ways</code>.</p>
</div>
<div id="comment-63126-info" class="comment-info">
<span class="comment-age">(25 Apr '18, 10:21)</span> <span class="comment-user userinfo">moriakaice</span>
</div>
</div>
<span id="63127"></span>
<div id="comment-63127" class="comment">
<div id="post-63127-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The relation is used when the area you want to describe is complex, it has holes for examples. See the wiki page for more details/examples <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon">https://wiki.openstreetmap.org/wiki/Relation:multipolygon</a></p>
<p>For Brockwell Park I don't see why it is describe with a relation, but i'm not an expert of multipolygon. And there is nothing that forbids using multipolygon if you think it's more convenient.</p>
</div>
<div id="comment-63127-info" class="comment-info">
<span class="comment-age">(25 Apr '18, 10:31)</span> <span class="comment-user userinfo">Kazing</span>
</div>
</div>
<span id="63128"></span>
<div id="comment-63128" class="comment">
<div id="post-63128-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So on the page you've provided, the examples are having both way and relation, while Brockwell Park seems to be only having a relation, which is very strange for me and, if possible, I'd love to have a <code>way</code> there as well.</p>
</div>
<div id="comment-63128-info" class="comment-info">
<span class="comment-age">(25 Apr '18, 10:44)</span> <span class="comment-user userinfo">moriakaice</span>
</div>
</div>
<span id="63129"></span>
<div id="comment-63129" class="comment">
<div id="post-63129-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The Brockwell Park, also have ways, the ways are all included in the relation that describe the park area, ways can have the role of "outer" perimeter or "inner" perimeter See this way, it describes a part of the park's external perimeter and its included inside the multipolygon relation: <a href="https://www.openstreetmap.org/way/232229963#map=17/51.44733/-0.10696">https://www.openstreetmap.org/way/232229963#map=17/51.44733/-0.10696</a></p>
</div>
<div id="comment-63129-info" class="comment-info">
<span class="comment-age">(25 Apr '18, 10:52)</span> <span class="comment-user userinfo">Kazing</span>
</div>
</div>
<span id="63130"></span>
<div id="comment-63130" class="comment not_top_scorer">
<div id="post-63130-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for pointing it out. Does it mean that, due to the fact those are not marked with <code>leisure=park</code>, the whole thing doesn't get highlighted with my original filter?</p>
<p>Would recreating it/adding appropriate tags fix the problem?</p>
</div>
<div id="comment-63130-info" class="comment-info">
<span class="comment-age">(25 Apr '18, 11:26)</span> <span class="comment-user userinfo">moriakaice</span>
</div>
</div>
<span id="63131"></span>
<div id="comment-63131" class="comment">
<div id="post-63131-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>No, there is no problem in the data. The tags belong on the multipolygon and not on the individual ways (see the first point at <a href="https://wiki.openstreetmap.org/wiki/Relation:multipolygon#Usage">multipolygon#Usage</a>). Otherwise you are creating an old-style multipolygon which has lead to several problems in the past and should be avoided. You have to fix your query, not the data.</p>
</div>
<div id="comment-63131-info" class="comment-info">
<span class="comment-age">(25 Apr '18, 11:46)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="63132"></span>
<div id="comment-63132" class="comment not_top_scorer">
<div id="post-63132-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's a shame. The query itself was rev-eng to cover for what Niantic, developer of Pokemon GO, is likely using for one of the in-game features. Not sure how exactly the data-mining was done to establish the query, but it's sad that only some parks that are marked in OSM will enjoy the feature, while others will miss it (Hyde Park vs Brockwell Park).</p>
</div>
<div id="comment-63132-info" class="comment-info">
<span class="comment-age">(25 Apr '18, 12:15)</span> <span class="comment-user userinfo">moriakaice</span>
</div>
</div>
</div>
<div id="comment-tools-63124" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-63124-form-container" class="comment-form-container">
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

