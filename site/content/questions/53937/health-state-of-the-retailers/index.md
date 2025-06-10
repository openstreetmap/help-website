+++
type = "question"
title = "health state of the retailers"
description = '''Hi it&#x27;s possible to identify the health state of the retailers. I have a project for identify the location of the free retailers. Imagines if you have the possibility to check the condition of the shops: active, not active,for rent, for sale. in this case the color of the identification symble it wi...'''
date = "2017-01-09T00:05:00Z"
lastmod = "2017-01-09T09:29:00Z"
weight = 53937
keywords = [ "healthstate" ]
aliases = [ "/questions/53937" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [health state of the retailers](/questions/53937/health-state-of-the-retailers)

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
<span id="post-53937-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53937-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53937-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi it's possible to identify the health state of the retailers. I have a project for identify the location of the free retailers. Imagines if you have the possibility to check the condition of the shops: active, not active,for rent, for sale. in this case the color of the identification symble it will be different, red, yellow etc. Is this already possible or it will be possible to do togheter? In the attached you can fine a exemple.<img src="http://help.openstreetmap.org/upfiles/Ipotesi_mappa_interattiva.jpg" alt="alt text" /></p>
<p>Best regards, Michele Fiaschi</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-healthstate" rel="tag" title="see questions tagged &#39;healthstate&#39;">healthstate</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jan '17, 00:05</strong></p>
<img src="https://secure.gravatar.com/avatar/b3104b16cf221fe323a08661f134887d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Michele%20Fiaschi&#39;s gravatar image" />
<p><span>Michele Fiaschi</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michele Fiaschi has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-53937" class="comments-container">
<span id="53938"></span>
<div id="comment-53938" class="comment">
<div id="post-53938-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>could you please tell us a bit more what you want to do? Do you search for a specific tag (maybe opening_hours, <a href="https://wiki.openstreetmap.org/wiki/Lifecycle_prefix">lifecycle prefixes</a>, ...) or are you asking how to change colours of symbols on a rendered map?</p>
<p>What is the motivation of your question?</p>
<p>A very quick way would be a overpass turbo query and css to style the icons.</p>
</div>
<div id="comment-53938-info" class="comment-info">
<span class="comment-age">(09 Jan '17, 06:52)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-53937" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53937-form-container" class="comment-form-container">
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

<span id="53943"></span>

<div id="answer-container-53943" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53943-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-53943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The quick answer is probably not. I do not believe that this type of information is widely or consistently stored in OpenStreetMap.</p>
<p>The longer answer is that IF the information was collected it could be possible:</p>
<ul>
<li>In the UK some of us tag shops (really retail premises) which are empty with shop=vacant (your case 3).</li>
<li>For former retail premises (case 2) you would have to rely on the underlying building tags: building=retail with a separate building:use tag (see <a href="http://wiki.openstreetmap.org/wiki/Tag:building%3Dapartments#Converted_Buildings_used_as_Apartments">description</a> for residential apartments in buildings built for other purposes). This latter approach will not work for buildings which were not built as shops, but have been used as such.</li>
<li>Data on demolished retail premises is not stored in OSM.</li>
</ul>
<p>Overall this approach is more likely to work for very specific classes of retail premises. For instance pubs in Britain are usually <a href="http://sk53-osm.blogspot.co.uk/2013/06/vanishing-pubs.html">architecturally distinctive</a> even when used for something else. I've wondered in the past about tagging former corner shops as these are usually still recognisable long after they have been converted to pure residential use.</p>
<p>To summarise:</p>
<ul>
<li>Class one: (shop=* and not (shop=mall)) or (amenity in ('pharmacy')</li>
<li>Class two: (building in ('retail'...) and building:use not in ('retail'...)</li>
<li>Class three: shop=vacant</li>
</ul>
<p>There are likely to be a range of other tags which have similar meanings. As stated above the major issue is that much of this information will not have been mapped.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jan '17, 09:29</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-53943" class="comments-container">
&#10;</div>
<div id="comment-tools-53943" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53943-form-container" class="comment-form-container">
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

