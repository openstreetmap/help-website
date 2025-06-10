+++
type = "question"
title = "Embed Nominatim Map and search bar on other website"
description = '''Hello, I managed to get my own Nominatim Server running. I also activated the website and I now see there a nice big map, a search bar / box and results that are displayed nicely.  I have another website and I would like to embed the above elements with workin functionality in it, is it possible and...'''
date = "2016-08-17T14:37:00Z"
lastmod = "2016-08-17T15:38:00Z"
weight = 51497
keywords = [ "html", "nominatim" ]
aliases = [ "/questions/51497" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Embed Nominatim Map and search bar on other website](/questions/51497/embed-nominatim-map-and-search-bar-on-other-website)

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
<span id="post-51497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51497-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I managed to get my own Nominatim Server running. I also activated the website and I now see there a nice big map, a search bar / box and results that are displayed nicely.</p>
<p>I have another website and I would like to embed the above elements with workin functionality in it, is it possible and if yes, how would I do that?</p>
<p>Thank your for your time and help, yours truly, Stephano</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-html" rel="tag" title="see questions tagged &#39;html&#39;">html</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Aug '16, 14:37</strong></p>
<img src="https://secure.gravatar.com/avatar/4aeaae6ed1cbb7581b9338affb59e4d2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stephano007&#39;s gravatar image" />
<p><span>Stephano007</span><br />
<span class="score" title="61 reputation points">61</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stephano007 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51497" class="comments-container">
&#10;</div>
<div id="comment-tools-51497" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51497-form-container" class="comment-form-container">
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

<span id="51498"></span>

<div id="answer-container-51498" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51498-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51498-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51498-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To create a map look at the tutorials on <a href="http://leafletjs.com/">http://leafletjs.com/</a></p>
<p>There is a plugin for leaflet <a href="https://github.com/perliedman/leaflet-control-geocoder">https://github.com/perliedman/leaflet-control-geocoder</a> that adds a searchbox. In the L.Control.Geocoder.Nominatim(options) option you can set the serviceUrl to point to your server URL.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '16, 15:38</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-51498" class="comments-container">
&#10;</div>
<div id="comment-tools-51498" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51498-form-container" class="comment-form-container">
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

