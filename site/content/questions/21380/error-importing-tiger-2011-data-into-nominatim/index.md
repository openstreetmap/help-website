+++
type = "question"
title = "Error importing tiger 2011 data into nominatim"
description = '''When trying to import the the Tiger 2011 data into nominatim, I get the following parse error: ./utils/imports.php --parse-tiger-2011 data/tiger/ftp2.census.gov/geo/tiger/TIGER2011/EDGES Processing 01001...  File &quot;/usr/src/nominatim/utils/tigerAddressImport.py&quot;, line 3340  raise KeyError, &#x27;missing F...'''
date = "2013-04-11T00:24:00Z"
lastmod = "2013-04-12T07:04:00Z"
weight = 21380
keywords = [ "tiger", "import", "nominatim" ]
aliases = [ "/questions/21380" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Error importing tiger 2011 data into nominatim](/questions/21380/error-importing-tiger-2011-data-into-nominatim)

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
<span id="post-21380-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21380-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21380-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When trying to import the the Tiger 2011 data into nominatim, I get the following parse error:</p>
<pre><code>./utils/imports.php --parse-tiger-2011 data/tiger/ftp2.census.gov/geo/tiger/TIGER2011/EDGES
Processing 01001...
  File &quot;/usr/src/nominatim/utils/tigerAddressImport.py&quot;, line 3340
    raise KeyError, &#39;missing FIPS code&#39;, fips
                  ^
SyntaxError: invalid syntax
Failed parse (/usr/src/nominatim/data/tiger/ftp2.census.gov/geo/tiger/TIGER2011/EDGES/tl_2011_01001_edges.zip)</code></pre>
<p>I am following the directions from the answer to this question: <a href="https://help.openstreetmap.org/questions/12150/missing-house-numbers-in-local-nominatim-instance">https://help.openstreetmap.org/questions/12150/missing-house-numbers-in-local-nominatim-instance</a></p>
<p>Does this still work?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiger" rel="tag" title="see questions tagged &#39;tiger&#39;">tiger</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Apr '13, 00:24</strong></p>
<img src="https://secure.gravatar.com/avatar/705d24784cee7f6cddc6a1e4211513cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="montanalow&#39;s gravatar image" />
<p><span>montanalow</span><br />
<span class="score" title="40 reputation points">40</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="montanalow has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-21380" class="comments-container">
&#10;</div>
<div id="comment-tools-21380" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21380-form-container" class="comment-form-container">
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

<span id="21405"></span>

<div id="answer-container-21405" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21405-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21405-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-21405-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It still works. Make sure that you use python 2.x and not python 3.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Apr '13, 14:07</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-21405" class="comments-container">
<span id="21406"></span>
<div id="comment-21406" class="comment">
<div id="post-21406-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thanks, I was use using python 3, and that was the problem. Works perfect with python 2.</p>
</div>
<div id="comment-21406-info" class="comment-info">
<span class="comment-age">(11 Apr '13, 14:33)</span> <span class="comment-user userinfo">montanalow</span>
</div>
</div>
<span id="21429"></span>
<div id="comment-21429" class="comment">
<div id="post-21429-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I just finished the import, and it looks like FIPS codes &gt; 60000 are not handled by tigerAddressImport.py, so they generate they same error, even though there is tiger EDGE data.</p>
<p>It looks like FIPS 60010 is American Somoa (not one of the 50 states), so I'm guessing this is intended behavior.</p>
</div>
<div id="comment-21429-info" class="comment-info">
<span class="comment-age">(12 Apr '13, 01:23)</span> <span class="comment-user userinfo">montanalow</span>
</div>
</div>
<span id="21438"></span>
<div id="comment-21438" class="comment">
<div id="post-21438-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Indeed, that is a known limitation. It should only be a matter of adding the FIPS codes in tigerAddressImport.py to make it work.</p>
</div>
<div id="comment-21438-info" class="comment-info">
<span class="comment-age">(12 Apr '13, 07:04)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
</div>
<div id="comment-tools-21405" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21405-form-container" class="comment-form-container">
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

