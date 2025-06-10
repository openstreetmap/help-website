+++
type = "question"
title = "Strange about nominatim OSM data"
description = '''Hi I&#x27;m using OSM in my project&#x27;s and somhow confused about it&#x27;s functionality. My issue is: I&#x27;m using the &quot;OSM Nominatim data&quot; whit ability to click on map and get location information. What i&#x27;m intresting of, is the (for me) basic information &quot;Street and Street number&quot; when i click on a location on...'''
date = "2017-03-08T19:56:00Z"
lastmod = "2017-03-10T00:22:00Z"
weight = 54996
keywords = [ "strange" ]
aliases = [ "/questions/54996" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Strange about nominatim OSM data](/questions/54996/strange-about-nominatim-osm-data)

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
<span id="post-54996-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54996-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54996-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I'm using OSM in my project's and somhow confused about it's functionality.</p>
<p>My issue is:</p>
<p>I'm using the "OSM Nominatim data" whit ability to click on map and get location information.</p>
<p>What i'm intresting of, is the (for me) basic information "Street and Street number" when i click on a location on the map.</p>
<p>This works perfektly for me at 90% of all cases, but if someone has added (for example) a store name or other (for my mind) overlayed information.... The basic street name and number will not be gathered !! Instead i get location information... THE STORE NAME !?</p>
<p>Aint this a fundamental OSM - BAsic Information Prioryty ERROR ??</p>
<p>BeRg /MA</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-strange" rel="tag" title="see questions tagged &#39;strange&#39;">strange</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Mar '17, 19:56</strong></p>
<img src="https://secure.gravatar.com/avatar/5b3b08eb1c80226c54dfecfc0b21b758?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="G2Map&#39;s gravatar image" />
<p><span>G2Map</span><br />
<span class="score" title="9 reputation points">9</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="G2Map has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54996" class="comments-container">
&#10;</div>
<div id="comment-tools-54996" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54996-form-container" class="comment-form-container">
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

<span id="54997"></span>

