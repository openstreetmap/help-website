+++
type = "question"
title = "osm2pqsql and lua"
description = '''I installed osm2pqsql the other day. At one point it said &quot;lua libraries not found. You will NOT be able to use lua scripts for tag transform.&quot;. I had no idea what a lua was or why I would want one, so I had a bit of a read here and here. After reading &quot;This allows you to unify disparate tagging (fo...'''
date = "2013-11-25T20:36:00Z"
lastmod = "2013-12-26T16:23:00Z"
weight = 28465
keywords = [ "lua", "osm2pgsql" ]
aliases = [ "/questions/28465" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [osm2pqsql and lua](/questions/28465/osm2pqsql-and-lua)

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
<span id="post-28465-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28465-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-28465-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I installed osm2pqsql the other day. At one point it said <code>"lua libraries not found. You will NOT be able to use lua scripts for tag transform."</code>. I had no idea what a <code>lua</code> was or why I would want one, so I had a bit of a read <a href="https://lists.openstreetmap.org/pipermail/dev/2013-April/026885.html">here</a> and <a href="https://github.com/openstreetmap/osm2pgsql/blob/master/docs/lua.md">here</a>. After reading "This allows you to unify disparate tagging (for example, highway=path; foot=yes and highway=footway)" it now sounds very useful indeed **.</p>
<p>There's what seems to be an example <a href="https://github.com/openstreetmap/osm2pgsql/blob/master/style.lua">here</a>, but what isn't clear, unfortunately, is whether the lua script passed to osm2pgsql on the command line has got to implement all of what's currently in <a href="https://github.com/openstreetmap/osm2pgsql/blob/master/style.lua">style.lua</a>, or whether something much simpler (for example just rewriting one tag as another) is also possible?</p>
<p>** I've done this to Garmin maps for years - generally sticking extra info into the name tag to reflect things such as the legal status of a footpath. It would be useful to be able to do this elsewhere too.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Nov '13, 20:36</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jan '15, 11:24</strong> </span></p>
</div>
</div>
<div id="comments-container-28465" class="comments-container">
&#10;</div>
<div id="comment-tools-28465" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28465-form-container" class="comment-form-container">
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

<span id="28466"></span>

<div id="answer-container-28466" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28466-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28466-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-28466-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You do need to implement what's included in style.lua. This is used in place of parts of the default, native processing. However, you can of course simply alter the existing style.lua for your own purposes, perhaps starting with filter_tags_way as a first step.</p>
<p>I'd very strongly recommend it if you're doing anything with rights of way, in particular. osm2pgsql's Lua processing has made my workflow much simpler and faster for exactly this reason.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Nov '13, 00:41</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-28466" class="comments-container">
<span id="29341"></span>
<div id="comment-29341" class="comment">
<div id="post-29341-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks - works a treat. What I ended up doing was:</p>
<p><a href="https://github.com/SomeoneElseOSM/designation-style">https://github.com/SomeoneElseOSM/designation-style</a></p>
</div>
<div id="comment-29341-info" class="comment-info">
<span class="comment-age">(26 Dec '13, 16:23)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-28466" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28466-form-container" class="comment-form-container">
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

