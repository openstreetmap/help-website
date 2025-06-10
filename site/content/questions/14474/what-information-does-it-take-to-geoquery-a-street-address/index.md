+++
type = "question"
title = "What information does it take to geoquery a street address"
description = '''What information would it take in the osm dataset to allow www.openstreetmap.org to geoquery an address? I downloaded a segment of the XML covering a large parts of Fremont, CA. USA via the HTTP API using a bounding box. I realized that there are not many house number included in the OSM file. Howev...'''
date = "2012-07-22T07:03:00Z"
lastmod = "2012-07-25T19:58:00Z"
weight = 14474
keywords = [ "nominatim", "geocoding" ]
aliases = [ "/questions/14474" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [What information does it take to geoquery a street address](/questions/14474/what-information-does-it-take-to-geoquery-a-street-address)

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
<span id="post-14474-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14474-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14474-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What information would it take in the osm dataset to allow www.openstreetmap.org to geoquery an address?</p>
<p>I downloaded a segment of the XML covering a large parts of Fremont, CA. USA via the HTTP API using a bounding box. I realized that there are not many house number included in the OSM file. However, openstreetmap.org map and also Mapquest is able to locate address where I used to live, even when no house on that street is labeled inside the XML. How is geocoding done in this case?</p>
<p>I also noticed that where I live right now in Taipei, Taiwan, no address is searchable. What would the OSM have to include to make an area geocode-able?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jul '12, 07:03</strong></p>
<img src="https://secure.gravatar.com/avatar/0e543123a2cc239ba3b6c45068663a5a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="huggie&#39;s gravatar image" />
<p><span>huggie</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="huggie has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jul '12, 11:15</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-14474" class="comments-container">
<span id="14480"></span>
<div id="comment-14480" class="comment">
<div id="post-14480-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please show us your query which you expect to fail but does succeed instead.</p>
</div>
<div id="comment-14480-info" class="comment-info">
<span class="comment-age">(22 Jul '12, 13:46)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="14577"></span>
<div id="comment-14577" class="comment">
<div id="post-14577-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well basically almost all street addresses in Fremont, because I close to finding nothing.</p>
</div>
<div id="comment-14577-info" class="comment-info">
<span class="comment-age">(25 Jul '12, 17:02)</span> <span class="comment-user userinfo">huggie</span>
</div>
</div>
<span id="14579"></span>
<div id="comment-14579" class="comment">
<div id="post-14579-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Nominatim can find <a href="http://www.openstreetmap.org/browse/node/1013810433">the one place that I know in Fremont</a> without problems. Searches of the form "streetname, fremont" also work, but as stephan75 has said, without extra addressing data there's no way to do better than that.</p>
<p>To add more info, have a look <a href="http://wiki.openstreetmap.org/wiki/Address">here</a>, <a href="http://wiki.openstreetmap.org/wiki/Addresses">here</a> and <a href="http://wiki.openstreetmap.org/wiki/Proposed_features/House_numbers/Karlsruhe_Schema#Tags">here</a> - but don't underestimate the work involved.</p>
</div>
<div id="comment-14579-info" class="comment-info">
<span class="comment-age">(25 Jul '12, 17:13)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-14474" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14474-form-container" class="comment-form-container">
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

<span id="14484"></span>

<div id="answer-container-14484" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14484-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14484-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-14484-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="huggie has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim, the OSM search engine, uses the TIGER data in the US to augment the OSM address data (see also <a href="http://help.openstreetmap.org/questions/12150/missing-house-numbers-in-local-nominatim-instance">this question</a>). If similar datasets exist in the public domain for other countries, there might be a way to use them for search as well.</p>
<p>But ultimately, the address search is best improved by mapping addresses in OSM.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jul '12, 20:25</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-14484" class="comments-container">
<span id="14543"></span>
<div id="comment-14543" class="comment">
<div id="post-14543-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... with the help of <a href="http://wiki.openstreetmap.org/wiki/Key:addr">http://wiki.openstreetmap.org/wiki/Key:addr</a> on each object.</p>
</div>
<div id="comment-14543-info" class="comment-info">
<span class="comment-age">(24 Jul '12, 16:23)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="14576"></span>
<div id="comment-14576" class="comment">
<div id="post-14576-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>And this addr tag is suppose to apply to nodes?</p>
</div>
<div id="comment-14576-info" class="comment-info">
<span class="comment-age">(25 Jul '12, 17:01)</span> <span class="comment-user userinfo">huggie</span>
</div>
</div>
<span id="14592"></span>
<div id="comment-14592" class="comment">
<div id="post-14592-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You can add this tag to nodes or to buildings that are a polygon / little area as well.</p>
</div>
<div id="comment-14592-info" class="comment-info">
<span class="comment-age">(25 Jul '12, 19:58)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-14484" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14484-form-container" class="comment-form-container">
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

