+++
type = "question"
title = "Extracting features that are inside a polygon set with overpass api"
description = '''I need to display school building. i have made the outer area of school and tagged it as amenity=school. there are some buildings inside the area, i need the data of the buildings.  using overpass api&#x27;s around clause i can get them but it also gives some buildings that are outside the school. i am t...'''
date = "2013-04-08T19:35:00Z"
lastmod = "2013-04-16T20:43:00Z"
weight = 21330
keywords = [ "overpass", "school", "area" ]
aliases = [ "/questions/21330" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Extracting features that are inside a polygon set with overpass api](/questions/21330/extracting-features-that-are-inside-a-polygon-set-with-overpass-api)

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
<span id="post-21330-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21330-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21330-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need to display school building. i have made the outer area of school and tagged it as amenity=school. there are some buildings inside the area, i need the data of the buildings.</p>
<p>using overpass api's around clause i can get them but it also gives some buildings that are outside the school. i am trying to use the area or pivot clause, but the results are empty. the overpass query is</p>
<pre><code>(way({{bbox}})[&#39;amenity&#39;~&#39;school|college|hospital|clinic&#39;];node(w);)-&gt;.boundary;(way(area.boundary);node(w););out skel;</code></pre>
<p>the <a href="http://overpass-turbo.eu/?Q=(way(%7B%7Bbbox%7D%7D)%5B&#39;amenity&#39;~&#39;school%7Ccollege%7Chospital%7Cclinic&#39;%5D%3Bnode(w)%3B%0A)-%3E.boundary%3B%0A%0A(way(area.boundary)%3Bnode(w)%3B)%3B%0A%0Aout%20skel%3B&amp;C=27.70645;85.32142;18&amp;R">test area</a></p>
<p>it should be like <a href="http://overpass-turbo.eu/?q=KCDEgCDEg25vZGUoe3tiYm94fX0pWyduYW1lJ34nc2Nob29sJHxjxKBsZWdlJCddO8SDKcStxIHEg8SExIbEiMSKxIzEjsSQxJInYnVpbGRpbmfEmcSbxJ3En2zEo8SlxKdlfGdvdmVybsSXbnTEq8SwxK_Eg8SCxLPEh8SJxIvEjcSPxJHEk8SWZW5pdHnFhMScxJ7EoMWJbMSmxKh8cHVibGljX8S8xL7FgMWCxZfErsSwxZsgxIXFncS2xaDEucSTb2ZmxbfEmMSaxY7FkMWSxZTFlsSsxb_FmsSyIHdhecWexLfFocS6xJXEl8WqxYbEoMSixKTFr8WLxKpdW8W6xL_FgWfGlMSyxoPEiHfFmSDGtcaWxLLGmcabxoXEuMWixLvEvcatxb3EmsWrxYfFrsWwxYzGj8WRxZPFpcaTxLDFnMazxrXGtcaBxrrGnMaGxr7FpMWmxajGosWsxYjGpseHxbLFtMW2xbjGrMW8xYPGsMePKMa0xZjFmCAtPi5hxK3HqcaaKGFyb3VuZCDHsCA6IDUwxJLHpMauxKzGssepxK_Fmce4dCDEl3THsQ&amp;c=BslsvZzEPS&amp;R">this</a></p>
<p>P.S. all the building have been tagged as building=school, which gives a shorter query. but i need to use the area clause because they might not be tagged properly in other places.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-school" rel="tag" title="see questions tagged &#39;school&#39;">school</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Apr '13, 19:35</strong></p>
<img src="https://secure.gravatar.com/avatar/651103e616e49724bb139f1a3e0a1a39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amritkarma&#39;s gravatar image" />
<p><span>amritkarma</span><br />
<span class="score" title="684 reputation points">684</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amritkarma has one accepted answer">11%</span></p>
</div>
</div>
<div id="comments-container-21330" class="comments-container">
&#10;</div>
<div id="comment-tools-21330" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21330-form-container" class="comment-form-container">
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

<span id="21384"></span>

<div id="answer-container-21384" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21384-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21384-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-21384-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="amritkarma has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The areas in Overpass API are generated for ways with specific tags only, for example for ways with a name and "area=yes" or a name and any value of "landuse".</p>
<p>I would recommend to retag way 142778170 with "amenity=school" and "area=yes" instead of "area=school". Then Overpass API would generate in the next run an area for that campus. This may take some hours, the timestamp "areas" in the meta tag of the returned data must become newer than your edit. Then you can select the buildings with</p>
<pre><code>way[amenity=school]({{bbox}});
node(w);is_in;
area._[amenity=school];
(
  way(area)[building];
  node(w);
);
out;</code></pre>
<p>like in <a href="http://overpass-turbo.eu/?Q=way%5Bamenity%3Dschool%5D(%7B%7Bbbox%7D%7D)%3B%0Anode(w)%3Bis_in%3B%0Aarea._%5Bamenity%3Dschool%5D%3B%0A(%0A%20%20way(area)%5Bbuilding%5D%3B%0A%20%20node(w)%3B%0A)%3B%0Aout%3B%0A&amp;C=50.74598;7.05563;18">this</a> example.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Apr '13, 06:20</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-21384" class="comments-container">
<span id="21385"></span>
<div id="comment-21385" class="comment">
<div id="post-21385-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>does it work for amenity=college,hospital,clinic? it has been tagged as amenity = college</p>
</div>
<div id="comment-21385-info" class="comment-info">
<span class="comment-age">(11 Apr '13, 07:45)</span> <span class="comment-user userinfo">amritkarma</span>
</div>
</div>
<span id="21393"></span>
<div id="comment-21393" class="comment">
<div id="post-21393-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Looks like it works for hospitals and schools, but not for colleges and clinics. Is there any workaround for colleges and clinics.</p>
</div>
<div id="comment-21393-info" class="comment-info">
<span class="comment-age">(11 Apr '13, 09:12)</span> <span class="comment-user userinfo">amritkarma</span>
</div>
</div>
<span id="21609"></span>
<div id="comment-21609" class="comment">
<div id="post-21609-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please try again. I have enlarged the scope of the areas, at least on overpass-api.de</p>
</div>
<div id="comment-21609-info" class="comment-info">
<span class="comment-age">(16 Apr '13, 20:43)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
</div>
<div id="comment-tools-21384" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21384-form-container" class="comment-form-container">
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

