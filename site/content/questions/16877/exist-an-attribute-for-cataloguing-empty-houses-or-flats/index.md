+++
type = "question"
title = "Exist an attribute for cataloguing empty houses or flats?"
description = '''Hi, We are a neighborhood collective that want to mark empty houses and flats: Their characteristics are that windows and doors are boarded up with cement. So it is a clear sign that they do not want to use that space for nothing for a long time. There is a spanish web [1] that do this, and uses osm...'''
date = "2012-10-13T11:58:00Z"
lastmod = "2012-10-15T11:58:00Z"
weight = 16877
keywords = [ "attributes", "tagging" ]
aliases = [ "/questions/16877" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Exist an attribute for cataloguing empty houses or flats?](/questions/16877/exist-an-attribute-for-cataloguing-empty-houses-or-flats)

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
<span id="post-16877-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16877-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-16877-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>We are a neighborhood collective that want to mark empty houses and flats: Their characteristics are that windows and doors are boarded up with cement. So it is a clear sign that they do not want to use that space for nothing for a long time.</p>
<p>There is a spanish web [1] that do this, and uses osm in background. The problem is that the data are licensed on "Public Domain", and we would like to use Open Data Commons Open Database License (ODbL).</p>
<p>Exist an attribute in OSM to mark this? In negative case, It can be created? References?</p>
<p>Thanks!</p>
<p>[1] <a href="http://casastristes.org/">http://casastristes.org/</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-attributes" rel="tag" title="see questions tagged &#39;attributes&#39;">attributes</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Oct '12, 11:58</strong></p>
<img src="https://secure.gravatar.com/avatar/5a3e011503c8bb0fd7913982b4137af6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="amapolas&#39;s gravatar image" />
<p><span>amapolas</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="amapolas has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Oct '12, 12:01</strong> </span></p>
</div>
</div>
<div id="comments-container-16877" class="comments-container">
&#10;</div>
<div id="comment-tools-16877" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16877-form-container" class="comment-form-container">
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

<span id="16896"></span>

<div id="answer-container-16896" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16896-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16896-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-16896-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The usual way to mark this in OSM is with <code>disused=yes</code>. From the <a href="https://wiki.openstreetmap.org/wiki/Key:disused">wiki page</a></p>
<blockquote>
<p>A disused feature is any man-made feature which is no longer used for its intended purpose, but which is still maintained and has repairs made. Reuse may be planned. Disused features are still useful for navigation and are visible in the landscape. Frequently these will be boarded-up buildings; for example, an old disused multi-storey car park.</p>
</blockquote>
<p>So this seems to fit your case quite well. Note that in addition to adding this tag, you should change any tags which no longer apply, by prefixing "disused:". For example <code>amenity=pub</code> becomse <code>disused:amenity=pub</code>, because the building in question no longer houses a pub. This is important for software which does not understand the <code>disused</code> tag - otherwise it would see the <code>amenity=pub</code> and list it is a pub.</p>
<p>So in your case you could just add <code>disused=yes</code> to the abandoned buildings. In that case, I don't think it's necessary to change the <code>building=yes</code> (or <code>building=residential</code> etc.) tag - the building is still a building.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Oct '12, 09:10</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-16896" class="comments-container">
<span id="16899"></span>
<div id="comment-16899" class="comment">
<div id="post-16899-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If you look at the <a href="https://wiki.openstreetmap.org/wiki/Railway">railway</a> tag the values abandoned and disused <em>can</em> have different meanings. A building which is empty for only a short time may be abandoned during that time, but not really disused. Of course this depends on the interpretation and should be clarified in the wiki.</p>
</div>
<div id="comment-16899-info" class="comment-info">
<span class="comment-age">(15 Oct '12, 11:58)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-16896" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16896-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16882"></span>

<div id="answer-container-16882" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16882-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16882-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-16882-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://taginfo.openstreetmap.org">taginfo</a> reports <a href="http://taginfo.openstreetmap.org/tags/building=abandoned">building=abandoned</a> which you could use for this. There is also <a href="http://taginfo.openstreetmap.org/tags/building=disused">building=disused</a> but the meaning seems not very clear to me.</p>
<p>Furthermore the wiki suggests that you can use <a href="https://wiki.openstreetmap.org/wiki/Any_tags_you_like">any tags you like</a>. But note that not every information belongs into OSM's database. For personal purposes better create a separate database and display its content via an overlay on top of a OSM map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Oct '12, 14:02</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-16882" class="comments-container">
<span id="16897"></span>
<div id="comment-16897" class="comment">
<div id="post-16897-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't think <code>building=abandoned</code> or <code>building=disused</code> are good ideas. They are not mentioned in the Wiki, and they are hardly used, as compared to <code>disused=yes</code>.</p>
</div>
<div id="comment-16897-info" class="comment-info">
<span class="comment-age">(15 Oct '12, 09:16)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
</div>
<div id="comment-tools-16882" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16882-form-container" class="comment-form-container">
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

