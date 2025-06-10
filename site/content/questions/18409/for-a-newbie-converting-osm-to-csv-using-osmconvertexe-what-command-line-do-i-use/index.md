+++
type = "question"
title = "For a newbie, converting OSM to CSV using OSMConvert.exe, what command line do I use?"
description = '''I have installed osmconvert.exe, put it in the same folder as the .osm file, but now I can&#x27;t figure out what code exactly to write to convert it to .csv (even though i&#x27;ve read the help pages) Ive been running the .exe file, then typing into the box: (taken from https://wiki.openstreetmap.org/wiki/Os...'''
date = "2012-12-13T10:07:00Z"
lastmod = "2014-04-23T08:53:00Z"
weight = 18409
keywords = [ "osmconvert", "csv", "osm", "convert" ]
aliases = [ "/questions/18409" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [For a newbie, converting OSM to CSV using OSMConvert.exe, what command line do I use?](/questions/18409/for-a-newbie-converting-osm-to-csv-using-osmconvertexe-what-command-line-do-i-use)

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
<span id="post-18409-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18409-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18409-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have installed osmconvert.exe, put it in the same folder as the .osm file, but now I can't figure out what code exactly to write to convert it to .csv (even though i've read the help pages) Ive been running the .exe file, then typing into the box: (taken from <a href="https://wiki.openstreetmap.org/wiki/Osmconvert#Writing_CSV_Files)">https://wiki.openstreetmap.org/wiki/Osmconvert#Writing_CSV_Files)</a> country.osm -o=country.csv ...or... country.osm --all-to-nodes -o=country.csv ..or... country.osm --all-to-nodes --csv="<span>@id</span> <span>@lat</span> <span>@lon</span>" -o=country.csv and many variations thereof. But none of these work, the box just disappears! What am I doing wrong? Thankyou :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-convert" rel="tag" title="see questions tagged &#39;convert&#39;">convert</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Dec '12, 10:07</strong></p>
<img src="https://secure.gravatar.com/avatar/b06a829efb1deddeae2605b0015eaa15?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jas1405&#39;s gravatar image" />
<p><span>jas1405</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jas1405 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18409" class="comments-container">
<span id="18413"></span>
<div id="comment-18413" class="comment">
<div id="post-18413-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Can you create a pastebin with your exact typing and the exact output?</p>
<p><a href="http://pastebin.com/">http://pastebin.com/</a></p>
</div>
<div id="comment-18413-info" class="comment-info">
<span class="comment-age">(13 Dec '12, 13:30)</span> <span class="comment-user userinfo">Sanderd17</span>
</div>
</div>
</div>
<div id="comment-tools-18409" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18409-form-container" class="comment-form-container">
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

<span id="18430"></span>

<div id="answer-container-18430" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18430-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18430-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-18430-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Are you sure to have started osmconvert from the command line? The interactive user interface "Bert" is not able to handle .csv functions. Thus you better should not start osmconvert by doubleclick if you want to create .csv output.</p>
<p>Please open a command line window change into your directory (use "cd" command) and enter for example:</p>
<p><code>osmconvert country.osm --csv="</code><span><code>@id</code></span><code> </code><span><code>@lat</code></span><code> </code><span><code>@lon</code></span><code> name amenity" -o=country.csv</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Dec '12, 21:18</strong></p>
<img src="https://secure.gravatar.com/avatar/3b5b4abfedd46928c7cd0d5cbf907ed3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marqqs&#39;s gravatar image" />
<p><span>Marqqs</span><br />
<span class="score" title="448 reputation points">448</span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marqqs has 2 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-18430" class="comments-container">
<span id="32547"></span>
<div id="comment-32547" class="comment">
<div id="post-32547-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>many many thanks</p>
</div>
<div id="comment-32547-info" class="comment-info">
<span class="comment-age">(23 Apr '14, 08:48)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
<span id="32548"></span>
<div id="comment-32548" class="comment">
<div id="post-32548-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>can i apply this and - additionally get the tags for adress too</p>
</div>
<div id="comment-32548-info" class="comment-info">
<span class="comment-age">(23 Apr '14, 08:53)</span> <span class="comment-user userinfo">say_hello_to...</span>
</div>
</div>
</div>
<div id="comment-tools-18430" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18430-form-container" class="comment-form-container">
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

