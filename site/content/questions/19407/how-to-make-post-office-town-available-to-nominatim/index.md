+++
type = "question"
title = "How to make &quot;post office town&quot; available to nominatim?"
description = '''In the US, it is common for areas outside of any municipality (&quot;unincorporated areas&quot;) to have an address that is based on the town where the nearest post office is. For instance, addresses on Abilene Road near where I live would be listed as &quot;xxx Abilene Rd, Farmville, VA&quot;. As it stands, if you typ...'''
date = "2013-01-28T19:34:00Z"
lastmod = "2014-08-05T16:34:00Z"
weight = 19407
keywords = [ "boundary", "nominatim", "postcode", "address", "unincorporated" ]
aliases = [ "/questions/19407" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to make "post office town" available to nominatim?](/questions/19407/how-to-make-post-office-town-available-to-nominatim)

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
<span id="post-19407-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19407-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-19407-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In the US, it is common for areas outside of any municipality ("unincorporated areas") to have an address that is based on the town where the nearest post office is. For instance, addresses on <a href="https://www.openstreetmap.org/browse/way/20415635">Abilene Road</a> near where I live would be listed as "xxx Abilene Rd, Farmville, VA".</p>
<p>As it stands, if you type in that address on osm.org, you get nothing at all. If you happen to know the ins and outs of nominatim, and you happen to know the name of the county that the municipality is in, you could type "Abilene Road, Prince Edward" (but not "Prince Edward County"!) and it would find it. But that's not exactly very user-friendly (to say the least), and it's certainly not what arbitrary users are likely to type into the search field.</p>
<p>So I assume that what's needed here is a separate set of boundaries, that Nominatim knows about, that correspond to post office service areas but include the name of the town that the post office serves (and there's a lot of complexity there in terms of overlap with other named entities, like towns, cities, and counties). Does such a thing already exist? Should it? Does it fit within the existing framework (i.e. "add a new key-value pair") or would this require additional architecting for some reason I can't think of right now?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundary" rel="tag" title="see questions tagged &#39;boundary&#39;">boundary</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-postcode" rel="tag" title="see questions tagged &#39;postcode&#39;">postcode</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span> <span class="post-tag tag-link-unincorporated" rel="tag" title="see questions tagged &#39;unincorporated&#39;">unincorporated</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jan '13, 19:34</strong></p>
<img src="https://secure.gravatar.com/avatar/4a4c8a91603aa21e05f5a441d5c13f26?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="blahedo&#39;s gravatar image" />
<p><span>blahedo</span><br />
<span class="score" title="736 reputation points">736</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="blahedo has 2 accepted answers">50%</span></p>
</div>
</div>
<div id="comments-container-19407" class="comments-container">
<span id="19416"></span>
<div id="comment-19416" class="comment">
<div id="post-19416-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just a note that Ireland is another country affected by this "postal address != geographical address" post-office crazyness. I dont think we've tried tagging that fact anywhere in Ireland yet, though.</p>
</div>
<div id="comment-19416-info" class="comment-info">
<span class="comment-age">(29 Jan '13, 09:38)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="29129"></span>
<div id="comment-29129" class="comment">
<div id="post-29129-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I just ran across another question on essentially the same problem, which I'll crosslink here for future reference: <a href="/questions/24133/incorrect-city-name">https://help.openstreetmap.org/questions/24133/incorrect-city-name</a></p>
</div>
<div id="comment-29129-info" class="comment-info">
<span class="comment-age">(16 Dec '13, 19:20)</span> <span class="comment-user userinfo">blahedo</span>
</div>
</div>
</div>
<div id="comment-tools-19407" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19407-form-container" class="comment-form-container">
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

<span id="19414"></span>

<div id="answer-container-19414" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19414-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19414-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-19414-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you are able to define postal town boundaries they can be drawn as polygons I would suggest tagging them in a similar way to how some postal_codes have been imported (<a href="https://wiki.openstreetmap.org/wiki/Key:boundary">see here</a>). i.e. tag the relation type=boundary, boundary=postal_town</p>
<p>If you decide to go down this route you should:</p>
<p>1) discuss it with the USA mapping community to get consensus</p>
<p>2) document the boundary=postal_town tagging on the wiki</p>
<p>When there is a reasonable amount of data in the correct format hopefully nominatim can be modified to make use of the data but it is easier to do once there is test data available.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jan '13, 01:37</strong></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twain has 15 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-19414" class="comments-container">
&#10;</div>
<div id="comment-tools-19414" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19414-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="19412"></span>

