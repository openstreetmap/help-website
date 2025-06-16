+++
type = "question"
title = "How can I request the API marked IATA?"
description = '''Moved from https://help.openstreetmap.org/questions/1989/load-data-from-sqlserver-and-display-markers-on-map: Hello! How can I request the API marked IATA? I need a base: Airport name in Russian, English , IATA- Code . Can I help with your service obtain the necessary information ?'''
date = "2016-03-22T10:54:00Z"
lastmod = "2016-03-25T11:34:00Z"
weight = 48771
keywords = [ "iata", "api" ]
aliases = [ "/questions/48771" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I request the API marked IATA?](/questions/48771/how-can-i-request-the-api-marked-iata)

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
<span id="post-48771-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48771-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48771-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Moved from <a href="/questions/1989/load-data-from-sqlserver-and-display-markers-on-map">https://help.openstreetmap.org/questions/1989/load-data-from-sqlserver-and-display-markers-on-map</a>:</p>
<p>Hello! How can I request the API marked IATA? I need a base: Airport name in Russian, English , IATA- Code . Can I help with your service obtain the necessary information ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-iata" rel="tag" title="see questions tagged &#39;iata&#39;">iata</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Mar '16, 10:54</strong></p>
<img src="https://secure.gravatar.com/avatar/4f89c11382c3a9132a62fbc7d10de0cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Evgeniya_VN&#39;s gravatar image" />
<p><span>Evgeniya_VN</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Evgeniya_VN has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> converted to question <strong>22 Mar '16, 16:44</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span></p>
</div>
</div>
<div id="comments-container-48771" class="comments-container">
&#10;</div>
<div id="comment-tools-48771" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48771-form-container" class="comment-form-container">
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

<span id="48781"></span>

<div id="answer-container-48781" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48781-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48781-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-48781-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Overpass API is one way to retrieve such data. Overpass Turbo is a nice front end for working out a query, here I've used the Overpass Turbo Wizard to find all the airports inside the current map view:</p>
<p><a href="http://overpass-turbo.eu/s/fbO">http://overpass-turbo.eu/s/fbO</a></p>
<p>And then here I've used the wizard again, this time further limiting the results to airports with an iata tag:</p>
<p><a href="http://overpass-turbo.eu/s/fbP">http://overpass-turbo.eu/s/fbP</a></p>
<p>Whether you get Russian and English names will of course depend on what is present in the data. Here I've edited the second query to output a delimited file with just the chosen tags:</p>
<p><a href="http://overpass-turbo.eu/s/fbQ">http://overpass-turbo.eu/s/fbQ</a></p>
<p>Consult the documentation to see about changing the area that results are pulled from:</p>
<p>wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL</p>
<p>There can also be no bounding box, a global bounding box, or there is support for selecting an area from the OSM database and restricting the results to be inside that area. Queries that need a lot of resources may time out, restricting the are of the query helps avoid this.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Mar '16, 19:31</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Mar '16, 19:39</strong> </span></p>
</div>
</div>
<div id="comments-container-48781" class="comments-container">
<span id="48847"></span>
<div id="comment-48847" class="comment">
<div id="post-48847-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>For the last query (CSV output), I'd recommend to replace <code>out;</code> by <code>out center;</code>, otherwise there will be no lat/lon values for ways and relations in the response.</p>
</div>
<div id="comment-48847-info" class="comment-info">
<span class="comment-age">(25 Mar '16, 11:34)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-48781" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48781-form-container" class="comment-form-container">
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

