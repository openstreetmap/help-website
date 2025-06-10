+++
type = "question"
title = "Looking for some tag - icon mapping"
description = '''Hello, I am adding a new feature to our online map, which would show OSM POIs as vectors and subsequently allow users to contribute new POIs. What I can&#x27;t really find is some iconset, which could be usable for selecting the right icon according to node&#x27;s properties. Something like mapping from &#x27;amen...'''
date = "2017-07-31T11:02:00Z"
lastmod = "2017-07-31T13:23:00Z"
weight = 57366
keywords = [ "icon", "renderer", "mapping", "tags" ]
aliases = [ "/questions/57366" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Looking for some tag - icon mapping](/questions/57366/looking-for-some-tag-icon-mapping)

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
<span id="post-57366-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57366-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57366-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I am adding a new feature to our online map, which would show OSM POIs as vectors and subsequently allow users to contribute new POIs. What I can't really find is some iconset, which could be usable for selecting the right icon according to node's properties. Something like mapping from 'amenity=restaurant' to /iconset/amenity/restaurant.svg. All I've found was incomplete and there was no mapping, or it was outdated (for example restaurant was under food, but now OSM chooses amenity, when I edit with id).</p>
<p>I know that it's upon every renderer, what icons it would use, but do I really have to create my own iconset and mapping from scratch? Isn't there at least some iconset to start with?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-icon" rel="tag" title="see questions tagged &#39;icon&#39;">icon</span> <span class="post-tag tag-link-renderer" rel="tag" title="see questions tagged &#39;renderer&#39;">renderer</span> <span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Jul '17, 11:02</strong></p>
<img src="https://secure.gravatar.com/avatar/a65aba25dacb2bea52f33610c698931d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="meehocz&#39;s gravatar image" />
<p><span>meehocz</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="meehocz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-57366" class="comments-container">
&#10;</div>
<div id="comment-tools-57366" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57366-form-container" class="comment-form-container">
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

<span id="57371"></span>

<div id="answer-container-57371" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57371-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57371-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-57371-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="meehocz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Any of the more popular preset systems provide tag combination -&gt; icon mappings in one way or another:</p>
<ul>
<li>iD <a href="https://github.com/openstreetmap/iD/tree/master/data/presets">https://github.com/openstreetmap/iD/tree/master/data/presets</a></li>
<li>JOSM format: <a href="https://josm.openstreetmap.de/wiki/Presets">https://josm.openstreetmap.de/wiki/Presets</a> <a href="https://josm.openstreetmap.de/browser/josm/trunk/data/defaultpresets.xml">https://josm.openstreetmap.de/browser/josm/trunk/data/defaultpresets.xml</a> and <a href="https://github.com/simonpoole/beautified-JOSM-preset">https://github.com/simonpoole/beautified-JOSM-preset</a></li>
</ul>
<p>Further the map styles have similar rules (but tend to less complete as they need to reduce the amount of information they display to be practical).</p>
<p>In general, before embarking on a larger coding exercise, I would recommend getting acquainted with how OSM tagging works and in general with the data model and the pitfalls you are likely to run in to when creating your application.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jul '17, 13:23</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Jul '17, 14:14</strong> </span></p>
</div>
</div>
<div id="comments-container-57371" class="comments-container">
&#10;</div>
<div id="comment-tools-57371" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57371-form-container" class="comment-form-container">
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