<div id="answer-container-19412" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19412-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19412-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-19412-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Simply add an addr:city tag to your road to indicate the postal town. Nominatim will respect that, provided the road is not inside the boundaries of another town.</p>
<p>I'm not aware of any established tagging schema for mapping something like that as boundaries but there are no architectural reasons for not adding support for it to Nominatim, should one come into regular use.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jan '13, 22:35</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-19412" class="comments-container">
<span id="19476"></span>
<div id="comment-19476" class="comment">
<div id="post-19476-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I dont think that will work, asfar as I can see nomiatim does not care about addr:city. See <a href="http://nominatim.openstreetmap.org/details.php?place_id=70613583">http://nominatim.openstreetmap.org/details.php?place_id=70613583</a> as an example</p>
</div>
<div id="comment-19476-info" class="comment-info">
<span class="comment-age">(31 Jan '13, 01:27)</span> <span class="comment-user userinfo">tothod</span>
</div>
</div>
<span id="19479"></span>
<div id="comment-19479" class="comment">
<div id="post-19479-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>addr:city is indeed only taken into account if it is on the road. It will not work on individual nodes/ways for house numbers. This is due to the way Nominatim handles house numbers internally: they don't have their own address but simply reuse the one from their parent street.</p>
</div>
<div id="comment-19479-info" class="comment-info">
<span class="comment-age">(31 Jan '13, 06:31)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="28671"></span>
<div id="comment-28671" class="comment">
<div id="post-28671-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There is some conflicting advice being given on a related question ( <a href="/questions/28625/automatically-add-addrcity-tag-to-roads?">https://help.openstreetmap.org/questions/28625/automatically-add-addrcity-tag-to-roads?</a> ).</p>
</div>
<div id="comment-28671-info" class="comment-info">
<span class="comment-age">(01 Dec '13, 20:45)</span> <span class="comment-user userinfo">blahedo</span>
</div>
</div>
<span id="28701"></span>
<div id="comment-28701" class="comment">
<div id="post-28701-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Hello blahedi and lonvia,</p>
<p>addr:city should really NOT be tagged to a street!</p>
<p>Here in Germany we have postal_code=XXXX on some ways, that wa sthe "old" method to define where a street belongs to. But this schema is superseded due to boundary relations that define the area where a postal_code is valid.</p>
<p>So please don't change OSM tagging because Nominatim "needs" this.</p>
</div>
<div id="comment-28701-info" class="comment-info">
<span class="comment-age">(02 Dec '13, 19:50)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="28730"></span>
<div id="comment-28730" class="comment">
<div id="post-28730-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There are boundary relations that define the area where a postal_code is valid? Is a postal_code the same as an addr:postcode? This is helpful and sounds like it would be an answer to this question---could you formulate that into an answer (not just a comment)?</p>
</div>
<div id="comment-28730-info" class="comment-info">
<span class="comment-age">(03 Dec '13, 17:26)</span> <span class="comment-user userinfo">blahedo</span>
</div>
</div>
</div>
<div id="comment-tools-19412" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19412-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="35490"></span>

<div id="answer-container-35490" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35490-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35490-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35490-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Blahedo (or anyone else, for that matter),</p>
<p>Has there ever been a resolution for this problem? I ask because I've noticed it as well for many addresses.</p>
<p>--jack</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Aug '14, 04:33</strong></p>
<img src="https://secure.gravatar.com/avatar/b95d3c8204ce3675edc226a8a55b7067?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jack%20the%20Ripper&#39;s gravatar image" />
<p><span>Jack the Ripper</span><br />
<span class="score" title="280 reputation points">280</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jack the Ripper has one accepted answer">12%</span></p>
</div>
</div>
<div id="comments-container-35490" class="comments-container">
<span id="35491"></span>
<div id="comment-35491" class="comment">
<div id="post-35491-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Not that I can tell (including in the other two related questions that I cross-linked). Part of the problem here, I think, is that most of the technical competence is held by residents of countries with a more sane boundary system, who are having a hard time even understanding the question. :)</p>
</div>
<div id="comment-35491-info" class="comment-info">
<span class="comment-age">(04 Aug '14, 04:48)</span> <span class="comment-user userinfo">blahedo</span>
</div>
</div>
<span id="35500"></span>
<div id="comment-35500" class="comment">
<div id="post-35500-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dpostal_code">https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dpostal_code</a></p>
<p>Seems like the best solution in my opinion, with a name if it matches the postal code area. If not then create something similar like <em>boundary=postal_town</em> as pointed out in the other comment.</p>
</div>
<div id="comment-35500-info" class="comment-info">
<span class="comment-age">(04 Aug '14, 12:13)</span> <span class="comment-user userinfo">AndiG88</span>
</div>
</div>
<span id="35535"></span>
<div id="comment-35535" class="comment">
<div id="post-35535-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah...the hard part will be figuring out exactly where the boundary is. I know it for some streets, but there are thousands of them in unincorporated areas of the county. :-( Me no likey this answer.</p>
</div>
<div id="comment-35535-info" class="comment-info">
<span class="comment-age">(05 Aug '14, 16:34)</span> <span class="comment-user userinfo">Jack the Ripper</span>
</div>
</div>
</div>
<div id="comment-tools-35490" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35490-form-container" class="comment-form-container">
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

