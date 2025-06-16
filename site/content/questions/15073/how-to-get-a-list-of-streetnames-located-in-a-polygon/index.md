+++
type = "question"
title = "how to get a list of streetnames located in a polygon"
description = '''How would one implement the following functionality : a user draws a polygon on a map and receives as a result a list of streetnames (or addresses) which are located within the polygon.  Doesn&#x27;t matter which maps, api or scripting language. Any ideas?'''
date = "2012-08-14T14:41:00Z"
lastmod = "2012-08-15T11:43:00Z"
weight = 15073
keywords = [ "geocoding", "reverse" ]
aliases = [ "/questions/15073" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to get a list of streetnames located in a polygon](/questions/15073/how-to-get-a-list-of-streetnames-located-in-a-polygon)

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
<span id="post-15073-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15073-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15073-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How would one implement the following functionality : a user draws a polygon on a map and receives as a result a list of streetnames (or addresses) which are located within the polygon.</p>
<p>Doesn't matter which maps, api or scripting language. Any ideas?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-reverse" rel="tag" title="see questions tagged &#39;reverse&#39;">reverse</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Aug '12, 14:41</strong></p>
<img src="https://secure.gravatar.com/avatar/0605c7c14899a65be4ee3dc022cef244?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jvm985&#39;s gravatar image" />
<p><span>jvm985</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jvm985 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-15073" class="comments-container">
&#10;</div>
<div id="comment-tools-15073" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15073-form-container" class="comment-form-container">
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

<span id="15105"></span>

<div id="answer-container-15105" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15105-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15105-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-15105-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you are able to split the polygon into bounding boxes you can use multiple <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">OverpassAPI</a> queries.</p>
<p>This example query will list all ways with a highway and a way tag:</p>
<pre><code>http://overpass.osm.rambler.ru/cgi/interpreter?data=[out:json];way[highway][name]%2850.66%2C10.91%2C50.7%2C10.95%29%3Bout%3B</code></pre>
<p><del>(Note: the regular expression <em>name~'.'</em> is only required due to a recently introduced <a href="/questions/15101/overpassapi-query-with-two-specific-keys-and-any-value">bug</a> and can be simplified by just specifying <em>name</em> in the future).</del></p>
<p>You just have to parse this output and extract all <em>name</em> fields.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Aug '12, 08:36</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Aug '12, 11:56</strong> </span></p>
</div>
</div>
<div id="comments-container-15105" class="comments-container">
<span id="15109"></span>
<div id="comment-15109" class="comment">
<div id="post-15109-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The bug has been fixed.</p>
</div>
<div id="comment-15109-info" class="comment-info">
<span class="comment-age">(15 Aug '12, 11:43)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
</div>
<div id="comment-tools-15105" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15105-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="15081"></span>

<div id="answer-container-15081" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-15081-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-15081-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-15081-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First you need to determine what the inner surface of your closed way is (if the way is oriented, you can save this with "left" or "right").</p>
<p>You can do this by connecting an arbitrary point of your polygon with a special point that will never be included in the polygon (like the north pole, there are no streets there).</p>
<p>Now, if the drawn line intersects with your polygon, draw the line again from that intersection point, until it doesn't intersect any more. After that, you can check if the line is right or left from the polygon boundary.</p>
<p>After that, for each point in your dataset*, you draw a line from the point (the direction doesn't matter). If the line doesn't cut with the drawn polygon, it's not in it. If the line cuts, you can check wether the part between your node and the line is left or right from your polygon and thus check if it's in or out the polygon.</p>
<p>And as a last thing, get all the ways that have a node in the selection you've received.</p>
<p>*) you can filter your dataset a bit on beforehand by placing the polygon in a BBOX and filtering on that BBOX first.</p>
<p>This method requires you know how to calculate intersection points and how to check if a line segment is left or right of an other segment (in other words, calculate the corner between two segments).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Aug '12, 16:49</strong></p>
<img src="https://secure.gravatar.com/avatar/1fe9a0c696a5000fb304ababea9f83af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanderd17&#39;s gravatar image" />
<p><span>Sanderd17</span><br />
<span class="score" title="1111 reputation points"><span>1.1k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanderd17 has 15 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-15081" class="comments-container">
<span id="15087"></span>
<div id="comment-15087" class="comment">
<div id="post-15087-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks for your reply which is quite helpful.</p>
<p>The thing is that I don't have a dataset with coordinates. I want the script to return a set of streetnames that are (partly) enclosed. I could come up with a list of streetnames, but not simple coordinates.</p>
<p>Does that make sense?</p>
</div>
<div id="comment-15087-info" class="comment-info">
<span class="comment-age">(14 Aug '12, 18:12)</span> <span class="comment-user userinfo">jvm985</span>
</div>
</div>
<span id="15088"></span>
<div id="comment-15088" class="comment">
<div id="post-15088-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh, so you want to get it live from OSM?</p>
<p>That depends on how big the polygon is, and how often you do a query in the same area.</p>
<p>You can first calculate a BBOX (biggest and smallest lat-lon values), and get data from OSM in that BBOX. This would work if your polygon is small enough.</p>
<p>Otherwise, you will have to work with an offline database.</p>
</div>
<div id="comment-15088-info" class="comment-info">
<span class="comment-age">(14 Aug '12, 18:18)</span> <span class="comment-user userinfo">Sanderd17</span>
</div>
</div>
</div>
<div id="comment-tools-15081" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-15081-form-container" class="comment-form-container">
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

