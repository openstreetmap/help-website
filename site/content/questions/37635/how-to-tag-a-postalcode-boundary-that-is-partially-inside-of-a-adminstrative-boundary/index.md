+++
type = "question"
title = "[closed] How to tag a postalcode boundary that is partially inside of a adminstrative boundary?"
description = '''In York County, PA, there is a township called York Township. York Township has multiple postal (zip) codes, and not all of them are York (city) post codes. For example, some of the houses and roads in York Township have an 17313 postcode of the nearby borough of Dallastown, PA. Another part of the ...'''
date = "2014-10-16T02:57:00Z"
lastmod = "2014-10-21T21:39:00Z"
weight = 37635
keywords = [ "pennsylvania", "township", "nominatim", "addressing" ]
aliases = [ "/questions/37635" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] How to tag a postalcode boundary that is partially inside of a adminstrative boundary?](/questions/37635/how-to-tag-a-postalcode-boundary-that-is-partially-inside-of-a-adminstrative-boundary)

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
<span id="post-37635-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37635-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37635-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In York County, PA, there is a township called York Township. York Township has multiple postal (zip) codes, and not all of them are York (city) post codes. For example, some of the houses and roads in York Township have an 17313 postcode of the nearby borough of Dallastown, PA. Another part of the township has a 17356 postcode of the nearby borough of Red Lion, PA. However, all of these addresses are actually in York Township. The only problem is that since a township boundary (admin level 8 for PA) has a higher priority over the postal boundary, Nominatim overrides my postal boundaries for Dallastown and Red Lion and returns incorrect address results:</p>
<p>Like for example: 123 Example St, York Township, York County, PA 17313, but it should say</p>
<p>123 Example St, Dallastown, York County, PA 17313 even though the address is in York Township.</p>
<p>How can I adjust tagging of the 17313 and 17356 postal code boundaries so that the actual name of the postal code town shows up, not York Township (postal boundary has priority instead)?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pennsylvania" rel="tag" title="see questions tagged &#39;pennsylvania&#39;">pennsylvania</span> <span class="post-tag tag-link-township" rel="tag" title="see questions tagged &#39;township&#39;">township</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-addressing" rel="tag" title="see questions tagged &#39;addressing&#39;">addressing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Oct '14, 02:57</strong></p>
<img src="https://secure.gravatar.com/avatar/a857d096efae972b1284159a0eeed8e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="elite_mapper&#39;s gravatar image" />
<p><span>elite_mapper</span><br />
<span class="score" title="9 reputation points">9</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="elite_mapper has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>21 Oct '14, 21:43</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-37635" class="comments-container">
&#10;</div>
<div id="comment-tools-37635" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37635-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "regarded as "solved" by the questioner. Also see the self-answer." by aseerel4c26 21 Oct '14, 21:43

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="37820"></span>

<div id="answer-container-37820" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37820-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37820-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-37820-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That is a bad idea. Do not misuse tags just to get your address shown correctly in Nominatim. If you come across a new concept while mapping, like postal towns, then you should invent a new tag and discuss it with the community to get a consensus on how to use the tag. Once that is done you can approach the developers of the software and ask to have the new tag implemented.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Oct '14, 07:20</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-37820" class="comments-container">
&#10;</div>
<div id="comment-tools-37820" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37820-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="37653"></span>

<div id="answer-container-37653" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37653-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37653-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-37653-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>US Postal code boundaries are not kept in OSM, because there really aren't postal code area boundaries in the US. <a href="http://en.wikipedia.org/wiki/ZIP_code">ZIP codes</a> are technically collections of routes, so they're line, or in some cases, point data. Postal_code is definitely used on buildings/POIs in the US, though. The US Census produces ZCTA (Zip Code Tabulation Area) data, but these are just approximations of postal code boundaries.</p>
<p>This question is really an issue with the <a href="https://wiki.openstreetmap.org/wiki/Nominatim">Nominatim</a> processing. Nominatim is what powers the OSM place search, and while it uses OSM data, it also uses other data too. Look up the <a href="https://help.openstreetmap.org/tags/nominatim/">nominatim</a> tag here in the forum, and you'll see many similar questions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Oct '14, 16:49</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Oct '14, 17:38</strong> </span></p>
</div>
</div>
<div id="comments-container-37653" class="comments-container">
<span id="37655"></span>
<div id="comment-37655" class="comment">
<div id="post-37655-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>But YES we have postalcode boundaries in OSM!</p>
<p>Try for a part of Germany in the Wizard of <a href="http://overpass-turbo.eu">http://overpass-turbo.eu</a> :</p>
<p>boundary=postal_code and type:relation in saarland</p>
<p>But I am not sure how we can adapt the tagging of those "clear and simple" postalcode areas on other countries like USA.</p>
</div>
<div id="comment-37655-info" class="comment-info">
<span class="comment-age">(16 Oct '14, 16:57)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="37656"></span>
<div id="comment-37656" class="comment">
<div id="post-37656-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>oops, my bad, I'll revise to make my answer US-specific</p>
</div>
<div id="comment-37656-info" class="comment-info">
<span class="comment-age">(16 Oct '14, 17:29)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
</div>
<div id="comment-tools-37653" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37653-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="37852"></span>

<div id="answer-container-37852" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-37852-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-37852-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-37852-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><span class="small"><a href="https://help.openstreetmap.org/users/9825/elite_mapper"></a><a href="https://help.openstreetmap.org/users/9825/elite_mapper">@elite_mapper</a></a> provided an own answer (in revision 3 of the question text):</span></p>
<p>I added an <code>boundary=administrative</code> and <code>place=locality</code> tag to the postcode boundary so the addresses inside of it takes on whatever name of the postal town it it assigned to, like it is supposed to.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Oct '14, 21:39</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Oct '14, 21:39</strong> </span></p>
</div>
</div>
<div id="comments-container-37852" class="comments-container">
&#10;</div>
<div id="comment-tools-37852" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-37852-form-container" class="comment-form-container">
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

