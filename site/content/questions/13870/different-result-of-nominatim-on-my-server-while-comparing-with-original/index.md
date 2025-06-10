+++
type = "question"
title = "Different result of nominatim on my server while comparing with original"
description = '''I was trying to configure Nominatim OSM DB on my own server and facing so many issues while using planet file. So as per the suggestions of experts on forums, I did this job for particular small city &quot;Bremen&quot; in Germany and I was successful to do so. Now my issue is, when I am checking the lat/lon o...'''
date = "2012-06-28T07:03:00Z"
lastmod = "2013-11-15T17:26:00Z"
weight = 13870
keywords = [ "planet", "city", "nominatim", "osm", "postgresql" ]
aliases = [ "/questions/13870" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Different result of nominatim on my server while comparing with original](/questions/13870/different-result-of-nominatim-on-my-server-while-comparing-with-original)

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
<span id="post-13870-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13870-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13870-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I was trying to configure Nominatim OSM DB on my own server and facing so many issues while using planet file. So as per the suggestions of experts on forums, I did this job for particular small city "Bremen" in Germany and I was successful to do so. Now my issue is, when I am checking the lat/lon of a place from that city I am getting following result:</p>
<p>My query: <a href="http://MY_SERVER/reverse.php?format=xml&amp;lat=53.078717&amp;lon=8.801239">http://MY_SERVER/reverse.php?format=xml&amp;lat=53.078717&amp;lon=8.801239</a></p>
<p>My result:</p>
<pre><code>&lt;reversegeocode timestamp=&quot;Thu, 28 Jun 12 07:38:58 +0200&quot; attribution=&quot;Data Copyright OpenStreetMap Contributors, Some Rights Reserved. CC-BY-SA 2.0.&quot; querystring=&quot;format=xml&amp;lat=53.078717&amp;lon=8.801239&quot;&gt;
    &lt;result place_id=&quot;127453&quot; osm_type=&quot;way&quot; osm_id=&quot;25418182&quot; lat=&quot;53.0784786859461&quot; lon=&quot;8.80216752051522&quot;&gt;
        Straßenbahn Linie 2,3,3S, Germany
    &lt;/result&gt;
&lt;addressparts&gt;
    &lt;tram&gt;Straßenbahn Linie 2,3,3S&lt;/tram&gt;
    &lt;country&gt;Germany&lt;/country&gt;
    &lt;country_code&gt;de&lt;/country_code&gt;
&lt;/addressparts&gt;</code></pre>
&lt;/reversegeocode&gt;
<p>While you can see the actual result here for the same lat/ lon: <a href="http://nominatim.openstreetmap.org/reverse.php?format=xml&amp;lat=53.078717&amp;lon=8.801239">http://nominatim.openstreetmap.org/reverse.php?format=xml&amp;lat=53.078717&amp;lon=8.801239</a></p>
<p>So please suggest why all this tags (pedestrian, neighbourhood, suburb , city, state, postcode etc.) are missing on my server. what is my mistake in configuration or import? What can I do to solve this?</p>
<p>More (Another question), As I have already nominatm installed for one city on my server and now I want to do it for planet. So should I do all the things from the begening? or there is some update kind of mechanism which will upgrade my installation to planet level from the current city level? Please anwser.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-planet" rel="tag" title="see questions tagged &#39;planet&#39;">planet</span> <span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jun '12, 07:03</strong></p>
<img src="https://secure.gravatar.com/avatar/b3013a84207a32bed7ddfad7004100f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ravi%20Kotwani&#39;s gravatar image" />
<p><span>Ravi Kotwani</span><br />
<span class="score" title="136 reputation points">136</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ravi Kotwani has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13870" class="comments-container">
&#10;</div>
<div id="comment-tools-13870" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13870-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="13894"></span>

<div id="answer-container-13894" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13894-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13894-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-13894-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Small extracts have the disadvantage that they often do not contain the relations of higher administrative units, city and state in your case. Or they are missing some of the boundary ways, which probably happens with the neighborhood.</p>
<p>There are two possibilities to fix this:</p>
<ol>
<li>Import a large enough extract, Germany should do in your case. You will have to start the import from scratch.</li>
<li><p>Add the missing boundaries. For this you need to find out the relation ID of the boundary or boundaries in question and then import them with:</p>
<pre><code>./utils/update.php --import-relation &lt;relation id&gt;</code></pre>
<p>Then reindex the entire database like this:</p>
<pre><code>psql -d nominatim -c &#39;UPDATE placex SET indexed_status=2&#39;
./utils/setup.php --index</code></pre></li>
</ol>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jun '12, 08:17</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-13894" class="comments-container">
<span id="13898"></span>
<div id="comment-13898" class="comment">
<div id="post-13898-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your answer. I am going with solution one. So doing process from scratch for Germany.</p>
</div>
<div id="comment-13898-info" class="comment-info">
<span class="comment-age">(29 Jun '12, 10:06)</span> <span class="comment-user userinfo">Ravi Kotwani</span>
</div>
</div>
<span id="13940"></span>
<div id="comment-13940" class="comment">
<div id="post-13940-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@lonvia</span> Hi, I have imported the Germany data from scratch as you told in your option 1. Still I am facing the same problem.</p>
<p>Some details: 1043 tables are in DB and following errors I faced while importing: -- type "planet_osm_ways" does not exist -- type "nearplace" does not exist -- type "nearfeature" does not exist -- relation "planet_osm_rels" does not exist</p>
<p>Please suggest the solution.</p>
</div>
<div id="comment-13940-info" class="comment-info">
<span class="comment-age">(02 Jul '12, 11:38)</span> <span class="comment-user userinfo">Ravi Kotwani</span>
</div>
</div>
<span id="13951"></span>
<div id="comment-13951" class="comment">
<div id="post-13951-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>If "planet_osm_ways" and "planet_osm_rels" do not exist then something went wrong already with the osm2pgsql import. Make sure you have the latest version of Nominatim (not older than a week) and that you use the version of osm2pgsql that comes with it.</p>
</div>
<div id="comment-13951-info" class="comment-info">
<span class="comment-age">(02 Jul '12, 20:13)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="13969"></span>
<div id="comment-13969" class="comment">
<div id="post-13969-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I upgraded my osm2pgsql version as you told. But still facing all the same error. There was no difference even in one small error. Everything was same as previous. Please suggest any other solution. Thanks in advance.</p>
</div>
<div id="comment-13969-info" class="comment-info">
<span class="comment-age">(03 Jul '12, 14:28)</span> <span class="comment-user userinfo">Ravi Kotwani</span>
</div>
</div>
</div>
<div id="comment-tools-13894" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13894-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="28137"></span>

<div id="answer-container-28137" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28137-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28137-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-28137-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi</p>
<p>is a old questiond, but i resolved with reindexed data, give the solution for someone in need ...</p>
<p>whit this resolved indexed all "place", before the "placex" is a 30%, now is a 100% of a "place" table.</p>
<pre><code>./utils/update.php --import-file &lt;osmfile.osm&gt;
./utils/update.php --index</code></pre>
<p>Gracias a todos por su ayuda</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Nov '13, 17:26</strong></p>
<img src="https://secure.gravatar.com/avatar/8151a2cd9f1041f10b62d8ca446d3b2a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alveniz&#39;s gravatar image" />
<p><span>alveniz</span><br />
<span class="score" title="51 reputation points">51</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alveniz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-28137" class="comments-container">
&#10;</div>
<div id="comment-tools-28137" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28137-form-container" class="comment-form-container">
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

