+++
type = "question"
title = "How can I get Zip Codes that map to corresponding latitude and longitude?"
description = '''I have the .xml data with all of the latitude and longitude points from the nodes for California, but I need corresponding zip codes as well. Anyone able to point me in the direction of a simple way to get these through OSM? Thanks. '''
date = "2014-06-12T19:22:00Z"
lastmod = "2014-06-13T07:15:00Z"
weight = 33924
keywords = [ "latitude", "zipcodes", "longitude" ]
aliases = [ "/questions/33924" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can I get Zip Codes that map to corresponding latitude and longitude?](/questions/33924/how-can-i-get-zip-codes-that-map-to-corresponding-latitude-and-longitude)

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
<span id="post-33924-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33924-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33924-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have the .xml data with all of the latitude and longitude points from the nodes for California, but I need corresponding zip codes as well. Anyone able to point me in the direction of a simple way to get these through OSM? Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-latitude" rel="tag" title="see questions tagged &#39;latitude&#39;">latitude</span> <span class="post-tag tag-link-zipcodes" rel="tag" title="see questions tagged &#39;zipcodes&#39;">zipcodes</span> <span class="post-tag tag-link-longitude" rel="tag" title="see questions tagged &#39;longitude&#39;">longitude</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jun '14, 19:22</strong></p>
<img src="https://secure.gravatar.com/avatar/b114d64c259e517c767ab8288222f6b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ah2oman&#39;s gravatar image" />
<p><span>ah2oman</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ah2oman has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33924" class="comments-container">
<span id="33928"></span>
<div id="comment-33928" class="comment">
<div id="post-33928-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Can you provide a rough estimate on the number of nodes? If we're talking about, say 1000 nodes, I wouldn't have an issue recommending Reverse Geocoding provided by Nominatim. If that's more like a million, I'd be more than reluctant to recommend that though, unless you set up your own infrastructure for that purpose.</p>
</div>
<div id="comment-33928-info" class="comment-info">
<span class="comment-age">(12 Jun '14, 20:34)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="33932"></span>
<div id="comment-33932" class="comment">
<div id="post-33932-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Unfortunately its going to be expanded to the US, so we're talking millions...thank you though for your response!</p>
</div>
<div id="comment-33932-info" class="comment-info">
<span class="comment-age">(12 Jun '14, 22:28)</span> <span class="comment-user userinfo">ah2oman</span>
</div>
</div>
<span id="33941"></span>
<div id="comment-33941" class="comment">
<div id="post-33941-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Then the only option is to <a href="https://wiki.openstreetmap.org/wiki/Nominatim/Installation">install a local Nominatim instance</a> and do the geocoding yourself. OSM doesn't have such a list but it can be generated using OSM data.</p>
<p>Maybe you can tell us your ultimate goal and we can try to find a better solution?</p>
</div>
<div id="comment-33941-info" class="comment-info">
<span class="comment-age">(13 Jun '14, 07:15)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-33924" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33924-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

