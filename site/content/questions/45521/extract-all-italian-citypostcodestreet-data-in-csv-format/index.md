+++
type = "question"
title = "Extract ALL ITALIAN &quot;City,PostCode,Street” data in csv format"
description = '''I need a list of all “City,PostCode,Street” of Italy. I downloaded from http://download.gisgraphy.com/openstreetmap/pbf/ the IT compressed file, and I followed different steps like below: Test 1)  ./osmfilter IT.pdb --keep=&quot;addr:country= and addr:city= and addr:postcode and addr:street=&quot; --ignore-de...'''
date = "2015-09-23T10:22:00Z"
lastmod = "2017-02-01T10:29:00Z"
weight = 45521
keywords = [ "street", "city", "csv", "extract", "postcode" ]
aliases = [ "/questions/45521" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Extract ALL ITALIAN "City,PostCode,Street” data in csv format](/questions/45521/extract-all-italian-citypostcodestreet-data-in-csv-format)

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
<span id="post-45521-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45521-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-45521-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I need a list of all “City,PostCode,Street” of Italy.</p>
<p>I downloaded from <a href="http://download.gisgraphy.com/openstreetmap/pbf/">http://download.gisgraphy.com/openstreetmap/pbf/</a> the IT compressed file, and I followed different steps like below:</p>
<p>Test 1) ./osmfilter IT.pdb --keep="addr:country= and addr:city= and addr:postcode and addr:street=" --ignore-dependencies | ./osmconvert --csv="addr:country addr:city adde:postcode addr:street” --csv-separator=","</p>
<p>But It does not extract ALL the addresses.</p>
<p>Test 2) As suggest here <a href="/questions/9816/the-best-way-to-extract-street-list">https://help.openstreetmap.org/questions/9816/the-best-way-to-extract-street-list</a> I tried with: "osmfilter with --keep="highway=residential =primary =secondary =tertiaty =unclassified", etc., to get all streets, then use osmconvert with --all-to-nodes and --csv="<a href="https://help.openstreetmap.org/users/1350/longestaugust">@lon</a> <a href="https://help.openstreetmap.org/users/5110/latroc">@lat</a> name etc." to get the CSV list.” But it does not works 100% because It does not extract ALL the Italian's address.</p>
<p>Test 3) I downloaded from <a href="http://download.gisgraphy.com/openstreetmap/csv/streets/">http://download.gisgraphy.com/openstreetmap/csv/streets/</a> the IT list of all the streets, but I don’t know how create a relationship with “City”, “PostCode” and related “Street”.</p>
<p>Someone known how resolve the problem ?</p>
<p>Thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-street" rel="tag" title="see questions tagged &#39;street&#39;">street</span> <span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-postcode" rel="tag" title="see questions tagged &#39;postcode&#39;">postcode</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Sep '15, 10:22</strong></p>
<img src="https://secure.gravatar.com/avatar/bc2776550b2995a9d0090bbb2005dcd1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MMM333&#39;s gravatar image" />
<p><span>MMM333</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MMM333 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-45521" class="comments-container">
&#10;</div>
<div id="comment-tools-45521" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45521-form-container" class="comment-form-container">
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

<span id="45523"></span>

<div id="answer-container-45523" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45523-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45523-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-45523-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To build a relationship between city and postcode and streets, you will need city polygons (should be available from OSM) and postcode polygons (unlikely that OSM has these for Italy though), and load them into a PostGIS database together with the street data. Then you can run spatial queries that find the enclosing polygon for each street. A good way to load OSM data into a PostGIS database is the "osm2pgsql" tool.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Sep '15, 10:50</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-45523" class="comments-container">
<span id="45669"></span>
<div id="comment-45669" class="comment">
<div id="post-45669-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do you know the sql queries that can solve it ? Or do you have some link that could help me ? thanks</p>
</div>
<div id="comment-45669-info" class="comment-info">
<span class="comment-age">(30 Sep '15, 13:38)</span> <span class="comment-user userinfo">MMM333</span>
</div>
</div>
<span id="45691"></span>
<div id="comment-45691" class="comment">
<div id="post-45691-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Here the query that resolve part of the problem (just City and Street):</p>
<p>SELECT polygon.name,line.name FROM planet_osm_line AS line CROSS JOIN planet_osm_polygon AS polygon WHERE polygon.admin_level = '8' AND ST_Contains(polygon.way, line.way) AND line.highway in ('primary', 'secondary', 'tertiary', 'road', 'residential','motorway', 'trunk', 'unclassified') GROUP BY polygon.name,line.name</p>
<p>Do you think it could be optimized ?</p>
<p>Unfortunately there is no postal code polygon for Italy, so I can't create the wished relationship.</p>
</div>
<div id="comment-45691-info" class="comment-info">
<span class="comment-age">(02 Oct '15, 09:02)</span> <span class="comment-user userinfo">MMM333</span>
</div>
</div>
</div>
<div id="comment-tools-45523" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45523-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="45522"></span>

<div id="answer-container-45522" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-45522-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45522-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-45522-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It probably doesn't extract ALL the addresses because OpenStreetMap doesn't have ALL the addresses in Italy. It only has the ones that people have mapped.</p>
<p>If there is data that you know is in OpenStreetMap, but you can't extract it, then please cite an example (using a link to that place on osm.org).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Sep '15, 10:32</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-45522" class="comments-container">
<span id="45524"></span>
<div id="comment-45524" class="comment">
<div id="post-45524-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Richard, When I say "does not extract ALL the addresses" I mean “from" the file. Here the example: $ grep Marchisio IT.xml &lt;tag k="name" v="Via Tancredi Marchisio"/&gt; #note: "via" mean "street" &lt;tag k="name" v="Via Pietro Marchisio"/&gt; etc…</p>
<p>$./osmfilter IT.xml --keep="addr:country= and addr:city= and addr:postcode= and addr:street=" --ignore-dependencies | ./osmconvert - --csv="addr:country addr:city addr:postcode addr:street" --csv-separator="," | sort | uniq &gt; all_italian.csv</p>
<p>$ wc -l all_italian.csv 16810 all_italian.csv #all italian address are ~ 200k</p>
<p>$grep “Marchisio” all_italian.csv # -&gt; No result</p>
</div>
<div id="comment-45524-info" class="comment-info">
<span class="comment-age">(23 Sep '15, 13:26)</span> <span class="comment-user userinfo">MMM333</span>
</div>
</div>
<span id="45525"></span>
<div id="comment-45525" class="comment">
<div id="post-45525-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>That's not an error, just missing address data in OSM. Although <em>Via Tancredi Marchisio</em> exists as a street name there is not even a single address for it in OSM, see <a href="https://www.openstreetmap.org/#map=19/44.38597/9.01461">https://www.openstreetmap.org/#map=19/44.38597/9.01461</a></p>
</div>
<div id="comment-45525-info" class="comment-info">
<span class="comment-age">(23 Sep '15, 13:57)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-45522" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45522-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="54396"></span>

<div id="answer-container-54396" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54396-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54396-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54396-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi MMM333, did u find, in the end, a working solution? I have the same problem....</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Feb '17, 10:29</strong></p>
<img src="https://secure.gravatar.com/avatar/d03b432404c1d35ad622740f8e398314?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gersis&#39;s gravatar image" />
<p><span>gersis</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gersis has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Feb '17, 10:29</strong> </span></p>
</div>
</div>
<div id="comments-container-54396" class="comments-container">
&#10;</div>
<div id="comment-tools-54396" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54396-form-container" class="comment-form-container">
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

