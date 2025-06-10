+++
type = "question"
title = "How to get lat long of address from osm file?"
description = '''Context: I&#x27;ve already stumbled apon nominatim although I can&#x27;t use the public version for production and I&#x27;m not sure how to maintain a local install effectively.  Edit: For further context I need to be able to make updates to some geocoding data (doesn&#x27;t have to be osm) have those updates go live w...'''
date = "2022-09-14T15:43:00Z"
lastmod = "2022-09-14T16:10:00Z"
weight = 85625
keywords = [ "openstreetmap", "osm", "reversegeocoding", "geocoding", "nominatim" ]
aliases = [ "/questions/85625" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get lat long of address from osm file?](/questions/85625/how-to-get-lat-long-of-address-from-osm-file)

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
<span id="post-85625-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85625-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85625-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><strong>Context:</strong> I've already stumbled apon nominatim although I can't use the public version for production and I'm not sure how to maintain a local install effectively.</p>
<p>Edit: For further context I need to be able to make updates to some geocoding data (doesn't have to be osm) have those updates go live withing 5-15min (preferably as little time as possible) and have an api that I can call as much as I want. Nominatim's public api has restrictions on the number/frequency of calls which wont work for me. Same will apply to any other api. Currently my setup is I have an instance of OSRM running on a ec2 server. Thanks to user SimonPoole on another question I figured out how to set up automated updates for the routing service using osmupdate. But OSRM takes lat long and gives a route, I basically need be able to get lat long of a specific street addresses.</p>
<p><strong>Question:</strong> I want to be able to have some sort of api / qt plugin that I can pass a street address and get a lat long back, your suggestions would be appreciated?</p>
<p>Edit: Shortly after posting this question I did find a qt osm plugin that uses Nominatim, if anyone with experience using the plugin could tell me how reliable it is? That would be appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Sep '22, 15:43</strong></p>
<img src="https://secure.gravatar.com/avatar/1a5c982dc8825ee7594f38a8876576b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeorgeValleyeats&#39;s gravatar image" />
<p><span>GeorgeValley...</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeorgeValleyeats has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Sep '22, 16:35</strong> </span></p>
</div>
</div>
<div id="comments-container-85625" class="comments-container">
&#10;</div>
<div id="comment-tools-85625" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85625-form-container" class="comment-form-container">
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

<span id="85626"></span>

<div id="answer-container-85626" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85626-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85626-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85626-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Is your requirement to search a OSM file you created yourself and you have on hour harddrive? Or search all of (planet, region or country) OSM data?</p>
<p>Search for 'geocoding API' or 'geocoding $your-programing-language-or-framework'.</p>
<p><a href="https://operations.osmfoundation.org/policies/nominatim/">https://operations.osmfoundation.org/policies/nominatim/</a> has a section on 'Alternatives / Third-party providers'. More listed on <a href="https://wiki.openstreetmap.org/wiki/Search_engines">https://wiki.openstreetmap.org/wiki/Search_engines</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Sep '22, 15:51</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-85626" class="comments-container">
<span id="85627"></span>
<div id="comment-85627" class="comment">
<div id="post-85627-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I need to be able to make updates to some geocoding data (doesn't have to be osm) have those updates go live withing 5-15min and have an api / plugin that I can call as much as I want. Nominatim's public api has restrictions on the number/frequency of calls which wont work for me. Same will apply to any other api. I'll add an edit to my questions context to elaborate further.</p>
</div>
<div id="comment-85627-info" class="comment-info">
<span class="comment-age">(14 Sep '22, 16:10)</span> <span class="comment-user userinfo">GeorgeValley...</span>
</div>
</div>
</div>
<div id="comment-tools-85626" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85626-form-container" class="comment-form-container">
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

