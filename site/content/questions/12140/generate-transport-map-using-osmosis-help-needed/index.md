+++
type = "question"
title = "Generate Transport Map using Osmosis - Help needed"
description = '''Hi My objective is to generate transport map for offline purpose; store the map in a mobile device and use it offline. The files will be saved in the mobile device as vector map (.map files) and can be viewed using AdvancedMapViewer. To do that, I have split the Planet OSM to smaller pieces using po...'''
date = "2012-04-18T15:52:00Z"
lastmod = "2012-04-25T08:33:00Z"
weight = 12140
keywords = [ "map", "offline", "transport", "generate", "osmosis" ]
aliases = [ "/questions/12140" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Generate Transport Map using Osmosis - Help needed](/questions/12140/generate-transport-map-using-osmosis-help-needed)

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
<span id="post-12140-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12140-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12140-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>My objective is to generate transport map for offline purpose; store the map in a mobile device and use it offline. The files will be saved in the mobile device as vector map (.map files) and can be viewed using AdvancedMapViewer. To do that, I have split the Planet OSM to smaller pieces using poly files... like country &amp; states. Using Osmosis, I tried generating transport map for smaller regions like states using the tags defined in wiki. But the final vector map when viewed has white screen [:(] and few tags in it. Without the tags mentioned in wiki, the vector map generated has all the details.</p>
<p>Is there an example available on how to generate transport map?</p>
<p>thank you in advance.</p>
<p>Kris</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span> <span class="post-tag tag-link-transport" rel="tag" title="see questions tagged &#39;transport&#39;">transport</span> <span class="post-tag tag-link-generate" rel="tag" title="see questions tagged &#39;generate&#39;">generate</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Apr '12, 15:52</strong></p>
<img src="https://secure.gravatar.com/avatar/382f63907e37a769341f345c01d8e8df?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kris&#39;s gravatar image" />
<p><span>kris</span><br />
<span class="score" title="46 reputation points">46</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kris has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12140" class="comments-container">
&#10;</div>
<div id="comment-tools-12140" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12140-form-container" class="comment-form-container">
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

<span id="12156"></span>

<div id="answer-container-12156" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12156-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12156-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-12156-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Somebody else may be able to suggest a better overall approach, but here's a couple of pointers for you:</p>
<p>You mention creating a .map file for AdvancedMapViewer, so I presume you're using the mapsforge and osmosis <a href="http://code.google.com/p/mapsforge/wiki/GettingStartedMapWriter">map writer plugin</a>. Don't know much about that myself, but I guess my first suggestion would be to take this out of the picture until you know you've got the data you want. Instead work with a small patch of data (e.g. just one city, perhaps using the <a href="http://metro.teczno.com/">metro extracts download service</a>) Try to filter by tags using osmosis, and write to an .osm file. Then use <a href="https://wiki.openstreetmap.org/wiki/JOSM">JOSM</a> to open this file and see if it worked (Note: JOSM will struggle if you try to open a very large amount of data)</p>
<p>As for the actual tag filtering, are you using the <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage#--tag-filter_.28--tf.29">--tag-filter option of Osmosis</a>? Scroll down in that doc section to see some examples. This talks about motorway tags, so just swap in some railway / bus tags. You may find this is a bit limited or longwinded to work with e.g. if wanted to include a large number of specific tags.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Apr '12, 04:14</strong></p>
<img src="https://secure.gravatar.com/avatar/9e04333be840d50c6aa66fb112aad77c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harry%20Wood&#39;s gravatar image" />
<p><span>Harry Wood</span><br />
<span class="score" title="9489 reputation points"><span>9.5k</span></span><span title="25 badges"><span class="badge1">●</span><span class="badgecount">25</span></span><span title="88 badges"><span class="silver">●</span><span class="badgecount">88</span></span><span title="128 badges"><span class="bronze">●</span><span class="badgecount">128</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harry Wood has 19 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-12156" class="comments-container">
<span id="12157"></span>
<div id="comment-12157" class="comment">
<div id="post-12157-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi Harry,</p>
<p>Im doing exactly the same as mentioned by you. I extracted a smaller area using osmosis plugin. Then I tried extracting only the transport map related tags using the --tag-filter option. I used the tags mentioned in the wiki section of OSM. But when I use those tags, Im unable to get a complete map (i.e. after converting it from OSM to .map using mapforge's mapswriter).</p>
<p>1) I will try the JOSM and see how it looks. 2) Are there any information available which has the tags for a default map? i.e. if I have planet OSM data for a smaller area, Im looking for bunch of tags which gives only street information.</p>
<p>thank you</p>
<p>Kris</p>
</div>
<div id="comment-12157-info" class="comment-info">
<span class="comment-age">(19 Apr '12, 05:04)</span> <span class="comment-user userinfo">kris</span>
</div>
</div>
<span id="12158"></span>
<div id="comment-12158" class="comment">
<div id="post-12158-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>kris, also have a look at <a href="https://wiki.openstreetmap.org/wiki/Osmfilter">https://wiki.openstreetmap.org/wiki/Osmfilter</a></p>
</div>
<div id="comment-12158-info" class="comment-info">
<span class="comment-age">(19 Apr '12, 06:47)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-12156" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12156-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="12345"></span>

<div id="answer-container-12345" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-12345-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-12345-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-12345-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I found the way to do. I used the Osmosis pipe commands to create 2 pipes (one for extracting highway data and another pipe for transport data for railways, tram and bus/public_transport etc..) and then merged the pipes along with the transport facilities extract (all done through osmosis). Then converted them to offline map files for different regions using mapfile-writer plugin. It works fine now.</p>
<p>thanks</p>
<p>Kris</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Apr '12, 08:33</strong></p>
<img src="https://secure.gravatar.com/avatar/382f63907e37a769341f345c01d8e8df?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kris&#39;s gravatar image" />
<p><span>kris</span><br />
<span class="score" title="46 reputation points">46</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kris has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-12345" class="comments-container">
&#10;</div>
<div id="comment-tools-12345" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-12345-form-container" class="comment-form-container">
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

