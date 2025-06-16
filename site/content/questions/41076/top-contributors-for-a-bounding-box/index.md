+++
type = "question"
title = "Top contributors for a bounding box"
description = '''I am interested in using an API that would do the following: Input: a geographic bounding box Output: a list of OSM contributors, ordered by the number of edited ways, nodes and relations from that bounding box. I checked the OSM API, but I didn’t find anything helpful. The history section displays ...'''
date = "2015-02-17T14:06:00Z"
lastmod = "2018-02-13T23:05:00Z"
weight = 41076
keywords = [ "contributor", "api", "history" ]
aliases = [ "/questions/41076" ]
osqa_answers = 5
osqa_accepted = false
+++

<div class="headNormal">

# [Top contributors for a bounding box](/questions/41076/top-contributors-for-a-bounding-box)

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
<span id="post-41076-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41076-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-41076-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am interested in using an API that would do the following:</p>
<p>Input: a geographic bounding box Output: a list of OSM contributors, ordered by the number of edited ways, nodes and relations from that bounding box.</p>
<p>I checked the <a href="https://wiki.openstreetmap.org/wiki/API_v0.6">OSM API</a>, but I didn’t find anything helpful. The <a href="https://www.openstreetmap.org/history">history section</a> displays recent changesets from the visible map, very similar to what I would need. Is it using an internal API? Would it be possible to implement the API myself if it's not available? If yes, what would be the easiest way to do so?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-contributor" rel="tag" title="see questions tagged &#39;contributor&#39;">contributor</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Feb '15, 14:06</strong></p>
<img src="https://secure.gravatar.com/avatar/ed3976e44742535b228c3a578ebcb6af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlexIlisei&#39;s gravatar image" />
<p><span>AlexIlisei</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlexIlisei has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-41076" class="comments-container">
<span id="41189"></span>
<div id="comment-41189" class="comment">
<div id="post-41189-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It may not be what you're looking for, but there is an API call for "changesets in a bounding box":</p>
<p><a href="http://wiki.osm.org/wiki/API_v0.6#Query:_GET_.2Fapi.2F0.6.2Fchangesets">http://wiki.osm.org/wiki/API_v0.6#Query:<em>GET</em>.2Fapi.2F0.6.2Fchangesets</a></p>
<p>It's not "for all time" though - just the last 100.</p>
</div>
<div id="comment-41189-info" class="comment-info">
<span class="comment-age">(20 Feb '15, 18:54)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41076" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41076-form-container" class="comment-form-container">
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

<span id="41155"></span>

<div id="answer-container-41155" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41155-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41155-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-41155-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Another option to look at is <a href="http://simon04.dev.openstreetmap.org/whodidit/">Whodidit</a></p>
<p>It has an API that returns changesets per tile, for example:</p>
<pre><code>http://simon04.dev.openstreetmap.org/whodidit/scripts/tiles.php?age=1000&amp;bbox=-111.92834854127,40.685132455819,-111.77749252321,40.740783521057</code></pre>
<p>returning</p>
<pre><code> { &quot;type&quot; : &quot;FeatureCollection&quot;, &quot;features&quot; : [{&quot;type&quot;:&quot;Feature&quot;,&quot;geometry&quot;:{&quot;type&quot;:&quot;Polygon&quot;,&quot;coordinates&quot;:[[[-111.78,40.68],[-111.77,40.68],[-111.77,40.69],[-111.78,40.69],[-111.78,40.68]]]},&quot;properties&quot;:{&quot;changesets&quot;:&quot;20478128,16462841&quot;,&quot;nodes_created&quot;:&quot;2&quot;,&quot;nodes_modified&quot;:&quot;0&quot;,&quot;nodes_deleted&quot;:&quot;0&quot;}}, {&quot;type&quot;:&quot;Feature&quot;,&quot;geometry&quot;:{&quot;type&quot;:&quot;Polygon&quot;,&quot;coordinates&quot;:[[[-111.8,40.68],[-111.79,40.68],[-111.79,40.69],[-111.8,40.69],[-111.8,40.68]]]},&quot;properties&quot;:{&quot;changesets&quot;:&quot;22954115,22954072,22954020,16712027,16449373,15265638,13183220,12441600,12293424,12293394&quot;,&quot;nodes_created&quot;:&quot;24&quot;,&quot;nodes_modified&quot;:&quot;21&quot;,&quot;nodes_deleted&quot;:&quot;60&quot;}},</code></pre>
<p>etcetera</p>
<p>You can then query the changesets with</p>
<pre><code>http://simon04.dev.openstreetmap.org/whodidit/scripts/changeset.php?id=27348492%2C26248890%2C20361446%2C18741987%2C18442800%2C17280797%2C17182635%2C17064018%2C16424995%2C15966785</code></pre>
<p>Which will return add / modify / delete counts per user for those:</p>
<pre><code>[{&quot;changeset_id&quot;:&quot;27348492&quot;,&quot;change_time&quot;:&quot;2014-12-09 04:25:08&quot;,&quot;comment&quot;:&quot;adding detail with bing images and tiger data Keep right not connected roads and bad intersections &quot;,&quot;user_id&quot;:&quot;567792&quot;,&quot;user_name&quot;:&quot;Natfoot&quot;,&quot;created_by&quot;:&quot;iD 1.6.2&quot;,&quot;nodes_created&quot;:&quot;102&quot;,&quot;nodes_modified&quot;:&quot;15&quot;,&quot;nodes_deleted&quot;:&quot;42&quot;,&quot;ways_created&quot;:&quot;7&quot;,&quot;ways_modified&quot;:&quot;16&quot;,&quot;ways_deleted&quot;:&quot;4&quot;,&quot;relations_created&quot;:&quot;0&quot;,&quot;relations_modified&quot;:&quot;1&quot;,&quot;relations_deleted&quot;:&quot;0&quot;,&quot;suspicious&quot;:0},</code></pre>
<p>etcetera.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Feb '15, 16:29</strong></p>
<img src="https://secure.gravatar.com/avatar/acea3c9fd5908d7ff09596d16b8724d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mvexel&#39;s gravatar image" />
<p><span>mvexel</span><br />
<span class="score" title="762 reputation points">762</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mvexel has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-41155" class="comments-container">
&#10;</div>
<div id="comment-tools-41155" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41155-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="41087"></span>

<div id="answer-container-41087" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41087-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-41087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have a closer look at <a href="https://wiki.openstreetmap.org/wiki/OSM_Mapper">OSM_Mapper</a> by ITO-World ... it has several features, like nshowing most active mappers in a defined bounding box.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Feb '15, 16:30</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-41087" class="comments-container">
<span id="41109"></span>
<div id="comment-41109" class="comment">
<div id="post-41109-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, will definitely take a look !</p>
</div>
<div id="comment-41109-info" class="comment-info">
<span class="comment-age">(18 Feb '15, 13:09)</span> <span class="comment-user userinfo">AlexIlisei</span>
</div>
</div>
<span id="62076"></span>
<div id="comment-62076" class="comment">
<div id="post-62076-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>To <em>get access to this service</em> you have to write them an email. They will answer within a few hours and open an account for your email address. Worked well for me. And this is the <strong>easiest way</strong> I have found to evaluate the top contributors of a bounding box without hacking. But I also use the overpass api mentioned by @joostschouppe in his answer and pipe the output through self made scripts.</p>
</div>
<div id="comment-62076-info" class="comment-info">
<span class="comment-age">(13 Feb '18, 23:05)</span> <span class="comment-user userinfo">erik</span>
</div>
</div>
</div>
<div id="comment-tools-41087" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41087-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="41077"></span>

<div id="answer-container-41077" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41077-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41077-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-41077-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>not an API (directly, except if you can find an internal interface in the JavaScript source) and not with all that restrictions, but do you know <a href="http://resultmaps.neis-one.org/oooc?layers=B00FTFFFFT">who's around me</a>? Also see <span>nearby users</span>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Feb '15, 14:10</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-41077" class="comments-container">
<span id="41110"></span>
<div id="comment-41110" class="comment">
<div id="post-41110-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, will definitely take a look !</p>
</div>
<div id="comment-41110-info" class="comment-info">
<span class="comment-age">(18 Feb '15, 13:13)</span> <span class="comment-user userinfo">AlexIlisei</span>
</div>
</div>
</div>
<div id="comment-tools-41077" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41077-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53122"></span>

<div id="answer-container-53122" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53122-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://overpass-turbo.eu/s/kjb">This Overpass query</a> will get you a CSV of all the contributors who are still visible in the current map data for a bounding box. Now all you have left to do, is count the number of nodes, ways and relations per contributor.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Nov '16, 18:43</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-53122" class="comments-container">
<span id="62075"></span>
<div id="comment-62075" class="comment">
<div id="post-62075-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Works very good. If you want to further evaluate, plot etc. the data, you can use the <em>export</em> tab and click on <em>rawdata from overpass API</em> to get a file that contains the output data.</p>
</div>
<div id="comment-62075-info" class="comment-info">
<span class="comment-age">(13 Feb '18, 22:58)</span> <span class="comment-user userinfo">erik</span>
</div>
</div>
</div>
<div id="comment-tools-53122" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53122-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="41187"></span>

<div id="answer-container-41187" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41187-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41187-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41187-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There might be issues with using other files than history files. If using a current world dump, you will miss a lot of contributors with few changesets. I wrote a bit about that <a href="https://www.openstreetmap.org/user/joost%20schouppe/diary/26259">in this post</a>.</p>
<p>If this is an issue, you could use <a href="http://osm.personalwerk.de/full-history-extracts/latest/">these</a> regularly updated full history dumps. Using the <a href="https://github.com/MaZderMind/osm-history-splitter">history splitter</a> you can make a full history dump for the bounding box that interests you. The <a href="https://github.com/MaZderMind/osm-history-renderer">history-renderer</a> imports this into a Postgress database which you could easily use to export the data you need.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Feb '15, 18:47</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-41187" class="comments-container">
&#10;</div>
<div id="comment-tools-41187" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41187-form-container" class="comment-form-container">
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

