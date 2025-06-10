+++
type = "question"
title = "Nominatim: relation place does not exist"
description = '''Good day I&#x27;ve installed Nominatim and am now trying to to import my country using the command: ./utils/setup.php --osm-file ../../all-data.pbf --all --osm2pgsql-cache 512 2&amp;gt;&amp;amp;1  It starts off with NOTICE: table &quot;place&quot; does not exist, Skipping. Afterwards, it seems to work fine until it tried ...'''
date = "2018-11-02T10:16:00Z"
lastmod = "2018-11-02T11:02:00Z"
weight = 66627
keywords = [ "nominatim" ]
aliases = [ "/questions/66627" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim: relation place does not exist](/questions/66627/nominatim-relation-place-does-not-exist)

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
<span id="post-66627-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66627-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66627-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Good day</p>
<p>I've installed Nominatim and am now trying to to import my country using the command:</p>
<pre><code>./utils/setup.php --osm-file ../../all-data.pbf --all --osm2pgsql-cache 512 2&gt;&amp;1</code></pre>
<p>It starts off with <strong>NOTICE: table "place" does not exist, Skipping</strong>. Afterwards, it seems to work fine until it tried to get data from the "place" table (which does not exist).</p>
<p>The error is: <strong>relation place does not exist</strong>.</p>
<p>Why does the place table not exist? Shouldn't all required tables be created by the setup.php file? Or am I missing something?</p>
<p>EDIT:</p>
<p>I should point out that I used osmconvert to merge two regions. I'm now trying to import only one of them and while it still gives me the same notice, it seems to be importing the data. Maybe something went wrong with the osmconvert process. Will update here if the one region actually imports successfully and maybe just import the second with update.php (although I think its slower).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Nov '18, 10:16</strong></p>
<img src="https://secure.gravatar.com/avatar/15af72fd19fceb8e6e76bac3db6418d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesleyjmertz&#39;s gravatar image" />
<p><span>wesleyjmertz</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesleyjmertz has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Nov '18, 10:34</strong> </span></p>
</div>
</div>
<div id="comments-container-66627" class="comments-container">
<span id="66629"></span>
<div id="comment-66629" class="comment">
<div id="post-66629-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You can ignore the NOTICE output. In SQL Nominatim wants to replace tables/functions and postgresql prints this if it previously doesn't exist (expected during a first installation). We haven't found a way to disable those yet. Place table not existing after the setup.php run would mean no suitable places to import were found in the input data, maybe the region is too small.</p>
</div>
<div id="comment-66629-info" class="comment-info">
<span class="comment-age">(02 Nov '18, 11:02)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
</div>
<div id="comment-tools-66627" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66627-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

