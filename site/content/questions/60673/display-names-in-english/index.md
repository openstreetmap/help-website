+++
type = "question"
title = "Display names in English"
description = '''I just started using OpenStreetMap, I am not an advanced user, I just want OpenStreetMap to replace Google Maps in my daily geographical searches. I would like to display the map from the main website using the English names everywhere. Is it possible via some easy manipulation not involving javascr...'''
date = "2017-11-18T09:24:00Z"
lastmod = "2022-11-01T11:39:00Z"
weight = 60673
keywords = [ "latin", "names" ]
aliases = [ "/questions/60673" ]
osqa_answers = 5
osqa_accepted = true
+++

<div class="headNormal">

# [Display names in English](/questions/60673/display-names-in-english)

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
<span id="post-60673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60673-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-60673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I just started using OpenStreetMap, I am not an advanced user, I just want OpenStreetMap to replace Google Maps in my daily geographical searches.</p>
<p>I would like to display the map from the main website using the English names everywhere. Is it possible via some easy manipulation not involving javascript and such ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-latin" rel="tag" title="see questions tagged &#39;latin&#39;">latin</span> <span class="post-tag tag-link-names" rel="tag" title="see questions tagged &#39;names&#39;">names</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Nov '17, 09:24</strong></p>
<img src="https://secure.gravatar.com/avatar/02308f9ed1dc73fbf51d51ae8e4a7c3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vkubicki&#39;s gravatar image" />
<p><span>vkubicki</span><br />
<span class="score" title="160 reputation points">160</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vkubicki has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60673" class="comments-container">
<span id="60797"></span>
<div id="comment-60797" class="comment">
<div id="post-60797-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>While you've gotten the correct answer already, but I would like to point out that while it is <em>local</em> names that are displayed with the default rendering, English names <em>are</em> in the database, and are searchable.</p>
<p>For example if I <a href="https://www.openstreetmap.org/search?query=Beijing#map=11/39.9061/116.3912">search for "Beijing"</a>, the first result is the what you'd expect, the capital of China. The result is displayed in English. If I <a href="https://www.openstreetmap.org/node/25248662">click on it</a>, I get all the tags on the Beijing. This includes well over 100 names in different languages. On the map it is written as "北京市", but in the sidebar all those different languages are displayed.</p>
<p>While this is a bit of an extreme example, it allows maps to be rendered in different languages.</p>
<p>Multilingual data is viewed as important to OSM, and the prominent local names, the non-English names (often written in non-Latin alphabets) is only one manifestation of that.</p>
</div>
<div id="comment-60797-info" class="comment-info">
<span class="comment-age">(26 Nov '17, 05:32)</span> <span class="comment-user userinfo">keithonearth</span>
</div>
</div>
</div>
<div id="comment-tools-60673" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60673-form-container" class="comment-form-container">
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

5 Answers:

</div>

</div>

<span id="60687"></span>

<div id="answer-container-60687" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60687-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60687-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-60687-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="vkubicki has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You are (currently) out of luck (the question is btw a FAQ), what you are seeing on the website when you select the standard style are images that are stored as individual image files. There is simply nothing to manipulate to start with.</p>
<p>Naturally it is quite possible to generate a map with English names from OSM data, if you look at the cycle map layer you for example will see English names everywhere we have them in the data.</p>
<p>That was the short version, the long version is, yes there is technology available that moves the rendering of the map images to your browser, which gives a lot more flexibility with such things. I wouldn't wager a bet on when we will switch or provide such functionality in parallel to the current system.</p>
<p>The other point is that the infrastructure at openstreetmap.org is geared towards supporting our contributors and from that point of view it makes a lot of sense to show the local names.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Nov '17, 23:40</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Nov '17, 23:44</strong> </span></p>
</div>
</div>
<div id="comments-container-60687" class="comments-container">
<span id="60688"></span>
<div id="comment-60688" class="comment">
<div id="post-60688-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK thank you. I understand the problem, but maybe rendering one local and one all-English map could be useful.</p>
</div>
<div id="comment-60688-info" class="comment-info">
<span class="comment-age">(19 Nov '17, 01:59)</span> <span class="comment-user userinfo">vkubicki</span>
</div>
</div>
<span id="60689"></span>
<div id="comment-60689" class="comment">
<div id="post-60689-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>There may be third party websites or desktop programs that can render an English-only map, using the OSM data.</p>
</div>
<div id="comment-60689-info" class="comment-info">
<span class="comment-age">(19 Nov '17, 02:20)</span> <span class="comment-user userinfo">dsh4</span>
</div>
</div>
<span id="60690"></span>
<div id="comment-60690" class="comment">
<div id="post-60690-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You can take a look at <a href="https://wiki.openstreetmap.org/wiki/Tiles">Tiles in the OSM wiki</a>, <a href="http://mapstyle.petschge.de/">mapstyle.petschge.de</a>, <a href="http://leaflet-extras.github.io/leaflet-providers/preview/">Leaflet Provider Demo</a> and <a href="https://mc.bbbike.org/mc/">Map Compare</a> for various OSM-based maps. Some of them have all-English names.</p>
</div>
<div id="comment-60690-info" class="comment-info">
<span class="comment-age">(19 Nov '17, 09:17)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="60692"></span>
<div id="comment-60692" class="comment">
<div id="post-60692-score" class="comment-score">
3
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14442/vkubicki">@vkubicki</a> For the avoidance of doubt, the OSM website currently renders 4 maps, 2 of which render English names.</p>
</div>
<div id="comment-60692-info" class="comment-info">
<span class="comment-age">(19 Nov '17, 09:57)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="60940"></span>
<div id="comment-60940" class="comment not_top_scorer">
<div id="post-60940-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>: are there url to reach those renderings ?</p>
</div>
<div id="comment-60940-info" class="comment-info">
<span class="comment-age">(02 Dec '17, 10:41)</span> <span class="comment-user userinfo">vkubicki</span>
</div>
</div>
<span id="60947"></span>
<div id="comment-60947" class="comment">
<div id="post-60947-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>On <a href="https://www.openstreetmap.org/">https://www.openstreetmap.org/</a> click the 4th button down at the right-hand side. It looks a bit like a stack of books, and there's a tooltip that says "layers". The Cycle Map and the Transport Map show names in English as well as the local name. When you select e.g. the Cycle map you'll see the URL change to to something like <a href="https://www.openstreetmap.org/#map=10/39.9066/115.9799&amp;layers=C">https://www.openstreetmap.org/#map=10/39.9066/115.9799&amp;layers=C</a> so that when you send that link to someone it loads the cycle map for them too.</p>
</div>
<div id="comment-60947-info" class="comment-info">
<span class="comment-age">(02 Dec '17, 14:09)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="60974"></span>
<div id="comment-60974" class="comment not_top_scorer">
<div id="post-60974-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes,you just need to add "&amp;layers=" with C, T or H at the end, for example with Beijing: cycle map: <a href="https://www.openstreetmap.org/#map=8/39.802/116.112&amp;layers=C">https://www.openstreetmap.org/#map=8/39.802/116.112&amp;layers=C</a> , transportation map: <a href="https://www.openstreetmap.org/#map=8/39.802/116.112&amp;layers=T">https://www.openstreetmap.org/#map=8/39.802/116.112&amp;layers=T</a> , humanitarian map: <a href="https://www.openstreetmap.org/#map=8/39.802/116.112&amp;layers=H">https://www.openstreetmap.org/#map=8/39.802/116.112&amp;layers=H</a></p>
</div>
<div id="comment-60974-info" class="comment-info">
<span class="comment-age">(03 Dec '17, 04:37)</span> <span class="comment-user userinfo">kocio</span>
</div>
</div>
<span id="86047"></span>
<div id="comment-86047" class="comment not_top_scorer">
<div id="post-86047-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> Yeeeess, it still works. I finally get the answer to a question that has bothered me for years. A bit convoluted though.</p>
</div>
<div id="comment-86047-info" class="comment-info">
<span class="comment-age">(01 Nov '22, 11:39)</span> <span class="comment-user userinfo">MaxDLN</span>
</div>
</div>
</div>
<div id="comment-tools-60687" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-60687-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="71895"></span>

<div id="answer-container-71895" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71895-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71895-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-71895-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you do want names displayed in English on those tiles in the osm style, there is a new project osMap that shows tiles with English labels (amongst others) using transscription if no English name tag is available.</p>
<p>It's also optimized for faster tile-loading speed depending on where you are right now: just use</p>
<ul>
<li><a href="https://www.osmap.us">www.osmap.us</a> if you are in the U.S. or Canada,</li>
<li><a href="https://www.osmap.uk">www.osmap.uk</a> if you are in Europe or</li>
<li><a href="https://www.osmap.asia">www.osmap.asia</a> if you are in Asia</li>
</ul>
<p>Some more European versions (French, Spanish, Italian, German, Dutch and Danish) can be found via <a href="https://www.osmap.info">www.osmap.info</a>.</p>
<p>As several people have asked: Access to the English tiles (as well as the Spanish and French) can now be obtained through <a href="http://www.maptilesapi.com">MapTiles API</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Nov '19, 22:00</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jan '20, 16:21</strong> </span></p>
</div>
</div>
<div id="comments-container-71895" class="comments-container">
&#10;</div>
<div id="comment-tools-71895" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71895-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="60793"></span>

<div id="answer-container-60793" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60793-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60793-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60793-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you like the standard style and you miss only the English labels, you can use this service:</p>
<p>[edited to not include the link to a map]</p>
<p>It uses slightly modified osm-carto code, so it's possible to set your own service with localized names in any other language, if you have the skills to deploy OSM maps rendering infrastructure:</p>
<p><a href="https://github.com/giggls/openstreetmap-carto-de/tree/upstream+l10n">https://github.com/giggls/openstreetmap-carto-de/tree/upstream+l10n</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Nov '17, 03:06</strong></p>
<img src="https://secure.gravatar.com/avatar/e228dd20b7da2a6c8f559e2118ce08d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kocio&#39;s gravatar image" />
<p><span>kocio</span><br />
<span class="score" title="2054 reputation points"><span>2.1k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kocio has 14 accepted answers">20%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Jan '20, 18:22</strong> </span></p>
</div>
</div>
<div id="comments-container-60793" class="comments-container">
<span id="70422"></span>
<div id="comment-70422" class="comment">
<div id="post-70422-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Unfortunately your answer gave the intention to a lot of people, that this server is a free service for third party maps which it never was!</p>
<p>This causes a lot of trouble in recent days :(</p>
<p>Please do not use this server for any commercial project. I will be able to make an exception for non-profit stuff, bit this is not a free to use service so do not use it but set up your own server instead.</p>
<p>Among others Geofabrik is providing this map style as a commercial service.</p>
<p>Regards</p>
<p>Sven</p>
</div>
<div id="comment-70422-info" class="comment-info">
<span class="comment-age">(19 Aug '19, 14:28)</span> <span class="comment-user userinfo">giggls</span>
</div>
</div>
</div>
<div id="comment-tools-60793" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60793-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="72047"></span>

<div id="answer-container-72047" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72047-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72047-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72047-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This solution is working for me. In the *.mml file, wherever there is a SELECT ... name ... statement, I replaced name with the following.</p>
<pre><code>         CASE
            WHEN tags-&gt;&#39;name:en&#39; IS NOT NULL AND name IS NOT NULL AND tags-&gt;&#39;name:en&#39; &lt;&gt; name
            THEN CONCAT(name, chr(10),&#39;(&#39;, tags-&gt;&#39;name:en&#39;, &#39;)&#39;)
            ELSE name
         END</code></pre>
<p>This is rendering name of entity in local language with English in Roman Alphabet in parentheses below the local language name. Two items to note: If the SELECT ... name ... is selecting name as a list of fields being selected, and name has a comma after it, the CASE statement needs to have that comma after it. If name is at the end of the list of fields and has no comma, the CASE statement needs to not have a comma after it. Second item, the CASE statement is evaluating tags-&gt;'name:en'. Therefore the FROM part of the SELECT statement needs to be evaluating the tags field in the table. In the default project.mml file, some of the SELECT statements FROM parts are querying a subset of fields in the table "(FROM (SELECT...". If you want to evaluate the tags-&gt;'name:en', then you need to add tags, to the "FROM (SELECT" part of the SELECT statement.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Dec '19, 16:18</strong></p>
<img src="https://secure.gravatar.com/avatar/ce3c9f8234a453acbf0e5bbec39e6466?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard%20Haimann&#39;s gravatar image" />
<p><span>Richard Haimann</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard Haimann has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72047" class="comments-container">
<span id="72048"></span>
<div id="comment-72048" class="comment">
<div id="post-72048-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>While such an approach would basically work it does not produce good results.</p>
<p>I would definitely recommend using my l10n code at <a href="https://github.com/giggls/mapnik-german-l10n">https://github.com/giggls/mapnik-german-l10n</a> instead.</p>
<p>BTW I decided against parentheses a long time ago as this produces more hassle than good IMO e.g. in right-to-left scripts. I now use Newline instead.</p>
</div>
<div id="comment-72048-info" class="comment-info">
<span class="comment-age">(09 Dec '19, 16:29)</span> <span class="comment-user userinfo">giggls</span>
</div>
</div>
</div>
<div id="comment-tools-72047" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72047-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="85290"></span>

<div id="answer-container-85290" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85290-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85290-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-85290-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I ended up going with osmand + scrcpy because every other solution had major drawbacks imo (qgis doesn't work with mapillary, couldn't figure out a custom api endpoint in josm with an api key, osmap.us doesn't have same capabilities as osm.org), mapillary (website) doesn't have a distance scale.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Aug '22, 18:12</strong></p>
<img src="https://secure.gravatar.com/avatar/adb8a2264896c7b39deddadb3daf1a61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hs5DBg5d5iXJ&#39;s gravatar image" />
<p><span>Hs5DBg5d5iXJ</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hs5DBg5d5iXJ has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Aug '22, 08:10</strong> </span></p>
</div>
</div>
<div id="comments-container-85290" class="comments-container">
&#10;</div>
<div id="comment-tools-85290" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85290-form-container" class="comment-form-container">
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

