+++
type = "question"
title = "Are there any XAPI-like services that return &quot;the first N&quot; rather than &quot;all&quot; matches?"
description = '''Imagine that I&#x27;m looking at the various options for &quot;highway&quot; tagging, and have found highway=services. If there were more objects in the OSM database then using taginfo, I&#x27;d be able to look at combinations. If there were fewer I&#x27;d be able to use the overpass &quot;XAPI&quot; link from that page to look at in...'''
date = "2013-02-12T21:40:00Z"
lastmod = "2013-02-13T13:53:00Z"
weight = 19891
keywords = [ "overpass", "taginfo", "xapi", "data" ]
aliases = [ "/questions/19891" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Are there any XAPI-like services that return "the first N" rather than "all" matches?](/questions/19891/are-there-any-xapi-like-services-that-return-the-first-n-rather-than-all-matches)

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
<span id="post-19891-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19891-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-19891-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Imagine that I'm looking at the various options for "highway" tagging, and have found highway=services.</p>
<p>If there were more objects in the OSM database then using <a href="http://taginfo.openstreetmap.org/tags/highway=services#overview">taginfo</a>, I'd be able to look at combinations. If there were fewer I'd be able to use the overpass "XAPI" link from that page to look at individual objects.</p>
<p>Assuming that in this case I don't want to look at all 4000-odd objects but only a few, is there an easy way to obtain a sample of the matching data, without using a local "select" statement on a local SQL database or passing a bounding box to the XAPI server?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-taginfo" rel="tag" title="see questions tagged &#39;taginfo&#39;">taginfo</span> <span class="post-tag tag-link-xapi" rel="tag" title="see questions tagged &#39;xapi&#39;">xapi</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Feb '13, 21:40</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-19891" class="comments-container">
&#10;</div>
<div id="comment-tools-19891" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19891-form-container" class="comment-form-container">
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

<span id="19894"></span>

<div id="answer-container-19894" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19894-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19894-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-19894-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#Limit_attribute_to_limit_elements_.28limit.2C_n.29">https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#limit_attribute</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Feb '13, 23:37</strong></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cartinus has 35 accepted answers">27%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Nov '17, 23:17</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-19894" class="comments-container">
<span id="19898"></span>
<div id="comment-19898" class="comment">
<div id="post-19898-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That would work for a specific area but not for obtaining a world-wide sample.</p>
</div>
<div id="comment-19898-info" class="comment-info">
<span class="comment-age">(13 Feb '13, 07:31)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="19911"></span>
<div id="comment-19911" class="comment">
<div id="post-19911-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><span></span><span>@scai</span>: because?</p>
<ul>
<li><code>way["name"="Wed"];out 20;</code> Gives three ways (in Rotterdam, Utrecht en Höchst)</li>
<li><code>way["name"="Wed"];out 2;</code> Gives only two ways (in Rotterdam and Utrecht)</li>
</ul>
</div>
<div id="comment-19911-info" class="comment-info">
<span class="comment-age">(13 Feb '13, 13:06)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
<span id="19912"></span>
<div id="comment-19912" class="comment">
<div id="post-19912-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@cartinus</span> Ah you are right. I thought it requires a bbox.</p>
</div>
<div id="comment-19912-info" class="comment-info">
<span class="comment-age">(13 Feb '13, 13:53)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-19894" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19894-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="19899"></span>

<div id="answer-container-19899" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19899-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19899-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19899-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Since taginfo's <a href="http://taginfo.openstreetmap.org/taginfo/apidoc">API</a> seems to have <a href="http://taginfo.openstreetmap.org/api/4/tag/combinations?key=highway&amp;value=services&amp;page=1&amp;rp=10">the same restrictions</a> you could <a href="http://taginfo.openstreetmap.org/download">download</a> <em>their</em> database and see if it still contains this information.</p>
<p>Update: No, <em>taginfo-db.db</em> doesn't contain this information anymore :(</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Feb '13, 07:44</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Feb '13, 08:09</strong> </span></p>
</div>
</div>
<div id="comments-container-19899" class="comments-container">
&#10;</div>
<div id="comment-tools-19899" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19899-form-container" class="comment-form-container">
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

