+++
type = "question"
title = "comparisons in lua called from osm2pgsql"
description = '''In a lua style file called from osm2pgsql, the following code works exactly as expected - the comparison of the two numbers works as expected: -- ---------------------------------------------------------------------------- -- Big peaks -- -------------------------------------------------------------...'''
date = "2019-10-25T22:04:00Z"
lastmod = "2019-10-26T11:03:00Z"
weight = 71333
keywords = [ "lua", "osm2pgsql", "arithmetic" ]
aliases = [ "/questions/71333" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [comparisons in lua called from osm2pgsql](/questions/71333/comparisons-in-lua-called-from-osm2pgsql)

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
<span id="post-71333-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71333-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71333-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In a lua style file called from osm2pgsql, the following code works exactly as expected - the comparison of the two numbers works as expected:</p>
<pre><code>-- ----------------------------------------------------------------------------
-- Big peaks
-- ----------------------------------------------------------------------------
   if ( keyvalues[&quot;natural&quot;] == &quot;peak&quot; ) then
      keyvalues[&quot;name&quot;] = &quot;before&quot;
&#10;      if ( keyvalues[&quot;ele&quot;] == nil ) then
         keyvalues[&quot;name&quot;] = &quot;elenil&quot;
      else
         keyvalues[&quot;name&quot;] = &quot;elenotnil&quot;
         if ( tonumber( keyvalues[&quot;ele&quot;] ) == 900 ) then
            keyvalues[&quot;name&quot;] = &quot;bigpeak&quot;
         else
            keyvalues[&quot;name&quot;] = &quot;notabigpeak&quot;
         end
      end
   end</code></pre>
<p>However, if I change the comparison to the following:</p>
<pre><code>    if ( tonumber( keyvalues[&quot;ele&quot;] ) &gt; 900 ) then</code></pre>
<p>then the following error occurs:</p>
<pre><code>Using lua based tag processing pipeline with script /home/renderaccount/src/SomeoneElse-style/style.lua
Using projection SRS 3857 (Spherical Mercator)
Setting up table: planet_osm_point
Osm2pgsql failed due to ERROR: SELECT * FROM planet_osm_point LIMIT 0 failed: ERROR:  relation &quot;planet_osm_point&quot; does not exist
LINE 1: SELECT * FROM planet_osm_point LIMIT 0</code></pre>
<p>I'd expect this to work, because the "tonumber" seems to work OK and <a href="https://www.lua.org/manual/5.0/manual.html#2.5.1">this page</a> suggests to me that "&gt;" ought to work there. osm2pgsql is "osm2pgsql version 0.96.0 (64 bit id space)", lua according to "dpkg -l" seems to be 5.1 or 5.2.</p>
<p>Any ideas?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span> <span class="post-tag tag-link-arithmetic" rel="tag" title="see questions tagged &#39;arithmetic&#39;">arithmetic</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Oct '19, 22:04</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Oct '19, 22:05</strong> </span></p>
</div>
</div>
<div id="comments-container-71333" class="comments-container">
&#10;</div>
<div id="comment-tools-71333" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71333-form-container" class="comment-form-container">
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

<span id="71336"></span>

<div id="answer-container-71336" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71336-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-71336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><code>tonumber()</code> returns <code>nil</code> when the string parameter is not something that can be converted into a number. You can compare <code>nil</code> against a number with the <code>==</code> operator but not with <code>&gt;</code>:</p>
<p><code>me@machine:~$ lua -e 'print(tonumber("1m"))' nil me@machine:~$ lua -e 'print(tonumber("1m") == 1)' false me@machine:~$ lua -e 'print(tonumber("1m") &gt; 1)' lua: (command line):1: attempt to compare number with nil</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Oct '19, 09:04</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-71336" class="comments-container">
<span id="71338"></span>
<div id="comment-71338" class="comment">
<div id="post-71338-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Often the easiest way to get round this is by adding an <code>or 0</code>, so <code>(tonumber(keyvalues["ele"]) or 0)&gt;900</code>.</p>
</div>
<div id="comment-71338-info" class="comment-info">
<span class="comment-age">(26 Oct '19, 11:03)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-71336" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71336-form-container" class="comment-form-container">
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

