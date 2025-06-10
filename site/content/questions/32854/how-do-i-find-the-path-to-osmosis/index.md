+++
type = "question"
title = "How do I find the &quot;path-to-osmosis&quot;"
description = '''https://wiki.openstreetmap.org/wiki/Osmosis/PostGIS_Setup says psql -d osm -f &amp;lt;path-to-osmosis&amp;gt;/package/script/pgsimple_schema_0.6.sql  I am on Ubuntu. osmosis runs from /usr/bin/osmosis but this is not the path where the scripts reside. Where can I find them?'''
date = "2014-05-04T19:23:00Z"
lastmod = "2014-05-08T20:57:00Z"
weight = 32854
keywords = [ "osmosis" ]
aliases = [ "/questions/32854" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How do I find the "path-to-osmosis"](/questions/32854/how-do-i-find-the-path-to-osmosis)

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
<span id="post-32854-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32854-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32854-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Osmosis/PostGIS_Setup">https://wiki.openstreetmap.org/wiki/Osmosis/PostGIS_Setup</a> says</p>
<pre><code>psql -d osm -f &lt;path-to-osmosis&gt;/package/script/pgsimple_schema_0.6.sql</code></pre>
<p>I am on Ubuntu. osmosis runs from /usr/bin/osmosis but this is not the path where the scripts reside. Where can I find them?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 May '14, 19:23</strong></p>
<img src="https://secure.gravatar.com/avatar/763e51406d48132ced03848e9e7b0fc0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="snupo&#39;s gravatar image" />
<p><span>snupo</span><br />
<span class="score" title="96 reputation points">96</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="snupo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 May '14, 18:43</strong> </span></p>
</div>
</div>
<div id="comments-container-32854" class="comments-container">
&#10;</div>
<div id="comment-tools-32854" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32854-form-container" class="comment-form-container">
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

<span id="32855"></span>

<div id="answer-container-32855" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32855-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32855-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-32855-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="snupo has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>sudo find / -name pgsimple_schema_0.6.sql -print</p>
<p>naturally only works if the file in question is actually present on your system</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 May '14, 19:59</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 May '14, 20:00</strong> </span></p>
</div>
</div>
<div id="comments-container-32855" class="comments-container">
<span id="33008"></span>
<div id="comment-33008" class="comment">
<div id="post-33008-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... or, on a system which supports "locate", as modern Ubuntu versions do by default:</p>
<p>locate pgsimple_schema_0.6.sql</p>
<p>The database that it uses is updated by an "updatedb" process that usually runs from cron once a day. You can run it manually as root if you want to.</p>
</div>
<div id="comment-33008-info" class="comment-info">
<span class="comment-age">(08 May '14, 20:57)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-32855" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32855-form-container" class="comment-form-container">
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

