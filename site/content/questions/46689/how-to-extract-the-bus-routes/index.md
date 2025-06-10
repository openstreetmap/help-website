+++
type = "question"
title = "how to extract the bus routes?"
description = '''i can&#x27;t download the bus routes, could you help me? thanks'''
date = "2015-11-18T20:36:00Z"
lastmod = "2023-06-01T14:18:00Z"
weight = 46689
keywords = [ "bus", "busroutes" ]
aliases = [ "/questions/46689" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [how to extract the bus routes?](/questions/46689/how-to-extract-the-bus-routes)

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
<span id="post-46689-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46689-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46689-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>i can't download the bus routes, could you help me? thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-busroutes" rel="tag" title="see questions tagged &#39;busroutes&#39;">busroutes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Nov '15, 20:36</strong></p>
<img src="https://secure.gravatar.com/avatar/0b44ec741cdb4fd0764a4004a7bfec6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pable%C3%B1o89&#39;s gravatar image" />
<p><span>pableño89</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pableño89 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-46689" class="comments-container">
<span id="46690"></span>
<div id="comment-46690" class="comment">
<div id="post-46690-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Can you explain in a little more detail what you are trying to do?</p>
</div>
<div id="comment-46690-info" class="comment-info">
<span class="comment-age">(18 Nov '15, 21:07)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="46706"></span>
<div id="comment-46706" class="comment">
<div id="post-46706-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hello, i need to export the public transport of Málaga,Spain. But when i click in export button (<a href="https://www.openstreetmap.org/export#map=15/36.7238/-4.4105&amp;layers=T)">https://www.openstreetmap.org/export#map=15/36.7238/-4.4105&amp;layers=T)</a> , it appears something like that(<a href="http://api.openstreetmap.org/api/0.6/map?bbox=-4.5032,36.6774,-4.3288,36.7616).">http://api.openstreetmap.org/api/0.6/map?bbox=-4.5032,36.6774,-4.3288,36.7616).</a> I'm doing a transport task and i only need the the bus routes in shp or something for arcGIS. thank you</p>
</div>
<div id="comment-46706-info" class="comment-info">
<span class="comment-age">(19 Nov '15, 09:00)</span> <span class="comment-user userinfo">pableño89</span>
</div>
</div>
<span id="46711"></span>
<div id="comment-46711" class="comment">
<div id="post-46711-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>In that case, see my answer below. The only thing left is to find a way to convert to shapefile. I think the most convenient would be to export as a GeoJSON and then use the free QGIS (similar to ArcGIS but more flexible) to convert to shapefile.</p>
</div>
<div id="comment-46711-info" class="comment-info">
<span class="comment-age">(19 Nov '15, 10:54)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
</div>
<div id="comment-tools-46689" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46689-form-container" class="comment-form-container">
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

<span id="46700"></span>

<div id="answer-container-46700" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46700-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46700-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-46700-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pableño89 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As <a href="http://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> said: if you don't explain what you have tried and what you are trying to achieve, it's hard to answer questions. I'll make the assumption that it's a simple question.</p>
<p>If you don't need a lot of bus routes (e.g. only bus routes in Colombia), you could use Overpass-turbo. You can find <a href="http://wiki.openstreetmap.org/wiki/Relation:route#Bus_routes_.28also_trolley_bus.29">the data model here</a>. Overpass-turbo is almost self explanatory thanks to the wizard. Here's an example for getting bus rout relations: <a href="http://overpass-turbo.eu/s/cOK">http://overpass-turbo.eu/s/cOK</a> You can then use Export to download in a number of data formats.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Nov '15, 08:14</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-46700" class="comments-container">
&#10;</div>
<div id="comment-tools-46700" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46700-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="87330"></span>

<div id="answer-container-87330" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87330-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87330-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87330-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://overpass-turbo.eu/">https://overpass-turbo.eu/</a></p>
<pre><code>[out:json][timeout:25];
// gather results
(
  // substitute the id the relation(e.g. route) that you want to query
  relation(1895592); &gt;&gt;;
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jun '23, 14:18</strong></p>
<img src="https://secure.gravatar.com/avatar/624807d51d1efdde9d4cfa037b098119?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="a_g&#39;s gravatar image" />
<p><span>a_g</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="a_g has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Jun '23, 14:20</strong> </span></p>
</div>
</div>
<div id="comments-container-87330" class="comments-container">
&#10;</div>
<div id="comment-tools-87330" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87330-form-container" class="comment-form-container">
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

