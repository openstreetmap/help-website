+++
type = "question"
title = "How do I get address range for a given way/street"
description = '''Is there a way to get an address range for a given relation or way? for example, way 102065354 has 10 nodes. I like to know what address range this street segment covers. This is a street segment called &quot;East Santa Fe Street&quot; in Olathe, ks, US. Using Nominatim&#x27;s reverse geocoding api like this http:...'''
date = "2012-11-19T22:58:00Z"
lastmod = "2012-11-21T15:07:00Z"
weight = 17816
keywords = [ "range", "nominatim", "geocoding", "reverse", "address" ]
aliases = [ "/questions/17816" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do I get address range for a given way/street](/questions/17816/how-do-i-get-address-range-for-a-given-waystreet)

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
<span id="post-17816-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17816-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17816-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to get an address range for a given relation or way? for example, <a href="https://www.openstreetmap.org/browse/way/102065354">way 102065354</a> has 10 nodes. I like to know what address range this street segment covers. This is a street segment called "East Santa Fe Street" in Olathe, ks, US. Using Nominatim's reverse geocoding api like this</p>
<p><a href="http://nominatim.openstreetmap.org/reverse?format=xml&amp;osm_type=W&amp;osm_id=102065354&amp;zoom=18&amp;addressdetails=1">http://nominatim.openstreetmap.org/reverse?format=xml&amp;osm_type=W&amp;osm_id=102065354&amp;zoom=18&amp;addressdetails=1</a></p>
<p>returns me the street name, city, state, etc.. but not exactly what I am looking for. I need to know what range of addresses fall in that street segment.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-range" rel="tag" title="see questions tagged &#39;range&#39;">range</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-reverse" rel="tag" title="see questions tagged &#39;reverse&#39;">reverse</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Nov '12, 22:58</strong></p>
<img src="https://secure.gravatar.com/avatar/343237842fce1f7a82f69ebf7a92f6b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kcjailbirds&#39;s gravatar image" />
<p><span>kcjailbirds</span><br />
<span class="score" title="141 reputation points">141</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kcjailbirds has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Nov '12, 10:09</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-17816" class="comments-container">
<span id="17818"></span>
<div id="comment-17818" class="comment">
<div id="post-17818-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There aren't any addresses in the near surrounding of this street in OSM's database so far. But you can try to improve our data and add them.</p>
</div>
<div id="comment-17818-info" class="comment-info">
<span class="comment-age">(20 Nov '12, 06:12)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="17821"></span>
<div id="comment-17821" class="comment">
<div id="post-17821-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you. This was just an example of a street with no address range data. I am asking in general, is it possible to get address ranges for streets? Is there a way to do get that data or extrapolate that range of addresses? Is address range data available anywhere that anyone knows of?</p>
</div>
<div id="comment-17821-info" class="comment-info">
<span class="comment-age">(20 Nov '12, 14:07)</span> <span class="comment-user userinfo">kcjailbirds</span>
</div>
</div>
</div>
<div id="comment-tools-17816" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17816-form-container" class="comment-form-container">
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

<span id="17860"></span>

<div id="answer-container-17860" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17860-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17860-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17860-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It may be not obvious for all but to retrieve address ranges from OSM, someone has to add them first into the OSM database. See the wiki documentation about <a href="https://wiki.openstreetmap.org/wiki/Addresses">addresses</a> and especially the section about <a href="https://wiki.openstreetmap.org/wiki/Addresses#Using_interpolation">address interpolation</a>.</p>
<p>If addresses ranges are missing in your area of interest, either add them into OSM or import them into OSM (only if the source is compatible with the OSM licence) or don't use OSM and look for another source.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Nov '12, 13:31</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-17860" class="comments-container">
&#10;</div>
<div id="comment-tools-17860" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17860-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="17867"></span>

<div id="answer-container-17867" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17867-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17867-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17867-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As far as I know there is no straightforward way for this.</p>
<p>In OSM addresses aren't assigned to way <em>IDs</em> or ways in particular, instead there are separate address <em>nodes</em> and <em>ways</em> (the latter usually corresponding to building outlines or other areas). One exception are the three address relation approaches mentioned <a href="https://wiki.openstreetmap.org/wiki/Addresses#See_also">here</a> but they are rarely used.</p>
<p>One possible solution is to use the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide">OverpassAPI</a> to retrieve all addresses for a specific street name in a given city, or bounding box, or near some specific element.</p>
<p>An example: the following query will return all address <em>nodes</em> for the street <em>Neuhaus</em> in the given bounding box (copy it by hand, the markup parser breaks it):</p>
<pre><code>http://overpass.osm.rambler.ru/cgi/interpreter?data=[out:json];node[&quot;addr:street&quot;=&quot;Neuhaus&quot;](50.67,10.91,50.70,10.94);out;</code></pre>
<p>You should then repeat the query, but this time with <em>way</em> instead of <em>node</em> to get all available addresses. Afterwards just parse the outputs and search for the lowest and highest <em>addr:housenumber</em> to get your range. Of course this is only the address range in OSM's database.</p>
<p>If you don't know the bounding box of your way you can also ask the Overpass API or Nominatim for the location and calculate it yourself, or specify the city instead of the bounding box.</p>
<p>There might be other solutions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Nov '12, 15:07</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Nov '12, 15:08</strong> </span></p>
</div>
</div>
<div id="comments-container-17867" class="comments-container">
&#10;</div>
<div id="comment-tools-17867" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17867-form-container" class="comment-form-container">
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

