+++
type = "question"
title = "museum density, OSM , Wikipedia and European Union"
description = '''Dear all,  I have been trying to find how many museums are there (big and small) in a country . With 28 member countries/states that is a large number of countries to look at.  Using a search-engine and trying to figure out how many museums are there in a country, how many museums are near to each o...'''
date = "2016-12-07T18:46:00Z"
lastmod = "2016-12-08T05:40:00Z"
weight = 53310
keywords = [ "museums", "rendering", "wikipedia", "lists" ]
aliases = [ "/questions/53310" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [museum density, OSM , Wikipedia and European Union](/questions/53310/museum-density-osm-wikipedia-and-european-union)

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
<span id="post-53310-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53310-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-53310-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear all,</p>
<p>I have been trying to find how many museums are there (big and small) in a country . With 28 member countries/states that is a large number of countries to look at.</p>
<p>Using a search-engine and trying to figure out how many museums are there in a country, how many museums are near to each other, how many museums are large or small is a mammoth undertaking due to the nature of query and limitation of the medium itself.</p>
<p>Wikipedia is a little help as it does list museums of some cities but don't know how complete or in-complete the listing are (apart from those in red) -</p>
<p><a href="https://en.wikipedia.org/wiki/Category:Lists_of_museums_by_city">https://en.wikipedia.org/wiki/Category:Lists_of_museums_by_city</a></p>
<p>Now can OSM help me here by -</p>
<p>a. Providing a list of museums based within the European Union</p>
<p>b. Have difference between large and small museums (rendering)</p>
<p>c. It would be interesting if there are plans afoot to link wikipedia articles to Places of Interest (POI)</p>
<p>I know I'm asking quite a lot and perhaps each should be a separate question but still it would be nice if at least some idea of how could it be done would be known.</p>
<p>If this could be done for European Union then it could be done for other places as well.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-museums" rel="tag" title="see questions tagged &#39;museums&#39;">museums</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-wikipedia" rel="tag" title="see questions tagged &#39;wikipedia&#39;">wikipedia</span> <span class="post-tag tag-link-lists" rel="tag" title="see questions tagged &#39;lists&#39;">lists</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Dec '16, 18:46</strong></p>
<img src="https://secure.gravatar.com/avatar/ae02b958f33b24e42b2a34802d1b801c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shirish&#39;s gravatar image" />
<p><span>shirish</span><br />
<span class="score" title="10 reputation points">10</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shirish has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Dec '16, 18:48</strong> </span></p>
</div>
</div>
<div id="comments-container-53310" class="comments-container">
&#10;</div>
<div id="comment-tools-53310" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53310-form-container" class="comment-form-container">
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

<span id="53327"></span>

<div id="answer-container-53327" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53327-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53327-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53327-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>With <a href="http://overpass-turbo.eu/">Overpass</a>, you could retrieve a list of musea. So "a" would get a yes. Note that the European union might be to big to download in 1 go. You could also download the planet file and work from that.</p>
<p>Since musea can be mapped as a point, you then need to find the building to which it belongs to get it's size. However, some musea consists of multiple buildings or an area (e.g. open-air musea). I do not expect that the extend of the area is always mapped. So the answer to "b" would be no</p>
<p>OSM does not have "projects", so there is no project to add wikipedia tags to object. This does not mean that no one is working on it, just that you cannot expect that all musea have a wikipedia tag by a given date. There is no formal plan, no formal deadline. That said, more and more people prefer a wikidata tag over a wikipedia tag. So people add those as well.</p>
<p>The best way to help out, is to start adding (manually, do no automate), wikipedia/wikidata tags to objects in your own neighborhood.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Dec '16, 04:57</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-53327" class="comments-container">
<span id="53329"></span>
<div id="comment-53329" class="comment">
<div id="post-53329-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The size problem is further complicated by the number of floors of the buildings and the actual area that is devoted to the exhibition.</p>
</div>
<div id="comment-53329-info" class="comment-info">
<span class="comment-age">(08 Dec '16, 05:40)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-53327" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53327-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53323"></span>

<div id="answer-container-53323" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53323-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Wow. This list would be very large and inexhaustible definitely. Just look at the Wikipedia one.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Dec '16, 23:31</strong></p>
<img src="https://secure.gravatar.com/avatar/100f8ccde5e9799707a5056f94fe183f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wetitpig0&#39;s gravatar image" />
<p><span>Wetitpig0</span><br />
<span class="score" title="307 reputation points">307</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wetitpig0 has 2 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-53323" class="comments-container">
&#10;</div>
<div id="comment-tools-53323" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53323-form-container" class="comment-form-container">
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

