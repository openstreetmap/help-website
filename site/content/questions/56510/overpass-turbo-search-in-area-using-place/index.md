+++
type = "question"
title = "overpass turbo search in area using place="
description = '''Hey! I have problems, finding supermarkets in a district of a city, using area. I found an example (https://github.com/mapbox/mapping/wiki/Overpass-Guide) which gives me all mountain peaks in the dolomites and tried to adapt it to my needs. Problem is: I can find my desired city (Hamburg) with place...'''
date = "2017-06-08T08:46:00Z"
lastmod = "2017-06-11T17:44:00Z"
weight = 56510
keywords = [ "overpass", "place", "overpass-turbo", "area" ]
aliases = [ "/questions/56510" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [overpass turbo search in area using place=](/questions/56510/overpass-turbo-search-in-area-using-place)

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
<span id="post-56510-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56510-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56510-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey! I have problems, finding supermarkets in a district of a city, using area. I found an example (<a href="https://github.com/mapbox/mapping/wiki/Overpass-Guide)">https://github.com/mapbox/mapping/wiki/Overpass-Guide)</a> which gives me all mountain peaks in the dolomites and tried to adapt it to my needs. Problem is: I can find my desired city (Hamburg) with place=city, but i´m not able to find districts, using borough, suburb or quarter or whatever. I would be so glad, if somebody could help me out! I´m pretty new to this whole thing, and i just want to find supermarkets in districts of hamburg. Maybe ther is even a way better approach? This is my code so far:</p>
<pre><code>*/
[out:json];
&#10;area
  [place=city]
  [&quot;name&quot;=&quot;Hamburg&quot;];
out body;
// query part
node
  [shop=supermarket]
  (area);
out body;
// outline
relation
  [place=city]
  [&quot;name&quot;=&quot;Hamburg&quot;];
&gt;;
out skel qt;</code></pre>
<p>Thank you guys so much! Cheers</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-place" rel="tag" title="see questions tagged &#39;place&#39;">place</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jun '17, 08:46</strong></p>
<img src="https://secure.gravatar.com/avatar/4c836c0daf4572c935757bee628e97f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="razer969&#39;s gravatar image" />
<p><span>razer969</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="razer969 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jun '17, 08:50</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-56510" class="comments-container">
&#10;</div>
<div id="comment-tools-56510" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56510-form-container" class="comment-form-container">
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

<span id="56511"></span>

<div id="answer-container-56511" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56511-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56511-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-56511-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="razer969 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try the <a href="http://overpass-turbo.eu/">Overpass Turbo</a> wizard, type "shop=supermarket in Hamburg" without the quotes in the wizard , zoom to see Hamburg on the map, build query and run query.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jun '17, 09:02</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Jun '17, 09:07</strong> </span></p>
</div>
</div>
<div id="comments-container-56511" class="comments-container">
<span id="56512"></span>
<div id="comment-56512" class="comment">
<div id="post-56512-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hey nevw, thanks for the quick response first of all! Problem is: I want to query a search for a specific district in hamburg. The code I posted above does search for supermarkets in hamburg, but i want to specify that and search only in various districts. I tried using place=district, place=borough and so on (every entry i found in the wiki for place=) but it just doesn´t work. So any help on that end would be greatly appreciated!</p>
</div>
<div id="comment-56512-info" class="comment-info">
<span class="comment-age">(08 Jun '17, 09:11)</span> <span class="comment-user userinfo">razer969</span>
</div>
</div>
<span id="56514"></span>
<div id="comment-56514" class="comment">
<div id="post-56514-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Can you name an example for such a district?</p>
</div>
<div id="comment-56514-info" class="comment-info">
<span class="comment-age">(08 Jun '17, 09:33)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="56515"></span>
<div id="comment-56515" class="comment">
<div id="post-56515-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>sorry, I don't know the area but this works fine and is suburb? "shop=supermarket in Altona-Altstadt"<br />
I would expect that you could extract those listed here <a href="https://wambachers-osm.website/boundaries/">https://wambachers-osm.website/boundaries/</a></p>
</div>
<div id="comment-56515-info" class="comment-info">
<span class="comment-age">(08 Jun '17, 09:34)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="56581"></span>
<div id="comment-56581" class="comment">
<div id="post-56581-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the help! I solved the problem using part of the wizard´s code to specify the searching area like this:</p>
<p>(area[admin_level=9]["name"="Eimsbüttel"][boundary=administrative]-&gt;.boundaryarea;)</p>
</div>
<div id="comment-56581-info" class="comment-info">
<span class="comment-age">(11 Jun '17, 17:44)</span> <span class="comment-user userinfo">razer969</span>
</div>
</div>
</div>
<div id="comment-tools-56511" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56511-form-container" class="comment-form-container">
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

