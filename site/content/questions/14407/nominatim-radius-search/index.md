+++
type = "question"
title = "Nominatim radius search"
description = '''Hello, I am looking for a way to search businesses within a circle (or a polygon) around a GPS coord. It will be nice if I am able to additionally filter results by passing in a parameter such as &quot;coffee&quot; or &quot;school&quot;. I looked around, but could not find exactly what I wanted. I have looked at the wi...'''
date = "2012-07-19T20:26:00Z"
lastmod = "2018-11-06T14:30:00Z"
weight = 14407
keywords = [ "search", "nominatim" ]
aliases = [ "/questions/14407" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim radius search](/questions/14407/nominatim-radius-search)

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
<span id="post-14407-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14407-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-14407-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I am looking for a way to search businesses within a circle (or a polygon) around a GPS coord. It will be nice if I am able to additionally filter results by passing in a parameter such as "coffee" or "school". I looked around, but could not find exactly what I wanted. I have looked at the wiki page for Nominatim, various other forums etc. Here are couple of searches i tried which gave me only one result. How do i increase the number of results I get back?</p>
<p><a href="http://nominatim.openstreetmap.org/search?format=xml&amp;q=41.760584,-88.320071">http://nominatim.openstreetmap.org/search?format=xml&amp;q=41.760584,-88.320071</a> That returns only one place thats at that specific lat lon.</p>
<p><a href="http://nominatim.openstreetmap.org/search?format=xml&amp;viewbox=-88.85,42.25,-87.65,41.05&amp;q=coffee&amp;bounded=1&amp;limit=100">http://nominatim.openstreetmap.org/search?format=xml&amp;viewbox=-88.85,42.25,-87.65,41.05&amp;q=coffee&amp;bounded=1&amp;limit=100</a> That returns a few (&lt;100) coffee shops in the bounding box, however, they are definitely not all.</p>
<p>Finally, if I want all places in the bounding box, (so if I omit the "q" param) I dont get any results at all.</p>
<p>So, how to really do this?</p>
<p>Best, Sachin Dole</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jul '12, 20:26</strong></p>
<img src="https://secure.gravatar.com/avatar/bc295681820a98a9c317fafe0f895fdd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sdole&#39;s gravatar image" />
<p><span>sdole</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sdole has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-14407" class="comments-container">
&#10;</div>
<div id="comment-tools-14407" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14407-form-container" class="comment-form-container">
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

<span id="14524"></span>

<div id="answer-container-14524" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14524-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14524-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-14524-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim understands the <em>near</em> keyword to search for certain POI types around a coordinate. For example, you can ask for schools around a geo point like this:</p>
<p><a href="http://nominatim.openstreetmap.org/search?q=school%20near%20%5B41.760584,-88.320071%5D"></a><a href="http://nominatim.openstreetmap.org/search?q=school">http://nominatim.openstreetmap.org/search?q=school</a> near [41.760584,-88.320071]</p>
<p>The types of POIs that Nominatim currently understands are listed on <a href="http://wiki.openstreetmap.org/wiki/Nominatim/Special_Phrases/EN">this page of special phrases</a>.</p>
<p>Note however, this query will not necessarily get you all the schools in the area but only a selection. Nominatim is a search tool after all, not a tool for downloading data. If you need complete lists, the Overpass or XAPI are indeed better suited.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jul '12, 22:57</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-14524" class="comments-container">
<span id="66697"></span>
<div id="comment-66697" class="comment">
<div id="post-66697-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Such a bad api. If I want to search for school in my language (Russian) I have to replace "near" to my language as well, школа возле [41.760584,-88.320071]. I can't do it programmatically for all languages and how I'm supposed to detect the language user types.</p>
</div>
<div id="comment-66697-info" class="comment-info">
<span class="comment-age">(06 Nov '18, 14:05)</span> <span class="comment-user userinfo">user5555</span>
</div>
</div>
<span id="66699"></span>
<div id="comment-66699" class="comment">
<div id="post-66699-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>1) There is Overpass API which might be better suited for your use case. 2) Detecting the user language can be done by looking at the browser's language setting, i.e. at the <code>Accept-Language</code> header.</p>
</div>
<div id="comment-66699-info" class="comment-info">
<span class="comment-age">(06 Nov '18, 14:30)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-14524" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14524-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="14412"></span>

<div id="answer-container-14412" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14412-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14412-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-14412-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>See the <a href="http://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a> or the <a href="http://wiki.openstreetmap.org/wiki/Xapi">XAPI</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jul '12, 21:31</strong></p>
<img src="https://secure.gravatar.com/avatar/97f754e0356a74acc666550948b48bd6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hfs&#39;s gravatar image" />
<p><span>hfs</span><br />
<span class="score" title="851 reputation points">851</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hfs has 3 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-14412" class="comments-container">
<span id="66698"></span>
<div id="comment-66698" class="comment">
<div id="post-66698-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, it has such function, but how to search for random query input? What would be equal to "search?q=*" of Nominatim API. Overpass API has tags like "name", "amenity" and so on but they are useless 'cause API expect full match (100%) with query you input for searching, so it doesn't work like Nominatim API or Google Search</p>
</div>
<div id="comment-66698-info" class="comment-info">
<span class="comment-age">(06 Nov '18, 14:09)</span> <span class="comment-user userinfo">user5555</span>
</div>
</div>
</div>
<div id="comment-tools-14412" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14412-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="14493"></span>

<div id="answer-container-14493" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14493-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14493-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-14493-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As written before:</p>
<p>If you want for example all schools around the coordinate 41.76 north 88.32 east, please use [<a href="http://overpass-api.de/api/interpreter?data=(way(bbox)%5Bamenity=school%5D;%3E;node(bbox)%5Bamenity=school%5D;);out;&amp;bbox=-88.4,41.7,-88.3,41.8%5D%5B1%5D">http://overpass-api.de/api/interpreter?data=(way(bbox)[amenity=school];&gt;;node(bbox)[amenity=school];);out;&amp;bbox=-88.4,41.7,-88.3,41.8][1]</a></p>
<p>Similarly, you can get all cafes with [<a href="http://overpass-api.de/api/interpreter?data=(way(bbox)%5Bamenity=cafe%5D;%3E;node(bbox)%5Bamenity=cafe%5D;);out;&amp;bbox=-88.4,41.7,-88.3,41.8%5D%5B2%5D">http://overpass-api.de/api/interpreter?data=(way(bbox)[amenity=cafe];&gt;;node(bbox)[amenity=cafe];);out;&amp;bbox=-88.4,41.7,-88.3,41.8][2]</a> Apparently, there are none in the database. You also don't see any on the Mapnik map there.</p>
<p>The location is specified as bounding box. Thus, the radius is controlled by the difference between the two longitude or latitude values.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jul '12, 08:57</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
</div>
<div id="comments-container-14493" class="comments-container">
&#10;</div>
<div id="comment-tools-14493" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14493-form-container" class="comment-form-container">
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

