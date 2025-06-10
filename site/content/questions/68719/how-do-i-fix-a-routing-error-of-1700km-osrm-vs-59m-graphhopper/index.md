+++
type = "question"
title = "How do I fix a routing error of 1700km OSRM vs 59m GraphHopper?"
description = '''I was trying to calculate a route I will be traveling this year and came up with a routing error that takes me 1706km Car (OSRM) vs 59m distance with Car (GraphHopper). I thought there was an error in the road as this is an area that has been under construction. I did a comparison to Google Maps and...'''
date = "2019-04-09T07:19:00Z"
lastmod = "2019-04-10T08:53:00Z"
weight = 68719
keywords = [ "osrm", "routing", "error" ]
aliases = [ "/questions/68719" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I fix a routing error of 1700km OSRM vs 59m GraphHopper?](/questions/68719/how-do-i-fix-a-routing-error-of-1700km-osrm-vs-59m-graphhopper)

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
<span id="post-68719-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68719-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68719-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I was trying to calculate a route I will be traveling this year and came up with a routing error that takes me 1706km Car (OSRM) vs 59m distance with Car (GraphHopper).</p>
<p>I thought there was an error in the road as this is an area that has been under construction. I did a comparison to Google Maps and with the have edited the map close to the same with more to do.</p>
<p>I am not sure why the routing takes me this way and have waited a couple of days for the server to update. The map is updated but the routing db for OSRM still has a problem.</p>
<p>Is this something I can fix?</p>
<p>How long do I need to wait for the OSRM routes to be updated?</p>
<p>Point 1 48.94339, -88.36608 Point 2 48.94291, -88.36644</p>
<p><a href="https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&amp;route=48.94339%2C-88.36608%3B48.94291%2C-88.36644#map=7/47.665/-88.206">https://www.openstreetmap.org/directions?engine=fossgis_osrm_car&amp;route=48.94339%2C-88.36608%3B48.94291%2C-88.36644#map=7/47.665/-88.206</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Apr '19, 07:19</strong></p>
<img src="https://secure.gravatar.com/avatar/64205d7e767055bacbe54a5d6b893164?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MeMaps&#39;s gravatar image" />
<p><span>MeMaps</span><br />
<span class="score" title="71 reputation points">71</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MeMaps has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-68719" class="comments-container">
&#10;</div>
<div id="comment-tools-68719" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-68719-form-container" class="comment-form-container">
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

<span id="68720"></span>

<div id="answer-container-68720" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-68720-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-68720-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-68720-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://www.openstreetmap.org/way/682312286/history">way 682312286</a> did still have <code>construction=trunk</code> set additionally to <code>highway=trunk</code>. I guess this <code>construction</code> tag is the reason why OSRM tried to avoid this road whereas GraphHopper did only look at the <code>highway</code> tag. I removed the construction tag.</p>
<p>It will take a while for routing engines to update their data. You will have to wait a few days, probably up to two weeks.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Apr '19, 07:24</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Apr '19, 07:26</strong> </span></p>
</div>
</div>
<div id="comments-container-68720" class="comments-container">
<span id="68721"></span>
<div id="comment-68721" class="comment">
<div id="post-68721-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ah, I was looking at the OSM inspector tonight and trying to learn some more and it said that there was a hidden NoOp in it as well.</p>
<p>I may have removed you edit as I was trying to remove this no-op about the same time you were editing.</p>
<p>I will have GPS traces of this area later this year so will know how the full construction is completed and the one ways at that time.</p>
</div>
<div id="comment-68721-info" class="comment-info">
<span class="comment-age">(09 Apr '19, 07:58)</span> <span class="comment-user userinfo">MeMaps</span>
</div>
</div>
<span id="68723"></span>
<div id="comment-68723" class="comment">
<div id="post-68723-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Next time please try to modify the existing way instead of deleting it. You can improve its geometry and change tags in order to keep the history. Most of the time deleting a way is not necessary.</p>
</div>
<div id="comment-68723-info" class="comment-info">
<span class="comment-age">(09 Apr '19, 08:13)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="68727"></span>
<div id="comment-68727" class="comment">
<div id="post-68727-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Just tested. The routing is now working. Thanks you.</p>
<p>I will learn more as I use the tools more. I tried to edit it for a few days but it wouldn't repair the routing.</p>
</div>
<div id="comment-68727-info" class="comment-info">
<span class="comment-age">(09 Apr '19, 17:11)</span> <span class="comment-user userinfo">MeMaps</span>
</div>
</div>
<span id="68728"></span>
<div id="comment-68728" class="comment">
<div id="post-68728-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The conclusion is that the routing in graphhopper is broken and OSRM was correct, so you should be opening a ticket with graphhopper to get that fixed.</p>
</div>
<div id="comment-68728-info" class="comment-info">
<span class="comment-age">(09 Apr '19, 19:14)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
<span id="68730"></span>
<div id="comment-68730" class="comment">
<div id="post-68730-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I wouldn't draw that conclusion Simon. highway=trunk + construction=trunk is broken tagging. Each router somehow handled it and in my opinion Graphhopper did the better interpretation by favoring the main tag over the secondary one.</p>
</div>
<div id="comment-68730-info" class="comment-info">
<span class="comment-age">(09 Apr '19, 19:20)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="68734"></span>
<div id="comment-68734" class="comment not_top_scorer">
<div id="post-68734-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The OSRM rounting graph is updated daily</p>
</div>
<div id="comment-68734-info" class="comment-info">
<span class="comment-age">(09 Apr '19, 19:57)</span> <span class="comment-user userinfo">datendelphin</span>
</div>
</div>
<span id="68744"></span>
<div id="comment-68744" class="comment not_top_scorer">
<div id="post-68744-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/10133/tzorn">@TZorn</a> I would disagree. While it isn't quite correct tagging, ignoring tagging that would imply ongoing construction work is not a good idea.</p>
</div>
<div id="comment-68744-info" class="comment-info">
<span class="comment-age">(10 Apr '19, 08:53)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-68720" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-68720-form-container" class="comment-form-container">
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

