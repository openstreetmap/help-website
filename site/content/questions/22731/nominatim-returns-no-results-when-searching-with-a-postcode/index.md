+++
type = "question"
title = "Nominatim returns no results when searching with a postcode"
description = '''I have just started using OpenStreetMap/Nominatim and I am struggling to understand what the current status of postcodes is, how they are used to find results, best practices and so on... For example, querying the following Northern Irish address returns a single accurate result: &quot;220 Ravenhill Aven...'''
date = "2013-05-24T15:50:00Z"
lastmod = "2020-08-25T11:06:00Z"
weight = 22731
keywords = [ "post", "nominatim", "geocoding", "postcode", "postcodes" ]
aliases = [ "/questions/22731" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim returns no results when searching with a postcode](/questions/22731/nominatim-returns-no-results-when-searching-with-a-postcode)

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
<span id="post-22731-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22731-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-22731-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have just started using OpenStreetMap/Nominatim and I am struggling to understand what the current status of postcodes is, how they are used to find results, best practices and so on...</p>
<p>For example, querying the following Northern Irish address returns a single accurate result: "220 Ravenhill Avenue, Belfast".</p>
<p>However, if I append the correct postcode to the query (either the full postcode or the first segment), no results are returned: "220 Ravenhill Avenue, Belfast, BT6 8LL" or "220 Ravenhill Avenue, Belfast, BT6"</p>
<p>I have encountered similar behaviour for a number of NI addresses but have noted that this isn't always the case when searching, for example, addresses in London.</p>
<ul>
<li>Is this the intended behaviour?</li>
<li>Can I assume from this that Postcode information for NI is simply incomplete?</li>
<li><strong>If so, is there somewhere I can go to see how complete postcode information for a particular area is?</strong></li>
<li>How are other people handling situations where they may have a list of addresses that require geocoding, all of which contain postcodes?</li>
</ul>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-post" rel="tag" title="see questions tagged &#39;post&#39;">post</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-postcode" rel="tag" title="see questions tagged &#39;postcode&#39;">postcode</span> <span class="post-tag tag-link-postcodes" rel="tag" title="see questions tagged &#39;postcodes&#39;">postcodes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 May '13, 15:50</strong></p>
<img src="https://secure.gravatar.com/avatar/ddd89dfcb11fb51df46979eefc69aef5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stevie&#39;s gravatar image" />
<p><span>Stevie</span><br />
<span class="score" title="76 reputation points">76</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stevie has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 May '13, 09:52</strong> </span></p>
</div>
</div>
<div id="comments-container-22731" class="comments-container">
<span id="22741"></span>
<div id="comment-22741" class="comment">
<div id="post-22741-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I entered a post code for a few houses where I live a few months ago. When I did a search with my post code, 7 characters no space. The result nominatim returned my street and others in the area that do not have that post code. Note the post codes were added to the house tags not the streets. This is a similar problem I found with town nodes (which spread out) compared to town boundaries (which worked). Tried again with same 7 characters with a space after 4th one and I only got one result to the search, a pointer near my house. with a source label NPEMap / FreeThe Postcode</p>
</div>
<div id="comment-22741-info" class="comment-info">
<span class="comment-age">(24 May '13, 19:13)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="22800"></span>
<div id="comment-22800" class="comment">
<div id="post-22800-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>4 days later and i only get the NPEMap / FreeThe Postcode result.</p>
</div>
<div id="comment-22800-info" class="comment-info">
<span class="comment-age">(28 May '13, 05:48)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-22731" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22731-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="22755"></span>

<div id="answer-container-22755" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22755-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22755-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22755-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Stevie,</p>
<p>Using Nominatim's map search site I searched for that address minus the postcode and this is the details page on that address <a href="http://nominatim.openstreetmap.org/details.php?place_id=24847069.">http://nominatim.openstreetmap.org/details.php?place_id=24847069.</a> There is no postcode nodes in that list which leads me to believe that your assumption is correct.</p>
<p>As for completeness of postcode information, I have no idea. My home city has no suburb boundaries or postcode boundaries. It appears it's rather difficult getting this information in a usable format, both technically and legally.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 May '13, 10:40</strong></p>
<img src="https://secure.gravatar.com/avatar/5f856e6a672fa11cd950852bf015b97c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Russkel&#39;s gravatar image" />
<p><span>Russkel</span><br />
<span class="score" title="161 reputation points">161</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Russkel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-22755" class="comments-container">
<span id="22780"></span>
<div id="comment-22780" class="comment">
<div id="post-22780-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Originally Nominatim used OS Open Data Code Point for postcode search, which did not contain any Northern Ireland postcodes. I suspect that it still does. The ONS postcode data set does contain Northern Ireland postcodes, but became available much more recently. Matt Williams' Postcode Finder is useful for checking postcodes in OSM <a href="http://milliams.dev.openstreetmap.org/postcodefinder/">http://milliams.dev.openstreetmap.org/postcodefinder/</a></p>
</div>
<div id="comment-22780-info" class="comment-info">
<span class="comment-age">(26 May '13, 12:15)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="22792"></span>
<div id="comment-22792" class="comment">
<div id="post-22792-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the reply <span>@Russkel</span>, I appreciate your help but I'm reluctant to mark your answer as accepted until the answer is clear.</p>
<p><span>@SK53</span> - are you saying that OSM is still using OS Open Data Code-Point? Where then, for example, is American post code information sourced? Surely there must be some sort of road map to show how complete this data is on a global scale? I would expect, with post code being such a vital part of an address, that it would be pivotal to ensure as much completeness of this information as possible? Especially in a Geocoding context.</p>
</div>
<div id="comment-22792-info" class="comment-info">
<span class="comment-age">(27 May '13, 12:04)</span> <span class="comment-user userinfo">Stevie</span>
</div>
</div>
<span id="22798"></span>
<div id="comment-22798" class="comment">
<div id="post-22798-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It entirely depends on the availability of suitable data sets (&amp; then the code &amp; other legwork to use them). Remember OSM is a project where the work is done by volunteers and handling a couple of hundred ways of doing it is a hard work. Adding postcodes to Northern Ireland data is a way which automatically helps the Nominatim results: whether from detailed survey, ONS data or using other address complete data sets such as the Food Hygiene Rating Scheme.</p>
</div>
<div id="comment-22798-info" class="comment-info">
<span class="comment-age">(27 May '13, 23:05)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="22805"></span>
<div id="comment-22805" class="comment">
<div id="post-22805-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span>@SK53</span> I absolutely understand Nominatim is an Open Source project - which is exactly why I'm confused that the information I'm looking for (i.e. the current coverage of postcode data) isn't readily available? Or any information pertaining to how much data a particular area/city/country has for that matter.</p>
<p>As a volunteer/contributor, how am I to know which areas need attention? Or as a Nominatim user, how am I to know which areas I can safely try to Geocode with a Postcode in the query?</p>
</div>
<div id="comment-22805-info" class="comment-info">
<span class="comment-age">(28 May '13, 09:43)</span> <span class="comment-user userinfo">Stevie</span>
</div>
</div>
<span id="22812"></span>
<div id="comment-22812" class="comment not_top_scorer">
<div id="post-22812-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Stevie</span> Being an open source project the available postcode data is available, it just takes some effort to turn it into the coverage data that you want. You're free to pitch the idea/raise an issue and maybe someone can code the tool up for us, or you could try your hand at it.</p>
</div>
<div id="comment-22812-info" class="comment-info">
<span class="comment-age">(28 May '13, 12:36)</span> <span class="comment-user userinfo">Russkel</span>
</div>
</div>
<span id="22816"></span>
<div id="comment-22816" class="comment not_top_scorer">
<div id="post-22816-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Russkel</span> Thank for you taking the time to get back to me; I appreciate all your help. After doing a bit of digging I'm beginning to think this should be raised as an issue - whether it's specifically a Nominatim issue or OSM, I think this information needs to exist somewhere.</p>
</div>
<div id="comment-22816-info" class="comment-info">
<span class="comment-age">(28 May '13, 14:24)</span> <span class="comment-user userinfo">Stevie</span>
</div>
</div>
<span id="22817"></span>
<div id="comment-22817" class="comment not_top_scorer">
<div id="post-22817-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Stevie</span>, it's my pleasure. I agree, I too would like to see proper suburb and postcode coverage in the areas I frequent. It's important for routing which I believe is one of the more impressive features that this open data lets us utilise.</p>
<p>But how post codes and suburb boundaries isn't public data released by Governments is beyond me and another topic altogether.</p>
</div>
<div id="comment-22817-info" class="comment-info">
<span class="comment-age">(28 May '13, 14:34)</span> <span class="comment-user userinfo">Russkel</span>
</div>
</div>
<span id="22818"></span>
<div id="comment-22818" class="comment">
<div id="post-22818-score" class="comment-score">
3
</div>
<div class="comment-text">
<p><span>@Stevie</span>, Nominatim as implemented is a address &amp; reverse geocode engine for OSM data, not necessarily just an OpenSource geocoder. It's efficiency will depend on the quality of data in OSM. A quick inspection of taginfo gb (<a href="http://taginfo.openstreetmap.org.uk/keys/addr%3Apostcode#overview">http://taginfo.openstreetmap.org.uk/keys/addr%3Apostcode#overview</a> sorry no NI) shows that there are 240k objects tagged addr:postcode with around 36k distinct values. compare this with around 27 million residential addresses in GB (OS GB data) and perhaps 2 million postcodes for the UK, and you can appreciate why it might be unusual for postcode searches to work.</p>
<p>The relevant data file is here <a href="https://github.com/twain47/Nominatim/tree/master/data">https://github.com/twain47/Nominatim/tree/master/data</a> and is loaded in php/utils. All code / data fixes welcome.</p>
</div>
<div id="comment-22818-info" class="comment-info">
<span class="comment-age">(28 May '13, 14:50)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="22820"></span>
<div id="comment-22820" class="comment not_top_scorer">
<div id="post-22820-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's great <span></span><span>@SK53</span> - TagInfo looks like what I've been looking for! Thank you.</p>
<p>Additionally, I believe the points you make highlight a problem with Nominatim. Clearly there is a need for a "best guess" based on what it <em>does</em> know. I would expect, if there is no post code data, that it would fall back and execute the query sans post code - not to fail altogether. Like <span></span><span>@Russkel</span> said, this is maybe something to raise as an issue.</p>
</div>
<div id="comment-22820-info" class="comment-info">
<span class="comment-age">(28 May '13, 15:05)</span> <span class="comment-user userinfo">Stevie</span>
</div>
</div>
</div>
<div id="comment-tools-22755" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-22755-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="22836"></span>

<div id="answer-container-22836" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22836-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22836-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22836-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><span><span>@SK53</span></span> and <span><span>@Russkel</span></span> really answered this in the comments of the other proposed answer, but for clarity, the approximate explanation/answer is as follows:</p>
<ul>
<li>Nominatim is based on the OSM data</li>
<li>OSM Post Code data is largely incomplete
<ul>
<li>The current status of Post Code data can be viewed on the <a href="http://taginfo.openstreetmap.org.uk/keys/addr%3Apostcode#overview">OSM TagInfo</a> website.</li>
</ul></li>
<li>Currently, if a Post Code is added to a Nominatim Query and the Post Code is not within the OSM data set, Nominatim will return <strong>no results</strong></li>
</ul>
<p>This appears to be the intended behaviour, which I believe to be wrong and have raised as an issue on Nominatim.</p>
<p><a href="https://trac.openstreetmap.org/ticket/4867">Issue on OSM Trac</a></p>
<p><a href="https://github.com/twain47/Nominatim/issues/59">Issue on Nominatim Github</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 May '13, 10:51</strong></p>
<img src="https://secure.gravatar.com/avatar/ddd89dfcb11fb51df46979eefc69aef5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stevie&#39;s gravatar image" />
<p><span>Stevie</span><br />
<span class="score" title="76 reputation points">76</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stevie has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 May '13, 16:44</strong> </span></p>
</div>
</div>
<div id="comments-container-22836" class="comments-container">
<span id="22860"></span>
<div id="comment-22860" class="comment">
<div id="post-22860-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just for the record, can you provide your ticket URL? It doesn't seem to exist <a href="http://trac.openstreetmap.org/query?status=new&amp;status=assigned&amp;status=reopened&amp;component=nominatim&amp;order=id&amp;desc=1">here</a>.</p>
</div>
<div id="comment-22860-info" class="comment-info">
<span class="comment-age">(29 May '13, 16:27)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="22861"></span>
<div id="comment-22861" class="comment">
<div id="post-22861-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Updated my answer to provide the ticket URL.</p>
</div>
<div id="comment-22861-info" class="comment-info">
<span class="comment-age">(29 May '13, 16:36)</span> <span class="comment-user userinfo">Stevie</span>
</div>
</div>
</div>
<div id="comment-tools-22836" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22836-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="22862"></span>

<div id="answer-container-22862" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22862-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22862-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22862-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim is not good at dropping terms because doing so makes the search graph very complex.</p>
<p>With regards to the specific issue of dropping postcodes from the search there is a chicken and egg problem - how does nominatim identify something as a postcode when the postcode isn't in the data?</p>
<p>Probably the suggestion would be some sort of regex matching but since postcodes follow a different format for every country this rapidly becomes a very difficult problem. At the moment the solution is that we ignore the whole issue and just find what is in the data and leave this as a problem for the user.</p>
<p>This is a known issue with several tickets against it in one form or another but it will require significant developer time before it is solved.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 May '13, 17:32</strong></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twain has 15 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-22862" class="comments-container">
<span id="22866"></span>
<div id="comment-22866" class="comment">
<div id="post-22866-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Twain, just the guy! I apologise for digging up an already known issue. This place isn't really suited for discussion, is there another more suited place to discuss developer issues such as this?</p>
</div>
<div id="comment-22866-info" class="comment-info">
<span class="comment-age">(29 May '13, 18:02)</span> <span class="comment-user userinfo">Stevie</span>
</div>
</div>
<span id="22869"></span>
<div id="comment-22869" class="comment">
<div id="post-22869-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://lists.openstreetmap.org/pipermail/geocoding/2013-May/000819.html">http://lists.openstreetmap.org/pipermail/geocoding/2013-May/000819.html</a></p>
<p>But as I say this is a known issue - unless you are able to code a solution there may not be a lot of point to discussion. It is a question of developer time.</p>
</div>
<div id="comment-22869-info" class="comment-info">
<span class="comment-age">(29 May '13, 18:38)</span> <span class="comment-user userinfo">twain</span>
</div>
</div>
</div>
<div id="comment-tools-22862" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22862-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76286"></span>

<div id="answer-container-76286" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76286-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76286-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76286-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Not the answer but a work around. If i can't find a place using a post code search i do a street and town, some times country is needed as well. Zoom in and centre over the place. Next note down the URL ( it's at the top ) like this one <a href="https://www.openstreetmap.org/#map=19/52.32929/-0.18013">https://www.openstreetmap.org/#map=19/52.32929/-0.18013</a> The co-ords from that, 19 is the zoom level followed by co-ords 52.32929/-0.18013 N and W, NOTE negative - values are used for south and west. I can use these in most SatNavs and GPSes as long as you set the device to decimal degrees. DDD.ddddd. Check the place and map on Sat Nav before setting off, so that all looks correct!! I usually use the routing on OSM map page to get an idea of route and travelling time, as another confirmation.<br />
I have added a few Postcodes to the addresses of places that i have visited and have noticed a mapper who is working hard on this, so Post code coverage is improving.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Aug '20, 11:06</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span> </br></p>
</div>
</div>
<div id="comments-container-76286" class="comments-container">
&#10;</div>
<div id="comment-tools-76286" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76286-form-container" class="comment-form-container">
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

