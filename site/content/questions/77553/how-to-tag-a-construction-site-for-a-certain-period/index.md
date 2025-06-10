+++
type = "question"
title = "How to tag a construction site for a certain period?"
description = '''Hi, Our company executes individual house construction projects for our customers&#x27;. During the project timelines, I would like to tag the construction sites with a tag &quot;Happho Construction Site&quot; in order for other visitors to easily identify the site location. But since this is a construction site, ...'''
date = "2020-11-15T10:25:00Z"
lastmod = "2020-11-15T13:04:00Z"
weight = 77553
keywords = [ "construction", "tagging", "photo_geotagging" ]
aliases = [ "/questions/77553" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag a construction site for a certain period?](/questions/77553/how-to-tag-a-construction-site-for-a-certain-period)

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
<span id="post-77553-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77553-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-77553-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Our company executes individual house construction projects for our customers'. During the project timelines, I would like to tag the construction sites with a tag "<a href="https://happho.com">Happho</a> Construction Site" in order for other visitors to easily identify the site location. But since this is a construction site, the tag needs to be there for only a certain period say 6-8 months time.</p>
<p>Can anyone please let me know how to do this. Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-construction" rel="tag" title="see questions tagged &#39;construction&#39;">construction</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-photo_geotagging" rel="tag" title="see questions tagged &#39;photo_geotagging&#39;">photo_geotagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Nov '20, 10:25</strong></p>
<img src="https://secure.gravatar.com/avatar/6c0789863bf81692b25ca6930ddc2b71?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Karthik%20Happho&#39;s gravatar image" />
<p><span>Karthik Happho</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Karthik Happho has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-77553" class="comments-container">
&#10;</div>
<div id="comment-tools-77553" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77553-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="77555"></span>

<div id="answer-container-77555" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77555-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77555-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-77555-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The tag <a href="https://wiki.openstreetmap.org/wiki/Tag:landuse%3Dconstruction"><code>landuse=construction</code></a> is commonly used to identify construction sites, although it wouldn't really apply to "invisible" construction or minor renovations. For new buildings <a href="https://wiki.openstreetmap.org/wiki/Tag:building%3Dconstruction"><code>building=construction</code></a> + <a href="https://wiki.openstreetmap.org/wiki/Key:building"><code>construction={building type}</code></a> are also used.</p>
<p>As stated on the <code>landuse=construction</code> page, the <a href="https://wiki.openstreetmap.org/wiki/Key:operator">operator tag</a> can be used to identify the main construction company. I don't think this is rendered on the map shown on OpenStreetMap.org, but should show up in queries and would be available for custom rendering.</p>
<p>Please be aware apps and maps that use OpenStreetMap data do not necessarily update very frequently with maps apps often updating only once every month or two. For this reason "temporary" items aren't usually mapped. As with many things in OSM there is no hard rule but the <a href="https://wiki.openstreetmap.org/wiki/Good_practice#Don.27t_map_temporary_events_and_temporary_features">good practice guide</a> recommends that items "should at least be expected to remain unchanged in the next few weeks". I would think 6-8 months should be just about OK as long as you are sure to either remove the objects or update the tagging to reflect the final configuration when the project completes.</p>
<p>If you need something that responds more quickly you might be better off having a page on your site that displays something like a <a href="https://wiki.openstreetmap.org/wiki/UMap">UMap</a> map of active projects.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '20, 11:52</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-77555" class="comments-container">
&#10;</div>
<div id="comment-tools-77555" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77555-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="77557"></span>

<div id="answer-container-77557" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77557-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77557-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-77557-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is an interesting use-case. We dont have any explicit way of flagging objects needing review at particular dates, but it is certainly practical for data such as your own. If you consistently tag your firm's name in the operator tag and use another tag to store the anticipated completion date in YYYY-MM-DD format it is possible to use Overpass-turbo to search for landuse=construction, operator=, &lt;completion_date&gt;. (I would suggest forecast_end_date, which shows a clear relationship to end_date.).</p>
<p>The format of an overpass-query would look something like this:</p>
<pre><code>way[landuse=construction][operator=&quot;Acme Construction&quot;][end_date](if: t[&quot;end_date&quot;] &lt;= &quot;2017-12-31&quot;);</code></pre>
<p>I've created <a href="https://overpass-turbo.eu/s/10b1">an example</a> to provide a suitable template (and, incidentally, for my own use!).</p>
<p>When performing the updates I presume you'll change the landuse to residential (or delete if already in a residential area), but it may also be nice if you can provide the new address. This would be a benefit for your customers as new home owners often have problems with deliveries at a time when they are inevitably making lots of purchases.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '20, 13:04</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-77557" class="comments-container">
&#10;</div>
<div id="comment-tools-77557" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77557-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="77556"></span>

<div id="answer-container-77556" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-77556-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-77556-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-77556-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I agree with InsertUser 's and SK53's answers. But a simple way to point to a location is to use the share link. <a href="https://www.openstreetmap.org/?mlat=52.33132&amp;mlon=-0.17397#map=17/52.33132/-0.17397">https://www.openstreetmap.org/?mlat=52.33132&amp;mlon=-0.17397#map=17/52.33132/-0.17397</a></p>
<p>For a step by step of how to do this see my answer to this one. <a href="https://help.openstreetmap.org/questions/25/how-do-i-add-a-marker-to-a-map">https://help.openstreetmap.org/questions/25/how-do-i-add-a-marker-to-a-map</a></p>
<p>Sat Nav users can use the mlat and mlon in their sat navs. that is 52.33132 N 0.17397 W so your suppliers should be able to locate your building site. note:- negative values signify South and West</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '20, 12:15</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Nov '20, 20:28</strong> </span></p>
</div>
</div>
<div id="comments-container-77556" class="comments-container">
&#10;</div>
<div id="comment-tools-77556" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-77556-form-container" class="comment-form-container">
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

