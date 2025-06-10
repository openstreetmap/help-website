+++
type = "question"
title = "Filtering planet for just placename geocoding"
description = '''I would like to start with the planet database, and then filter it to use for only administrative and geographic placename geocoding to lat-long (using nominatim). I don&#x27;t care about roads, POI&#x27;s, etc. I want to reduce the import time and storage requirements. I first tried this in a straightforward...'''
date = "2013-10-23T18:28:00Z"
lastmod = "2013-10-26T12:07:00Z"
weight = 27449
keywords = [ "filter", "placenames", "geocoding", "features" ]
aliases = [ "/questions/27449" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Filtering planet for just placename geocoding](/questions/27449/filtering-planet-for-just-placename-geocoding)

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
<span id="post-27449-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27449-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-27449-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to start with the planet database, and then filter it to use for only administrative and geographic placename geocoding to lat-long (using nominatim). I don't care about roads, POI's, etc. I want to reduce the import time and storage requirements.</p>
<p>I first tried this in a straightforward way: I started with the whole planet db (22GB) and then removed all relations and ways so I was only left with nodes (15GB). I further filtered the nodes to places and some geographic features (down to 117MB). The import took less than overnight.</p>
<p>However, this filtering does not work so well, because some containment relationships are specified by <em>boundary=administrative</em>. Since boundaries are ways, I lost those by removing all ways. For instance, I lost the state boundaries, and so some US cities came back with lookup results like <em>City, County, USA</em>, instead of <em>City, County, State, USA</em>.</p>
<p>I'll put back the administrative boundaries. But I would very much appreciate any further advice about what to remove and what not to remove so as not to lose too much information but still reduce the database size significantly.</p>
<p><strong>FOLLOWUP:</strong> For my purposes, removing buildings and roads was fine. The input data does not mention roads, so they could be safely removed. I used <code>osmfilter</code>:</p>
<pre><code> osmfilter --keep=&quot;name= and ( mountain_pass= or natural= or place= or waterway= or boundary=administrative or boundary=national_park or boundary=protected_area )&quot;</code></pre>
<p>I reduced the planet pbf from 22GB to 1.6GB using the above filtering. Doing <code>--drop-author</code> reduces it further to 1.4GB.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-placenames" rel="tag" title="see questions tagged &#39;placenames&#39;">placenames</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-features" rel="tag" title="see questions tagged &#39;features&#39;">features</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Oct '13, 18:28</strong></p>
<img src="https://secure.gravatar.com/avatar/507c65170b1d6d484cf28f1a4db5ecb6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dhalbert&#39;s gravatar image" />
<p><span>dhalbert</span><br />
<span class="score" title="61 reputation points">61</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dhalbert has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Oct '13, 20:25</strong> </span></p>
</div>
</div>
<div id="comments-container-27449" class="comments-container">
&#10;</div>
<div id="comment-tools-27449" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27449-form-container" class="comment-form-container">
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

<span id="27507"></span>

<div id="answer-container-27507" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27507-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27507-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-27507-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="dhalbert has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Removing ways which only have either a building tag, a building tag and a source tag or a building tag, source tag and wall tag will <strong>significantly</strong> reduce the file size. On the other hand, nominatim might do this already. You'd also want to remove their nodes if you're not planning to use updates.</p>
<p>You can't always remove roads because some geocoders rely on them.</p>
<p>From a file size perspective, the planet is largely buildings, roads and the nodes used for them. natural/landuse are the only other tags that spring to mind, but you don't want to removed any named landuse.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Oct '13, 12:07</strong></p>
<img src="https://secure.gravatar.com/avatar/5634c46072077e10f5b7c0da9b4bbb62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pnorman&#39;s gravatar image" />
<p><span>pnorman</span><br />
<span class="score" title="2352 reputation points"><span>2.4k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pnorman has 9 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Oct '13, 21:18</strong> </span></p>
</div>
</div>
<div id="comments-container-27507" class="comments-container">
&#10;</div>
<div id="comment-tools-27507" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27507-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="27465"></span>

<div id="answer-container-27465" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27465-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27465-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-27465-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think you are potentially underestimating the complexity of what you want to do. Nominatim employs a lot of logic to try to get it right using the whole database, has to use heuristics in some circumstances and still doesn't "always" get it right.</p>
<p>Probably the best approach would be to just remove data where you can be fairly sure that it will have no consequences for your application, for example just revmoving building outlines that have no interesting tags and are not member of a relation should already result in a noticeable size reduction.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Oct '13, 10:42</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-27465" class="comments-container">
&#10;</div>
<div id="comment-tools-27465" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27465-form-container" class="comment-form-container">
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

