+++
type = "question"
title = "City detail is missing from Nominatim query responses in Helsinki, Finland"
description = '''Hello! I have a problem the whole Helsinki city is missing in nominatim query responses. Someone in somewhere is switched isaddress boolean = false in city of Helsinki details and that could be the reason for that. Could someone advice me how to switch it back to true? I hope you have a nice day! Pe...'''
date = "2022-06-04T00:47:00Z"
lastmod = "2022-06-05T17:59:00Z"
weight = 84693
keywords = [ "city", "isaddress" ]
aliases = [ "/questions/84693" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [City detail is missing from Nominatim query responses in Helsinki, Finland](/questions/84693/city-detail-is-missing-from-nominatim-query-responses-in-helsinki-finland)

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
<span id="post-84693-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84693-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84693-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello!</p>
<p>I have a problem the whole Helsinki city is missing in nominatim query responses. Someone in somewhere is switched isaddress boolean = false in city of Helsinki details and that could be the reason for that. Could someone advice me how to switch it back to true?</p>
<p>I hope you have a nice day!</p>
<p>Peace &amp; happiness, always Ari</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-isaddress" rel="tag" title="see questions tagged &#39;isaddress&#39;">isaddress</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jun '22, 00:47</strong></p>
<img src="https://secure.gravatar.com/avatar/3d23564d397175b70be936844e1395e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="talousala&#39;s gravatar image" />
<p><span>talousala</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="talousala has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Jun '22, 22:56</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-84693" class="comments-container">
<span id="84694"></span>
<div id="comment-84694" class="comment">
<div id="post-84694-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could you explain in a bit more detail what seems to be the problem - what query you are actually executing and where?</p>
<p><a href="https://www.openstreetmap.org/search?whereami=1&amp;query=60.17063%2C24.93268">https://www.openstreetmap.org/search?whereami=1&amp;query=60.17063%2C24.93268</a></p>
<p>returns "Original Sokos Hotel Presidentti, 4, Eteläinen Rautatiekatu, Kamppi, Helsinki, Helsinki sub-region, Uusimaa, Southern Finland, Mainland Finland, 00100, Finland" for me, which seems correct?</p>
</div>
<div id="comment-84694-info" class="comment-info">
<span class="comment-age">(04 Jun '22, 01:05)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="84695"></span>
<div id="comment-84695" class="comment">
<div id="post-84695-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK. It looks like the whole Helsinki is not missing. E.g. address Iivarintie 3, Helsinki:</p>
<p><a href="https://nominatim.openstreetmap.org/search?q=Iivarintie+3,+Helsinki&amp;format=xml&amp;polygon_geojson=1&amp;addressdetails=1">https://nominatim.openstreetmap.org/search?q=Iivarintie+3,+Helsinki&amp;format=xml&amp;polygon_geojson=1&amp;addressdetails=1</a></p>
<p>place_id="123297206" have no &lt;city&gt; so that is wrong place_id="178976505" have &lt;city&gt; so that is correct</p>
<p>The problem is many places all around Helsinki area has similar problem the &lt;city&gt; data missing.</p>
<p>&lt;searchresults ...="" &lt;place="" place_id="123297206" ...="" &lt;house_number=""&gt;3&lt;/house_number&gt; &lt;road&gt;Iivarintie&lt;/road&gt; &lt;neighbourhood&gt;Puistola&lt;/neighbourhood&gt; &lt;suburb&gt;Suurmetsä&lt;/suburb&gt; &lt;city_district&gt;Northeastern major district&lt;/city_district&gt; &lt;municipality&gt;Helsinki sub-region&lt;/municipality&gt; &lt;county&gt;Uusimaa&lt;/county&gt; &lt;iso3166-2-lvl6&gt;FI-18&lt;/iso3166-2-lvl6&gt; &lt;state_district&gt;Southern Finland&lt;/state_district&gt; &lt;region&gt;Mainland Finland&lt;/region&gt; &lt;postcode&gt;00760&lt;/postcode&gt; &lt;country&gt;Finland&lt;/country&gt; &lt;country_code&gt;fi&lt;/country_code&gt; &lt;/place&gt;</p>
<p>&lt;place place_id="178976505" ...="" &lt;house_number=""&gt;3&lt;/house_number&gt; &lt;road&gt;Iivarintie&lt;/road&gt; &lt;neighbourhood&gt;Iivisniemi&lt;/neighbourhood&gt; &lt;suburb&gt;Kaitaa&lt;/suburb&gt; &lt;city_district&gt;Suur-Espoonlahti&lt;/city_district&gt; &lt;city&gt;Espoo&lt;/city&gt; ... &lt;/place&gt; &lt;/searchresults&gt;</p>
</div>
<div id="comment-84695-info" class="comment-info">
<span class="comment-age">(04 Jun '22, 01:38)</span> <span class="comment-user userinfo">talousala</span>
</div>
</div>
<span id="84697"></span>
<div id="comment-84697" class="comment">
<div id="post-84697-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse"></a><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>:</p>
<p>and your query example <a href="https://www.openstreetmap.org/search?whereami=1&amp;query=60.17063%2C24.93268">https://www.openstreetmap.org/search?whereami=1&amp;query=60.17063%2C24.93268</a> returns only Mainland Finland (so this relation: <a href="https://www.openstreetmap.org/relation/2375172">https://www.openstreetmap.org/relation/2375172</a> ) from here. So it looks like (at least) one of OpenStreetMaps Nominatim instances is having the problem...</p>
<p>Hm, I now checked pummelzacken, dulcy, longma, stormfly-04 separately and all return the Original Sokos Hotel, while using the search at www.openstreetmap.org (or your whereami link) only returns Mainland Finland.</p>
<p>And a few minutes later, the whereami link returns this relation: <a href="https://www.openstreetmap.org/relation/184714">https://www.openstreetmap.org/relation/184714</a> so it's getting closer :) (It does look as if someone is already working on the nominatim problem.)</p>
</div>
<div id="comment-84697-info" class="comment-info">
<span class="comment-age">(04 Jun '22, 09:36)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="84699"></span>
<div id="comment-84699" class="comment">
<div id="post-84699-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, we've discussed this in the OSM Finland Telegram group, and I'm not even close to being an expert in this either. I wasn't able to reproduce the problem in the neighboring city Espoo, or in Turku with the show address/whereami function on the OSM website. Some examples in Helsinki: <a href="https://www.openstreetmap.org/search?whereami=1&amp;query=60.2246%2C24.9183#map=16/60.2246/24.9183">https://www.openstreetmap.org/search?whereami=1&amp;query=60.2246%2C24.9183#map=16/60.2246/24.9183</a> , <a href="https://www.openstreetmap.org/search?whereami=1&amp;query=60.24335%2C24.95233#map=18/60.24335/24.95233">https://www.openstreetmap.org/search?whereami=1&amp;query=60.24335%2C24.95233#map=18/60.24335/24.95233</a> , <a href="https://www.openstreetmap.org/search?whereami=1&amp;query=60.15136%2C24.88384#map=17/60.15136/24.88384">https://www.openstreetmap.org/search?whereami=1&amp;query=60.15136%2C24.88384#map=17/60.15136/24.88384</a> All the other relevant info is included except city. And checking the API output showed that the isaddress field for "Helsinki" is false in such places for some reason: <a href="https://nominatim.openstreetmap.org/details.php?osmtype=W&amp;osmid=772172190&amp;class=highway&amp;addressdetails=1&amp;hierarchy=0&amp;group_hierarchy=1&amp;format=json">https://nominatim.openstreetmap.org/details.php?osmtype=W&amp;osmid=772172190&amp;class=highway&amp;addressdetails=1&amp;hierarchy=0&amp;group_hierarchy=1&amp;format=json</a></p>
</div>
<div id="comment-84699-info" class="comment-info">
<span class="comment-age">(04 Jun '22, 11:01)</span> <span class="comment-user userinfo">Larmax</span>
</div>
</div>
<span id="84702"></span>
<div id="comment-84702" class="comment">
<div id="post-84702-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The problem still exist. Can you SomeoneElse tell me who is fixing the problem just now? Is there anybody fixing it at all.</p>
<p>Larmax said the problem is active also in the Lauttasaari(suburb of the Helsinki) Helsinki. The problem exist all around in the Helsinki maybe other cities too. Someone must do a sql query and find out the problem and fix it. Also need to fix a buggy algorithm or correct the person who made this kind of problem.</p>
<p>In my point of view the problem is real major problem here in the Finland. If I compare that city missing problem to a credit card transaction: 1. so you know the product you are buing and the price for it; 2.you see the product name and other detail but you don't see the price you are going to accept when you are needed to accept the credit card transaction. 3. in the accepting view there is also other option with same details as the product you are going to buy also these product prices could be missing and invisible prices are also different - probably higher. None vise person don't want to use that kind of credit card you must use as blind eyes - am I right? Now the nominatim is like "blind eye" adderess source for some parts of the Finland.</p>
</div>
<div id="comment-84702-info" class="comment-info">
<span class="comment-age">(04 Jun '22, 20:27)</span> <span class="comment-user userinfo">talousala</span>
</div>
</div>
<span id="84703"></span>
<div id="comment-84703" class="comment not_top_scorer">
<div id="post-84703-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/21777/talousala"></a><a href="https://help.openstreetmap.org/users/21777/talousala">@talousala</a> and <a href="https://help.openstreetmap.org/users/21853/larmax"></a><a href="https://help.openstreetmap.org/users/21853/larmax">@Larmax</a> this is not the issue tracker for nominatim (or anything else), if you want to report a problem with the software you need to open an issue with the developers, in this case <a href="https://github.com/osm-search/Nominatim">https://github.com/osm-search/Nominatim</a></p>
<p>If it is a case of one instance having an issue and others not, this is likely an operational issue and should be reported here <a href="https://github.com/openstreetmap/operations">https://github.com/openstreetmap/operations</a></p>
<p>In both cases you are going to help everybody with legible, clearly laid out reports, that includes making an appropriate number of line breaks.</p>
</div>
<div id="comment-84703-info" class="comment-info">
<span class="comment-age">(05 Jun '22, 08:52)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-84693" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-84693-form-container" class="comment-form-container">
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

<span id="84704"></span>

<div id="answer-container-84704" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84704-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84704-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-84704-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SimonPoole has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>An artefact from times when the boundary of Helsinki wasn't properly classified as a city. Updating the whole area should have fixed this now. There is already a <a href="https://github.com/osm-search/Nominatim/issues/2551">bug report for Nominatim</a> that the classification changes can cause havoc.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jun '22, 09:08</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-84704" class="comments-container">
<span id="84705"></span>
<div id="comment-84705" class="comment">
<div id="post-84705-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. Actually I'm using nominatim query geocodejson format but in this question I opened I used xml format for reason to get my explain short for limited character space. The xml format query works now but geocodejson query have still wrong data. Is geocodejson format slower, have some kind of delay to get your update in or is there still some kind of issue?</p>
<p><a href="https://nominatim.openstreetmap.org/search?q=Iivarintie+3,+Helsinki&amp;format=geocodejson&amp;polygon_geojson=1&amp;addressdetails=1">https://nominatim.openstreetmap.org/search?q=Iivarintie+3,+Helsinki&amp;format=geocodejson&amp;polygon_geojson=1&amp;addressdetails=1</a></p>
<p>= city "Helsinki sub-region" . Not working.</p>
<p><a href="https://nominatim.openstreetmap.org/search?q=Iivarintie+3,+Helsinki&amp;format=xml&amp;polygon_geojson=1&amp;addressdetails=1">https://nominatim.openstreetmap.org/search?q=Iivarintie+3,+Helsinki&amp;format=xml&amp;polygon_geojson=1&amp;addressdetails=1</a></p>
<p>= &lt;city&gt;Helsinki&lt;/city&gt; . Working</p>
<p>I don't know what to do. Do I need to convert my code to use xml format or what. That's a bit crazy situation.</p>
<p>I hope you have a nice day!</p>
</div>
<div id="comment-84705-info" class="comment-info">
<span class="comment-age">(05 Jun '22, 15:30)</span> <span class="comment-user userinfo">talousala</span>
</div>
</div>
<span id="84706"></span>
<div id="comment-84706" class="comment">
<div id="post-84706-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Fixed that too, I hope.</p>
</div>
<div id="comment-84706-info" class="comment-info">
<span class="comment-age">(05 Jun '22, 16:08)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="84707"></span>
<div id="comment-84707" class="comment">
<div id="post-84707-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Still same situation: not works. geocodejson city = "Helsinki sub-region". What is different with xml and geocodejson? How those format works on server side? Could there be a bug in xml and different bug in geocodejson.</p>
<p>How I can easily find out what is different in xml and geocodejson at server side? - which format I should use.</p>
<p>What is the right place discuss about possibilities use nominatim for everyday needs. I have received data in correct from nominatim responses. I felt I can trust nominatim works for me. I'm not sure anymore what format I was used to collect the data. Now I feel a week ago something changed different and nominatim responses not anymore correct. How it could be possible things not working and probably changing that way? I really don't know what to do. I go crazy! Nightmare. Thank you all! I feel like cry now! Peace &amp; happiness, always Ari</p>
</div>
<div id="comment-84707-info" class="comment-info">
<span class="comment-age">(05 Jun '22, 17:59)</span> <span class="comment-user userinfo">talousala</span>
</div>
</div>
</div>
<div id="comment-tools-84704" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84704-form-container" class="comment-form-container">
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

