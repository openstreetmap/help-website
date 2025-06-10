+++
type = "question"
title = "Need some clarification for the osm2pgsql multi-backend documentation."
description = '''I was reading the osm2pgsql documentation on github for info on loading a custom lua script but I am confused on some of the instructions. In the file osm2pgsql/docs/lua.md, under the &quot;How To&quot; section, it gives as an example: osm2pgsql -S your.style --tag-transform-script your.lua --hstore-all extra...'''
date = "2016-08-31T15:25:00Z"
lastmod = "2016-08-31T15:25:00Z"
weight = 51843
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/51843" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Need some clarification for the osm2pgsql multi-backend documentation.](/questions/51843/need-some-clarification-for-the-osm2pgsql-multi-backend-documentation)

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
<span id="post-51843-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51843-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51843-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I was reading the osm2pgsql documentation on github for info on loading a custom lua script but I am confused on some of the instructions.</p>
<p>In the file <a href="https://github.com/openstreetmap/osm2pgsql/blob/master/docs/lua.md">osm2pgsql/docs/lua.md</a>, under the "How To" section, it gives as an example:</p>
<p>osm2pgsql -S your.style --tag-transform-script your.lua --hstore-all extract.osm.pbf</p>
<p>These five questions pertain to the example above:</p>
<ol>
<li>Is the multi-backend used to create postgres tables directly or is it more for filtering out unwanted metadata from osm when importing a pbf?</li>
<li>What are the different file formats that can be passed to the "-S" option? .style? .json? others?</li>
<li>When loading in custom styles, is the option "--hstore-all" required? Can we use one of the other hstore options instead?</li>
<li>If we already have a database loaded, will osm2pgsql build the newly styled tables by reading from the database or does it always read from pbf file.</li>
<li>Using --append, and assuming the new table names in the style file are different from what already exists in the database, does osm2pgsql just create the new tables alongside the preexisting ones?</li>
</ol>
<p>The last question is in regards to header in the <a href="https://github.com/openstreetmap/osm2pgsql/blob/master/multi.style.json">osm2pgsql/multi.style.json</a> file:</p>
<p><code>-- This is an example Lua transform for a multi style -- It is not intended for use directly with --tag-transform-script but -- for use from multi.style.json</code></p>
<p>What is meant by "not intended for"? Is it because the format of the style is json?</p>
<p>Thanks,</p>
<p>Will</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Aug '16, 15:25</strong></p>
<img src="https://secure.gravatar.com/avatar/487645f035e9b2f095acf7510b32ce89?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="placebo10&#39;s gravatar image" />
<p><span>placebo10</span><br />
<span class="score" title="71 reputation points">71</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="placebo10 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Aug '16, 15:32</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-51843" class="comments-container">
&#10;</div>
<div id="comment-tools-51843" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51843-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

