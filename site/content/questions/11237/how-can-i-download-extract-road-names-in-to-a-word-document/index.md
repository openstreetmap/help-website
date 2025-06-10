+++
type = "question"
title = "how can I download/ extract road names in to a word document"
description = '''I want to download all the road names (and the post code if possible) from one particular town in the UK and put it into a word or excel document- is this possible? if so, how?'''
date = "2012-03-16T00:44:00Z"
lastmod = "2012-03-16T20:14:00Z"
weight = 11237
keywords = [ "download", "word", "extract", "names", "road" ]
aliases = [ "/questions/11237" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how can I download/ extract road names in to a word document](/questions/11237/how-can-i-download-extract-road-names-in-to-a-word-document)

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
<span id="post-11237-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11237-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11237-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to download all the road names (and the post code if possible) from one particular town in the UK and put it into a word or excel document- is this possible? if so, how?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-word" rel="tag" title="see questions tagged &#39;word&#39;">word</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-names" rel="tag" title="see questions tagged &#39;names&#39;">names</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Mar '12, 00:44</strong></p>
<img src="https://secure.gravatar.com/avatar/7ae72693bb323d598219547114aa3230?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="summerbreeze123&#39;s gravatar image" />
<p><span>summerbreeze123</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="summerbreeze123 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11237" class="comments-container">
&#10;</div>
<div id="comment-tools-11237" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11237-form-container" class="comment-form-container">
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

<span id="11262"></span>

<div id="answer-container-11262" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11262-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11262-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-11262-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think your question was left unanswered because one might suspect it will be a steep learning curve for you to accomplish your wish, as you imply that getting it in to a Word-document is part of the problem ;)</p>
<p>But a straightforward way of doing this could be:</p>
<ol>
<li><a href="http://wiki.openstreetmap.org/wiki/Planet.osm">Download</a> planet.osm (20 GB), or better, a UK extract (~500 MB)<br />
<strong>(Don't do this if you don't feel confident executing the other steps)</strong></li>
<li>Install <a href="http://wiki.openstreetmap.org/wiki/PostgreSQL">PostgreSQL</a></li>
<li>Install <a href="http://wiki.openstreetmap.org/wiki/Osm2pgsql">Osm2pgsql</a> and import your osm-file to PostgreSQL</li>
<li>Apply relevant <a href="http://wiki.openstreetmap.org/wiki/Osm2pgsql/schema">SQL-query</a></li>
</ol>
<p>Or, if you're willing to compensate, you could contact any of the Openstreetmap consultants, like <a href="http://www.geofabrik.de/services/consulting.html">Geofabrik</a> or <a href="http://www.gravitystorm.co.uk/andy">gravitystorm</a></p>
<p>(There might be some clever way of doing this easy, like <a href="http://nominatim.openstreetmap.org/search?q=Restaurants%20in%20London&amp;format=xml">this</a>, or for your particular question: <a href="http://nominatim.openstreetmap.org/search?q=Residentials%20in%20London">http://nominatim.openstreetmap.org/search?q=Residentials%20in%20London</a>, but it doesn't work and would be some pain to extract the result.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Mar '12, 20:14</strong></p>
<img src="https://secure.gravatar.com/avatar/ec2962c6ef6aab7940982ed25f2ca544?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TheOddOne2&#39;s gravatar image" />
<p><span>TheOddOne2</span><br />
<span class="score" title="685 reputation points">685</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TheOddOne2 has one accepted answer">3%</span> </br></p>
</div>
</div>
<div id="comments-container-11262" class="comments-container">
&#10;</div>
<div id="comment-tools-11262" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11262-form-container" class="comment-form-container">
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

