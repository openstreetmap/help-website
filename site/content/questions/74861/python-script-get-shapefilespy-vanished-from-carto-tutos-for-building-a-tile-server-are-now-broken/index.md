+++
type = "question"
title = "Python script get-shapefiles.py vanished from carto, tutos for building a tile server are now broken."
description = '''Hello. I followed several times the step-by-step building tuto of a tile server, perfect. From mid-april, there is something that went wrong: the &quot;get-shapefiles.py&quot; vanished from the carto repository, hence was not anymore copied locally with carto stuff. Therefore the tuto died there, and if I tri...'''
date = "2020-05-17T21:55:00Z"
lastmod = "2020-05-17T23:43:00Z"
weight = 74861
keywords = [ "carto", "get-shapefiles.py", "switch2osm.org" ]
aliases = [ "/questions/74861" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Python script get-shapefiles.py vanished from carto, tutos for building a tile server are now broken.](/questions/74861/python-script-get-shapefilespy-vanished-from-carto-tutos-for-building-a-tile-server-are-now-broken)

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
<span id="post-74861-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74861-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74861-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello.</p>
<p>I followed several times the step-by-step building tuto of a tile server, perfect.</p>
<p>From mid-april, there is something that went wrong: the "get-shapefiles.py" vanished from the carto repository, hence was not anymore copied locally with carto stuff.</p>
<p>Therefore the tuto died there, and if I tried to bypass, nothing else worked afterwards in the tuto with tons of fatal errors.</p>
<p>Is there something to do ? I need to rebuild my tile server, 18.04LTS or 20.04LTS.</p>
<p>Regards.</p>
<p>EDIT: the tutos are on "switch2osm.org" of course :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-carto" rel="tag" title="see questions tagged &#39;carto&#39;">carto</span> <span class="post-tag tag-link-get-shapefiles.py" rel="tag" title="see questions tagged &#39;get-shapefiles.py&#39;">get-shapefiles.py</span> <span class="post-tag tag-link-switch2osm.org" rel="tag" title="see questions tagged &#39;switch2osm.org&#39;">switch2osm.org</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 May '20, 21:55</strong></p>
<img src="https://secure.gravatar.com/avatar/31e056a24dfc6a816acc70efb2bcb5ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Second%20Couteau&#39;s gravatar image" />
<p><span>Second Couteau</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Second Couteau has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 May '20, 22:00</strong> </span></p>
</div>
</div>
<div id="comments-container-74861" class="comments-container">
&#10;</div>
<div id="comment-tools-74861" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74861-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="74862"></span>

<div id="answer-container-74862" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74862-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74862-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74862-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Looks like it changed on <a href="https://github.com/gravitystorm/openstreetmap-carto/commit/67824003e02b27574de9b6f49313043248d5bcff#diff-7d442b7eb49f5fc377f51e74b291cfc1">26th March</a>:</p>
<p>Instead of</p>
<pre><code>scripts/get-shapefiles.py</code></pre>
<p>do</p>
<pre><code>scripts/get-external-data.py</code></pre>
<p>If that works, pull requests at <a href="https://github.com/switch2osm/switch2osm.github.io">https://github.com/switch2osm/switch2osm.github.io</a> welcome!</p>
<p>The instructions still worked for me on <a href="https://www.openstreetmap.org/user/SomeoneElse/diary/392942">4th May</a> - presumably there's been a release since then.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 May '20, 22:07</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-74862" class="comments-container">
<span id="74864"></span>
<div id="comment-74864" class="comment">
<div id="post-74864-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>EDIT:</p>
<p>Tried to install psycopg2:</p>
<p>apt-get install python-psycopg2</p>
<p>... ... ...</p>
<p>I then test this installed module:</p>
<p>username@osm-tileserver-01:~/src/openstreetmap-carto$ python Python 2.7.17 (default, Apr 15 2020, 17:20:14) [GCC 7.5.0] on linux2 Type "help", "copyright", "credits" or "license" for more information.</p>
<blockquote>
<blockquote>
<blockquote>
<p>import psycopg2</p>
<p>quit()</p>
</blockquote>
</blockquote>
</blockquote>
<p>Seems to be there.</p>
<p>Then I launch the faulty script:</p>
<p>username@osm-tileserver-01:~/src/openstreetmap-carto$ scripts/get-external-data.py Traceback (most recent call last): File "scripts/get-external-data.py", line 29, in &lt;module&gt; import psycopg2 ModuleNotFoundError: No module named 'psycopg2'</p>
<p>username@osm-tileserver-01:~/src/openstreetmap-carto$</p>
<p>Definitely BROKEN :(</p>
<p>Regards.</p>
</div>
<div id="comment-74864-info" class="comment-info">
<span class="comment-age">(17 May '20, 23:11)</span> <span class="comment-user userinfo">Second Couteau</span>
</div>
</div>
</div>
<div id="comment-tools-74862" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74862-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="74863"></span>

<div id="answer-container-74863" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74863-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74863-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74863-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hello.</p>
<p>It does not work (translated from french system messages):</p>
<p>username@osm-tileserver-01:~/src/openstreetmap-carto$ scripts/get-shapefiles.py bash: scripts/get-shapefiles.py: no file or directory of this type</p>
<p>username@osm-tileserver-01:~/src/openstreetmap-carto$ scripts/get-external-data.py Traceback (most recent call last): File "scripts/get-external-data.py", line 29, in &lt;module&gt; import psycopg2 ModuleNotFoundError: No module named 'psycopg2'</p>
<p>username@osm-tileserver-01:~/src/openstreetmap-carto$</p>
<p>So the old script is not there, and the new one requires ..."something".</p>
<p>Tuto is still broken.</p>
<p>Regards.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 May '20, 22:56</strong></p>
<img src="https://secure.gravatar.com/avatar/31e056a24dfc6a816acc70efb2bcb5ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Second%20Couteau&#39;s gravatar image" />
<p><span>Second Couteau</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Second Couteau has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 May '20, 22:57</strong> </span></p>
</div>
</div>
<div id="comments-container-74863" class="comments-container">
<span id="74865"></span>
<div id="comment-74865" class="comment">
<div id="post-74865-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>EDIT, seems to work !</p>
<p>0) install python3-psycop2</p>
<p>1) install python3-pip</p>
<p>2) pip3 install psycopg2</p>
<p>3) ./scripts/get-external-data.py</p>
</div>
<div id="comment-74865-info" class="comment-info">
<span class="comment-age">(17 May '20, 23:43)</span> <span class="comment-user userinfo">Second Couteau</span>
</div>
</div>
</div>
<div id="comment-tools-74863" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74863-form-container" class="comment-form-container">
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

