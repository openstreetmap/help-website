+++
type = "question"
title = "How to extract all admin_centres of an area?"
description = '''In this query [out:csv(::id, ::type, name, &quot;name:te&quot;, wikidata)]; area[&quot;boundary&quot;=&quot;administrative&quot;][&quot;admin_level&quot;=&quot;4&quot;][&quot;name&quot;=&quot;Andhra Pradesh&quot;]-&amp;gt;.searchArea; ( relation[&quot;boundary&quot;=&quot;administrative&quot;][&quot;admin_level&quot;=&quot;6&quot;](area.searchArea);  node(r:&quot;admin_centre&quot;)-&amp;gt;.result; ); /*(._ ; &amp;gt; ;);*/ .re...'''
date = "2021-07-19T07:59:00Z"
lastmod = "2021-07-19T11:57:00Z"
weight = 81027
keywords = [ "relation", "admin_centre" ]
aliases = [ "/questions/81027" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to extract all admin_centres of an area?](/questions/81027/how-to-extract-all-admin_centres-of-an-area)

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
<span id="post-81027-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81027-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81027-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In this query</p>
<pre><code>[out:csv(::id, ::type, name, &quot;name:te&quot;, wikidata)];
area[&quot;boundary&quot;=&quot;administrative&quot;][&quot;admin_level&quot;=&quot;4&quot;][&quot;name&quot;=&quot;Andhra Pradesh&quot;]-&gt;.searchArea;
(   relation[&quot;boundary&quot;=&quot;administrative&quot;][&quot;admin_level&quot;=&quot;6&quot;](area.searchArea);
    node(r:&quot;admin_centre&quot;)-&gt;.result;
);
/*(._ ; &gt; ;);*/
.result out;</code></pre>
<p>The result shows only 666 admin_centres. There are actually 670 admin_centres with 668 distinct ones. The missing admin_centres are <a href="https://www.openstreetmap.org/node/3665399128">https://www.openstreetmap.org/node/3665399128</a> and <a href="https://www.openstreetmap.org/node/2408119848">https://www.openstreetmap.org/node/2408119848</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-admin_centre" rel="tag" title="see questions tagged &#39;admin_centre&#39;">admin_centre</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jul '21, 07:59</strong></p>
<img src="https://secure.gravatar.com/avatar/3b9c98e91286cb9b84f3c64850b37944?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arjunaraoc&#39;s gravatar image" />
<p><span>arjunaraoc</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arjunaraoc has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jul '21, 08:00</strong> </span></p>
</div>
</div>
<div id="comments-container-81027" class="comments-container">
&#10;</div>
<div id="comment-tools-81027" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81027-form-container" class="comment-form-container">
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

<span id="81028"></span>

<div id="answer-container-81028" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81028-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81028-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81028-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I realised that relations with common admin_centre are present in output and there are 4 such duplicates</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Jul '21, 11:57</strong></p>
<img src="https://secure.gravatar.com/avatar/3b9c98e91286cb9b84f3c64850b37944?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arjunaraoc&#39;s gravatar image" />
<p><span>arjunaraoc</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arjunaraoc has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81028" class="comments-container">
&#10;</div>
<div id="comment-tools-81028" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81028-form-container" class="comment-form-container">
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

