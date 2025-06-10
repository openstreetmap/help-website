+++
type = "question"
title = "OsmConvert - cannot merge multiple maps"
description = '''I use osmconvert tool to merge maps. This tool merges 3 maps correctly, however if I merge 16 maps, then I see the following error:  osmconvert Error: could not get 183500800 bytes of memory  This my command: osmconvert.exe asia/armenia-latest.o5m asia/azerbaijan-latest.o5m  europe/belarus-latest.o5...'''
date = "2019-12-10T19:21:00Z"
lastmod = "2019-12-11T19:55:00Z"
weight = 72068
keywords = [ "osmconvert" ]
aliases = [ "/questions/72068" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [OsmConvert - cannot merge multiple maps](/questions/72068/osmconvert-cannot-merge-multiple-maps)

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
<span id="post-72068-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72068-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-72068-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I use <a href="https://wiki.openstreetmap.org/wiki/Osmconvert#Windows">osmconvert tool</a> to merge maps. This tool merges 3 maps correctly, however if I merge 16 maps, then I see the following error:</p>
<blockquote>
<p>osmconvert Error: could not get 183500800 bytes of memory</p>
</blockquote>
<p>This my command:</p>
<pre><code>osmconvert.exe asia/armenia-latest.o5m asia/azerbaijan-latest.o5m 
europe/belarus-latest.o5m asia/kazakhstan-latest.o5m asia/kyrgyzstan-latest.o5m 
europe/moldova-latest.o5m russia-latest.o5m asia/tajikistan-latest.o5m 
asia/uzbekistan-latest.o5m europe/bulgaria-latest.o5m europe/hungary-latest.o5m 
europe/poland-latest.o5m europe/romania-latest.o5m europe/slovakia-latest.o5m 
europe/ukraine-latest.o5m europe/czech-republic-latest.o5m -o=merged.o5m</code></pre>
<p>Could you say what am I doing wrong? How can I solve this problem?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Dec '19, 19:21</strong></p>
<img src="https://secure.gravatar.com/avatar/cbd5c282ccb929604467e3b3f900b0d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CuriosityBeginner&#39;s gravatar image" />
<p><span>CuriosityBeg...</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CuriosityBeginner has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72068" class="comments-container">
<span id="72071"></span>
<div id="comment-72071" class="comment">
<div id="post-72071-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It sounds like your system doesn't have enough memory to perform this operation. Maybe try merging in multiple steps (e.g. merge the Asian ones together, merge the European ones together, then merge those two files together).</p>
</div>
<div id="comment-72071-info" class="comment-info">
<span class="comment-age">(10 Dec '19, 23:16)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="72073"></span>
<div id="comment-72073" class="comment">
<div id="post-72073-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/8189/alester">@alester</a> thanks for your comment. However, the error is the same, even only Euopean maps are merged. Maybe you have another ideas?</p>
</div>
<div id="comment-72073-info" class="comment-info">
<span class="comment-age">(11 Dec '19, 19:55)</span> <span class="comment-user userinfo">CuriosityBeg...</span>
</div>
</div>
</div>
<div id="comment-tools-72068" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72068-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

