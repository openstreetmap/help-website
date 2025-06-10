+++
type = "question"
title = "Problems reverting changeset"
description = '''Hi, As a continuation of this question I would like to revert changeset 21219686. But I am having trouble doing this with two different methods.   JOSM reverter plugin - the connection times out.   Perl script - I get the following error: me@server ~/revert $ perl revert.pl 21219686 Use of uninitial...'''
date = "2014-03-23T21:06:00Z"
lastmod = "2014-03-24T21:09:00Z"
weight = 31804
keywords = [ "changeset", "revert" ]
aliases = [ "/questions/31804" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Problems reverting changeset](/questions/31804/problems-reverting-changeset)

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
<span id="post-31804-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31804-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31804-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>As a continuation of <a href="https://help.openstreetmap.org/questions/31732/oops-inadvertently-deleted-a-way-need-help-restoring">this question</a> I would like to revert changeset <a href="http://www.openstreetmap.org/changeset/21219686">21219686</a>. But I am having trouble doing this with two different methods.</p>
<ol>
<li><p>JOSM reverter plugin - the connection times out.</p></li>
<li><p>Perl script - I get the following error:</p>
<pre><code>me@server ~/revert $ perl revert.pl 21219686
Use of uninitialized value $current_cs_or_comment in pattern match (m//) at revert.pl line 45.
Use of uninitialized value $comment in string eq at revert.pl line 52.
PUT changeset/create
[[deleted line with HTML tags which don&#39;t show up nicely in help.openstreetmap.org editor]]
GET http://api06.dev.openstreetmap.org/api/0.6/changeset/21219686/download... 404 Not Found (0b)
changeset 21219686 cannot be retrieved: 404 Not Found</code></pre></li>
</ol>
<p>Can anyone help with this? Or just go ahead and do the revert for us?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changeset" rel="tag" title="see questions tagged &#39;changeset&#39;">changeset</span> <span class="post-tag tag-link-revert" rel="tag" title="see questions tagged &#39;revert&#39;">revert</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Mar '14, 21:06</strong></p>
<img src="https://secure.gravatar.com/avatar/ed0b2a6757c7515c4f9c529b2eb08ae3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eric22&#39;s gravatar image" />
<p><span>eric22</span><br />
<span class="score" title="401 reputation points">401</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eric22 has 2 accepted answers">50%</span></p>
</div>
</div>
<div id="comments-container-31804" class="comments-container">
&#10;</div>
<div id="comment-tools-31804" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31804-form-container" class="comment-form-container">
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

<span id="31805"></span>

<div id="answer-container-31805" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31805-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31805-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-31805-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="eric22 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You need to add a changeset comment when calling the Perl code. For example:</p>
<pre><code>perl revert.pl 21219686 &quot;Reverting damage in changeset 21219686&quot;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Mar '14, 21:58</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-31805" class="comments-container">
<span id="31806"></span>
<div id="comment-31806" class="comment">
<div id="post-31806-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That gets rid of the two "Use of..." errors at the top, but not the 404...</p>
<p>Interestingly, when I set "dryrun=0" in the config file and run again, the 404 error disappears, but instead I get "cannot create changeset: 401 Authorization Required". I wonder if this indicates my name/PW are wrong in the config file. But I've checked pretty closely, I really think they're correct.</p>
</div>
<div id="comment-31806-info" class="comment-info">
<span class="comment-age">(23 Mar '14, 22:09)</span> <span class="comment-user userinfo">eric22</span>
</div>
</div>
<span id="31820"></span>
<div id="comment-31820" class="comment">
<div id="post-31820-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Yes, that's because you're pointing at a test instance on OSM's development server (api06.dev.openstreetmap.org). You need to change this to the URL of the main OSM API. This is documented in the README at <a href="http://svn.openstreetmap.org/applications/utils/revert/README">http://svn.openstreetmap.org/applications/utils/revert/README</a> .</p>
</div>
<div id="comment-31820-info" class="comment-info">
<span class="comment-age">(24 Mar '14, 07:47)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="31858"></span>
<div id="comment-31858" class="comment">
<div id="post-31858-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Richard: Thanks for putting me on the right track. I figured it out :)</p>
</div>
<div id="comment-31858-info" class="comment-info">
<span class="comment-age">(24 Mar '14, 21:09)</span> <span class="comment-user userinfo">eric22</span>
</div>
</div>
</div>
<div id="comment-tools-31805" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31805-form-container" class="comment-form-container">
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

