+++
type = "question"
title = "How to query all elements within an outline way from Overpass API?"
description = '''Given the id of a closed way which represents an area, as indicated by an &quot;area&quot; tag such as building=*, how can I retrieve all nodes/ways contained entirely or partially within that area from Overpass API? What I have found so far is area-query, which sounds as if it should cover this use case, and...'''
date = "2013-03-20T18:40:00Z"
lastmod = "2014-04-21T10:54:00Z"
weight = 20841
keywords = [ "overpass", "area", "closed_way", "query" ]
aliases = [ "/questions/20841" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to query all elements within an outline way from Overpass API?](/questions/20841/how-to-query-all-elements-within-an-outline-way-from-overpass-api)

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
<span id="post-20841-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20841-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-20841-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Given the id of a closed way which represents an area, as indicated by an "area" tag such as building=*, how can I retrieve all nodes/ways contained entirely or partially within that area from Overpass API?</p>
<p>What I have found so far is <em>area-query</em>, which sounds as if it should cover this use case, and it works as expected for areas represented as multipolygons (if you remember to add the magic number 3600000000 to the id):</p>
<pre><code>&lt;query type=&quot;node&quot;&gt;
  &lt;area-query ref=&quot;3600015228&quot;/&gt;
&lt;/query&gt;</code></pre>
<p><a href="http://overpass-turbo.eu/?Q=%3Cosm-script%20output%3D%22json%22%3E%0A%20%20%3Cquery%20type%3D%22node%22%3E%0A%20%20%20%20%3Carea-query%20ref%3D%223600015228%22%2F%3E%0A%20%20%3C%2Fquery%3E%0A%20%20%3Cprint%20mode%3D%22body%22%2F%3E%0A%3C%2Fosm-script%3E&amp;C=48.57056;13.45693;18&amp;R"><em>(Overpass Turbo)</em></a></p>
<p>I've found a hint that adding 2400000000 to the id might do the trick for closed ways. However, this does not appear to work:</p>
<pre><code>&lt;query type=&quot;node&quot;&gt;
  &lt;area-query ref=&quot;2501518744&quot;/&gt;
&lt;/query&gt;</code></pre>
<p><a href="http://overpass-turbo.eu/?Q=%3Cosm-script%20output%3D%22json%22%3E%0A%20%20%3Cquery%20type%3D%22node%22%3E%0A%20%20%20%20%3Carea-query%20ref%3D%222501518744%22%2F%3E%0A%20%20%3C%2Fquery%3E%0A%20%20%3Cprint%20mode%3D%22body%22%2F%3E%0A%3C%2Fosm-script%3E&amp;C=48.56936;13.44751;18&amp;R"><em>(Overpass Turbo)</em></a></p>
<p>This example query for way <a href="https://www.openstreetmap.org/browse/way/101518744">101518744</a> should return <a href="https://www.openstreetmap.org/browse/node/1172225070">1172225070</a> as well as other nodes, but the result is empty. Is there something I'm missing?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span> <span class="post-tag tag-link-closed_way" rel="tag" title="see questions tagged &#39;closed_way&#39;">closed_way</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Mar '13, 18:40</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-20841" class="comments-container">
&#10;</div>
<div id="comment-tools-20841" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20841-form-container" class="comment-form-container">
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

<span id="20865"></span>

<div id="answer-container-20865" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20865-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20865-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-20865-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In short: an area for the given way has never been generated because the way has no name. I'm sorry that there is no immediate solution to your problem.</p>
<p>In more detail: <a href="https://github.com/drolbr/Overpass-API/blob/master/rules/areas.osm3s">https://github.com/drolbr/Overpass-API/blob/master/rules/areas.osm3s</a> contains the rules what objects are recognized as areas.</p>
<p>In particular, ways are selected there only if they have a name and one of various other tags (including "building=yes"). This ruleset isn't a fixed law, but rather reflects the discussion on the mailing list. It is likely to be incomplete anyway. Please send a mail to talk(at)openstreetmap.org to put the discussion further. I'll then expand the list when there is consensus that this is useful.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Mar '13, 08:22</strong></p>
<img src="https://secure.gravatar.com/avatar/fcfdb0825826fd13d2ff0d83d58819c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland%20Olbricht&#39;s gravatar image" />
<p><span>Roland Olbricht</span><br />
<span class="score" title="6666 reputation points"><span>6.7k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland Olbricht has 40 accepted answers">36%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Mar '13, 08:23</strong> </span></p>
</div>
</div>
<div id="comments-container-20865" class="comments-container">
<span id="20920"></span>
<div id="comment-20920" class="comment">
<div id="post-20920-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've taken this to talk now, as you asked: <a href="http://lists.openstreetmap.org/pipermail/talk/2013-March/066538.html">Thread archive</a></p>
</div>
<div id="comment-20920-info" class="comment-info">
<span class="comment-age">(22 Mar '13, 20:03)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-20865" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20865-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="28496"></span>

<div id="answer-container-28496" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28496-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28496-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-28496-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Is there some changes/news regarding this question which seems important. It would be very useful to have the possibility to make queries using for exemple ways[landuse] without name.</p>
<p>Ex : Finding all residential buildings, all industrial buildings, etc. depending if they are included in ways with landuse=residential or landuse=industrial etc. but without any name. Most of the time, ways[landuse=residential] don't have name, then we can not use them as areas.</p>
<p>In my use, I need categories of buildings to determine activities surfaces (buildings) on ground. (Building attractions in terms of activities/population)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Nov '13, 16:45</strong></p>
<img src="https://secure.gravatar.com/avatar/b7fc9df1510905dfa125c98598e6595c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="glider90&#39;s gravatar image" />
<p><span>glider90</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="glider90 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-28496" class="comments-container">
<span id="28542"></span>
<div id="comment-28542" class="comment">
<div id="post-28542-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Problem localy solved for me with the installation of a local Overpass server on wich we changed rules for areas (/rules/areas.osm3s). Thanks for this usefull post.</p>
</div>
<div id="comment-28542-info" class="comment-info">
<span class="comment-age">(27 Nov '13, 13:14)</span> <span class="comment-user userinfo">glider90</span>
</div>
</div>
<span id="32488"></span>
<div id="comment-32488" class="comment">
<div id="post-32488-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>FYI: There are now two similar GitHub tickets dealing with this issue:</p>
<p><a href="https://github.com/drolbr/Overpass-API/issues/77">https://github.com/drolbr/Overpass-API/issues/77</a></p>
<p><a href="https://github.com/drolbr/Overpass-API/issues/86">https://github.com/drolbr/Overpass-API/issues/86</a></p>
</div>
<div id="comment-32488-info" class="comment-info">
<span class="comment-age">(21 Apr '14, 10:54)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-28496" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28496-form-container" class="comment-form-container">
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

