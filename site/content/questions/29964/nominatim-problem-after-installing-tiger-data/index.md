+++
type = "question"
title = "nominatim problem after installing TIGER data"
description = '''Hi, I&#x27;m trying to install TIGER data on a local Nominatim server. During the first step in the installation, I started seeing errors like the one pasted below (only for numbers larger than about 60000). After installing the TIGER data (as specified at the bottom of the installation instructions page...'''
date = "2014-01-19T08:00:00Z"
lastmod = "2014-02-27T11:39:00Z"
weight = 29964
keywords = [ "tiger", "nominatim" ]
aliases = [ "/questions/29964" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [nominatim problem after installing TIGER data](/questions/29964/nominatim-problem-after-installing-tiger-data)

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
<span id="post-29964-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29964-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-29964-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'm trying to install TIGER data on a local Nominatim server.</p>
<p>During the first step in the installation, I started seeing errors like the one pasted below (only for numbers larger than about 60000).</p>
<p>After installing the TIGER data (as specified at the bottom of the installation instructions page) it stopped working fine.</p>
<p>Reverse geo queries return blank pages, if I view the source I only see "1" on the page. Geo coding queries seem not to find any results.</p>
<p>The table location_property_tiger still exists.</p>
<p>Any clues? Thanks, Raz</p>
<pre><code>Traceback (most recent call last):
  File &quot;/home/raz/Downloads/Nominatim-2.1/utils/tigerAddressImport.py&quot;, line 4064, in &lt;module&gt;
    shape_to_osm( shape, osm, id )
  File &quot;/home/raz/Downloads/Nominatim-2.1/utils/tigerAddressImport.py&quot;, line 3955, in shape_to_osm
    parsed_features = parse_shp_for_osm( shp_filename )
  File &quot;/home/raz/Downloads/Nominatim-2.1/utils/tigerAddressImport.py&quot;, line 3475, in parse_shp_for_osm
    tags.update( fipsstate(statefp, countyfp) )
  File &quot;/home/raz/Downloads/Nominatim-2.1/utils/tigerAddressImport.py&quot;, line 3344, in fipsstate
    county = county_fips[county_fips_code]
KeyError: &#39;60010&#39;
Failed parse (/data1/EDGES/tl_2013_60010_edges.zip)</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiger" rel="tag" title="see questions tagged &#39;tiger&#39;">tiger</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Jan '14, 08:00</strong></p>
<img src="https://secure.gravatar.com/avatar/84ebb95a07dd884e34f0170b07b1d652?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RazAlon&#39;s gravatar image" />
<p><span>RazAlon</span><br />
<span class="score" title="61 reputation points">61</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RazAlon has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Feb '14, 11:56</strong> </span></p>
</div>
</div>
<div id="comments-container-29964" class="comments-container">
<span id="29999"></span>
<div id="comment-29999" class="comment">
<div id="post-29999-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you check if the table <code>location_property_tiger</code> still exists in your DB?</p>
</div>
<div id="comment-29999-info" class="comment-info">
<span class="comment-age">(20 Jan '14, 08:20)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="30012"></span>
<div id="comment-30012" class="comment">
<div id="post-30012-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes, it's there</p>
</div>
<div id="comment-30012-info" class="comment-info">
<span class="comment-age">(20 Jan '14, 12:00)</span> <span class="comment-user userinfo">RazAlon</span>
</div>
</div>
</div>
<div id="comment-tools-29964" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29964-form-container" class="comment-form-container">
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

<span id="30873"></span>

<div id="answer-container-30873" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30873-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30873-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-30873-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="RazAlon has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your problems are not related to the error messages you got during import. They just indicate that some edge files couldn't be processed and have been skipped. All other edge files will have worked fine.</p>
<p>To find the source of your problem you need to find out more about what exactly happens when sending the requests. A few places to start looking:</p>
<ul>
<li>Check the postgresql log for errors.</li>
<li>Run the query with the additional parameter <code>debug=1</code>. It should give you a lot of debug output. See if you can find something about an SQL error there.</li>
<li>Make sure the php code has not been modified and there are no syntax errors in <code>setting/local.php</code>.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Feb '14, 12:32</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-30873" class="comments-container">
<span id="31074"></span>
<div id="comment-31074" class="comment">
<div id="post-31074-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>thank you for the advice. it was due to "www-data" versus "apache" username. I should have imported the TIGER data before changing the username, or, change back, import, and change back again... :)</p>
</div>
<div id="comment-31074-info" class="comment-info">
<span class="comment-age">(27 Feb '14, 11:39)</span> <span class="comment-user userinfo">RazAlon</span>
</div>
</div>
</div>
<div id="comment-tools-30873" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30873-form-container" class="comment-form-container">
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

