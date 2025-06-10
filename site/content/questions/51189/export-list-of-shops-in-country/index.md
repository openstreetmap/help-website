+++
type = "question"
title = "export list of shops in country"
description = '''Hi, I&#x27;m new to openstreetmaps, so pardon for the basic question. How do I extract a list of every Tesco in the UK with all relevant tags associated with each? The long term aim is to automate this process so I can have it all put into a DB. Can anyone point me in the right direction? Cheers,'''
date = "2016-08-01T14:02:00Z"
lastmod = "2016-08-02T12:15:00Z"
weight = 51189
keywords = [ "list", "export" ]
aliases = [ "/questions/51189" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [export list of shops in country](/questions/51189/export-list-of-shops-in-country)

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
<span id="post-51189-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51189-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51189-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm new to openstreetmaps, so pardon for the basic question. How do I extract a list of every Tesco in the UK with all relevant tags associated with each?</p>
<p>The long term aim is to automate this process so I can have it all put into a DB. Can anyone point me in the right direction?</p>
<p>Cheers,</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-list" rel="tag" title="see questions tagged &#39;list&#39;">list</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Aug '16, 14:02</strong></p>
<img src="https://secure.gravatar.com/avatar/688fe2a76a5d3843e2030260215159d6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scass&#39;s gravatar image" />
<p><span>scass</span><br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scass has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51189" class="comments-container">
&#10;</div>
<div id="comment-tools-51189" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51189-form-container" class="comment-form-container">
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

<span id="51190"></span>

<div id="answer-container-51190" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51190-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51190-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-51190-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="scass has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In general the easiest way is to use <a href="http://wiki.openstreetmap.org/wiki/Overpass_API">Overpass</a> or <a href="http://wiki.openstreetmap.org/wiki/Overpass_turbo">Overpass-Turbo</a>. This <a href="http://overpass-turbo.eu/s/hCZ">example</a> shows a suitable query using Overpass-Turbo. Both approaches allow a variety of output methods (such as Geojson or CSV).</p>
<p>The alternative is to start with a complete extract of a given country and use similar filters to obtain the same information. The most useful tools for this are osmconvert and <a href="http://wiki.openstreetmap.org/wiki/Osmfilter">osmfilter</a>.</p>
<p>You may need to consider a couple of things about such data:</p>
<ul>
<li>Convenience stores associated with petrol stations will often be mapped separately (they have different opening hours, food hygiene inspections etc), and this may lead to double counting for your purposes.</li>
<li>Beware of just searching for things like 'Tesco': you will find lots of bus stops and parking areas.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Aug '16, 18:34</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-51190" class="comments-container">
<span id="51197"></span>
<div id="comment-51197" class="comment">
<div id="post-51197-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for this explanation, it's very useful. just out of curiosity, I can see a Tesco supermarket that I know of in Kent which appears on OSM but not in the search, could you explain why? <a href="https://www.openstreetmap.org/#map=19/51.39486/0.49119">https://www.openstreetmap.org/#map=19/51.39486/0.49119</a></p>
</div>
<div id="comment-51197-info" class="comment-info">
<span class="comment-age">(02 Aug '16, 10:47)</span> <span class="comment-user userinfo">scass</span>
</div>
</div>
<span id="51204"></span>
<div id="comment-51204" class="comment">
<div id="post-51204-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Yes, very straightforward, each pair of lines should have contain one which starts with way not node. With overpass one needs to query both things mapped as a point (node) and as areas (ways). The corrected query is here: <a href="http://overpass-turbo.eu/s/hDn">http://overpass-turbo.eu/s/hDn</a> . This ups the number of results from under 1000 to nigh on 2000</p>
</div>
<div id="comment-51204-info" class="comment-info">
<span class="comment-age">(02 Aug '16, 12:15)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-51190" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51190-form-container" class="comment-form-container">
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