<div id="answer-container-54997" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54997-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54997-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-54997-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim is not limited to address lookups; it tries to describe as good as possible the coordinate pair that you input. If the coordinate pair refers to a bus stop or a shop, Nominiatim will give you that information. To a degree you can influence the search by specifying a "zoom" parameter in your search.</p>
<p>If your use case calls for an address-only search engine, you can download the Nominatim source code, install it on your own server, load the OSM data, and modify the code to return only the information that you need for your projects.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Mar '17, 20:14</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-54997" class="comments-container">
<span id="54998"></span>
<div id="comment-54998" class="comment">
<div id="post-54998-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for understanding my answer "FR".</p>
<p>I still think this is strange....</p>
<p>The factum that "we can't determine" In the Nominative functionality what info level we want iformation about. Ex. (Streeet / Number) or (Store / Citisen).</p>
<p>What do Y Think ?</p>
<p>I might go som lesson with Y here :)</p>
<p>/MA</p>
</div>
<div id="comment-54998-info" class="comment-info">
<span class="comment-age">(08 Mar '17, 20:44)</span> <span class="comment-user userinfo">G2Map</span>
</div>
</div>
</div>
<div id="comment-tools-54997" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54997-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55001"></span>

<div id="answer-container-55001" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55001-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55001-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55001-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have tried the following two queries on nominatim</p>
<ol>
<li><a href="http://nominatim.openstreetmap.org/search.php?q=Keurslager+De+roeck&amp;polygon=1&amp;viewbox=">http://nominatim.openstreetmap.org/search.php?q=Keurslager+De+roeck&amp;polygon=1&amp;viewbox=</a></li>
<li><a href="http://nominatim.openstreetmap.org/search.php?q=kreatos%2C+reet&amp;polygon=1&amp;viewbox=">http://nominatim.openstreetmap.org/search.php?q=kreatos%2C+reet&amp;polygon=1&amp;viewbox=</a></li>
</ol>
<p>In both cases it returns the complete address. In the first case, the address information is on the building in which the POI is placed, in the second case on the POI itself.</p>
<p>Can you show us the node on which the lookup does not work. Perhaps the address information is not in the OSM database. Addresss information is not complete in OSM. So maybe it is just a missing address ?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Mar '17, 04:28</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-55001" class="comments-container">
<span id="55006"></span>
<div id="comment-55006" class="comment">
<div id="post-55006-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi "escada" and thanks for your responce.</p>
<p>Sice i'm programing, I use the XML responce facility and reverse geocoding function by lat and lon cords.</p>
<p>Y can get info about this facility at link: <a href="http://wiki.openstreetmap.org/wiki/Nominatim#Reverse_Geocoding">http://wiki.openstreetmap.org/wiki/Nominatim#Reverse_Geocoding</a></p>
<p>If You try this link, You will get a XML responce to your browser that demonstrate my issue:</p>
<p><a href="http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=59.3023449&amp;lon=18.1243585&amp;zoom=18&amp;addressdetails=1">http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=59.3023449&amp;lon=18.1243585&amp;zoom=18&amp;addressdetails=1</a></p>
<p>The request respond: ... &lt;building&gt;Sickla Fritidsgård&lt;/building&gt; &lt;road&gt;Sickla Strand&lt;/road&gt; ...</p>
<p>But I think it should respond: ... &lt;house_number&gt;68&lt;/house_number&gt; &lt;road&gt;Sickla Strand&lt;/road&gt; ...</p>
<p>Why is it responding building when pointing at number 68 ?? /MA</p>
</div>
<div id="comment-55006-info" class="comment-info">
<span class="comment-age">(09 Mar '17, 09:45)</span> <span class="comment-user userinfo">G2Map</span>
</div>
</div>
<span id="55007"></span>
<div id="comment-55007" class="comment">
<div id="post-55007-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Nominatim cannot respond with the house number 68 because the house number is a node (not on the way representing the building).</p>
<p>Nominatim never brings house numbers of individual nodes on to the building level, even when the node belongs to the contour (or way) of the building. So as far as Nominatim is concerned, the building has no house number. Hence any point within the building will have no house number.</p>
<p>Nominatim will bring any address information on the way of the building to nodes included inside the building though. However, some countries (Denmark, The Netherlands) only have address points, which makes Nominatim less useful in your case.</p>
</div>
<div id="comment-55007-info" class="comment-info">
<span class="comment-age">(09 Mar '17, 09:53)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="55008"></span>
<div id="comment-55008" class="comment">
<div id="post-55008-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thnk's for a god explanation "escada".</p>
<p>/MA</p>
</div>
<div id="comment-55008-info" class="comment-info">
<span class="comment-age">(09 Mar '17, 09:59)</span> <span class="comment-user userinfo">G2Map</span>
</div>
</div>
</div>
<div id="comment-tools-55001" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55001-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55009"></span>

<div id="answer-container-55009" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55009-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55009-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-55009-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Is there any way to get a XML responce with node information only (= only nearest roadnumber and street) whitout installing the sourcecode ??</p>
<p>/MA</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Mar '17, 10:08</strong></p>
<img src="https://secure.gravatar.com/avatar/5b3b08eb1c80226c54dfecfc0b21b758?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="G2Map&#39;s gravatar image" />
<p><span>G2Map</span><br />
<span class="score" title="9 reputation points">9</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="G2Map has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Mar '17, 10:37</strong> </span></p>
</div>
</div>
<div id="comments-container-55009" class="comments-container">
<span id="55010"></span>
<div id="comment-55010" class="comment">
<div id="post-55010-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have no idea, but it even when it is possible, it might return the wrong number for your building, the numbers on the other side of the street might be closer than the 68, which is on the top right corner.</p>
<p>(for the other readers, this is the area: ww.openstreetmap.org/#map=19/59.30235/18.12402&amp;layers=N )</p>
</div>
<div id="comment-55010-info" class="comment-info">
<span class="comment-age">(09 Mar '17, 11:00)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="55015"></span>
<div id="comment-55015" class="comment">
<div id="post-55015-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>meta: please could you have a look at <span>faq</span> and try to stick to the format of this site? If this is a new question, please ask as a new question. If it is a clarification question regarding an answer, please use "add as comment".</p>
</div>
<div id="comment-55015-info" class="comment-info">
<span class="comment-age">(10 Mar '17, 00:22)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-55009" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55009-form-container" class="comment-form-container">
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

