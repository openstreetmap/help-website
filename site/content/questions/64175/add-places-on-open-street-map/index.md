+++
type = "question"
title = "Add places on Open Street Map"
description = '''I installed the Nominatim on an EC2 instance in AWS and importing the whole world. For me its use is similar to Facebook and Instagram in relation to the location of the posts. In my app a post has a location, so users can filter posts from a specific location. So far so good, now I need to let the ...'''
date = "2018-06-12T14:59:00Z"
lastmod = "2018-06-12T15:37:00Z"
weight = 64175
keywords = [ "search", "nominatim", "osm", "reverse" ]
aliases = [ "/questions/64175" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Add places on Open Street Map](/questions/64175/add-places-on-open-street-map)

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
<span id="post-64175-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64175-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64175-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I installed the <a href="http://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-16/">Nominatim</a> on an EC2 instance in AWS and importing the whole world.</p>
<p>For me its use is similar to Facebook and Instagram in relation to the location of the posts. In my app a post has a location, so users can filter posts from a specific location.</p>
<p>So far so good, now I need to let the user create places according to their need and that place appears in the <em>Search</em> and <em>Reverse</em> API of Nominatim.</p>
<p>I need a simple interface, like <a href="https://www.facebook.com/help/iphone-app/175921872462772">Facebook's</a>.</p>
<p>If it does not have anything like that, can you point out a way for me to develop the solution myself? I've already researched several OSM editors and found nothing like it.</p>
<p>Thank you</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-reverse" rel="tag" title="see questions tagged &#39;reverse&#39;">reverse</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jun '18, 14:59</strong></p>
<img src="https://secure.gravatar.com/avatar/1c276cd38b3a8114089732886a47d6d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gnosis7&#39;s gravatar image" />
<p><span>gnosis7</span><br />
<span class="score" title="19 reputation points">19</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gnosis7 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64175" class="comments-container">
&#10;</div>
<div id="comment-tools-64175" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64175-form-container" class="comment-form-container">
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

<span id="64176"></span>

<div id="answer-container-64176" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64176-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64176-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-64176-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gnosis7 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you wanted to use an OSM editor for this, you would have to have an OSM API and database, where your users add content and that then gets fed into your Nominatim instance (assuming that you do not want your users to add data to the global OpenStreetMap database - which would be a wholly different issue).</p>
<p>Setting up your own OSM API and database including replication to OSM is going to be difficult, and the OSM editors are built for much more than adding POIs so their interface will not necessarily be simple, although there are some editors specifically for that, like onosm.org.</p>
<p>What could be an option for you is writing your own web application that lets users add a POI, and then generate a short "osc" file for that, a changeset that only contains the addition of one node. You can then consume that using Nominatim's update.php and add it to your database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jun '18, 15:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-64176" class="comments-container">
<span id="64177"></span>
<div id="comment-64177" class="comment">
<div id="post-64177-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Frederik Ramm thank's for your time, Exactly what I need, I do not want POIs entered by users to be added to the OpenStreetMap global database. How would I use onosm.org on my own instance? Is there any documentation on how to generate the "osc" file? If I generate an "osc" file, can I generate it with all the relationships I see in the details.php of the nominatim in the session address? <a href="https://nominatim.openstreetmap.org/details.php?place_id=177715572#address">https://nominatim.openstreetmap.org/details.php?place_id=177715572#address</a></p>
</div>
<div id="comment-64177-info" class="comment-info">
<span class="comment-age">(12 Jun '18, 15:37)</span> <span class="comment-user userinfo">gnosis7</span>
</div>
</div>
</div>
<div id="comment-tools-64176" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64176-form-container" class="comment-form-container">
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

