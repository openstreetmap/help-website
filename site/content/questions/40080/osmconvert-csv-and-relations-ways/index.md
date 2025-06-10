+++
type = "question"
title = "osmconvert - CSV and relations / ways"
description = '''Hello, I have a question. Using osmconvert can reasonably be saved in CSV relations and ways? With the nodes do not have a problem. Simply: ./osmconvert europe-latest.osm.pbf --out-csv --csv=&quot;@id @lat @lon&quot;  The current record in the CSV relations and ways, however, does not make sense to me ... It ...'''
date = "2015-01-06T20:45:00Z"
lastmod = "2015-01-07T20:44:00Z"
weight = 40080
keywords = [ "osmconvert", "csv" ]
aliases = [ "/questions/40080" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [osmconvert - CSV and relations / ways](/questions/40080/osmconvert-csv-and-relations-ways)

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
<span id="post-40080-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40080-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40080-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I have a question. Using osmconvert can reasonably be saved in CSV relations and ways?</p>
<p>With the nodes do not have a problem. Simply:</p>
<pre><code>./osmconvert europe-latest.osm.pbf --out-csv --csv=&quot;@id @lat @lon&quot;</code></pre>
<p>The current record in the CSV relations and ways, however, does not make sense to me ...</p>
<p>It looks like this:</p>
<pre><code>relation    3903876     
relation    3903985     
relation    3903986     
relation    3903987     
relation    3903988     
relation    3903989     
relation    3903990</code></pre>
<p>How to identify what is in relation to what?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Jan '15, 20:45</strong></p>
<img src="https://secure.gravatar.com/avatar/874f428b539f501361c6a9947fe859f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rysiu&#39;s gravatar image" />
<p><span>Rysiu</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rysiu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-40080" class="comments-container">
&#10;</div>
<div id="comment-tools-40080" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40080-form-container" class="comment-form-container">
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

<span id="40081"></span>

<div id="answer-container-40081" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40081-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40081-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-40081-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Rysiu has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Ways and relations are too complex to be output in a CSV file. If you want to process ways and relations, other avenues might be more promising, e.g. writing a program that reads the OSM file (using e.g. the Osmium library), or loading the OSM file into a database with osm2pgsql and then running your analysis on the database.</p>
<p>If you really need a text file with one OSM object per line, try <a href="https://github.com/osmcode/libosmium-manual/blob/master/src/input-and-output.md#opl-object-per-line-format">Osmium's "OPL" format.</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jan '15, 22:42</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-40081" class="comments-container">
<span id="40082"></span>
<div id="comment-40082" class="comment">
<div id="post-40082-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How big will the MySQL database if the file osm.bz2 takes almost 900 MB?</p>
</div>
<div id="comment-40082-info" class="comment-info">
<span class="comment-age">(06 Jan '15, 22:54)</span> <span class="comment-user userinfo">Rysiu</span>
</div>
</div>
</div>
<div id="comment-tools-40081" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40081-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40090"></span>

<div id="answer-container-40090" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40090-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40090-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40090-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As <a href="http://help.openstreetmap.org/users/104/frederik-ramm">@Frederik</a> said, relations &amp; ways are complicated. <code>osm2psql</code> can output a <code>pgsimp</code> format, which is a directory of tab separated files (which are like CSVs). It might do what you want.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jan '15, 10:26</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-40090" class="comments-container">
&#10;</div>
<div id="comment-tools-40090" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40090-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="40105"></span>

<div id="answer-container-40105" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-40105-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-40105-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-40105-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <strong>--csv="<a href="http://help.openstreetmap.org/users/260/idoneus">@id</a> <a href="http://help.openstreetmap.org/users/5110/latroc">@lat</a> <a href="http://help.openstreetmap.org/users/1350/longestaugust">@lon</a>"</strong> in your question suggests that you need just IDs and coordinates. Maybe the option <strong>--all-to-nodes</strong> will help. It will retrieve the coordinates for all your ways and relations.</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Osmconvert#Dispose_of_Ways_and_Relations_and_Convert_them_to_Nodes">https://wiki.openstreetmap.org/wiki/Osmconvert#Dispose_of_Ways_and_Relations_and_Convert_them_to_Nodes</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jan '15, 20:44</strong></p>
<img src="https://secure.gravatar.com/avatar/3b5b4abfedd46928c7cd0d5cbf907ed3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marqqs&#39;s gravatar image" />
<p><span>Marqqs</span><br />
<span class="score" title="448 reputation points">448</span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marqqs has 2 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-40105" class="comments-container">
&#10;</div>
<div id="comment-tools-40105" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-40105-form-container" class="comment-form-container">
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

