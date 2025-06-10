+++
type = "question"
title = "All postal codes around a specific postal code"
description = '''Hey there! I was trying to figure out if it would be possible to get all postal codes within a specific radius around a given postal_code. For Bonn I tried: http://overpass-api.de/api/interpreter?data=[out:json];area(around:10000)[postal_code=&quot;53111&quot;]-&amp;gt;.a;node(area.a)[&quot;addr:postcode&quot;][&quot;addr:postc...'''
date = "2014-08-14T09:42:00Z"
lastmod = "2022-01-05T08:16:00Z"
weight = 35813
keywords = [ "overpass", "postal_code", "around", "area" ]
aliases = [ "/questions/35813" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [All postal codes around a specific postal code](/questions/35813/all-postal-codes-around-a-specific-postal-code)

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
<span id="post-35813-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35813-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35813-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey there! I was trying to figure out if it would be possible to get all postal codes within a specific radius around a given postal_code. For Bonn I tried:</p>
<p><a href="http://overpass-api.de/api/interpreter?data=%5Bout:json%5D;area(around:10000)%5Bpostal_code=">http://overpass-api.de/api/interpreter?data=[out:json];area(around:10000)[postal_code="53111"]-&gt;.a;node(area.a)["addr:postcode"]["addr:postcode"!="53111"];out;</a></p>
<p>..but gives me no results. Does around work with area?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-postal_code" rel="tag" title="see questions tagged &#39;postal_code&#39;">postal_code</span> <span class="post-tag tag-link-around" rel="tag" title="see questions tagged &#39;around&#39;">around</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Aug '14, 09:42</strong></p>
<img src="https://secure.gravatar.com/avatar/55881ed1d4529d5730abaeed106a58c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Korbi&#39;s gravatar image" />
<p><span>Korbi</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Korbi has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Aug '14, 06:18</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span></p>
</div>
</div>
<div id="comments-container-35813" class="comments-container">
&#10;</div>
<div id="comment-tools-35813" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35813-form-container" class="comment-form-container">
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

<span id="35856"></span>

<div id="answer-container-35856" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35856-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35856-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-35856-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>From looking at the code I would say that <em>around</em> is indeed not yet implemented for areas. You might want to raise an issue for this on <a href="https://github.com/drolbr/Overpass-API">github</a>. However, you could as well use the corresponding relation and run <em>around</em> on the relation instead:</p>
<pre><code>area[boundary=postal_code][postal_code=&quot;53111&quot;];rel(pivot);(rel(around:10000)[boundary=postal_code][postal_code][postal_code!=&quot;53111&quot;];&gt;;);out;</code></pre>
<p>Try it on <a href="http://overpass-turbo.eu/s/4Az">overpass turbo</a></p>
<p>In fact, you can skip the area part altogether and start with the relation for a simpler approach:</p>
<pre><code>rel[boundary=postal_code][postal_code=&quot;53111&quot;];(rel(around:10000)[boundary=postal_code][postal_code][postal_code!=&quot;53111&quot;];&gt;;);out;</code></pre>
<p>Try it on <a href="http://overpass-turbo.eu/s/4AA">overpass turbo</a></p>
<p>BTW: In your overpass api query you seem to check for nodes with "addr:postcode". This doesn't exactly match your question where you wanted to find postal codes within a given radius around a specific postal code. Maybe you want to rephrase your question a bit to clarify what you are looking for.</p>
<p>A slightly modified version of the last query will return all relevant relations. In a post-processing step, you'll have to extract the postal code from the relations to get a list of postal codes:</p>
<pre><code>rel[boundary=postal_code][postal_code=&quot;53111&quot;];rel(around:10000)[boundary=postal_code][postal_code][postal_code!=&quot;53111&quot;];out;</code></pre>
<p>Try it on <a href="http://overpass-turbo.eu/s/4AH">overpass turbo</a> (you can ignore the warning message when executing the query)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Aug '14, 06:21</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Aug '14, 09:28</strong> </span></p>
</div>
</div>
<div id="comments-container-35856" class="comments-container">
<span id="35858"></span>
<div id="comment-35858" class="comment">
<div id="post-35858-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well I was actually looking for an opportunity to get all postal codes within a specific radius. Let's say, I do have Bonn's postal code and would like to get all postal codes within a radius of 10.000m calculated from Bonn's postal code area (or its center). I'm not very much interested in all border nodes, streets etc, I just would like to get the postal codes within the given radius. Does this clarify my problem?</p>
<p>EDIT: I think I'm gettin closer now: rel[boundary=postal_code][postal_code="53111"]-&gt;.a;(rel(around.a:10000)[boundary=postal_code][postal_code][postal_code!="53111"][postal_code_level][type="boundary"];);out;</p>
</div>
<div id="comment-35858-info" class="comment-info">
<span class="comment-age">(15 Aug '14, 09:21)</span> <span class="comment-user userinfo">Korbi</span>
</div>
</div>
<span id="35860"></span>
<div id="comment-35860" class="comment">
<div id="post-35860-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Ok, I've updated my reply. Note that you'll have to do some kind of post processing on the result to extract a list of postal codes from the list of relations. However, this should be straightforward.</p>
</div>
<div id="comment-35860-info" class="comment-info">
<span class="comment-age">(15 Aug '14, 09:29)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="35861"></span>
<div id="comment-35861" class="comment">
<div id="post-35861-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your help, it seems our answers just crossed ;)</p>
</div>
<div id="comment-35861-info" class="comment-info">
<span class="comment-age">(15 Aug '14, 09:38)</span> <span class="comment-user userinfo">Korbi</span>
</div>
</div>
</div>
<div id="comment-tools-35856" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35856-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82948"></span>

<div id="answer-container-82948" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82948-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82948-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82948-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello, I have exactly the same need and the query suits me perfectly :</p>
<pre><code>rel[boundary=postal_code][postal_code=&quot;53111&quot;];rel(around:10000)[boundary=postal_code][postal_code][postal_code!=&quot;53111&quot;];out;</code></pre>
<p>I just want to specify the country of the postal code in my query. Can you help me!</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jan '22, 08:16</strong></p>
<img src="https://secure.gravatar.com/avatar/5a81d949fb53d2b4e9e63e1c81b13aa4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AYADI&#39;s gravatar image" />
<p><span>AYADI</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AYADI has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jan '22, 08:17</strong> </span></p>
</div>
</div>
<div id="comments-container-82948" class="comments-container">
&#10;</div>
<div id="comment-tools-82948" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82948-form-container" class="comment-form-container">
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

