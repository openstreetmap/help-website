+++
type = "question"
title = "Extract street names"
description = '''Hello, I am a functional tester for a map data validation software developed by company. They need me to validate the quantity/quality of map data. I need a list of street names present in Saudi Arabia esp Riyadh,Dammam,Makkah and Madinah. Please help!'''
date = "2012-11-22T18:26:00Z"
lastmod = "2012-11-23T11:11:00Z"
weight = 17903
keywords = [ "streetnames", "extract", "saudi_arabia", "data" ]
aliases = [ "/questions/17903" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extract street names](/questions/17903/extract-street-names)

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
<span id="post-17903-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17903-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17903-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I am a functional tester for a map data validation software developed by company. They need me to validate the quantity/quality of map data. I need a list of street names present in Saudi Arabia esp Riyadh,Dammam,Makkah and Madinah.</p>
<p>Please help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-saudi_arabia" rel="tag" title="see questions tagged &#39;saudi_arabia&#39;">saudi_arabia</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Nov '12, 18:26</strong></p>
<img src="https://secure.gravatar.com/avatar/bb0ec1aad333aab8e2d929f86fd3c963?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aneess&#39;s gravatar image" />
<p><span>Aneess</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aneess has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> retagged <strong>23 Nov '12, 05:36</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/01d01832dff61a6bcf68913f1dc001bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Circeus&#39;s gravatar image" />
<p><span>Circeus</span><br />
<span class="score" title="583 reputation points">583</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span></p>
</div>
</div>
<div id="comments-container-17903" class="comments-container">
&#10;</div>
<div id="comment-tools-17903" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17903-form-container" class="comment-form-container">
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

<span id="17905"></span>

<div id="answer-container-17905" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17905-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17905-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-17905-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Get some raw OSM data via geofabrik.de or overpassAPI for the regions that you need.</p>
<p>If neccesary, cut it with osmosis or osmconverter. Maybe osmfilter can also be helpful.</p>
<p>Then convert the data into a CSV file with the help of osmconverter.</p>
<p>Load that CSV data in any capable spreadsheet software like LibreofficeCalc or any database. Sort it about highway= and name= ... and delete any doublettes.</p>
<p>All needed sites and software is described in the OSM wiki, do a search there about each key word.</p>
<p>Add a comment here if you get stuck anywhere.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Nov '12, 20:31</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-17905" class="comments-container">
<span id="17914"></span>
<div id="comment-17914" class="comment">
<div id="post-17914-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Converting to CSV is not strictly necessary : if you know a bit of SQL, querying the database directly might be more convenient.</p>
</div>
<div id="comment-17914-info" class="comment-info">
<span class="comment-age">(23 Nov '12, 10:53)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="17916"></span>
<div id="comment-17916" class="comment">
<div id="post-17916-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Querying the database requires that the data is in the database to start with so you'd have to use osmosis/osm2pgsql/imposm to import it. Another option is using Overpass to directly ask for anything tagged highway=*.</p>
</div>
<div id="comment-17916-info" class="comment-info">
<span class="comment-age">(23 Nov '12, 11:11)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-17905" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17905-form-container" class="comment-form-container">
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

