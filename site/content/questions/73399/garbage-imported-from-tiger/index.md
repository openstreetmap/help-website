+++
type = "question"
title = "GARBAGE imported from Tiger"
description = '''In Sequoyah County, Oklahoma, USA, a bulk import of data from Tiger Map Service has resulted in tons of dirt paths labeled highway=residential, many roads and paths where none has ever actually existed, service roads FAR from where they were actually placed, and so on. I have fixed many, but I can’t...'''
date = "2020-03-05T15:30:00Z"
lastmod = "2023-02-09T21:20:00Z"
weight = 73399
keywords = [ "tiger" ]
aliases = [ "/questions/73399" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [GARBAGE imported from Tiger](/questions/73399/garbage-imported-from-tiger)

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
<span id="post-73399-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73399-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73399-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In Sequoyah County, Oklahoma, USA, a bulk import of data from Tiger Map Service has resulted in tons of dirt paths labeled highway=residential, many roads and paths where none has ever actually existed, service roads FAR from where they were actually placed, and so on. I have fixed many, but I can’t possibly spare the time to fix all of them, and I only find them if I happen to be working in the same area.</p>
<p>Is there a way that others (assuming anyone cares) can find them, and after fixing them, mark them so others don’t waste time looking at one that’s already fixed?</p>
<p>And, when we fix one, should we remove the tiger tags?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiger" rel="tag" title="see questions tagged &#39;tiger&#39;">tiger</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Mar '20, 15:30</strong></p>
<img src="https://secure.gravatar.com/avatar/4dbb88ad9ac898c20c4d084107218785?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Happy%20Hobo&#39;s gravatar image" />
<p><span>Happy Hobo</span><br />
<span class="score" title="85 reputation points">85</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Happy Hobo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73399" class="comments-container">
<span id="84165"></span>
<div id="comment-84165" class="comment">
<div id="post-84165-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have a similar problem in that a local editor has taken it himself to "clean up" OSM in my area by referencing Tiger.</p>
<p>In doing so, he deletes real roads, paths and other information presumably because it doesn't exist in Tiger!</p>
</div>
<div id="comment-84165-info" class="comment-info">
<span class="comment-age">(13 Apr '22, 04:54)</span> <span class="comment-user userinfo">kevinp2</span>
</div>
</div>
<span id="84173"></span>
<div id="comment-84173" class="comment">
<div id="post-84173-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/21624/kevinp2">@kevinp2</a> I'd suggest you politely communicate with this mapper using a public changeset comment on one of their "clean up" changesets, or by sending a private OSM message if you prefer. I'd emphasize that TIGER is a useful but not authoritative data source, and that many real-world roads and paths do not appear in TIGER.</p>
<p>As a last resort, you can report this mapper to OSM's <a href="https://wiki.openstreetmap.org/wiki/Data_working_group">Data Working Group</a> by emailing data@openstreetmap.org or using the "Report this User" link on the mapper's profile page.</p>
</div>
<div id="comment-84173-info" class="comment-info">
<span class="comment-age">(13 Apr '22, 15:47)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
</div>
<div id="comment-tools-73399" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73399-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="73401"></span>

<div id="answer-container-73401" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73401-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73401-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-73401-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The short answer is to remove the <strong><code>tiger:reviewed=no</code></strong> tag after having confirmed or fixed the geometry <em>and properties</em> (see below) of a TIGER-imported road. Then mappers who are looking for roads to fix can search for those that still have <strong><code>tiger:reviewed=no</code></strong>.</p>
<p>Ed's is the long answer, if you read that whole page, but it's worth reading. In particular note that TIGER data has continued to improve in some areas, and while it's not feasible to redo the import, it is possible to view the new TIGER roads as an overlay layer which can help with fixing up some of the old TIGER garbage.</p>
<p>Some <strong><code>tiger:</code></strong> tags are automatically removed by the editing software whenever a road is modified, but not all. Personally I like to leave at least the <strong><code>tiger:cfcc</code></strong> and sometimes <strong><code>tiger:county</code></strong> -- and also the road name components, if it's a named road.</p>
<hr />
<p>Edit - Incorporating Richard's good advice, I changed "geometry" to "geometry and properties". Primarily this means that in addition to the road's shape you should confirm or fix the value of the <strong><code>highway=</code></strong> tag, and also add <strong><code>surface=</code></strong> for any unpaved residential/unclassified roads. And only then remove the <strong><code>tiger:reviewed=no</code></strong> tag.</p>
<p>(Correctly tagging <strong><code>surface=</code></strong> is always welcome of course, but it's especially important for roads that fall in the gap between track and paved residential/unclassified, and there are many of these in rural USA.)</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '20, 16:31</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Mar '20, 12:58</strong> </span></p>
</div>
</div>
<div id="comments-container-73401" class="comments-container">
<span id="73411"></span>
<div id="comment-73411" class="comment">
<div id="post-73411-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't like how editor-software would automatically remove those tags either. This should be a default disabled option, or prompted for review before removing.</p>
</div>
<div id="comment-73411-info" class="comment-info">
<span class="comment-age">(06 Mar '20, 07:48)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
<span id="73416"></span>
<div id="comment-73416" class="comment">
<div id="post-73416-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Some tiger: tags are by common agreement useless and should never have been imported. There's therefore an agreement that it's ok for editors to remove them silently.</p>
</div>
<div id="comment-73416-info" class="comment-info">
<span class="comment-age">(06 Mar '20, 09:15)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="73423"></span>
<div id="comment-73423" class="comment">
<div id="post-73423-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Most of them also have “tiger:corrected=no” so I suppose I should also change that? And if other tiger things are WRONG, I think I should delete those (because correcting them implies that they are correct in Tiger). But what is the meaning of “tiger:separated=no”?</p>
</div>
<div id="comment-73423-info" class="comment-info">
<span class="comment-age">(06 Mar '20, 13:47)</span> <span class="comment-user userinfo">Happy Hobo</span>
</div>
</div>
<span id="73426"></span>
<div id="comment-73426" class="comment">
<div id="post-73426-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What is the difference between removing “tiger:reviewed=no” and changing it to “yes”?</p>
</div>
<div id="comment-73426-info" class="comment-info">
<span class="comment-age">(06 Mar '20, 14:02)</span> <span class="comment-user userinfo">Happy Hobo</span>
</div>
</div>
<span id="73428"></span>
<div id="comment-73428" class="comment">
<div id="post-73428-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The <strong><code>tiger:separated</code></strong> tag refers to "grade separation", ie, roads that cross but don't intersect because of bridges or tunnels. The value <strong><code>no</code></strong> means that the road segment intersects roads that it crosses, which is the norm, especially in rural situations. The tag was useful during the initial import process but can be removed now.</p>
<p>As far as I know there's no difference in meaning between removing <strong><code>tiger:reviewed=no</code></strong> and setting the value to <strong><code>yes</code></strong>, but the general push is to get rid of the extra <strong><code>tiger:</code></strong> tags so IMO removing the tag is better than changing the value.</p>
</div>
<div id="comment-73428-info" class="comment-info">
<span class="comment-age">(06 Mar '20, 14:24)</span> <span class="comment-user userinfo">jmapb</span>
</div>
</div>
</div>
<div id="comment-tools-73401" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73401-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73417"></span>

<div id="answer-container-73417" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73417-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73417-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-73417-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is the case all over the US. Generally, the issue is <code>highway=residential</code> roads in rural areas that may or may not be roads at all. Some rules of thumb:</p>
<ol>
<li><p>You can change the <code>highway=</code> tag to something else:</p></li>
<li><p><code>highway=unclassified</code> is the OSM standard for rural roads</p></li>
<li><code>highway=track</code> for ungraded/double-track</li>
<li><code>highway=path</code> / <code>footway</code> / <code>cycleway</code> as appropriate</li>
<li><p><code>highway=service; service=driveway</code> for private driveways</p></li>
<li><p>In the developed world, <code>unclassified</code>, <code>residential</code> and <code>service</code> are generally assumed to be paved. If you retag an unpaved road to these, <strong>make sure you also add a surface tag</strong> - <code>surface=unpaved</code> will do fine, but if you can be more specific and use <code>gravel</code> or <code>dirt</code>, so much the better.</p></li>
<li><p>If the road simply doesn't exist, feel free to delete it.</p></li>
<li><p>You can remove <code>tiger:reviewed=no</code> if you like. But <strong>please don't remove this for unpaved roads unless you also add a surface tag</strong> (or something that implies unpaved, such as <code>highway=track</code>).</p></li>
</ol>
<p>(Apologies for nonsensical numbering, help.osm.org's Markdown parsing is beyond broken.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Mar '20, 09:22</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Mar '20, 09:25</strong> </span></p>
</div>
</div>
<div id="comments-container-73417" class="comments-container">
<span id="73424"></span>
<div id="comment-73424" class="comment">
<div id="post-73424-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the additional attributes. Please consider putting them in the Wiki if they are not already there. Sometimes my editor fails to offer suggestions, and I look in the Wiki without success.</p>
</div>
<div id="comment-73424-info" class="comment-info">
<span class="comment-age">(06 Mar '20, 13:49)</span> <span class="comment-user userinfo">Happy Hobo</span>
</div>
</div>
</div>
<div id="comment-tools-73417" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73417-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73400"></span>

<div id="answer-container-73400" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73400-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73400-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-73400-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is a <a href="https://wiki.openstreetmap.org/wiki/TIGER_fixup">TIGER fixup page on the wiki</a> which mentions the incorrect classification as one of the common issues. There is a link to <a href="https://wiki.openstreetmap.org/wiki/TIGER_fixup/Overpass_queries">some overpass queries</a> to help identify area which may still need checking.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Mar '20, 16:08</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-73400" class="comments-container">
&#10;</div>
<div id="comment-tools-73400" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73400-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="73425"></span>

<div id="answer-container-73425" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73425-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73425-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73425-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The “accept” mechanism is also broken. The full answer here unfortunately is a combination of several very useful answers. I tried to accept more than one, but that’s not allowed. I didn’t want to favor part of the answer over another part, but to un-accept took <em>several</em> tries. Many thanks to <strong><em>all</em></strong> who contributed.</p>
<p>As bad as I’ve seen so far, I wonder whether I should recommend <strong>not</strong> using a data source proven to be as bad as this.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Mar '20, 13:55</strong></p>
<img src="https://secure.gravatar.com/avatar/4dbb88ad9ac898c20c4d084107218785?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Happy%20Hobo&#39;s gravatar image" />
<p><span>Happy Hobo</span><br />
<span class="score" title="85 reputation points">85</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Happy Hobo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-73425" class="comments-container">
<span id="73429"></span>
<div id="comment-73429" class="comment">
<div id="post-73429-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The TIGER import had/has enough problems that it has soured a large portion of OSM contributors toward all imports. The TIGER import happened prior to my involvement in OSM and I've cursed it multiple times but thinking back on the state of the map in the US prior to the import I suspect that overall it was a good thing. It at least gave a frame work for the whole country that could be improved upon. If we had the density of mappers that Europe has then it would have been a different story.</p>
<p>One side effect: Having cleaned up a bunch of rural TIGER messes I can see where that same data was used by other maps (Google, Apple, Here, etc.) and can take pride in seeing that OSM volunteers have usually done a better job of cleaning it up in rural areas than some of the for profit mapping outfits. The built in map on my late model Toyota uses Here Maps data and it reminds me every time I glance at it when in the sticks how bad it still is.</p>
</div>
<div id="comment-73429-info" class="comment-info">
<span class="comment-age">(06 Mar '20, 17:26)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="86657"></span>
<div id="comment-86657" class="comment">
<div id="post-86657-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I can still remember asking Mapquest for the route my parents should take to my house. Get off the highway, turn right, go under the highway, then jump the curb and drive into the pond! The road that used to be where the pond now is had been removed for decades (when the highway was built).</p>
</div>
<div id="comment-86657-info" class="comment-info">
<span class="comment-age">(09 Feb '23, 21:20)</span> <span class="comment-user userinfo">Happy Hobo</span>
</div>
</div>
</div>
<div id="comment-tools-73425" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73425-form-container" class="comment-form-container">
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

