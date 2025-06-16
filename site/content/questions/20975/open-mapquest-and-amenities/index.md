+++
type = "question"
title = "Open mapquest and amenities"
description = '''Background: I have been adding some local businesses to OSM using, I hope, appropriate properties. In doing so, I have sometimes added the building outlines as well. The building outlines and business names are showing up on http://open.mapquest.com/ but the amenity search (bank, atm, restaurant, et...'''
date = "2013-03-25T23:16:00Z"
lastmod = "2013-03-26T16:13:00Z"
weight = 20975
keywords = [ "mapquest", "amenity" ]
aliases = [ "/questions/20975" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Open mapquest and amenities](/questions/20975/open-mapquest-and-amenities)

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
<span id="post-20975-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20975-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-20975-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Background:</p>
<p>I have been adding some local businesses to OSM using, I hope, appropriate properties. In doing so, I have sometimes added the building outlines as well.</p>
<p>The building outlines and business names are showing up on <a href="http://open.mapquest.com/">http://open.mapquest.com/</a> but the amenity search (bank, atm, restaurant, etc.) does not find the new additions. Frustrating, for example, to have a map showing a building clearly labeled with a bank name but have the bank search function say there are no banks in the view.</p>
<p>I have double checked the properties I have for the nodes and ways (buildings) I've added against previously existing ones near by (found by the search function) and against the usage description at <a href="https://wiki.openstreetmap.org/wiki/Key:amenity">https://wiki.openstreetmap.org/wiki/Key:amenity</a> and don't see what I might be doing wrong.</p>
<p>I realize that mapquest can do what they want when updating their presentation of the OSM data. And volunteers with OSM may not know exactly what mapquest does. But does anyone know for sure that the amenity data is used to update the category search at the same time as the tile data is updated?</p>
<p>If others have not noticed this with their edits, it would indicate I am not following appropriate tagging conventions. Limiting the discussion to banks, my recent changes have the building (way) set with properties: amenity=bank atm=yes building=yes name=First Whatever Bank</p>
<p>I have been setting nodes on the building "way" in appropriate locations with the properties: amenity=atm operator=First Whatever Bank</p>
<p>I found that neither banks nor ATMs were showing up in the search, so in some cases I've gone back and added a node inside the building footprint with the following properties: amenity=bank atm=yes name=First Whatever Bank</p>
<p>That seems to work sometimes but not always for banks. But at all for other amenities. Am I wrong in thinking that having a building marked as a bank (or whatever) should be sufficient? Does it need an independent node inside the way with duplicate information?</p>
<p>In summary, a few questions: 1. Am I adding the properties appropriately? I've looked through lots of posts and read the wiki on this and it seems best practices may have changed over time but I thought I was using the current best practice.</p>
<ol>
<li><p>Does open mapquest actually use the property data from OSM when setting up their search database?</p></li>
<li><p>Does open mapquest update their search data at the same time as they update their tiles? Maybe I am not waiting long enough to test things...</p></li>
</ol>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapquest" rel="tag" title="see questions tagged &#39;mapquest&#39;">mapquest</span> <span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Mar '13, 23:16</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-20975" class="comments-container">
<span id="20976"></span>
<div id="comment-20976" class="comment">
<div id="post-20976-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Would it be possible to provide a link to an example area in which there are things that don't show up?</p>
</div>
<div id="comment-20976-info" class="comment-info">
<span class="comment-age">(25 Mar '13, 23:33)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="20977"></span>
<div id="comment-20977" class="comment">
<div id="post-20977-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Area is shown at <a href="https://www.openstreetmap.org/?lat=37.374419420957565&amp;lon=-122.0347112417221&amp;zoom=17">https://www.openstreetmap.org/?lat=37.374419420957565&amp;lon=-122.0347112417221&amp;zoom=17</a> and <a href="http://mapq.st/14qPhTr">http://mapq.st/14qPhTr</a></p>
</div>
<div id="comment-20977-info" class="comment-info">
<span class="comment-age">(25 Mar '13, 23:47)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="20999"></span>
<div id="comment-20999" class="comment">
<div id="post-20999-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Your specific mapquest questions can probably only be answered by mapquest support.</p>
<p>I cannot see why <a href="https://www.openstreetmap.org/browse/way/210312326">https://www.openstreetmap.org/browse/way/210312326</a> should behave differently than <a href="https://www.openstreetmap.org/browse/way/47286731">https://www.openstreetmap.org/browse/way/47286731</a> , one is found with your search, the other not. Only difference is the name.</p>
<p>I also found that some ATMs have <code>amenity=atm</code> and some <code>amenity=ATM</code> (differing in case), but as far as i saw that isn't the cause of the problems.</p>
</div>
<div id="comment-20999-info" class="comment-info">
<span class="comment-age">(26 Mar '13, 15:03)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
</div>
<div id="comment-tools-20975" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20975-form-container" class="comment-form-container">
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

<span id="21000"></span>

<div id="answer-container-21000" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21000-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21000-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21000-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To answer one of your questions: your tagging looks good!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Mar '13, 15:04</strong></p>
<img src="https://secure.gravatar.com/avatar/806d5a652505590a9eba797ad5bea8db?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gormo&#39;s gravatar image" />
<p><span>gormo</span><br />
<span class="score" title="2928 reputation points"><span>2.9k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gormo has 13 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-21000" class="comments-container">
<span id="21005"></span>
<div id="comment-21005" class="comment">
<div id="post-21005-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for that. I'll just continue on the with how I am doing tagging and hope that mapquest eventually gets it.</p>
</div>
<div id="comment-21005-info" class="comment-info">
<span class="comment-age">(26 Mar '13, 16:13)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
</div>
<div id="comment-tools-21000" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21000-form-container" class="comment-form-container">
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

