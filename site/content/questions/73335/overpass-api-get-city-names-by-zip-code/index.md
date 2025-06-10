+++
type = "question"
title = "Overpass API: Get city names by zip code"
description = '''Hello! Is there a way to get all city names by zip codes? Thanks in advance for your help.'''
date = "2020-03-03T16:46:00Z"
lastmod = "2020-03-17T17:34:00Z"
weight = 73335
keywords = [ "openstreetmap", "overpass", "germany" ]
aliases = [ "/questions/73335" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass API: Get city names by zip code](/questions/73335/overpass-api-get-city-names-by-zip-code)

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
<span id="post-73335-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73335-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73335-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello!</p>
<p>Is there a way to get all city names by zip codes?</p>
<p>Thanks in advance for your help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-germany" rel="tag" title="see questions tagged &#39;germany&#39;">germany</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Mar '20, 16:46</strong></p>
<img src="https://secure.gravatar.com/avatar/4a1005d44d537160f06ec9789ac121f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vielhuber&#39;s gravatar image" />
<p><span>vielhuber</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vielhuber has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Mar '20, 15:16</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span></p>
</div>
</div>
<div id="comments-container-73335" class="comments-container">
<span id="73337"></span>
<div id="comment-73337" class="comment">
<div id="post-73337-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you tell us more about what goal you're trying to reach? Do you have ZIP codes and you want to identify the city in which they're each located? Keep in mind that while some parts of the US may have more ZIP codes mapped, other parts might not have any.</p>
</div>
<div id="comment-73337-info" class="comment-info">
<span class="comment-age">(03 Mar '20, 20:58)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="73340"></span>
<div id="comment-73340" class="comment">
<div id="post-73340-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello! That's exactly the goal: Provice a single zip code and get all cities that have that zip code. I don't mind if the results may vary (in Germany, I think the results are quite good). From a query standpoint I thing I need: Get the area A for that zip code and get all areas of type city where area A is inside.</p>
</div>
<div id="comment-73340-info" class="comment-info">
<span class="comment-age">(03 Mar '20, 21:07)</span> <span class="comment-user userinfo">vielhuber</span>
</div>
</div>
<span id="73341"></span>
<div id="comment-73341" class="comment">
<div id="post-73341-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You mean in the whole world ? Or find city names for a specific zip code ?</p>
<p>BTW <a href="https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service">Wikidata</a> might be a better source for this. See for example <a href="https://www.wikidata.org/wiki/Wikidata:Request_a_query/Archive/2020/02#Communes_de_France">this discussion</a>.</p>
</div>
<div id="comment-73341-info" class="comment-info">
<span class="comment-age">(03 Mar '20, 21:31)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="73342"></span>
<div id="comment-73342" class="comment">
<div id="post-73342-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I mean: "Find city names for a specific zip code". I would prefer openstreetmap with overpass.</p>
</div>
<div id="comment-73342-info" class="comment-info">
<span class="comment-age">(03 Mar '20, 21:46)</span> <span class="comment-user userinfo">vielhuber</span>
</div>
</div>
<span id="73343"></span>
<div id="comment-73343" class="comment">
<div id="post-73343-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry I did not refresh, so I did see the previous comments ! ;-) I'll try to answer.</p>
</div>
<div id="comment-73343-info" class="comment-info">
<span class="comment-age">(03 Mar '20, 21:53)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-73335" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73335-form-container" class="comment-form-container">
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

<span id="73344"></span>

<div id="answer-container-73344" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-73344-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73344-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73344-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>See this <a href="https://overpass-turbo.eu/s/Rh2">query</a>.</p>
<p>The tilde (~) is necessary because there are several postcodes for this city, separated by semicolons.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Mar '20, 21:57</strong></p>
<img src="https://secure.gravatar.com/avatar/9434692e9afccaf03af5acf20b3a3279?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="H_mlet&#39;s gravatar image" />
<p><span>H_mlet</span><br />
<span class="score" title="5443 reputation points"><span>5.4k</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="81 badges"><span class="bronze">●</span><span class="badgecount">81</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="H_mlet has 40 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-73344" class="comments-container">
<span id="73346"></span>
<div id="comment-73346" class="comment">
<div id="post-73346-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello! Thanks for your answer. Unfortunately I get an empty result, tried several prominent zip codes from germany.</p>
</div>
<div id="comment-73346-info" class="comment-info">
<span class="comment-age">(03 Mar '20, 22:23)</span> <span class="comment-user userinfo">vielhuber</span>
</div>
</div>
<span id="73352"></span>
<div id="comment-73352" class="comment">
<div id="post-73352-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>it's normal that you get an empty result in Germany. The postal codes are not mapped on the city. They are mapped as separate boundaries.</p>
</div>
<div id="comment-73352-info" class="comment-info">
<span class="comment-age">(04 Mar '20, 04:06)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="73367"></span>
<div id="comment-73367" class="comment">
<div id="post-73367-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry, I forgot that on some tricky points, standards vary widely.</p>
<p>You can use this <a href="http://overpass-turbo.eu/s/RiE">query</a>, to find the relation of a postcode, and in the note tag you have the name of the associated place (I guess, it's not documented anywhere).</p>
<p>With this <a href="http://overpass-turbo.eu/s/RiG">other query</a>, you'll get all the place nodes inside the postal code area. Trouble is I don't understand how a city is tagged in Germany. And anyway a place=city node will be only in one postal code area, leaving the others empty.</p>
<p>You could ask on the german forum for more localized help.</p>
<p>Regards.</p>
</div>
<div id="comment-73367-info" class="comment-info">
<span class="comment-age">(04 Mar '20, 15:15)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
<span id="73577"></span>
<div id="comment-73577" class="comment">
<div id="post-73577-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello H_mlet,</p>
<p>thanks for your help! This is very helpful and interesting.</p>
<p>The thing is:</p>
<p>Cities are big areas with postal code areas inside. I think this must be a complex query (because we can only go the other way around).</p>
<p>Is this even possible with overpass turbo?</p>
</div>
<div id="comment-73577-info" class="comment-info">
<span class="comment-age">(17 Mar '20, 14:22)</span> <span class="comment-user userinfo">vielhuber</span>
</div>
</div>
<span id="73584"></span>
<div id="comment-73584" class="comment">
<div id="post-73584-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think that you can use <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Query_for_areas_.28is_in.29">is_in</a>. If the cities have a admin_level and a name attributes, they should be included in the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Areas">Area</a> definition of overpass.</p>
</div>
<div id="comment-73584-info" class="comment-info">
<span class="comment-age">(17 Mar '20, 17:34)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-73344" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73344-form-container" class="comment-form-container">
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

