+++
type = "question"
title = "Mapping Kuwait subdvisions problems"
description = '''I&#x27;m currently mapping Kuwait. However, Kuwait subdivions are a little troublesome for mapping:  Kuwait is divided to six governorates (province is used on OSM for that), this is not a big deal. Governorates are divided to areas. Areas are not big at all (a typical area is normally no more than 5KM2 ...'''
date = "2015-08-12T14:43:00Z"
lastmod = "2015-08-14T07:34:00Z"
weight = 44736
keywords = [ "kuwait", "admin_level" ]
aliases = [ "/questions/44736" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mapping Kuwait subdvisions problems](/questions/44736/mapping-kuwait-subdvisions-problems)

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
<span id="post-44736-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44736-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-44736-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm currently mapping Kuwait. However, Kuwait subdivions are a little troublesome for mapping:</p>
<ul>
<li>Kuwait is divided to six governorates (province is used on OSM for that), this is not a big deal.</li>
<li>Governorates are divided to <em>areas</em>. Areas are not big at all (a typical area is normally no more than 5KM2 in size). Area names are not repeated (not used for more than one time for one place only) across the whole country. I don't know what to call them in OSM. I used <code>place=city</code> for now.</li>
<li><p>The real problem is with the blocks. So each area is divided to blocks. Blocks <em>need</em> to be included in the address, because streets can be repeated across all blocks. For example, we have:</p>
<ul>
<li>House 18, Street 1, Block 1, Jabriya, Kuwait</li>
<li>House 18, Street 1, Block 2, Jabriya, Kuwait</li>
<li>House 18, Street 1, Block 3, Jabriya, Kuwait</li>
<li>House 18, Street 1, Block 4, Jabriya, Kuwait</li>
</ul>
<p>etc... I need a solution that will show <em>both</em> the block number and the area name in addresses, and how should I tag the blocks and how should I tag areas? Please keep in mind that mentioning the governorate is not important at all and mentioning the governorate after the area is not normal and not used locally.</p></li>
</ul>
<p>Note: this question was asked before but one year ago but no answer was given.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-kuwait" rel="tag" title="see questions tagged &#39;kuwait&#39;">kuwait</span> <span class="post-tag tag-link-admin_level" rel="tag" title="see questions tagged &#39;admin_level&#39;">admin_level</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Aug '15, 14:43</strong></p>
<img src="https://secure.gravatar.com/avatar/404941922cbd5a6c25f206e88eeb734d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kuwaity26&#39;s gravatar image" />
<p><span>Kuwaity26</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kuwaity26 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-44736" class="comments-container">
<span id="44743"></span>
<div id="comment-44743" class="comment">
<div id="post-44743-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So you say: I need a solution that will show both the block number and the area name in addresses.</p>
<p>Where does this "show" take place? as a result on any geocoding service like the ones listet at <a href="http://wiki.openstreetmap.org/wiki/Search_engines">http://wiki.openstreetmap.org/wiki/Search_engines</a> ?</p>
<p>And about correct tagging of each house with an address: I think we need looking at <a href="http://wiki.openstreetmap.org/wiki/Addresses">http://wiki.openstreetmap.org/wiki/Addresses</a> and <a href="http://wiki.openstreetmap.org/wiki/Key:addr">http://wiki.openstreetmap.org/wiki/Key:addr</a></p>
<p>There we have tags like addr:suburb, addr:district or addr:subdistrict</p>
<p>Can that be helpful?</p>
</div>
<div id="comment-44743-info" class="comment-info">
<span class="comment-age">(12 Aug '15, 16:59)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="44744"></span>
<div id="comment-44744" class="comment">
<div id="post-44744-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>and <a href="https://osm.wno-edv-service.de/boundaries/?zoom=8&amp;lat=29.29514&amp;lon=47.82471&amp;layers=0BT&amp;selected=305099_4579477_4579478_4579479_4579480_4579481_4579482_2649754">here</a> you can see what boundaries are present at the moment inside the OSM database.</p>
</div>
<div id="comment-44744-info" class="comment-info">
<span class="comment-age">(12 Aug '15, 17:01)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="44745"></span>
<div id="comment-44745" class="comment">
<div id="post-44745-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/99/stephan75"></a><a href="http://help.openstreetmap.org/users/99/stephan75">@Stephan75</a> That's what I am trying to achieve. As for your second comment, I was thinking about services like Mapquest, when the user righ-clicks somewhere, the pop-up will tell them that they're in Street X, Area, Governorate, Kuwait, which wouldn't be much useful. If we could remove the governorate and put the block number before the area that'd be problem solved.</p>
</div>
<div id="comment-44745-info" class="comment-info">
<span class="comment-age">(12 Aug '15, 18:01)</span> <span class="comment-user userinfo">Kuwaity26</span>
</div>
</div>
<span id="44746"></span>
<div id="comment-44746" class="comment">
<div id="post-44746-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If I put areas as districts and blocks as subdistrict, will that solve the problem? I mean will they <em>both</em> show when the user do as in the previous example? because AFAIK, they only show the city (or its equivalent) and the province (and it's equivalent). I really don't care about naming, I just want the end user to get a good result if he wants to know about his location.</p>
</div>
<div id="comment-44746-info" class="comment-info">
<span class="comment-age">(12 Aug '15, 18:10)</span> <span class="comment-user userinfo">Kuwaity26</span>
</div>
</div>
<span id="44747"></span>
<div id="comment-44747" class="comment">
<div id="post-44747-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If that doesn't work and the block doesn't show on the results, can we just make each area a province and each block a town/city? it's of course wrong, technically speaking, but it'll finally show the two important fields <em>AND</em> make the unnecessary province (governorate) field not show up. The naming may be wrong but the most important thing is the end result for the user.</p>
</div>
<div id="comment-44747-info" class="comment-info">
<span class="comment-age">(12 Aug '15, 18:13)</span> <span class="comment-user userinfo">Kuwaity26</span>
</div>
</div>
<span id="44749"></span>
<div id="comment-44749" class="comment not_top_scorer">
<div id="post-44749-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>An approach used by HERE maps is labeling each block with it's area name. So for Rumaithiya, which consists of 12 blocks, there is twelve entries called Rumaithiya-Block 1, Rumaithiya-Block 2...etc. This approach surely fixes the problem, but it will make searching for the area without a specific block show 12 results instead of just one, and will make the map appear very congested, as showing the area name+block+number will take too much space on the map.</p>
</div>
<div id="comment-44749-info" class="comment-info">
<span class="comment-age">(12 Aug '15, 18:19)</span> <span class="comment-user userinfo">Kuwaity26</span>
</div>
</div>
</div>
<div id="comment-tools-44736" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-44736-form-container" class="comment-form-container">
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

<span id="44762"></span>

<div id="answer-container-44762" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-44762-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44762-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44762-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://wiki.openstreetmap.org/wiki/Tag%3Aplace%3Dcity_block">place=city_block</a> has <a href="http://taginfo.openstreetmap.org/tags/place=city_block#overview">some usage</a> (~4000). People have sometimes used it as a point, sometimes as an area. It's not clear to me how/if Nominatim or the standard rendering handle it. But it seems most important to get the data in, then you can figure out the rest.</p>
<p>On a related note, <a href="http://taginfo.openstreetmap.org/keys/addr%3Ablock_number">addr:block_number</a> is used quite a bit (~20K) in Japan on individual addresses.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Aug '15, 14:31</strong></p>
<img src="https://secure.gravatar.com/avatar/cebf8499a8a3009705e261cfd224e8c0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="neuhausr&#39;s gravatar image" />
<p><span>neuhausr</span><br />
<span class="score" title="7460 reputation points"><span>7.5k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="70 badges"><span class="silver">●</span><span class="badgecount">70</span></span><span title="121 badges"><span class="bronze">●</span><span class="badgecount">121</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="neuhausr has 36 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-44762" class="comments-container">
<span id="44767"></span>
<div id="comment-44767" class="comment">
<div id="post-44767-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I'll try them and see if they (block numbers) show on the map, and if they show when righ-clicking on a Mapquest location.</p>
</div>
<div id="comment-44767-info" class="comment-info">
<span class="comment-age">(14 Aug '15, 07:34)</span> <span class="comment-user userinfo">Kuwaity26</span>
</div>
</div>
</div>
<div id="comment-tools-44762" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44762-form-container" class="comment-form-container">
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

