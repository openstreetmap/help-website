+++
type = "question"
title = "Import data without changeset history"
description = '''Hi,  I downloaded planet-latest.osm and I want to import data for Eastern Europe in a PostgreSQL database. I tested the osmosis command for a small region and what I observed is that it imports all the changeset history. I find this information redundant for my application and I only want to import ...'''
date = "2013-04-15T23:33:00Z"
lastmod = "2013-04-16T13:33:00Z"
weight = 21564
keywords = [ "import", "changeset" ]
aliases = [ "/questions/21564" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Import data without changeset history](/questions/21564/import-data-without-changeset-history)

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
<span id="post-21564-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21564-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21564-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,<br />
</p>
<p>I downloaded planet-latest.osm and I want to import data for Eastern Europe in a PostgreSQL database. I tested the osmosis command for a small region and what I observed is that it imports all the changeset history. I find this information redundant for my application and I only want to import the most recent node from the changeset.<br />
</p>
<p>The command I used:<br />
<em>7z.exe e -so "I:\Restricted\Radu\Facultate\2012-2013\Licenta\planet-latest.osm.bz2" | "C:\Program Files (x86)\osmosis\bin\osmosis.bat" --read-xml file=- --bounding-box left=12.481037 top=41.894315 right=12.485399 bottom=41.891903 --write-pgsql database="europe" user="postgres" password="parola"</em><br />
</p>
<p>How can I do that and in what way will it affect my database in the future if I plan to update data using daily regular diffs.<br />
</p>
<p>Thank you,<br />
Radu-Stefan Zugravu</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Apr '13, 23:33</strong></p>
<img src="https://secure.gravatar.com/avatar/af030346f57b37767fe7e80f23e07d7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="raduzugravu&#39;s gravatar image" />
<p><span>raduzugravu</span><br />
<span class="score" title="31 reputation points">31</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="raduzugravu has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Apr '13, 23:34</strong> </span></p>
</div>
</div>
<div id="comments-container-21564" class="comments-container">
&#10;</div>
<div id="comment-tools-21564" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21564-form-container" class="comment-form-container">
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

<span id="21578"></span>

<div id="answer-container-21578" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21578-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21578-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-21578-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="raduzugravu has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The standard planet file does not include any history, and the "snapshot" schema used by the Osmosis `--write-pgsql`` task you mention does not have room for history information. You must be mistaken.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Apr '13, 10:56</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span> </br></br></p>
</div>
</div>
<div id="comments-container-21578" class="comments-container">
<span id="21580"></span>
<div id="comment-21580" class="comment">
<div id="post-21580-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi,</p>
<p>Maybe I didn't make myself clear so I will try to give you an example. Here are three different nodes from the area pointed above, extracted from planet.osm:<br />
</p>
<p><em>node id="1270510177" version="3" timestamp="2011-08-05T22:00:21Z" uid="430115" user="Emistrac" changeset="8933229" lat="41.8941708" lon="12.4831246"</em><br />
<em>node id="1270510178" version="3" timestamp="2011-08-05T22:00:21Z" uid="430115" user="Emistrac" changeset="8933229" lat="41.8941769" lon="12.4831607"</em><br />
<em>node id="1270511991" version="3" timestamp="2011-08-05T22:00:21Z" uid="430115" user="Emistrac" changeset="8933229" lat="41.8941797" lon="12.4828525"</em><br />
</p>
<p>If I execute a reverse search all 3 nodes will return same result. When I import this to a postgresql database it will create 3 different rows for each row. Is it normal?</p>
</div>
<div id="comment-21580-info" class="comment-info">
<span class="comment-age">(16 Apr '13, 11:35)</span> <span class="comment-user userinfo">raduzugravu</span>
</div>
</div>
<span id="21581"></span>
<div id="comment-21581" class="comment">
<div id="post-21581-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>They're three different nodes (3 different geographical items). To omit any of them would mean that your database is not complete.<br />
</p>
<p>Also, what do you mean by "execute a reverse search" here?</p>
</div>
<div id="comment-21581-info" class="comment-info">
<span class="comment-age">(16 Apr '13, 11:59)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="21585"></span>
<div id="comment-21585" class="comment">
<div id="post-21585-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This is what I mean.<br />
<a href="http://nominatim.openstreetmap.org/reverse?lat=41.8941708&amp;lon=12.4831246">http://nominatim.openstreetmap.org/reverse?lat=41.8941708&amp;lon=12.4831246</a><br />
<a href="http://nominatim.openstreetmap.org/reverse?lat=41.8941769&amp;lon=12.4831607">http://nominatim.openstreetmap.org/reverse?lat=41.8941769&amp;lon=12.4831607</a><br />
<a href="http://nominatim.openstreetmap.org/reverse?lat=41.8941797&amp;lon=12.4828525">http://nominatim.openstreetmap.org/reverse?lat=41.8941797&amp;lon=12.4828525</a><br />
This 3 requests will return the same place. The latitude and longitude values are the ones for the three different nodes listed above. Why is this necessary?</p>
</div>
<div id="comment-21585-info" class="comment-info">
<span class="comment-age">(16 Apr '13, 12:40)</span> <span class="comment-user userinfo">raduzugravu</span>
</div>
</div>
<span id="21587"></span>
<div id="comment-21587" class="comment not_top_scorer">
<div id="post-21587-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In what way is that wrong? If I was at any of those three lat/long combinations I'd say that I was at that momument. What do you expect Nominatim to return for those lat/long combinations?</p>
</div>
<div id="comment-21587-info" class="comment-info">
<span class="comment-age">(16 Apr '13, 12:46)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="21590"></span>
<div id="comment-21590" class="comment">
<div id="post-21590-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Did you look at the data? The first two nodes are part of <a href="https://www.openstreetmap.org/browse/way/44490528">this footway</a> and the third one belongs to <a href="https://www.openstreetmap.org/browse/way/124808569">this building</a>. These are three more or less independent nodes and each of them is useful. They don't have anything to do with a history.</p>
</div>
<div id="comment-21590-info" class="comment-info">
<span class="comment-age">(16 Apr '13, 12:53)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="21592"></span>
<div id="comment-21592" class="comment">
<div id="post-21592-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you scai.<br />
I missinterpreted the data. It all makes sense now.<br />
I am really sorry.</p>
</div>
<div id="comment-21592-info" class="comment-info">
<span class="comment-age">(16 Apr '13, 13:33)</span> <span class="comment-user userinfo">raduzugravu</span>
</div>
</div>
</div>
<div id="comment-tools-21578" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-21578-form-container" class="comment-form-container">
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

