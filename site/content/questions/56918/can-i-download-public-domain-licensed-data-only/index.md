+++
type = "question"
title = "Can I download public domain licensed data only?"
description = '''Hello Awesome OSM Community! I&#x27;d like to setup a Nominatim-Server for in company use. We want to validate and complete our databases with it. The ODb-License is too complicated for our small company, we do not want to get in trouble after all. So my question is: Can we somehow get PD data only? Chee...'''
date = "2017-07-06T17:45:00Z"
lastmod = "2017-07-07T13:06:00Z"
weight = 56918
keywords = [ "download", "nominatim", "license", "public_domain" ]
aliases = [ "/questions/56918" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Can I download public domain licensed data only?](/questions/56918/can-i-download-public-domain-licensed-data-only)

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
<span id="post-56918-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56918-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-56918-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello Awesome OSM Community! I'd like to setup a Nominatim-Server for in company use. We want to validate and complete our databases with it. The ODb-License is too complicated for our small company, we do not want to get in trouble after all. So my question is: Can we somehow get PD data only?</p>
<p>Cheers, osmb0t</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-license" rel="tag" title="see questions tagged &#39;license&#39;">license</span> <span class="post-tag tag-link-public_domain" rel="tag" title="see questions tagged &#39;public_domain&#39;">public_domain</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jul '17, 17:45</strong></p>
<img src="https://secure.gravatar.com/avatar/2363fc250e6fc78f7016826704402254?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="osmb0t&#39;s gravatar image" />
<p><span>osmb0t</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="osmb0t has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56918" class="comments-container">
&#10;</div>
<div id="comment-tools-56918" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56918-form-container" class="comment-form-container">
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

<span id="56919"></span>

<div id="answer-container-56919" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56919-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56919-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-56919-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="osmb0t has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>Can we somehow get PD data only?</p>
</blockquote>
<p>I don't think there's an easy way to do that. Some users have reported that all their edits are in the PD (check the OSM wiki), so you'd have to filter out for only things touched by someone who has marked that. (if an object was created by someone who doesn't release PD data, and last changed by someone who does, then that object is tainted). I suspect you'll get hardly any data. So practically, there's no proper "PD-only" data set.</p>
<p>You could look at the import data, and check the licence for that, and just use that directly.</p>
<blockquote>
<p>The ODb-License is too complicated for our small company, we do not want to get in trouble after a</p>
</blockquote>
<p>ODbL isn't too complicated. If you release your data (&amp; attribute OSM) then you're in the clear. There are some times you don't have to release data (like if only employees use it), and some uncertain areas. But if you release the data, you'll definitly be in the clear. (NB if you're using another data source as well, you may not be legally able to release that, and I'm not sure how data protection affects it too)/.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jul '17, 19:52</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-56919" class="comments-container">
<span id="56934"></span>
<div id="comment-56934" class="comment">
<div id="post-56934-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for the fast reply. However we're not authorized to release our customers data, we just store, validate and enrich it to return it back to them. So I guess we're not allowed to integrate OSM data into our database. I'll see how it is with checking for every object, maybe I can modify nominatim to only return PD data.</p>
</div>
<div id="comment-56934-info" class="comment-info">
<span class="comment-age">(07 Jul '17, 11:49)</span> <span class="comment-user userinfo">osmb0t</span>
</div>
</div>
<span id="56935"></span>
<div id="comment-56935" class="comment">
<div id="post-56935-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I simplified the releasing requirements. If you only use OSM internally and nothing OSM derived goes to the public/your customers, then you are not required to share the data you have. Perhaps this might be good enough for your use cases?</p>
<p>Have you seen OpenAddresses.io? It's a collection of many address databases, under a variety of licences. Many don't have the "share-alike" aspect of OSM. Perhaps you could use something from there.</p>
</div>
<div id="comment-56935-info" class="comment-info">
<span class="comment-age">(07 Jul '17, 12:19)</span> <span class="comment-user userinfo">rorym</span>
</div>
</div>
<span id="56940"></span>
<div id="comment-56940" class="comment">
<div id="post-56940-score" class="comment-score">
3
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/30/rorym">@rorym</a> I would recommend against using OA if you are not willing to vet the provenance (some of the sources have been obtained in more than shady ways) and licence suitability yourself.</p>
</div>
<div id="comment-56940-info" class="comment-info">
<span class="comment-age">(07 Jul '17, 13:02)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-56919" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56919-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="56941"></span>

<div id="answer-container-56941" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56941-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56941-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-56941-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Using OpenStreetMap data with other data, which for example is private and confidential is completely possible.</p>
<p>If this is an internal only use, the share alike provisions of the ODbL do not apply in any case, for other uses that do not invoke share alike see: <a href="https://wiki.osmfoundation.org/wiki/Licence/Community_Guidelines/Collective_Database_Guideline_Guideline">Collective Database Guideline</a></p>
<p>As to the original question, see <a href="https://blog.openstreetmap.org/2013/10/15/the-pd-checkbox/">https://blog.openstreetmap.org/2013/10/15/the-pd-checkbox/</a> for why it is not possible in any practical way.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jul '17, 13:06</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Jul '17, 13:08</strong> </span></p>
</div>
</div>
<div id="comments-container-56941" class="comments-container">
&#10;</div>
<div id="comment-tools-56941" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56941-form-container" class="comment-form-container">
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

