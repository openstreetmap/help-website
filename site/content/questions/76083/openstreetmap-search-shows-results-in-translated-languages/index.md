+++
type = "question"
title = "OpenStreetmap search shows results in translated languages"
description = '''Hello, When I&#x27;m searching for any location in Republic of Moldova, although I write the name in the local language, the results are being shown in different translated languages. For exemple, if I search for a street &quot;Strada 31 August 1989, Bălți&quot;, the result is &quot;улица 31 Августа 1989, Берестечко, B...'''
date = "2020-08-09T16:16:00Z"
lastmod = "2020-08-11T18:06:00Z"
weight = 76083
keywords = [ "openstreetmap", "romanian", "search", "language", "moldova" ]
aliases = [ "/questions/76083" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [OpenStreetmap search shows results in translated languages](/questions/76083/openstreetmap-search-shows-results-in-translated-languages)

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
<span id="post-76083-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76083-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76083-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>When I'm searching for any location in Republic of Moldova, although I write the name in the local language, the results are being shown in different translated languages.</p>
<p>For exemple, if I search for a street "Strada 31 August 1989, Bălți", the result is "улица 31 Августа 1989, Берестечко, Bălți Municipality, MD-3110, Moldavie" because the location and the neighborhood have a "name:ru" tag, and the city is shown in "name:en" while the country in "name:fr". Why is this happening and how to fix that ?</p>
<p>A solution was adding the local language key "name:ro". This solved my problem for the street, but it's the same for the neighborhood and the country.</p>
<p>In this case, if I write "Strada 31 August 1989, Chișinău", since it has the "name:ro", the result is "Strada 31 August 1989, Historical Centre, Chișinău, Municipalité de Chișinău, MD-2012, Moldavie" with the neighborhood being syill showed in English this time and the municipality and the country in French.</p>
<p>I think for both cases, the result should be seen in local language, unless I set a specific order of languages in my profile. Is this a bug or I'm using wrong OSM ?</p>
<p>Note: Adding name:ro is seen bad by other editor as he calls the local language "Romanian" with "Moldovan" and he also adds the wrong tag "name:mo" or "name:md" (the ISO 639-1 code is "ro" and there is no "mo" or "md" existing code as there is no such language). Also, the OpenStreetMap <a href="https://wiki.openstreetmap.org/wiki/Multilingual_names">Multilingual</a> wiki shows the exemple of France or Romania where only name: <em>is used without name:fr:</em> or name:ro:* although the <a href="https://wiki.openstreetmap.org/wiki/Names#Repeating_name_with_language_specific_tag">Names#Repeating_name_with_language_specific_tag</a> page encourages it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-romanian" rel="tag" title="see questions tagged &#39;romanian&#39;">romanian</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-language" rel="tag" title="see questions tagged &#39;language&#39;">language</span> <span class="post-tag tag-link-moldova" rel="tag" title="see questions tagged &#39;moldova&#39;">moldova</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Aug '20, 16:16</strong></p>
<img src="https://secure.gravatar.com/avatar/5ca9ef508a6a0ff5c4d9c925a57269ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="VitalieS&#39;s gravatar image" />
<p><span>VitalieS</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="VitalieS has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Aug '20, 16:59</strong> </span></p>
</div>
</div>
<div id="comments-container-76083" class="comments-container">
<span id="76103"></span>
<div id="comment-76103" class="comment">
<div id="post-76103-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is this on the main site?</p>
</div>
<div id="comment-76103-info" class="comment-info">
<span class="comment-age">(11 Aug '20, 17:46)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="76104"></span>
<div id="comment-76104" class="comment">
<div id="post-76104-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/4426/insertuser">@InsertUser</a>, Yes, either when searching on view mode (<a href="https://www.openstreetmap.org/search?query=Strada%2031%20august%201989%2C%20Balti#map=19/47.75178/27.93476)">https://www.openstreetmap.org/search?query=Strada%2031%20august%201989%2C%20Balti#map=19/47.75178/27.93476)</a> or iD browser modify mode (<a href="https://www.openstreetmap.org/edit#map=19/47.75178/27.93476)">https://www.openstreetmap.org/edit#map=19/47.75178/27.93476)</a></p>
</div>
<div id="comment-76104-info" class="comment-info">
<span class="comment-age">(11 Aug '20, 18:06)</span> <span class="comment-user userinfo">VitalieS</span>
</div>
</div>
</div>
<div id="comment-tools-76083" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76083-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

